import os
import shutil

root = r"c:\Users\hp\Desktop\sewa setu copies\SewaSetuRag - Copy (2)"

# Define folder mappings
dirs_to_create = [
    os.path.join(root, "01_preprocessing"),
    os.path.join(root, "02_optimization"),
    os.path.join(root, "03_chunking"),
    os.path.join(root, "04_embeddings_and_kg"),
    os.path.join(root, "05_webui"),
    os.path.join(root, "05_webui", "backend"),
    os.path.join(root, "05_webui", "frontend"),
    os.path.join(root, "docs"),
]

for d in dirs_to_create:
    os.makedirs(d, exist_ok=True)
    print(f"Created/Verified directory: {d}")

# Movement specifications: (source, destination)
moves = [
    # ingestion/ocr_pdfs.py -> 01_preprocessing/ocr_pdfs.py
    (os.path.join(root, "ingestion", "ocr_pdfs.py"), os.path.join(root, "01_preprocessing", "ocr_pdfs.py")),
    # pdf_data -> 01_preprocessing/pdf_data
    (os.path.join(root, "pdf_data"), os.path.join(root, "01_preprocessing", "pdf_data")),
    # ingestion/chunker.py -> 03_chunking/chunker.py
    (os.path.join(root, "ingestion", "chunker.py"), os.path.join(root, "03_chunking", "chunker.py")),
    # ingestion/scraper -> 03_chunking/scraper
    (os.path.join(root, "ingestion", "scraper"), os.path.join(root, "03_chunking", "scraper")),
    # ingestion/embed_and_store.py -> 04_embeddings_and_kg/embed_and_store.py
    (os.path.join(root, "ingestion", "embed_and_store.py"), os.path.join(root, "04_embeddings_and_kg", "embed_and_store.py")),
    # chroma_db -> 04_embeddings_and_kg/chroma_db
    (os.path.join(root, "chroma_db"), os.path.join(root, "04_embeddings_and_kg", "chroma_db")),
    # data -> 04_embeddings_and_kg/data
    (os.path.join(root, "data"), os.path.join(root, "04_embeddings_and_kg", "data")),
    # backend files -> 05_webui/backend/
    (os.path.join(root, "backend", "main.py"), os.path.join(root, "05_webui", "backend", "main.py")),
    (os.path.join(root, "backend", "rag.py"), os.path.join(root, "05_webui", "backend", "rag.py")),
    (os.path.join(root, "backend", "llm_router.py"), os.path.join(root, "05_webui", "backend", "llm_router.py")),
    # Markdown documentation -> docs/
    (os.path.join(root, "PROJECT_DOCUMENTATION.md"), os.path.join(root, "docs", "PROJECT_DOCUMENTATION.md")),
    (os.path.join(root, "answerRetrieval.md"), os.path.join(root, "docs", "answerRetrieval.md")),
    (os.path.join(root, "api.md"), os.path.join(root, "docs", "api.md")),
    (os.path.join(root, "history.md"), os.path.join(root, "docs", "history.md")),
    (os.path.join(root, "two_stage_routing_progress.md"), os.path.join(root, "docs", "two_stage_routing_progress.md")),
    (os.path.join(root, "rag_pipeline_architecture.md"), os.path.join(root, "docs", "rag_pipeline_architecture.md")),
]

# Perform file/directory moves
for src, dest in moves:
    if os.path.exists(src):
        # Handle directory overwrite/move logic
        if os.path.isdir(src) and os.path.exists(dest):
            print(f"Destination directory already exists. Deleting it to refresh: {dest}")
            shutil.rmtree(dest)
        
        shutil.move(src, dest)
        print(f"Moved: {src} -> {dest}")
    else:
        print(f"Source not found (skipping): {src}")

# Move all frontend folder contents to 05_webui/frontend
frontend_src = os.path.join(root, "frontend")
frontend_dest = os.path.join(root, "05_webui", "frontend")

if os.path.exists(frontend_src):
    for item in os.listdir(frontend_src):
        s_item = os.path.join(frontend_src, item)
        d_item = os.path.join(frontend_dest, item)
        # Skip node_modules or dist to save time/space if desired, but instruction is "do NOT delete any files".
        # We should move everything.
        if os.path.exists(d_item):
            if os.path.isdir(d_item):
                shutil.rmtree(d_item)
            else:
                os.remove(d_item)
        shutil.move(s_item, d_item)
        print(f"Moved frontend asset: {s_item} -> {d_item}")

# Clean up empty original source directories
for d in ["ingestion", "backend", "frontend"]:
    path = os.path.join(root, d)
    if os.path.exists(path) and not os.listdir(path):
        os.rmdir(path)
        print(f"Removed empty directory: {path}")
