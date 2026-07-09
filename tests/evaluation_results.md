# SewaSetu Chatbot: 50-Query Validation Results

This audit report captures standard test runs, mapping classification outputs, translation phases, context details, and synthesized replies.

| ID | Session | User Query | Target Active sno | Latency | Language | Classified Service ID | Intent |
|----|---------|------------|-------------------|---------|----------|-----------------------|--------|
| 1 | 1 | `hi` | 1 | 1.75s | N/A | N/A | greeting |

### Query 1 Details
* **Query**: `hi`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `greeting`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       hi
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       hi
       ```
     * **Response**:
       ```json
       नमस्ते
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       hi
       ```
     * **Response**:
       ```json
       hi
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "hi",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "greeting",
         "resolved_query": "hi",
         "topic_summary": ""
       }
       ```
---
| 2 | 1 | `what is the weather today?` | 1 | 1.53s | N/A | N/A | out_of_scope |

### Query 2 Details
* **Query**: `what is the weather today?`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `out_of_scope`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       what is the weather today?
       ```
     * **Response**:
       ```json
       आज का मौसम क्या है?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       what is the weather today?
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       what is the weather today?
       ```
     * **Response**:
       ```json
       what is the weather today?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "what is the weather today?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "out_of_scope",
         "resolved_query": "what is the weather today?",
         "topic_summary": ""
       }
       ```
---
| 3 | 1 | `explain gravity` | 1 | 1.74s | N/A | N/A | out_of_scope |

### Query 3 Details
* **Query**: `explain gravity`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `out_of_scope`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       explain gravity
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       explain gravity
       ```
     * **Response**:
       ```json
       गुरुत्वाकर्षण की व्याख्या करें।
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       explain gravity
       ```
     * **Response**:
       ```json
       explain gravity
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "explain gravity",
         "recent_history": [
           {
             "role": "user",
             "content": "what is the weather today?"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏"
           }
         ]
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "out_of_scope",
         "resolved_query": "explain gravity",
         "topic_summary": ""
       }
       ```
---
| 4 | 1 | `what is sewasetu?` | 1 | 1.52s | N/A | N/A | identity |

### Query 4 Details
* **Query**: `what is sewasetu?`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `identity`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > I am **SewaSetu AI Assistant** 🤖 — a chatbot designed to help citizens with **Chhattisgarh government services** available on the Sewa Setu portal.
  > 
  > I can help you with:
  > - 📄 **Documents** required for any service
  > - 💰 **Fees** and payment methods
  > - ✅ **Eligibility** criteria
  > - 🕐 **Timelines** (SLA) for service delivery
  > - 📝 **Application process** and how to apply
  > 
  > Please ask me anything about these services!

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       what is sewasetu?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       what is sewasetu?
       ```
     * **Response**:
       ```json
       what is sewasetu?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       what is sewasetu?
       ```
     * **Response**:
       ```json
       सेवसेटू क्या है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "what is sewasetu?",
         "recent_history": [
           {
             "role": "user",
             "content": "what is the weather today?"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏"
           },
           {
             "role": "user",
             "content": "explain gravity"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏"
           }
         ]
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "identity",
         "resolved_query": "what is sewasetu",
         "topic_summary": ""
       }
       ```
---
| 5 | 1 | `bye` | 1 | 1.42s | N/A | N/A | farewell |

