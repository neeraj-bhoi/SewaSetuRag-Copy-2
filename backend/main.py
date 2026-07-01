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
        translate_query_to_hindi
    )
except ImportError:
    from rag import retrieve_context
    from llm_router import (
        generate_answer, 
        classify_service, 
        detect_query_language, 
        translate_query_to_english,
        translate_query_to_hindi
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


# Pydantic schemas
class Message(BaseModel):
    role: str  # 'user', 'assistant' or 'system'
    content: str

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


async def run_rag_pipeline_intermediates(query: str, request: ChatRequest, service_id: Optional[int]):
    """
    Runs language processing, context retrieval, and intermediate response generation (async).
    """
    query = normalize_query_terms(query)
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
    (context_en, metadata_en), (context_hi, metadata_hi) = await asyncio.gather(context_en_task, context_hi_task)

    if query_lang == "en":
        fallback_msg = "Information not available."
    elif query_lang == "hi":
        fallback_msg = "जानकारी उपलब्ध नहीं है।"
    else:
        fallback_msg = "Jaankari uplabhd nahi hai."

    if not context_en and not context_hi:
        return query_lang, english_query, hindi_query, "", "", "Information not available.", "जानकारी उपलब्ध नहीं है।", fallback_msg

    # Resolve history
    history = request.conversation_history
    if not history and request.messages:
        history = request.messages[:-1]

    # Generate Intermediate English Answer
    messages_en = [
        {
            "role": "system",
            "content": (
                "You are a helpful, polite, and empathetic government services assistant for the Sewa Setu Chhattisgarh portal.\n"
                "Answer the citizen's question using ONLY the provided English context.\n"
                "Output your response ENTIRELY in English using only the Roman alphabet.\n\n"
                "TONE AND CONDUCT RULES:\n"
                "- Always be warm, respectful, and encouraging. You represent a government portal serving citizens.\n"
                "- NEVER use harsh, dismissive, or discouraging language. Even when a citizen may not be eligible, guide them gently and highlight any alternative paths or exceptions that may apply.\n"
                "- Use phrases like 'You may be eligible if...', 'Based on the rules, here is what applies to your situation...', 'Please note that...' instead of blunt refusals.\n\n"
                "CONCISENESS RULES:\n"
                "- Answer ONLY what the citizen asked. Do NOT volunteer extra information they did not request.\n"
                "- If the citizen asks about eligibility, answer ONLY about eligibility. Do NOT add document lists, fees, timelines, or application process unless explicitly asked.\n"
                "- If the citizen asks about documents, answer ONLY about documents. Do NOT add eligibility criteria, fees, or process steps.\n"
                "- If the citizen asks a specific question about a single document (e.g., whether a specific document is mandatory/optional, or how to get it), answer ONLY that specific question about that single document. Do NOT output or dump the entire list of required documents or other unrelated documents.\n"
                "- Keep your response focused and concise. A short, precise answer is always better than a long, unfocused one.\n\n"
                "FORMATTING RULES:\n"
                "- You MUST structure your answer using clean markdown, bold text highlights, and lists (bullet points or numbered lists).\n"
                "- Avoid large, cluttered paragraphs of block text. Split your response into clear, logical sections with headings and line breaks.\n"
                "- Even for short answers, organize the key takeaways into bullet points to ensure it is visually appealing, spaced out, and scan-friendly for the citizen.\n\n"
                "STRICT FACTUAL GROUNDING:\n"
                "- Read the context very carefully. Base your answer ONLY on what is stated in the context.\n"
                "- ELIGIBILITY: If the context contains eligibility criteria, rules, or conditions, read ALL of them thoroughly before answering. "
                "Pay special attention to alternative criteria, exceptions, and special cases. "
                "For Domicile eligibility, note that: Criteria One (A) and Criteria Two (B) must BOTH be met to get the certificate. Criteria Three (C) is a standalone alternative set of conditions (if Criteria Three is met, Criteria One and Two are NOT required). Thus, eligibility is achieved by: (Criteria One AND Criteria Two) OR (Criteria Three). Do NOT state that all three are required. "
                "Do NOT assume ineligibility if there is ANY criterion in the context that could apply to the citizen's situation. Present all relevant criteria to the citizen.\n"
                "- MARRIAGE JURISDICTION: For Marriage registration queries, always clarify that a marriage must be registered in the local area where it was solemnized/performed (not in the couple's hometown or place of residence), and with the appropriate local authority of that area (Gram Panchayat if rural; Municipality/Municipal Corporation if urban).\n"
                "- DOCUMENTS: Determine the mandatory or optional status of any document ONLY from the 'REQUIRED DOCUMENTS' list in the context. "
                "Do NOT infer mandatory status from User Manual text, official notification pages, or form guidelines. "
                "If a document is listed with '(Mandatory: No)' or '(Mandatory: नहीं)', it is optional.\n\n"
                f"--- RETRIEVED CONTEXT (ENGLISH) ---\n{context_en}\n--- END CONTEXT ---"
            )
        }
    ]
    if history:
        for msg in history:
            messages_en.append({"role": msg.role, "content": msg.content})
    messages_en.append({
        "role": "user",
        "content": f"{english_query}\n\nIMPORTANT: Output your response ENTIRELY in English. Do NOT write in Devanagari script (Hindi characters) and do NOT use Hinglish. Every single word must be standard English using only Latin letters."
    })

    # Generate Intermediate Hindi Answer Messages (defined here to run in parallel)
    messages_hi = [
        {
            "role": "system",
            "content": (
                "You are a helpful, polite, and empathetic government services assistant for the Sewa Setu Chhattisgarh portal.\n"
                "Answer the citizen's question using ONLY the provided Hindi context.\n"
                "Output your response ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n\n"
                "स्वर और आचरण नियम:\n"
                "- हमेशा विनम्र, सम्मानजनक और सहानुभूतिपूर्ण रहें। आप एक सरकारी पोर्टल का प्रतिनिधित्व करते हैं।\n"
                "- कभी भी कठोर, अपमानजनक या हतोत्साहित करने वाली भाषा का प्रयोग न करें। यदि नागरिक पात्र नहीं भी हो, तो भी उन्हें सौम्यता से मार्गदर्शन दें और कोई भी वैकल्पिक रास्ता या अपवाद बताएं।\n\n"
                "संक्षिप्तता नियम:\n"
                "- केवल वही उत्तर दें जो नागरिक ने पूछा है। अतिरिक्त जानकारी स्वयं से न जोड़ें।\n"
                "- यदि नागरिक पात्रता के बारे में पूछे, तो केवल पात्रता का उत्तर दें। दस्तावेज सूची, शुल्क, समयसीमा या आवेदन प्रक्रिया न जोड़ें जब तक स्पष्ट रूप से न पूछा जाए।\n"
                "- यदि नागरिक दस्तावेजों के बारे में पूछे, तो केवल दस्तावेजों का उत्तर दें।\n"
                "- यदि नागरिक किसी एक दस्तावेज के बारे में विशिष्ट प्रश्न पूछता है (जैसे कि क्या कोई विशिष्ट दस्तावेज अनिवार्य/वैकल्पिक है, या इसे कैसे प्राप्त करें), तो केवल उसी विशिष्ट दस्तावेज के बारे में उत्तर दें। सभी आवश्यक दस्तावेजों या असंबंधित दस्तावेजों की पूरी सूची प्रदर्शित न करें।\n"
                "- संक्षिप्त और सटीक उत्तर हमेशा लंबे और बिखरे उत्तर से बेहतर है।\n\n"
                "प्रारूपण नियम (FORMATTING RULES):\n"
                "- आपको अपने उत्तर को स्पष्ट मार्कडाउन, बोल्ड टेक्स्ट हाइलाइट्स और सूचियों (बुलेट पॉइंट या नंबर सूची) का उपयोग करके व्यवस्थित करना होगा।\n"
                "- बड़े, अव्यवस्थित पैराग्राफ से बचें। अपने उत्तर को स्पष्ट शीर्षकों और लाइन ब्रेक के साथ तार्किक भागों में विभाजित करें।\n"
                "- छोटे उत्तरों के लिए भी, मुख्य बातों को बुलेट पॉइंट में व्यवस्थित करें ताकि यह नागरिक के लिए पढ़ने में आसान और आकर्षक लगे।\n\n"
                "सख्त तथ्यात्मक आधार:\n"
                "- संदर्भ को बहुत ध्यान से पढ़ें। अपना उत्तर केवल संदर्भ में दी गई जानकारी पर आधारित करें।\n"
                "- पात्रता: यदि संदर्भ में पात्रता मानदंड, नियम या शर्तें हैं, तो उत्तर देने से पहले सभी को अच्छी तरह पढ़ें। "
                "वैकल्पिक मानदंडों, अपवादों और विशेष मामलों पर विशेष ध्यान दें। "
                "छत्तीसगढ़ मूल निवासी (Domicile) पात्रता के लिए, ध्यान दें: Criteria One (A) और Criteria Two (B) दोनों का पूरा होना अनिवार्य है। Criteria Three (C) एक वैकल्पिक (alternative) स्वतंत्र नियम है (यदि Criteria Three पूरा होता है, तो Criteria One और Two की आवश्यकता नहीं है)। इसलिए, पात्रता या तो (Criteria One AND Criteria Two) से या फिर (Criteria Three) से मिलती है। कभी भी यह न कहें कि तीनों मानदंडों को पूरा करना अनिवार्य है। "
                "यदि संदर्भ में कोई भी मानदंड नागरिक की स्थिति पर लागू हो सकता है, तो अपात्रता न मानें।\n"
                "- विवाह पंजीकरण क्षेत्र: विवाह पंजीकरण के प्रश्नों के लिए हमेशा स्पष्ट करें कि विवाह का पंजीकरण उसी स्थानीय क्षेत्र में होना चाहिए जहां वह संपन्न हुआ है (न कि वर-वधू के गृहनगर या निवास स्थान पर), और उसी क्षेत्र के उपयुक्त स्थानीय निकाय (ग्रामीण के लिए ग्राम पंचायत; शहरी के लिए नगर पालिका/नगर निगम) में होना चाहिए।\n"
                "- दस्तावेज: किसी भी दस्तावेज की अनिवार्यता का निर्धारण केवल 'REQUIRED DOCUMENTS' या 'आवश्यक दस्तावेज' सूची से करें। "
                "यदि कोई दस्तावेज '(Mandatory: नहीं)' या '(Mandatory: No)' के साथ सूचीबद्ध है, तो वह वैकल्पिक है।\n\n"
                f"--- RETRIEVED CONTEXT (HINDI) ---\n{context_hi}\n--- END CONTEXT ---"
            )
        }
    ]
    if history:
        for msg in history:
            messages_hi.append({"role": msg.role, "content": msg.content})
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
    service_id: Optional[int]
):
    """
    Synthesizes consensus response and post-processes URLs (async).
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

    system_instruction = f"""You are SewaSetu AI Assistant — a polite, helpful, and empathetic government services assistant for the Chhattisgarh Sewa Setu portal.
