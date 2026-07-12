import os
import sys
import json
import time
from fastapi.testclient import TestClient

# Adjust path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

client = TestClient(app)

# 50 very random normal real-life user queries in English, Hindi, and Hinglish
test_cases = [
    # === Service 1: Marriage Registration & Certificate (SNO: 1, Service ID: 3) ===
    {
        "id": 1,
        "sno": "1",
        "language": "en",
        "query": "What is the official government fee to get a marriage certificate online in Chhattisgarh?",
        "service": "Marriage Registration"
    },
    {
        "id": 2,
        "sno": "1",
        "language": "hinglish",
        "query": "Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?",
        "service": "Marriage Registration"
    },
    {
        "id": 3,
        "sno": "1",
        "language": "hi",
        "query": "विवाह पंजीकरण के लिए आवश्यक दस्तावेजों की सूची क्या है?",
        "service": "Marriage Registration"
    },
    {
        "id": 4,
        "sno": "1",
        "language": "hinglish",
        "query": "Mera shadi ka card (invitation card) nahi hai, to kya online shadi register ho sakti hai?",
        "service": "Marriage Registration"
    },
    {
        "id": 5,
        "sno": "1",
        "language": "en",
        "query": "Is there any penalty or extra fee if I register my marriage after 1 year of marriage in CG?",
        "service": "Marriage Registration"
    },
    {
        "id": 6,
        "sno": "1",
        "language": "hi",
        "query": "विवाह प्रमाण पत्र प्राप्त करने की समय सीमा (SLA) कितने दिनों की होती है?",
        "service": "Marriage Registration"
    },
    {
        "id": 7,
        "sno": "1",
        "language": "hinglish",
        "query": "Online apply karne ke baad verification ke liye kya dono husband aur wife ko office jana padega?",
        "service": "Marriage Registration"
    },
    {
        "id": 8,
        "sno": "1",
        "language": "en",
        "query": "Who acts as the Registrar of Marriages in a small village or rural area in CG?",
        "service": "Marriage Registration"
    },
    {
        "id": 9,
        "sno": "1",
        "language": "hi",
        "query": "क्या ग्रामीण क्षेत्रों में पंचायत सचिव विवाह का रजिस्ट्रेशन कर सकते हैं?",
        "service": "Marriage Registration"
    },
    {
        "id": 10,
        "sno": "1",
        "language": "en",
        "query": "I got married in a temple in Bhilai. Can I get a government marriage certificate?",
        "service": "Marriage Registration"
    },

    # === Service 2: SC/ST Caste Certificate (SNO: 2, Service ID: 4) ===
    {
        "id": 11,
        "sno": "2",
        "language": "hi",
        "query": "छत्तीसगढ़ में एससी एसटी जाति प्रमाण पत्र के लिए पात्रता मानदंड क्या हैं?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 12,
        "sno": "2",
        "language": "hinglish",
        "query": "Caste certificate st/sc ke liye kaun kaun se government documents mandatory hain?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 13,
        "sno": "2",
        "language": "en",
        "query": "Is land record document (like B1/P2/Misal Bandobast) compulsory for SC certificate in CG?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 14,
        "sno": "2",
        "language": "hinglish",
        "query": "Mera purana hand-written offline SC certificate hai. Use online digital cert me kaise convert karein?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 15,
        "sno": "2",
        "language": "hi",
        "query": "क्या छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 16,
        "sno": "2",
        "language": "en",
        "query": "How long does it take for the Tehsil office to issue a permanent ST caste certificate?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 17,
        "sno": "2",
        "language": "hinglish",
        "query": "Caste certificate apply karne ke liye sewasetu portal ka direct link kya hai?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 18,
        "sno": "2",
        "language": "en",
        "query": "Which government officer is authorized to issue a permanent SC certificate in a district?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 19,
        "sno": "2",
        "language": "hi",
        "query": "क्या जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर (digital signature) जरूरी है?",
        "service": "SC/ST Caste Certificate"
    },
    {
        "id": 20,
        "sno": "2",
        "language": "hinglish",
        "query": "SC caste praman patra online apply karne me portal aur kiosk charge kitna lagta hai?",
        "service": "SC/ST Caste Certificate"
    },

    # === Service 3: OBC Caste Certificate (SNO: 3, Service ID: 5) ===
    {
        "id": 21,
        "sno": "3",
        "language": "hinglish",
        "query": "OBC certificate banane ke liye creamy layer aur non-creamy layer ki income limit kitni hai?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 22,
        "sno": "3",
        "language": "hi",
        "query": "ओबीसी जाति प्रमाण पत्र के लिए क्या निवास प्रमाण पत्र (domicile) जमा करना जरूरी है?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 23,
        "sno": "3",
        "language": "en",
        "query": "Can an OBC candidate apply for OBC certificate online on Sewa Setu portal?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 24,
        "sno": "3",
        "language": "hinglish",
        "query": "OBC non-creamy layer praman patra ke liye self-declaration affidavit ka format kaisa hona chahiye?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 25,
        "sno": "3",
        "language": "hi",
        "query": "छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि (validity period) कितनी होती है?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 26,
        "sno": "3",
        "language": "en",
        "query": "What are the specific form fields and details required to be filled for OBC certificate application?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 27,
        "sno": "3",
        "language": "hinglish",
        "query": "OBC certificate apply karte waqt lok seva kendra ya kiosk center me kitna extra charge liya jata hai?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 28,
        "sno": "3",
        "language": "hi",
        "query": "क्या किसी निजी स्कूल (private school) का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त है?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 29,
        "sno": "3",
        "language": "en",
        "query": "Is a separate income certificate mandatory to get a non-creamy layer OBC certificate?",
        "service": "OBC Caste Certificate"
    },
    {
        "id": 30,
        "sno": "3",
        "language": "hinglish",
        "query": "Bhai, agar parivar ki salana aamdani 8 lakh se jyada hai, to kya OBC certificate mil sakta hai?",
        "service": "OBC Caste Certificate"
    },

    # === Service 4: Domicile Certificate (SNO: 4, Service ID: 7) ===
    {
        "id": 31,
        "sno": "4",
        "language": "en",
        "query": "What is the exact residency criteria or years of stay required to get a Domicile Certificate in Chhattisgarh?",
        "service": "Domicile Certificate"
    },
    {
        "id": 32,
        "sno": "4",
        "language": "hinglish",
        "query": "Niwas praman patra cg ke liye exceptions kya hain? Jaise central govt employees ke liye?",
        "service": "Domicile Certificate"
    },
    {
        "id": 33,
        "sno": "4",
        "language": "hi",
        "query": "क्या छत्तीसगढ़ का निवास प्रमाण पत्र राज्य सरकार के सेवानिवृत्त (retired) कर्मचारियों के बच्चों को मिल सकता है?",
        "service": "Domicile Certificate"
    },
    {
        "id": 34,
        "sno": "4",
        "language": "hinglish",
        "query": "Kya domicile praman patra ke liye school study cg me minimum 3 saal hona zaroori hai?",
        "service": "Domicile Certificate"
    },
    {
        "id": 35,
        "sno": "4",
        "language": "en",
        "query": "How many days (SLA) does it take to issue a domicile certificate in Chhattisgarh?",
        "service": "Domicile Certificate"
    },
    {
        "id": 36,
        "sno": "4",
        "language": "hinglish",
        "query": "Niwas praman patra ke liye voter ID card stay ka proof ban sakta hai kya?",
        "service": "Domicile Certificate"
    },
    {
        "id": 37,
        "sno": "4",
        "language": "hi",
        "query": "निवास प्रमाण पत्र के लिए ऑनलाइन आवेदन शुल्क कितना है?",
        "service": "Domicile Certificate"
    },
    {
        "id": 38,
        "sno": "4",
        "language": "en",
        "query": "Can a student born in CG but studying college in Delhi apply for CG domicile certificate?",
        "service": "Domicile Certificate"
    },
    {
        "id": 39,
        "sno": "4",
        "language": "hinglish",
        "query": "Domicile certificate apply karne ka offline form pdf kahan se download karein?",
        "service": "Domicile Certificate"
    },
    {
        "id": 40,
        "sno": "4",
        "language": "hi",
        "query": "छत्तीसगढ़ के मूल निवासी प्रमाण पत्र के लिए सक्षम प्राधिकारी कौन है?",
        "service": "Domicile Certificate"
    },

    # === Service 5: Name Change Gazette Notification (SNO: 5, Service ID: 201) ===
    {
        "id": 41,
        "sno": "5",
        "language": "hinglish",
        "query": "Naam badalne ka gazette notification (Ordinary Gazette) ke liye kya step-by-step process hai?",
        "service": "Name Change"
    },
    {
        "id": 42,
        "sno": "5",
        "language": "en",
        "query": "What is the exact advertisement fee for publication of name change in Ordinary Gazette?",
        "service": "Name Change"
    },
    {
        "id": 43,
        "sno": "5",
        "language": "hi",
        "query": "नाम बदलने के लिए विज्ञापन प्रकाशन हेतु कितने गवाहों (witnesses) की आवश्यकता होती है?",
        "service": "Name Change"
    },
    {
        "id": 44,
        "sno": "5",
        "language": "hinglish",
        "query": "Gazette notification me name change ke liye stamp paper par affidavit kahan se notary karwayein?",
        "service": "Name Change"
    },
    {
        "id": 45,
        "sno": "5",
        "language": "en",
        "query": "What is the SLA timeline for the publication of name change in CG Ordinary Gazette?",
        "service": "Name Change"
    },
    {
        "id": 46,
        "sno": "5",
        "language": "hinglish",
        "query": "Gazette publication name change advertisement ke liye Form-I aur Form-II kahan se milega?",
        "service": "Name Change"
    },
    {
        "id": 47,
        "sno": "5",
        "language": "hi",
        "query": "क्या किसी नाबालिग बच्चे (minor child) का नाम बदलने के लिए उसके माता-पिता आवेदन कर सकते हैं?",
        "service": "Name Change"
    },
    {
        "id": 48,
        "sno": "5",
        "language": "en",
        "query": "How can I download a digital copy of the published gazette notification for my name change?",
        "service": "Name Change"
    },
    {
        "id": 49,
        "sno": "5",
        "language": "hinglish",
        "query": "Name change advertisement ke liye local newspaper me chhapwana compulsory hai kya?",
        "service": "Name Change"
    },
    {
        "id": 50,
        "sno": "5",
        "language": "hi",
        "query": "राजपत्र (gazette) में नाम परिवर्तन प्रकाशन के लिए कुल कितना सरकारी खर्च आता है?",
        "service": "Name Change"
    }
]

