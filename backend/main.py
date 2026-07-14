import os
import sys
import json
import re
import requests
import asyncio
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional, Any
from dotenv import load_dotenv

try:
    from backend.rag import retrieve_context
    from backend.llm_router import (
        generate_answer, 
        classify_service, 
        detect_query_language, 
        translate_query_to_english,
        translate_query_to_hindi,
        classify_query_intent,
        llm_trace
    )
except ImportError:
    from rag import retrieve_context
    from llm_router import (
        generate_answer, 
        classify_service, 
        detect_query_language, 
        translate_query_to_english,
        translate_query_to_hindi,
        classify_query_intent,
        llm_trace
    )


# Ensure stdout uses UTF-8 to prevent Windows-specific print emoji/char crashes
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# App paths
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(WORKSPACE_DIR, "data", "rag_kb_manifest.json")

# 1. Initialize FastAPI app
app = FastAPI(title="SewaSetu RAG API Server")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load Services Manifest
if not os.path.exists(MANIFEST_PATH):
    raise FileNotFoundError(f"Manifest file not found at: {MANIFEST_PATH}")

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest_data = json.load(f)

services_list = manifest_data.get("services", [])

# Map sno to service_id and vice-versa
sno_to_sid = {s["sno"]: int(s["service_id"]) for s in services_list}

# 3. Modular imports are now used instead of global model initialization.



