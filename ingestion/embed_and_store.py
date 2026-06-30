import os
import json
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load env variables
load_dotenv()

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHUNKS_PATH = os.path.join(WORKSPACE_DIR, "data", "chunks.json")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-large")

# Collection Name
COLLECTION_NAME = "sewa_setu_services"

def main():
    print("=== Embedding & Storing Chunks in ChromaDB ===")
    
    if not os.path.exists(CHUNKS_PATH):
        print(f"[Embed] Error: Chunks file not found at {CHUNKS_PATH}. Run chunker first.")
        return

    # Load generated chunks
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)
        
    print(f"[Embed] Loaded {len(chunks)} chunks from {CHUNKS_PATH}")
    
    if not chunks:
        print("[Embed] Warning: No chunks found to embed!")
        return

    # Initialize ChromaDB persistent client
    print(f"[Embed] Connecting to ChromaDB at: {CHROMA_DB_PATH}")
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    
    # Re-create collection to avoid stale data duplicates on re-runs
    try:
        client.delete_collection(COLLECTION_NAME)
        print(f"  Deleted old collection '{COLLECTION_NAME}'")
    except Exception:
        pass
        
    collection = client.create_collection(COLLECTION_NAME)
    print(f"  Created collection '{COLLECTION_NAME}'")
    
    # Load SentenceTransformer model
    print(f"[Embed] Loading model: {EMBEDDING_MODEL}...")
    model = SentenceTransformer(EMBEDDING_MODEL)
    print("  Model loaded successfully.")

    # Embed and upload in batches of 32
    batch_size = 32
    total_chunks = len(chunks)
    
    print(f"[Embed] Generating embeddings and uploading in batches of {batch_size}...")
    
    for i in range(0, total_chunks, batch_size):
        batch = chunks[i : i + batch_size]
        print(f"  Processing batch {i // batch_size + 1} / {int((total_chunks - 1) / batch_size) + 1}...")
        
        # Prepare inputs with "passage: " prefix for E5 convention
        texts_to_embed = [f"passage: {c['text']}" for c in batch]
        
        # Generate embeddings
        embeddings = model.encode(texts_to_embed, show_progress_bar=False).tolist()
        
        # Prepare lists for Chroma DB
        ids = [c["chunk_id"] for c in batch]
        metadatas = []
        documents = []
        
        for c in batch:
            # Only store basic metadata fields that are scalar types (strings, ints)
            meta = {
                "service_id": int(c["service_id"]),
                "service_name": c["service_name"],
                "lang": c["lang"],
                "section": c["section"],
                "doc_type": c["doc_type"],
                "source_url": c["source_url"],
                "chunk_index": int(c["chunk_index"]),
                "total_chunks": int(c["total_chunks"])
            }
            metadatas.append(meta)
            documents.append(c["text"])
            
        # Add to Chroma collection
        collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents
        )
        
    print("\n[Embed] Database records uploaded successfully.")
    
    # Generate summary statistics
    # Stats maps: service_id -> count, lang -> count, doc_type -> count
    stats_service = {}
    stats_lang = {"en": 0, "hi": 0}
    stats_doc = {"web": 0, "pdf": 0}
    
    for c in chunks:
        sid = str(c["service_id"])
        stats_service[sid] = stats_service.get(sid, 0) + 1
        
        lang = c["lang"]
        stats_lang[lang] = stats_lang.get(lang, 0) + 1
        
        dtype = c["doc_type"]
        stats_doc[dtype] = stats_doc.get(dtype, 0) + 1
        
    print("\n" + "=" * 50)
    print("INGESTION SUMMARY STATISTICS")
    print("=" * 50)
    print("Chunks per Service:")
    for sid, count in sorted(stats_service.items()):
        print(f"  Service ID {sid}: {count} chunks")
    print("\nChunks per Language:")
    for lang, count in stats_lang.items():
        print(f"  {lang.upper()}: {count} chunks")
    print("\nChunks per Source Type:")
    for dtype, count in stats_doc.items():
        print(f"  {dtype.upper()}: {count} chunks")
    print("=" * 50)

if __name__ == "__main__":
    main()
