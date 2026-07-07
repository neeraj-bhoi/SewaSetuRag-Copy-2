"""
Test script: 50 queries with follow-ups and new topics.
Sends to /api/chat with detailed=true, captures intermediate steps,
and writes results to test_results3.md after each query.
"""
import requests
import json
import time
import os
from datetime import datetime

API_URL = "http://localhost:8000/api/chat"
RESULTS_FILE = "test_results5.md"

# Service sno mapping:
# sno=1 -> Marriage Registration (service_id=3)
# sno=2 -> SC/ST Certificate (service_id=4)
# sno=3 -> OBC Certificate (service_id=5)
# sno=4 -> Domicile Certificate (service_id=7)
# sno=5 -> Name Change (service_id=201)

# ======= TEST QUERIES =======
# Format: (query, selected_sno, language, is_follow_up_of_previous)
# is_follow_up_of_previous=True means keep conversation history from previous query
QUERIES = [
    # --- Block 1: Greetings & Identity ---
    ("namaste ji, aapka swagat hai", None, "hi", False),
    ("who is this chatbot?", None, "en", False),
    ("kya aap meri madad kar sakte hain?", None, "hi", False),
    
    # --- Block 2: Caste Certificate (SC/ST) ---
    ("SC/ST praman patra ke liye eligibility kya hai?", "2", "hi", False),
    ("kya isme pitaji ka chhattisgarh ka resident record chahiye?", "2", "hi", True),
    ("is certificate ko banwane me kitna paisa lagta hai?", "2", "hi", True),
    ("kya offline form fill up karna padega?", "2", "hi", True),
    
    # --- Block 3: Switch to Domicile (aspect carry-over) ---
    ("aur domicile certificate ki kya eligibility hai?", "4", "hi", True),
    ("kya 15 saal chhattisgarh me rehna mandatory hai?", "4", "hi", True),
    ("education certificate cg ka hona zaroori hai?", "4", "hi", True),
    ("domicile certificate banne me kitna time lagta hai?", "4", "hi", True),
    
    # --- Block 4: OBC Certificate (fees & process) ---
    ("OBC certificate banwane ka kharcha kitna hai?", "3", "hi", False),
    ("online apply karne ka kya process hai?", "3", "hi", True),
    ("kya isme income details deni hoti hai?", "3", "hi", True),
    ("process me kitne working days lagte hain?", "3", "hi", True),
    
    # --- Block 5: Out of Scope filtering ---
    ("how can I cook biryani?", None, "en", False),
    ("who is the president of america?", None, "en", False),
    ("chhattisgarh me kitne districts hain?", None, "hi", False),
    
    # --- Block 6: Marriage Certificate ---
    ("marriage certificate ke liye kaise register karein?", "1", "hi", False),
    ("kya marriage certificate offline gram panchayat se milega?", "1", "hi", True),
    ("invitation card upload karna zaroori hai?", "1", "hi", True),
    ("kya dono bride aur groom ke age certificate mandatory hain?", "1", "hi", True),
    ("shadi register karne ki time limit kya hai?", "1", "hi", True),
    
    # --- Block 7: Switch to Name Change ---
    ("naam badalne ka gazette notification kaise banwayein?", "5", "hi", True),
    ("is process me kitne din lagte hain?", "5", "hi", True),
    ("affidavit kitne rupaye ka stamp paper par banta hai?", "5", "hi", True),
    ("newspaper me advertisement kaise publish karwana hai?", "5", "hi", True),
    
    # --- Block 8: Conversational filler & thanks ---
    ("thank you so much for the detailed information", None, "en", False),
    ("bye bye", None, "en", False),
    
    # --- Block 9: Rapid Service Switches (aspect carry-over) ---
    ("caste certificate ki online application fee kitni hai?", "2", "hi", False),
    ("aur domicile ki?", "4", "hi", True),
    ("aur obc certificate ki?", "3", "hi", True),
    ("marriage registration ki kitni hai?", "1", "hi", True),
    ("name change notification ki fee kitni hai?", "5", "hi", True),
    
    # --- Block 10: Special Documents requirements checks ---
    ("kya OBC certificate me self-declaration mandatory hai?", "3", "hi", False),
    ("aur SC/ST certificate me?", "2", "hi", True),
    ("name change notification me witnesses ke sign zaroori hain?", "5", "hi", True),
    ("kya dono witnesses ka ID proof upload karna hoga?", "5", "hi", True),
    
    # --- Block 11: Switch back to Marriage ---
    ("marriage registration ke liye fees detail batayein", "1", "hi", True),
    ("kya online payment ho sakta hai?", "1", "hi", True),
    ("shadi register karne me kitna time lagta hai?", "1", "hi", True),
    
    # --- Block 12: Domicile exceptions path ---
    ("domicile certificate criteria three exceptions rules kya hain?", "4", "hi", False),
    ("kya isme 15 saal chhattisgarh stay proof zaroori hai?", "4", "hi", True),
    ("kya central government employee ke children eligible hain exception me?", "4", "hi", True),
    
    # --- Block 13: OBC validation ---
    ("obc certificate validation validity kitne time ki hoti hai?", "3", "hi", False),
    ("kya isko renew karwana padta hai?", "3", "hi", True),
    
    # --- Block 14: Greetings & casual closure ---
    ("hello sewasetu assistant", None, "en", False),
    ("thanks a lot!", None, "en", False),
    ("good night", None, "en", False),
    ("have a great day ahead", None, "en", True)
]