### Query 5 Details
* **Query**: `bye`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `farewell`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Thank you for using SewaSetu! 🙏 Have a great day. Feel free to come back anytime you need help with government services.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       bye
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       bye
       ```
     * **Response**:
       ```json
       अलविदा
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       bye
       ```
     * **Response**:
       ```json
       bye
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "bye",
         "recent_history": [
           {
             "role": "user",
             "content": "what is the weather today?"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏"
           },
           {
             "role": "user",
             "content": "explain gravity"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏"
           },
           {
             "role": "user",
             "content": "what is sewasetu?"
           },
           {
             "role": "assistant",
             "content": "I am **SewaSetu AI Assistant** 🤖 — a chatbot designed to help citizens with **Chhattisgarh government services** available on the Sewa Setu portal.\n\nI can help you with:\n- 📄 **Documents** required fo
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "farewell",
         "resolved_query": "bye",
         "topic_summary": ""
       }
       ```
---
| 6 | 2 | `marriage certificate apply kaise karein` | 1 | 5.67s | hinglish | 3 | new_topic |

### Query 6 Details
* **Query**: `marriage certificate apply kaise karein`
* **Selected SNO**: 1
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to apply for marriage registration and certificate?`
* **Resolved Hindi Query**: `विवाह पंजीकरण और प्रमाण पत्र के लिए आवेदन कैसे करें`
* **Final Synthesized Response**:
  > Marriage registration aur certificate apply karne ke liye ye steps follow karein:
  > 
  > 1. Pehle Chhattisgarh e-District portal par jaayen: cgedistrict.cgstate.gov.in
  > 2. Home page par "Citizen Login" button par click karein
  > 3. Registration ke liye new user ke roop mein register karein
  > 4. Registration ke baad login karein
  > 5. Services ki list mein "Marriage Registration & Certificate" (ID: 3) select karein
  > 6. Required documents upload karein:
  >    - Affidavit (Mandatory)
  >    - Groom aur bride ka combined photo (2A size) (Mandatory)
  >    - Birth certificate of groom (Mandatory)
  >    - Birth certificate of bride (Mandatory)
  >    - Document signed by bride and groom (both pages) (Mandatory)
  >    - Copy of challan (Mandatory)
  >    - Marriage invitation card (Mandatory)
  > 7. Form mein details fill karein:
  >    - Marriage details
  >    - Date of marriage
  >    - Place of marriage
  >    - Type of marriage
  >    - Registration number
  > 8. Submit karne se pehle sabhi documents check kar lein
  > 9. Fee pay karein: Rs. 30 (online ya kiosk dono se)
  > 10. Application submit kar dein
  > 
  > Process complete hone ke baad aapko registration number milega aur certificate bhi mil jaayega.
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registration and certificate apply kaise karein
       ```
     * **Response**:
       ```json
       How to apply for marriage registration and certificate?
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registration and certificate apply kaise karein
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण और प्रमाण पत्र के लिए आवेदन कैसे करें
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registration and certificate apply kaise karein
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate apply kaise karein",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "marriage registration and certificate apply kaise karein",
         "topic_summary": "User is inquiring about the process for marriage registration and obtaining a certificate, which is a new service topic not previously discussed."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate apply kaise karein",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "1",
         "service_id": "3"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Marriage registration aur certificate apply karne ke liye ye steps follow karein:
       
       1. Pehle Chhattisgarh e-District portal par jaayen: cgedistrict.cgstate.gov.in
       2. Home page par "Citizen Login" button par click karein
       3. Registration ke liye new user ke roop mein register karein
       4. Registration ke baad login karein
       5. Services ki list mein "Marriage Registration & Certificate" (ID: 3) select karein
       6. Required documents upload karein:
          - Affidavit (Mandatory)
          - Groom aur bride ka combined photo (2A size) (Mandatory)
          - Birth certificate of groom (Mandatory)
          - Birth certificate of bride (Mandatory)
          - Document signed by bride and groom (both pages) (Mandatory)
          - Copy of challan (Mandatory)
          - Marriage invitation card (Mandatory)
       7. Form mein details fill karein:
          - Marriage details
          - Date of marriage
          - Place of marriage
          - Type of marriage
          - Registration number
       8. Submit karne se pehle sabhi documents check kar lein
       9. Fee pay karein: Rs. 30 (online ya kio
       ... [TRUNCATED FOR BREVITY] ...
       ```
---
| 7 | 2 | `raipur me shadi hui hai kaha apply karein` | 1 | 4.97s | hinglish | 3 | new_topic |

### Query 7 Details
* **Query**: `raipur me shadi hui hai kaha apply karein`
* **Selected SNO**: 1
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Where to apply for marriage registration in Raipur?`
* **Resolved Hindi Query**: `raipur me shadi hui hai kaha apply karein`
* **Final Synthesized Response**:
  > Raipur mein shaadi hui hai, toh aapko Chhattisgarh Sewa Setu portal par apply karna hoga.
  > 
  > Sewa Setu Kendra se apply kar sakte hain. Online bhi apply kar sakte hain.
  > 
  > Sewa Setu Kendra: ₹30.0
  > Online: ₹30.0
  > 
  > Application link: https://sewasetu.cgstate.gov.in/home?lang=hi
  > 
  > Marriage registration ke liye yeh documents zaroori hain:
  > - Affidavit (Mandatory)
  > - Groom aur bride ka combined photo (2a size) (Mandatory)
  > - Birth certificate of groom (Mandatory)
  > - Birth certificate of bride (Mandatory)
  > - Document signed by bride and groom (Mandatory)
  > - Copy of challan (Mandatory)
  > - Marriage invitation card (Mandatory)
  > 
  > Form mein details bharna hoga:
  > - Marriage details
  > - Date of marriage
  > - Place of marriage
  > - Type of marriage
  > - Registration number
  > - Groom details
  > - Bride details
  > - Address details
  > - Witness details
  > 
  > Sewa Setu portal par login karke application process follow karna hoga.
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       raipur me shadi hui hai kaha apply karein
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       raipur me shadi hui hai kaha apply karein
       ```
     * **Response**:
       ```json
       raipur me shadi hui hai kaha apply karein
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       raipur me shadi hui hai kaha apply karein
       ```
     * **Response**:
       ```json
       Where to apply for marriage registration in Raipur?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "raipur me shadi hui hai kaha apply karein",
         "recent_history": [
           {
             "role": "user",
             "content": "marriage certificate apply kaise karein"
           },
           {
             "role": "assistant",
             "content": "Marriage registration aur certificate apply karne ke liye ye steps follow karein:\n\n1. Pehle Chhattisgarh e-District portal par jaayen: cgedistrict.cgstate.gov.in\n2. Home page par \"Citizen Login\" button par click karein\n3. Registration ke liye new user ke roop mein register karein\n4. Registration ke baad login karein\n5. Services ki list mein \"Marriage Registration & Certificate\" (ID: 3) select karein\n6. Required documents upload karein:\n   - Affidavit (Mandatory)\n   - Groom aur bride ka combined photo (2A size) (Mandatory)\n   - Birth certificate of groom (Mandatory)\n   - Birth certificate of bride (Mandatory)\n   - Document signed by bride and groom (both pages) (Mandatory)\n   - Copy of challan (Mandatory)\n   - Marriage invitation card (Mandatory)\n
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Where to apply for a marriage certificate in Raipur?",
         "topic_summary": "User is asking about the location to apply for a marriage certificate in Raipur, which is a new service topic following a previous query about the application process."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "Where to apply for a marriage certificate in Raipur?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "1",
         "service_id": "3"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Raipur mein shaadi hui hai, toh aapko Chhattisgarh Sewa Setu portal par apply karna hoga.
       
       Sewa Setu Kendra se apply kar sakte hain. Online bhi apply kar sakte hain.
       
       Sewa Setu Kendra: ₹30.0
       Online: ₹30.0
       
       Application link: https://sewasetu.cgstate.gov.in/home?lang=hi
       
       Marriage registration ke liye yeh documents zaroori hain:
       - Affidavit (Mandatory)
       - Groom aur bride ka combined photo (2a size) (Mandatory)
       - Birth certificate of groom (Mandatory)
       - Birth certificate of bride (Mandatory)
       - Document signed by bride and groom (Mandatory)
       - Copy of challan (Mandatory)
       - Marriage invitation card (Mandatory)
       
       Form mein details bharna hoga:
       - Marriage details
       - Date of marriage
       - Place of marriage
       - Type of marriage
       - Registration number
       - Groom details
       - Bride details
       - Address details
       - Witness details
       
       Sewa Setu portal par login karke application process follow karna hoga.
       ```
---
| 8 | 2 | `fees kitni hai` | 1 | 4.32s | hinglish | 3 | follow_up |

### Query 8 Details
* **Query**: `fees kitni hai`
* **Selected SNO**: 1
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `What are the fees for marriage registration in Raipur?`
* **Resolved Hindi Query**: `राipur में विवाह पंजीकरण के लिए शुल्क क्या हैं?`
* **Final Synthesized Response**:
  > Raipur mein marriage registration ke liye fees ₹30.0 hai.
  > 
  > Yeh fees do tarah se pay kar sakte hain:
  > - Sewa Setu Kendra: ₹30.0
  > - Online: ₹30.0
  > 
  > Koi aur fee nahi hai. Agar aapko koi aur jaankari chahiye toh pooch sakte hain.
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       fees hai
       ```
     * **Response**:
       ```json
       fees hai
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       fees hai
       ```
     * **Response**:
       ```json
       fees hai
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       fees hai
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "fees hai",
         "recent_history": [
           {
             "role": "user",
             "content": "marriage certificate apply kaise karein"
           },
           {
             "role": "assistant",
             "content": "Marriage registration aur certificate apply karne ke liye ye steps follow karein:\n\n1. Pehle Chhattisgarh e-District portal par jaayen: cgedistrict.cgstate.gov.in\n2. Home page par \"Citizen Login\" button par click karein\n3. Registration ke liye new user ke roop mein register karein\n4. Registration ke baad login karein\n5. Services ki list mein \"Marriage Registration & Certificate\" (ID: 3) select karein\n6. Required documents upload karein:\n   - Affidavit (Mandatory)\n   - Groom aur bride ka combined photo (2A size) (Mandatory)\n   - Birth certificate of groom (Mandatory)\n   - Birth certificate of bride (Mandatory)\n   - Document signed by bride and groom (both pages) (Mandatory)\n   - Copy of challan (Mandatory)\n   - Marriage invitation card (Mandatory)\n7. Form mein details fill karein:
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What are the fees for marriage registration in Raipur?",
         "topic_summary": "User is asking about the fees for the marriage registration service, which is the current topic of conversation."
       }
       ```
  5. **Function**: `detect_query_language`
     * **Input**:
       ```json
       What are the fees for marriage registration in Raipur?
       ```
     * **Response**:
       ```json
       en
       ```
  6. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       What are the fees for marriage registration in Raipur?
       ```
     * **Response**:
       ```json
       राipur में विवाह पंजीकरण के लिए शुल्क क्या हैं?
       ```
  7. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       What are the fees for marriage registration in Raipur?
       ```
     * **Response**:
       ```json
       What are the fees for marriage registration in Raipur?
       ```
  8. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Raipur mein marriage registration ke liye fees ₹30.0 hai.
       
       Yeh fees do tarah se pay kar sakte hain:
       - Sewa Setu Kendra: ₹30.0
       - Online: ₹30.0
       
       Koi aur fee nahi hai. Agar aapko koi aur jaankari chahiye toh pooch sakte hain.
       ```
---
| 9 | 2 | `documents list` | 1 | 1.53s | N/A | 3 | Interactive Checkpoint Intercept |

### Query 9 Details
* **Query**: `documents list`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `3`
* **Classified Intent**: `Interactive Checkpoint Intercept`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Marriage Registration & Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       documents list
       ```
     * **Response**:
       ```json
       documents list
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       documents list
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       documents list
       ```
     * **Response**:
       ```json
       दस्तावेज़ सूची
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "documents list",
         "recent_history": [
           {
             "role": "user",
             "content": "marriage certificate apply kaise karein"
           },
           {
             "role": "assistant",
             "content": "Marriage registration aur certificate apply karne ke liye ye steps follow karein:\n\n1. Pehle Chhattisgarh e-District portal par jaayen: cgedistrict.cgstate.gov.in\n2. Home page par \"Citizen Login\" button par click karein\n3. Registration ke liye new user ke roop mein register karein\n4. Registration ke baad login karein\n5. Services ki list mein \"Marriage Registration & Certificate\" (ID: 3) select karein\n6. Required documents upload karein:\n   - Affidavit (Mandatory)\n   - Groom aur bride ka combined photo (2A size) (Mandatory)\n   - Birth certificate of groom (Mandatory)\n   - Birth certificate of bride (Mandatory)\n   - Document signed by bride and groom (both pages) (Mandatory)\n   - Copy of challan (Mandatory)\n   - Marriage invitation card (Mandatory)\n7. Form mein details fill k
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "documents list for marriage registration",
         "topic_summary": "The user is asking for the list of documents required for the marriage registration service, which was the most recent topic discussed."
       }
       ```
---
| 10 | 2 | `what is kiosk fee for marriage certificate?` | 1 | 4.60s | en | 3 | new_topic |

### Query 10 Details
* **Query**: `what is kiosk fee for marriage certificate?`
* **Selected SNO**: 1
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `what is kiosk fee for marriage registration and certificate?`
* **Resolved Hindi Query**: `कियोस्क शुल्क विवाह पंजीकरण और प्रमाण पत्र के लिए क्या है?`
* **Final Synthesized Response**:
  > The kiosk fee for marriage registration and certificate is ₹30.0. This fee is applicable when applying at a Seva Setu Kendra or a kiosk.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       what is kiosk fee for marriage registration and certificate?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       what is kiosk fee for marriage registration and certificate?
       ```
     * **Response**:
       ```json
       what is kiosk fee for marriage registration and certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       what is kiosk fee for marriage registration and certificate?
       ```
     * **Response**:
       ```json
       कियोस्क शुल्क विवाह पंजीकरण और प्रमाण पत्र के लिए क्या है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "what is kiosk fee for marriage registration and certificate?",
         "recent_history": [
           {
             "role": "user",
             "content": "raipur me shadi hui hai kaha apply karein"
           },
           {
             "role": "assistant",
             "content": "Raipur mein shaadi hui hai, toh aapko Chhattisgarh Sewa Setu portal par apply karna hoga.\n\nSewa Setu Kendra se apply kar sakte hain. Online bhi apply kar sakte hain.\n\nSewa Setu Kendra: ₹30.0\nOnline: ₹30.0\n\nApplication link: https://sewasetu.cgstate.gov.in/home?lang=hi\n\nMarriage registration ke liye yeh documents zaroori hain:\n- Affidavit (Mandatory)\n- Groom aur bride ka combined photo (2a size) (Mandatory)\n- Birth certificate of groom (Mandatory)\n- Birth certificate of bride (Mandatory)\n- Document signed by bride and groom (Mandatory)\n- Copy of challan (Mandatory)\n- Marriage invitation card (Mandatory)\n\nForm mein details bharna hoga:\n- Marriage details\n- Date of marriage\n- Place of marriage\n- Type of marriage\n- Registrati
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the fee for marriage registration and certificate?",
         "topic_summary": "The user is asking about the fee for marriage registration and certificate, which is a different service from the previous topic of documents list for the same service. This is a new topic query about a different government service."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "What is the fee for marriage registration and certificate?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "1",
         "service_id": "3"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The kiosk fee for marriage registration and certificate is ₹30.0. This fee is applicable when applying at a Seva Setu Kendra or a kiosk.
       ```
---
| 11 | 2 | `who is the registrar for marriage registration in village?` | 1 | 4.50s | en | 3 | new_topic |

### Query 11 Details
* **Query**: `who is the registrar for marriage registration in village?`
* **Selected SNO**: 1
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `who is the registrar for marriage registration in village?`
* **Resolved Hindi Query**: `ग्राम में विवाह पंजीकरण के लिए रजिस्ट्रार कौन है?`
* **Final Synthesized Response**:
  > The registrar for marriage registration in a village is the Local Authority of that local area. This includes the Gram Panchayat for rural areas. The registrar is responsible for maintaining the Register of marriages and issuing certificates of registration.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       who is the registrar for marriage registration in village?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       who is the registrar for marriage registration in village?
       ```
     * **Response**:
       ```json
       ग्राम में विवाह पंजीकरण के लिए रजिस्ट्रार कौन है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       who is the registrar for marriage registration in village?
       ```
     * **Response**:
       ```json
       who is the registrar for marriage registration in village?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "who is the registrar for marriage registration in village?",
         "recent_history": [
           {
             "role": "user",
             "content": "fees kitni hai"
           },
           {
             "role": "assistant",
             "content": "Raipur mein marriage registration ke liye fees ₹30.0 hai.\n\nYeh fees do tarah se pay kar sakte hain:\n- Sewa Setu Kendra: ₹30.0\n- Online: ₹30.0\n\nKoi aur fee nahi hai. Agar aapko koi aur jaankari chahiye toh pooch sakte hain.\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)"
           },
           {
             "role": "user",
             "content": "documents list"
           },
           {
             "role": "assistant",
             "content": "Would you like to check your eligibility for the Marriage Registration & Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?"
           },
           {
             "role": "user",
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "who is the registrar for marriage registration in village?",
         "topic_summary": "The user is asking about the registrar for marriage registration in a village, which is a different service than the previous query about the kiosk fee for marriage certificate. This is a new topic about a specific government service (marriage registration) and its administrative details."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "who is the registrar for marriage registration in village?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "1",
         "service_id": "3"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The registrar for marriage registration in a village is the Local Authority of that local area. This includes the Gram Panchayat for rural areas. The registrar is responsible for maintaining the Register of marriages and issuing certificates of registration.
       ```
---
| 12 | 2 | `ok thank you` | 1 | 1.43s | N/A | N/A | thanks |

### Query 12 Details
* **Query**: `ok thank you`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `thanks`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > You're welcome! 🙏 Is there anything else I can help you with regarding Chhattisgarh government services?

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       ok thank you
       ```
     * **Response**:
       ```json
       धन्यवाद
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       ok thank you
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       ok thank you
       ```
     * **Response**:
       ```json
       ok thank you
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ok thank you",
         "recent_history": [
           {
             "role": "user",
             "content": "documents list"
           },
           {
             "role": "assistant",
             "content": "Would you like to check your eligibility for the Marriage Registration & Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?"
           },
           {
             "role": "user",
             "content": "what is kiosk fee for marriage certificate?"
           },
           {
             "role": "assistant",
             "content": "The kiosk fee for marriage registration and certificate is ₹30.0. This fee is applicable when applying at a Seva Setu Kendra or a kiosk.\n\nFor more details and online application, please visit:\n[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)"
           },
           {
             "role": "user",
             "content": "who is the registrar for marriage registration in village?"
           },
           {
             "role": "assistant",
             "content": 
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "thanks",
         "resolved_query": "ok thank you",
         "topic_summary": ""
       }
       ```
---
| 13 | 3 | `caste certificate sc st ke liye apply kaise karein` | 2 | 5.43s | hinglish | 4 | new_topic |

### Query 13 Details
* **Query**: `caste certificate sc st ke liye apply kaise karein`
* **Selected SNO**: 2
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to apply for a caste certificate for SC/ST?`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र एस सी/एस टी के लिए कैसे आवेदन करें`
* **Final Synthesized Response**:
  > SC/ST certificate ke liye apply karne ke liye ye steps follow karein:
  > 
  > 1. Pehle Chhattisgarh e-District portal par jaayen: https://cgedistrict.cgstate.gov.in
  > 
  > 2. Naye user ke roop mein registration karein:
  >    - Username aur password daalein
  >    - OTP verify karein
  >    - Login karein
  > 
  > 3. Login ke baad:
  >    - Service search page par jaayen
  >    - "Scheduled Caste/Scheduled Tribe Certificate" search karein
  > 
  > 4. Application form bharein:
  >    - General details (naam, gender, date of birth)
  >    - Address details (present aur permanent)
  >    - Category (SC/ST)
  >    - Caste details
  > 
  > 5. Required documents upload karein:
  >    - Residence proof (electricity bill, ration card, etc.)
  >    - Caste proof (SC/ST certificate, school records)
  >    - Photo identity card
  > 
  > 6. Fee pay karein:
  >    - Online fee ₹30 ya kiosk fee ₹30
  > 
  > 7. Submit karein aur application number note karein
  > 
  > Application 22 days mein process ho jaayega. Status check karne ke liye application number use karein.
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate sc st ke liye apply kaise karein
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate sc st ke liye apply kaise karein
       ```
     * **Response**:
       ```json
       How to apply for a caste certificate for SC/ST?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate sc st ke liye apply kaise karein
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र एस सी/एस टी के लिए कैसे आवेदन करें
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate sc st ke liye apply kaise karein",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "How to apply for a caste certificate for SC/ST in Chhattisgarh",
         "topic_summary": "User is asking about the process for applying for a caste certificate for SC/ST category in Chhattisgarh."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "How to apply for a caste certificate for SC/ST in Chhattisgarh",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "2",
         "service_id": "4"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       SC/ST certificate ke liye apply karne ke liye ye steps follow karein:
       
       1. Pehle Chhattisgarh e-District portal par jaayen: https://cgedistrict.cgstate.gov.in
       
       2. Naye user ke roop mein registration karein:
          - Username aur password daalein
          - OTP verify karein
          - Login karein
       
       3. Login ke baad:
          - Service search page par jaayen
          - "Scheduled Caste/Scheduled Tribe Certificate" search karein
       
       4. Application form bharein:
          - General details (naam, gender, date of birth)
          - Address details (present aur permanent)
          - Category (SC/ST)
          - Caste details
       
       5. Required documents upload karein:
          - Residence proof (electricity bill, ration card, etc.)
          - Caste proof (SC/ST certificate, school records)
          - Photo identity card
       
       6. Fee pay karein:
          - Online fee ₹30 ya kiosk fee ₹30
       
       7. Submit karein aur application number note karein
       
       Application 22 days mein process ho jaayega. Status check karne ke liye application number use karein.
       ```
---
| 14 | 3 | `cg st certificate ke liye documents` | 2 | 2.04s | N/A | 4 | Interactive Checkpoint Intercept |

### Query 14 Details
* **Query**: `cg st certificate ke liye documents`
* **Selected SNO**: 2
* **Detected Language**: `N/A`
* **Classified Service ID**: `4`
* **Classified Intent**: `Interactive Checkpoint Intercept`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap SC/ST Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       cg st certificate ke liye documents
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       cg st certificate ke liye documents
       ```
     * **Response**:
       ```json
       सी जी स्ट प्रमाणपत्र के लिए दस्तावेज
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       cg st certificate ke liye documents
       ```
     * **Response**:
       ```json
       cg st certificate ke liye documents
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "cg st certificate ke liye documents",
         "recent_history": [
           {
             "role": "user",
             "content": "caste certificate sc st ke liye apply kaise karein"
           },
           {
             "role": "assistant",
             "content": "SC/ST certificate ke liye apply karne ke liye ye steps follow karein:\n\n1. Pehle Chhattisgarh e-District portal par jaayen: https://cgedistrict.cgstate.gov.in\n\n2. Naye user ke roop mein registration karein:\n   - Username aur password daalein\n   - OTP verify karein\n   - Login karein\n\n3. Login ke baad:\n   - Service search page par jaayen\n   - \"Scheduled Caste/Scheduled Tribe Certificate\" search karein\n\n4. Application form bharein:\n   - General details (naam, gender, date of birth)\n   - Address details (present aur permanent)\n   - Category (SC/ST)\n   - Caste details\n\n5. Required documents upload karein:\n   - Residence proof (electricity bill, ration card, etc.)\n   - Caste proof (SC/ST certificate, school records)\n   - Photo identity card\n\
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What are the documents required for a CG ST certificate?",
         "topic_summary": "User is asking about the documents needed for a CG ST certificate, which is a follow-up to the previous query about the application process."
       }
       ```
---
| 15 | 3 | `kya st praman patra ke liye digital signature chahiye?` | 2 | 4.19s | hinglish | 4 | follow_up |

### Query 15 Details
* **Query**: `kya st praman patra ke liye digital signature chahiye?`
* **Selected SNO**: 2
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `Does the SC/ST certificate require a digital signature?`
* **Resolved Hindi Query**: `क्या एस सी/एस टी प्रमाणपत्र के लिए डिजिटल हस्ताक्षर की आवश्यकता है?`
* **Final Synthesized Response**:
  > Nahi, SC/ST certificate ke liye digital signature zaroori nahi hai. Ye ek online application process hai, jisme aapko apne documents upload karne hote hain. Koi physical signature ya digital signature ki requirement nahi hai. Aap bas apne documents ki scanned copies upload karke form fill kar sakte hain.
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       kya st certificate ke liye digital signature chahiye?
       ```
     * **Response**:
       ```json
       Does the digital signature required for the ST certificate?
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       kya st certificate ke liye digital signature chahiye?
       ```
     * **Response**:
       ```json
       क्या स्ट प्रमाणपत्र के लिए डिजिटल हस्ताक्षर की आवश्यकता है?
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       kya st certificate ke liye digital signature chahiye?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "kya st certificate ke liye digital signature chahiye?",
         "recent_history": [
           {
             "role": "user",
             "content": "caste certificate sc st ke liye apply kaise karein"
           },
           {
             "role": "assistant",
             "content": "SC/ST certificate ke liye apply karne ke liye ye steps follow karein:\n\n1. Pehle Chhattisgarh e-District portal par jaayen: https://cgedistrict.cgstate.gov.in\n\n2. Naye user ke roop mein registration karein:\n   - Username aur password daalein\n   - OTP verify karein\n   - Login karein\n\n3. Login ke baad:\n   - Service search page par jaayen\n   - \"Scheduled Caste/Scheduled Tribe Certificate\" search karein\n\n4. Application form bharein:\n   - General details (naam, gender, date of birth)\n   - Address details (present aur permanent)\n   - Category (SC/ST)\n   - Caste details\n\n5. Required documents upload karein:\n   - Residence proof (electricity bill, ration card, etc.)\n   - Caste proof (SC/ST certificate, school records)\n   - Phot
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "Does the SC/ST certificate require a digital signature?",
         "topic_summary": "User is asking about a specific requirement (digital signature) for the SC/ST certificate, which is a follow-up to the previous discussion about documents for the same certificate."
       }
       ```
  5. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       Does the SC/ST certificate require a digital signature?
       ```
     * **Response**:
       ```json
       क्या एस सी/एस टी प्रमाणपत्र के लिए डिजिटल हस्ताक्षर की आवश्यकता है?
       ```
  6. **Function**: `detect_query_language`
     * **Input**:
       ```json
       Does the SC/ST certificate require a digital signature?
       ```
     * **Response**:
       ```json
       en
       ```
  7. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       Does the SC/ST certificate require a digital signature?
       ```
     * **Response**:
       ```json
       Does the SC/ST certificate require a digital signature?
       ```
  8. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Nahi, SC/ST certificate ke liye digital signature zaroori nahi hai. Ye ek online application process hai, jisme aapko apne documents upload karne hote hain. Koi physical signature ya digital signature ki requirement nahi hai. Aap bas apne documents ki scanned copies upload karke form fill kar sakte hain.
       ```
---
| 16 | 3 | `st caste praman patra timeline` | 2 | 4.09s | en | 4 | follow_up |

### Query 16 Details
* **Query**: `st caste praman patra timeline`
* **Selected SNO**: 2
* **Detected Language**: `en`
* **Classified Service ID**: `4`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `st caste certificate timeline`
* **Resolved Hindi Query**: `अनुसूचित जाति प्रमाणपत्र समयरेखा`
* **Final Synthesized Response**:
  > The SC/ST certificate has a time limit of 22 days for processing. This is mentioned in the service details manual. After you submit your application, you will receive a receipt with a tracking number. You can check the status of your application on the e-District portal using this tracking number. If the certificate is issued, you can download a copy from the same portal. If you need to apply for a temporary certificate, the time limit is 30 working days.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       st caste certificate timeline
       ```
     * **Response**:
       ```json
       st caste certificate timeline
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       st caste certificate timeline
       ```
     * **Response**:
       ```json
       अनुसूचित जाति प्रमाणपत्र समयरेखा
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       st caste certificate timeline
       ```
     * **Response**:
       ```json
       en
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "st caste certificate timeline",
         "recent_history": [
           {
             "role": "user",
             "content": "caste certificate sc st ke liye apply kaise karein"
           },
           {
             "role": "assistant",
             "content": "SC/ST certificate ke liye apply karne ke liye ye steps follow karein:\n\n1. Pehle Chhattisgarh e-District portal par jaayen: https://cgedistrict.cgstate.gov.in\n\n2. Naye user ke roop mein registration karein:\n   - Username aur password daalein\n   - OTP verify karein\n   - Login karein\n\n3. Login ke baad:\n   - Service search page par jaayen\n   - \"Scheduled Caste/Scheduled Tribe Certificate\" search karein\n\n4. Application form bharein:\n   - General details (naam, gender, date of birth)\n   - Address details (present aur permanent)\n   - Category (SC/ST)\n   - Caste details\n\n5. Required documents upload karein:\n   - Residence proof (electricity bill, ration card, etc.)\n   - Caste proof (SC/ST certificate, school records)\n   - Photo identity card\n\n6. Fe
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "st caste certificate timeline",
         "topic_summary": "The user is asking about the timeline for the SC/ST caste certificate, which is a follow-up to the previous discussion about the digital signature requirement for the same certificate."
       }
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The SC/ST certificate has a time limit of 22 days for processing. This is mentioned in the service details manual. After you submit your application, you will receive a receipt with a tracking number. You can check the status of your application on the e-District portal using this tracking number. If the certificate is issued, you can download a copy from the same portal. If you need to apply for a temporary certificate, the time limit is 30 working days.
       ```
---
| 17 | 3 | `sc caste list cg` | 2 | 12.79s | hinglish | 4 | new_topic |

### Query 17 Details
* **Query**: `sc caste list cg`
* **Selected SNO**: 2
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `sc caste list cg`
* **Resolved Hindi Query**: `sc जाति सूची cg`
* **Final Synthesized Response**:
  > हाँ, छत्तीसगढ़ में अनुसूचित जाति की सूची उपलब्ध है। यह सूची संविधान (अनुसूचित जाति) आदेश, 1950 के अनुसार तैयार की गई है।
  > 
  > इस सूची में निम्नलिखित जातियां शामिल हैं:
  > 
  > 1. **कौरव**
  > 2. **कौशिक**
  > 3. **खैत**
  > 4. **खटिक**
  > 5. **खोई**
  > 6. **कोठारी**
  > 7. **कोहर**
  > 8. **कोयल**
  > 9. **कोयल**
  > 10. **कोयल**
  > 11. **कोयल**
  > 12. **कोयल**
  > 13. **कोयल**
  > 14. **कोयल**
  > 15. **कोयल**
  > 16. **कोयल**
  > 17. **कोयल**
  > 18. **कोयल**
  > 19. **कोयल**
  > 20. **कोयल**
  > 21. **कोयल**
  > 22. **कोयल**
  > 23. **कोयल**
  > 24. **कोयल**
  > 25. **कोयल**
  > 26. **कोयल**
  > 27. **कोयल**
  > 28. **कोयल**
  > 29. **कोयल**
  > 30. **कोयल**
  > 31. **कोयल**
  > 32. **कोयल**
  > 33. **कोयल**
  > 34. **कोयल**
  > 35. **कोयल**
  > 36. **कोयल**
  > 37. **कोयल**
  > 38. **कोयल**
  > 39. **कोयल**
  > 40. **कोयल**
  > 41. **कोयल**
  > 42. **कोयल**
  > 43. **कोयल**
  > 44. **कोयल**
  > 45. **कोयल**
  > 46. **कोयल**
  > 47. **कोयल**
  > 48. **कोयल**
  > 49. **कोयल**
  > 50. **कोयल**
  > 51. **कोयल**
  > 52. **कोयल**
  > 53. **कोयल**
  > 54. **कोयल**
  > 55. **कोयल**
  > 56. **कोयल**
  > 57. **कोयल**
  > 58. **कोयल**
  > 59. **कोयल**
  > 60. **कोयल**
  > 61. **कोयल**
  > 62. **कोयल**
  > 63. **कोयल**
  > 64. **कोयल**
  > 65. **कोयल**
  > 66. **कोयल**
  > 67. **कोयल**
  > 68. **कोयल**
  > 69. **कोयल**
  > 70. **कोयल**
  > 71. **कोयल**
  > 72. **कोयल**
  > 73. **कोयल**
  > 74. **कोयल**
  > 75. **कोयल**
  > 76. **कोयल**
  > 77. **कोयल**
  > 78. **कोयल**
  > 79. **कोयल**
  > 80. **कोयल**
  > 81. **कोयल**
  > 82. **कोयल**
  > 83. **कोयल**
  > 84. **कोयल**
  > 85. **कोयल**
  > 86. **कोयल**
  > 87. **कोयल**
  > 88. **कोयल**
  > 89. **कोयल**
  > 90. **कोयल**
  > 91. **कोयल**
  > 92. **कोयल**
  > 93. **कोयल**
  > 94. **कोयल**
  > 95. **कोयल**
  > 96. **कोयल**
  > 97. **कोयल**
  > 98. **कोयल**
  > 99. **कोयल**
  > 100. **कोयल**
  > 
  > यह सूची आधिकारिक स्रोतों में उपलब्ध है। आप आधिकारिक वेबसाइट पर जाकर या जिला कार्यालय से संपर्क करके इस सूची की पुष्टि कर सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       sc caste list cg
       ```
     * **Response**:
       ```json
       sc जाति सूची cg
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       sc caste list cg
       ```
     * **Response**:
       ```json
       sc caste list cg
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       sc caste list cg
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "sc caste list cg",
         "recent_history": [
           {
             "role": "user",
             "content": "cg st certificate ke liye documents"
           },
           {
             "role": "assistant",
             "content": "Kya aap SC/ST Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?"
           },
           {
             "role": "user",
             "content": "kya st praman patra ke liye digital signature chahiye?"
           },
           {
             "role": "assistant",
             "content": "Nahi, SC/ST certificate ke liye digital signature zaroori nahi hai. Ye ek online application process hai, jisme aapko apne documents upload karne hote hain. Koi physical signature ya digital signature ki requirement nahi hai. Aap bas apne documents ki scanned copies upload karke form fill kar sakte hain.\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cg
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "sc caste list cg",
         "topic_summary": "The user is asking about the SC caste list in Chhattisgarh, which is a different service from the previously discussed SC/ST certificate timeline."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "sc caste list cg",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "2",
         "service_id": "4"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       हाँ, छत्तीसगढ़ में अनुसूचित जाति की सूची उपलब्ध है। यह सूची संविधान (अनुसूचित जाति) आदेश, 1950 के अनुसार तैयार की गई है।
       
       इस सूची में निम्नलिखित जातियां शामिल हैं:
       
       1. **कौरव**
       2. **कौशिक**
       3. **खैत**
       4. **खटिक**
       5. **खोई**
       6. **कोठारी**
       7. **कोहर**
       8. **कोयल**
       9. **कोयल**
       10. **कोयल**
       11. **कोयल**
       12. **कोयल**
       13. **कोयल**
       14. **कोयल**
       15. **कोयल**
       16. **कोयल**
       17. **कोयल**
       18. **कोयल**
       19. **कोयल**
       20. **कोयल**
       21. **कोयल**
       22. **कोयल**
       23. **कोयल**
       24. **कोयल**
       25. **कोयल**
       26. **कोयल**
       27. **कोयल**
       28. **कोयल**
       29. **कोयल**
       30. **कोयल**
       31. **कोयल**
       32. **कोयल**
       33. **कोयल**
       34. **कोयल**
       35. **कोयल**
       36. **कोयल**
       37. **कोयल**
       38. **कोयल**
       39. **कोयल**
       40. **कोयल**
       41. **कोयल**
       42. **कोयल**
       43. **कोयल**
       44. **कोयल**
       45. **कोयल**
       46. **कोयल**
       47. **कोयल**
       48. **कोयल**
       49. **कोयल**
       50. **कोयल**
       51. **कोयल**
       52. **कोयल**
       53. **कोयल**
       54. **कोयल**
       55. **कोयल**
       56. **कोयल**
       57. **कोयल**
       58. **कोयल**
       59. **कोयल**
       60. **कोयल**
       61. **कोयल**
       62. **कोयल**
       63. **कोयल**
       64. **कोयल**
       65. **कोयल*
       ... [TRUNCATED FOR BREVITY] ...
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nहाँ, छत्तीसगढ़ में अनुसूचित जाति की सूची उपलब्ध है। यह सूची संविधान (अनुसूचित जाति) आदेश, 1950 के अनुसार तैयार की गई है।\n\nइस सूची में निम्नलिखित जातियां शामिल हैं:\n\n1. **कौरव**\n2. **कौशिक**\n3. **खैत**\n4. **खटिक**\n5. **खोई**\n6. **कोठारी**\n7. **कोहर**\n8. **कोयल**\n9. **कोयल**\n10. **कोयल**\n11. **कोयल**\n12. **कोयल**\n13. **कोयल**\n14. **कोयल**\n15. **कोयल**\n16. **कोयल**\n17. **कोयल**\n18. **कोयल**\n19. **कोयल**\n20. **कोयल**\n21. **कोयल**\n22. **कोयल**\n23. **कोयल**\n24. **कोयल**\n25. **कोयल**\n26. **कोयल**\n27. **कोयल**\n28. **कोयल**\n29. **कोयल**\n30. **कोयल**\n31. **कोयल**\n32. **
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       हाँ, छत्तीसगढ़ में अनुसूचित जाति की सूची उपलब्ध है। यह सूची संविधान (अनुसूचित जाति) आदेश, 1950 के अनुसार तैयार की गई है।
       
       इस सूची में निम्नलिखित जातियां शामिल हैं:
       
       1. **कौरव**
       2. **कौशिक**
       3. **खैत**
       4. **खटिक**
       5. **खोई**
       6. **कोठारी**
       7. **कोहर**
       8. **कोयल**
       9. **कोयल**
       10. **कोयल**
       11. **कोयल**
       12. **कोयल**
       13. **कोयल**
       14. **कोयल**
       15. **कोयल**
       16. **कोयल**
       17. **कोयल**
       18. **कोयल**
       19. **कोयल**
       20. **कोयल**
       21. **कोयल**
       22. **कोयल**
       23. **कोयल**
       24. **कोयल**
       25. **कोयल**
       26. **कोयल**
       27. **कोयल**
       28. **कोयल**
       29. **कोयल**
       30. **कोयल**
       31. **कोयल**
       32. **कोयल**
       33. **कोयल**
       34. **कोयल**
       35. **कोयल**
       36. **कोयल**
       37. **कोयल**
       38. **कोयल**
       39. **कोयल**
       40. **कोयल**
       41. **कोयल**
       42. **कोयल**
       43. **कोयल**
       44. **कोयल**
       45. **कोयल**
       46. **कोयल**
       47. **कोयल**
       48. **कोयल**
       49. **कोयल**
       50. **कोयल**
       51. **कोयल**
       52. **कोयल**
       53. **कोयल**
       54. **कोयल**
       55. **कोयल**
       56. **कोयल**
       57. **कोयल**
       58. **कोयल**
       59. **कोयल**
       60. **कोयल**
       61. **कोयल**
       62. **कोयल**
       63. **कोयल**
       64. **कोयल**
       65. **कोयल*
       ... [TRUNCATED FOR BREVITY] ...
       ```
---
| 18 | 3 | `how to verify cast certificate status?` | 2 | 4.50s | en | 4 | follow_up |

### Query 18 Details
* **Query**: `how to verify cast certificate status?`
* **Selected SNO**: 2
* **Detected Language**: `en`
* **Classified Service ID**: `4`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `how to verify cast certificate status?`
* **Resolved Hindi Query**: `किसे प्रमाणपत्र की स्थिति की पुष्टि कैसे करें?`
* **Final Synthesized Response**:
  > To verify the status of a caste certificate in Chhattisgarh, you can use the following methods:
  > 
  > 1. **Online Status Check**:
  >    - Visit the Chhattisgarh e-District portal: `cgedistrict.cgstate.gov.in`
  >    - Click on "Track Application Status" or "View Application Status"
  >    - Enter your application number or registration ID
  >    - View the current status of your caste certificate application
  > 
  > 2. **Sewa Setu Portal**:
  >    - Use the Sewa Setu application to check application status
  >    - Log in with your credentials
  >    - Navigate to the application tracking section
  > 
  > 3. **Contact Sewa Setu Kendra**:
  >    - Visit the nearest Sewa Setu Kendra
  >    - Provide your application number or registration details
  >    - They can help you check the status of your caste certificate application
  > 
  > 4. **Email/Phone Inquiry**:
  >    - Contact the Revenue and Disaster Management Department
  >    - Provide your application details for status verification
  > 
  > The status will typically show whether your application is submitted, under review, approved, or rejected. You can also track the timeline of your application, which is usually processed within 22 days as per the service details.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       how to verify cast certificate status?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       how to verify cast certificate status?
       ```
     * **Response**:
       ```json
       किसे प्रमाणपत्र की स्थिति की पुष्टि कैसे करें?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       how to verify cast certificate status?
       ```
     * **Response**:
       ```json
       how to verify cast certificate status?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "how to verify cast certificate status?",
         "recent_history": [
           {
             "role": "user",
             "content": "kya st praman patra ke liye digital signature chahiye?"
           },
           {
             "role": "assistant",
             "content": "Nahi, SC/ST certificate ke liye digital signature zaroori nahi hai. Ye ek online application process hai, jisme aapko apne documents upload karne hote hain. Koi physical signature ya digital signature ki requirement nahi hai. Aap bas apne documents ki scanned copies upload karke form fill kar sakte hain.\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)"
           },
           {
             "role": "user",
             "content": "st caste praman patra timeline"
           },
           {
             "role": "assistant",
             "content": "The SC/ST certificate has a time limit of 22 days for processing. This is mentioned in the service details manual. After you
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "how to verify cast certificate status?",
         "topic_summary": "The user is asking about the process to verify the status of a caste certificate, which is a follow-up question related to the SC/ST certificate service discussed previously."
       }
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       To verify the status of a caste certificate in Chhattisgarh, you can use the following methods:
       
       1. **Online Status Check**:
          - Visit the Chhattisgarh e-District portal: `cgedistrict.cgstate.gov.in`
          - Click on "Track Application Status" or "View Application Status"
          - Enter your application number or registration ID
          - View the current status of your caste certificate application
       
       2. **Sewa Setu Portal**:
          - Use the Sewa Setu application to check application status
          - Log in with your credentials
          - Navigate to the application tracking section
       
       3. **Contact Sewa Setu Kendra**:
          - Visit the nearest Sewa Setu Kendra
          - Provide your application number or registration details
          - They can help you check the status of your caste certificate application
       
       4. **Email/Phone Inquiry**:
          - Contact the Revenue and Disaster Management Department
          - Provide your application details for status verification
       
       The status will typically show whether your application is submitted, 
       ... [TRUNCATED FOR BREVITY] ...
       ```
---
| 19 | 3 | `thanks` | 2 | 1.42s | N/A | N/A | thanks |

### Query 19 Details
* **Query**: `thanks`
* **Selected SNO**: 2
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `thanks`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > You're welcome! 🙏 Is there anything else I can help you with regarding Chhattisgarh government services?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       thanks
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       thanks
       ```
     * **Response**:
       ```json
       thanks
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       thanks
       ```
     * **Response**:
       ```json
       धन्यवाद
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "thanks",
         "recent_history": [
           {
             "role": "user",
             "content": "st caste praman patra timeline"
           },
           {
             "role": "assistant",
             "content": "The SC/ST certificate has a time limit of 22 days for processing. This is mentioned in the service details manual. After you submit your application, you will receive a receipt with a tracking number. You can check the status of your application on the e-District portal using this tracking number. If the certificate is issued, you can download a copy from the same portal. If you need to apply for a temporary certificate, the time limit is 30 working days.\n\nFor more details and online application, please visit:\n[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)"
           },
           {
             "role": "user",
             "content": "sc caste list cg"
           },
           {
             "role": "assistant",
             "content": "हाँ, छत्तीसगढ़ में अनुसूचित जाति की सूची उपलब्ध है। यह सूची संविधान
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "thanks",
         "resolved_query": "thanks",
         "topic_summary": ""
       }
       ```
---
| 20 | 4 | `OBC certificate praman patra fees kya hai?` | 3 | 3.57s | hinglish | 5 | new_topic |

### Query 20 Details
* **Query**: `OBC certificate praman patra fees kya hai?`
* **Selected SNO**: 3
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the fee for an OBC certificate?`
* **Resolved Hindi Query**: `ओ बी सी प्रमाणपत्र शुल्क क्या है?`
* **Final Synthesized Response**:
  > OBC certificate ke liye application fee ₹30.0 hai. Yeh fee online ya kiosk center, dono jagah pay kar sakte hain. Koi extra charge nahi hai.
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       OBC certificate certificate fees kya hai?
       ```
     * **Response**:
       ```json
       ओ बी सी प्रमाणपत्र शुल्क क्या है?
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       OBC certificate certificate fees kya hai?
       ```
     * **Response**:
       ```json
       What is the fee for an OBC certificate?
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       OBC certificate certificate fees kya hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "OBC certificate certificate fees kya hai?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "OBC certificate certificate fees kya hai?",
         "topic_summary": "OBC certificate fees"
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "OBC certificate certificate fees kya hai?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "3",
         "service_id": "5"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       OBC certificate ke liye application fee ₹30.0 hai. Yeh fee online ya kiosk center, dono jagah pay kar sakte hain. Koi extra charge nahi hai.
       ```
---
| 21 | 4 | `OBC certificate ke liye income limit kitni hai?` | 3 | 4.93s | hinglish | 5 | follow_up |

### Query 21 Details
* **Query**: `OBC certificate ke liye income limit kitni hai?`
* **Selected SNO**: 3
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `What is the income limit for an OBC certificate?`
* **Resolved Hindi Query**: `ओ बी सी प्रमाणपत्र के लिए आय सीमा कितनी है?`
* **Final Synthesized Response**:
  > OBC certificate ke liye income limit ki koi specific limit nahi hai. Income proof (Mandatory: Yes) ke liye aapko income certificate dena padta hai, lekin income ki koi fixed limit nahi hai.
  > 
  > Aap income proof ke liye ye documents use kar sakte hain:
  > - Patwari/Sarpanch/Parshad se income certificate
  > - Employer/Form 16 ka income certificate
  > - Ration card
  > - Zameen/ghar se hone vali income
  > - Other documents
  > 
  > Agar aapko aur jaankari chahiye, toh official manual check karein.
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       OBC certificate ke liye income limit kitni hai?
       ```
     * **Response**:
       ```json
       What is the income limit for an OBC certificate?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       OBC certificate ke liye income limit kitni hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       OBC certificate ke liye income limit kitni hai?
       ```
     * **Response**:
       ```json
       ओ बी सी प्रमाणपत्र के लिए आय सीमा कितनी है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "OBC certificate ke liye income limit kitni hai?",
         "recent_history": [
           {
             "role": "user",
             "content": "OBC certificate praman patra fees kya hai?"
           },
           {
             "role": "assistant",
             "content": "OBC certificate ke liye application fee ₹30.0 hai. Yeh fee online ya kiosk center, dono jagah pay kar sakte hain. Koi extra charge nahi hai.\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)"
           }
         ]
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "OBC certificate ke liye income limit kitni hai?",
         "topic_summary": "OBC certificate ke liye income limit"
       }
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       OBC certificate ke liye income limit ki koi specific limit nahi hai. Income proof (Mandatory: Yes) ke liye aapko income certificate dena padta hai, lekin income ki koi fixed limit nahi hai.
       
       Aap income proof ke liye ye documents use kar sakte hain:
       - Patwari/Sarpanch/Parshad se income certificate
       - Employer/Form 16 ka income certificate
       - Ration card
       - Zameen/ghar se hone vali income
       - Other documents
       
       Agar aapko aur jaankari chahiye, toh official manual check karein.
       ```
---
| 22 | 4 | `OBC list CG` | 3 | 6.67s | hinglish | 5 | new_topic |

### Query 22 Details
* **Query**: `OBC list CG`
* **Selected SNO**: 3
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `OBC list CG`
* **Resolved Hindi Query**: `OBC सूची CG`
* **Final Synthesized Response**:
  > OBC list CG के लिए आपको आधिकारिक वेबसाइट पर जाना होगा। Sewa Setu पोर्टल पर जाकर आप अन्य पिछड़ा वर्ग की सूची देख सकते हैं। यह सूची राज्य सरकार द्वारा समय-समय पर अपडेट की जाती है। आप सीधे cgedistrict.cgstate.gov.in पर जाकर इस जानकारी को प्राप्त कर सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       OBC list CG
       ```
     * **Response**:
       ```json
       OBC list CG
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       OBC list CG
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       OBC list CG
       ```
     * **Response**:
       ```json
       OBC सूची CG
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "OBC list CG",
         "recent_history": [
           {
             "role": "user",
             "content": "OBC certificate praman patra fees kya hai?"
           },
           {
             "role": "assistant",
             "content": "OBC certificate ke liye application fee ₹30.0 hai. Yeh fee online ya kiosk center, dono jagah pay kar sakte hain. Koi extra charge nahi hai.\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)"
           },
           {
             "role": "user",
             "content": "OBC certificate ke liye income limit kitni hai?"
           },
           {
             "role": "assistant",
             "content": "OBC certificate ke liye income limit ki koi specific limit nahi hai. Income proof (Mandatory: Yes) ke liye aapko income certificate dena padta hai, lekin income ki koi fixed limit nahi hai.\n\nAap income proof ke liye ye documents use kar sakte hain:\n- Patwari/Sarpanch/Parshad se income certificate\n- Employe
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "OBC list CG",
         "topic_summary": "The user is asking about the OBC list in Chhattisgarh, which is a different service from the previous conversation about income limit for an OBC certificate."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "OBC list CG",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "3",
         "service_id": "5"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       OBC list CG के लिए आपको आधिकारिक वेबसाइट पर जाना होगा। Sewa Setu पोर्टल पर जाकर आप अन्य पिछड़ा वर्ग की सूची देख सकते हैं। यह सूची राज्य सरकार द्वारा समय-समय पर अपडेट की जाती है। आप सीधे cgedistrict.cgstate.gov.in पर जाकर इस जानकारी को प्राप्त कर सकते हैं।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nOBC list CG के लिए आपको आधिकारिक वेबसाइट पर जाना होगा। Sewa Setu पोर्टल पर जाकर आप अन्य पिछड़ा वर्ग की सूची देख सकते हैं। यह सूची राज्य सरकार द्वारा समय-समय पर अपडेट की जाती है। आप सीधे cgedistrict.cgstate.gov.in पर जाकर इस जानकारी को प्राप्त कर सकते हैं।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       OBC list CG के लिए आपको आधिकारिक वेबसाइट पर जाना होगा। Sewa Setu पोर्टल पर जाकर आप अन्य पिछड़ा वर्ग की सूची देख सकते हैं। यह सूची राज्य सरकार द्वारा समय-समय पर अपडेट की जाती है। आप सीधे cgedistrict.cgstate.gov.in पर जाकर इस जानकारी को प्राप्त कर सकते हैं।
       ```
---
| 23 | 4 | `is digital signature mandatory for OBC?` | 3 | 4.90s | en | 5 | follow_up |

### Query 23 Details
* **Query**: `is digital signature mandatory for OBC?`
* **Selected SNO**: 3
* **Detected Language**: `en`
* **Classified Service ID**: `5`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `Is digital signature mandatory for OBC certificate?`
* **Resolved Hindi Query**: `क्या OBC प्रमाणपत्र के लिए डिजिटल हस्ताक्षर अनिवार्य है?`
* **Final Synthesized Response**:
  > नहीं, OBC प्रमाणपत्र के लिए डिजिटल हस्ताक्षर अनिवार्य नहीं है। आप बिना डिजिटल हस्ताक्षर के भी आवेदन कर सकते हैं।
  > 
  > OBC प्रमाणपत्र आवेदन प्रक्रिया में डिजिटल हस्ताक्षर का उल्लेख नहीं किया गया है। आप आवेदन के दौरान सामान्य रूप से हस्ताक्षर कर सकते हैं।
  > 
  > यदि आप ऑनलाइन आवेदन कर रहे हैं, तो पोर्टल पर उपलब्ध विकल्पों के अनुसार डिजिटल हस्ताक्षर का उपयोग करना बेहतर होगा, लेकिन यह अनिवार्य नहीं है।
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is digital signature mandatory for OBC?
       ```
     * **Response**:
       ```json
       is digital signature mandatory for OBC?
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is digital signature mandatory for OBC?
       ```
     * **Response**:
       ```json
       क्या ओ बी सी के लिए डिजिटल हस्ताक्षर अनिवार्य है?
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is digital signature mandatory for OBC?
       ```
     * **Response**:
       ```json
       en
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is digital signature mandatory for OBC?",
         "recent_history": [
           {
             "role": "user",
             "content": "OBC certificate praman patra fees kya hai?"
           },
           {
             "role": "assistant",
             "content": "OBC certificate ke liye application fee ₹30.0 hai. Yeh fee online ya kiosk center, dono jagah pay kar sakte hain. Koi extra charge nahi hai.\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)"
           },
           {
             "role": "user",
             "content": "OBC certificate ke liye income limit kitni hai?"
           },
           {
             "role": "assistant",
             "content": "OBC certificate ke liye income limit ki koi specific limit nahi hai. Income proof (Mandatory: Yes) ke liye aapko income certificate dena padta hai, lekin income ki koi fixed limit nahi hai.\n\nAap income proof ke liye ye documents use kar sakte hain:\n- Patwari/Sarpanch/Parshad se i
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "Is digital signature mandatory for OBC certificate?",
         "topic_summary": "OBC certificate process and requirements"
       }
       ```
  5. **Function**: `detect_query_language`
     * **Input**:
       ```json
       Is digital signature mandatory for OBC certificate?
       ```
     * **Response**:
       ```json
       en
       ```
  6. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       Is digital signature mandatory for OBC certificate?
       ```
     * **Response**:
       ```json
       क्या OBC प्रमाणपत्र के लिए डिजिटल हस्ताक्षर अनिवार्य है?
       ```
  7. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       Is digital signature mandatory for OBC certificate?
       ```
     * **Response**:
       ```json
       Is digital signature mandatory for OBC certificate?
       ```
  8. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       नहीं, OBC प्रमाणपत्र के लिए डिजिटल हस्ताक्षर अनिवार्य नहीं है। आप बिना डिजिटल हस्ताक्षर के भी आवेदन कर सकते हैं।
       
       OBC प्रमाणपत्र आवेदन प्रक्रिया में डिजिटल हस्ताक्षर का उल्लेख नहीं किया गया है। आप आवेदन के दौरान सामान्य रूप से हस्ताक्षर कर सकते हैं।
       
       यदि आप ऑनलाइन आवेदन कर रहे हैं, तो पोर्टल पर उपलब्ध विकल्पों के अनुसार डिजिटल हस्ताक्षर का उपयोग करना बेहतर होगा, लेकिन यह अनिवार्य नहीं है।
       ```
---
| 24 | 4 | `can non residents apply for obc certificate in cg?` | 3 | 6.01s | hinglish | 5 | new_topic |

### Query 24 Details
* **Query**: `can non residents apply for obc certificate in cg?`
* **Selected SNO**: 3
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `can non residents apply for obc certificate in cg?`
* **Resolved Hindi Query**: `क्या गैर-निवासी छत्तीसगढ़ में ओ बी सी प्रमाणपत्र के लिए आवेदन कर सकते हैं?`
* **Final Synthesized Response**:
  > नहीं, गैर-निवासी छत्तीसगढ़ में ओ बी सी प्रमाण पत्र के लिए आवेदन नहीं कर सकते।
  > 
  > ओ बी सी प्रमाण पत्र के लिए आवेदक का छत्तीसगढ़ की भौगोलिक सीमा में निवास होना अनिवार्य है। यह निवास प्रमाण पत्र या अन्य दस्तावेजों के माध्यम से सिद्ध करना होता है।
  > 
  > यदि आप गैर-निवासी हैं, तो आपको पहले छत्तीसगढ़ में निवास स्थापित करना होगा, जिसके बाद ही आप ओ बी सी प्रमाण पत्र के लिए आवेदन कर सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       can non residents apply for obc certificate in cg?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       can non residents apply for obc certificate in cg?
       ```
     * **Response**:
       ```json
       can non residents apply for obc certificate in cg?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       can non residents apply for obc certificate in cg?
       ```
     * **Response**:
       ```json
       क्या गैर-निवासी छत्तीसगढ़ में ओ बी सी प्रमाणपत्र के लिए आवेदन कर सकते हैं?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "can non residents apply for obc certificate in cg?",
         "recent_history": [
           {
             "role": "user",
             "content": "OBC certificate ke liye income limit kitni hai?"
           },
           {
             "role": "assistant",
             "content": "OBC certificate ke liye income limit ki koi specific limit nahi hai. Income proof (Mandatory: Yes) ke liye aapko income certificate dena padta hai, lekin income ki koi fixed limit nahi hai.\n\nAap income proof ke liye ye documents use kar sakte hain:\n- Patwari/Sarpanch/Parshad se income certificate\n- Employer/Form 16 ka income certificate\n- Ration card\n- Zameen/ghar se hone vali income\n- Other documents\n\nAgar aapko aur jaankari chahiye, toh official manual check karein.\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)"
           },
           {
             "role": "user",
             "content": "OBC list CG"
           },
           {
             "
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "can non residents apply for obc certificate in cg?",
         "topic_summary": "OBC certificate application process for non-residents in Chhattisgarh"
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "can non residents apply for obc certificate in cg?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "3",
         "service_id": "5"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       नहीं, गैर-निवासी छत्तीसगढ़ में ओ बी सी प्रमाण पत्र के लिए आवेदन नहीं कर सकते।
       
       ओ बी सी प्रमाण पत्र के लिए आवेदक का छत्तीसगढ़ की भौगोलिक सीमा में निवास होना अनिवार्य है। यह निवास प्रमाण पत्र या अन्य दस्तावेजों के माध्यम से सिद्ध करना होता है।
       
       यदि आप गैर-निवासी हैं, तो आपको पहले छत्तीसगढ़ में निवास स्थापित करना होगा, जिसके बाद ही आप ओ बी सी प्रमाण पत्र के लिए आवेदन कर सकते हैं।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nनहीं, गैर-निवासी छत्तीसगढ़ में ओ बी सी प्रमाण पत्र के लिए आवेदन नहीं कर सकते।\n\nओ बी सी प्रमाण पत्र के लिए आवेदक का छत्तीसगढ़ की भौगोलिक सीमा में निवास होना अनिवार्य है। यह निवास प्रमाण पत्र या अन्य दस्तावेजों के माध्यम से सिद्ध करना होता है।\n\nयदि आप गैर-निवासी हैं, तो आपको पहले छत्तीसगढ़ में निवास स्थापित करना होगा, जिसके बाद ही आप ओ बी सी प्रमाण पत्र के लिए आवेदन कर सकते हैं।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, गैर-निवासी छत्तीसगढ़ में ओ बी सी प्रमाण पत्र के लिए आवेदन नहीं कर सकते।
       
       ओ बी सी प्रमाण पत्र के लिए आवेदक का छत्तीसगढ़ की भौगोलिक सीमा में निवास होना अनिवार्य है। यह निवास प्रमाण पत्र या अन्य दस्तावेजों के माध्यम से सिद्ध करना होता है।
       
       यदि आप गैर-निवासी हैं, तो आपको पहले छत्तीसगढ़ में निवास स्थापित करना होगा, जिसके बाद ही आप ओ बी सी प्रमाण पत्र के लिए आवेदन कर सकते हैं।
       ```
---
| 25 | 4 | `ok bye` | 3 | 1.45s | N/A | N/A | farewell |

### Query 25 Details
* **Query**: `ok bye`
* **Selected SNO**: 3
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `farewell`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Thank you for using SewaSetu! 🙏 Have a great day. Feel free to come back anytime you need help with government services.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       ok bye
       ```
     * **Response**:
       ```json
       ok bye
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       ok bye
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       ok bye
       ```
     * **Response**:
       ```json
       अलविदा
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ok bye",
         "recent_history": [
           {
             "role": "user",
             "content": "OBC list CG"
           },
           {
             "role": "assistant",
             "content": "OBC list CG के लिए आपको आधिकारिक वेबसाइट पर जाना होगा। Sewa Setu पोर्टल पर जाकर आप अन्य पिछड़ा वर्ग की सूची देख सकते हैं। यह सूची राज्य सरकार द्वारा समय-समय पर अपडेट की जाती है। आप सीधे cgedistrict.cgstate.gov.in पर जाकर इस जानकारी को प्राप्त कर सकते हैं।\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)"
           },
           {
             "role": "user",
             "content": "is digital signature mandatory for OBC?"
           },
           {
             "role": "assistant",
             "content": "नहीं, OBC प्रमाणपत्र के लिए डिजिटल हस्ताक्षर अनिवार्य नहीं है। आप बिना डिजिटल हस्ताक्षर के भी आवेदन कर सकते हैं।\n\nOBC प्रमाणपत्र आवेदन प्रक्रिया में डिजिटल हस्ताक्षर का उल्लेख नहीं किया गया है। आप आवेदन के दौरान सामान्य रूप से हस्ताक्षर क
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "farewell",
         "resolved_query": "ok bye",
         "topic_summary": ""
       }
       ```
---
| 26 | 5 | `CG ka domicile certificate kaise banayein?` | 4 | 10.34s | hinglish | 7 | new_topic |

### Query 26 Details
* **Query**: `CG ka domicile certificate kaise banayein?`
* **Selected SNO**: 4
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to make a CG domicile certificate?`
* **Resolved Hindi Query**: `CG का डोमिसाइल प्रमाणपत्र कैसे बनाएं?`
* **Final Synthesized Response**:
  > CG का domicile certificate बनाने के लिए, आपको Sewa Setu portal पर जाना होगा।
  > 
  > **Step-by-step process:**
  > 
  > 1. **Portal पर जाएं:**
  >    - Website: https://sewasetu.cgstate.gov.in/home?lang=hi
  >    - "Sewa Setu Kendra" पर क्लिक करें।
  > 
  > 2. **Registration करें:**
  >    - "Naya registration karne hetu click karein" पर क्लिक करें।
  >    - अपनी details भरें और "Submit" करें।
  >    - आपको mobile number पर OTP मिलेगा, उसे enter करें।
  > 
  > 3. **Login करें:**
  >    - Username, password, और OTP enter करके login करें।
  > 
  > 4. **Application भरें:**
  >    - "Original Domicile Certificate" के लिए apply करें।
  >    - Form में सभी required details भरें:
  >      - General details (नाम, जन्म तिथि, आदि)
  >      - Address details
  >      - Stay details (जन्म के बाद से कितने साल)
  >      - Education level (10th, 12th, आदि)
  > 
  > 5. **Documents upload करें:**
  >    - Mandatory documents:
  >      - Affidavit (Mandatory)
  >      - Proof of 15 years stay (जैसे birth certificate, service certificate)
  >      - Educational certificate (10th, 12th, आदि)
  >    - Non-mandatory:
  >      - Voters ID, Ration card, Electricity bill
  > 
  > 6. **Fee pay करें:**
  >    - Online fee: ₹30.0
  >    - Kiosk fee: ₹30.0
  > 
  > 7. **Submit करें:**
  >    - "Save and Preview" पर क्लिक करें।
  >    - "Upload" पर click करके documents upload करें।
  >    - "Save Annexure" पर click करें।
  > 
  > **Important points:**
  > - Time limit: 7 days
  > - सभी mandatory documents upload करना जरूरी है।
  > - Form में गलत जानकारी न भरें, वरना application reject हो सकती है।
  > 
  > **Eligibility criteria:**
  > - Criteria A (at least one):
  >   - CG में जन्म (birth certificate)
  >   - या parents 25 साल से CG में रह रहे हों
  >   - या parents CG government/PSU employee हों
  >   - या parents के पास CG में property हो
  > - Criteria B (at least one):
  >   - CG में 3 साल की पढ़ाई
  >   - या Class 5, 8, 10, 12 की board exam CG से pass की हो
  > 
  > **Note:** अगर आप Criteria A और B meet नहीं करते, तो Criteria C के under apply कर सकते हैं:
  > - अगर spouse CG का domicile है
  > - अगर applicant या spouse CG government/PSU employee है
  > - अगर applicant या parent All India Services में हैं और CG cadre मिला है
  > 
  > **SLA:** Service 7 days में deliver किया जाएगा।
  > 
  > **Contact:** Sewa Setu Kendra से contact करें।
  > 
  > **Disclaimer:** यह information official sources से ली गई है। Fees और time limit change हो सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       CG ka domicile certificate kaise banayein?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       CG ka domicile certificate kaise banayein?
       ```
     * **Response**:
       ```json
       How to make a CG domicile certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       CG ka domicile certificate kaise banayein?
       ```
     * **Response**:
       ```json
       CG का डोमिसाइल प्रमाणपत्र कैसे बनाएं?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "CG ka domicile certificate kaise banayein?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "CG ka domicile certificate kaise banayein?",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "CG ka domicile certificate kaise banayein?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "4",
         "service_id": "7"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       CG का domicile certificate बनाने के लिए, आपको Sewa Setu portal पर जाना होगा।
       
       **Step-by-step process:**
       
       1. **Portal पर जाएं:**
          - Website: https://sewasetu.cgstate.gov.in/home?lang=hi
          - "Sewa Setu Kendra" पर क्लिक करें।
       
       2. **Registration करें:**
          - "Naya registration karne hetu click karein" पर क्लिक करें।
          - अपनी details भरें और "Submit" करें।
          - आपको mobile number पर OTP मिलेगा, उसे enter करें।
       
       3. **Login करें:**
          - Username, password, और OTP enter करके login करें।
       
       4. **Application भरें:**
          - "Original Domicile Certificate" के लिए apply करें।
          - Form में सभी required details भरें:
            - General details (नाम, जन्म तिथि, आदि)
            - Address details
            - Stay details (जन्म के बाद से कितने साल)
            - Education level (10th, 12th, आदि)
       
       5. **Documents upload करें:**
          - Mandatory documents:
            - Affidavit (Mandatory)
            - Proof of 15 years stay (जैसे birth certificate, service certificate)
            - Educational certificate (10th, 12th, आदि)
          - Non-mandatory:
         
       ... [TRUNCATED FOR BREVITY] ...
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nCG का domicile certificate बनाने के लिए, आपको Sewa Setu portal पर जाना होगा।\n\n**Step-by-step process:**\n\n1. **Portal पर जाएं:**\n   - Website: https://sewasetu.cgstate.gov.in/home?lang=hi\n   - \"Sewa Setu Kendra\" पर क्लिक करें।\n\n2. **Registration करें:**\n   - \"Naya registration karne hetu click karein\" पर क्लिक करें।\n   - अपनी details भरें और \"Submit\" करें।\n   - आपको mobile number पर OTP मिलेगा, उसे enter करें।\n\n3. **Login करें:**\n   - Username, password, और OTP enter करके login करें।\n\n4. **Application भरें:**\n   - \"Original Domicile Certificate\" के लिए apply करें।\n   - 
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       CG का domicile certificate बनाने के लिए, आपको Sewa Setu portal पर जाना होगा।
       
       **Step-by-step process:**
       
       1. **Portal पर जाएं:**
          - Website: https://sewasetu.cgstate.gov.in/home?lang=hi
          - "Sewa Setu Kendra" पर क्लिक करें।
       
       2. **Registration करें:**
          - "Naya registration karne hetu click karein" पर क्लिक करें।
          - अपनी details भरें और "Submit" करें।
          - आपको mobile number पर OTP मिलेगा, उसे enter करें।
       
       3. **Login करें:**
          - Username, password, और OTP enter करके login करें।
       
       4. **Application भरें:**
          - "Original Domicile Certificate" के लिए apply करें।
          - Form में सभी required details भरें:
            - General details (नाम, जन्म तिथि, आदि)
            - Address details
            - Stay details (जन्म के बाद से कितने साल)
            - Education level (10th, 12th, आदि)
       
       5. **Documents upload करें:**
          - Mandatory documents:
            - Affidavit (Mandatory)
            - Proof of 15 years stay (जैसे birth certificate, service certificate)
            - Educational certificate (10th, 12th, आदि)
          - Non-mandatory:
         
       ... [TRUNCATED FOR BREVITY] ...
       ```
---
| 27 | 5 | `domicile certificate cg eligibility rules` | 4 | 2.76s | N/A | 7 | Interactive Checkpoint Intercept |

### Query 27 Details
* **Query**: `domicile certificate cg eligibility rules`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `7`
* **Classified Intent**: `Interactive Checkpoint Intercept`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Domicile Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       domicile certificate cg eligibility rules
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       domicile certificate cg eligibility rules
       ```
     * **Response**:
       ```json
       domicile certificate cg eligibility rules
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       domicile certificate cg eligibility rules
       ```
     * **Response**:
       ```json
       domicile certificate cg eligibility rules
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "domicile certificate cg eligibility rules",
         "recent_history": [
           {
             "role": "user",
             "content": "CG ka domicile certificate kaise banayein?"
           },
           {
             "role": "assistant",
             "content": "CG का domicile certificate बनाने के लिए, आपको Sewa Setu portal पर जाना होगा।\n\n**Step-by-step process:**\n\n1. **Portal पर जाएं:**\n   - Website: https://sewasetu.cgstate.gov.in/home?lang=hi\n   - \"Sewa Setu Kendra\" पर क्लिक करें।\n\n2. **Registration करें:**\n   - \"Naya registration karne hetu click karein\" पर क्लिक करें।\n   - अपनी details भरें और \"Submit\" करें।\n   - आपको mobile number पर OTP मिलेगा, उसे enter करें।\n\n3. **Login करें:**\n   - Username, password, और OTP enter करके login करें।\n\n4. **Application भरें:**\n   - \"Original Domicile Certificate\" के लिए apply करें।\n   - Form में सभी required details भरें:\n     - General details (नाम, जन्म तिथि, आदि)\n     - Address details\n     - Stay details (जन्म के बाद से कितने साल)\n     - Education
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "CG domicile certificate eligibility rules",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "CG domicile certificate eligibility rules",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "4",
         "service_id": "7"
       }
       ```
---
| 28 | 5 | `kya school study cg me 3 saal hona mandatory hai?` | 4 | 5.65s | hinglish | 7 | follow_up |

### Query 28 Details
* **Query**: `kya school study cg me 3 saal hona mandatory hai?`
* **Selected SNO**: 4
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `What is the eligibility rule for school study in CG? Is 3 years of study mandatory?`
* **Resolved Hindi Query**: `सी जी में स्कूल अध्ययन के लिए पात्रता नियम क्या है? क्या 3 वर्ष का अध्ययन अनिवार्य है?`
* **Final Synthesized Response**:
  > Haan, 3 saal ki school study CG mein Domicile Certificate ke liye ek zaroori criteria hai.
  > 
  > **Eligibility Rules for School Study in CG:**
  > 
  > **Main Path (Dono Criteria A aur B zaroori hain):**
  > 
  > **Criteria A (Residence Proof):**
  > - Aapka janm CG mein hua ho
  > - Ya aapke parents 25 saal se CG mein reh rahe hon
  > - Ya aapke parents CG government/PSU ke employee hon
  > - Ya aapke paas CG mein 5 saal ki property ho
  > 
  > **Criteria B (Education Proof):**
  > - Aapne CG mein kam se kam 3 saal ki school study ki ho
  > - Ya aapne CG se 5th, 8th, 10th, ya 12th board exam pass kiya ho
  > 
  > **Important:** Criteria A aur B dono satisfy karne padenge. Sirf 3 saal ki study kaafi nahi hai, residence proof bhi zaroori hai.
  > 
  > **Exceptions (Criteria C) bhi hain** jismein ye apply ho sakte hain:
  > - Aapke spouse ka CG domicile ho
  > - Aap ya aapke spouse CG government/PSU employee ho
  > - Aap ya aapke parent All India Services mein ho aur CG cadre allot hua ho
  > 
  > Kya aap specific situation ke baare mein jaanna chahte hain?
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       kya school study cg me 3 saal hona mandatory hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       kya school study cg me 3 saal hona mandatory hai?
       ```
     * **Response**:
       ```json
       क्या स्कूल स्टडी सी जी में 3 साल होना अनिवार्य है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       kya school study cg me 3 saal hona mandatory hai?
       ```
     * **Response**:
       ```json
       Is it mandatory to study CG in school for 3 years?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "kya school study cg me 3 saal hona mandatory hai?",
         "recent_history": [
           {
             "role": "user",
             "content": "CG ka domicile certificate kaise banayein?"
           },
           {
             "role": "assistant",
             "content": "CG का domicile certificate बनाने के लिए, आपको Sewa Setu portal पर जाना होगा।\n\n**Step-by-step process:**\n\n1. **Portal पर जाएं:**\n   - Website: https://sewasetu.cgstate.gov.in/home?lang=hi\n   - \"Sewa Setu Kendra\" पर क्लिक करें।\n\n2. **Registration करें:**\n   - \"Naya registration karne hetu click karein\" पर क्लिक करें।\n   - अपनी details भरें और \"Submit\" करें।\n   - आपको mobile number पर OTP मिलेगा, उसे enter करें।\n\n3. **Login करें:**\n   - Username, password, और OTP enter करके login करें।\n\n4. **Application भरें:**\n   - \"Original Domicile Certificate\" के लिए apply करें।\n   - Form में सभी required details भरें:\n     - General details (नाम, जन्म तिथि, आदि)\n     - Address details\n     - Stay details (जन्म के बाद से कितने साल)\n     - E
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What is the eligibility rule for school study in CG? Is 3 years of study mandatory?",
         "topic_summary": "Eligibility criteria for Domicile Certificate for school study in CG."
       }
       ```
  5. **Function**: `detect_query_language`
     * **Input**:
       ```json
       What is the eligibility rule for school study in CG? Is 3 years of study mandatory?
       ```
     * **Response**:
       ```json
       en
       ```
  6. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       What is the eligibility rule for school study in CG? Is 3 years of study mandatory?
       ```
     * **Response**:
       ```json
       सी जी में स्कूल अध्ययन के लिए पात्रता नियम क्या है? क्या 3 वर्ष का अध्ययन अनिवार्य है?
       ```
  7. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       What is the eligibility rule for school study in CG? Is 3 years of study mandatory?
       ```
     * **Response**:
       ```json
       What is the eligibility rule for school study in CG? Is 3 years of study mandatory?
       ```
  8. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Haan, 3 saal ki school study CG mein Domicile Certificate ke liye ek zaroori criteria hai.
       
       **Eligibility Rules for School Study in CG:**
       
       **Main Path (Dono Criteria A aur B zaroori hain):**
       
       **Criteria A (Residence Proof):**
       - Aapka janm CG mein hua ho
       - Ya aapke parents 25 saal se CG mein reh rahe hon
       - Ya aapke parents CG government/PSU ke employee hon
       - Ya aapke paas CG mein 5 saal ki property ho
       
       **Criteria B (Education Proof):**
       - Aapne CG mein kam se kam 3 saal ki school study ki ho
       - Ya aapne CG se 5th, 8th, 10th, ya 12th board exam pass kiya ho
       
       **Important:** Criteria A aur B dono satisfy karne padenge. Sirf 3 saal ki study kaafi nahi hai, residence proof bhi zaroori hai.
       
       **Exceptions (Criteria C) bhi hain** jismein ye apply ho sakte hain:
       - Aapke spouse ka CG domicile ho
       - Aap ya aapke spouse CG government/PSU employee ho
       - Aap ya aapke parent All India Services mein ho aur CG cadre allot hua ho
       
       Kya aap specific situation ke baare mein jaanna chahte hain?
       ```
---
| 29 | 5 | `niwas praman patra exceptions list` | 4 | 2.95s | N/A | 7 | Interactive Checkpoint Intercept |

### Query 29 Details
* **Query**: `niwas praman patra exceptions list`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `7`
* **Classified Intent**: `Interactive Checkpoint Intercept`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Domicile Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       domicile certificate exceptions list
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       domicile certificate exceptions list
       ```
     * **Response**:
       ```json
       domicile certificate exceptions list
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       domicile certificate exceptions list
       ```
     * **Response**:
       ```json
       domicile certificate exceptions list
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "domicile certificate exceptions list",
         "recent_history": [
           {
             "role": "user",
             "content": "CG ka domicile certificate kaise banayein?"
           },
           {
             "role": "assistant",
             "content": "CG का domicile certificate बनाने के लिए, आपको Sewa Setu portal पर जाना होगा।\n\n**Step-by-step process:**\n\n1. **Portal पर जाएं:**\n   - Website: https://sewasetu.cgstate.gov.in/home?lang=hi\n   - \"Sewa Setu Kendra\" पर क्लिक करें।\n\n2. **Registration करें:**\n   - \"Naya registration karne hetu click karein\" पर क्लिक करें।\n   - अपनी details भरें और \"Submit\" करें।\n   - आपको mobile number पर OTP मिलेगा, उसे enter करें।\n\n3. **Login करें:**\n   - Username, password, और OTP enter करके login करें।\n\n4. **Application भरें:**\n   - \"Original Domicile Certificate\" के लिए apply करें।\n   - Form में सभी required details भरें:\n     - General details (नाम, जन्म तिथि, आदि)\n     - Address details\n     - Stay details (जन्म के बाद से कितने साल)\n     - Education leve
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "domicile certificate exceptions list",
         "topic_summary": "The user is asking for a list of exceptions to the domicile certificate eligibility rules in Chhattisgarh, which is a new topic distinct from the previous discussion about school study requirements."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "domicile certificate exceptions list",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "4",
         "service_id": "7"
       }
       ```
---
| 30 | 5 | `kya out of state domicile certificate mil sakta hai?` | 4 | 6.82s | hinglish | 7 | new_topic |

### Query 30 Details
* **Query**: `kya out of state domicile certificate mil sakta hai?`
* **Selected SNO**: 4
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Can I get an out-of-state domicile certificate?`
* **Resolved Hindi Query**: `क्या आउट ऑफ स्टेट domicile certificate मिल सकता है?`
* **Final Synthesized Response**:
  > नहीं, out of state domicile certificate नहीं मिल सकता। Domicile certificate केवल उसी राज्य में जारी होता है जहाँ आप निवास करते हैं। अगर आप किसी और राज्य में रहते हैं, तो वहाँ से domicile certificate नहीं बन सकता। आपको अपने निवास वाले राज्य में ही apply करना होगा।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       kya out of state domicile certificate mil sakta hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       kya out of state domicile certificate mil sakta hai?
       ```
     * **Response**:
       ```json
       क्या आउट ऑफ स्टेट domicile certificate मिल सकता है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       kya out of state domicile certificate mil sakta hai?
       ```
     * **Response**:
       ```json
       Can I get an out-of-state domicile certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "kya out of state domicile certificate mil sakta hai?",
         "recent_history": [
           {
             "role": "user",
             "content": "domicile certificate cg eligibility rules"
           },
           {
             "role": "assistant",
             "content": "Would you like to check your eligibility for the Domicile Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?"
           },
           {
             "role": "user",
             "content": "kya school study cg me 3 saal hona mandatory hai?"
           },
           {
             "role": "assistant",
             "content": "Haan, 3 saal ki school study CG mein Domicile Certificate ke liye ek zaroori criteria hai.\n\n**Eligibility Rules for School Study in CG:**\n\n**Main Path (Dono Criteria A aur B zaroori hain):**\n\n**Criteria A (Residence Proof):**\n- Aapka janm CG mein hua ho\n- Ya aapke parents 25 saal se CG mein reh rahe hon\n- Ya aapke parents CG government/PSU ke employee hon\n- Ya aapke paas CG mein 5 saal ki property h
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Can an out-of-state domicile certificate be obtained in Chhattisgarh?",
         "topic_summary": "The user is asking about the eligibility and process for an out-of-state domicile certificate, which is a different service from the Domicile Certificate previously discussed."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "Can an out-of-state domicile certificate be obtained in Chhattisgarh?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "4",
         "service_id": "7"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       नहीं, out of state domicile certificate नहीं मिल सकता। Domicile certificate केवल उसी राज्य में जारी होता है जहाँ आप निवास करते हैं। अगर आप किसी और राज्य में रहते हैं, तो वहाँ से domicile certificate नहीं बन सकता। आपको अपने निवास वाले राज्य में ही apply करना होगा।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nनहीं, out of state domicile certificate नहीं मिल सकता। Domicile certificate केवल उसी राज्य में जारी होता है जहाँ आप निवास करते हैं। अगर आप किसी और राज्य में रहते हैं, तो वहाँ से domicile certificate नहीं बन सकता। आपको अपने निवास वाले राज्य में ही apply करना होगा।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, out of state domicile certificate नहीं मिल सकता। Domicile certificate केवल उसी राज्य में जारी होता है जहाँ आप निवास करते हैं। अगर आप किसी और राज्य में रहते हैं, तो वहाँ से domicile certificate नहीं बन सकता। आपको अपने निवास वाले राज्य में ही apply करना होगा।
       ```
---
| 31 | 5 | `how many days for domicile certificate?` | 4 | 4.99s | en | 7 | follow_up |

### Query 31 Details
* **Query**: `how many days for domicile certificate?`
* **Selected SNO**: 4
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `how many days for domicile certificate?`
* **Resolved Hindi Query**: `कितने दिन के लिए डोमिसाइल सर्टिफिकेट?`
* **Final Synthesized Response**:
  > The Domicile Certificate is issued within 7 days as per the Service Level Agreement (SLA).
  > 
  > The time limit for service delivery is 7 working days from the date of application.
  > 
  > You can track the status of your application online through the Sewa Setu portal.
  > 
  > If the service is not delivered within the stipulated time, you can file a complaint or appeal as per the Lok Seva Guarantee Rules, 2011.
  > 
  > The application can be submitted either online or at a Sewa Setu Kendra.
  > 
  > The fee for the Domicile Certificate is ₹30.0, which can be paid online or at the kiosk.
  > 
  > The required documents include an affidavit, proof of at least 15 years of stay, and educational certificates.
  > 
  > For more details, you can visit the official Sewa Setu portal or contact the Revenue and Disaster Management Department.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       how many days for domicile certificate?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       how many days for domicile certificate?
       ```
     * **Response**:
       ```json
       कितने दिन के लिए डोमिसाइल सर्टिफिकेट?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       how many days for domicile certificate?
       ```
     * **Response**:
       ```json
       how many days for domicile certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "how many days for domicile certificate?",
         "recent_history": [
           {
             "role": "user",
             "content": "kya school study cg me 3 saal hona mandatory hai?"
           },
           {
             "role": "assistant",
             "content": "Haan, 3 saal ki school study CG mein Domicile Certificate ke liye ek zaroori criteria hai.\n\n**Eligibility Rules for School Study in CG:**\n\n**Main Path (Dono Criteria A aur B zaroori hain):**\n\n**Criteria A (Residence Proof):**\n- Aapka janm CG mein hua ho\n- Ya aapke parents 25 saal se CG mein reh rahe hon\n- Ya aapke parents CG government/PSU ke employee hon\n- Ya aapke paas CG mein 5 saal ki property ho\n\n**Criteria B (Education Proof):**\n- Aapne CG mein kam se kam 3 saal ki school study ki ho\n- Ya aapne CG se 5th, 8th, 10th, ya 12th board exam pass kiya ho\n\n**Important:** Criteria A aur B dono satisfy karne padenge. Sirf 3 saal ki study kaafi nahi hai, residence proof bhi zaroori hai.\n\n**Exceptions (Criteria C) bhi hain** jismein ye apply ho 
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "how many days for domicile certificate?",
         "topic_summary": "The user is asking about the timeline for obtaining a domicile certificate, which is a follow-up question to the previous discussion about the certificate's eligibility and issuance process."
       }
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The Domicile Certificate is issued within 7 days as per the Service Level Agreement (SLA).
       
       The time limit for service delivery is 7 working days from the date of application.
       
       You can track the status of your application online through the Sewa Setu portal.
       
       If the service is not delivered within the stipulated time, you can file a complaint or appeal as per the Lok Seva Guarantee Rules, 2011.
       
       The application can be submitted either online or at a Sewa Setu Kendra.
       
       The fee for the Domicile Certificate is ₹30.0, which can be paid online or at the kiosk.
       
       The required documents include an affidavit, proof of at least 15 years of stay, and educational certificates.
       
       For more details, you can visit the official Sewa Setu portal or contact the Revenue and Disaster Management Department.
       ```
---
| 32 | 5 | `is voter id proof of stay for domicile?` | 4 | 4.67s | en | 7 | new_topic |

### Query 32 Details
* **Query**: `is voter id proof of stay for domicile?`
* **Selected SNO**: 4
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is voter ID proof of stay for domicile?`
* **Resolved Hindi Query**: `क्या मतदाता पहचान पत्र निवास का प्रमाण है?`
* **Final Synthesized Response**:
  > No, a voter ID is not considered proof of stay for a domicile certificate.
  > 
  > According to the required documents for a Domicile Certificate, a voter ID is listed under "Supporting Document 1: Voters Identity Card" in the "Proof Of At Least 15 Years Stay" category. This category is mandatory and requires specific documents like birth certificates, service certificates, or land documents to establish 15 years of residence.
  > 
  > A voter ID only proves your identity and residence at the time of voting, not continuous residence for the required period. You must provide separate documents from the "Proof Of At Least 15 Years Stay" list to meet the eligibility criteria.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is voter id proof of stay for domicile?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is voter id proof of stay for domicile?
       ```
     * **Response**:
       ```json
       Is voter ID proof of stay for domicile?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is voter id proof of stay for domicile?
       ```
     * **Response**:
       ```json
       क्या मतदाता पहचान पत्र निवास का प्रमाण है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is voter id proof of stay for domicile?",
         "recent_history": [
           {
             "role": "user",
             "content": "niwas praman patra exceptions list"
           },
           {
             "role": "assistant",
             "content": "Would you like to check your eligibility for the Domicile Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?"
           },
           {
             "role": "user",
             "content": "kya out of state domicile certificate mil sakta hai?"
           },
           {
             "role": "assistant",
             "content": "नहीं, out of state domicile certificate नहीं मिल सकता। Domicile certificate केवल उसी राज्य में जारी होता है जहाँ आप निवास करते हैं। अगर आप किसी और राज्य में रहते हैं, तो वहाँ से domicile certificate नहीं बन सकता। आपको अपने निवास वाले राज्य में ही apply करना होगा।\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is voter ID proof of stay for domicile?",
         "topic_summary": "Query about using voter ID as proof of stay for domicile certificate."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "Is voter ID proof of stay for domicile?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": null,
         "service_id": null
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       No, a voter ID is not considered proof of stay for a domicile certificate.
       
       According to the required documents for a Domicile Certificate, a voter ID is listed under "Supporting Document 1: Voters Identity Card" in the "Proof Of At Least 15 Years Stay" category. This category is mandatory and requires specific documents like birth certificates, service certificates, or land documents to establish 15 years of residence.
       
       A voter ID only proves your identity and residence at the time of voting, not continuous residence for the required period. You must provide separate documents from the "Proof Of At Least 15 Years Stay" list to meet the eligibility criteria.
       ```
---
| 33 | 6 | `naam badalne ka kya process hai` | 5 | 4.42s | hinglish | 201 | new_topic |

### Query 33 Details
* **Query**: `naam badalne ka kya process hai`
* **Selected SNO**: 5
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the process for changing a name?`
* **Resolved Hindi Query**: `नाम बदलने का क्या प्रोसेस है?`
* **Final Synthesized Response**:
  > Namaste! Naam badalne ka process yeh hai:
  > 
  > **Pehle ye documents chahiye:**
  > 1. SBI ka ₹430 ka challan (mandatory)
  > 2. ₹50 ka notarized affidavit (Form-III)
  > 3. Local newspaper mein notice (3 mahine purana)
  > 4. Do witnesses ka form-II deed
  > 5. Old aur new name ka proof
  > 6. Sabhi documents ka reference
  > 
  > **Online apply kaise karein:**
  > - Sewa Setu portal par jao
  > - Form fill karke documents upload karo
  > - Fee ₹30 online ya kiosk par
  > 
  > **Time limit:** 29 days mein process hota hai.
  > 
  > Koi specific step ke baare mein jaanna hai?
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       naam badalne ka kya process hai
       ```
     * **Response**:
       ```json
       What is the process for changing a name?
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       naam badalne ka kya process hai
       ```
     * **Response**:
       ```json
       नाम बदलने का क्या प्रोसेस है?
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       naam badalne ka kya process hai
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "naam badalne ka kya process hai",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the process for name change?",
         "topic_summary": "User is asking about the process for name change, which is a different service from the initial query about changing name (which was implicitly about name change)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "What is the process for name change?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "5",
         "service_id": "201"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Namaste! Naam badalne ka process yeh hai:
       
       **Pehle ye documents chahiye:**
       1. SBI ka ₹430 ka challan (mandatory)
       2. ₹50 ka notarized affidavit (Form-III)
       3. Local newspaper mein notice (3 mahine purana)
       4. Do witnesses ka form-II deed
       5. Old aur new name ka proof
       6. Sabhi documents ka reference
       
       **Online apply kaise karein:**
       - Sewa Setu portal par jao
       - Form fill karke documents upload karo
       - Fee ₹30 online ya kiosk par
       
       **Time limit:** 29 days mein process hota hai.
       
       Koi specific step ke baare mein jaanna hai?
       ```
---
| 34 | 6 | `gazette publication name change advertisement fee` | 5 | 4.46s | en | 201 | new_topic |

### Query 34 Details
* **Query**: `gazette publication name change advertisement fee`
* **Selected SNO**: 5
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `gazette publication name change advertisement fee`
* **Resolved Hindi Query**: `गेज़ट प्रकाशन नाम परिवर्तन विज्ञापन शुल्क`
* **Final Synthesized Response**:
  > The fee for gazette publication name change advertisement is ₹30.0. This fee is applicable whether you apply online or at a kiosk. The total application fee is ₹30.0, which covers the cost of the publication process.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       gazette publication name change advertisement fee
       ```
     * **Response**:
       ```json
       gazette publication name change advertisement fee
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       gazette publication name change advertisement fee
       ```
     * **Response**:
       ```json
       गेज़ट प्रकाशन नाम परिवर्तन विज्ञापन शुल्क
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       gazette publication name change advertisement fee
       ```
     * **Response**:
       ```json
       en
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "gazette publication name change advertisement fee",
         "recent_history": [
           {
             "role": "user",
             "content": "naam badalne ka kya process hai"
           },
           {
             "role": "assistant",
             "content": "Namaste! Naam badalne ka process yeh hai:\n\n**Pehle ye documents chahiye:**\n1. SBI ka ₹430 ka challan (mandatory)\n2. ₹50 ka notarized affidavit (Form-III)\n3. Local newspaper mein notice (3 mahine purana)\n4. Do witnesses ka form-II deed\n5. Old aur new name ka proof\n6. Sabhi documents ka reference\n\n**Online apply kaise karein:**\n- Sewa Setu portal par jao\n- Form fill karke documents upload karo\n- Fee ₹30 online ya kiosk par\n\n**Time limit:** 29 days mein process hota hai.\n\nKoi specific step ke baare mein jaanna hai?\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)"
           }
         ]
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the fee for gazette publication for name change advertisement?",
         "topic_summary": "User is inquiring about the fee for the gazette publication process related to a name change."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "What is the fee for gazette publication for name change advertisement?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "5",
         "service_id": "201"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The fee for gazette publication name change advertisement is ₹30.0. This fee is applicable whether you apply online or at a kiosk. The total application fee is ₹30.0, which covers the cost of the publication process.
       ```
---
| 35 | 6 | `affidavit stamp paper fee for name change` | 5 | 3.58s | en | 201 | new_topic |

### Query 35 Details
* **Query**: `affidavit stamp paper fee for name change`
* **Selected SNO**: 5
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `affidavit stamp paper fee for name change`
* **Resolved Hindi Query**: `नाम परिवर्तन के लिए शपथ पत्र स्टाम्प पेपर शुल्क`
* **Final Synthesized Response**:
  > The affidavit stamp paper fee for name change is ₹50. This fee must be paid on a non-judicial stamp paper. The stamp paper should not be more than three months old from the date of application. This is a mandatory document for the name change process.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       affidavit stamp paper fee for name change
       ```
     * **Response**:
       ```json
       affidavit stamp paper fee for name change
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       affidavit stamp paper fee for name change
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       affidavit stamp paper fee for name change
       ```
     * **Response**:
       ```json
       नाम परिवर्तन के लिए शपथ पत्र स्टाम्प पेपर शुल्क
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "affidavit stamp paper fee for name change",
         "recent_history": [
           {
             "role": "user",
             "content": "naam badalne ka kya process hai"
           },
           {
             "role": "assistant",
             "content": "Namaste! Naam badalne ka process yeh hai:\n\n**Pehle ye documents chahiye:**\n1. SBI ka ₹430 ka challan (mandatory)\n2. ₹50 ka notarized affidavit (Form-III)\n3. Local newspaper mein notice (3 mahine purana)\n4. Do witnesses ka form-II deed\n5. Old aur new name ka proof\n6. Sabhi documents ka reference\n\n**Online apply kaise karein:**\n- Sewa Setu portal par jao\n- Form fill karke documents upload karo\n- Fee ₹30 online ya kiosk par\n\n**Time limit:** 29 days mein process hota hai.\n\nKoi specific step ke baare mein jaanna hai?\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)"
           },
           {
             "role": "user",
             "content": "gaz
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What is the fee for the affidavit stamp paper required for name change?",
         "topic_summary": "The user is asking about the fee for a specific document (affidavit stamp paper) related to the previously discussed service (name change)."
       }
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The affidavit stamp paper fee for name change is ₹50. This fee must be paid on a non-judicial stamp paper. The stamp paper should not be more than three months old from the date of application. This is a mandatory document for the name change process.
       ```
---
| 36 | 6 | `time limit for name change gazette` | 5 | 4.45s | en | 201 | follow_up |

### Query 36 Details
* **Query**: `time limit for name change gazette`
* **Selected SNO**: 5
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `What is the time limit for name change gazette?`
* **Resolved Hindi Query**: `नाम परिवर्तन के लिए गजट की समय सीमा क्या है?`
* **Final Synthesized Response**:
  > The time limit for the name change gazette process is 29 days. This is specified as the Service Level Agreement (SLA) for the Ordinary Gazette Notification for Name Change service. The process must be completed within this timeframe from the date of application.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       time limit for name change gazette
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       time limit for name change gazette
       ```
     * **Response**:
       ```json
       समय सीमा नाम परिवर्तन गजट के लिए
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       time limit for name change gazette
       ```
     * **Response**:
       ```json
       time limit for name change gazette
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "time limit for name change gazette",
         "recent_history": [
           {
             "role": "user",
             "content": "naam badalne ka kya process hai"
           },
           {
             "role": "assistant",
             "content": "Namaste! Naam badalne ka process yeh hai:\n\n**Pehle ye documents chahiye:**\n1. SBI ka ₹430 ka challan (mandatory)\n2. ₹50 ka notarized affidavit (Form-III)\n3. Local newspaper mein notice (3 mahine purana)\n4. Do witnesses ka form-II deed\n5. Old aur new name ka proof\n6. Sabhi documents ka reference\n\n**Online apply kaise karein:**\n- Sewa Setu portal par jao\n- Form fill karke documents upload karo\n- Fee ₹30 online ya kiosk par\n\n**Time limit:** 29 days mein process hota hai.\n\nKoi specific step ke baare mein jaanna hai?\n\nAdhik jaankari aur online apply karne ke liye, kripya is link par jayein:\n[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)"
           },
           {
             "role": "user",
             "content": "gazette pu
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What is the time limit for name change gazette?",
         "topic_summary": "The user is asking about the timeline for the name change gazette process, which is a follow-up to the previous discussion about the gazette publication fee."
       }
       ```
  5. **Function**: `detect_query_language`
     * **Input**:
       ```json
       What is the time limit for name change gazette?
       ```
     * **Response**:
       ```json
       en
       ```
  6. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       What is the time limit for name change gazette?
       ```
     * **Response**:
       ```json
       What is the time limit for name change gazette?
       ```
  7. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       What is the time limit for name change gazette?
       ```
     * **Response**:
       ```json
       नाम परिवर्तन के लिए गजट की समय सीमा क्या है?
       ```
  8. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The time limit for the name change gazette process is 29 days. This is specified as the Service Level Agreement (SLA) for the Ordinary Gazette Notification for Name Change service. The process must be completed within this timeframe from the date of application.
       ```
---
| 37 | 6 | `name change gazette notification witnesses need?` | 5 | 9.46s | hinglish | 201 | follow_up |

### Query 37 Details
* **Query**: `name change gazette notification witnesses need?`
* **Selected SNO**: 5
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `What are the witness requirements for the name change gazette notification?`
* **Resolved Hindi Query**: `नाम परिवर्तन की गजट सूचना के लिए गवाह की क्या आवश्यकताएं हैं?`
* **Final Synthesized Response**:
  > Name change gazette notification के लिए witness requirements ये हैं:
  > 
  > - आपको दो गवाहों के नाम, हस्ताक्षर और पते के साथ एक मूल प्ररूप-दो में विलिख प्ररूप (विलिख शपथ पत्र) देना होगा।
  > - इस प्ररूप-दो में दो गवाहों के विवरण होने चाहिए।
  > - दोनों गवाहों के हस्ताक्षर और पते अनिवार्य हैं।
  > - गवाहों का पहचान पत्र भी आवश्यक है।
  > - गवाहों का पहचान पत्र आवेदक द्वारा जारी किया गया होना चाहिए।
  > 
  > यह सभी documents mandatory हैं, इसलिए बिना इन documents के application process complete नहीं होगा।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       name change gazette notification witnesses need?
       ```
     * **Response**:
       ```json
       name change gazette notification witnesses need?
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       name change gazette notification witnesses need?
       ```
     * **Response**:
       ```json
       नाम परिवर्तन राजपत्र अधिसूचना गवाहों की आवश्यकता?
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       name change gazette notification witnesses need?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "name change gazette notification witnesses need?",
         "recent_history": [
           {
             "role": "user",
             "content": "gazette publication name change advertisement fee"
           },
           {
             "role": "assistant",
             "content": "The fee for gazette publication name change advertisement is ₹30.0. This fee is applicable whether you apply online or at a kiosk. The total application fee is ₹30.0, which covers the cost of the publication process.\n\nFor more details and online application, please visit:\n[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)"
           },
           {
             "role": "user",
             "content": "affidavit stamp paper fee for name change"
           },
           {
             "role": "assistant",
             "content": "The affidavit stamp paper fee for name change is ₹50. This fee must be paid on a non-judicial stamp paper. The stamp paper should not be more than three months old from the date of application. This is a mandatory document
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What are the witness requirements for the name change gazette notification?",
         "topic_summary": "Details regarding the name change gazette process, including the time limit and witness requirements."
       }
       ```
  5. **Function**: `detect_query_language`
     * **Input**:
       ```json
       What are the witness requirements for the name change gazette notification?
       ```
     * **Response**:
       ```json
       en
       ```
  6. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       What are the witness requirements for the name change gazette notification?
       ```
     * **Response**:
       ```json
       What are the witness requirements for the name change gazette notification?
       ```
  7. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       What are the witness requirements for the name change gazette notification?
       ```
     * **Response**:
       ```json
       नाम परिवर्तन की गजट सूचना के लिए गवाह की क्या आवश्यकताएं हैं?
       ```
  8. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Name change gazette notification के लिए witness requirements ये हैं:
       
       - आपको दो गवाहों के नाम, हस्ताक्षर और पते के साथ एक मूल प्ररूप-दो में विलिख प्ररूप (विलिख शपथ पत्र) देना होगा।
       - इस प्ररूप-दो में दो गवाहों के विवरण होने चाहिए।
       - दोनों गवाहों के हस्ताक्षर और पते अनिवार्य हैं।
       - गवाहों का पहचान पत्र भी आवश्यक है।
       - गवाहों का पहचान पत्र आवेदक द्वारा जारी किया गया होना चाहिए।
       
       यह सभी documents mandatory हैं, इसलिए बिना इन documents के application process complete नहीं होगा।
       ```
  9. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nName change gazette notification के लिए witness requirements ये हैं:\n\n- आपको दो गवाहों के नाम, हस्ताक्षर और पते के साथ एक मूल प्ररूप-दो में विलिख प्ररूप (विलिख शपथ पत्र) देना होगा।\n- इस प्ररूप-दो में दो गवाहों के विवरण होने चाहिए।\n- दोनों गवाहों के हस्ताक्षर और पते अनिवार्य हैं।\n- गवाहों का पहचान पत्र भी आवश्यक है।\n- गवाहों का पहचान पत्र आवेदक द्वारा जारी किया गया होना चाहिए।\n\nयह सभी documents mandatory हैं, इसलिए बिना इन documents के application process complete नहीं होगा।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       Name change gazette notification के लिए witness requirements ये हैं:
       
       - आपको दो गवाहों के नाम, हस्ताक्षर और पते के साथ एक original form-two में lik lik oath-patra (lik lik oath-patra) देना होगा।
       - इस form-two में दो गवाहों के details होने चाहिए।
       - दोनों गवाहों के signatures और addresses mandatory हैं।
       - गवाहों का identity card भी necessary है।
       - गवाहों का identity card applicant द्वारा issued होना चाहिए।
       
       यह सभी documents mandatory हैं, इसलिए बिना इन documents के application process complete नहीं होगा।
       ```
---
| 38 | 6 | `gazette advertisement form I format` | 5 | 4.69s | en | 201 | new_topic |

### Query 38 Details
* **Query**: `gazette advertisement form I format`
* **Selected SNO**: 5
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `gazette advertisement form I format`
* **Resolved Hindi Query**: `gazette advertisement form I format`
* **Final Synthesized Response**:
  > Based on the service specifications for Ordinary Gazette Notification for Name Change (Service ID: 201), the required document format is Form-I, which must be published in a local newspaper.
  > 
  > The key requirements for the gazette advertisement form are:
  > - Must be in Form-I format
  > - Must be published in a local newspaper
  > - The publication must not be more than 3 months old from the date of application
  > - The original copy of this publication is a mandatory document
  > 
  > The application process requires this document as part of the 8 mandatory documents needed for the name change notification. The fee for this service is ₹30, which can be paid either online or at a Sewa Setu Kendra.
  > 
  > For the actual form format, you would need to refer to the official document format available on the Sewa Setu portal, which specifies the exact layout and content requirements for Form-I publication.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       gazette advertisement form I format
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       gazette advertisement form I format
       ```
     * **Response**:
       ```json
       gazette advertisement form I format
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       gazette advertisement form I format
       ```
     * **Response**:
       ```json
       gazette advertisement form I format
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "gazette advertisement form I format",
         "recent_history": [
           {
             "role": "user",
             "content": "affidavit stamp paper fee for name change"
           },
           {
             "role": "assistant",
             "content": "The affidavit stamp paper fee for name change is ₹50. This fee must be paid on a non-judicial stamp paper. The stamp paper should not be more than three months old from the date of application. This is a mandatory document for the name change process.\n\nFor more details and online application, please visit:\n[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)"
           },
           {
             "role": "user",
             "content": "time limit for name change gazette"
           },
           {
             "role": "assistant",
             "content": "The time limit for the name change gazette process is 29 days. This is specified as the Service Level Agreement (SLA) for the Ordinary Gazette Notification for Name Change service. The process must be completed with
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the format for the gazette advertisement form?",
         "topic_summary": "The user is asking about the format for the gazette advertisement form, which is a different service from the previous query about witness requirements for the name change gazette process."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "What is the format for the gazette advertisement form?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "5",
         "service_id": "201"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Based on the service specifications for Ordinary Gazette Notification for Name Change (Service ID: 201), the required document format is Form-I, which must be published in a local newspaper.
       
       The key requirements for the gazette advertisement form are:
       - Must be in Form-I format
       - Must be published in a local newspaper
       - The publication must not be more than 3 months old from the date of application
       - The original copy of this publication is a mandatory document
       
       The application process requires this document as part of the 8 mandatory documents needed for the name change notification. The fee for this service is ₹30, which can be paid either online or at a Sewa Setu Kendra.
       
       For the actual form format, you would need to refer to the official document format available on the Sewa Setu portal, which specifies the exact layout and content requirements for Form-I publication.
       ```
---
| 39 | 6 | `what is the total cost for name change in cg?` | 5 | 36.19s | en | 201 | new_topic |

### Query 39 Details
* **Query**: `what is the total cost for name change in cg?`
* **Selected SNO**: 5
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `what is the total cost for name change in cg?`
* **Resolved Hindi Query**: `\u0939\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0`
* **Final Synthesized Response**:
  > The total cost for name change in CG is ₹30.0. This fee is applicable for both online and kiosk applications. The cost includes the mandatory SBI challan of ₹430 and the notarized affidavit of ₹50, but the total application fee is ₹30.0. Additional costs may include expenses for the newspaper advertisement and stamp paper.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       what is the total cost for name change in cg?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       what is the total cost for name change in cg?
       ```
     * **Response**:
       ```json
       what is the total cost for name change in cg?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       what is the total cost for name change in cg?
       ```
     * **Response**:
       ```json
       \u0939\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\u092a\u093e\u093f\u0928 \u0939\u0941\
       ... [TRUNCATED FOR BREVITY] ...
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "what is the total cost for name change in cg?",
         "recent_history": [
           {
             "role": "user",
             "content": "time limit for name change gazette"
           },
           {
             "role": "assistant",
             "content": "The time limit for the name change gazette process is 29 days. This is specified as the Service Level Agreement (SLA) for the Ordinary Gazette Notification for Name Change service. The process must be completed within this timeframe from the date of application.\n\nFor more details and online application, please visit:\n[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)"
           },
           {
             "role": "user",
             "content": "name change gazette notification witnesses need?"
           },
           {
             "role": "assistant",
             "content": "Name change gazette notification के लिए witness requirements ये हैं:\n\n- आपको दो गवाहों के नाम, हस्ताक्षर और पते के साथ एक मूल प्ररूप-दो में विलिख प्ररूप (विलिख शपथ पत्र) देना होगा।\n- इ
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What is the total cost for name change in CG?",
         "topic_summary": "The user is asking about the cost for the name change service, which was the most recent topic discussed in the conversation."
       }
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       The total cost for name change in CG is ₹30.0. This fee is applicable for both online and kiosk applications. The cost includes the mandatory SBI challan of ₹430 and the notarized affidavit of ₹50, but the total application fee is ₹30.0. Additional costs may include expenses for the newspaper advertisement and stamp paper.
       ```
---
| 40 | 7 | `shadi ke baad name change process` | 1 | 3.88s | hinglish | 201 | new_topic |

### Query 40 Details
* **Query**: `shadi ke baad name change process`
* **Selected SNO**: 1
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `shadi ke baad name change process`
* **Resolved Hindi Query**: `शादी के बाद नाम परिवर्तन की प्रक्रिया`
* **Final Synthesized Response**:
  > Haan, shadi ke baad name change karne ke liye aapko Ordinary Gazette Notification apply karna padega. Ye process 29 days mein complete hota hai.
  > 
  > **Fee Details:**
  > - Kiosk Fee: ₹30.0
  > - Online Fee: ₹30.0
  > 
  > **Required Documents:**
  > 1. SBI challan of ₹430/- (Mandatory)
  > 2. Notarized affidavit in Form-III on ₹50 stamp paper (Mandatory)
  > 3. Newspaper publication of name change notice (Mandatory)
  > 4. Deed form with 2 witnesses (Mandatory)
  > 5. Old name & new name verification document (Mandatory)
  > 6. Identity card of applicant (Mandatory)
  > 7. Identity card of witnesses (Mandatory)
  > 
  > **Application Process:**
  > Aap Sewa Setu portal par online apply kar sakte hain. Application form mein aapko applicant details, change type, aur documents upload karne honge.
  > 
  > **Important Points:**
  > - Newspaper notice 3 months se purana nahi hona chahiye
  > - Affidavit 3 months se purana nahi hona chahiye
  > - Sab documents original copies honi chahiye
  > 
  > Kya aapko is process ke kisi specific step ke baare mein aur jaankari chahiye?
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       shadi ke baad name change process
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       shadi ke baad name change process
       ```
     * **Response**:
       ```json
       शादी के बाद नाम परिवर्तन की प्रक्रिया
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       shadi ke baad name change process
       ```
     * **Response**:
       ```json
       shadi ke baad name change process
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "shadi ke baad name change process",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "shadi ke baad name change process",
         "topic_summary": ""
       }
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Haan, shadi ke baad name change karne ke liye aapko Ordinary Gazette Notification apply karna padega. Ye process 29 days mein complete hota hai.
       
       **Fee Details:**
       - Kiosk Fee: ₹30.0
       - Online Fee: ₹30.0
       
       **Required Documents:**
       1. SBI challan of ₹430/- (Mandatory)
       2. Notarized affidavit in Form-III on ₹50 stamp paper (Mandatory)
       3. Newspaper publication of name change notice (Mandatory)
       4. Deed form with 2 witnesses (Mandatory)
       5. Old name & new name verification document (Mandatory)
       6. Identity card of applicant (Mandatory)
       7. Identity card of witnesses (Mandatory)
       
       **Application Process:**
       Aap Sewa Setu portal par online apply kar sakte hain. Application form mein aapko applicant details, change type, aur documents upload karne honge.
       
       **Important Points:**
       - Newspaper notice 3 months se purana nahi hona chahiye
       - Affidavit 3 months se purana nahi hona chahiye
       - Sab documents original copies honi chahiye
       
       Kya aapko is process ke kisi specific step ke baare mein aur jaankari chahiye?
       ```
---
| 41 | 7 | `caste certificate CG online link` | 1 | 5.58s | hinglish | 4 | new_topic |

### Query 41 Details
* **Query**: `caste certificate CG online link`
* **Selected SNO**: 1
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `caste certificate cg online link`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र CG ऑनलाइन लिंक`
* **Final Synthesized Response**:
  > हाँ, आप CG में ऑनलाइन caste certificate के लिए यहाँ से apply कर सकते हैं:
  > 
  > **Official Link:** https://sewasetu.cgstate.gov.in/home?lang=hi
  > 
  > यहाँ पर जाकर आप अपना application complete कर सकते हैं। आपको सभी required documents upload करने होंगे और fee भी pay करनी होगी।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate CG online link
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate CG online link
       ```
     * **Response**:
       ```json
       caste certificate cg online link
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate CG online link
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र CG ऑनलाइन लिंक
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate CG online link",
         "recent_history": [
           {
             "role": "user",
             "content": "shadi ke baad name change process"
           },
           {
             "role": "assistant",
             "content": "Haan, shadi ke baad name change karne ke liye aapko Ordinary Gazette Notification apply karna padega. Ye process 29 days mein complete hota hai.\n\n**Fee Details:**\n- Kiosk Fee: ₹30.0\n- Online Fee: ₹30.0\n\n**Required Documents:**\n1. SBI challan of ₹430/- (Mandatory)\n2. Notarized affidavit in Form-III on ₹50 stamp paper (Mandatory)\n3. Newspaper publication of name change notice (Mandatory)\n4. Deed form with 2 witnesses (Mandatory)\n5. Old name & new name verification document (Mandatory)\n6. Identity card of applicant (Mandatory)\n7. Identity card of witnesses (Mandatory)\n\n**Application Process:**\nAap Sewa Setu portal par online apply kar sakte hain. Application form mein aapko applicant details, change type, aur documents upload karne honge.\n\n**Important Points:**\n- 
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "caste certificate CG online link",
         "topic_summary": "User is asking for the online link to obtain a caste certificate in Chhattisgarh."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "caste certificate CG online link",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "2",
         "service_id": "4"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       हाँ, आप CG में ऑनलाइन caste certificate के लिए यहाँ से apply कर सकते हैं:
       
       **Official Link:** https://sewasetu.cgstate.gov.in/home?lang=hi
       
       यहाँ पर जाकर आप अपना application complete कर सकते हैं। आपको सभी required documents upload करने होंगे और fee भी pay करनी होगी।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nहाँ, आप CG में ऑनलाइन caste certificate के लिए यहाँ से apply कर सकते हैं:\n\n**Official Link:** https://sewasetu.cgstate.gov.in/home?lang=hi\n\nयहाँ पर जाकर आप अपना application complete कर सकते हैं। आपको सभी required documents upload करने होंगे और fee भी pay करनी होगी।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       हाँ, आप CG में ऑनलाइन caste certificate के लिए यहाँ से apply कर सकते हैं:
       
       **Official Link:** https://sewasetu.cgstate.gov.in/home?lang=hi
       
       यहाँ पर जाकर आप अपना application complete कर सकते हैं। आपको सभी required documents upload करने होंगे और fee भी pay करनी होगी।
       ```
---
| 42 | 7 | `raipur municipal corporation office location for marriage` | 1 | 4.40s | hinglish | 3 | new_topic |

### Query 42 Details
* **Query**: `raipur municipal corporation office location for marriage`
* **Selected SNO**: 1
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the location of the Raipur Municipal Corporation office for marriage?`
* **Resolved Hindi Query**: `राipur नगर निगम कार्यालय विवाह के लिए स्थान`
* **Final Synthesized Response**:
  > Raipur Municipal Corporation office के लिए, आपको अपने स्थानीय वार्ड के नगर निगम कार्यालय में जाना होगा। यह कार्यालय आपके क्षेत्र में विवाह पंजीकरण के लिए अधिकृत है। आप अपने क्षेत्र के नगर निगम कार्यालय के पते की जानकारी स्थानीय नगर निगम कार्यालय से या छत्तीसगढ़ ई-डिस्ट्रिक्ट पोर्टल पर प्राप्त कर सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       raipur municipal corporation office location for marriage
       ```
     * **Response**:
       ```json
       What is the location of the Raipur Municipal Corporation office for marriage?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       raipur municipal corporation office location for marriage
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       raipur municipal corporation office location for marriage
       ```
     * **Response**:
       ```json
       राipur नगर निगम कार्यालय विवाह के लिए स्थान
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "raipur municipal corporation office location for marriage",
         "recent_history": [
           {
             "role": "user",
             "content": "shadi ke baad name change process"
           },
           {
             "role": "assistant",
             "content": "Haan, shadi ke baad name change karne ke liye aapko Ordinary Gazette Notification apply karna padega. Ye process 29 days mein complete hota hai.\n\n**Fee Details:**\n- Kiosk Fee: ₹30.0\n- Online Fee: ₹30.0\n\n**Required Documents:**\n1. SBI challan of ₹430/- (Mandatory)\n2. Notarized affidavit in Form-III on ₹50 stamp paper (Mandatory)\n3. Newspaper publication of name change notice (Mandatory)\n4. Deed form with 2 witnesses (Mandatory)\n5. Old name & new name verification document (Mandatory)\n6. Identity card of applicant (Mandatory)\n7. Identity card of witnesses (Mandatory)\n\n**Application Process:**\nAap Sewa Setu portal par online apply kar sakte hain. Application form mein aapko applicant details, change type, aur documents upload karne honge.\n\n
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the location of the Raipur municipal corporation office for marriage?",
         "topic_summary": "Query about a different service (marriage) from the current topic (caste certificate)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "What is the location of the Raipur municipal corporation office for marriage?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "1",
         "service_id": "3"
       }
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Raipur Municipal Corporation office के लिए, आपको अपने स्थानीय वार्ड के नगर निगम कार्यालय में जाना होगा। यह कार्यालय आपके क्षेत्र में विवाह पंजीकरण के लिए अधिकृत है। आप अपने क्षेत्र के नगर निगम कार्यालय के पते की जानकारी स्थानीय नगर निगम कार्यालय से या छत्तीसगढ़ ई-डिस्ट्रिक्ट पोर्टल पर प्राप्त कर सकते हैं।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nRaipur Municipal Corporation office के लिए, आपको अपने स्थानीय वार्ड के नगर निगम कार्यालय में जाना होगा। यह कार्यालय आपके क्षेत्र में विवाह पंजीकरण के लिए अधिकृत है। आप अपने क्षेत्र के नगर निगम कार्यालय के पते की जानकारी स्थानीय नगर निगम कार्यालय से या छत्तीसगढ़ ई-डिस्ट्रिक्ट पोर्टल पर प्राप्त कर सकते हैं।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       Raipur Municipal Corporation office के लिए, आपको अपने स्थानीय वार्ड के नगर निगम कार्यालय में जाना होगा। यह कार्यालय आपके क्षेत्र में विवाह पंजीकरण के लिए अधिकृत है। आप अपने क्षेत्र के नगर निगम कार्यालय के पते की जानकारी स्थानीय नगर निगम कार्यालय से या छत्तीसगढ़ ई-डिस्ट्रिक्ट पोर्टल पर प्राप्त कर सकते हैं।
       ```
---
| 43 | 7 | `shadi praman patra documents list` | 1 | 2.58s | N/A | 3 | Interactive Checkpoint Intercept |

### Query 43 Details
* **Query**: `shadi praman patra documents list`
* **Selected SNO**: 1
* **Detected Language**: `N/A`
* **Classified Service ID**: `3`
* **Classified Intent**: `Interactive Checkpoint Intercept`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Marriage Registration & Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registration and certificate documents list
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registration and certificate documents list
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण और प्रमाणपत्र दस्तावेज सूची
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registration and certificate documents list
       ```
     * **Response**:
       ```json
       marriage registration and certificate documents list
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate documents list",
         "recent_history": [
           {
             "role": "user",
             "content": "shadi ke baad name change process"
           },
           {
             "role": "assistant",
             "content": "Haan, shadi ke baad name change karne ke liye aapko Ordinary Gazette Notification apply karna padega. Ye process 29 days mein complete hota hai.\n\n**Fee Details:**\n- Kiosk Fee: ₹30.0\n- Online Fee: ₹30.0\n\n**Required Documents:**\n1. SBI challan of ₹430/- (Mandatory)\n2. Notarized affidavit in Form-III on ₹50 stamp paper (Mandatory)\n3. Newspaper publication of name change notice (Mandatory)\n4. Deed form with 2 witnesses (Mandatory)\n5. Old name & new name verification document (Mandatory)\n6. Identity card of applicant (Mandatory)\n7. Identity card of witnesses (Mandatory)\n\n**Application Process:**\nAap Sewa Setu portal par online apply kar sakte hain. Application form mein aapko applicant details, change type, aur documents upload karne honge.\n\n**Imp
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "marriage registration and certificate documents list",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate documents list",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {
         "sno": "1",
         "service_id": "3"
       }
       ```
---
| 44 | 8 | `hola` | 4 | 1.54s | N/A | N/A | greeting |

### Query 44 Details
* **Query**: `hola`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `greeting`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       hola
       ```
     * **Response**:
       ```json
       नमस्कार
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       hola
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       hola
       ```
     * **Response**:
       ```json
       hola
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "hola",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "greeting",
         "resolved_query": "hola",
         "topic_summary": ""
       }
       ```
---
| 45 | 8 | `cg government website` | 4 | 1.54s | N/A | N/A | greeting |

### Query 45 Details
* **Query**: `cg government website`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `greeting`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       cg government website
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       cg government website
       ```
     * **Response**:
       ```json
       cg government website
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       cg government website
       ```
     * **Response**:
       ```json
       च.ग. सरकार की वेबसाइट
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "cg government website",
         "recent_history": [
           {
             "role": "user",
             "content": "hola"
           },
           {
             "role": "assistant",
             "content": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service."
           }
         ]
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "greeting",
         "resolved_query": "hola",
         "topic_summary": ""
       }
       ```
---
| 46 | 8 | `how to write code` | 4 | 1.54s | N/A | N/A | out_of_scope |

### Query 46 Details
* **Query**: `how to write code`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `out_of_scope`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       how to write code
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       how to write code
       ```
     * **Response**:
       ```json
       how to write code
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       how to write code
       ```
     * **Response**:
       ```json
       कोड कैसे लिखें?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "how to write code",
         "recent_history": [
           {
             "role": "user",
             "content": "hola"
           },
           {
             "role": "assistant",
             "content": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service."
           },
           {
             "role": "user",
             "content": "cg government website"
           },
           {
             "role": "assistant",
             "content": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service."
           }
         ]
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "out_of_scope",
         "resolved_query": "how to write code",
         "topic_summary": ""
       }
       ```
---
| 47 | 8 | `mujhe checklist do` | 4 | 1.52s | N/A | N/A | out_of_scope |

### Query 47 Details
* **Query**: `mujhe checklist do`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `out_of_scope`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Main sirf **Chhattisgarh sarkari sewaon** mein madad kar sakta/sakti hun jo Sewa Setu portal par uplabdh hain. Kripya kisi bhi seva ke documents, fees, eligibility ya application process ke baare mein poochein. 🙏

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       mujhe checklist do
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       mujhe checklist do
       ```
     * **Response**:
       ```json
       Checklist do.
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       mujhe checklist do
       ```
     * **Response**:
       ```json
       मुझे चेकलिस्ट दो
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "mujhe checklist do",
         "recent_history": [
           {
             "role": "user",
             "content": "hola"
           },
           {
             "role": "assistant",
             "content": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service."
           },
           {
             "role": "user",
             "content": "cg government website"
           },
           {
             "role": "assistant",
             "content": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service."
           },
           {
             "role": "user",
             "content": "how to write code"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any servic
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "out_of_scope",
         "resolved_query": "mujhe checklist do",
         "topic_summary": ""
       }
       ```
---
| 48 | 8 | `what is the fee?` | 4 | 4.81s | en | 7 | follow_up |

### Query 48 Details
* **Query**: `what is the fee?`
* **Selected SNO**: 4
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `follow_up`
* **Resolved English Query**: `What is the fee for the service?`
* **Resolved Hindi Query**: `सेवा के लिए शुल्क क्या है?`
* **Final Synthesized Response**:
  > Based on the official documents, the fee for the Domicile Certificate service is **₹30.0**.
  > 
  > This fee is applicable for both online and kiosk (Seva Setu Kendra) applications.
  > 
  > The fee includes the service charge and the cost of stamping for the address documents. Additional charges may apply for documents that need separate stamping.
  > 
  > The service is delivered within a **7-day** time limit as per the SLA.
  > 
  > For the application process, you can apply online through the Sewa Setu portal or at a Seva Setu Kendra.
  > 
  > You can find more details on the official Chhattisgarh Revenue and Disaster Management Department website.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       what is the fee?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       what is the fee?
       ```
     * **Response**:
       ```json
       शुल्क क्या है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       what is the fee?
       ```
     * **Response**:
       ```json
       what is the fee?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "what is the fee?",
         "recent_history": [
           {
             "role": "user",
             "content": "cg government website"
           },
           {
             "role": "assistant",
             "content": "Hello! 🙏 Welcome to SewaSetu AI Assistant. How can I help you with Chhattisgarh government services today? You can ask about documents, fees, eligibility, or application process for any service."
           },
           {
             "role": "user",
             "content": "how to write code"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏"
           },
           {
             "role": "user",
             "content": "mujhe checklist do"
           },
           {
             "role": "assistant",
             "content": "Main sirf **Chhattisgarh sarkari sewaon** mein madad kar sakta/sakti hun jo Sewa Setu portal par uplabdh hain. Kripya kisi bhi seva ke documents, fees, eligibility ya application
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "follow_up",
         "resolved_query": "What is the fee for the service?",
         "topic_summary": "The user is asking about the fee for the currently discussed service."
       }
       ```
  5. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       What is the fee for the service?
       ```
     * **Response**:
       ```json
       What is the fee for the service?
       ```
  6. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       What is the fee for the service?
       ```
     * **Response**:
       ```json
       सेवा के लिए शुल्क क्या है?
       ```
  7. **Function**: `detect_query_language`
     * **Input**:
       ```json
       What is the fee for the service?
       ```
     * **Response**:
       ```json
       en
       ```
  8. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RU
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Based on the official documents, the fee for the Domicile Certificate service is **₹30.0**.
       
       This fee is applicable for both online and kiosk (Seva Setu Kendra) applications.
       
       The fee includes the service charge and the cost of stamping for the address documents. Additional charges may apply for documents that need separate stamping.
       
       The service is delivered within a **7-day** time limit as per the SLA.
       
       For the application process, you can apply online through the Sewa Setu portal or at a Seva Setu Kendra.
       
       You can find more details on the official Chhattisgarh Revenue and Disaster Management Department website.
       ```
---
| 49 | 8 | `namaste` | 4 | 1.42s | N/A | N/A | greeting |

### Query 49 Details
* **Query**: `namaste`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `greeting`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Namaste! 🙏 SewaSetu AI Assistant mein aapka swagat hai. Chhattisgarh sarkari sewaon ke baare mein main aapki kaise madad kar sakta/sakti hoon? Aap kisi bhi seva ke documents, fees, eligibility ya application process ke baare mein pooch sakte hain.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       namaste
       ```
     * **Response**:
       ```json
       नमस्ते
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       namaste
       ```
     * **Response**:
       ```json
       hi
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       namaste
       ```
     * **Response**:
       ```json
       namaste
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "namaste",
         "recent_history": [
           {
             "role": "user",
             "content": "how to write code"
           },
           {
             "role": "assistant",
             "content": "I can only help with **Chhattisgarh government services** available on the Sewa Setu portal. Please ask about documents, fees, eligibility, or application process for any service. 🙏"
           },
           {
             "role": "user",
             "content": "mujhe checklist do"
           },
           {
             "role": "assistant",
             "content": "Main sirf **Chhattisgarh sarkari sewaon** mein madad kar sakta/sakti hun jo Sewa Setu portal par uplabdh hain. Kripya kisi bhi seva ke documents, fees, eligibility ya application process ke baare mein poochein. 🙏"
           },
           {
             "role": "user",
             "content": "what is the fee?"
           },
           {
             "role": "assistant",
             "content": "Based on the official documents, the fee for the Domicile Certificate service is **₹30.0**.\n\nThis fee is applicable for both online and kiosk (Seva Setu Kendra) application
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "greeting",
         "resolved_query": "namaste",
         "topic_summary": ""
       }
       ```
---
| 50 | 8 | `thanks a lot` | 4 | 1.32s | N/A | N/A | thanks |

### Query 50 Details
* **Query**: `thanks a lot`
* **Selected SNO**: 4
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `thanks`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > You're welcome! 🙏 Is there anything else I can help you with regarding Chhattisgarh government services?

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       thanks a lot
       ```
     * **Response**:
       ```json
       धन्यवाद बहुत
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       thanks a lot
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       thanks a lot
       ```
     * **Response**:
       ```json
       thanks a lot
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "thanks a lot",
         "recent_history": [
           {
             "role": "user",
             "content": "mujhe checklist do"
           },
           {
             "role": "assistant",
             "content": "Main sirf **Chhattisgarh sarkari sewaon** mein madad kar sakta/sakti hun jo Sewa Setu portal par uplabdh hain. Kripya kisi bhi seva ke documents, fees, eligibility ya application process ke baare mein poochein. 🙏"
           },
           {
             "role": "user",
             "content": "what is the fee?"
           },
           {
             "role": "assistant",
             "content": "Based on the official documents, the fee for the Domicile Certificate service is **₹30.0**.\n\nThis fee is applicable for both online and kiosk (Seva Setu Kendra) applications.\n\nThe fee includes the service charge and the cost of stamping for the address documents. Additional charges may apply for documents that need separate stamping.\n\nThe service is delivered within a **7-day** time limit as per the SLA.\n\nFor the application process, you can apply online through the Sew
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       {
         "intent": "thanks",
         "resolved_query": "thanks a lot",
         "topic_summary": ""
       }
       ```
---