def normalize_query_terms(text: str) -> str:
    """
    Normalizes query terms to ensure consistency across languages and avoid synonym mismatches.
    """
    if not text:
        return text
    # Case-insensitive replacements for English / Hinglish terms
    normalized = text
    
    # 1. Domicile / Residence Certificate synonyms
    normalized = re.sub(r'\b(residence certificate|niwas praman patra|niwas pramanpatra|local resident certificate)\b', 'domicile certificate', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'(निवास प्रमाण पत्र|निवास प्रमाणपत्र|स्थानीय निवास प्रमाण पत्र|स्थानीय निवासी प्रमाण पत्र)', 'मूल निवासी प्रमाण पत्र', normalized)
    
    # 2. Marriage Registration / Certificate synonyms
    normalized = re.sub(r'\b(marriage certificate|shadi certificate|shadi praman patra)\b', 'marriage registration and certificate', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'(शादी प्रमाण पत्र|शादी का प्रमाण पत्र|शादी प्रमाणपत्र|विवाह प्रमाण पत्र|विवाह प्रमाणपत्र)', 'विवाह पंजीकरण एवं प्रमाण पत्र', normalized)
    
    # 3. Caste Certificate synonyms
    normalized = re.sub(r'\b(caste certificate|jati certificate|jati praman patra|jati pramanpatra)\b', 'caste certificate', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'(जाति प्रमाण पत्र|जाति प्रमाणपत्र)', 'जाति प्रमाण पत्र', normalized)
    
    # 4. Affidavit / Shapath Patra — commonly mistranslated as "marriage certificate" by the LLM
    normalized = re.sub(r'\b(shapath patra|shapath\s*patra|shapathpatra|shapat patra|shapatpatra)\b', 'affidavit', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'(शपथ पत्र|शपथपत्र|शपत पत्र)', 'शपथ पत्र (affidavit)', normalized)

    # 5. Common Hinglish government document terms
    normalized = re.sub(r'\b(praman patra|pramanpatra|pramaan patra)\b', 'certificate', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\b(aavedan|aavedan patra|aavedan form)\b', 'application form', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\b(shulk|fees kitni|kitna paisa|kitne paise)\b', 'fees', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\b(samay seema|samay sima|kitne din|kitna samay)\b', 'time limit', normalized, flags=re.IGNORECASE)
    
    return normalized


def is_info_not_available(ans: str) -> bool:
    """
    Checks if the response indicates that the information is not available in the records.
    Normalizes the text to handle variations in punctuation, casing, language, and spacing.
    """
    if not ans:
        return True
    clean = re.sub(r'[^a-zA-Z0-9\u0900-\u097f\s]', '', ans).strip().lower()
    # English patterns
    if "information not available" in clean or "not available in my records" in clean or "insufficient information" in clean or "sufficient information" in clean or "records do not contain" in clean:
        return True
    # Hindi patterns
    if "जानकारी उपलब्ध नहीं" in clean or "पर्याप्त जानकारी नहीं" in clean or "रिकॉर्ड में पर्याप्त जानकारी नहीं" in clean:
        return True
    # Hinglish patterns
    if "jaankari uplabhd nahi" in clean or "jaankari uplabdha nahi" in clean or "uplabdh nahi" in clean or "paryapt jankari" in clean or "paryapt information" in clean or "uttar dene" in clean:
        return True
    return False


def _detect_query_language_simple(query: str) -> str:
    """
    Quick language detection for canned responses.
    Returns 'hi' for Hindi (Devanagari), 'hinglish' for Romanized Hindi, 'en' for English.
    """
    # Check for Devanagari characters
    if any('\u0900' <= c <= '\u097f' for c in query):
        return "hi"
    # Check for common Hinglish markers
    hinglish_markers = {"kya", "hai", "ho", "hain", "kaun", "kaise", "kahan", "kab",
                        "aap", "tum", "mujhe", "mera", "tera", "uska", "sab",
                        "namaste", "namaskar", "shukriya", "dhanyavaad", "alvida",
                        "haan", "nahi", "theek", "acha", "accha", "mein", "ki",
                        "ke", "ka", "se", "ko", "aur", "bhi", "toh", "hoga", "hogi",
                        "karna", "karne", "karo", "kariye", "kitna", "kitni",
                        "kitne", "kyun", "apna", "apni", "apne", "hum"}
    words = set(re.sub(r'[!?.,।\s]+', ' ', query.strip().lower()).split())
    if words & hinglish_markers:
        return "hinglish"
    return "en"


def get_intent_response(intent: str, query: str) -> Optional[dict]:
    """
    Given a classified intent from the LLM classifier, returns the appropriate
    canned response. Returns None if the intent requires RAG processing.
    
    Handles: greeting, farewell, thanks, identity, out_of_scope
    Does NOT handle: follow_up, new_topic (these go through RAG)
    """
    lang = _detect_query_language_simple(query)
    
    responses = {
        "greeting": {
            "en": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service.",
            "hi": "नमस्ते! 🙏 सेवासेतु एआई सहायक में आपका स्वागत है। छत्तीसगढ़ सरकारी सेवाओं के बारे में मैं आपकी कैसे मदद कर सकता/सकती हूँ? आप किसी भी सेवा के दस्तावेज़, शुल्क, पात्रता या आवेदन प्रक्रिया के बारे में पूछ सकते हैं।",
            "hinglish": "Namaste! 🙏 SewaSetu AI Assistant mein aapka swagat hai. Chhattisgarh sarkari sewaon ke baare mein main aapki kaise madad kar sakta/sakti hoon? Aap kisi bhi seva ke documents, fees, eligibility ya application process ke baare mein pooch sakte hain."
        },
        "farewell": {
            "en": "Thank you for using SewaSetu! 🙏 Have a great day. Feel free to come back anytime you need help with government services.",
            "hi": "सेवासेतु का उपयोग करने के लिए धन्यवाद! 🙏 आपका दिन शुभ हो। सरकारी सेवाओं में मदद के लिए कभी भी वापस आएं।",
            "hinglish": "SewaSetu use karne ke liye dhanyavaad! 🙏 Aapka din shubh ho. Sarkari sewaon mein madad ke liye kabhi bhi wapas aayein."
        },
        "thanks": {
            "en": "You're welcome! 🙏 Is there anything else I can help you with regarding Chhattisgarh government services?",
            "hi": "आपका स्वागत है! 🙏 क्या छत्तीसगढ़ सरकारी सेवाओं के बारे में कोई और मदद चाहिए?",
            "hinglish": "Aapka swagat hai! 🙏 Kya Chhattisgarh sarkari sewaon ke baare mein koi aur madad chahiye?"
        },
        "identity": {
            "en": "I am **SewaSetu AI Assistant** 🤖 — a chatbot designed to help citizens with **Chhattisgarh government services** available on the Sewa Setu portal.\n\nI can help you with:\n- 📄 **Documents** required for any service\n- 💰 **Fees** and payment methods\n- ✅ **Eligibility** criteria\n- 🕐 **Timelines** (SLA) for service delivery\n- 📝 **Application process** and how to apply\n\nPlease ask me anything about these services!",
            "hi": "मैं **सेवासेतु एआई सहायक** 🤖 हूँ — छत्तीसगढ़ सेवा सेतु पोर्टल पर उपलब्ध **सरकारी सेवाओं** में नागरिकों की मदद करने के लिए बनाया गया चैटबॉट।\n\nमैं इनमें मदद कर सकता/सकती हूँ:\n- 📄 किसी भी सेवा के लिए **आवश्यक दस्तावेज़**\n- 💰 **शुल्क** और भुगतान के तरीके\n- ✅ **पात्रता** मानदंड\n- 🕐 सेवा वितरण की **समयसीमा** (SLA)\n- 📝 **आवेदन प्रक्रिया**\n\nकृपया इन सेवाओं के बारे में कुछ भी पूछें!",
            "hinglish": "Main **SewaSetu AI Assistant** 🤖 hun — Chhattisgarh Sewa Setu portal par uplabdh **sarkari sewaon** mein nagrikon ki madad karne ke liye banaya gaya chatbot.\n\nMain in cheezon mein madad kar sakta/sakti hun:\n- 📄 Kisi bhi seva ke liye **zaroori documents**\n- 💰 **Fees** aur payment ke tarike\n- ✅ **Eligibility** criteria\n- 🕐 Seva delivery ki **timeline** (SLA)\n- 📝 **Application process** aur kaise apply karein\n\nKripya in sewaon ke baare mein kuch bhi poochein!"
        },
        "out_of_scope": {
            "en": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏",
            "hi": "मैं केवल सेवा सेतु पोर्टल पर उपलब्ध **छत्तीसगढ़ सरकारी सेवाओं** में मदद कर सकता/सकती हूँ। कृपया किसी भी सेवा के दस्तावेज़, शुल्क, पात्रता या आवेदन प्रक्रिया के बारे में पूछें। 🙏",
            "hinglish": "Main sirf **Chhattisgarh sarkari sewaon** mein madad kar sakta/sakti hun jo Sewa Setu portal par uplabdh hain. Kripya kisi bhi seva ke documents, fees, eligibility ya application process ke baare mein poochein. 🙏"
        }
    }
    
    if intent in responses:
        return {"response": responses[intent].get(lang, responses[intent]["en"])}
    
    return None




def sanitize_history(messages: Optional[list]) -> list:
    """
    Cleans conversation history:
    - Removes messages with empty/null content
    - Removes special message types (interactive_checklist, options)
    - Returns only valid user/assistant text messages
    """
    if not messages:
        return []
    
    clean = []
    for msg in messages:
        # Handle both Pydantic Message objects and dicts
        if hasattr(msg, 'content'):
            content = msg.content
            role = msg.role
        elif isinstance(msg, dict):
            content = msg.get('content')
            role = msg.get('role', 'user')
        else:
            continue
        
        # Skip empty content
        if not content or not content.strip():
            continue
        
        # Skip system messages
        if role == 'system':
            continue
        
        # Only keep user and assistant roles
        if role in ('user', 'assistant'):
            clean.append({"role": role, "content": content.strip()})
    
    return clean


def query_contains_service_keywords(query: str, resolved_query: str, service_id: int) -> bool:
    """
    Checks if the user query or the resolved query contains keywords matching the given service_id.
    Helps in detecting explicit service switches.
    """
    q = (query + " " + resolved_query).lower()
    keywords = {
        3: ["marriage", "shadi", "shaadi", "विवाह", "शादी"],
        4: ["sc", "st", "caste", "jati", "जाति", "एससी", "एसटी"],
        5: ["obc", "caste", "jati", "पिछड़ा", "ओबीसी"],
        7: ["domicile", "resident", "niwas", "निवास", "निवासी", "मूल निवासी"],
        201: ["name change", "gazette", "नाम", "परिवर्तन", "राजपत्र", "naam change", "naam badal", "naam parivartan", "naam correction", "change name"]
    }
    return any(kw in q for kw in keywords.get(service_id, []))


def build_condensed_history(sanitized_history: list, is_follow_up: bool, topic_summary: str = "") -> list:
    """
    Builds a condensed history for the final synthesis stage.
    
    To implement the 'Query Reformulation + Stateless QA' pattern and prevent
    context leakage/attention hijacking (e.g. repeating document checklists 
    when answering unrelated follow-up questions), history is completely 
    eradicated from the final answer generation phase.
    
    History remains fully utilized in the classifier phase for intent detection 
    and query rewriting/resolution.
    """
    return []


def is_checklist_query(query: str, english_query: str, hindi_query: str) -> bool:
    """
    Determines if the query is requesting the document checklist itself.
    """
    text = f"{query} {english_query} {hindi_query}".lower()
    
    # Checklist indicators
    checklist_indicators = [
        "documents required", "document required", "required documents", "required document",
        "documents needed", "document needed", "needed documents", "needed document",
        "documents list", "document list", "list of documents", "list of document",
        "what documents", "which documents", "checklist", "check list",
        "documents do i need", "documents to apply", "dastavez ki list", "dastavej ki list",
        "dastawez ki list", "dastavez chahiye", "dastavej chahiye", "dastawez chahiye",
        "kaun se document", "kaun-se document", "kaun kaun se", "documents ki list",
        "ज़रूरी दस्तावेज़", "आवश्यक दस्तावेज़", "आवश्यक दस्तावेज", "दस्तावेजों की सूची",
        "दस्तावेज सूची", "कागजात"
    ]
    if any(k in text for k in checklist_indicators):
        return True
        
    if re.search(r'\b(document|documents|dastavez|dastawez|dastavej|dastawej|kaagaz|kagaz)\b', text):
        specific_docs = ["birth", "marriage", "caste", "domicile", "income", "ration", "electricity", "affidavit", "photo"]
        if not any(d in text for d in specific_docs):
            return True
            
    return False


def is_eligibility_or_document_query(query: str, english_query: str, hindi_query: str) -> bool:
    """
    Determines if the query is about either eligibility criteria or required documents.
    """
    text = f"{query} {english_query} {hindi_query}".lower()
    keywords = [
        "eligibility", "eligible", "patrata", "criteria", "condition", "conditions",
        "rule", "rules", "exception", "exceptions", "document", "documents", 
        "dastavez", "dastawez", "dastavej", "dastawej", "checklist", "check list",
        "list of", "ज़रूरी दस्तावेज़", "दस्तावेज़", "दस्तावेज", "पात्रता", "नियम", "शर्तें"
    ]
    return any(k in text for k in keywords)


# Pydantic schemas
class Message(BaseModel):
    role: str  # 'user', 'assistant' or 'system'
    content: Optional[str] = None

class ChatRequest(BaseModel):
    query: Optional[str] = None
    lang: Optional[str] = None
    service_id: Optional[Any] = None
    conversation_history: Optional[List[Message]] = None

    # Frontend support schemas
    messages: Optional[List[Message]] = None
    selected_sno: Optional[str] = None
    language: Optional[str] = None
    detailed: Optional[bool] = False
    interactive: Optional[bool] = False
    is_option_click: Optional[bool] = False

class SearchRequest(BaseModel):
    query: str
    language: Optional[str] = "en"


# Endpoints

@app.get("/api/services")
def list_services():
    """
    Returns the list of the 5 in-scope services from the manifest.
    """
    # Keep the response model clean for the frontend, return target fields
    result = []
    for s in services_list:
        result.append({
            "sno": s["sno"],
            "service_id": s["service_id"],
            "name_en": s["name_en"],
            "name_hi": s["name_hi"],
            "dept_en": s["dept_en"],
            "dept_hi": s["dept_hi"],
            "is_internal": s.get("is_internal", True)
        })
    return result


@app.get("/api/services/{sno}")
def get_service_details(sno: str, lang: str = "en"):
    """
    Retrieves the detailed JSON profile of a specific service from the profiles directory.
    """
    target_service = None
    for s in services_list:
        if str(s["sno"]) == str(sno):
            target_service = s
            break

    if not target_service:
        raise HTTPException(status_code=404, detail=f"Service with serial number {sno} not found.")

    # Determine profile path
    path_key = f"path_{lang}"
    rel_path = target_service.get(path_key) or target_service.get("path_en")
    if not rel_path:
        raise HTTPException(status_code=404, detail="Service profile path not configured in manifest.")

    filepath = os.path.join(WORKSPACE_DIR, rel_path)
    if not os.path.exists(filepath):
        # Fallback to English profile
        rel_path_en = target_service.get("path_en")
        if rel_path_en:
            filepath = os.path.join(WORKSPACE_DIR, rel_path_en)

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail=f"Profile JSON details not found at {rel_path}.")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        fees_obj = data.get("fees", {})
        kiosk_fee = fees_obj.get("kiosk_fee", "30.0")
        online_fee = fees_obj.get("online_fee", "30.0")
        raw_fees_text = fees_obj.get("raw_text", "")

        req_docs_structured = data.get("required_documents_structured", [])
        req_docs = data.get("required_documents", [])

        details_payload = {
            "sno": str(sno),
            "service_id": str(target_service["service_id"]),
            "name": data.get("name"),
            "department": data.get("department"),
            "time_limit": data.get("time_limit") or data.get("sla"),
            "contact_details": data.get("contact_details", "Sewa Setu Kendra"),
            "fees": {
                "online_fee": online_fee,
                "kiosk_fee": kiosk_fee,
                "raw_text": raw_fees_text
            },
            "details_link": data.get("details_link"),
            "required_documents_structured": req_docs_structured,
            "required_documents": req_docs,
            "form_fields": data.get("form_fields", [])
        }
        return details_payload
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading service details profile: {str(e)}")