Synthesize the provided information into a unified and consistent final response.
- LANGUAGE AND SCRIPT RULES: {lang_instruction}

TONE RULES:
- Always be warm, respectful, and citizen-friendly. You represent an official government portal.
- NEVER use harsh, dismissive, blunt, or discouraging language.
- When a citizen asks about eligibility, present ALL applicable criteria and exceptions from the context before drawing conclusions. If there is ANY criterion that could make them eligible, highlight it clearly and encouragingly.
- ELIGIBILITY LOGIC RULE (Domicile): For Chhattisgarh Domicile Certificate eligibility, note that: Criteria One (A) and Criteria Two (B) must BOTH be met. Criteria Three (C) is a standalone alternative set of conditions (if Criteria Three is met, Criteria One and Two are NOT required). Thus, eligibility is achieved by: (Criteria One AND Criteria Two) OR (Criteria Three). Do NOT state that all three are required.
- MARRIAGE JURISDICTION RULE: Under the Chhattisgarh Compulsory Registration of Marriages Rules, a marriage MUST be registered in the local area where the marriage was solemnized or performed, NOT at the couple's hometown or place of residence. The registrar is the Local Authority of that local area (Gram Panchayat if rural; Municipality or Municipal Corporation if urban). State this clearly when citizens ask where or under which office/authority to register their marriage.
- Use supportive phrases like "Based on the rules, you may be eligible because...", "Please note this helpful provision...", "Here is what applies to your situation..." instead of flat refusals.

