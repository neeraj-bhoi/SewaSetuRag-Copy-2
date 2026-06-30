import os
import sys

# Configure stdout to use UTF-8 to prevent unicode print crashes on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

import re
import json
import time
import unicodedata
from datetime import datetime, timezone
import pytesseract
import easyocr
from pdf2image import convert_from_path
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Setup pytesseract binary path on Windows
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TESSERACT_CMD):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
    print(f"[OCR] Configured pytesseract path to: {TESSERACT_CMD}")
else:
    print("[OCR] Warning: Tesseract executable not found at default location. Make sure it is in PATH.")

POPPLER_PATH = os.getenv("POPPLER_PATH", r"C:\Release-26.02.0-0\poppler-26.02.0\Library\bin")
print(f"[OCR] Using Poppler path: {POPPLER_PATH}")

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DATA_DIR = os.path.join(WORKSPACE_DIR, "pdf_data")
OCR_OUT_DIR = os.path.join(WORKSPACE_DIR, "data", "ocr_output")

# Map of PDF file names to their corresponding services, language, and service names
PDF_MAPPING = {
    "Compulsory marriage rule.pdf": {
        "service_ids": [3],
        "service_name": "Marriage Certificate",
        "lang": "en",
        "source_url": "pdf_data/Compulsory marriage rule.pdf"
    },
    "Criteria for CG Domicile.pdf": {
        "service_ids": [7],
        "service_name": "Domicile Certificate",
        "lang": "en",
        "source_url": "pdf_data/Criteria for CG Domicile.pdf"
    },
    "Social Status Rule 2013.pdf": {
        "service_ids": [4, 5],
        "service_name": "Caste Certificate (SC/ST/OBC)",
        "lang": "hi",
        "source_url": "pdf_data/Social Status Rule 2013.pdf"
    },
    "social status act.pdf": {
        "service_ids": [4, 5],
        "service_name": "Caste Certificate (SC/ST/OBC)",
        "lang": "hi",
        "source_url": "pdf_data/social status act.pdf"
    },
    "the constitution (scheduled castes) order, 1950.pdf": {
        "service_ids": [4],
        "service_name": "SC/ST Certificate",
        "lang": "en",
        "source_url": "pdf_data/the constitution (scheduled castes) order, 1950.pdf"
    },
    "the constitution (scheduled tribes) order, 1950.pdf": {
        "service_ids": [4],
        "service_name": "SC/ST Certificate",
        "lang": "en",
        "source_url": "pdf_data/the constitution (scheduled tribes) order, 1950.pdf"
    }
}

# EasyOCR Reader Instance (initialized lazily)
_easyocr_reader = None

def get_easyocr_reader():
    global _easyocr_reader
    if _easyocr_reader is None:
        print("[OCR] Initializing EasyOCR Reader (Hindi + English)...")
        _easyocr_reader = easyocr.Reader(['hi', 'en'], gpu=False)
    return _easyocr_reader

def setup_directories():
    os.makedirs(OCR_OUT_DIR, exist_ok=True)
    # Delete all files in OCR_OUT_DIR to start fresh
    for filename in os.listdir(OCR_OUT_DIR):
        file_path = os.path.join(OCR_OUT_DIR, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"[OCR] Deleted old file: {filename}")
        except Exception as e:
            print(f"[OCR] Failed to delete {filename}: {e}")
            
    # Also create data/pdfs/ to store copies of PDFs if needed
    os.makedirs(os.path.join(WORKSPACE_DIR, "data", "pdfs"), exist_ok=True)
    print(f"[OCR] Output directory ready and cleared: {OCR_OUT_DIR}")

def post_process_text(text):
    if not text:
        return ""
    # Normalize unicode (NFC)
    text = unicodedata.normalize('NFC', text)
    # Strip double spaces and excess spacing
    text = re.sub(r'[ \t]+', ' ', text)
    # Fix common Tesseract Hindi ligature errors (e.g. replacing common broken chars)
    # We can replace any known common OCR patterns if needed:
    text = text.replace('|', '।') # Replace vertical bars with poorna viram
    # Keep lines clean
    lines = [line.strip() for line in text.split('\n')]
    cleaned_lines = [l for l in lines if l]
    return "\n".join(cleaned_lines)

