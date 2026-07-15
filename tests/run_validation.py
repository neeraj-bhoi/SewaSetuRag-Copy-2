import os
import sys
import json
import time
from fastapi.testclient import TestClient

# Adjust path to import backend modules
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "05_webui"))

from backend.main import app

client = TestClient(app)

# Define 50 test cases grouped by session to simulate conversational turns
test_cases = [
    # === Session 1: General & Out of Scope ===
    {"id": 1, "session": 1, "query": "hi", "sno": "1", "reset_history": True},
    {"id": 2, "session": 1, "query": "what is the weather today?", "sno": "1", "reset_history": False},
    {"id": 3, "session": 1, "query": "explain gravity", "sno": "1", "reset_history": False},
    {"id": 4, "session": 1, "query": "what is sewasetu?", "sno": "1", "reset_history": False},
    {"id": 5, "session": 1, "query": "bye", "sno": "1", "reset_history": False},

    # === Session 2: Marriage Certificate Flow ===
    {"id": 6, "session": 2, "query": "marriage certificate apply kaise karein", "sno": "1", "reset_history": True},
    {"id": 7, "session": 2, "query": "raipur me shadi hui hai kaha apply karein", "sno": "1", "reset_history": False},
    {"id": 8, "session": 2, "query": "fees kitni hai", "sno": "1", "reset_history": False},
    {"id": 9, "session": 2, "query": "documents list", "sno": "1", "reset_history": False},
    {"id": 10, "session": 2, "query": "what is kiosk fee for marriage certificate?", "sno": "1", "reset_history": False},
    {"id": 11, "session": 2, "query": "who is the registrar for marriage registration in village?", "sno": "1", "reset_history": False},
    {"id": 12, "session": 2, "query": "ok thank you", "sno": "1", "reset_history": False},

    # === Session 3: Caste Certificates - SC/ST Flow ===
    {"id": 13, "session": 3, "query": "caste certificate sc st ke liye apply kaise karein", "sno": "2", "reset_history": True},
    {"id": 14, "session": 3, "query": "cg st certificate ke liye documents", "sno": "2", "reset_history": False},
    {"id": 15, "session": 3, "query": "kya st praman patra ke liye digital signature chahiye?", "sno": "2", "reset_history": False},
    {"id": 16, "session": 3, "query": "st caste praman patra timeline", "sno": "2", "reset_history": False},
    {"id": 17, "session": 3, "query": "sc caste list cg", "sno": "2", "reset_history": False},
    {"id": 18, "session": 3, "query": "how to verify cast certificate status?", "sno": "2", "reset_history": False},
    {"id": 19, "session": 3, "query": "thanks", "sno": "2", "reset_history": False},

    # === Session 4: OBC Certificate Flow ===
    {"id": 20, "session": 4, "query": "OBC certificate praman patra fees kya hai?", "sno": "3", "reset_history": True},
    {"id": 21, "session": 4, "query": "OBC certificate ke liye income limit kitni hai?", "sno": "3", "reset_history": False},
    {"id": 22, "session": 4, "query": "OBC list CG", "sno": "3", "reset_history": False},
    {"id": 23, "session": 4, "query": "is digital signature mandatory for OBC?", "sno": "3", "reset_history": False},
    {"id": 24, "session": 4, "query": "can non residents apply for obc certificate in cg?", "sno": "3", "reset_history": False},
    {"id": 25, "session": 4, "query": "ok bye", "sno": "3", "reset_history": False},

    # === Session 5: Domicile Certificate Flow ===
    {"id": 26, "session": 5, "query": "CG ka domicile certificate kaise banayein?", "sno": "4", "reset_history": True},
    {"id": 27, "session": 5, "query": "domicile certificate cg eligibility rules", "sno": "4", "reset_history": False},
    {"id": 28, "session": 5, "query": "kya school study cg me 3 saal hona mandatory hai?", "sno": "4", "reset_history": False},
    {"id": 29, "session": 5, "query": "niwas praman patra exceptions list", "sno": "4", "reset_history": False},
    {"id": 30, "session": 5, "query": "kya out of state domicile certificate mil sakta hai?", "sno": "4", "reset_history": False},
    {"id": 31, "session": 5, "query": "how many days for domicile certificate?", "sno": "4", "reset_history": False},
    {"id": 32, "session": 5, "query": "is voter id proof of stay for domicile?", "sno": "4", "reset_history": False},

    # === Session 6: Name Change Flow ===
    {"id": 33, "session": 6, "query": "naam badalne ka kya process hai", "sno": "5", "reset_history": True},
    {"id": 34, "session": 6, "query": "gazette publication name change advertisement fee", "sno": "5", "reset_history": False},
    {"id": 35, "session": 6, "query": "affidavit stamp paper fee for name change", "sno": "5", "reset_history": False},
    {"id": 36, "session": 6, "query": "time limit for name change gazette", "sno": "5", "reset_history": False},
    {"id": 37, "session": 6, "query": "name change gazette notification witnesses need?", "sno": "5", "reset_history": False},
    {"id": 38, "session": 6, "query": "gazette advertisement form I format", "sno": "5", "reset_history": False},
    {"id": 39, "session": 6, "query": "what is the total cost for name change in cg?", "sno": "5", "reset_history": False},

    # === Session 7: Context Switch & Topic Swapping ===
    {"id": 40, "session": 7, "query": "shadi ke baad name change process", "sno": "1", "reset_history": True},
    {"id": 41, "session": 7, "query": "caste certificate CG online link", "sno": "1", "reset_history": False},
    {"id": 42, "session": 7, "query": "raipur municipal corporation office location for marriage", "sno": "1", "reset_history": False},
    {"id": 43, "session": 7, "query": "shadi praman patra documents list", "sno": "1", "reset_history": False},

    # === Session 8: Random / Test Queries ===
    {"id": 44, "session": 8, "query": "hola", "sno": "4", "reset_history": True},
    {"id": 45, "session": 8, "query": "cg government website", "sno": "4", "reset_history": False},
    {"id": 46, "session": 8, "query": "how to write code", "sno": "4", "reset_history": False},
    {"id": 47, "session": 8, "query": "mujhe checklist do", "sno": "4", "reset_history": False},
    {"id": 48, "session": 8, "query": "what is the fee?", "sno": "4", "reset_history": False},
    {"id": 49, "session": 8, "query": "namaste", "sno": "4", "reset_history": False},
    {"id": 50, "session": 8, "query": "thanks a lot", "sno": "4", "reset_history": False}
]

