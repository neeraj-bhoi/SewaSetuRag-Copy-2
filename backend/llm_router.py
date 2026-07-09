import os
import sys
import re
import json
import requests
import contextvars
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

llm_trace = contextvars.ContextVar("llm_trace", default=None)

def log_llm_call(function_name: str, input_val: Any, output_val: Any):
    trace = llm_trace.get()
    if isinstance(trace, list):
        trace.append({
            "function": function_name,
            "input": input_val,
            "output": output_val
        })

# Ensure stdout uses UTF-8 to prevent Windows-specific print crashes
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# Sarvam AI API Configurations
sarvam_api_key = os.getenv("SARVAM_API_KEY", "")
sarvam_api_url = os.getenv("SARVAM_API_URL", "https://api.sarvam.ai/v1/chat/completions")
sarvam_model = os.getenv("SARVAM_MODEL", "sarvam-30b")


import time

def _post_with_retry(url: str, headers: dict, json_payload: dict, timeout: int = 180, max_retries: int = 3) -> requests.Response:
    """
    Executes a POST request to Sarvam API with exponential backoff retries for 5xx errors or timeouts.
    """
    backoff = 2
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(url, headers=headers, json=json_payload, timeout=timeout)
            if response.status_code in [500, 502, 503, 504]:
                print(f"[LLM Router] Transient server error {response.status_code}. Attempt {attempt + 1}/{max_retries + 1}...")
                if attempt == max_retries:
                    return response
            else:
                return response
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            print(f"[LLM Router] Request timeout or connection error on attempt {attempt + 1}/{max_retries + 1}: {e}")
            if attempt == max_retries:
                raise e
        
        # Wait before next attempt
        time.sleep(backoff)
        backoff *= 2


class ThinkStripper:
    def __init__(self):
        self.buffer = ""
        self.inside_think = False

    def feed(self, token: str) -> str:
        if token is None:
            token = ""
        self.buffer += token
        output = ""
        
        while True:
            if not self.inside_think:
                # Look for "<think>"
                idx = self.buffer.find("<think>")
                if idx != -1:
                    output += self.buffer[:idx]
                    self.buffer = self.buffer[idx + 7:]
                    self.inside_think = True
                else:
                    # Check for partial "<think" at the end of the buffer
                    partial_found = False
                    for i in range(1, min(len(self.buffer), 7)):
                        suffix = self.buffer[-i:]
                        if "<think>".startswith(suffix):
                            output += self.buffer[:-i]
                            self.buffer = suffix
                            partial_found = True
                            break
                    if not partial_found:
                        output += self.buffer
                        self.buffer = ""
                    break
            else:
                # Inside think, look for "</think>"
                idx = self.buffer.find("</think>")
                if idx != -1:
                    self.buffer = self.buffer[idx + 8:]
                    self.inside_think = False
                else:
                    # Check for partial "</think" at the end of the buffer
                    partial_found = False
                    for i in range(1, min(len(self.buffer), 8)):
                        suffix = self.buffer[-i:]
                        if "</think>".startswith(suffix):
                            self.buffer = suffix
                            partial_found = True
                            break
                    if not partial_found:
                        self.buffer = ""
                    break
        return output

    def flush(self) -> str:
        if not self.inside_think:
            res = self.buffer
            self.buffer = ""
            return res
        return ""