CONCISENESS RULES:
- Answer ONLY what the citizen asked. Do NOT volunteer extra information they did not request.
- If the citizen asks about eligibility, answer ONLY about eligibility. Do NOT add document lists, fees, timelines, or application process unless explicitly asked.
- If the citizen asks about documents, answer ONLY about documents. Do NOT add eligibility criteria, fees, or process steps.
- If the citizen asks a specific question about a single document (e.g., whether a specific document is mandatory/optional, or how to get it), answer ONLY that specific question about that single document. Do NOT output or dump the entire list of required documents or other unrelated documents.
- Keep your response focused and concise. A short, precise answer is always better than a long, unfocused one.

FORMATTING RULES:
- You MUST structure your final answer using clear sections, bold text highlights, and markdown lists (bullet points or numbered lists).
- NEVER output large, blocky paragraphs of text.
- Even for short answers, organize different key facts, steps, or rules into distinct bullet points.
- Ensure the answer is visually clean, spaced out, and appealing to scan.

CRITICAL: You are strictly FORBIDDEN from mentioning or using technical terms like 'RAG-based', 'RAG', 'First Answer', 'Second Answer', 'Translated to English', 'Reference Context Details', or the synthesis process itself. Do not repeat intermediate headers. Answer naturally as a single consolidated assistance response that a normal user would want to hear.

RAG CONTEXT:
{rag_context}
"""

    messages_final = [{"role": "system", "content": system_instruction}]
    history = request.conversation_history or []
    if not history and request.messages:
        history = request.messages[:-1]
    for msg in history:
        messages_final.append({"role": msg.role, "content": msg.content})
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
    query_lang, english_query, hindi_query, context_en, context_hi, english_answer, hindi_answer, fallback_msg = await run_rag_pipeline_intermediates(query, request, service_id)
    
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
        request, service_id
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
