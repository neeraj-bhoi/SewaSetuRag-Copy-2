import os
import re
import json
import uuid
import tiktoken
from dotenv import load_dotenv

# Load env variables
load_dotenv()

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRACTED_TEXT_DIR = os.path.join(WORKSPACE_DIR, "data", "extracted_text")
OCR_DIR = os.path.join(WORKSPACE_DIR, "data", "ocr_output")
CHUNKS_OUT_PATH = os.path.join(WORKSPACE_DIR, "data", "chunks.json")

# Initialize tiktoken encoder
ENCODER = tiktoken.get_encoding("cl100k_base")

def count_tokens(text):
    if not text:
        return 0
    return len(ENCODER.encode(text))

def chunk_prose(text, chunk_size=1500, overlap=200):
    """
    Chunks a text string into overlapping chunks using tiktoken counts.
    """
    tokens = ENCODER.encode(text)
    total_tokens = len(tokens)
    
    if total_tokens <= chunk_size:
        return [text]
        
    chunks = []
    start = 0
    while start < total_tokens:
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_text = ENCODER.decode(chunk_tokens)
        chunks.append(chunk_text.strip())
        
        # Advance the sliding window
        start += (chunk_size - overlap)
        if start >= total_tokens - overlap: # Avoid tiny tail chunks
            break
            
    return chunks

SERVICE_METADATA = {
    3: {
        "name_en": "Marriage Registration & Certificate",
        "name_hi": "विवाह पंजीकरण एवं प्रमाण पत्र",
        "dept_en": "Urban Administration and development Department",
        "dept_hi": "नगरीय प्रशासन एवं विकास विभाग",
        "url": "https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3"
    },
    4: {
        "name_en": "SC/ST Certificate",
        "name_hi": "अनुसूचित जाति/जनजाति प्रमाण पत्र",
        "dept_en": "Revenue and disaster management Department",
        "dept_hi": "राजस्व एवं आपदा प्रबंधन विभाग",
        "url": "https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4"
    },
    5: {
        "name_en": "OBC Certificate",
        "name_hi": "अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र",
        "dept_en": "Revenue and disaster management Department",
        "dept_hi": "राजस्व एवं आपदा प्रबंधन विभाग",
        "url": "https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5"
    },
    7: {
        "name_en": "Domicile Certificate",
        "name_hi": "मूल निवासी प्रमाण पत्र",
        "dept_en": "Revenue and disaster management Department",
        "dept_hi": "राजस्व एवं आपदा प्रबंधन विभाग",
        "url": "https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7"
    },
    201: {
        "name_en": "Ordinary Gazette Notification for Name Change",
        "name_hi": "नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना",
        "dept_en": "Government Printing and Stationery Department",
        "dept_hi": "शासकीय मुद्रण एवं लेखन सामग्री विभाग",
        "url": "https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201"
    }
}

OCR_MAPPING = {
    "Compulsory marriage rule.txt": [{"service_id": 3, "lang": "en"}],
    "Criteria for CG Domicile.txt": [{"service_id": 7, "lang": "en"}],
    "Social Status Rule 2013.txt": [{"service_id": 4, "lang": "hi"}, {"service_id": 5, "lang": "hi"}],
    "social status act.txt": [{"service_id": 4, "lang": "hi"}, {"service_id": 5, "lang": "hi"}],
    "the constitution (scheduled castes) order, 1950.txt": [{"service_id": 4, "lang": "en"}],
    "the constitution (scheduled tribes) order, 1950.txt": [{"service_id": 4, "lang": "en"}]
}