async def process_query_languages(query: str):
    """
    Detects language and translates to English & Hindi conditionally.
    """
    query_lang = await asyncio.to_thread(detect_query_language, query)
    lang = (query_lang or "").strip().lower()
    
    if lang == "en":
        english_query = query
        hindi_query = await asyncio.to_thread(translate_query_to_hindi, query)
    elif lang == "hi":
        english_query = await asyncio.to_thread(translate_query_to_english, query)
        hindi_query = query
    else:
        # Hinglish or other: translate to both
        en_task = asyncio.to_thread(translate_query_to_english, query)
        hi_task = asyncio.to_thread(translate_query_to_hindi, query)
        english_query, hindi_query = await asyncio.gather(en_task, hi_task)
        
    return query_lang, english_query, hindi_query


def parse_checklist_chunk_to_json(chunk_text: str) -> dict:
    """
    Parses the pinned REQUIRED DOCUMENTS chunk text using regex.
    Output format:
    {
      "groups": [
        {
          "id": "g1",
          "title": "Group name",
          "mandatory": true,
          "anyOne": true,
          "docs": [
            {"id": "d1", "name": "Document name", "mandatory": true}
          ]
        }
      ]
    }
    """
    groups = []
    current_group = None
    group_id_counter = 1
    doc_id_counter = 1
    
    # Split into lines
    lines = chunk_text.split('\n')
    
    # Find where the REQUIRED DOCUMENTS section starts
    started = False
    for line in lines:
        if "REQUIRED DOCUMENTS:" in line or "आवश्यक दस्तावेज़:" in line or "आवश्यक दस्तावेज:" in line:
            started = True
            continue
        
        # If we hit another section (like APPLICATION FORM FIELDS:), we can stop
        if started and ":" in line and not (line.strip().startswith("-") or line.strip().startswith("*")):
            if any(x in line for x in ["APPLICATION FORM FIELDS", "APPLICATION", "EXTRACTED PDF"]):
                break

        if not started:
            continue
            
        # Match group header
        # Format: - SNo 1: Residential Proof (Mandatory: No)
        # Or Hindi: - SNo 1: निवास का प्रमाण (Mandatory: नहीं)
        group_match = re.match(r'^\s*-\s*SNo\s+\d+:\s*(.*?)\s*\(\s*(?:Mandatory|अनिवार्य)\s*:\s*(.*?)\s*\)', line)
        if group_match:
            title = group_match.group(1).strip()
            mandatory_str = group_match.group(2).strip().lower()
            is_mandatory = mandatory_str in ["yes", "हाँ", "हा", "true"]
            
            current_group = {
                "id": f"g{group_id_counter}",
                "title": title,
                "mandatory": is_mandatory,
                "anyOne": False, # Will be set to True if len(docs) > 1
                "docs": []
            }
            group_id_counter += 1
            groups.append(current_group)
            continue
            
        # Match supporting document
        # Format:   * Supporting Document 1: Domicile Certificate
        # Or Hindi:   * Supporting Document 1: मूल निवासी प्रमाण पत्र
        doc_match = re.match(r'^\s*\*\s*Supporting\s+Document\s+\d+:\s*(.*)', line)
        if doc_match and current_group:
            doc_name = doc_match.group(1).strip()
            if not doc_name:
                continue
                
            doc_item = {
                "id": f"d{doc_id_counter}",
                "name": doc_name,
                "mandatory": current_group["mandatory"]
            }
            doc_id_counter += 1
            current_group["docs"].append(doc_item)
            
            # Update anyOne flag: if a group contains more than 1 doc, it's anyOne
            if len(current_group["docs"]) > 1:
                current_group["anyOne"] = True
                
    return {"groups": groups}