def generate_answer(messages: List[Dict[str, str]]) -> str:
    """
    Calls Sarvam AI completions (non-streaming, max_tokens=2048) and strips thinking blocks.
    Also handles repetition and loop prevention in responses.
    """
    if not sarvam_api_key:
        print("[LLM Router] Warning: SARVAM_API_KEY is not set.")

    headers = {
        "api-subscription-key": sarvam_api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "model": sarvam_model,
        "messages": messages,
        "temperature": 0.0,
        "stream": False,
        "max_tokens": 4096,
        "reasoning_effort": None
    }
    
    print(f"[LLM Router] Calling Sarvam AI completions...")
    response = _post_with_retry(sarvam_api_url, headers=headers, json_payload=payload, timeout=180)
    
    if response.status_code != 200:
        print(f"[LLM Router] Sarvam AI returned status {response.status_code}: {response.text}")
        raise ValueError(f"Sarvam AI returned status {response.status_code}")

    res_json = response.json()
    choices = res_json.get("choices", [])
    reply_content = ""
    if choices:
        message_obj = choices[0].get("message", {})
        reply_content = message_obj.get("content") or ""
    
    # Strip reasoning tags
    stripper = ThinkStripper()
    clean_reply = stripper.feed(reply_content) + stripper.flush()
    clean_reply = clean_reply.strip()
    
    # Repetition / Infinite loop prevention post-processing
    clean_reply = clean_reply.replace("\r\n", "\n")
    
    # Deduplicate consecutive paragraphs
    paragraphs = clean_reply.split("\n")
    seen_paras = set()
    unique_paras = []
    for p in paragraphs:
        p_stripped = p.strip()
        if not p_stripped:
            unique_paras.append("")
            continue
        # Normalize to find duplicates
        norm_p = re.sub(r'[^a-zA-Z0-9\u0900-\u097F]', '', p_stripped).lower()
        if norm_p not in seen_paras:
            seen_paras.add(norm_p)
            unique_paras.append(p)
    clean_reply = "\n".join(unique_paras)
    clean_reply = re.sub(r'\n{3,}', '\n\n', clean_reply).strip()
    
    # Deduplicate consecutive sentences within the text
    sentences = re.split(r'([.!?।\n]+)', clean_reply)
    seen_sents = set()
    reconstructed = []
    i = 0
    while i < len(sentences):
        sent = sentences[i]
        punc = sentences[i+1] if i + 1 < len(sentences) else ""
        sent_stripped = sent.strip()
        if not sent_stripped:
            reconstructed.append(sent + punc)
            i += 2
            continue
        norm_s = re.sub(r'[^a-zA-Z0-9\u0900-\u097F]', '', sent_stripped).lower()
        # Don't filter out numbers/short bullet indicators (length < 6 chars)
        if len(norm_s) < 6 or norm_s not in seen_sents:
            if len(norm_s) >= 6:
                seen_sents.add(norm_s)
            reconstructed.append(sent + punc)
        i += 2
    
    final_clean = "".join(reconstructed).strip()
    return final_clean


def detect_query_language(query: str) -> str:
    """
    Calls Sarvam AI to detect if the query is in English, Hindi, or Hinglish.
    Returns: 'en', 'hi', or 'hinglish'.
    """
    if not query:
        return 'en'
        
    # Check for Devanagari characters first - fast and 100% accurate for Devanagari Hindi
    for char in query:
        if '\u0900' <= char <= '\u097F':
            return 'hi'
            
    prompt = (
        "Identify the language of the following user query.\n"
        "The language can be English, Hindi (in Devanagari script), or Hinglish (Hindi written in Roman/Latin script).\n\n"
        f"Query: '{query}'\n\n"
        "Instructions:\n"
        "- Respond with EXACTLY one of these three strings: 'english', 'hindi', or 'hinglish'.\n"
        "- Do not explain your answer. Do not include formatting or markdown. Only return the lowercase word.\n\n"
        "Language:"
    )

    try:
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": sarvam_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "stream": False,
            "max_tokens": 256,
            "reasoning_effort": None
        }
        
        print(f"[LLM Router] Calling language detection endpoint...")
        res = _post_with_retry(sarvam_api_url, headers=headers, json_payload=payload, timeout=45)
        if res.status_code == 200:
            choices = res.json().get("choices", [])
            reply = ""
            reasoning = ""
            if choices:
                message_obj = choices[0].get("message", {})
                reply = message_obj.get("content") or ""
                reasoning = message_obj.get("reasoning_content") or ""
            
            print(f"[LLM Router] Language detection raw reply: '{reply}'")
            print(f"[LLM Router] Language detection raw reasoning: '{reasoning}'")
            reply_lower = reply.strip().lower()
            reasoning_lower = reasoning.strip().lower()
            
            # Strip reasoning tags if present in reply
            stripper = ThinkStripper()
            reply_clean = stripper.feed(reply_lower) + stripper.flush()
            reply_clean = reply_clean.strip()

            print(f"[LLM Router] Language detection stripped reply: '{reply_clean}'")
            
            def extract_lang(text: str) -> Optional[str]:
                found = re.findall(r'\b(english|hindi|hinglish)\b', text.lower())
                if found:
                    if 'hinglish' in found:
                        return 'hinglish'
                    if 'english' in found:
                        return 'en'
                    if 'hindi' in found:
                        return 'hi'
                return None

            # 1. Check stripped response
            detected = extract_lang(reply_clean)
            if detected:
                return detected
                
            # 2. Fallback: check raw content response
            detected = extract_lang(reply_lower)
            if detected:
                return detected

            # 3. Fallback: check reasoning_content
            detected = extract_lang(reasoning_lower)
            if detected:
                return detected
        else:
            print(f"[LLM Router] Language detection API call failed with status code {res.status_code}")
    except Exception as e:
        print(f"[LLM Router] Language detection failed: {e}")
        
    # Basic unicode fallback
    for char in query:
        if '\u0900' <= char <= '\u097F':
            return 'hi'
            
            
    return 'en'


