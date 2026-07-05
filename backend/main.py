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
        classify_query_intent
    )
except ImportError:
    from rag import retrieve_context
    from llm_router import (
        generate_answer, 
        classify_service, 
        detect_query_language, 
        translate_query_to_english,
        translate_query_to_hindi,
        classify_query_intent
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


def detect_greeting(query: str) -> Optional[dict]:
    """
    Detects if the query is a greeting/salutation and returns a warm response.
    Returns None if the query is not a greeting.
    Returns {"response": "..."} if it is a greeting.
    """
    q_clean = re.sub(r'[!?.,।\s]+$', '', query.strip().lower())
    
    # Greeting responses by category
    hello_patterns = {
        "hi", "hello", "hey", "hii", "hiii", "helloo", "hellooo",
        "good morning", "good afternoon", "good evening"
    }
    hello_patterns_hi = {"नमस्ते", "नमस्कार", "हेलो", "हाय", "हैलो"}
    hello_patterns_hinglish = {"namaste", "namaskar", "namaskaar", "pranam"}
    
    bye_patterns = {"bye", "byee", "goodbye", "good bye", "see you", "take care", "good night"}
    bye_patterns_hi = {"अलविदा", "बाय"}
    bye_patterns_hinglish = {"alvida"}
    
    thanks_patterns = {"thanks", "thank you", "thankyou", "thank u", "thnx", "thnks", "ty"}
    thanks_patterns_hi = {"धन्यवाद", "शुक्रिया"}
    thanks_patterns_hinglish = {"dhanyavaad", "dhanyawad", "shukriya"}
    
    ok_patterns = {"ok", "okay", "okk", "okkk", "hmm", "hmmm"}
    ok_patterns_hi = {"ठीक है", "ठीक", "जी", "जी हाँ", "हाँ"}
    ok_patterns_hinglish = {"haan", "theek hai", "thik hai", "acha", "accha", "achha"}
    
    # Detect language for response
    is_hindi = any('\u0900' <= c <= '\u097f' for c in query)
    
    if q_clean in hello_patterns:
        return {"response": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service."}
    elif q_clean in hello_patterns_hi:
        return {"response": "नमस्ते! 🙏 सेवासेतु एआई सहायक में आपका स्वागत है। छत्तीसगढ़ सरकारी सेवाओं के बारे में मैं आपकी कैसे मदद कर सकता/सकती हूँ? आप किसी भी सेवा के दस्तावेज़, शुल्क, पात्रता या आवेदन प्रक्रिया के बारे में पूछ सकते हैं।"}
    elif q_clean in hello_patterns_hinglish:
        return {"response": "Namaste! 🙏 SewaSetu AI Assistant mein aapka swagat hai. Chhattisgarh sarkari sewaon ke baare mein main aapki kaise madad kar sakta/sakti hoon? Aap kisi bhi seva ke documents, fees, eligibility ya application process ke baare mein pooch sakte hain."}
    
    elif q_clean in bye_patterns:
        return {"response": "Thank you for using SewaSetu! 🙏 Have a great day. Feel free to come back anytime you need help with government services."}
    elif q_clean in bye_patterns_hi:
        return {"response": "सेवासेतु का उपयोग करने के लिए धन्यवाद! 🙏 आपका दिन शुभ हो। सरकारी सेवाओं में मदद के लिए कभी भी वापस आएं।"}
    elif q_clean in bye_patterns_hinglish:
        return {"response": "SewaSetu use karne ke liye dhanyavaad! 🙏 Aapka din shubh ho. Sarkari sewaon mein madad ke liye kabhi bhi wapas aayein."}
    
    elif q_clean in thanks_patterns:
        return {"response": "You're welcome! 🙏 Is there anything else I can help you with regarding Chhattisgarh government services?"}
    elif q_clean in thanks_patterns_hi:
        return {"response": "आपका स्वागत है! 🙏 क्या छत्तीसगढ़ सरकारी सेवाओं के बारे में कोई और मदद चाहिए?"}
    elif q_clean in thanks_patterns_hinglish:
        return {"response": "Aapka swagat hai! 🙏 Kya Chhattisgarh sarkari sewaon ke baare mein koi aur madad chahiye?"}
    
    elif q_clean in ok_patterns:
        return {"response": "Alright! 👍 Let me know if you have any questions about Chhattisgarh government services."}
    elif q_clean in ok_patterns_hi:
        return {"response": "ठीक है! 👍 छत्तीसगढ़ सरकारी सेवाओं के बारे में कोई सवाल हो तो बताइए।"}
    elif q_clean in ok_patterns_hinglish:
        return {"response": "Theek hai! 👍 Chhattisgarh sarkari sewaon ke baare mein koi sawal ho toh bataiye."}
    
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


def build_condensed_history(sanitized_history: list, is_follow_up: bool, topic_summary: str = "") -> list:
    """
    Builds a condensed history for the final synthesis stage only.
    
    - For follow-ups: includes last 2 turns + a topic summary line
    - For new topics: returns empty (no history needed)
    """
    if not is_follow_up or not sanitized_history:
        return []
    
    # Take only the last 4 messages (2 turns)
    recent = sanitized_history[-4:]
    
    condensed = []
    if topic_summary:
        condensed.append({
            "role": "system",
            "content": f"Previous conversation context: {topic_summary}"
        })
    
    for msg in recent:
        content = msg["content"]
        # Truncate long assistant responses to keep context focused
        if msg["role"] == "assistant" and len(content) > 400:
            content = content[:400] + "\n... (truncated for brevity)"
        condensed.append({"role": msg["role"], "content": content})
    
    return condensed


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
    Detects language and translates to English & Hindi concurrently.
    """
    lang_task = asyncio.to_thread(detect_query_language, query)
    en_task = asyncio.to_thread(translate_query_to_english, query)
    hi_task = asyncio.to_thread(translate_query_to_hindi, query)
    
    query_lang, english_query, hindi_query = await asyncio.gather(lang_task, en_task, hi_task)
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
    Runs language processing, context retrieval, and intermediate response generation (async).
    """
    query = normalize_query_terms(query)
    if not query_lang or not english_query or not hindi_query:
        query_lang, english_query, hindi_query = await process_query_languages(query)

    if service_id is None:
        if query_lang == "en":
            fallback_msg = "Information not available."
        elif query_lang == "hi":
            fallback_msg = "जानकारी उपलब्ध नहीं है।"
        else:
            fallback_msg = "Jaankari uplabhd nahi hai."
        return query_lang, english_query, hindi_query, "", "", "Information not available.", "जानकारी उपलब्ध नहीं है।", fallback_msg

    # Retrieve English and Hindi contexts concurrently
    context_en_task = asyncio.to_thread(retrieve_context, query, service_id, 6, english_query, hindi_query, "en")
    context_hi_task = asyncio.to_thread(retrieve_context, query, service_id, 6, english_query, hindi_query, "hi")
    (context_en, metadata_en, checklist_text_en), (context_hi, metadata_hi, checklist_text_hi) = await asyncio.gather(context_en_task, context_hi_task)

    if query_lang == "en":
        fallback_msg = "Information not available."
    elif query_lang == "hi":
        fallback_msg = "जानकारी उपलब्ध नहीं है।"
    else:
        fallback_msg = "Jaankari uplabhd nahi hai."

    if not context_en and not context_hi:
        return query_lang, english_query, hindi_query, "", "", "Information not available.", "जानकारी उपलब्ध नहीं है।", fallback_msg

    # NOTE: NO history is passed to intermediate calls.
    # History is only used in the final synthesis stage (condensed form).
    # This prevents the triple-amplification problem.

    # Build dynamic service-specific rules
    service_rules_en = ""
    service_rules_hi = ""
    if service_id is not None:
        if int(service_id) == 7:
            service_rules_en = (
                "- ELIGIBILITY (Domicile): If the citizen asks about eligibility or exceptions for Domicile Certificate, explain the rules strictly according to the context:\n"
                "  1. Main Path (Both Criteria One AND Criteria Two must be met): The applicant must satisfy AT LEAST ONE option from Criteria One (Criteria A) AND AT LEAST ONE option from Criteria Two (Criteria B). You MUST list Criteria One and Criteria Two under separate, clearly-labeled headers or bullet points.\n"
                "     * Criteria One (Criteria A) options: Birth in CG, parent resident for 25 years, parent is CG Government/PSU employee, or property in CG for 5 years.\n"
                "     * Criteria Two (Criteria B) options: 3 years of school study in CG, or passing Class 5, 8, 10, 12 board exam from CG.\n"
                "     * Never merge them into one list and never omit the education requirements of Criteria Two.\n"
                "  2. Exceptions (Criteria Three / Criteria C): If they do not meet the Main Path (for example, if they lack 'Proof of 15 Years Stay' or did not study in CG), they are still eligible under the exceptions of Criteria Three (C). Under Criteria Three (C), Criteria A and B are NOT required. The exceptions are: (a) spouse is a domicile of CG, (b) applicant or spouse is a CG Government/PSU employee, or (c) applicant or parent is in All India Services and allotted CG Cadre.\n"
                "  3. Clarity: Do NOT say that Criteria Three requires stay proof or education. Clearly explain that Criteria Three is a standalone set of exceptions that bypasses the need for the stay proof or CG education requirements of Criteria One and Two.\n"
                "  Do NOT assume ineligibility if there is ANY criterion in the context that could apply to the citizen's situation. Present all relevant criteria to the citizen.\n"
            )
            service_rules_hi = (
                "- पात्रता (Domicile Eligibility): यदि नागरिक मूल निवासी प्रमाण पत्र (Domicile) के लिए पात्रता या अपवादों के बारे में पूछता है, तो संदर्भ के आधार पर सख्ती से समझाएं:\n"
                "  1. मुख्य मार्ग (Main Path): आवेदक को Criteria One (जिसे Criteria A भी कहा जाता है) से कम से कम एक विकल्प और Criteria Two (जिसे Criteria B भी कहा जाता है) से कम से कम एक विकल्प दोनों को पूरा करना होगा। आपको Criteria One और Criteria Two को अलग-अलग शीर्षकों (headers) या बुलेट पॉइंट्स के तहत सूचीबद्ध करना होगा।\n"
                "     * Criteria One (Criteria A) के विकल्प: छत्तीसगढ़ में जन्म, माता-पिता का 25 वर्ष का निवास, माता-पिता का सरकारी/PSU कर्मचारी होना, या 5 वर्ष की संपत्ति होना।\n"
                "     * Criteria Two (Criteria B) के विकल्प: CG में 3 वर्ष की स्कूल शिक्षा, या CG से 5वीं, 8वीं, 10वीं, 12वीं की बोर्ड परीक्षा उत्तीर्ण होना।\n"
                "     * इन्हें कभी भी एक सूची में न मिलाएँ और Criteria Two (शिक्षा की आवश्यकता) के विकल्पों को कभी न छोड़ें।\n"
                "  2. अपवाद (Criteria Three / Criteria C): यदि वे मुख्य मार्ग को पूरा नहीं करते हैं (उदाहरण के लिए, यदि उनके पास 15 वर्ष का निवास प्रमाण नहीं है या CG में पढ़ाई नहीं की है), तो भी वे Criteria Three (C) के अपवादों के तहत पात्र हैं। Criteria Three (C) के लिए Criteria A और B की आवश्यकता नहीं होती है। ये अपवाद हैं: (क) जीवनसाथी (spouse) छत्तीसगढ़ का मूल निवासी हो, (ख) आवेदक या जीवनसाथी छत्तीसगढ़ सरकार/PSU का कर्मचारी हो, या (ग) आवेदक या माता-पिता अखिल भारतीय सेवाओं (All India Services) में हों और उन्हें CG कैडर आवंटित किया गया हो।\n"
                "  3. स्पष्टता: कभी भी यह न कहें कि Criteria Three के लिए निवास प्रमाण या शिक्षा की आवश्यकता है। स्पष्ट रूप से समझाएं कि Criteria Three एक स्वतंत्र अपवाद है जो Criteria One और Two (निवास प्रमाण और शिक्षा) की आवश्यकता को समाप्त करता है।\n"
                "  यदि संदर्भ में कोई भी मानदंड नागरिक की स्थिति पर लागू हो सकता है, तो अपात्रता न मानें।\n"
            )
        elif int(service_id) == 3:
            service_rules_en = (
                "- MARRIAGE JURISDICTION: For Marriage registration queries, always clarify that a marriage must be registered in the local area where it was solemnized/performed (not in the couple's hometown or place of residence), and with the appropriate local authority of that area (Gram Panchayat if rural; Municipality/Municipal Corporation if urban).\n"
            )
            service_rules_hi = (
                "- विवाह पंजीकरण क्षेत्र: विवाह पंजीकरण के प्रश्नों के लिए हमेशा स्पष्ट करें कि विवाह का पंजीकरण उसी स्थानीय क्षेत्र में होना चाहिए जहां वह संपन्न हुआ है (न कि वर-वधू के गृहनगर या निवास स्थान पर), और उसी क्षेत्र के उपयुक्त स्थानीय निकाय (ग्रामीण के लिए ग्राम पंचायत; शहरी के लिए नगर पालिका/नगर निगम) में होना चाहिए।\n"
            )

    # Generate Intermediate English Answer — NO HISTORY, only RAG context + query
    messages_en = [
        {
            "role": "system",
            "content": (
                "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY):\n"
                "Your ENTIRE response must address ONLY the specific question asked. Do NOT add ANY extra information.\n"
                "- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n"
                "- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n"
                "- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n"
                "- If asked about timeline/SLA → respond ONLY with the timeline. Do NOT mention anything else.\n"
                "- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n"
                "Adding unrequested information is STRICTLY FORBIDDEN.\n\n"
                "You are a polite government services assistant for the Sewa Setu Chhattisgarh portal.\n"
                "Answer using ONLY the provided context. Output ENTIRELY in English (Roman alphabet only).\n"
                "Be warm and respectful. Use markdown formatting with bullet points.\n"
                f"{service_rules_en}"
                "DOCUMENT RULES: Determine mandatory/optional status ONLY from 'REQUIRED DOCUMENTS' list. "
                "If a document is '(Mandatory: Yes)' with no alternatives, clearly state it cannot be bypassed.\n"
                "FEE INTERPRETATION RULE: When the context mentions 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee', these are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. "
                "The total application fee is the fee for ONE method, not both added together. "
                "If the citizen asks about total cost and the required documents mention any monetary costs (like challans, stamp paper fees, notarization fees), mention those as additional costs on top of the application fee.\n\n"
                f"--- RETRIEVED CONTEXT (ENGLISH) ---\n{context_en}\n--- END CONTEXT ---"
            )
        }
    ]
    # NO history appended — intermediate calls use only context + query
    messages_en.append({
        "role": "user",
        "content": f"{english_query}\n\nIMPORTANT: Output your response ENTIRELY in English. Do NOT write in Devanagari script (Hindi characters) and do NOT use Hinglish. Every single word must be standard English using only Latin letters."
    })

    # Generate Intermediate Hindi Answer — NO HISTORY, only RAG context + query
    messages_hi = [
        {
            "role": "system",
            "content": (
                "सख्त उत्तर-मात्र नियम (सर्वोच्च प्राथमिकता):\n"
                "आपका पूरा उत्तर केवल पूछे गए प्रश्न का ही होना चाहिए। कोई भी अतिरिक्त जानकारी न जोड़ें।\n"
                "- शुल्क पूछा गया → केवल शुल्क बताएं। दस्तावेज, पात्रता, प्रक्रिया या समयसीमा न जोड़ें।\n"
                "- पात्रता पूछी गई → केवल पात्रता बताएं। दस्तावेज, शुल्क, प्रक्रिया या समयसीमा न जोड़ें।\n"
                "- दस्तावेज पूछे गए → केवल दस्तावेज बताएं। पात्रता, शुल्क, प्रक्रिया या समयसीमा न जोड़ें।\n"
                "- एक विशिष्ट दस्तावेज पूछा गया → केवल उसी दस्तावेज के बारे में बताएं। पूरी सूची न दें।\n"
                "अनावश्यक जानकारी जोड़ना सख्त वर्जित है।\n\n"
                "आप सेवा सेतु छत्तीसगढ़ पोर्टल के सहायक हैं।\n"
                "केवल संदर्भ की जानकारी से उत्तर दें। देवनागरी लिपि में उत्तर दें।\n"
                "विनम्र रहें। मार्कडाउन और बुलेट पॉइंट का उपयोग करें।\n"
                f"{service_rules_hi}"
                "दस्तावेज नियम: अनिवार्यता केवल 'आवश्यक दस्तावेज' सूची से निर्धारित करें।\n"
                "शुल्क व्याख्या नियम: जब संदर्भ में 'ऑनलाइन शुल्क/पोर्टल शुल्क' और 'कियोस्क शुल्क/केंद्र शुल्क' दोनों हों, तो ये वैकल्पिक भुगतान विधियां हैं (ऑनलाइन या कियोस्क पर), संचयी नहीं। "
                "कुल आवेदन शुल्क एक विधि का शुल्क है, दोनों का जोड़ नहीं। "
                "यदि नागरिक कुल लागत पूछे और आवश्यक दस्तावेजों में कोई मौद्रिक लागत (जैसे चालान, स्टांप पेपर, नोटरी शुल्क) हो, तो उन्हें अतिरिक्त लागत के रूप में बताएं।\n\n"
                f"--- RETRIEVED CONTEXT (HINDI) ---\n{context_hi}\n--- END CONTEXT ---"
            )
        }
    ]
    # NO history appended — intermediate calls use only context + query
    messages_hi.append({
        "role": "user",
        "content": f"{hindi_query}\n\nIMPORTANT: Output your response ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि). Do NOT write in English or use Roman alphabet/Latin characters. Every single word must be Devanagari."
    })

    # Generate answers concurrently
    ans_en_task = asyncio.to_thread(generate_answer, messages_en)
    ans_hi_task = asyncio.to_thread(generate_answer, messages_hi)
    english_answer, hindi_answer = await asyncio.gather(ans_en_task, ans_hi_task)

    return query_lang, english_query, hindi_query, context_en, context_hi, english_answer, hindi_answer, fallback_msg

async def synthesize_consensus_response(
    query: str,
    query_lang: str,
    english_query: str,
    hindi_query: str,
    context_en: str,
    context_hi: str,
    english_answer: str,
    hindi_answer: str,
    fallback_msg: str,
    request: ChatRequest,
    service_id: Optional[int],
    condensed_history: Optional[list] = None
):
    """
    Synthesizes consensus response and post-processes URLs (async).
    Uses condensed history (last 2 turns only) instead of full raw history.
    """

    # Consensus Synthesis to generate final response in the target language
    if query_lang == "en":
        lang_label = "English"
        lang_instruction = (
            "You MUST respond ENTIRELY in English using only the Roman alphabet. "
            "Do NOT write in Devanagari script (Hindi characters) and do NOT use Hinglish words. "
            "Every single word must be standard English."
        )
        if english_answer and re.search(r'[\u0900-\u097f]', english_answer) and english_answer.strip() not in ["जानकारी उपलब्ध नहीं है।", "Information not available."]:
            try:
                english_answer = await asyncio.to_thread(translate_query_to_english, english_answer)
            except:
                pass

        if hindi_answer and hindi_answer.strip() not in ["जानकारी उपलब्ध नहीं है।", "Information not available."]:
            try:
                translated_hindi_answer = await asyncio.to_thread(translate_query_to_english, hindi_answer)
            except:
                translated_hindi_answer = "Information not available."
        else:
            translated_hindi_answer = "Information not available."

        rag_context = f"Reference Context Details:\n- {english_answer}\n- {translated_hindi_answer}"

    elif query_lang == "hi":
        lang_label = "Hindi"
        lang_instruction = (
            "You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n"
            "- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n"
            "- Every single word must be written in Devanagari.\n"
            "- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
        )
        if hindi_answer and not re.search(r'[\u0900-\u097f]', hindi_answer) and hindi_answer.strip() not in ["Information not available.", "जानकारी उपलब्ध नहीं है।"]:
            try:
                hindi_answer = await asyncio.to_thread(translate_query_to_hindi, hindi_answer)
            except:
                pass

        if english_answer and english_answer.strip() not in ["Information not available.", "जानकारी उपलब्ध नहीं है।"]:
            try:
                translated_english_answer = await asyncio.to_thread(translate_query_to_hindi, english_answer)
            except:
                translated_english_answer = "जानकारी उपलब्ध नहीं है।"
        else:
            translated_english_answer = "जानकारी उपलब्ध नहीं है।"

        rag_context = f"Reference Context Details:\n- {translated_english_answer}\n- {hindi_answer}"

    else:  # hinglish
        lang_label = "Hinglish"
        lang_instruction = (
            "You MUST respond ENTIRELY in Hinglish — that is, Hindi language written ONLY in Roman/Latin alphabet script. "
            "ABSOLUTELY NO Devanagari characters (क, ख, ग, है, हैं, क्या, आप, जी, etc.) are allowed anywhere in your response. "
            "Every single character must be a Latin letter (a-z, A-Z), number, or standard punctuation. "
            "Write Hindi words in Roman script. For example: 'Haan', 'Nahi', 'Aap', 'Kya', 'Zaroor', 'Domicile certificate', 'Sarkari naukri'. "
            "Do NOT write in pure formal English either — use natural conversational Hinglish as spoken in India. "
            "If you accidentally write even one Devanagari character, your response will be rejected."
        )
        if english_answer and re.search(r'[\u0900-\u097f]', english_answer) and english_answer.strip() not in ["जानकारी उपलब्ध नहीं है।", "Information not available."]:
            try:
                english_answer = await asyncio.to_thread(translate_query_to_english, english_answer)
            except:
                pass

        if hindi_answer and hindi_answer.strip() not in ["जानकारी उपलब्ध नहीं है।", "Information not available."]:
            try:
                translated_hindi_answer = await asyncio.to_thread(translate_query_to_english, hindi_answer)
            except:
                translated_hindi_answer = "Information not available."
        else:
            translated_hindi_answer = "Information not available."

        rag_context = f"Reference Context Details:\n- {english_answer}\n- {translated_hindi_answer}"

    # Build dynamic service-specific rules for final synthesis
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

    system_instruction = f"""STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):
Your ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.
- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.
- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.
- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.
- If asked about timeline/SLA → respond ONLY with the timeline. Do NOT mention anything else.
- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.
- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.
- A short, precise, focused answer is ALWAYS better than a long one.

You are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.
- LANGUAGE AND SCRIPT RULES: {lang_instruction}
- Be warm, respectful, and citizen-friendly.
{service_rules_final}
- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.
- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.
- RAG CONTEXT is the ONLY source of truth. Ignore any contradictions in conversation history.

FORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.

CRITICAL: Never mention 'RAG', 'First Answer', 'Second Answer', 'Reference Context Details', or the synthesis process.

RAG CONTEXT:
{rag_context}
"""

    messages_final = [{"role": "system", "content": system_instruction}]
    # Use CONDENSED history only (last 2 turns), not full raw history
    if condensed_history:
        for msg in condensed_history:
            messages_final.append({"role": msg["role"], "content": msg["content"]})
    messages_final.append({"role": "user", "content": f"{query}\n\nIMPORTANT: You MUST respond ENTIRELY in {lang_label}. {lang_instruction}"})

    final_reply = await asyncio.to_thread(generate_answer, messages_final)

    # Post-processing: Devanagari leakage safety net for Hinglish responses
    if query_lang == "hinglish" and re.search(r'[\u0900-\u097f]', final_reply):
        print("[Synthesis] WARNING: Hinglish response contains Devanagari characters. Re-converting to Roman script...")
        try:
            romanize_prompt = (
                "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. "
                "Replace ALL Devanagari characters with their Roman transliteration. "
                "Keep English words as-is. Keep the meaning and structure exactly the same. "
                "Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\n"
                f"Text to convert:\n{final_reply}\n\nRoman script output:"
            )
            romanized = await asyncio.to_thread(
                generate_answer, [{"role": "user", "content": romanize_prompt}]
            )
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
            "english_answer": english_answer,
            "hindi_answer": hindi_answer,
            "service_id": service_id
        }
    return {"response": final_reply}


async def run_rag_pipeline(query: str, request: ChatRequest, service_id: Optional[int]):
    """
    Consolidated RAG execution and response synthesis pipeline (Async).
    """
    query = normalize_query_terms(query)
    query_lang, english_query, hindi_query = await process_query_languages(query)

    service_name = "Chhattisgarh Citizen Service"
    if service_id:
        for s in services_list:
            if str(s["service_id"]) == str(service_id):
                service_name = s["name_en"]
                break

    # 1. Deterministic choice prompt for eligibility or document queries
    if request.interactive and service_id and not request.is_option_click and is_eligibility_or_document_query(query, english_query, hindi_query):
        if query_lang == "hi":
            default_text = "क्या आप दस्तावेज़ चेकलिस्ट का उपयोग करके अपनी पात्रता जांचना चाहते हैं, या विस्तृत पात्रता मानदंडों की जानकारी देखना चाहते हैं, या सीधे अपने प्रश्न का उत्तर चाहते हैं?"
            options = [
                {
                    "label": "📋 दस्तावेज़ चेकलिस्ट द्वारा पात्रता जांचें",
                    "query": f"Show required documents checklist for {service_name}"
                },
                {
                    "label": "ℹ️ विस्तृत पात्रता मानदंड और नियम देखें",
                    "query": f"Explain all criteria and eligibility rules for {service_name}"
                },
                {
                    "label": "💬 सीधे मेरे सवाल का जवाब पाएं",
                    "query": query
                }
            ]
        elif query_lang == "hinglish":
            default_text = "Kya aap document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?"
            options = [
                {
                    "label": "📋 Check Eligibility via Document Checklist",
                    "query": f"Show required documents checklist for {service_name}"
                },
                {
                    "label": "ℹ️ Explain Detailed Eligibility & Criteria Rules",
                    "query": f"Explain all criteria and eligibility rules for {service_name}"
                },
                {
                    "label": "💬 Directly Answer My Question",
                    "query": query
                }
            ]
        else:
            default_text = "Would you like to check your eligibility using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?"
            options = [
                {
                    "label": "📋 Check Eligibility via Document Checklist",
                    "query": f"Show required documents checklist for {service_name}"
                },
                {
                    "label": "ℹ️ Explain Detailed Eligibility & Criteria Rules",
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

    # 3. Standard RAG execution
    # === INTENT CLASSIFICATION + QUERY RESOLUTION ===
    # Sanitize history: remove null/empty/special-type messages
    raw_history = request.conversation_history or []
    if not raw_history and request.messages:
        raw_history = request.messages[:-1]
    sanitized = sanitize_history(raw_history)

    # Filter out greeting exchanges from history (they're not service context)
    greeting_words = {"hi", "hello", "hey", "hii", "hiii", "namaste", "namaskar", "bye", "thanks", "thank you", "ok", "okay", "haan", "theek hai"}
    filtered_sanitized = []
    skip_next = False
    for i, msg in enumerate(sanitized):
        if skip_next:
            skip_next = False
            continue
        if msg["role"] == "user" and msg["content"].strip().lower() in greeting_words:
            # Skip this user greeting AND the next assistant response
            skip_next = True
            continue
        filtered_sanitized.append(msg)
    sanitized = filtered_sanitized

    # Classify query intent: greeting/follow_up/new_topic
    intent_result = await asyncio.to_thread(
        classify_query_intent, query, sanitized
    )
    intent = intent_result["intent"]
    resolved_query = intent_result["resolved_query"]
    topic_summary = intent_result["topic_summary"]
    
    print(f"[RAG Pipeline] Intent: {intent}, Resolved query: '{resolved_query}', Topic: '{topic_summary}'")

    # Always use resolved_query for RAG retrieval — the classifier now produces
    # a self-contained query for BOTH intents (with aspect carry-over for new_topic)
    rag_query = resolved_query
    is_follow_up = (intent == "follow_up")

    # SAFETY CHECK: Detect misclassified topic switches
    # If the classifier says follow_up but the topic_summary mentions "different service",
    # force-clear history to prevent cross-service contamination
    if is_follow_up and topic_summary:
        topic_lower = topic_summary.lower()
        if any(phrase in topic_lower for phrase in ["different service", "new service", "another service", "different topic"]):
            print(f"[RAG Pipeline] SAFETY: Classifier said follow_up but topic indicates topic switch. Forcing new_topic.")
            is_follow_up = False
            intent = "new_topic"

    # Build condensed history for final synthesis only
    condensed = build_condensed_history(sanitized, is_follow_up, topic_summary)

    # If resolved query differs from original, re-translate for better RAG retrieval
    # e.g., original "and what about marriage?" → resolved "What are the fees for marriage registration?"
    # Without re-translation, RAG would search for vague "what about marriage?" and get ALL chunks
    if rag_query.lower().strip() != query.lower().strip():
        print(f"[RAG Pipeline] Re-translating resolved query for RAG: '{rag_query}'")
        query_lang, english_query, hindi_query = await process_query_languages(rag_query)

    # Use the resolved query + re-translated languages for RAG retrieval
    query_lang, english_query, hindi_query, context_en, context_hi, english_answer, hindi_answer, fallback_msg = await run_rag_pipeline_intermediates(
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
                "english_answer": english_answer,
                "hindi_answer": hindi_answer,
                "service_id": service_id
            }
        return {"response": fallback_msg}
            
    return await synthesize_consensus_response(
        query, query_lang, english_query, hindi_query,
        context_en, context_hi, english_answer, hindi_answer, fallback_msg,
        request, service_id, condensed_history=condensed
    )


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

    # 1. Resolve query
    query = request.query
    if not query and request.messages:
        query = request.messages[-1].content

    if not query:
        raise HTTPException(status_code=400, detail="Query text is required.")

    query = normalize_query_terms(query)

    # === GREETING INTERCEPTOR (before any LLM/RAG calls) ===
    greeting_result = detect_greeting(query)
    if greeting_result:
        print(f"[API Chat] Greeting detected: '{query}' -> responding with canned greeting")
        return {"response": greeting_result["response"]}

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
            if classification and classification.get("service_id"):
                service_id = int(classification["service_id"])
                print(f"[API Chat] Auto-classified query '{query}' to service_id: {service_id}")
        except Exception as e:
            print(f"[API Chat] Failed to auto-classify service: {e}")

    # Execute standard RAG pipeline directly (location flows removed)
    return await run_rag_pipeline(query, request, service_id)


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