async def run_rag_pipeline_intermediates(
    query: str, 
    request: ChatRequest, 
    service_id: Optional[int],
    query_lang: Optional[str] = None,
    english_query: Optional[str] = None,
    hindi_query: Optional[str] = None
):
    """
    Runs language processing and context retrieval concurrently (async).
    """
    query = normalize_query_terms(query)
    if not query_lang or not english_query or not hindi_query:
        query_lang, english_query, hindi_query = await process_query_languages(query)

    if query_lang == "en":
        fallback_msg = "I do not have sufficient information or context in my records to answer this question. Please check the Sewa Setu portal."
    elif query_lang == "hi":
        fallback_msg = "मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी या आवश्यक संदर्भ नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।"
    else:
        fallback_msg = "Mere paas is question ka answer dene ke liye records mein context ya paryapt information nahi hai. Kripya Sewa Setu portal par check karein."

    if service_id is None:
        return query_lang, english_query, hindi_query, "", "", fallback_msg

    # Retrieve English and Hindi contexts concurrently
    context_en_task = asyncio.to_thread(retrieve_context, query, service_id, 4, english_query, hindi_query, "en")
    context_hi_task = asyncio.to_thread(retrieve_context, query, service_id, 4, english_query, hindi_query, "hi")
    (context_en, metadata_en, checklist_text_en), (context_hi, metadata_hi, checklist_text_hi) = await asyncio.gather(context_en_task, context_hi_task)

    return query_lang, english_query, hindi_query, context_en, context_hi, fallback_msg