def translate_query_to_english(query: str) -> str:
    """
    Translates a Hindi or Hinglish query to English using Sarvam's LLM instead of the translation API.
    """
    if not query:
        return ""

    prompt = (
        "You are a strict translation assistant. Translate the user's input to standard English.\n"
        "Do NOT answer the query or question. Do NOT add any extra explanation, response, or conversational filler.\n"
        "If the input query is already in standard English, output it exactly as-is.\n"
        "If it is a question, keep it as a question in English. Do NOT answer it.\n"
        "Output ONLY the final English translation and nothing else.\n\n"
        f"Input: {query}\n"
        "Output:"
    )

    try:
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": sarvam_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "stream": False,
            "max_tokens": 4096,
            "reasoning_effort": None
        }
        
        print(f"[LLM Router] Translating query to English using LLM...")
        res = _post_with_retry(sarvam_api_url, headers=headers, json_payload=payload, timeout=90)
        if res.status_code == 200:
            choices = res.json().get("choices", [])
            reply = ""
            if choices:
                message_obj = choices[0].get("message", {})
                reply = message_obj.get("content") or ""
            
            # Clean up thinking blocks if any
            stripper = ThinkStripper()
            reply_clean = (stripper.feed(reply) + stripper.flush()).strip()
            
            # Clean up potential prompt leakage
            if "Output:" in reply_clean:
                reply_clean = reply_clean.split("Output:")[-1].strip()
            if "Input:" in reply_clean:
                reply_clean = reply_clean.split("Input:")[0].strip()
                
            if not reply_clean:
                print("[LLM Router] Translated query to English is empty, falling back to original query")
                return query
            return reply_clean
        else:
            print(f"[LLM Router] LLM query translation failed with status code {res.status_code}: {res.text}")
    except Exception as e:
        print(f"[LLM Router] LLM query translation failed: {e}")
        
    return query


def translate_query_to_hindi(query: str) -> str:
    """
    Translates an English query to Hindi using Sarvam's LLM.
    """
    if not query:
        return ""

    # Check for Devanagari characters first - fast and 100% accurate for Devanagari Hindi
    for char in query:
        if '\u0900' <= char <= '\u097F':
            return query

    prompt = (
        "You are a strict translation assistant. Translate the user's input to Hindi Devanagari script.\n"
        "Do NOT answer the query or question. Do NOT add any extra explanation, response, or conversational filler.\n"
        "If the input query is already in standard Hindi Devanagari script, output it exactly as-is.\n"
        "If it is a question, keep it as a question in Hindi. Do NOT answer it.\n"
        "Output ONLY the final Hindi translation in Devanagari script and nothing else.\n\n"
        f"Input: {query}\n"
        "Output:"
    )

    try:
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": sarvam_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "stream": False,
            "max_tokens": 4096,
            "reasoning_effort": None
        }
        
        print(f"[LLM Router] Translating query to Hindi using LLM...")
        res = _post_with_retry(sarvam_api_url, headers=headers, json_payload=payload, timeout=90)
        if res.status_code == 200:
            choices = res.json().get("choices", [])
            reply = ""
            if choices:
                message_obj = choices[0].get("message", {})
                reply = message_obj.get("content") or ""
            
            # Clean up thinking blocks if any
            stripper = ThinkStripper()
            reply_clean = (stripper.feed(reply) + stripper.flush()).strip()
            
            # Clean up potential prompt leakage
            if "Output:" in reply_clean:
                reply_clean = reply_clean.split("Output:")[-1].strip()
            if "Input:" in reply_clean:
                reply_clean = reply_clean.split("Input:")[0].strip()
                
            if not reply_clean:
                print("[LLM Router] Translated query to Hindi is empty, falling back to original query")
                return query
            return reply_clean
        else:
            print(f"[LLM Router] LLM query translation to Hindi failed with status code {res.status_code}: {res.text}")
    except Exception as e:
        print(f"[LLM Router] LLM query translation to Hindi failed: {e}")
        
    return query


