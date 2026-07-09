import os
import sys
import json
import time
from fastapi.testclient import TestClient

# Adjust path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

client = TestClient(app)

# Define 50 confusing test cases that mix multiple service concepts
# Expected classification is indicated by expected_service_id
test_cases = [
    {"id": 1, "query": "shadi ke baad naam change kaise karein?", "expected_service_id": 201},
    {"id": 2, "query": "is domicile necessary for obc certificate?", "expected_service_id": 5},
    {"id": 3, "query": "caste certificate ke liye niwas praman patra ki eligibility kya hai?", "expected_service_id": 4},
    {"id": 4, "query": "obc certificate banane ke liye cg ka domicile hona zaroori hai?", "expected_service_id": 5},
    {"id": 5, "query": "shadi certificate me name correction kaise karein?", "expected_service_id": 201}, # Corrected
    {"id": 6, "query": "st certificate ke documents me domicile praman patra lagta hai kya?", "expected_service_id": 4},
    {"id": 7, "query": "niwas praman patra ke liye caste certificate chahiye?", "expected_service_id": 7},
    {"id": 8, "query": "gazette notification name change ke liye marriage certificate mandatory hai?", "expected_service_id": 201},
    {"id": 9, "query": "caste validation rules in cg domicile certificate", "expected_service_id": 7},
    {"id": 10, "query": "can a married woman apply for domicile certificate using father's address?", "expected_service_id": 7},
    {"id": 11, "query": "obc certificate and sc st certificate difference in fees", "expected_service_id": None}, # Comparison
    {"id": 12, "query": "marriage certificate apply online using caste certificate details", "expected_service_id": 3},
    {"id": 13, "query": "obc praman patra me domicile praman patra rules", "expected_service_id": 5},
    {"id": 14, "query": "shadi praman patra ke sath name change ka affidavit lagega?", "expected_service_id": 201}, # Corrected
    {"id": 15, "query": "niwas praman patra cg fees vs caste certificate fees", "expected_service_id": None}, # Comparison
    {"id": 16, "query": "gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper", "expected_service_id": 201},
    {"id": 17, "query": "do we need sc certificate for obc scholarship application?", "expected_service_id": None}, # Out of Scope
    {"id": 18, "query": "is digital signature of sdo for st certificate same as domicile?", "expected_service_id": None}, # Comparison
    {"id": 19, "query": "obc non-creamy layer certificate me domicile conditions", "expected_service_id": 5},
    {"id": 20, "query": "naam badalne ke baad marriage certificate update kaise hoga?", "expected_service_id": 201},
    {"id": 21, "query": "what is the timeline for domicile certificate compared to obc certificate?", "expected_service_id": 7},
    {"id": 22, "query": "caste certificate st sc validity vs niwas praman patra validity", "expected_service_id": 4},
    {"id": 23, "query": "marriage registration offline location Raipur municipal corporation rules for out of state domicile", "expected_service_id": 3},
    {"id": 24, "query": "gazette notification rules for name change after divorce decree", "expected_service_id": 201},
    {"id": 25, "query": "sc certificate application with mother's domicile certificate", "expected_service_id": 4},
    {"id": 26, "query": "obc certificate download online using caste registry credentials", "expected_service_id": 5},
    {"id": 27, "query": "shadi praman patra eligibility for non-domicile of cg", "expected_service_id": 3},
    {"id": 28, "query": "caste certificate correction name change application format", "expected_service_id": 201}, # Corrected
    {"id": 29, "query": "is 15 years stay domicile rule applicable for obc certificate?", "expected_service_id": 5},
    {"id": 30, "query": "gazette notification cost for change of name vs marriage certificate online fee", "expected_service_id": 201},
    {"id": 31, "query": "can married daughters apply for st certificate using father's caste proof?", "expected_service_id": 4},
    {"id": 32, "query": "niwas praman patra ke liye school study cg me 3 saal rule obc ke liye bhi hai?", "expected_service_id": 7},
    {"id": 33, "query": "caste certificate digital signature verification vs domicile verification status", "expected_service_id": None}, # Comparison
    {"id": 34, "query": "marriage registrar local area authority in village for caste certificate holders", "expected_service_id": 3}, # Corrected
    {"id": 35, "query": "is it mandatory to submit marriage invitation card for name change in gazette?", "expected_service_id": 201},
    {"id": 36, "query": "obc certificate fee payment online cg state vs sc st certificate online fee", "expected_service_id": 5},
    {"id": 37, "query": "domicile certificate cg eligibility criteria for central govt employees vs cg state st employees", "expected_service_id": 7},
    {"id": 38, "query": "name change publication in gazette timeline vs marriage certificate timeline", "expected_service_id": 201},
    {"id": 39, "query": "caste certificate offline tehsil office address for obc domicile", "expected_service_id": 4},
    {"id": 40, "query": "is notarized affidavit in Form-III for name change same as marriage affidavit?", "expected_service_id": 201}, # Corrected
    {"id": 41, "query": "st caste praman patra verification with land documents and domicile certificate", "expected_service_id": 4},
    {"id": 42, "query": "obc income certificate slab details for domicile students", "expected_service_id": None}, # Out of Scope
    {"id": 43, "query": "can we apply for marriage certificate and name change together on sewasetu?", "expected_service_id": None}, # Generic multi-service
    {"id": 44, "query": "what are the documents for sc caste certificate list if i already have domicile?", "expected_service_id": 4},
    {"id": 45, "query": "niwas praman patra rules for spouse of cg domicile person", "expected_service_id": 7},
    {"id": 46, "query": "fees of obc certificate vs ordinary gazette publication fee", "expected_service_id": None}, # Comparison
    {"id": 47, "query": "is voter id mandatory for st certificate if i have school study certificate?", "expected_service_id": 4},
    {"id": 48, "query": "where to submit marriage certificate application if husband belongs to other state?", "expected_service_id": 3},
    {"id": 49, "query": "can a name change gazette be used to correct name in obc certificate?", "expected_service_id": 201},
    {"id": 50, "query": "caste certificate validity timeline for married women", "expected_service_id": 4}
]

