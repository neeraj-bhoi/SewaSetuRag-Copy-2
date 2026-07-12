import os
import sys
import time
import requests
import json
import asyncio
from fastapi.testclient import TestClient

# Adjust path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

client = TestClient(app)

# 50 confusing test cases pre-translated to Hindi with corrected expected service IDs
test_cases = [
    {"id": 1, "query": "शादी के बाद नाम परिवर्तन कैसे करें?", "expected_service_id": 201},
    {"id": 2, "query": "क्या ओबीसी प्रमाणपत्र के लिए निवास प्रमाणपत्र आवश्यक है?", "expected_service_id": 5},
    {"id": 3, "query": "जाति प्रमाण पत्र के लिए निवास प्रमाण पत्र की पात्रता क्या है?", "expected_service_id": 4},
    {"id": 4, "query": "ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का निवास प्रमाण पत्र होना जरूरी है?", "expected_service_id": 5},
    {"id": 5, "query": "शादी प्रमाणपत्र में नाम सुधार कैसे करें?", "expected_service_id": 201},
    {"id": 6, "query": "एसटी प्रमाण पत्र के दस्तावेजों में निवास प्रमाण पत्र लगता है क्या?", "expected_service_id": 4},
    {"id": 7, "query": "निवास प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?", "expected_service_id": 7},
    {"id": 8, "query": "राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह प्रमाण पत्र अनिवार्य है?", "expected_service_id": 201},
    {"id": 9, "query": "छत्तीसगढ़ निवास प्रमाण पत्र में जाति सत्यापन नियम", "expected_service_id": 7},
    {"id": 10, "query": "क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके निवास प्रमाण पत्र के लिए आवेदन कर सकती है?", "expected_service_id": 7},
    {"id": 11, "query": "ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?", "expected_service_id": None},
    {"id": 12, "query": "जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?", "expected_service_id": 3},
    {"id": 13, "query": "ओबीसी प्रमाण पत्र में निवास प्रमाण पत्र के नियम", "expected_service_id": 5},
    {"id": 14, "query": "शादी प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र लगेगा?", "expected_service_id": 201},
    {"id": 15, "query": "निवास प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क", "expected_service_id": None},
    {"id": 16, "query": "राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र स्टाम्प पेपर", "expected_service_id": None},
    {"id": 17, "query": "क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?", "expected_service_id": None},
    {"id": 18, "query": "क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर निवास प्रमाण पत्र के समान है?", "expected_service_id": 4},
    {"id": 19, "query": "ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें", "expected_service_id": 5},
    {"id": 20, "query": "नाम बदलने के बाद विवाह प्रमाण पत्र अपडेट कैसे होगा?", "expected_service_id": 201},
    {"id": 21, "query": "ओबीसी प्रमाण पत्र की तुलना में निवास प्रमाण पत्र की समय सीमा क्या है?", "expected_service_id": None},
    {"id": 22, "query": "जाति प्रमाण पत्र एसटी एससी वैधता बनाम निवास प्रमाण पत्र वैधता", "expected_service_id": None},
    {"id": 23, "query": "बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम", "expected_service_id": 3},
    {"id": 24, "query": "तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम", "expected_service_id": 201},
    {"id": 25, "query": "माता के निवास प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन", "expected_service_id": 4},
    {"id": 26, "query": "जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें", "expected_service_id": 5},
    {"id": 27, "query": "छत्तीसगढ़ के गैर-निवासी के लिए शादी प्रमाण पत्र की पात्रता", "expected_service_id": 3},
    {"id": 28, "query": "जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप", "expected_service_id": 201},
    {"id": 29, "query": "क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?", "expected_service_id": 5},
    {"id": 30, "query": "नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह प्रमाण पत्र ऑनलाइन शुल्क", "expected_service_id": None},
    {"id": 31, "query": "क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?", "expected_service_id": 4},
    {"id": 32, "query": "क्या निवास प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?", "expected_service_id": 7},
    {"id": 33, "query": "जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति", "expected_service_id": 4},
    {"id": 34, "query": "जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण", "expected_service_id": 3},
    {"id": 35, "query": "क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?", "expected_service_id": 201},
    {"id": 36, "query": "ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क", "expected_service_id": 5},
    {"id": 37, "query": "केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए निवास प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड", "expected_service_id": 7},
    {"id": 38, "query": "राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह प्रमाण पत्र की समय सीमा", "expected_service_id": None},
    {"id": 39, "query": "ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता", "expected_service_id": 4},
    {"id": 40, "query": "क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र विवाह शपथ पत्र के समान है?", "expected_service_id": None},
    {"id": 41, "query": "भूमि दस्तावेजों और निवास प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन", "expected_service_id": 4},
    {"id": 42, "query": "निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण", "expected_service_id": None},
    {"id": 43, "query": "क्या हम सेवासेतु पर विवाह प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?", "expected_service_id": None},
    {"id": 44, "query": "यदि मेरे पास पहले से ही निवास प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?", "expected_service_id": 4},
    {"id": 45, "query": "छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए निवास प्रमाण पत्र के नियम", "expected_service_id": 7},
    {"id": 46, "query": "ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क", "expected_service_id": None},
    {"id": 47, "query": "क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?", "expected_service_id": 4},
    {"id": 48, "query": "यदि पति दूसरे राज्य से संबंधित है तो विवाह प्रमाण पत्र का आवेदन कहां जमा करें?", "expected_service_id": 3},
    {"id": 49, "query": "क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?", "expected_service_id": 201},
    {"id": 50, "query": "विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा", "expected_service_id": 4}
]