def classify_service(query: str, services_list: List[Dict[str, Any]], use_llm_only: bool = False) -> Dict[str, Optional[str]]:
    """
    Service classification mapping matching query to correct serial number 'sno'.
    Uses LLM classification for all queries to ensure 100% accuracy and zero hardcoded rules.
    """
    if not query:
        return {"sno": None, "service_id": None}

    q_lower = query.lower()

    # Avoid calling API for very short generic inputs or greetings
    greetings = {"hi", "hello", "hey", "ok", "okay", "yes", "no", "thanks", "thank you", "plz", "please", "help", "namaste", "नमस्ते", "हेलो", "बाय", "bye"}
    words = set(q_lower.split())
    if len(q_lower.strip()) < 3 or (len(words) == 1 and words.intersection(greetings)):
        print(f"[LLM Router] Simple greeting or short query detected: '{query}'. Skipping classification.")
        return {"sno": None, "service_id": None}

    # Call LLM classifier directly for all in-scope mapping
    services_catalog_desc = "\n".join([
        f"{s['sno']}. Serial Number {s['sno']} (Service ID: {s['service_id']}): {s['name_en']} | {s['name_hi']}"
        for s in services_list
    ])

    import re
    is_hindi = bool(re.search(r'[\u0900-\u097f]', query))

    english_few_shots = (
        "FEW-SHOT EXAMPLES (ENGLISH/HINGLISH):\n"
        "- Query: 'domicile certificate application me spelling mistake ho gayi hai correct kaise karein?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'obc income required for creamy status'\n"
        "  Output: {\"sno\": \"3\", \"service_id\": \"5\"}\n"
        "- Query: 'domicile ki kia requirement hai marriage me?'\n"
        "  Output: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Query: 'shadi ke baad caste certificate me name change kaise karein?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'is domicile necessary for obc certificate?'\n"
        "  Output: {\"sno\": \"3\", \"service_id\": \"5\"}\n"
        "- Query: 'st certificate ke liye domicile rules kya hain?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'driving license renewal online process'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'ration card list me name correction kaise hoga?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'do we need sc certificate for obc scholarship application?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'is voter id mandatory for st certificate if i have school study certificate?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'caste certificate correction name change application format'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'marriage registrar local area authority in village for caste certificate holders'\n"
        "  Output: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Query: 'is notarized affidavit in Form-III for name change same as marriage affidavit?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'obc income certificate slab details for domicile students'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'can we apply for marriage certificate and name change together on sewasetu?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'fees of obc certificate vs ordinary gazette publication fee'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'caste certificate digital signature verification vs domicile verification status'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'is digital signature of sdo for st certificate same as domicile?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
    )

    hindi_few_shots = (
        "FEW-SHOT EXAMPLES (HINDI):\n"
        "- Query: 'मूल निवास प्रमाण पत्र आवेदन में नाम की त्रुटि सुधार कैसे करें?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'ओबीसी क्रीमी स्टेटस के लिए आवश्यक आय'\n"
        "  Output: {\"sno\": \"3\", \"service_id\": \"5\"}\n"
        "- Query: 'क्या विवाह पंजीकरण के लिए निवास प्रमाण पत्र अनिवार्य है?'\n"
        "  Output: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Query: 'शादी के बाद जाति प्रमाण पत्र में नाम सुधार कैसे होगा?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'क्या ओबीसी प्रमाण पत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?'\n"
        "  Output: {\"sno\": \"3\", \"service_id\": \"5\"}\n"
        "- Query: 'एसटी प्रमाण पत्र के लिए छत्तीसगढ़ निवास नियम क्या हैं?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'ड्राइविंग लाइसेंस ऑनलाइन नवीनीकरण प्रक्रिया'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'राशन कार्ड सूची में नाम सुधार कैसे होगा?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप क्या है?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण कौन है?'\n"
        "  Output: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Query: 'क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र विवाह शपथ पत्र के समान है?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'क्या हम सेवासेतु पर विवाह प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क क्या है?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'क्या ओबीसी प्रमाणपत्र के लिए निवास प्रमाणपत्र आवश्यक है?'\n"
        "  Output: {\"sno\": \"3\", \"service_id\": \"5\"}\n"
        "- Query: 'ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'निवास प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर निवास प्रमाण पत्र के समान है?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
    )

    selected_few_shots = hindi_few_shots if is_hindi else english_few_shots

    prompt = (
        "You are an expert service mapping assistant for the SewaSetu Chhattisgarh portal.\n"
        "Your task is to map a user query to the correct service from the catalog below.\n\n"
        "CATALOG OF SERVICES:\n"
        f"{services_catalog_desc}\n\n"
        "CLASSIFICATION RULES:\n"
        "1. PRIMARY TARGET RULE (Mixed Services): If a query mentions multiple services or certificates (e.g. asking about supporting documents like Domicile for a target certificate like Marriage or OBC), ALWAYS map it to the primary TARGET service that the user is trying to obtain, NOT the supporting document. For example:\n"
        "   - 'is domicile necessary for obc' -> OBC Certificate (SNO 3)\n"
        "   - 'marriage registration for domicile holder' -> Marriage Registration (SNO 1)\n"
        "2. NAME CHANGE / CORRECTION ON ISSUED CERTIFICATE: If the query asks about changing, correcting, or updating a name or spelling on an ALREADY ISSUED certificate or document (e.g., SC/ST or OBC certificate, Domicile, or Marriage certificate), you MUST map it to 'Ordinary Gazette Notification for Name Change' (SNO 5, Service ID 201). For example:\n"
        "   - 'caste certificate me name correction' -> SNO 5\n"
        "   - 'domicile me naam change process' -> SNO 5\n"
        "   - 'shadi ke baad name change kaise karein' -> SNO 5\n"
        "3. ACTIVE/PENDING APPLICATION FORM TYPOS: If the user asks about correcting a spelling mistake, typo, or details in an active, pending, draft, or submitted application form (e.g., 'application form', 'submitted application', 'form correction', 'application me mistake'), you MUST map it to the SPECIFIC certificate service being applied for (e.g., Domicile Certificate SNO 4, SC/ST Certificate SNO 2, OBC Certificate SNO 3), NOT the Gazette service. For example:\n"
        "   - 'domicile certificate application me correction kaise karein' -> SNO 4\n"
        "   - 'submitted caste certificate application correction' -> SNO 2\n"
        "4. OUT OF SCOPE / OTHER SERVICES: If the query is about any service, document, or scheme NOT listed in the catalog of 5 services (such as driving license, ration card, income certificate, electricity connection, land records/khasra/mutation, PAN card, Aadhaar card, voter ID, old age pension, scholarships, solar panels, water connections, or general chit-chat), you MUST return 'null' for both keys. For example:\n"
        "   - 'income certificate criteria' -> Output: {\"sno\": null, \"service_id\": null}\n"
        "   - 'ration card me name add' -> Output: {\"sno\": null, \"service_id\": null}\n"
        "   - Note: If the primary subject or topic of the query is any out-of-scope service, application, or scheme (e.g. scholarships, old-age pensions, water/electricity connections), even if the user mentions an in-scope certificate (like SC certificate, Domicile certificate) as a supporting document or eligibility proof, the entire query is OUT OF SCOPE and must map to null. For example: 'do we need sc certificate for obc scholarship application?' -> Output: {\"sno\": null, \"service_id\": null}\n\n"
        "FEW-SHOT EXAMPLES:\n"
        "- Query: 'domicile certificate application me spelling mistake ho gayi hai correct kaise karein?'\n"
        "  Output: {\"sno\": \"4\", \"service_id\": \"7\"}\n"
        "- Query: 'domicile ki kia requirement hai marriage me?'\n"
        "  Output: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Query: 'shadi ke baad caste certificate me name change kaise karein?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'is domicile necessary for obc certificate?'\n"
        "  Output: {\"sno\": \"3\", \"service_id\": \"5\"}\n"
        "- Query: 'st certificate ke liye domicile rules kya hain?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'driving license renewal online process'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'ration card list me name correction kaise hoga?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'do we need sc certificate for obc scholarship application?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'is voter id mandatory for st certificate if i have school study certificate?'\n"
        "  Output: {\"sno\": \"2\", \"service_id\": \"4\"}\n"
        "- Query: 'caste certificate correction name change application format'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'marriage registrar local area authority in village for caste certificate holders'\n"
        "  Output: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Query: 'is notarized affidavit in Form-III for name change same as marriage affidavit?'\n"
        "  Output: {\"sno\": \"5\", \"service_id\": \"201\"}\n"
        "- Query: 'obc income certificate slab details for domicile students'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'can we apply for marriage certificate and name change together on sewasetu?'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n"
        "- Query: 'fees of obc certificate vs ordinary gazette publication fee'\n"
        "  Output: {\"sno\": null, \"service_id\": null}\n\n"
        f"User Query: '{query}'\n\n"
        "Return ONLY a JSON object containing the mapped 'sno' and 'service_id' as strings. Do not write any explanation, and do not use markdown code fences.\n"
        "Output JSON:"
    )

    try:
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": sarvam_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "stream": False,
            "max_tokens": 512,
            "reasoning_effort": None
        }
        
        print(f"[LLM Router] Calling classification endpoint...")
        res = _post_with_retry(sarvam_api_url, headers=headers, json_payload=payload, timeout=30)
        if res.status_code == 200:
            choices = res.json().get("choices", [])
            reply = ""
            if choices:
                message_obj = choices[0].get("message", {})
                reply = message_obj.get("content") or ""
            reply = reply.strip()
            
            # Strip reasoning tags
            stripper = ThinkStripper()
            reply = stripper.feed(reply) + stripper.flush()
            reply = reply.strip()

            json_match = re.search(r'\{.*?\}', reply, re.DOTALL)
            if json_match:
                json_data = json.loads(json_match.group(0))
                sno_val = json_data.get("sno")
                sid_val = json_data.get("service_id")
                if sno_val and str(sno_val).lower() != "null":
                    # Validate that the sno matches a valid sno in services
                    valid_snos = {str(s["sno"]) for s in services_list}
                    if str(sno_val) in valid_snos:
                        return {
                            "sno": str(sno_val),
                            "service_id": str(sid_val) if sid_val else None
                        }
    except Exception as e:
        print(f"[LLM Router] Service mapping classification failed: {e}")

    return {"sno": None, "service_id": None}


