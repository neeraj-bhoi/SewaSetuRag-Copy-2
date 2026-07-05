import os
import sys
import re
import json
import requests
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

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


def classify_service(query: str, services_list: List[Dict[str, Any]]) -> Dict[str, Optional[str]]:
    """
    Service classification mapping matching query to correct serial number 'sno'.
    Uses rule-based heuristics first, then calls Sarvam AI if no high-confidence rule match is found.
    """
    if not query:
        return {"sno": None, "service_id": None}

    q_lower = query.lower()

    # Avoid calling LLM for very short generic inputs or greetings
    greetings = {"hi", "hello", "hey", "ok", "okay", "yes", "no", "thanks", "thank you", "plz", "please", "help", "namaste", "नमस्ते", "हेलो", "बाय", "bye"}
    words = set(q_lower.split())
    if len(q_lower.strip()) < 3 or (len(words) == 1 and words.intersection(greetings)):
        print(f"[LLM Router] Simple greeting or short query detected: '{query}'. Skipping classification.")
        return {"sno": None, "service_id": None}

    # Define in-scope keywords
    has_marriage = any(k in q_lower for k in ["marriage", "marrage", "mariage", "shadi", "shaadi", "vivah", "विवाह", "शादी", "मैरिज", "मॅरिज"])
    has_gazette = any(k in q_lower for k in ["gazette", "gazzete", "gazzette", "gazet", "name change", "नाम परिवर्तन", "राजपत्र", "affidavit for name change", "गजट"])
    has_domicile = any(k in q_lower for k in ["domicile", "domicil", "domiciel", "domicille", "dimicile", "domisile", "domisiel", "domocile", "domociel", "resident", "residence", "निवास", "मूल निवासी", "डोमिसाइल"])
    has_obc = any(k in q_lower for k in ["obc", "अन्य पिछड़ा वर्ग", "पिछड़ा वर्ग", "ओबीसी", "ओ.बी.सी."])
    has_caste = any(k in q_lower for k in ["sc/st", "scheduled caste", "scheduled tribe", "अनुसूचित जाति", "अनुसूचित जनजाति", "caste", "cast", "जाति", "tribal", "जनजाति", "gond", "chamar", "mahyavanshi", "khadiya", "kharwar", "एससी", "एसटी", "एससी/एसटी"]) or any(re.search(r'\b' + re.escape(k) + r'\b', q_lower) for k in ["sc", "st"])

    has_in_scope = has_marriage or has_gazette or has_domicile or has_obc or has_caste

    # Define out-of-scope keywords
    has_out_of_scope = any(k in q_lower for k in [
        "scholarship", "छात्रवृत्ति", "matric", "स्कॉलरशिप",
        "rental", "rent", "किराया", "रेंट", "एग्रीमेंट",
        "water connection", "जल कनेक्शन", "नल कनेक्शन", "water supply",
        "electricity", "बिजली", "power", "विद्युत",
        "ration card", "राशन कार्ड",
        "land records", "khasra", "khatauni", "b-1", "b-i", "खसरा", "नक्शा", "ज़मीन",
        "housing loan", "home loan", "ऋण", "लोन", "loan",
        "income certificate", "आय प्रमाण पत्र", "आय प्रमाणपत्र"
    ])

    # If it contains out-of-scope keywords and NOT in-scope keywords, it is definitely out-of-scope
    if has_out_of_scope and not has_in_scope:
        print(f"[LLM Router] Rule-based filter: Query contains out-of-scope terms and no in-scope terms. Mapping to None.")
        return {"sno": None, "service_id": None}

    # 1. Quick rule-based heuristic check for high confidence in-scope keywords
    if has_marriage:
        return {"sno": "1", "service_id": "3"}
    if has_gazette:
        return {"sno": "5", "service_id": "201"}
    if has_obc:
        return {"sno": "3", "service_id": "5"}
    if has_caste:
        return {"sno": "2", "service_id": "4"}
    if has_domicile:
        return {"sno": "4", "service_id": "7"}

    # 2. Try semantic database lookup before LLM fallback
    try:
        try:
            from backend.rag import collection, embedding_model
        except ImportError:
            from rag import collection, embedding_model

        print(f"[LLM Router] Performing semantic lookup fallback for query: '{query}'")
        query_text = f"query: {query}"
        query_vector = embedding_model.encode(query_text).tolist()
        
        # Query database without service filter
        results = collection.query(
            query_embeddings=[query_vector],
            n_results=3,
            where={"lang": "en"}
        )
        
        if results and "documents" in results and results["documents"]:
            docs = results["documents"][0]
            metas = results["metadatas"][0]
            distances = results["distances"][0]
            
            threshold = 0.45 if has_in_scope else 0.33
            if distances and distances[0] < threshold:
                matched_sid = metas[0].get("service_id")
                if matched_sid:
                    # Find matching sno in services_list
                    matched_sno = None
                    for s in services_list:
                        if str(s["service_id"]) == str(matched_sid):
                            matched_sno = str(s["sno"])
                            break
                    if matched_sno:
                        print(f"[LLM Router] Semantic match found: service_id {matched_sid} (sno {matched_sno}) with distance {distances[0]:.4f}")
                        return {"sno": matched_sno, "service_id": str(matched_sid)}
    except Exception as e:
        print(f"[LLM Router] Semantic classification fallback failed: {e}")

    # 3. Fall back to LLM classification for complex/ambiguous queries or queries with spelling typos
    services_catalog_desc = "\n".join([
        f"{s['sno']}. Serial Number {s['sno']} (Service ID: {s['service_id']}): {s['name_en']} | {s['name_hi']}"
        for s in services_list
    ])

    prompt = (
        "You are an expert service mapping assistant for the SewaSetu Chhattisgarh portal.\n"
        "Your task is to identify which specific service from the catalog is the closest match to the user query.\n"
        "The query could be in English, Hindi, or Hinglish.\n\n"
        "Here is the catalog of services:\n"
        f"{services_catalog_desc}\n\n"
        f"User Query: '{query}'\n\n"
        "Instructions:\n"
        "- Match the query to a service if the query is asking about requirements, rules, procedures, fees, eligibility, or lists of Castes/Tribes related to that service.\n"
        "- For example, queries about specific castes (SC/ST/OBC), tribes, or caste list entries belong to the SC/ST Certificate or OBC Certificate services.\n"
        "- Domicile/Residence queries belong to the Domicile Certificate service.\n"
        "- Marriage registration/certificate queries belong to the Marriage Registration & Certificate service.\n"
        "- Name change, gazette publication, or affidavit for name change queries belong to the Ordinary Gazette Notification for Name Change service.\n"
        "- If the query is generic, completely unrelated to these 5 services (e.g., solar panels, water connections, electricity, scholarships, land records, or general chat), return {\"sno\": null, \"service_id\": null}.\n"
        "- Return ONLY a JSON object containing the mapped 'sno' and 'service_id' as strings. For example: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Do not explain your choice. Do not output markdown, only raw JSON.\n\n"
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
    Classifies a user query as 'greeting', 'follow_up', or 'new_topic' based on conversation history.
    For follow-ups, rewrites the query into a self-contained form.
    
    Returns:
        {
            "intent": "greeting" | "follow_up" | "new_topic",
            "resolved_query": "the self-contained rewritten query (or original if new_topic/greeting)",
            "topic_summary": "1-line summary of what the conversation is about"
        }
    """
    if not query:
        return {"intent": "new_topic", "resolved_query": query, "topic_summary": ""}

    # Fast rule-based greeting detection (no LLM needed)
    q_stripped = query.strip().lower()
    # Remove trailing punctuation for matching
    q_clean = re.sub(r'[!?.,।\s]+$', '', q_stripped)
    
    greeting_patterns = {
        # English greetings
        "hi", "hello", "hey", "hii", "hiii", "helloo", "hellooo",
        "good morning", "good afternoon", "good evening", "good night",
        # English farewells
        "bye", "byee", "goodbye", "good bye", "see you", "take care",
        # English thanks
        "thanks", "thank you", "thankyou", "thank u", "thnx", "thnks", "ty",
        # English pleasantries
        "ok", "okay", "okk", "okkk", "yes", "no", "hmm", "hmmm",
        "please", "plz", "pls",
        # Hindi greetings (Devanagari)
        "नमस्ते", "नमस्कार", "हेलो", "हाय", "हैलो",
        # Hindi farewells
        "अलविदा", "बाय", "धन्यवाद", "शुक्रिया",
        # Hindi pleasantries
        "जी", "जी हाँ", "जी नहीं", "हाँ", "नहीं", "ठीक है", "ठीक",
        # Hinglish greetings
        "namaste", "namaskar", "namaskaar", "pranam",
        "dhanyavaad", "dhanyawad", "shukriya", "alvida",
        "haan", "nahi", "nhi", "theek hai", "thik hai",
        "acha", "accha", "achha"
    }
    
    if q_clean in greeting_patterns:
        return {"intent": "greeting", "resolved_query": query, "topic_summary": ""}

    # If no history, it's definitely a new topic — no need for LLM call
    if not recent_history or len(recent_history) == 0:
        return {"intent": "new_topic", "resolved_query": query, "topic_summary": ""}

    # Build a compact history string for the LLM
    history_str = ""
    for msg in recent_history[-4:]:  # Last 2 turns max
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if content:
            # Truncate long assistant responses to save tokens
            if role == "assistant" and len(content) > 200:
                content = content[:200] + "..."
            history_str += f"{role.upper()}: {content}\n"

    prompt = (
        "You are a query classifier for a government services chatbot. Given a conversation history and the user's latest query, classify the intent and produce a self-contained resolved query.\n\n"
        "RECENCY RULE (HIGHEST PRIORITY):\n"
        "The MOST RECENT service/topic in the conversation is the current context. When a user's query refers to something implicitly (e.g., 'the cost', 'its documents', 'how long'), they are ALWAYS referring to the MOST RECENT service discussed — never an older one.\n\n"
        "CLASSIFICATION RULES:\n"
        "1. new_topic: The query mentions or names a DIFFERENT service/certificate/scheme than the MOST RECENT one in history. This applies even with connective words like 'aur' (and), 'what about', 'how about', 'bhi' (also).\n"
        "2. follow_up: The query asks about the SAME service as the MOST RECENT one in history — either a different aspect (fees, documents, eligibility, timeline) or a correction/clarification of the previous answer.\n\n"
        "RESOLVED QUERY RULES (applies to BOTH intents):\n"
        "- ALWAYS produce a fully self-contained resolved_query that includes the service name AND the specific aspect.\n"
        "- For follow_up: Replace pronouns/implicit references with the MOST RECENT service name from history.\n"
        "- For new_topic with aspect carry-over: If the query is short and references a new service but the ASPECT is implied from the previous conversation (e.g., 'what about Service B?' after discussing fees of Service A), carry over the aspect into the resolved_query (e.g., 'what are the fees for Service B?').\n"
        "- For new_topic that is fully self-contained: Keep the resolved_query as the original query.\n\n"
        f"CONVERSATION HISTORY:\n{history_str}\n"
        f"LATEST USER QUERY: {query}\n\n"
        "Respond with ONLY a JSON object (no markdown, no code fences, no explanation):\n"
        '{"intent": "follow_up" or "new_topic", "resolved_query": "fully self-contained rewritten query with service name and aspect", "topic_summary": "1-line summary"}\n'
        "JSON:"
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
                if intent not in ("follow_up", "new_topic", "greeting"):
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