def send_query(query, selected_sno, language, messages_history):
    """Send a single query to the API and return the response."""
    # Build messages array
    messages = list(messages_history)  # copy
    messages.append({"role": "user", "content": query})
    
    payload = {
        "messages": messages,
        "selected_sno": selected_sno,
        "language": language,
        "detailed": True,
        "interactive": False,
        "is_option_click": False
    }
    
    try:
        start_time = time.time()
        resp = requests.post(API_URL, json=payload, timeout=120)
        elapsed = time.time() - start_time
        
        if resp.status_code == 200:
            data = resp.json()
            return data, elapsed, None
        else:
            return None, elapsed, f"HTTP {resp.status_code}: {resp.text[:200]}"
    except Exception as e:
        return None, 0, str(e)


def write_results(results, filepath):
    """Write all results to markdown file."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# SewaSetu RAG Test Results\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Total Queries:** {len(results)}\n\n")
        f.write("---\n\n")
        
        for i, r in enumerate(results):
            status_icon = "✅" if not r.get("error") else "❌"
            follow_up_tag = "🔄 Follow-up" if r.get("is_follow_up_input") else "🆕 New Topic"
            
            f.write(f"## Query {i+1}: {status_icon} {follow_up_tag}\n\n")
            f.write(f"**User Query:** `{r['query']}`\n\n")
            f.write(f"**Service sno:** `{r['selected_sno']}` | **Language:** `{r['language']}` | **Time:** `{r.get('elapsed', 0):.1f}s`\n\n")
            
            if r.get("error"):
                f.write(f"**Error:** {r['error']}\n\n")
                f.write("---\n\n")
                continue
            
            # Intermediate steps
            f.write("### Intermediate Steps\n\n")
            f.write("| Step | Value |\n")
            f.write("|------|-------|\n")
            
            data = r.get("data", {})
            
            # Query language detection
            f.write(f"| Detected Language | `{data.get('query_lang', 'N/A')}` |\n")
            
            # English translation
            en_q = data.get("english_query", "N/A")
            if en_q and len(en_q) > 80:
                en_q = en_q[:80] + "..."
            f.write(f"| English Query | `{en_q}` |\n")
            
            # Hindi translation
            hi_q = data.get("hindi_query", "N/A")
            if hi_q and len(hi_q) > 80:
                hi_q = hi_q[:80] + "..."
            f.write(f"| Hindi Query | `{hi_q}` |\n")
            
            # Service ID
            f.write(f"| Service ID | `{data.get('service_id', 'N/A')}` |\n")
            
            f.write("\n")
            
            # English intermediate answer
            en_ans = data.get("english_answer", "")
            if en_ans:
                f.write("#### English Intermediate Answer\n\n")
                if len(en_ans) > 500:
                    f.write(f"{en_ans[:500]}...\n\n")
                else:
                    f.write(f"{en_ans}\n\n")
            
            # Hindi intermediate answer
            hi_ans = data.get("hindi_answer", "")
            if hi_ans:
                f.write("#### Hindi Intermediate Answer\n\n")
                if len(hi_ans) > 500:
                    f.write(f"{hi_ans[:500]}...\n\n")
                else:
                    f.write(f"{hi_ans}\n\n")
            
            # Final response
            response = data.get("response", "N/A")
            f.write("### Final Response\n\n")
            if len(response) > 800:
                f.write(f"{response[:800]}...\n\n")
            else:
                f.write(f"{response}\n\n")
            
            f.write("---\n\n")
    
    print(f"  -> Results written to {filepath}")


def main():
    print(f"Starting 50-query test at {datetime.now().strftime('%H:%M:%S')}")
    print(f"API: {API_URL}")
    print(f"Results: {RESULTS_FILE}")
    print("=" * 60)
    
    results = []
    messages_history = []  # Running conversation history
    
    for i, (query, sno, lang, is_follow_up) in enumerate(QUERIES):
        # If not a follow-up, clear conversation history
        if not is_follow_up:
            messages_history = []
        
        print(f"\n[{i+1}/{len(QUERIES)}] {'FOLLOW-UP' if is_follow_up else 'NEW'} | sno={sno} | {query.encode('ascii', 'ignore').decode('ascii')}")
        
        data, elapsed, error = send_query(query, sno, lang, messages_history)
        
        result = {
            "query": query,
            "selected_sno": sno,
            "language": lang,
            "is_follow_up_input": is_follow_up,
            "elapsed": elapsed,
            "error": error,
            "data": data or {}
        }
        results.append(result)
        
        if error:
            print(f"  [FAIL] Error: {error}")
        else:
            response_text = data.get("response", "")
            preview = response_text[:100].replace("\n", " ") + ("..." if len(response_text) > 100 else "")
            safe_preview = preview.encode('ascii', 'ignore').decode('ascii')
            print(f"  [OK] ({elapsed:.1f}s) {safe_preview}")
            
            # Update conversation history for follow-ups
            messages_history.append({"role": "user", "content": query})
            messages_history.append({"role": "assistant", "content": response_text})
        
        # Write results after EVERY query
        write_results(results, RESULTS_FILE)
        
        # Small delay to not overwhelm the API
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print(f"Test complete! {len(results)} queries processed.")
    print(f"Results saved to {RESULTS_FILE}")
    
    # Summary
    errors = sum(1 for r in results if r.get("error"))
    avg_time = sum(r.get("elapsed", 0) for r in results if not r.get("error")) / max(1, len(results) - errors)
    print(f"Errors: {errors}/{len(results)}")
    print(f"Avg response time: {avg_time:.1f}s")


if __name__ == "__main__":
    main()