async def synthesize_final_response(
    query: str,
    query_lang: str,
    english_query: str,
    hindi_query: str,
    context_en: str,
    context_hi: str,
    fallback_msg: str,
    request: ChatRequest,
    service_id: Optional[int],
    condensed_history: Optional[list] = None
):
    """
    Synthesizes final response in the user's language using dual context in a single LLM call.
    """
    # Dynamic target language matching
    if query_lang == "en":
        lang_label = "English"
        lang_instruction = (
            "You MUST respond ENTIRELY in English using only the Roman alphabet. "
            "Do NOT write in Devanagari script (Hindi characters) and do NOT use Hinglish words. "
            "Every single word must be standard English."
        )
    elif query_lang == "hi":
        lang_label = "Hindi"
        lang_instruction = (
            "You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n"
            "- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n"
            "- Every single word must be written in Devanagari.\n"
            "- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
        )
    else:  # Hinglish
        lang_label = "Hinglish"
        lang_instruction = (
            "You MUST respond ENTIRELY in Hinglish — that is, Hindi language written ONLY in Roman/Latin alphabet script. "
            "ABSOLUTELY NO Devanagari characters (क, ख, ग, है, हैं, क्या, आप, जी, etc.) are allowed anywhere in your response. "
            "Every single character must be a Latin letter (a-z, A-Z), number, or standard punctuation. "
            "Write Hindi words in Roman script. For example: 'Haan', 'Nahi', 'Aap', 'Kya', 'Zaroor', 'Domicile certificate', 'Sarkari naukri'. "
            "Do NOT write in pure formal English either — use natural conversational Hinglish as spoken in India. "
            "If you accidentally write even one Devanagari character, your response will be rejected."
        )

    # Dynamic service-specific rules
    service_rules_final = ""
    if service_id is not None:
        if int(service_id) == 7:
            service_rules_final = (
                "- ELIGIBILITY LOGIC RULE (Domicile): If a citizen asks about eligibility or exceptions for the Domicile Certificate, explain the rules strictly:\n"
                "  1. Main Path (Both Criteria One AND Criteria Two must be met): The applicant must satisfy AT LEAST ONE option from Criteria One (Criteria A) AND AT LEAST ONE option from Criteria Two (Criteria B).\n"
                "     * You MUST list Criteria One and Criteria Two under separate, clearly-labeled headers or bullet points.\n"
                "     * Criteria One (Criteria A) options: Birth in CG, parent resident for 25 years, parent is CG Government/PSU employee, or property in CG for 5 years.\n"
                "     * Criteria Two (Criteria B) options: 3 years of school study in CG, or passing Class 5, 8, 10, 12 board exam from CG.\n"
                "     * Never merge them into one list or omit the education requirements of Criteria Two.\n"
                "  2. Exceptions (Criteria Three / Criteria C): If they do not meet the Main Path (for example, if they lack 'Proof of 15 Years Stay' or did not study in CG), they can still get a Domicile Certificate under the exceptions of Criteria Three (C). For Criteria Three (C), Criteria A and B are NOT required. The exceptions are: (a) spouse is a domicile of CG, (b) applicant or spouse is a CG Government/PSU employee, or (c) applicant or parent is in All India Services and allotted CG Cadre.\n"
                "  3. Clarity: Never state that Criteria Three requires stay proof or education. Clearly explain that Criteria Three is a standalone set of exceptions that bypasses the need for the stay proof or CG education requirements of Criteria One and Two.\n"
            )
        elif int(service_id) == 3:
            service_rules_final = (
                "- MARRIAGE JURISDICTION RULE: Under the Chhattisgarh Compulsory Registration of Marriages Rules, a marriage MUST be registered in the local area where the marriage was solemnized or performed, NOT at the couple's hometown or place of residence. The registrar is the Local Authority of that local area (Gram Panchayat if rural; Municipality or Municipal Corporation if urban). State this clearly when citizens ask where or under which office/authority to register their marriage.\n"
            )
        elif int(service_id) == 5:
            service_rules_final = (
                "- OBC RESIDENCY/DOMICILE RULE: If the citizen asks about Domicile or Residence rules/requirements for the OBC Certificate, explain clearly based on the context:\n"
                "  1. A Domicile Certificate (मूल निवासी प्रमाण पत्र) is NOT mandatory (it is listed as one of several optional supporting documents under 'Residential Proof').\n"
                "  2. To satisfy the residency requirement for the OBC Certificate, the applicant or their ancestors must have been residing in the geographical limits of Chhattisgarh since or before the OBC notification date, which is December 26, 1984 (२६ दिसम्बर १९८४).\n"
                "  3. List the alternative supporting documents for Residential Proof (such as Land/House documents, Ration Card, Electricity Bill, Ward Member/MLA/MP certificate, Birth Certificate).\n"
            )
        elif int(service_id) == 201:
            service_rules_final = (
                "- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n"
                "  1. Do NOT output 'Information not available.'\n"
                "  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n"
                "  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n"
            )

    system_instruction = f"""STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):
Your ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.
- If asked about fees or penalties → respond ONLY with fee, penalty, and fine details. Do NOT mention documents, eligibility, or process. If a fee or penalty is contingent on a timeframe or delay (such as late registration penalties), you are allowed and expected to explain the timeframe/deadline and the corresponding fine or penalty amount.
- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.
- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.
- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.
- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.
- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.

BREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.
- For single-aspect questions (like "how many days?" or "what is the fee?"), your answer should be 2-5 lines MAX.
- NEVER dump the full service overview when only one aspect is asked.

You are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.
- LANGUAGE AND SCRIPT RULES: {lang_instruction}
- Be warm, respectful, and citizen-friendly.
{service_rules_final}
- DOCUMENT MANDATORINESS RULE (REQUIRED VS OPTIONAL): When answering if a document is required, mandatory, or optional:
  1. Check the 'REQUIRED DOCUMENTS' section in the context.
  2. If a document category is marked as 'Mandatory: No' or 'Mandatory: नहीं', it is OPTIONAL (वैकल्पिक), not mandatory (अनिवार्य).
  3. If a document category is optional, check the list of 'Supporting Documents' under it. These are alternative options. Explain that the applicant can submit ANY ONE of these alternatives (e.g. Electricity Bill, Ration Card, Voter ID, Domicile certificate) to satisfy that category, and that a Domicile Certificate (निवास प्रमाण पत्र) is NOT mandatory if other alternatives are provided.
  4. Only state a document is mandatory (अनिवार्य) if it is explicitly marked as 'Mandatory: Yes' or 'Mandatory: हाँ'. If a citizen asks about bypassing an explicitly mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.
  5. If the user asks if X is required or needed (e.g., 'X लगता है क्या?', 'is X required?'), and X is optional (Mandatory: No / नहीं), you MUST begin your response by clearly stating that 'नहीं, X अनिवार्य नहीं है (यह वैकल्पिक है)।' (No, X is not mandatory; it is optional) and explain they can submit other alternative documents instead. Do NOT say 'Yes, X is required/essential'.
- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs. If the query asks about late registration, delay penalty, or extra fees for late submission, check the retrieved context rules for any mention of time limits and associated penalties or fines (such as fines for late submission). If a time limit is exceeded based on the timeframe in the user's query, clearly state that a penalty or fine applies as per the rules. Note that if a rule specifies a penalty or fine for failing to submit or register within a given timeframe, this penalty/fine applies to any registrations or submissions made after that timeframe has passed (for example, registering after 1 year when the limit is 30 days).
- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS.
  1. Do NOT assume, extrapolate, or use external knowledge. Simple mathematical calculations, duration comparisons, or logical time-period deductions based directly on facts in the context (for example, comparing a user's stated delay or timeframe against a deadline or duration limit specified in the context) are allowed and expected, and are NOT considered extrapolation. Additionally, treat equivalent administrative terms as referring to the same process (for example, submitting the marriage memorandum refers to registering a marriage under the rules).
  2. LOGICAL DEDUCTION: If a query asks about a timeframe, delay, or duration that exceeds a deadline or time limit specified in the context, you must reason step-by-step: first identify the deadline/timeframe in the context, then compare the user's duration to that deadline, and clearly state the penalty, fine, or consequences defined in the context rules. Specifically, if a rule requires an action within a specific timeframe (like submitting a memorandum within 30 days) and another rule penalizes the failure to perform that action under the first rule, then performing that action after the timeframe has passed (like after 1 year) constitutes a failure to comply with the timeframe and is subject to that penalty/fine. You must explain that the penalty/fine (e.g. fine up to 500 rupees) applies to such late submissions/registrations. Do not claim there is no penalty or that the fine only applies to not submitting at all.
  3. If the user's query refers to a specific named individual, public figure, celebrity, politician, organization, or entity (e.g. Narendra Modi, Rahul Gandhi, MS Dhoni, etc.) that is NOT explicitly mentioned in the source documents, you MUST treat it as having insufficient information and reply EXACTLY with the language-specific fallback message. You are STRICTLY FORBIDDEN from using external knowledge about their background, or applying the context eligibility criteria to speculate on their status.
  4. If the user asks about performing a specific action, update, process, correction, or change (e.g. 'address change on marriage certificate', 'download certificate using digital signature', 'correction of date of birth') that is NOT explicitly described in the retrieved source context, you MUST treat it as having insufficient information. Do NOT guess, assume, or fabricate a process, options, or fees. You MUST reply EXACTLY with the language-specific fallback message.
  5. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: "I do not have sufficient information or context in my records to answer this question. Please check the Sewa Setu portal." (or its equivalent translation based on the query language: "मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी या आवश्यक संदर्भ नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।" for Hindi, and "Mere paas is question ka answer dene ke liye records mein context ya paryapt information nahi hai. Kripya Sewa Setu portal par check karein." for Hinglish).
- NO PLACEHOLDERS OR BLANK FORM TEMPLATES: If you find yourself writing template placeholders like '[जिला का नाम]', '[तहसील का नाम]', '[आवेदक का नाम]', 'वर्ष २०', 'दिनांक', 'क्रमांक', or generic blank template fields, it means the source documents DO NOT contain the actual address or answer. You are STRICTLY FORBIDDEN from outputting these placeholders. In all such cases, you MUST return the exact fallback message instead.
- Ignore any contradictions in conversation history.

FORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.

CRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.

--- ENGLISH SOURCE DOCUMENTS ---
{context_en}
--- END ENGLISH SOURCE DOCUMENTS ---

--- HINDI SOURCE DOCUMENTS ---
{context_hi}
--- END HINDI SOURCE DOCUMENTS ---
"""

    messages_final = [{"role": "system", "content": system_instruction}]
    if condensed_history:
        for msg in condensed_history:
            messages_final.append({"role": msg["role"], "content": msg["content"]})
    messages_final.append({"role": "user", "content": f"{query}\n\nIMPORTANT: You MUST respond ENTIRELY in {lang_label}. {lang_instruction}"})

    final_reply = await asyncio.to_thread(generate_answer, messages_final)

    # Post-processing: Devanagari leakage safety net for Hinglish responses
    if query_lang == "hinglish" and re.search(r'[\u0900-\u097f]', final_reply):
        print("[Synthesis] WARNING: Hinglish response contains Devanagari characters. Re-converting to Roman script...")
        try:
            romanize_messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a strict Devanagari-to-Roman script transliterator (converting Hindi to Hinglish).\n"
                        "ABSOLUTELY NO Devanagari characters (क, ख, ग, है, हैं, क्या, etc.) are allowed in your output. "
                        "Do NOT write any introduction, greetings, explanations, or conversational filler. "
                        "Translate/transliterate ALL Devanagari Hindi characters to Roman script/Hinglish (e.g. 'नहीं' to 'Nahi', 'अनिवार्य' to 'Anivarya'). "
                        "Keep all English words in the text exactly as-is. "
                        "Do NOT translate Hindi to English; only transliterate it phonetically to Hinglish (Roman alphabet)."
                    )
                },
                {
                    "role": "user",
                    "content": f"Text to convert:\n{final_reply}\n\nRoman script output:"
                }
            ]
            romanized = await asyncio.to_thread(generate_answer, romanize_messages)
            if romanized and not re.search(r'[\u0900-\u097f]', romanized):
                final_reply = romanized
                print("[Synthesis] Successfully romanized Hinglish response.")
            else:
                print("[Synthesis] Romanization still contains Devanagari. Using as-is.")
        except Exception as e:
            print(f"[Synthesis] Romanization failed: {e}")
    
    # Post processing for links
    final_reply = re.sub(r'\[.*?\]\(https?://.*?\)', '', final_reply)
    
    # Resolve and append redirection link
    details_link = None
    if service_id:
        target_service = None
        for s in services_list:
            if int(s["service_id"]) == int(service_id):
                target_service = s
                break
        if target_service:
            lang_str = "hi" if query_lang == "hi" else "en"
            details_link = f"https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId={service_id}&lang={lang_str}"
            
    grounding_status = "N/A"

    if is_info_not_available(final_reply):
        final_reply = fallback_msg

    if details_link and final_reply != fallback_msg and details_link not in final_reply:
        if query_lang == "en":
            final_reply += f"\n\nFor more details and online application, please visit:\n[Apply on Sewa Setu Portal]({details_link})"
        elif query_lang == "hi":
            final_reply += f"\n\nअधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:\n[सेवा सेतु पोर्टल पर आवेदन करें]({details_link})"
        else:
            final_reply += f"\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein]({details_link})"

    if request.detailed:
        return {
            "response": final_reply,
            "query_lang": query_lang,
            "english_query": english_query,
            "hindi_query": hindi_query,
            "context_en": context_en,
            "context_hi": context_hi,
            "english_answer": "N/A",
            "hindi_answer": "N/A",
            "service_id": service_id,
            "grounding_status": grounding_status
        }
    return {"response": final_reply, "service_id": service_id}




