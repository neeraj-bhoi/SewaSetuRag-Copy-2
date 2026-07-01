# SewaSetu RAG Chatbot: Full Technical & Product Documentation

This document provides a highly detailed, end-to-end technical overview and architectural guide for the **SewaSetu RAG Chatbot**. This system is specifically designed to act as an AI Sahayak (Assistant) for the **SewaSetu Chhattisgarh Portal**, answering citizen queries regarding public services in **English, Hindi, and Hinglish**, with intelligent document pinning, hybrid reranking, and state-machine-driven location routing.

---

## Table of Contents
1. [Product Overview & Domain Scope](#1-product-overview--domain-scope)
2. [Key Product Features](#2-key-product-features)
3. [Architecture & Message Lifecycle](#3-architecture--message-lifecycle)
4. [Backend Directory & Component Deep Dive](#4-backend-directory--component-deep-dive)
5. [Frontend React Interface & State Machine](#5-frontend-react-interface--state-machine)
6. [Ingestion Pipeline & Vector Database](#6-ingestion-pipeline--vector-database)
7. [Automated Testing & Verification](#7-automated-testing--verification)
8. [Setup & Deployment Guide](#8-setup--deployment-guide)

---

## 1. Product Overview & Domain Scope

The SewaSetu Chhattisgarh Portal provides various government-to-citizen (G2C) services. However, citizens often struggle to understand required documents, service timelines (SLA), fees, and the correct office locations to apply. 

The SewaSetu RAG Chatbot solves this by processing natural language queries and returning factually grounded answers. It is scoped to **5 primary services**:
1. **Marriage Registration & Certificate** (Service ID: `3`, sno: `1`)
2. **SC/ST Caste Certificate** (Service ID: `4`, sno: `2`)
3. **OBC Caste Certificate** (Service ID: `5`, sno: `3`)
4. **Domicile Certificate** (Service ID: `7`, sno: `4`)
5. **Ordinary Gazette Notification for Name Change** (Service ID: `201`, sno: `5`)

---

## 2. Key Product Features

### A. Multilingual Query Translation & Normalization
* **Language Classification:** The system detects if the query is in English, Hindi, or Hinglish using the Sarvam AI LLM.
* **Dual-Query Translation:** English queries are translated to Hindi, and Hindi/Hinglish queries are translated to English, allowing the retriever to fetch context from both English and Hindi knowledge stores in parallel.
* **Term Normalization:** A regex-based normalization layer resolves dialect and colloquial synonyms (e.g., mapping `"niwas praman patra"`, `"residence certificate"`, and `"स्थानीय निवास प्रमाण पत्र"` to Domicile Certificate).

### B. Hybrid Retrieval & Pinning
* **Semantic Embeddings:** Uses the `intfloat/multilingual-e5-large` model to encode chunks and queries.
* **Lexical Scoring:** Computes BM25/TF-IDF lexical matches on raw text.
* **Composite Score:** Reranks candidate chunks using:
  $$\text{Score} = 0.7 \times \text{Semantic Similarity} + 0.3 \times \text{Lexical Overlap}$$
* **Manual Portal Boost (+0.1):** Dynamically applies a `+0.1` boost to all `combined_manual` portal specification chunks. This prioritizes portal rules over raw legal notification texts (such as gazettes and rulebooks) which may be outdated or lack implementation checklists.
* **Checklist Pinning:** If a query contains document, fee, or timeline keywords, the backend isolates the service's `REQUIRED DOCUMENTS` table chunk and pins it to **Rank 1** of the context.




### D. Strict Factual Grounding (Checklist Validation)
* The system enforces strict rules on document status:
  - Documents marked as `(Mandatory: Yes)` or `(Mandatory: हाँ)` are flagged as mandatory.
  - Documents marked as `(Mandatory: No)` or `(Mandatory: नहीं)` are explicitly identified as optional.
  - The LLM is strictly forbidden from inferring document status from User Manual instructions or general notification paragraphs.

### E. Eligibility Criteria Awareness
* The system prompts instruct the LLM to read **ALL** eligibility criteria, rules, and exceptions from the retrieved context before answering eligibility questions.
* **Domicile Logic Rules:** The system strictly parses Domicile eligibility logic as `(Criteria One AND Criteria Two) OR (Criteria Three)`. It enforces this logical distinction at both prompt and synthesis stages so that the bot does not incorrectly declare that all criteria groups must be satisfied.
* Special attention is given to alternative criteria, exceptions, and special cases (e.g., criteria for spouses of government employees, property holders, All India Services cadre allottees).
* The LLM is forbidden from assuming ineligibility if **any** criterion in the context could apply to the citizen's situation.

### F. Contextual Grounding & RAG Context Injection
* Retrieved chunks from ChromaDB are directly embedded into the LLM system prompts for both intermediate (English/Hindi) answer generation.
* This ensures the LLM generates answers grounded in actual database content rather than relying on its parametric knowledge, preventing hallucinated document lists or incorrect eligibility determinations.

### G. Conciseness Enforcement
* The LLM is instructed to answer **ONLY** what the citizen asked, without volunteering unrelated information.
* Eligibility questions receive only eligibility answers (no document dumps, fees, or process steps).
* Document questions receive only document answers (no eligibility or process information).

### H. Polite Tone Enforcement
* All system prompts require warm, respectful, and citizen-friendly language.
* The LLM is forbidden from using harsh, dismissive, blunt, or discouraging phrasing.
* Even when a citizen may not be eligible, the system guides them gently and highlights any alternative paths or exceptions.

### I. Consensus Response Synthesis
* Calls the Sarvam LLM in parallel to generate:
  - An intermediate English response from the English context.
  - An intermediate Hindi response from the Hindi context.
* A final consensus synthesis prompt combines both intermediate answers, resolves conflicts by prioritizing the most informative facts, and outputs a single, cohesive response in the target query language.
* Markdown URLs are sanitized, and a single, official Sewa Setu application button is appended to the message.

### J. Hinglish Script Enforcement
* For Hinglish (Hindi in Roman script) responses, the system applies a multi-layer enforcement:
  - **Prompt-level:** Strong instructions with explicit examples of forbidden Devanagari characters and required Roman transliterations.
  - **Post-processing safety net:** After synthesis, a regex check detects any Devanagari character leakage (`[\u0900-\u097f]`). If detected, a second LLM call automatically transliterates the response to Roman script while preserving meaning and structure.

---

## 3. Architecture & Message Lifecycle

The following Mermaid diagram illustrates the lifecycle of a query sent to the `/api/chat` endpoint:

```mermaid
sequenceDiagram
    autonumber
    actor User as Citizen (Client UI)
    participant API as FastAPI Backend (main.py)
    participant LLM as Sarvam AI (llm_router.py)
    participant DB as ChromaDB Vector Store (rag.py)

    User->>API: POST /api/chat {query, selected_sno, ...}
    
    rect rgb(240, 248, 255)
        Note over API: Query Normalization & Language Detection
        API->>LLM: Detect Language (en, hi, hinglish)
        LLM-->>API: Returns detected language
    end

    Note over API: Run Standard RAG Pipeline
    API->>DB: Query contexts (En/Hi)
    DB-->>API: Return retrieved chunks
    API->>LLM: Generate intermediate En/Hi responses & Synthesize final
    LLM-->>API: Returns final synthesized response
    API-->>User: Return response
```

---

## 4. Backend Directory & Component Deep Dive

The backend is built with Python 3.10+ and FastAPI. It consists of the following core modules:

### A. `backend/main.py`
Acts as the root API router, configuring middleware (CORS) and defining Pydantic schemas and endpoints:
* **Pydantic Schemas:**
  - `Message`: Represents roles (`user`, `assistant`, `system`) and content.
  - `ChatRequest`: Standardizes incoming payload structures (supporting `selected_sno`, `messages`, `detailed`).
* **Endpoints:**
  - `GET /api/services`: Returns services manifest metadata.
  - `GET /api/services/{sno}`: Pulls structured metadata profile (fees, SLA, documents list, form fields) from `data/profiles/`.
  - `POST /api/search`: Fast rule-based/semantic catalog classification matching queries to an `sno`.
  - `POST /api/chat`: Standard RAG chatbot handler.
  - `GET /health`: Returns server status.
* **Unified RAG Pipeline:**
  - `run_rag_pipeline(query, request, service_id)`: Drives context retrieval, thread-based parallel completions generation, synthesis rules, regex URL strip rules, and portal apply link injections.

### B. `backend/llm_router.py`
Manages connections and post-processing for the Sarvam AI endpoints:
* `_post_with_retry(url, headers, json_payload)`: Implements exponential backoff retries to handle transient 5xx errors or network socket timeouts.
* `ThinkStripper`: A buffered stream parser that removes `<think> ... </think>` thinking blocks from DeepSeek-based or reasoning-enabled models.
* `detect_query_language(query: str)`: Detects English, Hindi, or Hinglish. Inspects Devanagari unicode characters (`\u0900` to `\u097F`) for fast-path Hindi detection.
* `translate_query_to_english` / `translate_query_to_hindi`: Handles bidirectionally translating query inputs using the LLM.
* **Spelling robustification:** Expanded rule-based keyword mapping for Domicile (`dimicile`, `domisile`, `domocile`) and Marriage (`shaadi`) to resolve classifications correctly on user typos.
* **Strict threshold check:** If the query has no in-scope keywords (e.g. `"koi aur criteria..."`), the semantic database fallback threshold is restricted to `0.33` (instead of `0.45`). If it fails this strict check, LLM classification is bypassed completely. This prevents generic questions from triggering incorrect active service auto-switching.

### C. `backend/rag.py`
Drives database connections and reranking operations:
* `retrieve_context(query, service_id, top_k, english_query, hindi_query, lang)`: Configures checklist keyword match triggers. Performs metadata-filtered ChromaDB vector queries. Evaluates lexical matches. Computes composite scores, applies manual portal manual boosts (`+0.1`), reranks candidates, and returns a formatted context string.

---

## 5. Frontend React Interface & State Machine

The frontend is a single-page React application compiled via Vite. 

### A. Core State Management (`App.jsx`)
Coordinates the chat lifecycle and details drawer:
```javascript
const [chatMessages, setChatMessages] = useState([]);
const [inputText, setInputText] = useState('');
const [isChatLoading, setIsChatLoading] = useState(false);
```

---

## 6. Ingestion Pipeline & Vector Database

The ingestion pipeline populates the persistent vector database (`chroma_db/`) from raw documentation:

1. **OCR Extraction (`ingestion/ocr_pdfs.py`):** Uses EasyOCR to parse scanned PDF manuals (located in `data/pdf_data/`) into structured txt logs inside `data/ocr_output/`.
2. **Semantic Chunking (`ingestion/chunker.py`):** Splits the raw texts into overlapping chunks, identifying service tables, headers, and metadata rules.
3. **Embeddings Storage (`ingestion/embed_and_store.py`):** Encodes text chunks using `intfloat/multilingual-e5-large` and inserts them into ChromaDB with metadata filters (`service_id`, `lang`).

---

No standalone location test suites are needed as the location-specific routing flow has been removed. Standard RAG responses can be tested interactively.

---

## 8. Setup & Deployment Guide

### Configuration (`.env`)
Create a `.env` file at the root containing:
```env
SARVAM_API_KEY="your-sarvam-api-key"
SARVAM_MODEL="sarvam-30b"
SARVAM_API_URL="https://api.sarvam.ai/v1/chat/completions"
EMBEDDING_MODEL="intfloat/multilingual-e5-large"
CHROMA_DB_PATH="./chroma_db"
```

### Steps to Run
1. **Start Backend Server:**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
   ```
2. **Start Frontend Server:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
3. **Verify:** Open `http://localhost:5173` in your browser.