# Paths
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(TESTS_DIR, "random_50_test_results.md")

# Initialize markdown report
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write("# SewaSetu RAG Chatbot: 50 Random Real-Life Queries Test Results\n\n")
    f.write("This audit report captures testing the RAG chatbot with 50 diverse, random, real-life queries. ")
    f.write("The questions cover all 5 scoped services of the SewaSetu Chhattisgarh Portal with a realistic ")
    f.write("mix of English, Hindi, and Hinglish queries.\n\n")
    f.write("## Execution Summary Table\n\n")
    f.write("| ID | Service Category | User Query | Language | Mapped Service ID | Intent | Latency | Status |\n")
    f.write("|----|------------------|------------|----------|-------------------|--------|---------|--------|\n")

print(f"Starting test execution. Output report will be generated at: {REPORT_PATH}")

for tc in test_cases:
    tc_id = tc["id"]
    query = tc["query"]
    sno = tc["sno"]
    lang = tc["language"]
    service_cat = tc["service"]
    
    # Run each test case with a fresh context payload to avoid context leaking between random questions
    payload = {
        "messages": [{"role": "user", "content": query}],
        "selected_sno": sno,
        "language": "en", # default language configuration
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
            
            # Extract returned values
            res_text = data.get("response", data.get("text", "No text response"))
            q_lang = data.get("query_lang", "N/A")
            english_q = data.get("english_query", "N/A")
            hindi_q = data.get("hindi_query", "N/A")
            ans_en = data.get("english_answer", "N/A")
            ans_hi = data.get("hindi_answer", "N/A")
            service_id = data.get("service_id", "N/A")
            intent = data.get("intent", "new_topic")
            
            # Write row to summary table
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"| {tc_id} | {service_cat} | `{query}` | {lang.upper()} ({q_lang}) | {service_id} | {intent} | {latency:.2f}s | ✅ SUCCESS |\n")
            
            # Write detailed case section
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"\n### Query {tc_id} Details\n")
                f.write(f"* **Query**: `{query}`\n")
                f.write(f"* **Service Category**: {service_cat} (Target SNO: {sno})\n")
                f.write(f"* **Detected Language**: `{q_lang}`\n")
                f.write(f"* **Classified Service ID**: `{service_id}`\n")
                f.write(f"* **Classified Intent**: `{intent}`\n")
                f.write(f"* **Resolved English Translation**: `{english_q}`\n")
                f.write(f"* **Resolved Hindi Translation**: `{hindi_q}`\n")
                
                if ans_en and ans_en != "N/A":
                    f.write(f"* **Intermediate English Answer**:\n  ```markdown\n  {ans_en}\n  ```\n")
                if ans_hi and ans_hi != "N/A":
                    f.write(f"* **Intermediate Hindi Answer**:\n  ```markdown\n  {ans_hi}\n  ```\n")
                
                f.write(f"* **Final Synthesized Chatbot Response**:\n")
                f.write(f"  ```markdown\n  {res_text}\n  ```\n")
                f.write("\n---\n")
                
            print(f"[{tc_id}/50] Query: '{query[:40]}...' -> Status: SUCCESS ({latency:.2f}s)")
            
        else:
            latency = time.time() - start_time
            with open(REPORT_PATH, "a", encoding="utf-8") as f:
                f.write(f"| {tc_id} | {service_cat} | `{query}` | {lang.upper()} | N/A | N/A | {latency:.2f}s | ❌ ERROR ({response.status_code}) |\n")
            print(f"[{tc_id}/50] Query: '{query[:40]}...' -> Status: ERROR ({response.status_code}, {latency:.2f}s)")
            
    except Exception as e:
        latency = time.time() - start_time
        with open(REPORT_PATH, "a", encoding="utf-8") as f:
            f.write(f"| {tc_id} | {service_cat} | `{query}` | {lang.upper()} | N/A | N/A | {latency:.2f}s | ❌ EXCEPTION ({str(e)}) |\n")
        print(f"[{tc_id}/50] Query: '{query[:40]}...' -> Status: EXCEPTION ({str(e)}, {latency:.2f}s)")

print(f"\nExecution Complete! Report saved to: {REPORT_PATH}")