async def run_rag_pipeline(query: str, request: ChatRequest, service_id: Optional[int]):
    """
    Consolidated RAG execution and response synthesis pipeline (Async).
    """
    query = normalize_query_terms(query)
    query_lang, english_query, hindi_query = await process_query_languages(query)


    # === INTENT CLASSIFICATION + QUERY RESOLUTION (MOVED TO TOP) ===
    raw_history = request.conversation_history or []
    if not raw_history and request.messages:
        raw_history = request.messages[:-1]
    sanitized = sanitize_history(raw_history)

    # Filter out greeting exchanges from history (they're not service context)
    greeting_words = {"hi", "hello", "hey", "hii", "hiii", "namaste", "namaskar", "bye", "thanks", "thank you", "ok", "okay", "haan", "theek hai"}
    filtered_sanitized = []
    skip_next = False
    for msg in sanitized:
        if skip_next:
            skip_next = False
            continue
        if msg["role"] == "user" and msg["content"].strip().lower() in greeting_words:
            # Skip this user greeting AND the next assistant response
            skip_next = True
            continue
        filtered_sanitized.append(msg)
    sanitized = filtered_sanitized

    # Programmatic override for spelling/name corrections on active applications vs issued certificates
    force_new_topic_201 = False
    q_clean = query.lower()
    
    # Generic structural keywords (no specific out-of-scope services hardcoded)
    status_terms = ["submitted", "pending", "draft", "lending", "in-progress", "fill", "filling", "bhara", "bharne", "जमा", "भरने", "भरते"]
    form_terms = ["application", "form", "आवेदन", "फॉर्म"]
    mistake_terms = ["mistake", "error", "typo", "spelling", "speling", "mistak", "mistek", "spelling mistake", "spelling error", "गलती", "त्रुटि", "वर्तनी"]
    correction_terms = ["correct", "correction", "change", "update", "modify", "amend", "sujhaar", "sudhaar", "सुधार", "संशोधन", "बदल"]

    has_status = any(word in q_clean for word in status_terms)
    has_form = any(word in q_clean for word in form_terms)
    has_mistake = any(word in q_clean for word in mistake_terms)
    has_correction = any(word in q_clean for word in correction_terms)

    # Typo correction on an active/draft/submitted application form:
    is_active_form_typo = (has_mistake and (has_form or has_status)) or (has_correction and has_status and has_form)

    if is_active_form_typo:
        print("[RAG Pipeline] Programmatic intercept: active application typo correction. Returning fallback.")
        if query_lang == "en":
            fallback_msg = "I do not have sufficient information or context in my records to answer this question. Please check the Sewa Setu portal."
        elif query_lang == "hi":
            fallback_msg = "मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी या आवश्यक संदर्भ नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।"
        else:
            fallback_msg = "Mere paas is question ka answer dene ke liye records mein context ya paryapt information nahi hai. Kripya Sewa Setu portal par check karein."
        
        if request.detailed:
            return {
                "response": fallback_msg,
                "query_lang": query_lang,
                "english_query": english_query,
                "hindi_query": hindi_query,
                "context_en": "",
                "context_hi": "",
                "english_answer": "I do not have sufficient information or context in my records to answer this question. Please check the Sewa Setu portal.",
                "hindi_answer": "मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी या आवश्यक संदर्भ नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।",
                "service_id": service_id
            }
        return {"response": fallback_msg, "service_id": service_id}
    
    # Name correction on ALREADY ISSUED certificates:
    # Exclude joint-application or comparison queries structurally (words like "together", "vs")
    elif has_correction and not is_active_form_typo:
        has_cert = any(word in q_clean for word in ["certificate", "praman", "प्रमाण", "caste", "domicile", "marriage", "obc", "sc", "st", "jati", "shadi", "विवाह", "शादी", "मूल", "निवास"])
        is_name_query = any(word in q_clean for word in ["name", "naam", "नाम", "spelling", "वर्तनी", "spell"])
        is_joint_or_comparison = any(word in q_clean for word in ["together", "dono", "ek sath", "ek-sath", "vs", "difference", "comparison", "अंतर", "तुलना", "तुलना करें", "बनाम", "समान", "समानता", "बराबर"])
        
        if has_cert and is_name_query and not is_joint_or_comparison:
            print("[RAG Pipeline] Programmatic override: routing issued certificate correction to Gazette (Service ID 201)")
            service_id = 201
            force_new_topic_201 = True

    # Classify query intent FIRST — needs full history to understand follow-ups
    intent_result = await asyncio.to_thread(
        classify_query_intent, query, sanitized
    )
    intent = intent_result["intent"]
    resolved_query = intent_result["resolved_query"]
    topic_summary = intent_result["topic_summary"]
    
    if force_new_topic_201:
        print("[RAG Pipeline] Forcing new_topic for Gazette correction override.")
        intent = "new_topic"
        resolved_query = query
    
    print(f"[RAG Pipeline] Intent: {intent}, Resolved query: '{resolved_query}', Topic: '{topic_summary}'")

    if intent == "new_topic" and not force_new_topic_201:
        try:
            classification = await asyncio.to_thread(classify_service, query, services_list, False)
            if classification:
                if classification.get("service_id"):
                    new_service_id = int(classification["service_id"])
                    print(f"[RAG Pipeline] Dynamic LLM classification mapped query to service_id: {new_service_id}")
                    service_id = new_service_id
                else:
                    # Generic / Comparison / Out-of-Scope queries mapped to None (no sidebar pinning, search entire DB)
                    print(f"[RAG Pipeline] Dynamic LLM classification mapped query to None")
                    service_id = None
        except Exception as e:
            print(f"[RAG Pipeline] Dynamic LLM classification failed: {e}")

    # === INTERCEPT non-RAG intents (greeting, farewell, thanks, identity, out_of_scope) ===
    intent_response = get_intent_response(intent, query)
    if intent_response:
        print(f"[RAG Pipeline] Intent '{intent}' intercepted -> returning canned response")
        if request.detailed:
            intent_response.update({
                "query_lang": "N/A",
                "english_query": "N/A",
                "hindi_query": "N/A",
                "context_en": "",
                "context_hi": "",
                "english_answer": "N/A",
                "hindi_answer": "N/A",
                "service_id": "N/A",
                "intent": intent
            })
        return intent_response

    service_name = "Chhattisgarh Citizen Service"
    service_name_hi = "छत्तीसगढ़ नागरिक सेवा"
    if service_id:
        for s in services_list:
            if str(s["service_id"]) == str(service_id):
                service_name = s["name_en"]
                service_name_hi = s["name_hi"]
                break

    # 1. Deterministic choice prompt for eligibility or document queries
    if request.interactive and service_id and not request.is_option_click and is_eligibility_or_document_query(query, english_query, hindi_query):
        if query_lang == "hi":
            default_text = f"क्या आप {service_name_hi} दस्तावेज़ चेकलिस्ट का उपयोग करके अपनी पात्रता जांचना चाहते हैं, या विस्तृत पात्रता मानदंडों की जानकारी देखना चाहते हैं, या सीधे अपने प्रश्न का उत्तर चाहते हैं?"
            options = [
                {
                    "label": f"📋 {service_name_hi} चेकलिस्ट द्वारा पात्रता जांचें",
                    "query": f"Show required documents checklist for {service_name}"
                },
                {
                    "label": f"ℹ️ {service_name_hi} के विस्तृत नियम देखें",
                    "query": f"Explain all criteria and eligibility rules for {service_name}"
                },
                {
                    "label": "💬 सीधे अपने सवाल का जवाब पाएं",
                    "query": query
                }
            ]
        elif query_lang == "hinglish":
            default_text = f"Kya aap {service_name} ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?"
            options = [
                {
                    "label": f"📋 Check Eligibility for {service_name} via Checklist",
                    "query": f"Show required documents checklist for {service_name}"
                },
                {
                    "label": f"ℹ️ Explain Detailed Eligibility & Rules for {service_name}",
                    "query": f"Explain all criteria and eligibility rules for {service_name}"
                },
                {
                    "label": "💬 Directly Answer My Question",
                    "query": query
                }
            ]
        else:
            default_text = f"Would you like to check your eligibility for the {service_name} using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?"
            options = [
                {
                    "label": f"📋 Check Eligibility for {service_name} via Checklist",
                    "query": f"Show required documents checklist for {service_name}"
                },
                {
                    "label": f"ℹ️ Explain Detailed Eligibility & Rules for {service_name}",
                    "query": f"Explain all criteria and eligibility rules for {service_name}"
                },
                {
                    "label": "💬 Directly Answer My Question",
                    "query": query
                }
            ]
            
        return {
            "mode": "options",
            "text": default_text,
            "options": options,
            "service_id": service_id
        }

    # 2. Interactive checklist intercept:
    should_intercept = False
    if request.interactive and service_id:
        if request.is_option_click:
            if "show required documents checklist" in query.lower():
                should_intercept = True
        else:
            if is_checklist_query(query, english_query, hindi_query):
                should_intercept = True

    if should_intercept:
        lang_to_use = "hi" if query_lang == "hi" else "en"
        
        # Retrieve context with force_checklist = True
        context_string, metadata_list, raw_checklist_text = await asyncio.to_thread(
            retrieve_context, query, service_id, 6, english_query, hindi_query, lang_to_use, True
        )
        
        if raw_checklist_text:
            parsed_json = parse_checklist_chunk_to_json(raw_checklist_text)
            return {
                "mode": "interactive",
                "documents": parsed_json,
                "service_id": service_id
            }

    # Always use resolved_query for RAG retrieval — the classifier now produces
    # a self-contained query for BOTH intents (with aspect carry-over for new_topic)
    rag_query = resolved_query
    is_follow_up = (intent == "follow_up")
    
    # If the user is starting a new topic, use the original query instead of the rewritten query to prevent hallucination switches
    if intent == "new_topic":
        rag_query = query

    # Check if target service has switched compared to history
    last_service_id = None
    for msg in reversed(sanitized):
        if msg["role"] == "assistant":
            match = re.search(r'serviceId=(\d+)', msg["content"])
            if match:
                last_service_id = int(match.group(1))
                break
    
    if last_service_id and service_id and last_service_id != service_id:
        if is_follow_up and query_contains_service_keywords(query, resolved_query, service_id):
            print(f"[RAG Pipeline] SAFETY: Query contains keywords of the new service ({service_id}) which differs from history ({last_service_id}). Forcing new_topic.")
            is_follow_up = False
            intent = "new_topic"
            rag_query = query
        
        if is_follow_up:
            print(f"[RAG Pipeline] Follow-up detected but sidebar service ({service_id}) differs from conversation service ({last_service_id}). Trusting classifier → using service_id={last_service_id}")
            service_id = last_service_id
        else:
            print(f"[RAG Pipeline] Service switch detected (history={last_service_id}, sidebar={service_id}). Clearing history for synthesis.")
            sanitized = []
            is_follow_up = False

    # SAFETY CHECK: Detect misclassified topic switches
    if is_follow_up and topic_summary:
        topic_lower = topic_summary.lower()
        if any(phrase in topic_lower for phrase in ["different service", "new service", "another service", "different topic"]):
            print(f"[RAG Pipeline] SAFETY: Classifier said follow_up but topic indicates topic switch. Forcing new_topic.")
            is_follow_up = False
            intent = "new_topic"
            rag_query = query

    # Build condensed history for final synthesis only
    condensed = build_condensed_history(sanitized, is_follow_up, topic_summary)

    if rag_query.lower().strip() != query.lower().strip():
        print(f"[RAG Pipeline] Re-translating resolved query for RAG: '{rag_query}'")
        original_query_lang = query_lang
        _, english_query, hindi_query = await process_query_languages(rag_query)
        query_lang = original_query_lang
        print(f"[RAG Pipeline] Preserved original query_lang: '{query_lang}'")

    # Use the resolved query + re-translated languages for RAG retrieval
    query_lang, english_query, hindi_query, context_en, context_hi, fallback_msg = await run_rag_pipeline_intermediates(
        rag_query, request, service_id, query_lang, english_query, hindi_query
    )
    
    if not context_en and not context_hi:
        if request.detailed:
            return {
                "response": fallback_msg,
                "query_lang": query_lang,
                "english_query": english_query,
                "hindi_query": hindi_query,
                "context_en": "",
                "context_hi": "",
                "english_answer": "Information not available.",
                "hindi_answer": "जानकारी उपलब्ध नहीं है।",
                "service_id": service_id,
                "intent": intent
            }
        return {"response": fallback_msg, "service_id": service_id}

    # Call single final synthesis response
    res = await synthesize_final_response(
        rag_query, query_lang, english_query, hindi_query,
        context_en, context_hi, fallback_msg,
        request, service_id, condensed_history=condensed
    )

    # Apply the safeguard fallback override on the final synthesized response
    final_text = res["response"] if isinstance(res, dict) else res
    if is_info_not_available(final_text):
        print(f"[RAG Safe-Guard] Programmatic bypass: Returning language-specific fallback message directly. Original text:\n{final_text}")
        if request.detailed:
            return {
                "response": fallback_msg,
                "query_lang": query_lang,
                "english_query": english_query,
                "hindi_query": hindi_query,
                "context_en": context_en,
                "context_hi": context_hi,
                "english_answer": "I do not have sufficient information or context in my records to answer this question. Please check the Sewa Setu portal.",
                "hindi_answer": "मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी या आवश्यक संदर्भ नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।",
                "service_id": service_id,
                "intent": intent,
                "grounding_status": res.get("grounding_status", "N/A") if isinstance(res, dict) else "N/A"
            }
        return {"response": fallback_msg, "service_id": service_id}

    if request.detailed and isinstance(res, dict):
        res["intent"] = intent
    return res