# Paths
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(TESTS_DIR, "confused_queries_results_hindi.md")

# Initialize markdown report
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("# SewaSetu Chatbot: 50 Confusing Queries Validation Results (Hindi Language)\n\n")
    f.write("This report captures validation runs of confusing queries typed directly in Devanagari Hindi.\n\n")
    f.write("| ID | Confusing Hindi User Query | Expected Service ID | Mapped Service ID | Match Status | Intent | Latency |\n")
    f.write("|----|----------------------------|---------------------|-------------------|--------------|--------|---------|\n")

print(f"Starting confusing queries validation test execution (Hindi). Progress will be updated in: {REPORT_PATH}")

async def run_validation():
    passed = 0
    total = len(test_cases)
    
    for tc in test_cases:
        tc_id = tc["id"]
        query = tc["query"]
        expected_id = tc["expected_service_id"]
        
        payload = {
            "messages": [{"role": "user", "content": query}],
            "selected_sno": "1",  # Reset to 1 initially to force classification
            "language": "hi",
            "detailed": True,
            "interactive": True,
            "is_option_click": False
        }
        
        start_time = time.time()
        try:
            # We mock the async call using FastAPI TestClient
            response = client.post("/api/chat", json=payload)
            latency = time.time() - start_time
            
            if response.status_code == 200:
                res_data = response.json()
                bot_response = res_data.get("response", "")
                mapped_id = res_data.get("service_id")
                # Normalize values for check comparison
                mapped_normalized = int(mapped_id) if mapped_id is not None else None
                expected_normalized = int(expected_id) if expected_id is not None else None
                
                # Special cases matching
                is_match = (mapped_normalized == expected_normalized)
                status_str = "✅ MATCH" if is_match else "❌ MISMATCH"
                if is_match:
                    passed += 1
                
                intent_val = res_data.get("intent", "new_topic")
                
                # Append result row to the MD report table
                with open(REPORT_PATH, "a", encoding="utf-8") as f:
                    f.write(f"| {tc_id} | `{query}` | {expected_id} | {mapped_id} | {status_str} | {intent_val} | {latency:.2f}s |\n")
                
                # Write individual details block to MD
                with open(REPORT_PATH, "a", encoding="utf-8") as f:
                    f.write(f"\n### Query {tc_id} Details\n")
                    f.write(f"* **Query**: `{query}`\n")
                    f.write(f"* **Expected Service ID**: `{expected_id}`\n")
                    f.write(f"* **Classified Service ID**: `{mapped_id}`\n")
                    f.write(f"* **Match Status**: {status_str}\n")
                    f.write(f"* **Classified Intent**: `{intent_val}`\n")
                    f.write(f"* **Resolved English Query**: `{res_data.get('english_query', '')}`\n")
                    f.write(f"* **Resolved Hindi Query**: `{res_data.get('hindi_query', '')}`\n")
                    f.write(f"* **Intermediate English Answer**:\n  > {res_data.get('english_answer', '').replace(chr(10), chr(10) + '  > ')}\n")
                    f.write(f"* **Intermediate Hindi Answer**:\n  > {res_data.get('hindi_answer', '').replace(chr(10), chr(10) + '  > ')}\n")
                    f.write(f"* **Final Synthesized Response**:\n  > {bot_response.replace(chr(10), chr(10) + '  > ')}\n\n")
                    
                    # LLM Call traces
                    f.write(f"* **LLM Call Trace**:\n")
                    trace_list = res_data.get("llm_calls_trace", [])
                    for i, trace in enumerate(trace_list):
                        f.write(f"  {i+1}. **Function**: `{trace.get('function')}`\n")
                        f.write(f"     * **Input**:\n       ```json\n       {json.dumps(trace.get('input'), indent=2, ensure_ascii=False).replace(chr(10), chr(10) + '       ')}\n       ```\n")
                        f.write(f"     * **Response**:\n       ```json\n       {str(trace.get('output')).replace(chr(10), chr(10) + '       ')}\n       ```\n")
                
                print(f"[{tc_id}/{total}] Confusing Query: '{query}' -> Expected: {expected_id}, Classified: {mapped_id} ({status_str})")
            else:
                print(f"[{tc_id}/{total}] Confusing Query: '{query}' Failed with status code {response.status_code}")
        except Exception as e:
            print(f"[{tc_id}/{total}] Confusing Query: '{query}' Failed with exception: {e}")
            
    accuracy = (passed / total) * 100
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n## Summary Metrics\n")
        f.write(f"- Total Test Cases: {total}\n")
        f.write(f"- Passed Matches: {passed}\n")
        f.write(f"- Accuracy: {accuracy:.2f}%\n")
        
    print(f"Completed! Validation report generated successfully: {REPORT_PATH}")

if __name__ == "__main__":
    asyncio.run(run_validation())