# Paths
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(TESTS_DIR, "confused_queries_results.md")

# Initialize markdown report
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("# SewaSetu Chatbot: 50 Confusing Queries Validation Results\n\n")
    f.write("This report captures validation runs of confusing queries that mix multiple government service concepts in a single request.\n\n")
    f.write("| ID | Confusing User Query | Expected Service ID | Mapped Service ID | Match Status | Intent | Latency |\n")
    f.write("|----|----------------------|---------------------|-------------------|--------------|--------|---------|\n")

print(f"Starting confusing queries validation test execution. Progress will be updated in: {REPORT_PATH}")

for tc in test_cases:
    tc_id = tc["id"]
    query = tc["query"]
    expected_id = tc["expected_service_id"]
    
    # We run standalone chat requests (no history) to check standard classification/routing robustness
    payload = {
        "messages": [{"role": "user", "content": query}],
        "selected_sno": "1",  # Reset to 1 initially to force classification
        "language": "en",
        "detailed": True,
        "interactive": True,
        "is_option_click": False
    }

    start_time = time.time()
    
    try:
        response = client.post("/api/chat", json=payload)
        latency = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            
            res_text = data.get("response", data.get("text", "No text response"))
            q_lang = data.get("query_lang", "N/A")
            english_q = data.get("english_query", "N/A")
            hindi_q = data.get("hindi_query", "N/A")
            ans_en = data.get("english_answer", "N/A")
            ans_hi = data.get("hindi_answer", "N/A")
            service_id = data.get("service_id", "N/A")
            intent = data.get("intent", "new_topic")
            
            # Check match status
            service_id_num = None
            try:
                service_id_num = int(service_id)
            except:
                pass
            
            match_status = "✅ MATCH" if service_id_num == expected_id else "❌ MISMATCH"
            
            # Append to summary table
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"| {tc_id} | `{query}` | {expected_id} | {service_id} | {match_status} | {intent} | {latency:.2f}s |\n")

            # Append detailed traces
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"\n### Query {tc_id} Details\n")
                f.write(f"* **Query**: `{query}`\n")
                f.write(f"* **Expected Service ID**: `{expected_id}`\n")
                f.write(f"* **Classified Service ID**: `{service_id}`\n")
                f.write(f"* **Match Status**: {match_status}\n")
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
                
            print(f"[{tc_id}/50] Confusing Query: '{query}' -> Expected: {expected_id}, Classified: {service_id} ({match_status})")
            
        else:
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"| {tc_id} | `{query}` | {expected_id} | N/A | ERROR ({response.status_code}) | N/A | {latency:.2f}s |\n")
            print(f"[{tc_id}/50] Confusing Query: '{query}' -> Status: ERROR ({response.status_code})")
            
    except Exception as e:
        with open(REPORT_PATH, "a", encoding="utf-8") as f:
            f.write(f"| {tc_id} | `{query}` | {expected_id} | N/A | EXCEPTION ({str(e)}) | N/A | 0.00s |\n")
        print(f"[{tc_id}/50] Confusing Query: '{query}' -> Status: EXCEPTION ({str(e)})")

print(f"Completed! Validation report generated successfully: {REPORT_PATH}")