@app.post("/api/chat")
async def chat_with_bot(request: ChatRequest):
    """
    State-aware Chatbot endpoint coordinating location intent routing and standard RAG execution.
    """
    print("\n" + "=" * 80)
    print("[DEBUG] /api/chat INCOMING REQUEST PAYLOAD:")
    try:
        print(request.model_dump_json(indent=2))
    except Exception as e:
        print(f"Error printing payload: {e}")
    print("=" * 80 + "\n")

    token = llm_trace.set([])
    try:
        # 1. Resolve query
        query = request.query
        if not query and request.messages:
            query = request.messages[-1].content

        # Handle option click query resolution
        if request.is_option_click and request.messages and len(request.messages) >= 3:
            last_msg = query or ""
            if "directly answer" in last_msg.lower() or "सीधे अपने सवाल" in last_msg:
                # Find the original user query before the assistant's option selection
                original_query = request.messages[-3].content
                if original_query:
                    query = original_query
                    print(f"[API Chat] Option click detected. Resolved query to original user question: '{query}'")

        if not query:
            raise HTTPException(status_code=400, detail="Query text is required.")

        query = normalize_query_terms(query)

        # 2. Resolve service_id / sno
        service_id = None
        sno = request.selected_sno or request.service_id
        if sno:
            sno_str = str(sno)
            if sno_str in sno_to_sid:
                service_id = sno_to_sid[sno_str]
            elif sno_str in ["3", "4", "5", "7", "201"]:
                service_id = int(sno_str)

        # Auto-classify query to specific service if not explicitly selected
        if not service_id:
            try:
                classification = classify_service(query, services_list)
                if classification:
                    if classification.get("service_id"):
                        service_id = int(classification["service_id"])
                        print(f"[API Chat] Auto-classified query '{query}' to service_id: {service_id}")
                    else:
                        print(f"[API Chat] Auto-classified query mapped to None")
                        service_id = None
            except Exception as e:
                print(f"[API Chat] Failed to auto-classify service: {e}")

        # Execute standard RAG pipeline directly (location flows removed)
        res = await run_rag_pipeline(query, request, service_id)
        if isinstance(res, dict):
            res["llm_calls_trace"] = llm_trace.get()
        return res
    finally:
        llm_trace.reset(token)


@app.post("/api/search")
async def search_services(request: SearchRequest):
    """
    Service classification mapping matching query to correct serial number 'sno'.
    Uses Sarvam AI to classify.
    """
    query = request.query.strip()
    if not query:
        return {"sno": None, "service_id": None}

    return classify_service(query, services_list)


@app.get("/health")
def health_check():
    """
    Returns API health status.
    """
    return {"status": "ok", "llm": "sarvam"}


@app.post("/api/ingest")
def trigger_ingestion(background_tasks: BackgroundTasks):
    """
    Simplified ingest endpoint.
    """
    return {"message": "Ingestion is already complete and vector database contains 282 chunks."}


@app.post("/api/ingest")
def trigger_ingestion(background_tasks: BackgroundTasks):
    """
    Simplified ingest endpoint.
    """
    return {"message": "Ingestion is already complete and vector database contains 282 chunks."}