def process_manual_file(filepath, sid, lang):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    if not content:
        return []
        
    meta = SERVICE_METADATA[sid]
    service_name = meta["name_hi"] if lang == "hi" else meta["name_en"]
    dept = meta["dept_hi"] if lang == "hi" else meta["dept_en"]
    source_url = f"{meta['url']}&lang={lang}"
    
    text_chunks = chunk_prose(content, chunk_size=1500, overlap=200)
    
    chunks = []
    total_chunks = len(text_chunks)
    for idx, chunk_text in enumerate(text_chunks):
        chunk_id = str(uuid.uuid4())
        formatted_text = f"Service: {service_name}\nDepartment: {dept}\nCombined Manual Content: {chunk_text}"
        chunks.append({
            "chunk_id": chunk_id,
            "service_id": sid,
            "service_name": service_name,
            "lang": lang,
            "section": "combined_manual",
            "doc_type": "web",
            "source_url": source_url,
            "chunk_index": idx + 1,
            "total_chunks": total_chunks,
            "text": formatted_text
        })
    return chunks

def process_ocr_file(filename, filepath):
    if filename not in OCR_MAPPING:
        print(f"  [Warning] OCR file {filename} not mapped to any service. Skipping.")
        return []
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read().strip()
        
    if not content:
        return []
        
    mappings = OCR_MAPPING[filename]
    chunks = []
    
    for mapping in mappings:
        sid = mapping["service_id"]
        lang = mapping["lang"]
        
        meta = SERVICE_METADATA[sid]
        service_name = meta["name_hi"] if lang == "hi" else meta["name_en"]
        dept = meta["dept_hi"] if lang == "hi" else meta["dept_en"]
        source_url = f"{meta['url']}&lang={lang}"
        
        text_chunks = chunk_prose(content, chunk_size=1500, overlap=200)
        total_chunks = len(text_chunks)
        
        for idx, chunk_text in enumerate(text_chunks):
            chunk_id = str(uuid.uuid4())
            formatted_text = f"Service: {service_name}\nDepartment: {dept}\nOfficial Document Content: {chunk_text}"
            chunks.append({
                "chunk_id": chunk_id,
                "service_id": sid,
                "service_name": service_name,
                "lang": lang,
                "section": "official_document",
                "doc_type": "pdf",
                "source_url": source_url,
                "chunk_index": idx + 1,
                "total_chunks": total_chunks,
                "text": formatted_text
            })
            
    return chunks

def main():
    print("=== Chunking Unified Ingested Data (Manuals & OCR Texts) ===")
    
    all_chunks = []
    
    # 1. Process Combined Manuals
    if os.path.exists(EXTRACTED_TEXT_DIR):
        print(f"[Chunker] Reading combined manuals from: {EXTRACTED_TEXT_DIR}")
        for sid in SERVICE_METADATA.keys():
            for lang in ["en", "hi"]:
                filename = f"combined_manual_{sid}_{lang}.txt"
                filepath = os.path.join(EXTRACTED_TEXT_DIR, filename)
                if os.path.exists(filepath):
                    try:
                        chunks = process_manual_file(filepath, sid, lang)
                        all_chunks.extend(chunks)
                        print(f"  Processed {filename}: generated {len(chunks)} chunks.")
                    except Exception as e:
                        print(f"  [Error] Failed to chunk manual {filename}: {e}")
                else:
                    print(f"  [Warning] Manual file {filename} not found.")
                    
    # 2. Process OCR files
    if os.path.exists(OCR_DIR):
        print(f"[Chunker] Reading OCR files from: {OCR_DIR}")
        for filename in sorted(os.listdir(OCR_DIR)):
            if filename.endswith(".txt"):
                filepath = os.path.join(OCR_DIR, filename)
                try:
                    chunks = process_ocr_file(filename, filepath)
                    all_chunks.extend(chunks)
                    print(f"  Processed OCR file {filename}: generated {len(chunks)} chunks.")
                except Exception as e:
                    print(f"  [Error] Failed to chunk OCR file {filename}: {e}")
                    
    # Write all chunks to chunks.json
    os.makedirs(os.path.dirname(CHUNKS_OUT_PATH), exist_ok=True)
    with open(CHUNKS_OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
        
    print(f"\n[Chunker] Completed! Total chunks generated: {len(all_chunks)}")
    print(f"[Chunker] Saved compiled chunks to: {CHUNKS_OUT_PATH}")

if __name__ == "__main__":
    main()
