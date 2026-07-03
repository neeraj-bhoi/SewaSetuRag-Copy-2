import os
import sys
import re
from typing import List, Dict, Any, Tuple, Optional
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb

# Ensure stdout uses UTF-8 to prevent Windows print crash
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# Configuration paths
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-large")
COLLECTION_NAME = "sewa_setu_services"

# Initialize models & client on import
print(f"[RAG] Loading embedding model: {EMBEDDING_MODEL_NAME}...")
embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)

print(f"[RAG] Connecting to ChromaDB at: {CHROMA_DB_PATH}")
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_collection(COLLECTION_NAME)
print(f"[RAG] Connected successfully to collection '{COLLECTION_NAME}' (Total count: {collection.count()})")


def tokenize_text(text: str) -> set:
    """
    Preserves both standard word characters and Devanagari script characters (including combining marks).
    """
    cleaned = re.sub(r'[^\w\u0900-\u097f\s]', ' ', text.lower())
    return set(cleaned.split())


def rerank_chunks(
    query: str, 
    chunks: List[Dict[str, Any]], 
    top_n: int = 4,
    english_query: Optional[str] = None,
    hindi_query: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Reranks the retrieved chunks using a hybrid semantic distance + lexical overlap score.
    Returns:
        The top_n reranked chunks.
    """
    stop_words = {
        'a', 'an', 'the', 'for', 'to', 'is', 'of', 'in', 'on', 'at', 'by', 'with', 'from', 'what', 'which', 'who', 'how', 'why', 'where', 'when',
        'के', 'लिए', 'है', 'का', 'की', 'में', 'को', 'और', 'से', 'पर', 'हो', 'कर', 'था', 'थी', 'थे', 'या', 'भी', 'ने', 'तक', 'जो', 'तो', 'ही'
    }

    # Pre-tokenize original/translated Hindi query keywords
    hi_query_to_use = hindi_query if hindi_query else query
    hi_words = tokenize_text(hi_query_to_use)
    hi_keywords = hi_words - stop_words
    if not hi_keywords:
        hi_keywords = hi_words

    # Pre-tokenize English query keywords
    en_query_to_use = english_query if english_query else query
    en_words = tokenize_text(en_query_to_use)
    en_keywords = en_words - stop_words
    if not en_keywords:
        en_keywords = en_words

    scored_chunks = []
    for chunk in chunks:
        # Convert distance to semantic similarity (smaller distance -> higher similarity)
        distance = chunk.get("distance", 1.0)
        semantic_sim = max(0.0, 1.0 - (distance / 2.0))

        # Lexical keyword overlap score based on chunk language
        chunk_lang = chunk["metadata"].get("lang", "en")
        chunk_words = tokenize_text(chunk["text"])

        if chunk_lang == "hi":
            # Match against original/translated Hindi query keywords
            overlap = len(hi_keywords.intersection(chunk_words))
            lexical_score = overlap / len(hi_keywords) if hi_keywords else 0.0
        else:
            # Match against English/translated query keywords
            overlap = len(en_keywords.intersection(chunk_words))
            lexical_score = overlap / len(en_keywords) if en_keywords else 0.0

        # Combine scores (semantic similarity weighted at 0.7, lexical overlap at 0.3)
        hybrid_score = 0.7 * semantic_sim + 0.3 * lexical_score
        
        # Give combined_manuals an edge/boost
        if chunk["metadata"].get("section") == "combined_manual":
            hybrid_score += 0.1

        chunk["hybrid_score"] = hybrid_score
        scored_chunks.append(chunk)

    # Sort chunks by hybrid score descending
    scored_chunks.sort(key=lambda x: x["hybrid_score"], reverse=True)
    
    if os.getenv("DEBUG_PRINT_CHUNKS", "true").lower() == "true":
        print(f"[RAG Reranking] Reranked {len(scored_chunks)} chunks:")
        for idx, chunk in enumerate(scored_chunks):
            meta = chunk["metadata"]
            print(f"  Rank {idx+1}: Service={meta.get('service_id')}, Section={meta.get('section')}, Lang={meta.get('lang')}, Distance={chunk.get('distance'):.4f}, HybridScore={chunk['hybrid_score']:.4f}")
    
    return scored_chunks[:top_n]


def retrieve_context(
    query: str, 
    service_id: Optional[int] = None, 
    top_k: int = 6,
    english_query: Optional[str] = None,
    hindi_query: Optional[str] = None,
    lang: str = "en",
    force_checklist: bool = False
) -> Tuple[str, List[Dict[str, Any]], Optional[str]]:
    """
    Retrieves top_k target-language chunks from ChromaDB, reranks them, 
    and returns a structured context string from the top 4 chunks.
    """
    # Increase retrieve size if no specific service filter is specified
    if service_id is None:
        top_k = max(top_k, 15)

    # Determine query to use based on target database language
    if lang == "hi" and hindi_query:
        search_query = hindi_query
    elif lang == "en" and english_query:
        search_query = english_query
    else:
        search_query = query

    query_text = f"query: {search_query}"
    query_vector = embedding_model.encode(query_text).tolist()

    # 1. Determine if this is a query about details available in the combined manual
    is_details_query = False
    if service_id:
        text_to_check = f"{query} {english_query or ''} {hindi_query or ''}".lower()
        details_keywords = [
            # Documents / Checklist
            "document", "proof", "card", "chalan", "challan", "affidavit", "certificate", 
            "dastavez", "dastawez", "dastavej", "dastawej", "shapath", "praman", "patra", 
            "upload", "submit", "need", "require", "mandatory", "optional", "checklist",
            "दस्तावेज", "दस्तावेज़", "प्रमाण", "पत्र", "शपथ", "चालान", "अनिवार्य", "वैकल्पिक",
            # Fees
            "fee", "fees", "charge", "charges", "cost", "payment", "rupees", "rs", "₹", 
            "शुल्क", "भुगतान", "पैसे", "रुपये", "रुपया",
            # SLA / Timeline
            "sla", "time limit", "days", "timeline", "duration", "days required", 
            "समय", "सीमा", "अवधि", "दिन",
            # Department
            "department", "dept", "ministry", "विभाग",
            # Form fields
            "field", "fields", "form field", "form fields", "application field", 
            "application fields", "form detail", "form details", "फ़ील्ड", "फील्ड", "कॉलम"
        ]
        is_details_query = any(k in text_to_check for k in details_keywords) or force_checklist

    where_clause = {"lang": lang}
    if service_id:
        where_clause = {
            "$and": [
                {"service_id": int(service_id)},
                {"lang": lang}
            ]
        }

    # 2. Check if we need to retrieve and pin the checklist chunk
    checklist_chunk = None
    if service_id and is_details_query:
        try:
            where_clause_c = {
                "$and": [
                    {"service_id": int(service_id)},
                    {"lang": lang}
                ]
            }
            # Query top 10 chunks specifically to find the checklist chunk
            query_text_c = "query: REQUIRED DOCUMENTS"
            query_vector_c = embedding_model.encode(query_text_c).tolist()
            results_c = collection.query(
                query_embeddings=[query_vector_c],
                n_results=10,
                where=where_clause_c
            )
            if results_c and "documents" in results_c and results_c["documents"]:
                docs_c = results_c["documents"][0]
                metas_c = results_c["metadatas"][0]
                distances_c = results_c["distances"][0]
                for idx_c, doc_c in enumerate(docs_c):
                    doc_c_upper = doc_c.upper()
                    if "REQUIRED DOCUMENTS" in doc_c_upper or "आवश्यक दस्तावेज़" in doc_c_upper or "आवश्यक दस्तावेज" in doc_c_upper:
                        checklist_chunk = {
                            "text": doc_c,
                            "metadata": metas_c[idx_c],
                            "distance": distances_c[idx_c]
                        }
                        print(f"[RAG] Successfully located and pinned checklist chunk for service_id={service_id}, lang={lang}")
                        break
        except Exception as e:
            print(f"[RAG] Failed to locate checklist chunk: {e}")

    # 2. Query for user query chunks
    print(f"[RAG] Querying database (service_id={service_id}, top_k={top_k}, lang={lang}, search_query='{search_query}')")
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        where=where_clause
    )

    top_chunks = []
    seen_texts = set()
    
    # Pre-add checklist chunk to seen_texts if it exists to avoid duplication
    if checklist_chunk:
        normalized_c = " ".join(checklist_chunk["text"].strip().split())
        seen_texts.add(normalized_c)

    if results and "documents" in results and results["documents"]:
        docs = results["documents"][0]
        metas = results["metadatas"][0]
        distances = results["distances"][0]
        for idx, (doc, meta) in enumerate(zip(docs, metas)):
            normalized = " ".join(doc.strip().split())
            if normalized in seen_texts:
                continue
            seen_texts.add(normalized)
            top_chunks.append({
                "text": doc, 
                "metadata": meta, 
                "distance": distances[idx]
            })

    # Rerank other chunks and combine with checklist chunk
    if checklist_chunk:
        top_other_chunks = rerank_chunks(query, top_chunks, top_n=3, english_query=english_query, hindi_query=hindi_query)
        top_4_chunks = [checklist_chunk] + top_other_chunks
    else:
        top_4_chunks = rerank_chunks(query, top_chunks, top_n=4, english_query=english_query, hindi_query=hindi_query)

    # If the top match has a very low hybrid score, the query is likely out-of-scope.
    # We bypass this check if we have pinned a checklist chunk since it is definitely in-scope.
    if not checklist_chunk and top_4_chunks and top_4_chunks[0].get("hybrid_score", 0.0) < 0.35:
        print(f"[RAG] Warning: Top hybrid score {top_4_chunks[0].get('hybrid_score', 0.0):.4f} is below threshold 0.35. Treating as out-of-scope.")
        return "", [], None

    # Build structured context string with labels
    context_parts = []
    metadata_list = []
    raw_checklist_text = None
    if checklist_chunk:
        raw_checklist_text = checklist_chunk["text"]

    for idx, chunk in enumerate(top_4_chunks):
        meta = chunk["metadata"]
        doc_type = meta.get("doc_type", "web")
        lang_label = "English" if meta.get("lang") == "en" else "Hindi"
        label = f"Official Specification ({lang_label})" if doc_type == "web" else f"User Manual ({lang_label})"
        
        # Clean EasyOCR character mistranslations
        cleaned_text = chunk['text']
        cleaned_text = re.sub(r'\b[Ll]०\b', '10', cleaned_text)
        cleaned_text = re.sub(r'\b[Ll]२\b', '12', cleaned_text)
        cleaned_text = cleaned_text.replace("L०", "10").replace("L२", "12").replace("l०", "10").replace("l२", "12")
        
        context_parts.append(
            f"--- Source {idx+1}: [{label}] ---\n"
            f"Service: {meta.get('service_name')} (ID: {meta.get('service_id')})\n"
            f"Section: {meta.get('section')}\n"
            f"Content:\n{cleaned_text}\n"
        )
        metadata_list.append(meta)

    context_string = "\n".join(context_parts)
    return context_string, metadata_list, raw_checklist_text