def run_pytesseract_ocr(image):
    try:
        # Run OCR with detailed data to get confidence score
        data = pytesseract.image_to_data(image, lang='hin+eng', output_type=pytesseract.Output.DICT)
        
        # Calculate average confidence for non-empty tokens
        confidences = [int(c) for c in data['conf'] if c != '-1' and str(c).strip()]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
        
        # Run standard OCR to get the text
        text = pytesseract.image_to_string(image, lang='hin+eng')
        return text, avg_confidence
    except Exception as e:
        print(f"  [OCR] Pytesseract failed: {e}")
        return "", 0.0

def run_easyocr_ocr(image):
    try:
        reader = get_easyocr_reader()
        # Convert image to numpy array for easyocr
        import numpy as np
        img_np = np.array(image)
        results = reader.readtext(img_np, paragraph=True)
        text = "\n".join([r[1] for r in results])
        # EasyOCR doesn't give a simple page-level confidence score directly matching pytesseract,
        # but since we are using it as fallback, we return 100 as proxy.
        return text, 80.0
    except Exception as e:
        print(f"  [OCR] EasyOCR failed: {e}")
        return "", 0.0

def process_pdf(pdf_filename, mapping):
    pdf_path = os.path.join(PDF_DATA_DIR, pdf_filename)
    if not os.path.exists(pdf_path):
        print(f"[OCR] Error: PDF file not found at: {pdf_path}")
        return
        
    print(f"\n[OCR] Processing PDF: {pdf_filename}")
    
    # 1. Convert pages to images
    try:
        pages = convert_from_path(pdf_path, dpi=300, poppler_path=POPPLER_PATH)
        print(f"  Converted {len(pages)} pages using pdf2image.")
    except Exception as e:
        print(f"  [OCR] Failed to convert PDF {pdf_filename} to images: {e}")
        return

    # 2. Run OCR page by page
    full_text_pages = []
    for idx, page in enumerate(pages):
        print(f"  OCRing Page {idx+1}/{len(pages)} using EasyOCR...")
        
        # Run EasyOCR directly for complete extraction
        text, _ = run_easyocr_ocr(page)
            
        cleaned_text = post_process_text(text)
        full_text_pages.append(f"--- Page {idx+1} ---\n{cleaned_text}")

    full_extracted_text = "\n\n".join(full_text_pages)
    
    # 3. Create structured JSON outputs per service and language mapping
    for sid in mapping["service_ids"]:
        lang = mapping["lang"]
        
        sections = {
            "introduction": full_extracted_text,
            "required_documents": [],
            "fees": "",
            "processing_time": "",
            "eligibility": "",
            "steps": [],
            "department": ""
        }
        
        output_data = {
            "service_id": sid,
            "service_name": mapping["service_name"],
            "lang": lang,
            "sections": sections,
            "source_url": mapping["source_url"],
            "scraped_at": datetime.now(timezone.utc).isoformat()
        }
        
        # Make a safe filename for JSON output
        safe_name = pdf_filename.lower().replace(" ", "_").replace(".pdf", "")
        out_filename = f"ocr_pdf_{safe_name}_{sid}_{lang}.json"
        out_filepath = os.path.join(OCR_OUT_DIR, out_filename)
        
        with open(out_filepath, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
            
        print(f"  Saved OCR output JSON: {out_filename} ({len(full_extracted_text)} chars)")
        
        # Copy the PDF to data/pdfs/ as requested by prompt structure
        import shutil
        target_pdf_dir = os.path.join(WORKSPACE_DIR, "data", "pdfs")
        shutil.copy(pdf_path, os.path.join(target_pdf_dir, pdf_filename))

def main():
    print("=== Running PDF OCR Ingestion Pipeline ===")
    setup_directories()
    
    for filename, mapping in PDF_MAPPING.items():
        process_pdf(filename, mapping)
        
    print("\n[OCR] PDF Ingestion and OCR parsing completed successfully.")

if __name__ == "__main__":
    main()