def classify_query_intent(query: str, recent_history: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Classifies a user query using an LLM into one of:
      'greeting', 'farewell', 'thanks', 'identity', 'out_of_scope',
      'follow_up', or 'new_topic'.
    
    No hardcoded word lists — the LLM handles spelling variations, typos,
    and multilingual inputs (English, Hindi, Hinglish) naturally.
    
    Returns:
        {
            "intent": one of the above intents,
            "resolved_query": "self-contained rewritten query (for follow_up/new_topic)",
            "topic_summary": "1-line summary"
        }
    """
    if not query or not query.strip():
        return {"intent": "new_topic", "resolved_query": query or "", "topic_summary": ""}

    # Build structured history for context (only needed for follow_up/new_topic)
    history_str = ""
    if recent_history and len(recent_history) > 0:
        history_msgs = recent_history[-4:]  # Last 2 turns max
        
        if len(history_msgs) >= 4:
            history_str += "OLDER CONTEXT (background only, NOT the current topic):\n"
            for msg in history_msgs[:2]:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if content:
                    if role == "assistant" and len(content) > 150:
                        content = content[:150] + "..."
                    history_str += f"  {role.upper()}: {content}\n"
            
            history_str += "\nMOST RECENT EXCHANGE (THIS IS THE CURRENT TOPIC):\n"
            for msg in history_msgs[2:]:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if content:
                    if role == "assistant" and len(content) > 150:
                        content = content[:150] + "..."
                    history_str += f"  {role.upper()}: {content}\n"
        else:
            history_str += "MOST RECENT EXCHANGE (THIS IS THE CURRENT TOPIC):\n"
            for msg in history_msgs:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if content:
                    if role == "assistant" and len(content) > 150:
                        content = content[:150] + "..."
                    history_str += f"  {role.upper()}: {content}\n"

    history_block = f"CONVERSATION HISTORY:\n{history_str}\n" if history_str else "CONVERSATION HISTORY: (none)\n"

    prompt = (
        "You are a query classifier for a Chhattisgarh government services chatbot (SewaSetu). "
        "Classify the user's latest query into EXACTLY ONE intent.\n\n"
        "INTENT CATEGORIES (choose exactly one):\n"
        "1. greeting — Any hello/hi/hey/good morning type salutation, in any language or spelling. "
        "Examples: 'hi', 'hii', 'hello', 'namaste', 'namaskar', 'hey there', 'helo', 'hlw', 'good morning'\n"
        "2. farewell — Any goodbye/bye/see you type farewell. "
        "Examples: 'bye', 'goodbye', 'alvida', 'good night', 'see you'\n"
        "3. thanks — Any thank you/thanks/appreciation or simple acknowledgement like ok/okay/hmm/yes/haan/theek hai/acha. "
        "Examples: 'thanks', 'thank you', 'shukriya', 'dhanyavaad', 'ok', 'okay', 'hmm', 'acha', 'theek hai', 'haan'\n"
        "4. identity — User is asking who/what the chatbot is, what it can do, or asking it to introduce itself. "
        "Examples: 'who are you', 'aap kaun ho', 'tum kaun ho', 'ye kya hai', 'what can you do', 'what is sewasetu'\n"
        "5. out_of_scope — The query is NOT about Chhattisgarh government services. This includes politics, general knowledge, celebrities, weather, sports, entertainment, math, coding, personal advice, or any topic unrelated to government services/certificates/documents/fees. "
        "Examples: 'modi kaun hai', 'who is the president', 'what is the weather', 'tell me a joke', '2+2 kya hai', 'capital of India'\n"
        "6. follow_up — The query asks about the SAME government service/certificate as the MOST RECENT one in the conversation history — either a different aspect (fees, documents, eligibility, timeline) or a clarification. "
        "Examples: 'what is the fee?', 'documents needed?', 'how long does it take?', 'eligibility criteria?' (when referring to the SAME service currently being discussed).\n"
        "7. new_topic — The query is about a Chhattisgarh government service but refers to or names a DIFFERENT service/certificate than the one in the conversation history, OR it is the first service query with no history. "
        "Examples: 'and for marriage?', 'what about birth certificate?', 'caste certificate fees?' (when the previous topic was name change or domicile).\n\n"
        "CRITICAL SERVICE CLASSIFICATION RULE:\n"
        "- Questions asking about the 'process', 'procedure', 'documents', 'fees', 'timeline', or checking if a specific document/ID is valid as eligibility proof (e.g., 'caste certificate ka process', 'name change kaise karein', 'obc praman patra ke liye documents list', 'is voter id proof of stay for domicile') are government service queries. They MUST be classified as 'new_topic' or 'follow_up', NEVER as 'identity' or 'out_of_scope'.\n"
        "- 'identity' is STRICTLY reserved for general questions about the chatbot itself (e.g., 'who are you', 'what can you do', 'introduce yourself', 'explain what is sewasetu'). It does NOT apply to queries asking about how to perform a specific government task or service.\n\n"
        "CRITICAL SERVICE SWITCH RULE:\n"
        "- If the latest query refers to or mentions a DIFFERENT service (e.g., Marriage Certificate) than the most recent service discussed (e.g., Name Change), the intent MUST be 'new_topic'. It is NEVER a 'follow_up'.\n"
        "- Even if the query is short and relies on carrying over the aspect from history (e.g., 'and for marriage?' asking about fees after discussing name change fees), it is still a 'new_topic' because the service itself has changed.\n\n"
        "IMPORTANT RULES:\n"
        "- For greeting/farewell/thanks/identity/out_of_scope: set resolved_query to the original query and topic_summary to empty string.\n"
        "- For follow_up: rewrite resolved_query to be fully self-contained with the service name and aspect.\n"
        "- For new_topic: if the query is short and the ASPECT is implied from history (e.g., 'what about marriage?' after discussing fees of name change), carry over the aspect into the resolved_query (e.g., 'What is the cost for marriage registration?').\n"
        "- RECENCY RULE: implicit references ('the cost', 'its documents') without naming any new service ALWAYS refer to the MOST RECENT service discussed.\n"
        "- CONSISTENCY CHECK: if resolved_query references a DIFFERENT service than history, intent MUST be 'new_topic'.\n"
        "- The query can be in English, Hindi (Devanagari), Hinglish, or have typos — classify based on meaning, not exact spelling.\n\n"
        f"{history_block}"
        f"LATEST USER QUERY: {query}\n\n"
        "Respond with ONLY a JSON object (no markdown, no code fences, no explanation):\n"
        '{"intent": "greeting|farewell|thanks|identity|out_of_scope|follow_up|new_topic", "resolved_query": "...", "topic_summary": "..."}\n'
        "JSON:"
    )

    valid_intents = {"greeting", "farewell", "thanks", "identity", "out_of_scope", "follow_up", "new_topic"}

    try:
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": sarvam_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "stream": False,
            "max_tokens": 256,
            "reasoning_effort": None
        }
        
        print(f"[LLM Router] Classifying query intent...")
        res = _post_with_retry(sarvam_api_url, headers=headers, json_payload=payload, timeout=30)
        if res.status_code == 200:
            choices = res.json().get("choices", [])
            reply = ""
            if choices:
                message_obj = choices[0].get("message", {})
                reply = message_obj.get("content") or ""
            
            # Strip reasoning tags
            stripper = ThinkStripper()
            reply = (stripper.feed(reply) + stripper.flush()).strip()
            
            print(f"[LLM Router] Intent classification raw reply: '{reply}'")
            
            json_match = re.search(r'\{.*?\}', reply, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group(0))
                intent = result.get("intent", "new_topic")
                resolved = result.get("resolved_query", query)
                summary = result.get("topic_summary", "")
                
                # Validate intent value
                if intent not in valid_intents:
                    intent = "new_topic"
                
                # Safety: if resolved_query is empty, fall back to original
                if not resolved or not resolved.strip():
                    resolved = query
                
                print(f"[LLM Router] Intent: {intent}, Resolved: '{resolved}', Summary: '{summary}'")
                return {"intent": intent, "resolved_query": resolved, "topic_summary": summary}
        else:
            print(f"[LLM Router] Intent classification failed with status {res.status_code}")
    except Exception as e:
        print(f"[LLM Router] Intent classification error: {e}")
    
    # Fallback: treat as new topic
    return {"intent": "new_topic", "resolved_query": query, "topic_summary": ""}


# Save the original functions for wrapping
_original_generate_answer = generate_answer
_original_detect_query_language = detect_query_language
_original_translate_query_to_english = translate_query_to_english
_original_translate_query_to_hindi = translate_query_to_hindi
_original_classify_query_intent = classify_query_intent
_original_classify_service = classify_service

# Define wrapper functions that invoke originals and record details in trace
def generate_answer(messages: List[Dict[str, str]]) -> str:
    res = _original_generate_answer(messages)
    log_llm_call("generate_answer", messages, res)
    return res

def detect_query_language(query: str) -> str:
    res = _original_detect_query_language(query)
    log_llm_call("detect_query_language", query, res)
    return res

def translate_query_to_english(query: str) -> str:
    res = _original_translate_query_to_english(query)
    log_llm_call("translate_query_to_english", query, res)
    return res

def translate_query_to_hindi(query: str) -> str:
    res = _original_translate_query_to_hindi(query)
    log_llm_call("translate_query_to_hindi", query, res)
    return res

def classify_query_intent(query: str, recent_history: List[Dict[str, str]]) -> Dict[str, str]:
    res = _original_classify_query_intent(query, recent_history)
    log_llm_call("classify_query_intent", {"query": query, "recent_history": recent_history}, res)
    return res

def classify_service(query: str, services_list: List[Dict[str, Any]], use_llm_only: bool = False) -> Dict[str, Optional[str]]:
    res = _original_classify_service(query, services_list, use_llm_only)
    log_llm_call("classify_service", {"query": query, "use_llm_only": use_llm_only}, res)
    return res