# Paths
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(TESTS_DIR, "evaluation_results.md")

# Initialize markdown report
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("# SewaSetu Chatbot: 50-Query Validation Results\n\n")
    f.write("This audit report captures standard test runs, mapping classification outputs, translation phases, context details, and synthesized replies.\n\n")
    f.write("| ID | Session | User Query | Target Active sno | Latency | Language | Classified Service ID | Intent |\n")
    f.write("|----|---------|------------|-------------------|---------|----------|-----------------------|--------|\n")

history = []

print(f"Starting test execution. Progress will be updated in: {REPORT_PATH}")

for tc in test_cases:
    tc_id = tc["id"]
    query = tc["query"]
    sno = tc["sno"]
    session = tc["session"]
    
    if tc["reset_history"]:
        history = []

    # Prepare chat payload
    payload = {
        "messages": history + [{"role": "user", "content": query}],
        "selected_sno": sno,
        "language": "en",
        "detailed": True,
        "interactive": True,
        "is_option_click": False
    }

    start_time = time.time()
    
    # Call the API
    try:
        response = client.post("/api/chat", json=payload)
        latency = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract returned values
            res_text = data.get("response", data.get("text", "No text response"))
            q_lang = data.get("query_lang", "N/A")
            english_q = data.get("english_query", "N/A")
            hindi_q = data.get("hindi_query", "N/A")
            context_en = data.get("context_en", "")
            context_hi = data.get("context_hi", "")
            ans_en = data.get("english_answer", "N/A")
            ans_hi = data.get("hindi_answer", "N/A")
            service_id = data.get("service_id", "N/A")
            
            # Parse intent classification
            intent = data.get("intent")
            if not intent:
                if data.get("mode") == "options":
                    intent = "Interactive Checkpoint Intercept"
                elif "canned" in res_text.lower() or "welcome" in res_text.lower() or "thank" in res_text.lower() or "goodbye" in res_text.lower() or "sorry" in res_text.lower():
                    intent = "Canned/Intercept"
                else:
                    intent = "RAG Query"
            
            # Append conversation history
            history.append({"role": "user", "content": query})
            history.append({"role": "assistant", "content": res_text})
            # Limit history to 6 messages to follow client logic
            if len(history) > 6:
                history = history[-6:]

            # Append to table in markdown file
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"| {tc_id} | {session} | `{query}` | {sno} | {latency:.2f}s | {q_lang} | {service_id} | {intent} |\n")

            # Append detailed block
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"\n### Query {tc_id} Details\n")
                f.write(f"* **Query**: `{query}`\n")
                f.write(f"* **Selected SNO**: {sno}\n")
                f.write(f"* **Detected Language**: `{q_lang}`\n")
                f.write(f"* **Classified Service ID**: `{service_id}`\n")
                f.write(f"* **Classified Intent**: `{intent}`\n")
                f.write(f"* **Resolved English Query**: `{english_q}`\n")
                f.write(f"* **Resolved Hindi Query**: `{hindi_q}`\n")
                
                if ans_en and ans_en != "N/A":
                    f.write(f"* **Intermediate English Answer**:\n  > {ans_en.replace(chr(10), chr(10) + '  > ')}\n")
                if ans_hi and ans_hi != "N/A":
                    f.write(f"* **Intermediate Hindi Answer**:\n  > {ans_hi.replace(chr(10), chr(10) + '  > ')}\n")
                f.write(f"* **Final Synthesized Response**:\n  > {res_text.replace(chr(10), chr(10) + '  > ')}\n\n")
                
                # Append LLM Calls Trace
                llm_calls = data.get("llm_calls_trace", [])
                if llm_calls:
                    f.write("* **LLM Call Trace**:\n")
                    for idx, call in enumerate(llm_calls):
                        func = call.get("function")
                        inp = call.get("input")
                        out = call.get("output")
                        
                        inp_str = json.dumps(inp, indent=2, ensure_ascii=False) if isinstance(inp, (dict, list)) else str(inp)
                        out_str = json.dumps(out, indent=2, ensure_ascii=False) if isinstance(out, (dict, list)) else str(out)
                        
                        # Truncate very long inputs/outputs to keep markdown clean
                        if len(inp_str) > 1000:
                            inp_str = inp_str[:1000] + "\n... [TRUNCATED FOR BREVITY] ..."
                        if len(out_str) > 1000:
                            out_str = out_str[:1000] + "\n... [TRUNCATED FOR BREVITY] ..."
                            
                        f.write(f"  {idx+1}. **Function**: `{func}`\n")
                        f.write(f"     * **Input**:\n")
                        f.write(f"       ```json\n       {inp_str.replace(chr(10), chr(10) + '       ')}\n       ```\n")
                        f.write(f"     * **Response**:\n")
                        f.write(f"       ```json\n       {out_str.replace(chr(10), chr(10) + '       ')}\n       ```\n")
                
                f.write("---\n")
                
            print(f"[{tc_id}/50] Query: '{query}' -> Lang: {q_lang}, ServID: {service_id}, Status: SUCCESS ({latency:.2f}s)")

        else:
            latency = time.time() - start_time
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"| {tc_id} | {session} | `{query}` | {sno} | {latency:.2f}s | N/A | N/A | ERROR ({response.status_code}) |\n")
            print(f"[{tc_id}/50] Query: '{query}' -> Status: ERROR ({response.status_code}, {latency:.2f}s)")
            
    except Exception as e:
        latency = time.time() - start_time
        with open(REPORT_PATH, "a", encoding="utf-8") as f:
            f.write(f"| {tc_id} | {session} | `{query}` | {sno} | {latency:.2f}s | N/A | N/A | EXCEPTION ({str(e)}) |\n")
        print(f"[{tc_id}/50] Query: '{query}' -> Status: EXCEPTION ({str(e)}, {latency:.2f}s)")

print(f"Completed! Validation report generated successfully: {REPORT_PATH}")
