# SewaSetu Chatbot: 50 Confusing Queries Validation Results

This report captures validation runs of confusing queries that mix multiple government service concepts in a single request.

| ID | Confusing User Query | Expected Service ID | Mapped Service ID | Match Status | Intent | Latency |
|----|----------------------|---------------------|-------------------|--------------|--------|---------|
| 1 | `shadi ke baad naam change kaise karein?` | 201 | 201 | ✅ MATCH | new_topic | 4.57s |

### Query 1 Details
* **Query**: `shadi ke baad naam change kaise karein?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to change name after marriage?`
* **Resolved Hindi Query**: `शादी के बाद नाम परिवर्तन कैसे करें?`
* **Final Synthesized Response**:
  > Haan, shadi ke baad naam change karne ke liye aapko Ordinary Gazette Notification ke liye apply karna hoga. Ye process hai:
  > 
  > **Required Documents:**
  > 1. SBI ka ₹430 ka challan (mandatory)
  > 2. ₹50 ka notarized affidavit (Form-III) (mandatory)
  > 3. Local newspaper mein notice ka publication (mandatory)
  > 4. Do witnesses ka deed form (mandatory)
  > 5. Old name aur new name verification (mandatory)
  > 6. Sabhi documents ka reference (mandatory)
  > 
  > **Application Process:**
  > - Sewa Setu Kendra ya online portal par apply kar sakte hain
  > - Fee ₹30 hai (online ya kiosk dono mein)
  > - Time limit 29 days hai
  > 
  > **Important Points:**
  > - Sabhi documents original hone chahiye
  > - Newspaper notice 3 months se purana nahi hona chahiye
  > - Form-III affidavit 3 months se purana nahi hona chahiye
  > 
  > Kya aapko is process ke kisi specific step ke baare mein aur jaankari chahiye?
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       shadi ke baad naam change kaise karein?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       shadi ke baad naam change kaise karein?
       ```
     * **Response**:
       ```json
       How to change name after marriage?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       shadi ke baad naam change kaise karein?
       ```
     * **Response**:
       ```json
       शादी के बाद नाम परिवर्तन कैसे करें?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "shadi ke baad naam change kaise karein?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "shadi ke baad naam change kaise karein?",
         "topic_summary": "User is asking about the process for name change after marriage, which is a different service from any previous (non-existent) conversation. This is a new service query about a government process."
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
       Haan, shadi ke baad naam change karne ke liye aapko Ordinary Gazette Notification ke liye apply karna hoga. Ye process hai:
       
       **Required Documents:**
       1. SBI ka ₹430 ka challan (mandatory)
       2. ₹50 ka notarized affidavit (Form-III) (mandatory)
       3. Local newspaper mein notice ka publication (mandatory)
       4. Do witnesses ka deed form (mandatory)
       5. Old name aur new name verification (mandatory)
       6. Sabhi documents ka reference (mandatory)
       
       **Application Process:**
       - Sewa Setu Kendra ya online portal par apply kar sakte hain
       - Fee ₹30 hai (online ya kiosk dono mein)
       - Time limit 29 days hai
       
       **Important Points:**
       - Sabhi documents original hone chahiye
       - Newspaper notice 3 months se purana nahi hona chahiye
       - Form-III affidavit 3 months se purana nahi hona chahiye
       
       Kya aapko is process ke kisi specific step ke baare mein aur jaankari chahiye?
       ```
---
| 2 | `is domicile necessary for obc certificate?` | 5 | 5 | ✅ MATCH | new_topic | 5.45s |

### Query 2 Details
* **Query**: `is domicile necessary for obc certificate?`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is domicile necessary for OBC certificate?`
* **Resolved Hindi Query**: `क्या ओ बी सी प्रमाणपत्र के लिए निवास अनिवार्य है?`
* **Final Synthesized Response**:
  > नहीं, domicile certificate अनिवार्य नहीं है। आप बिना domicile certificate के भी OBC प्रमाण पत्र के लिए आवेदन कर सकते हैं।
  > 
  > OBC प्रमाण पत्र के लिए निवास प्रमाण के रूप में कई वैकल्पिक दस्तावेज हो सकते हैं, जैसे:
  > - वार्ड सदस्य या स्थानीय विधायक/सांसद का प्रमाण पत्र
  > - घर या भूमि का दस्तावेज
  > - राशन कार्ड
  > - बिजली का बिल
  > - जन्म प्रमाण पत्र
  > 
  > Domicile certificate को वैकल्पिक सहायक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is domicile necessary for obc certificate?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is domicile necessary for obc certificate?
       ```
     * **Response**:
       ```json
       Is domicile necessary for OBC certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is domicile necessary for obc certificate?
       ```
     * **Response**:
       ```json
       क्या ओ बी सी प्रमाणपत्र के लिए निवास अनिवार्य है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is domicile necessary for obc certificate?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is domicile necessary for OBC certificate?",
         "topic_summary": "Query about the requirements for an OBC certificate, specifically regarding the need for domicile."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "is domicile necessary for obc certificate?",
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
       नहीं, domicile certificate अनिवार्य नहीं है। आप बिना domicile certificate के भी OBC प्रमाण पत्र के लिए आवेदन कर सकते हैं।
       
       OBC प्रमाण पत्र के लिए निवास प्रमाण के रूप में कई वैकल्पिक दस्तावेज हो सकते हैं, जैसे:
       - वार्ड सदस्य या स्थानीय विधायक/सांसद का प्रमाण पत्र
       - घर या भूमि का दस्तावेज
       - राशन कार्ड
       - बिजली का बिल
       - जन्म प्रमाण पत्र
       
       Domicile certificate को वैकल्पिक सहायक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nनहीं, domicile certificate अनिवार्य नहीं है। आप बिना domicile certificate के भी OBC प्रमाण पत्र के लिए आवेदन कर सकते हैं।\n\nOBC प्रमाण पत्र के लिए निवास प्रमाण के रूप में कई वैकल्पिक दस्तावेज हो सकते हैं, जैसे:\n- वार्ड सदस्य या स्थानीय विधायक/सांसद का प्रमाण पत्र\n- घर या भूमि का दस्तावेज\n- राशन कार्ड\n- बिजली का बिल\n- जन्म प्रमाण पत्र\n\nDomicile certificate को वैकल्पिक सहायक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, domicile certificate अनिवार्य नहीं है। आप बिना domicile certificate के भी OBC प्रमाण पत्र के लिए आवेदन कर सकते हैं।
       
       OBC प्रमाण पत्र के लिए निवास प्रमाण के रूप में कई वैकल्पिक दस्तावेज हो सकते हैं, जैसे:
       - वार्ड सदस्य या स्थानीय विधायक/सांसद का प्रमाण पत्र
       - घर या भूमि का दस्तावेज
       - राशन कार्ड
       - बिजली का बिल
       - जन्म प्रमाण पत्र
       
       Domicile certificate को वैकल्पिक सहायक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य।
       ```
---
| 3 | `caste certificate ke liye niwas praman patra ki eligibility kya hai?` | 4 | 4 | ✅ MATCH | new_topic | 2.76s |

### Query 3 Details
* **Query**: `caste certificate ke liye niwas praman patra ki eligibility kya hai?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap SC/ST Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate ke liye domicile certificate ki eligibility kya hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate ke liye domicile certificate ki eligibility kya hai?
       ```
     * **Response**:
       ```json
       What is the eligibility for a domicile certificate for a caste certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate ke liye domicile certificate ki eligibility kya hai?
       ```
     * **Response**:
       ```json
       क्या जाति प्रमाण पत्र के लिए निवास प्रमाण पत्र की पात्रता है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate ke liye domicile certificate ki eligibility kya hai?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the eligibility criteria for a caste certificate using a domicile certificate?",
         "topic_summary": "Eligibility criteria for a caste certificate using a domicile certificate."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "caste certificate ke liye domicile certificate ki eligibility kya hai?",
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
---
| 4 | `obc certificate banane ke liye cg ka domicile hona zaroori hai?` | 5 | 5 | ✅ MATCH | new_topic | 7.97s |

### Query 4 Details
* **Query**: `obc certificate banane ke liye cg ka domicile hona zaroori hai?`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is it necessary to be a domicile of CG to get an OBC certificate?`
* **Resolved Hindi Query**: `क्या सी जी का डोमिसाइल होना ओ बी सी प्रमाण पत्र बनाने के लिए आवश्यक है?`
* **Final Synthesized Response**:
  > नहीं, CG का डोमिसाइल होना OBC सर्टिफिकेट के लिए अनिवार्य नहीं है।
  > 
  > OBC सर्टिफिकेट के लिए निवास का प्रमाण (रेसिडेंशियल प्रूफ) चाहिए, जो कई दस्तावेजों से पूरा किया जा सकता है। इनमें शामिल हैं:
  > 
  > - वार्ड मेंबर/MLA/MP का प्रमाण पत्र
  > - जमीन और घर का दस्तावेज
  > - राशन कार्ड
  > - बिजली का बिल
  > - जन्म प्रमाण पत्र
  > - Domicile सर्टिफिकेट (वैकल्पिक)
  > 
  > डोमिसाइल सर्टिफिकेट को भी एक वैकल्पिक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य। आप सेवा सेतु केंद्र या ऑनलाइन पोर्टल पर आवेदन कर सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       obc certificate banane ke liye cg ka domicile hona zaroori hai?
       ```
     * **Response**:
       ```json
       Is it necessary to be a domicile of CG to get an OBC certificate?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       obc certificate banane ke liye cg ka domicile hona zaroori hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       obc certificate banane ke liye cg ka domicile hona zaroori hai?
       ```
     * **Response**:
       ```json
       क्या सी जी का डोमिसाइल होना ओ बी सी प्रमाण पत्र बनाने के लिए आवश्यक है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "obc certificate banane ke liye cg ka domicile hona zaroori hai?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is domicile required in Chhattisgarh for an OBC certificate?",
         "topic_summary": "Query about the requirement of domicile for an OBC certificate in Chhattisgarh."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "obc certificate banane ke liye cg ka domicile hona zaroori hai?",
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
       नहीं, CG का डोमिसाइल होना OBC सर्टिफिकेट के लिए अनिवार्य नहीं है।
       
       OBC सर्टिफिकेट के लिए निवास का प्रमाण (रेसिडेंशियल प्रूफ) चाहिए, जो कई दस्तावेजों से पूरा किया जा सकता है। इनमें शामिल हैं:
       
       - वार्ड मेंबर/MLA/MP का प्रमाण पत्र
       - जमीन और घर का दस्तावेज
       - राशन कार्ड
       - बिजली का बिल
       - जन्म प्रमाण पत्र
       - Domicile सर्टिफिकेट (वैकल्पिक)
       
       डोमिसाइल सर्टिफिकेट को भी एक वैकल्पिक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य। आप सेवा सेतु केंद्र या ऑनलाइन पोर्टल पर आवेदन कर सकते हैं।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nनहीं, CG का डोमिसाइल होना OBC सर्टिफिकेट के लिए अनिवार्य नहीं है।\n\nOBC सर्टिफिकेट के लिए निवास का प्रमाण (रेसिडेंशियल प्रूफ) चाहिए, जो कई दस्तावेजों से पूरा किया जा सकता है। इनमें शामिल हैं:\n\n- वार्ड मेंबर/MLA/MP का प्रमाण पत्र\n- जमीन और घर का दस्तावेज\n- राशन कार्ड\n- बिजली का बिल\n- जन्म प्रमाण पत्र\n- Domicile सर्टिफिकेट (वैकल्पिक)\n\nडोमिसाइल सर्टिफिकेट को भी एक वैकल्पिक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य। आप सेवा सेतु केंद्र या ऑनलाइन पोर्टल पर आवेदन कर सकते हैं।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, CG का डोमिसाइल होना OBC सर्टिफिकेट के लिए अनिवार्य नहीं है।
       
       OBC सर्टिफिकेट के लिए निवास का प्रमाण (रेसिडेंशियल प्रूफ) चाहिए, जो कई दस्तावेजों से पूरा किया जा सकता है। इनमें शामिल हैं:
       
       - वार्ड मेंबर/MLA/MP का प्रमाण पत्र
       - जमीन और घर का दस्तावेज
       - राशन कार्ड
       - बिजली का बिल
       - जन्म प्रमाण पत्र
       - Domicile सर्टिफिकेट (वैकल्पिक)
       
       डोमिसाइल सर्टिफिकेट को भी एक वैकल्पिक दस्तावेज के रूप में सूचीबद्ध किया गया है, न कि अनिवार्य। आप सेवा सेतु केंद्र या ऑनलाइन पोर्टल पर आवेदन कर सकते हैं।
       ```
---
| 5 | `shadi certificate me name correction kaise karein?` | 3 | 201 | ❌ MISMATCH | new_topic | 3.60s |

### Query 5 Details
* **Query**: `shadi certificate me name correction kaise karein?`
* **Expected Service ID**: `3`
* **Classified Service ID**: `201`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to correct name in marriage registration and certificate?`
* **Resolved Hindi Query**: `विवाह पंजीकरण और प्रमाण पत्र में नाम सुधार कैसे करें?`
* **Final Synthesized Response**:
  > Namaste! Aapke sawal ka jawab deta hun.
  > 
  > Marriage registration ke baad name correction ke liye aapko ye process follow karna hoga:
  > 
  > **Name Correction Process:**
  > 1. Pehle se issued marriage certificate mein name change ke liye ordinary gazette notification apply karna hoga
  > 2. Iske liye SBI se ₹430 ka challan lena padega
  > 3. Notarized affidavit ₹50 ka stamp paper pe banana hoga
  > 4. Local newspaper mein notice publish karana hoga
  > 5. Do witnesses ke saath deed form fill karna hoga
  > 
  > **Important Points:**
  > - Time limit 29 days hai
  > - Fee ₹30 hai (online ya kiosk dono se)
  > - Sab documents original hone chahiye
  > - Old name aur new name verification document zaroori hai
  > 
  > Kya aapko is process ke kisi specific step ke baare mein aur jaankari chahiye?
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registration and certificate me name correction kaise karein?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registration and certificate me name correction kaise karein?
       ```
     * **Response**:
       ```json
       How to correct name in marriage registration and certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registration and certificate me name correction kaise karein?
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण और प्रमाण पत्र में नाम सुधार कैसे करें?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate me name correction kaise karein?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the process for marriage registration and name correction in a certificate?",
         "topic_summary": "User is asking about two distinct government services: marriage registration and name correction in a certificate."
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
       Namaste! Aapke sawal ka jawab deta hun.
       
       Marriage registration ke baad name correction ke liye aapko ye process follow karna hoga:
       
       **Name Correction Process:**
       1. Pehle se issued marriage certificate mein name change ke liye ordinary gazette notification apply karna hoga
       2. Iske liye SBI se ₹430 ka challan lena padega
       3. Notarized affidavit ₹50 ka stamp paper pe banana hoga
       4. Local newspaper mein notice publish karana hoga
       5. Do witnesses ke saath deed form fill karna hoga
       
       **Important Points:**
       - Time limit 29 days hai
       - Fee ₹30 hai (online ya kiosk dono se)
       - Sab documents original hone chahiye
       - Old name aur new name verification document zaroori hai
       
       Kya aapko is process ke kisi specific step ke baare mein aur jaankari chahiye?
       ```
---
| 6 | `st certificate ke documents me domicile praman patra lagta hai kya?` | 4 | 4 | ✅ MATCH | new_topic | 2.42s |

### Query 6 Details
* **Query**: `st certificate ke documents me domicile praman patra lagta hai kya?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap SC/ST Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       st certificate ke documents me domicile certificate lagta hai kya?
       ```
     * **Response**:
       ```json
       क्या domicile certificate lagta hai st certificate ke documents me?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       st certificate ke documents me domicile certificate lagta hai kya?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       st certificate ke documents me domicile certificate lagta hai kya?
       ```
     * **Response**:
       ```json
       Is the domicile certificate included in the documents for the ST certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "st certificate ke documents me domicile certificate lagta hai kya?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What are the documents required for a ST certificate, including the domicile certificate?",
         "topic_summary": "User is asking about the documents for an ST certificate, which is a different service from the general introduction or a follow-up to a previous service. This is a new service query."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "st certificate ke documents me domicile certificate lagta hai kya?",
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
---
| 7 | `niwas praman patra ke liye caste certificate chahiye?` | 7 | 7 | ✅ MATCH | new_topic | 5.07s |

### Query 7 Details
* **Query**: `niwas praman patra ke liye caste certificate chahiye?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Do you need a caste certificate for a domicile certificate?`
* **Resolved Hindi Query**: `क्या आपको डोमिसाइल प्रमाण पत्र के लिए जाति प्रमाण पत्र की आवश्यकता है?`
* **Final Synthesized Response**:
  > नहीं, domicile certificate के लिए caste certificate की जरूरत नहीं है। आप domicile certificate के लिए सीधे apply कर सकते हैं।
  > 
  > Domicile certificate के लिए जो documents चाहिए, उनमें affidavit, proof of 15 years stay, और educational certificate शामिल हैं। Caste certificate एक separate document है और domicile certificate के लिए mandatory नहीं है।
  > 
  > अगर आप domicile certificate के लिए apply करना चाहते हैं, तो आप Sewa Setu portal पर जाकर apply कर सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       domicile certificate ke liye caste certificate chahiye?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       domicile certificate ke liye caste certificate chahiye?
       ```
     * **Response**:
       ```json
       Do you need a caste certificate for a domicile certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       domicile certificate ke liye caste certificate chahiye?
       ```
     * **Response**:
       ```json
       क्या आपको डोमिसाइल प्रमाण पत्र के लिए जाति प्रमाण पत्र की आवश्यकता है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "domicile certificate ke liye caste certificate chahiye?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "domicile certificate ke liye caste certificate chahiye?",
         "topic_summary": "User is asking about the relationship between two different government services: domicile certificate and caste certificate."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "domicile certificate ke liye caste certificate chahiye?",
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
       नहीं, domicile certificate के लिए caste certificate की जरूरत नहीं है। आप domicile certificate के लिए सीधे apply कर सकते हैं।
       
       Domicile certificate के लिए जो documents चाहिए, उनमें affidavit, proof of 15 years stay, और educational certificate शामिल हैं। Caste certificate एक separate document है और domicile certificate के लिए mandatory नहीं है।
       
       अगर आप domicile certificate के लिए apply करना चाहते हैं, तो आप Sewa Setu portal पर जाकर apply कर सकते हैं।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nनहीं, domicile certificate के लिए caste certificate की जरूरत नहीं है। आप domicile certificate के लिए सीधे apply कर सकते हैं।\n\nDomicile certificate के लिए जो documents चाहिए, उनमें affidavit, proof of 15 years stay, और educational certificate शामिल हैं। Caste certificate एक separate document है और domicile certificate के लिए mandatory नहीं है।\n\nअगर आप domicile certificate के लिए apply करना चाहते हैं, तो आप Sewa Setu portal पर जाकर apply कर सकते हैं।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, domicile certificate के लिए caste certificate की जरूरत नहीं है। आप domicile certificate के लिए सीधे apply कर सकते हैं।
       
       Domicile certificate के लिए जो documents चाहिए, उनमें affidavit, proof of 15 years stay, और educational certificate शामिल हैं। Caste certificate एक separate document है और domicile certificate के लिए mandatory नहीं है।
       
       अगर आप domicile certificate के लिए apply करना चाहते हैं, तो आप Sewa Setu portal पर जाकर apply कर सकते हैं।
       ```
---
| 8 | `gazette notification name change ke liye marriage certificate mandatory hai?` | 201 | 201 | ✅ MATCH | new_topic | 4.07s |

### Query 8 Details
* **Query**: `gazette notification name change ke liye marriage certificate mandatory hai?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is it mandatory to have a marriage registration and certificate for a gazette notification name change?`
* **Resolved Hindi Query**: `क्या विवाह पंजीकरण और प्रमाण पत्र नाम परिवर्तन के लिए अनिवार्य है?`
* **Final Synthesized Response**:
  > नहीं, marriage registration और certificate इस service के लिए mandatory नहीं है। आप नाम परिवर्तन के लिए ordinary gazette notification apply कर सकते हैं। इसके लिए जो documents चाहिए, जैसे SBI challan, notarized affidavit, और newspaper notice, वे ही sufficient हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       gazette notification name change ke liye marriage registration and certificate mandatory hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       gazette notification name change ke liye marriage registration and certificate mandatory hai?
       ```
     * **Response**:
       ```json
       क्या विवाह पंजीकरण और प्रमाण पत्र नाम परिवर्तन के लिए अनिवार्य है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       gazette notification name change ke liye marriage registration and certificate mandatory hai?
       ```
     * **Response**:
       ```json
       Is it mandatory to have a marriage registration and certificate for a gazette notification name change?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "gazette notification name change ke liye marriage registration and certificate mandatory hai?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is a marriage registration and certificate mandatory for a gazette notification name change?",
         "topic_summary": "User is asking about the requirements for a name change via gazette notification, specifically if a marriage registration and certificate are mandatory."
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
       नहीं, marriage registration और certificate इस service के लिए mandatory नहीं है। आप नाम परिवर्तन के लिए ordinary gazette notification apply कर सकते हैं। इसके लिए जो documents चाहिए, जैसे SBI challan, notarized affidavit, और newspaper notice, वे ही sufficient हैं।
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nनहीं, marriage registration और certificate इस service के लिए mandatory नहीं है। आप नाम परिवर्तन के लिए ordinary gazette notification apply कर सकते हैं। इसके लिए जो documents चाहिए, जैसे SBI challan, notarized affidavit, और newspaper notice, वे ही sufficient हैं।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, marriage registration और certificate इस service के लिए mandatory नहीं है। आप नाम परिवर्तन के लिए ordinary gazette notification apply कर सकते हैं। इसके लिए जो documents चाहिए, जैसे SBI challan, notarized affidavit, और newspaper notice, वे ही sufficient हैं।
       ```
---
| 9 | `caste validation rules in cg domicile certificate` | 7 | 7 | ✅ MATCH | new_topic | 2.21s |

### Query 9 Details
* **Query**: `caste validation rules in cg domicile certificate`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Domicile Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste validation rules in cg domicile certificate
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste validation rules in cg domicile certificate
       ```
     * **Response**:
       ```json
       जाति सत्यापन नियम cg निवास प्रमाण पत्र में
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste validation rules in cg domicile certificate
       ```
     * **Response**:
       ```json
       caste validation rules in cg domicile certificate
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste validation rules in cg domicile certificate",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "caste validation rules in cg domicile certificate",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "caste validation rules in cg domicile certificate",
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
| 10 | `can a married woman apply for domicile certificate using father's address?` | 7 | 7 | ✅ MATCH | new_topic | 4.76s |

### Query 10 Details
* **Query**: `can a married woman apply for domicile certificate using father's address?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `can a married woman apply for domicile certificate using father's address?`
* **Resolved Hindi Query**: `क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके निवास प्रमाण पत्र के लिए आवेदन कर सकती है?`
* **Final Synthesized Response**:
  > No, a married woman cannot apply for a domicile certificate using her father's address. The application requires the applicant's own place of birth and residence details. The service is specifically for establishing domicile based on the individual's own history, not through family members. You must provide your own birth certificate and proof of residence to meet the mandatory requirements.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       can a married woman apply for domicile certificate using father's address?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       can a married woman apply for domicile certificate using father's address?
       ```
     * **Response**:
       ```json
       can a married woman apply for domicile certificate using father's address?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       can a married woman apply for domicile certificate using father's address?
       ```
     * **Response**:
       ```json
       क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके निवास प्रमाण पत्र के लिए आवेदन कर सकती है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "can a married woman apply for domicile certificate using father's address?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Can a married woman apply for a domicile certificate using her father's address?",
         "topic_summary": "Query about applying for a domicile certificate, a specific government service. The user is asking about the eligibility criteria and process for a particular service, which is a government service query. This is a new topic as it's a different service than the one in history (which is none)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "can a married woman apply for domicile certificate using father's address?",
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
       No, a married woman cannot apply for a domicile certificate using her father's address. The application requires the applicant's own place of birth and residence details. The service is specifically for establishing domicile based on the individual's own history, not through family members. You must provide your own birth certificate and proof of residence to meet the mandatory requirements.
       ```
---
| 11 | `obc certificate and sc st certificate difference in fees` | 5 | None | ❌ MISMATCH | new_topic | 2.75s |

### Query 11 Details
* **Query**: `obc certificate and sc st certificate difference in fees`
* **Expected Service ID**: `5`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the difference in fees between an OBC certificate and an SC/ST certificate?`
* **Resolved Hindi Query**: `ओ बी सी प्रमाणपत्र और एस सी एस टी प्रमाणपत्र शुल्क में अंतर`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       obc certificate and sc st certificate difference in fees
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       obc certificate and sc st certificate difference in fees
       ```
     * **Response**:
       ```json
       What is the difference in fees between an OBC certificate and an SC/ST certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       obc certificate and sc st certificate difference in fees
       ```
     * **Response**:
       ```json
       ओ बी सी प्रमाणपत्र और एस सी एस टी प्रमाणपत्र शुल्क में अंतर
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "obc certificate and sc st certificate difference in fees",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the difference in fees between OBC and SC/ST certificates?",
         "topic_summary": "Comparison of fees for two different government certificates."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "obc certificate and sc st certificate difference in fees",
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
---
| 12 | `marriage certificate apply online using caste certificate details` | 3 | 3 | ✅ MATCH | new_topic | 3.81s |

### Query 12 Details
* **Query**: `marriage certificate apply online using caste certificate details`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `marriage registration and certificate apply online using caste certificate details`
* **Resolved Hindi Query**: `विवाह पंजीकरण और प्रमाणपत्र ऑनलाइन आवेदन करें, जाति प्रमाणपत्र विवरण का उपयोग करके।`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registration and certificate apply online using caste certificate details
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registration and certificate apply online using caste certificate details
       ```
     * **Response**:
       ```json
       marriage registration and certificate apply online using caste certificate details
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registration and certificate apply online using caste certificate details
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण और प्रमाणपत्र ऑनलाइन आवेदन करें, जाति प्रमाणपत्र विवरण का उपयोग करके।
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate apply online using caste certificate details",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the process and documents required for marriage registration using caste certificate details?",
         "topic_summary": "User is inquiring about the process and documents for marriage registration, which is a new service topic not previously discussed."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate apply online using caste certificate details",
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
       I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.
       ```
---
| 13 | `obc praman patra me domicile praman patra rules` | 5 | 5 | ✅ MATCH | new_topic | 2.67s |

### Query 13 Details
* **Query**: `obc praman patra me domicile praman patra rules`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap OBC Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       obc certificate me domicile certificate rules
       ```
     * **Response**:
       ```json
       What are the rules for an OBC certificate and a domicile certificate?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       obc certificate me domicile certificate rules
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       obc certificate me domicile certificate rules
       ```
     * **Response**:
       ```json
       ओ बी सी प्रमाणपत्र में डोमिसाइल प्रमाणपत्र नियम
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "obc certificate me domicile certificate rules",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What are the domicile certificate rules for an OBC certificate?",
         "topic_summary": "Query about rules for obtaining an OBC certificate with domicile proof."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "obc certificate me domicile certificate rules",
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
---
| 14 | `shadi praman patra ke sath name change ka affidavit lagega?` | 3 | 201 | ❌ MISMATCH | new_topic | 3.44s |

### Query 14 Details
* **Query**: `shadi praman patra ke sath name change ka affidavit lagega?`
* **Expected Service ID**: `3`
* **Classified Service ID**: `201`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is it required to have an affidavit for name change along with marriage registration and certificate?`
* **Resolved Hindi Query**: `विवाह पंजीकरण और प्रमाणपत्र के साथ नाम परिवर्तन का शपथ पत्र लगेगा?`
* **Final Synthesized Response**:
  > Haan, name change ke liye affidavit zaroori hai. Lekin marriage registration aur certificate ke sath alag-alag documents chahiye hote hain.
  > 
  > Name change ke liye ye documents chahiye:
  > - SBI ka challan (₹430)
  > - Notarized affidavit (₹50 stamp paper)
  > - Newspaper mein notice
  > - 2 witnesses ka deed form
  > - Old aur new name ka verification document
  > - Government ID card
  > 
  > Agar aapka marriage registration hua hai to uska certificate bhi chahiye hoga. Certificate ke liye alag se affidavit nahi lagta, bas original certificate aur application form bharna hota hai.
  > 
  > Kya aap batayenge ki aapka name change kiske liye karna hai? Jaise marriage ke baad ya kisi aur reason se?
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registration and certificate ke sath name change ka affidavit lagega?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registration and certificate ke sath name change ka affidavit lagega?
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण और प्रमाणपत्र के साथ नाम परिवर्तन का शपथ पत्र लगेगा?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registration and certificate ke sath name change ka affidavit lagega?
       ```
     * **Response**:
       ```json
       Is it required to have an affidavit for name change along with marriage registration and certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate ke sath name change ka affidavit lagega?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the process and required documents for marriage registration and name change affidavit?",
         "topic_summary": "User is inquiring about two different government services: marriage registration and name change affidavit. This is a new topic as it involves a different service than any previous (non-existent) conversation."
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
       Haan, name change ke liye affidavit zaroori hai. Lekin marriage registration aur certificate ke sath alag-alag documents chahiye hote hain.
       
       Name change ke liye ye documents chahiye:
       - SBI ka challan (₹430)
       - Notarized affidavit (₹50 stamp paper)
       - Newspaper mein notice
       - 2 witnesses ka deed form
       - Old aur new name ka verification document
       - Government ID card
       
       Agar aapka marriage registration hua hai to uska certificate bhi chahiye hoga. Certificate ke liye alag se affidavit nahi lagta, bas original certificate aur application form bharna hota hai.
       
       Kya aap batayenge ki aapka name change kiske liye karna hai? Jaise marriage ke baad ya kisi aur reason se?
       ```
---
| 15 | `niwas praman patra cg fees vs caste certificate fees` | 7 | None | ❌ MISMATCH | new_topic | 2.36s |

### Query 15 Details
* **Query**: `niwas praman patra cg fees vs caste certificate fees`
* **Expected Service ID**: `7`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `domicile certificate cg fees vs caste certificate fees`
* **Resolved Hindi Query**: `Domicile certificate CG fees vs caste certificate fees`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Jaankari uplabhd nahi hai.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       domicile certificate cg fees vs caste certificate fees
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       domicile certificate cg fees vs caste certificate fees
       ```
     * **Response**:
       ```json
       Domicile certificate CG fees vs caste certificate fees
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       domicile certificate cg fees vs caste certificate fees
       ```
     * **Response**:
       ```json
       domicile certificate cg fees vs caste certificate fees
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "domicile certificate cg fees vs caste certificate fees",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "domicile certificate cg fees vs caste certificate fees",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "domicile certificate cg fees vs caste certificate fees",
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
---
| 16 | `gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper` | 201 | 201 | ✅ MATCH | new_topic | 5.12s |

### Query 16 Details
* **Query**: `gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper`
* **Resolved Hindi Query**: `गैजेट प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र स्टाम्प पेपर`
* **Final Synthesized Response**:
  > Service ID 201 के लिए gazette publication और marriage affidavit stamp paper के बीच अंतर:
  > 
  > **Gazette Publication के लिए:**
  > - Non-judicial stamp paper ₹50 का notarized affidavit (Form-III)
  > - Local newspaper में name change की notice (Form-I)
  > - 3 witnesses के साथ deed form (Form-II)
  > - Old name और new name verification document
  > 
  > **Marriage Affidavit के लिए:**
  > - Marriage affidavit (Form-III)
  > - Marriage certificate या proof
  > - Identity proof (Aadhaar/PAN)
  > 
  > दोनों के लिए ₹30 का fee है (online या kiosk से)। Gazette process में newspaper publication और deed registration शामिल है, जबकि marriage affidavit में सिर्फ affidavit और marriage proof की जरूरत होती है।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper
       ```
     * **Response**:
       ```json
       गैजेट प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र स्टाम्प पेपर
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper
       ```
     * **Response**:
       ```json
       gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the difference between gazette publication and marriage affidavit stamp paper?",
         "topic_summary": "Discussion about stamp paper types for name change and marriage."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "gazette publication name change advertisement stamp paper vs marriage affidavit stamp paper",
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
       Service ID 201 के लिए gazette publication और marriage affidavit stamp paper के बीच अंतर:
       
       **Gazette Publication के लिए:**
       - Non-judicial stamp paper ₹50 का notarized affidavit (Form-III)
       - Local newspaper में name change की notice (Form-I)
       - 3 witnesses के साथ deed form (Form-II)
       - Old name और new name verification document
       
       **Marriage Affidavit के लिए:**
       - Marriage affidavit (Form-III)
       - Marriage certificate या proof
       - Identity proof (Aadhaar/PAN)
       
       दोनों के लिए ₹30 का fee है (online या kiosk से)। Gazette process में newspaper publication और deed registration शामिल है, जबकि marriage affidavit में सिर्फ affidavit और marriage proof की जरूरत होती है।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nService ID 201 के लिए gazette publication और marriage affidavit stamp paper के बीच अंतर:\n\n**Gazette Publication के लिए:**\n- Non-judicial stamp paper ₹50 का notarized affidavit (Form-III)\n- Local newspaper में name change की notice (Form-I)\n- 3 witnesses के साथ deed form (Form-II)\n- Old name और new name verification document\n\n**Marriage Affidavit के लिए:**\n- Marriage affidavit (Form-III)\n- Marriage certificate या proof\n- Identity proof (Aadhaar/PAN)\n\nदोनों के लिए ₹30 का fee है (online या kiosk से)। Gazette process में newspaper publication और deed registration शामिल है, जबकि marriag
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Service ID 201 के लिए gazette publication और marriage affidavit stamp paper के बीच अंतर:
       
       **Gazette Publication के लिए:**
       - Non-judicial stamp paper ₹50 का notarized affidavit (Form-III)
       - Local newspaper में name change की notice (Form-I)
       - 3 witnesses के साथ deed form (Form-II)
       - Old name और new name verification document
       
       **Marriage Affidavit के लिए:**
       - Marriage affidavit (Form-III)
       - Marriage certificate या proof
       - Identity proof (Aadhaar/PAN)
       
       दोनों के लिए ₹30 का fee है (online या kiosk से)। Gazette process में newspaper publication और deed registration शामिल है, जबकि marriage affidavit में सिर्फ affidavit और marriage proof की जरूरत होती है।
       ```
---
| 17 | `do we need sc certificate for obc scholarship application?` | 5 | None | ❌ MISMATCH | new_topic | 2.27s |

### Query 17 Details
* **Query**: `do we need sc certificate for obc scholarship application?`
* **Expected Service ID**: `5`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `do we need sc certificate for obc scholarship application?`
* **Resolved Hindi Query**: `क्या हमें ओ बी सी स्कॉलरशिप आवेदन के लिए एस सी प्रमाणपत्र की आवश्यकता है?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       do we need sc certificate for obc scholarship application?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       do we need sc certificate for obc scholarship application?
       ```
     * **Response**:
       ```json
       क्या हमें ओ बी सी स्कॉलरशिप आवेदन के लिए एस सी प्रमाणपत्र की आवश्यकता है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       do we need sc certificate for obc scholarship application?
       ```
     * **Response**:
       ```json
       do we need sc certificate for obc scholarship application?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "do we need sc certificate for obc scholarship application?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the requirement of SC certificate for OBC scholarship application?",
         "topic_summary": "OBC scholarship application requirements"
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "do we need sc certificate for obc scholarship application?",
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
---
| 18 | `is digital signature of sdo for st certificate same as domicile?` | 4 | None | ❌ MISMATCH | new_topic | 3.21s |

### Query 18 Details
* **Query**: `is digital signature of sdo for st certificate same as domicile?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is the digital signature of SDO for ST certificate the same as domicile?`
* **Resolved Hindi Query**: `क्या डिजिटल हस्ताक्षर sdo के st प्रमाणपत्र के लिए domicile के समान है?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Jaankari uplabhd nahi hai.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is digital signature of sdo for st certificate same as domicile?
       ```
     * **Response**:
       ```json
       Is the digital signature of SDO for ST certificate the same as domicile?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is digital signature of sdo for st certificate same as domicile?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is digital signature of sdo for st certificate same as domicile?
       ```
     * **Response**:
       ```json
       क्या डिजिटल हस्ताक्षर sdo के st प्रमाणपत्र के लिए domicile के समान है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is digital signature of sdo for st certificate same as domicile?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is the digital signature of an SDO for a ST certificate the same as a domicile certificate?",
         "topic_summary": "Query about the validity of a digital signature for an ST certificate compared to a domicile certificate."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "is digital signature of sdo for st certificate same as domicile?",
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
---
| 19 | `obc non-creamy layer certificate me domicile conditions` | 5 | 5 | ✅ MATCH | new_topic | 2.17s |

### Query 19 Details
* **Query**: `obc non-creamy layer certificate me domicile conditions`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap OBC Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       obc non-creamy layer certificate me domicile conditions
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       obc non-creamy layer certificate me domicile conditions
       ```
     * **Response**:
       ```json
       Obc non-creamy layer certificate me domicile conditions
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       obc non-creamy layer certificate me domicile conditions
       ```
     * **Response**:
       ```json
       obc non-creamy layer certificate me domicile conditions
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "obc non-creamy layer certificate me domicile conditions",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What are the domicile conditions for an OBC non-creamy layer certificate?",
         "topic_summary": "Query about domicile conditions for a specific government service (OBC non-creamy layer certificate)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "obc non-creamy layer certificate me domicile conditions",
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
---
| 20 | `naam badalne ke baad marriage certificate update kaise hoga?` | 201 | 201 | ✅ MATCH | new_topic | 6.16s |

### Query 20 Details
* **Query**: `naam badalne ke baad marriage certificate update kaise hoga?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How will marriage registration and certificate update happen after changing the name?`
* **Resolved Hindi Query**: `नाम बदलने के बाद विवाह पंजीकरण और प्रमाणपत्र अद्यतन कैसे होगा?`
* **Final Synthesized Response**:
  > Service ID 201 के तहत नाम परिवर्तन के बाद, शादी का रजिस्ट्रेशन और सर्टिफिकेट अपडेट करने के लिए ये स्टेप्स फॉलो करें:
  > 
  > 1. **Marriage Certificate Update**:
  >    - नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (Service ID 201) का इस्तेमाल करें
  >    - इसके लिए SBI से 430 रुपये का चालान, नोटराइज्ड शपथ पत्र (50 रुपये), और स्थानीय अखबार में विज्ञापन देना होगा
  >    - 29 दिन का समय लगता है
  > 
  > 2. **Sewa Setu Portal पर**:
  >    - https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं
  >    - "Where to Apply" में Sewa Setu Kendra या Online विकल्प चुनें
  >    - Fee 30 रुपये है (Online और Kiosk दोनों के लिए)
  > 
  > 3. **Required Documents**:
  >    - पुराना नाम और नया नाम सत्यापन
  >    - सभी ID कार्ड (आवेदक और गवाहों के)
  >    - फॉर्म-I (अखबार में विज्ञापन)
  >    - फॉर्म-II (शपथ पत्र)
  > 
  > 4. **Process**:
  >    - फॉर्म भरें और सभी दस्तावेज अपलोड करें
  >    - 29 दिन में अपडेटेड सर्टिफिकेट मिल जाएगा
  >    - अपडेटेड सर्टिफिकेट के लिए दोबारा आवेदन करना होगा
  > 
  > क्या आप किसी खास डॉक्यूमेंट के बारे में और जानकारी चाहते हैं?
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       naam badalne ke baad marriage registration and certificate update kaise hoga?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       naam badalne ke baad marriage registration and certificate update kaise hoga?
       ```
     * **Response**:
       ```json
       नाम बदलने के बाद विवाह पंजीकरण और प्रमाणपत्र अद्यतन कैसे होगा?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       naam badalne ke baad marriage registration and certificate update kaise hoga?
       ```
     * **Response**:
       ```json
       How will marriage registration and certificate update happen after changing the name?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "naam badalne ke baad marriage registration and certificate update kaise hoga?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "How to do marriage registration and certificate update after name change?",
         "topic_summary": "User is asking about the process for marriage registration and certificate update after a name change."
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
       Service ID 201 के तहत नाम परिवर्तन के बाद, शादी का रजिस्ट्रेशन और सर्टिफिकेट अपडेट करने के लिए ये स्टेप्स फॉलो करें:
       
       1. **Marriage Certificate Update**:
          - नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (Service ID 201) का इस्तेमाल करें
          - इसके लिए SBI से 430 रुपये का चालान, नोटराइज्ड शपथ पत्र (50 रुपये), और स्थानीय अखबार में विज्ञापन देना होगा
          - 29 दिन का समय लगता है
       
       2. **Sewa Setu Portal पर**:
          - https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं
          - "Where to Apply" में Sewa Setu Kendra या Online विकल्प चुनें
          - Fee 30 रुपये है (Online और Kiosk दोनों के लिए)
       
       3. **Required Documents**:
          - पुराना नाम और नया नाम सत्यापन
          - सभी ID कार्ड (आवेदक और गवाहों के)
          - फॉर्म-I (अखबार में विज्ञापन)
          - फॉर्म-II (शपथ पत्र)
       
       4. **Process**:
          - फॉर्म भरें और सभी दस्तावेज अपलोड करें
          - 29 दिन में अपडेटेड सर्टिफिकेट मिल जाएगा
          - अपडेटेड सर्टिफिकेट के लिए दोबारा आवेदन करना होगा
       
       क्या आप किसी खास डॉक्यूमेंट के बारे में और जानकारी चाहते हैं?
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nService ID 201 के तहत नाम परिवर्तन के बाद, शादी का रजिस्ट्रेशन और सर्टिफिकेट अपडेट करने के लिए ये स्टेप्स फॉलो करें:\n\n1. **Marriage Certificate Update**:\n   - नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (Service ID 201) का इस्तेमाल करें\n   - इसके लिए SBI से 430 रुपये का चालान, नोटराइज्ड शपथ पत्र (50 रुपये), और स्थानीय अखबार में विज्ञापन देना होगा\n   - 29 दिन का समय लगता है\n\n2. **Sewa Setu Portal पर**:\n   - https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं\n   - \"Where to Apply\" में Sewa Setu Kendra या Online विकल्प चुनें\n   - Fee 30 रुपये है (Online और Kiosk दोनों के लिए)\n\n3. **
       ... [TRUNCATED FOR BREVITY] ...
       ```
     * **Response**:
       ```json
       Service ID 201 के तहत नाम परिवर्तन के बाद, शादी का रजिस्ट्रेशन और सर्टिफिकेट अपडेट करने के लिए ये स्टेप्स फॉलो करें:
       
       1. **Marriage Certificate Update**:
          - नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (Service ID 201) का इस्तेमाल करें
          - इसके लिए SBI से 430 रुपये का चालान, नोटराइज्ड शपथ पत्र (50 रुपये), और स्थानीय अखबार में विज्ञापन देना होगा
          - 29 दिन का समय लगता है
       
       2. **Sewa Setu Portal पर**:
          - https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं
          - "Where to Apply" में Sewa Setu Kendra या Online विकल्प चुनें
          - Fee 30 रुपये है (Online और Kiosk दोनों के लिए)
       
       3. **Required Documents**:
          - पुराना नाम और नया नाम सत्यापन
          - सभी ID कार्ड (आवेदक और गवाहों के)
          - Form-I (अखबार में विज्ञापन)
          - Form-II (शपथ पत्र)
       
       4. **Process**:
          - फॉर्म भरें और सभी दस्तावेज अपलोड करें
          - 29 दिन में अपडेटेड सर्टिफिकेट मिल जाएगा
          - अपडेटेड सर्टिफिकेट के लिए दोबारा आवेदन करना होगा
       
       क्या आप किसी खास डॉक्यूमेंट के बारे में और जानकारी चाहते हैं?
       ```
---
| 21 | `what is the timeline for domicile certificate compared to obc certificate?` | 7 | 7 | ✅ MATCH | new_topic | 4.01s |

### Query 21 Details
* **Query**: `what is the timeline for domicile certificate compared to obc certificate?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `what is the timeline for domicile certificate compared to obc certificate?`
* **Resolved Hindi Query**: `समय-सीमा क्या है जो domicile प्रमाणपत्र के लिए है, जिसकी तुलना OBC प्रमाणपत्र से की गई है?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       what is the timeline for domicile certificate compared to obc certificate?
       ```
     * **Response**:
       ```json
       समय-सीमा क्या है जो domicile प्रमाणपत्र के लिए है, जिसकी तुलना OBC प्रमाणपत्र से की गई है?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       what is the timeline for domicile certificate compared to obc certificate?
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       what is the timeline for domicile certificate compared to obc certificate?
       ```
     * **Response**:
       ```json
       what is the timeline for domicile certificate compared to obc certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "what is the timeline for domicile certificate compared to obc certificate?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the timeline for domicile certificate compared to obc certificate?",
         "topic_summary": "Comparison of timelines for two different government certificates: Domicile and OBC."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "what is the timeline for domicile certificate compared to obc certificate?",
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
       Based on the provided documents, the timeline for a Domicile Certificate is 7 days, as stated in the Service Details Manual. However, the documents do not contain any information regarding the timeline for an OBC Certificate. Therefore, I cannot provide a comparison.
       
       I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.
       ```
---
| 22 | `caste certificate st sc validity vs niwas praman patra validity` | 4 | 4 | ✅ MATCH | new_topic | 5.81s |

### Query 22 Details
* **Query**: `caste certificate st sc validity vs niwas praman patra validity`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `caste certificate st sc validity vs domicile certificate validity`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र बनाम domicile प्रमाण पत्र की वैधता`
* **Final Synthesized Response**:
  > दोनों प्रमाण पत्रों की वैधता अवधि अलग-अलग है:
  > 
  > **SC/ST प्रमाण पत्र:**
  > - यह स्थायी प्रमाण पत्र है
  > - इसकी वैधता 22 दिन है (सेवा सेतु पोर्टल के अनुसार)
  > - यह राजस्व और आपदा प्रबंधन विभाग द्वारा जारी किया जाता है
  > 
  > **डोमिसाइल प्रमाण पत्र:**
  > - यह निवास प्रमाण पत्र है
  > - इसकी वैधता 30 दिन है (ई-डिस्ट्रिक्ट पोर्टल के अनुसार)
  > - यह भी राजस्व और आपदा प्रबंधन विभाग द्वारा जारी होता है
  > 
  > दोनों प्रमाण पत्र राजस्व विभाग के कार्यालयों से प्राप्त किए जा सकते हैं, लेकिन उनकी वैधता अवधि अलग-अलग है।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate st sc validity vs domicile certificate validity
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र बनाम domicile प्रमाण पत्र की वैधता
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate st sc validity vs domicile certificate validity
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate st sc validity vs domicile certificate validity
       ```
     * **Response**:
       ```json
       caste certificate st sc validity vs domicile certificate validity
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate st sc validity vs domicile certificate validity",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "caste certificate st sc validity vs domicile certificate validity",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "caste certificate st sc validity vs domicile certificate validity",
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
       दोनों प्रमाण पत्रों की वैधता अवधि अलग-अलग है:
       
       **SC/ST प्रमाण पत्र:**
       - यह स्थायी प्रमाण पत्र है
       - इसकी वैधता 22 दिन है (सेवा सेतु पोर्टल के अनुसार)
       - यह राजस्व और आपदा प्रबंधन विभाग द्वारा जारी किया जाता है
       
       **डोमिसाइल प्रमाण पत्र:**
       - यह निवास प्रमाण पत्र है
       - इसकी वैधता 30 दिन है (ई-डिस्ट्रिक्ट पोर्टल के अनुसार)
       - यह भी राजस्व और आपदा प्रबंधन विभाग द्वारा जारी होता है
       
       दोनों प्रमाण पत्र राजस्व विभाग के कार्यालयों से प्राप्त किए जा सकते हैं, लेकिन उनकी वैधता अवधि अलग-अलग है।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nदोनों प्रमाण पत्रों की वैधता अवधि अलग-अलग है:\n\n**SC/ST प्रमाण पत्र:**\n- यह स्थायी प्रमाण पत्र है\n- इसकी वैधता 22 दिन है (सेवा सेतु पोर्टल के अनुसार)\n- यह राजस्व और आपदा प्रबंधन विभाग द्वारा जारी किया जाता है\n\n**डोमिसाइल प्रमाण पत्र:**\n- यह निवास प्रमाण पत्र है\n- इसकी वैधता 30 दिन है (ई-डिस्ट्रिक्ट पोर्टल के अनुसार)\n- यह भी राजस्व और आपदा प्रबंधन विभाग द्वारा जारी होता है\n\nदोनों प्रमाण पत्र राजस्व विभाग के कार्यालयों से प्राप्त किए जा सकते हैं, लेकिन उनकी वैधता अवधि अलग-अलग है।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       दोनों प्रमाण पत्रों की वैधता अवधि अलग-अलग है:
       
       **SC/ST प्रमाण पत्र:**
       - यह स्थायी प्रमाण पत्र है
       - इसकी वैधता 22 दिन है (सेवा सेतु पोर्टल के अनुसार)
       - यह राजस्व और आपदा प्रबंधन विभाग द्वारा जारी किया जाता है
       
       **डोमिसाइल प्रमाण पत्र:**
       - यह निवास प्रमाण पत्र है
       - इसकी वैधता 30 दिन है (ई-डिस्ट्रिक्ट पोर्टल के अनुसार)
       - यह भी राजस्व और आपदा प्रबंधन विभाग द्वारा जारी होता है
       
       दोनों प्रमाण पत्र राजस्व विभाग के कार्यालयों से प्राप्त किए जा सकते हैं, लेकिन उनकी वैधता अवधि अलग-अलग है।
       ```
---
| 23 | `marriage registration offline location Raipur municipal corporation rules for out of state domicile` | 3 | 3 | ✅ MATCH | new_topic | 2.37s |

### Query 23 Details
* **Query**: `marriage registration offline location Raipur municipal corporation rules for out of state domicile`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap Marriage Registration & Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registration offline location Raipur municipal corporation rules for out of state domicile
       ```
     * **Response**:
       ```json
       marriage registration offline location Raipur municipal corporation rules for out of state domicile
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registration offline location Raipur municipal corporation rules for out of state domicile
       ```
     * **Response**:
       ```json
       hinglish
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registration offline location Raipur municipal corporation rules for out of state domicile
       ```
     * **Response**:
       ```json
       Raipur municipal corporation के अंतर्गत विवाह पंजीकरण ऑफलाइन स्थान नियम, राज्य से बाहर के निवासियों के लिए
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registration offline location Raipur municipal corporation rules for out of state domicile",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "marriage registration offline location raipur municipal corporation rules for out of state domicile",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "marriage registration offline location Raipur municipal corporation rules for out of state domicile",
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
| 24 | `gazette notification rules for name change after divorce decree` | 201 | 201 | ✅ MATCH | new_topic | 3.27s |

### Query 24 Details
* **Query**: `gazette notification rules for name change after divorce decree`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Ordinary Gazette Notification for Name Change using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       gazette notification rules for name change after divorce decree
       ```
     * **Response**:
       ```json
       gazette notification rules for name change after divorce decree
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       gazette notification rules for name change after divorce decree
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       gazette notification rules for name change after divorce decree
       ```
     * **Response**:
       ```json
       घोषणापत्र अधिसूचना नियम तलाक की डिक्री के बाद नाम परिवर्तन के लिए
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "gazette notification rules for name change after divorce decree",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "gazette notification rules for name change after divorce decree",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "gazette notification rules for name change after divorce decree",
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
---
| 25 | `sc certificate application with mother's domicile certificate` | 4 | 4 | ✅ MATCH | new_topic | 5.42s |

### Query 25 Details
* **Query**: `sc certificate application with mother's domicile certificate`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `sc certificate application with mother's domicile certificate`
* **Resolved Hindi Query**: `स्क प्रमाणपत्र आवेदन अपनी माता के निवास प्रमाण पत्र के साथ`
* **Final Synthesized Response**:
  > Based on the provided documents, here is the information regarding the SC certificate application with a mother's domicile certificate:
  > 
  > **Fee Details:**
  > - Kiosk Fee: ₹30.0
  > - Online Fee: ₹30.0
  > - Total Application Fee: ₹30.0 (for one payment method)
  > 
  > **Required Documents:**
  > - **Mother's Domicile Certificate:** This is listed as a supporting document under "Residence Proof" (SNo 1), specifically as "Domicile Certificate" (Supporting Document 1).
  > - **Other Mandatory Documents:**
  >   - Caste Proof (SNo 2): Must include at least one of the following:
  >     - SC/ST Certificate from Sarpanch/Parshad/MLA/MP (Supporting Document 2)
  >     - Transfer Certificate from a recognized school (Supporting Document 3)
  >   - **Affidavit (SNo 3):** Not mandatory, but if provided, must be submitted.
  >   - **Vanshavali (SNo 4):** Not mandatory.
  > 
  > **Application Process:**
  > 1. Apply online via the Sewa Setu portal or at a Sewa Setu Kendra.
  > 2. Upload all required documents, including the mother's domicile certificate.
  > 3. Pay the applicable fee (₹30.0) either online or at the kiosk.
  > 4. Submit the application and obtain a receipt with an application number.
  > 
  > **Time Limit / SLA:**
  > - The service is guaranteed within 22 days from the date of application submission.
  > 
  > **Additional Notes:**
  > - The application can be tracked on the e-District portal using the application number.
  > - After issuance, the certificate can be downloaded from the e-District portal.
  > 
  > For more details, you can refer to the official Sewa Setu portal or the user manual.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       sc certificate application with mother's domicile certificate
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       sc certificate application with mother's domicile certificate
       ```
     * **Response**:
       ```json
       sc certificate application with mother's domicile certificate
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       sc certificate application with mother's domicile certificate
       ```
     * **Response**:
       ```json
       स्क प्रमाणपत्र आवेदन अपनी माता के निवास प्रमाण पत्र के साथ
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "sc certificate application with mother's domicile certificate",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "sc certificate application with mother's domicile certificate",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "sc certificate application with mother's domicile certificate",
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
       Based on the provided documents, here is the information regarding the SC certificate application with a mother's domicile certificate:
       
       **Fee Details:**
       - Kiosk Fee: ₹30.0
       - Online Fee: ₹30.0
       - Total Application Fee: ₹30.0 (for one payment method)
       
       **Required Documents:**
       - **Mother's Domicile Certificate:** This is listed as a supporting document under "Residence Proof" (SNo 1), specifically as "Domicile Certificate" (Supporting Document 1).
       - **Other Mandatory Documents:**
         - Caste Proof (SNo 2): Must include at least one of the following:
           - SC/ST Certificate from Sarpanch/Parshad/MLA/MP (Supporting Document 2)
           - Transfer Certificate from a recognized school (Supporting Document 3)
         - **Affidavit (SNo 3):** Not mandatory, but if provided, must be submitted.
         - **Vanshavali (SNo 4):** Not mandatory.
       
       **Application Process:**
       1. Apply online via the Sewa Setu portal or at a Sewa Setu Kendra.
       2. Upload all required documents, including the mother's domicile certificate.
       3. P
       ... [TRUNCATED FOR BREVITY] ...
       ```
---
| 26 | `obc certificate download online using caste registry credentials` | 5 | 5 | ✅ MATCH | new_topic | 25.00s |

### Query 26 Details
* **Query**: `obc certificate download online using caste registry credentials`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `obc certificate download online using caste registry credentials`
* **Resolved Hindi Query**: `ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें

ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       obc certificate download online using caste registry credentials
       ```
     * **Response**:
       ```json
       obc certificate download online using caste registry credentials
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       obc certificate download online using caste registry credentials
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       obc certificate download online using caste registry credentials
       ```
     * **Response**:
       ```json
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति प्रमाण पत्र डाउनलोड करें
       
       ऑनलाइन जाति 
       ... [TRUNCATED FOR BREVITY] ...
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "obc certificate download online using caste registry credentials",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "obc certificate download online using caste registry credentials",
         "topic_summary": "User is asking about the process for downloading an OBC certificate online using caste registry credentials. This is a government service query related to a specific certificate, distinct from any previous service in the conversation history (which is empty)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "obc certificate download online using caste registry credentials",
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
       I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.
       ```
---
| 27 | `shadi praman patra eligibility for non-domicile of cg` | 3 | 3 | ✅ MATCH | new_topic | 28.73s |

### Query 27 Details
* **Query**: `shadi praman patra eligibility for non-domicile of cg`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Marriage Registration & Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registration and certificate eligibility for non-domicile of cg
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registration and certificate eligibility for non-domicile of cg
       ```
     * **Response**:
       ```json
       marriage registration and certificate eligibility for non-domicile of cg
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registration and certificate eligibility for non-domicile of cg
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण और cg के गैर-निवासी के लिए प्रमाणपत्र पात्रता
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       विवाह पंजीकरण और प्रमाणपत्र पात्रता cg के गैर-निवासी के लिए
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domicile of cg
       
       marriage registration and certificate eligibility for non-domici
       ... [TRUNCATED FOR BREVITY] ...
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate eligibility for non-domicile of cg",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "marriage registration and certificate eligibility for non-domicile of cg",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "marriage registration and certificate eligibility for non-domicile of cg",
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
| 28 | `caste certificate correction name change application format` | 4 | 201 | ❌ MISMATCH | new_topic | 3.20s |

### Query 28 Details
* **Query**: `caste certificate correction name change application format`
* **Expected Service ID**: `4`
* **Classified Service ID**: `201`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `caste certificate correction name change application format`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate correction name change application format
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate correction name change application format
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate correction name change application format
       ```
     * **Response**:
       ```json
       caste certificate correction name change application format
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate correction name change application format",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "caste certificate correction name change application format",
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
       I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.
       ```
---
| 29 | `is 15 years stay domicile rule applicable for obc certificate?` | 5 | 5 | ✅ MATCH | new_topic | 2.45s |

### Query 29 Details
* **Query**: `is 15 years stay domicile rule applicable for obc certificate?`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap OBC Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is 15 years stay domicile rule applicable for obc certificate?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is 15 years stay domicile rule applicable for obc certificate?
       ```
     * **Response**:
       ```json
       Is the 15-year domicile rule applicable for an OBC certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is 15 years stay domicile rule applicable for obc certificate?
       ```
     * **Response**:
       ```json
       क्या 15 वर्ष का निवास अधिवास नियम ओ बी सी प्रमाण पत्र के लिए लागू है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is 15 years stay domicile rule applicable for obc certificate?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is the 15 years stay domicile rule applicable for OBC certificate?",
         "topic_summary": "Query about OBC certificate eligibility criteria, specifically the 15 years stay rule for domicile."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "is 15 years stay domicile rule applicable for obc certificate?",
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
---
| 30 | `gazette notification cost for change of name vs marriage certificate online fee` | 201 | 201 | ✅ MATCH | new_topic | 4.41s |

### Query 30 Details
* **Query**: `gazette notification cost for change of name vs marriage certificate online fee`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `gazette notification cost for change of name vs marriage registration and certificate online fee`
* **Resolved Hindi Query**: `गज़ट अधिसूचना लागत नाम परिवर्तन बनाम विवाह पंजीकरण और प्रमाणपत्र ऑनलाइन शुल्क के लिए`
* **Final Synthesized Response**:
  > Based on the provided information, here are the costs for the services you asked about:
  > 
  > **Gazette Notification for Name Change:**
  > - **Application Fee:** ₹30.0 (either online or at a Sewa Setu Kendra)
  > - **Mandatory Documents:** SBI challan of ₹430, notarized affidavit on ₹50 stamp paper, newspaper publication, deed form with witness details, and identity proofs.
  > 
  > **Marriage Registration:**
  > - The provided documents do not specify the fee for marriage registration.
  > 
  > **Certificate Online Fee:**
  > - The provided documents do not specify the fee for certificate online applications.
  > 
  > For the most accurate and up-to-date fee information on marriage registration and certificate online services, please refer to the official Chhattisgarh Sewa Setu portal.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       gazette notification cost for change of name vs marriage registration and certificate online fee
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       gazette notification cost for change of name vs marriage registration and certificate online fee
       ```
     * **Response**:
       ```json
       gazette notification cost for change of name vs marriage registration and certificate online fee
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       gazette notification cost for change of name vs marriage registration and certificate online fee
       ```
     * **Response**:
       ```json
       गज़ट अधिसूचना लागत नाम परिवर्तन बनाम विवाह पंजीकरण और प्रमाणपत्र ऑनलाइन शुल्क के लिए
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "gazette notification cost for change of name vs marriage registration and certificate online fee",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the cost for gazette notification for change of name and marriage registration?",
         "topic_summary": "User is asking about the cost for two different government services: gazette notification for change of name and marriage registration."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "gazette notification cost for change of name vs marriage registration and certificate online fee",
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
       Based on the provided information, here are the costs for the services you asked about:
       
       **Gazette Notification for Name Change:**
       - **Application Fee:** ₹30.0 (either online or at a Sewa Setu Kendra)
       - **Mandatory Documents:** SBI challan of ₹430, notarized affidavit on ₹50 stamp paper, newspaper publication, deed form with witness details, and identity proofs.
       
       **Marriage Registration:**
       - The provided documents do not specify the fee for marriage registration.
       
       **Certificate Online Fee:**
       - The provided documents do not specify the fee for certificate online applications.
       
       For the most accurate and up-to-date fee information on marriage registration and certificate online services, please refer to the official Chhattisgarh Sewa Setu portal.
       ```
---
| 31 | `can married daughters apply for st certificate using father's caste proof?` | 4 | 4 | ✅ MATCH | new_topic | 5.81s |

### Query 31 Details
* **Query**: `can married daughters apply for st certificate using father's caste proof?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `can married daughters apply for st certificate using father's caste proof?`
* **Resolved Hindi Query**: `क्या विवाहित पुत्रियाँ अपने पिता के जाति प्रमाण का उपयोग करके एस टी प्रमाणपत्र के लिए आवेदन कर सकती हैं?`
* **Final Synthesized Response**:
  > नहीं, शादीशुदा बेटी अपने पिता के जाति प्रमाण का उपयोग करके ST प्रमाण पत्र के लिए आवेदन नहीं कर सकती।
  > 
  > ST प्रमाण पत्र के लिए जाति प्रमाण अनिवार्य है और यह आवेदक के स्वयं के जाति प्रमाण पर आधारित होता है। पिता का प्रमाण पत्र केवल तभी स्वीकार किया जाता है जब आवेदक स्वयं SC/ST समुदाय से संबंधित हो।
  > 
  > अगर बेटी शादी के बाद अपने पति के समुदाय में शामिल हो गई है, तो उसे अपने पति के जाति प्रमाण के आधार पर प्रमाण पत्र के लिए आवेदन करना होगा।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       can married daughters apply for st certificate using father's caste proof?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       can married daughters apply for st certificate using father's caste proof?
       ```
     * **Response**:
       ```json
       can married daughters apply for st certificate using father's caste proof?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       can married daughters apply for st certificate using father's caste proof?
       ```
     * **Response**:
       ```json
       क्या विवाहित पुत्रियाँ अपने पिता के जाति प्रमाण का उपयोग करके एस टी प्रमाणपत्र के लिए आवेदन कर सकती हैं?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "can married daughters apply for st certificate using father's caste proof?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Can married daughters apply for a caste certificate using their father's caste proof?",
         "topic_summary": "Query about applying for a caste certificate for a married daughter, using father's proof."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "can married daughters apply for st certificate using father's caste proof?",
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
       नहीं, शादीशुदा बेटी अपने पिता के जाति प्रमाण का उपयोग करके ST प्रमाण पत्र के लिए आवेदन नहीं कर सकती।
       
       ST प्रमाण पत्र के लिए जाति प्रमाण अनिवार्य है और यह आवेदक के स्वयं के जाति प्रमाण पर आधारित होता है। पिता का प्रमाण पत्र केवल तभी स्वीकार किया जाता है जब आवेदक स्वयं SC/ST समुदाय से संबंधित हो।
       
       अगर बेटी शादी के बाद अपने पति के समुदाय में शामिल हो गई है, तो उसे अपने पति के जाति प्रमाण के आधार पर प्रमाण पत्र के लिए आवेदन करना होगा।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nनहीं, शादीशुदा बेटी अपने पिता के जाति प्रमाण का उपयोग करके ST प्रमाण पत्र के लिए आवेदन नहीं कर सकती।\n\nST प्रमाण पत्र के लिए जाति प्रमाण अनिवार्य है और यह आवेदक के स्वयं के जाति प्रमाण पर आधारित होता है। पिता का प्रमाण पत्र केवल तभी स्वीकार किया जाता है जब आवेदक स्वयं SC/ST समुदाय से संबंधित हो।\n\nअगर बेटी शादी के बाद अपने पति के समुदाय में शामिल हो गई है, तो उसे अपने पति के जाति प्रमाण के आधार पर प्रमाण पत्र के लिए आवेदन करना होगा।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, शादीशुदा बेटी अपने पिता के जाति प्रमाण का उपयोग करके ST प्रमाण पत्र के लिए आवेदन नहीं कर सकती।
       
       ST प्रमाण पत्र के लिए जाति प्रमाण अनिवार्य है और यह आवेदक के स्वयं के जाति प्रमाण पर आधारित होता है। पिता का प्रमाण पत्र केवल तभी स्वीकार किया जाता है जब आवेदक स्वयं SC/ST समुदाय से संबंधित हो।
       
       अगर बेटी शादी के बाद अपने पति के समुदाय में शामिल हो गई है, तो उसे अपने पति के जाति प्रमाण के आधार पर प्रमाण पत्र के लिए आवेदन करना होगा।
       ```
---
| 32 | `niwas praman patra ke liye school study cg me 3 saal rule obc ke liye bhi hai?` | 7 | 7 | ✅ MATCH | new_topic | 2.33s |

### Query 32 Details
* **Query**: `niwas praman patra ke liye school study cg me 3 saal rule obc ke liye bhi hai?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap Domicile Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       domicile certificate ke liye school study cg me 3 saal rule obc ke liye bhi hai?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       domicile certificate ke liye school study cg me 3 saal rule obc ke liye bhi hai?
       ```
     * **Response**:
       ```json
       Is there a 3-year rule for school study in CG for a domicile certificate for OBC?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       domicile certificate ke liye school study cg me 3 saal rule obc ke liye bhi hai?
       ```
     * **Response**:
       ```json
       क्या domicile certificate के लिए स्कूल स्टडी CG में 3 साल का नियम OBC के लिए भी है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "domicile certificate ke liye school study cg me 3 saal rule obc ke liye bhi hai?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "domicile certificate ke liye school study cg me 3 saal rule obc ke liye bhi hai?",
         "topic_summary": "Query about domicile certificate requirements in Chhattisgarh, specifically regarding the 3-year rule for school studies and its applicability for OBC status."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "domicile certificate ke liye school study cg me 3 saal rule obc ke liye bhi hai?",
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
| 33 | `caste certificate digital signature verification vs domicile verification status` | 4 | None | ❌ MISMATCH | new_topic | 2.31s |

### Query 33 Details
* **Query**: `caste certificate digital signature verification vs domicile verification status`
* **Expected Service ID**: `4`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `caste certificate digital signature verification vs domicile verification status`
* **Resolved Hindi Query**: `डिजिटल हस्ताक्षर सत्यापन के साथ जाति प्रमाण पत्र बनाम निवास प्रमाण पत्र स्थिति`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate digital signature verification vs domicile verification status
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate digital signature verification vs domicile verification status
       ```
     * **Response**:
       ```json
       caste certificate digital signature verification vs domicile verification status
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate digital signature verification vs domicile verification status
       ```
     * **Response**:
       ```json
       डिजिटल हस्ताक्षर सत्यापन के साथ जाति प्रमाण पत्र बनाम निवास प्रमाण पत्र स्थिति
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate digital signature verification vs domicile verification status",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "caste certificate digital signature verification vs domicile verification status",
         "topic_summary": "User is asking about two different aspects of a government service: digital signature verification for a caste certificate and status checking for domicile verification. This is a new topic as it involves a different service (caste certificate) and a different aspect (digital signature) compared to any previous conversation history (which is empty)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "caste certificate digital signature verification vs domicile verification status",
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
---
| 34 | `marriage registrar local area authority in village for caste certificate holders` | 3 | 3 | ✅ MATCH | new_topic | 4.80s |

### Query 34 Details
* **Query**: `marriage registrar local area authority in village for caste certificate holders`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the marriage registrar's local area authority in a village for caste certificate holders?`
* **Resolved Hindi Query**: `विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण गाँव में जाति प्रमाण पत्र धारकों के लिए`
* **Final Synthesized Response**:
  > Based on the provided documents, the marriage registrar is the Local Authority of the local area where the marriage was solemnized. This includes the Gram Panchayat for rural areas or the Municipality or Municipal Corporation for urban areas. The registrar is responsible for maintaining the Register of marriages and issuing certificates of registration. The Local Authority is defined as the Gram Panchayat, Municipality, or Municipal Corporation, depending on the area.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       marriage registrar local area authority in village for caste certificate holders
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       marriage registrar local area authority in village for caste certificate holders
       ```
     * **Response**:
       ```json
       What is the marriage registrar's local area authority in a village for caste certificate holders?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       marriage registrar local area authority in village for caste certificate holders
       ```
     * **Response**:
       ```json
       विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण गाँव में जाति प्रमाण पत्र धारकों के लिए
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "marriage registrar local area authority in village for caste certificate holders",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the process for getting a marriage registrar local area authority in a village for caste certificate holders?",
         "topic_summary": "User is inquiring about the process for a marriage registration service, specifically for caste certificate holders in a village, which is a new service topic not previously discussed."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "marriage registrar local area authority in village for caste certificate holders",
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
       Based on the provided documents, the marriage registrar is the Local Authority of the local area where the marriage was solemnized. This includes the Gram Panchayat for rural areas or the Municipality or Municipal Corporation for urban areas. The registrar is responsible for maintaining the Register of marriages and issuing certificates of registration. The Local Authority is defined as the Gram Panchayat, Municipality, or Municipal Corporation, depending on the area.
       ```
---
| 35 | `is it mandatory to submit marriage invitation card for name change in gazette?` | 201 | 201 | ✅ MATCH | new_topic | 4.08s |

### Query 35 Details
* **Query**: `is it mandatory to submit marriage invitation card for name change in gazette?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is it mandatory to submit a marriage invitation card for name change in the gazette?`
* **Resolved Hindi Query**: `क्या नाम परिवर्तन के लिए गज़ट में विवाह आमंत्रण पत्र जमा करना अनिवार्य है?`
* **Final Synthesized Response**:
  > No, a marriage invitation card is not a mandatory document for name change in the gazette. The required documents are:
  > 
  > 1. Original copy of a challan of ₹430/- from any State Bank of India branch
  > 2. Notarized affidavit in Form-III on ₹50 non-judicial stamp paper (not more than 3 months old)
  > 3. Original copy of the publication of the notice for name change in Form-I in a local newspaper (not more than 3 months old)
  > 4. Original copy of the deed form in Form-II with names, signatures and addresses of 2 witnesses
  > 5. Old name & new name verification document
  > 6. All types of documents/identity cards/IDs mentioned in the affidavit
  > 7. Identity card of the applicant issued by the government
  > 8. Identity card of witnesses issued by the government
  > 
  > The marriage invitation card is not listed among the mandatory documents.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is it mandatory to submit marriage invitation card for name change in gazette?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is it mandatory to submit marriage invitation card for name change in gazette?
       ```
     * **Response**:
       ```json
       Is it mandatory to submit a marriage invitation card for name change in the gazette?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is it mandatory to submit marriage invitation card for name change in gazette?
       ```
     * **Response**:
       ```json
       क्या नाम परिवर्तन के लिए गज़ट में विवाह आमंत्रण पत्र जमा करना अनिवार्य है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is it mandatory to submit marriage invitation card for name change in gazette?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is it mandatory to submit a marriage invitation card for name change in the gazette?",
         "topic_summary": "Query about the requirement of a marriage invitation card for name change in the gazette."
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
       No, a marriage invitation card is not a mandatory document for name change in the gazette. The required documents are:
       
       1. Original copy of a challan of ₹430/- from any State Bank of India branch
       2. Notarized affidavit in Form-III on ₹50 non-judicial stamp paper (not more than 3 months old)
       3. Original copy of the publication of the notice for name change in Form-I in a local newspaper (not more than 3 months old)
       4. Original copy of the deed form in Form-II with names, signatures and addresses of 2 witnesses
       5. Old name & new name verification document
       6. All types of documents/identity cards/IDs mentioned in the affidavit
       7. Identity card of the applicant issued by the government
       8. Identity card of witnesses issued by the government
       
       The marriage invitation card is not listed among the mandatory documents.
       ```
---
| 36 | `obc certificate fee payment online cg state vs sc st certificate online fee` | 5 | 5 | ✅ MATCH | new_topic | 6.15s |

### Query 36 Details
* **Query**: `obc certificate fee payment online cg state vs sc st certificate online fee`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `obc certificate fee payment online cg state vs sc st certificate online fee`
* **Resolved Hindi Query**: `ओ बी सी प्रमाणपत्र शुल्क भुगतान ऑनलाइन सी जी राज्य बनाम एस सी एस टी प्रमाणपत्र ऑनलाइन शुल्क`
* **Final Synthesized Response**:
  > दोनों प्रमाण पत्रों के लिए ऑनलाइन शुल्क समान है।
  > 
  > - **OBC प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0
  > - **SC/ST प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0
  > 
  > दोनों प्रमाण पत्रों के लिए शुल्क समान है।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       obc certificate fee payment online cg state vs sc st certificate online fee
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       obc certificate fee payment online cg state vs sc st certificate online fee
       ```
     * **Response**:
       ```json
       ओ बी सी प्रमाणपत्र शुल्क भुगतान ऑनलाइन सी जी राज्य बनाम एस सी एस टी प्रमाणपत्र ऑनलाइन शुल्क
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       obc certificate fee payment online cg state vs sc st certificate online fee
       ```
     * **Response**:
       ```json
       obc certificate fee payment online cg state vs sc st certificate online fee
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "obc certificate fee payment online cg state vs sc st certificate online fee",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the fee for an OBC certificate?",
         "topic_summary": "User is asking about the fee for an OBC certificate, which is a different service from the previous conversation history (which was about SC/ST certificates)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "obc certificate fee payment online cg state vs sc st certificate online fee",
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
       दोनों प्रमाण पत्रों के लिए ऑनलाइन शुल्क समान है।
       
       - **OBC प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0
       - **SC/ST प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0
       
       दोनों प्रमाण पत्रों के लिए शुल्क समान है।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nदोनों प्रमाण पत्रों के लिए ऑनलाइन शुल्क समान है।\n\n- **OBC प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0\n- **SC/ST प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0\n\nदोनों प्रमाण पत्रों के लिए शुल्क समान है।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       दोनों प्रमाण पत्रों के लिए ऑनलाइन शुल्क समान है।
       
       - **OBC प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0
       - **SC/ST प्रमाण पत्र:** ऑनलाइन शुल्क ₹30.0
       
       दोनों प्रमाण पत्रों के लिए शुल्क समान है।
       ```
---
| 37 | `domicile certificate cg eligibility criteria for central govt employees vs cg state st employees` | 7 | 7 | ✅ MATCH | new_topic | 2.55s |

### Query 37 Details
* **Query**: `domicile certificate cg eligibility criteria for central govt employees vs cg state st employees`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap Domicile Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       domicile certificate cg eligibility criteria for central govt employees vs cg state st employees
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       domicile certificate cg eligibility criteria for central govt employees vs cg state st employees
       ```
     * **Response**:
       ```json
       What are the domicile certificate CG eligibility criteria for central government employees versus CG state ST employees?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       domicile certificate cg eligibility criteria for central govt employees vs cg state st employees
       ```
     * **Response**:
       ```json
       cg domicile certificate cg eligibility criteria for central govt employees vs cg state st employees
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "domicile certificate cg eligibility criteria for central govt employees vs cg state st employees",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "domicile certificate cg eligibility criteria for central govt employees vs cg state st employees",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "domicile certificate cg eligibility criteria for central govt employees vs cg state st employees",
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
| 38 | `name change publication in gazette timeline vs marriage certificate timeline` | 201 | 201 | ✅ MATCH | new_topic | 5.62s |

### Query 38 Details
* **Query**: `name change publication in gazette timeline vs marriage certificate timeline`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `name change publication in gazette timeline vs marriage registration and certificate timeline`
* **Resolved Hindi Query**: `नाम परिवर्तन प्रकाशन राजपत्र समयरेखा बनाम विवाह पंजीकरण और प्रमाणपत्र समयरेखा`
* **Final Synthesized Response**:
  > Service ID: 201 के लिए gazette publication का timeline 29 दिन है। यह एक combined process है, जिसमें 29 दिन में सभी documents submit करने होते हैं।
  > 
  > Marriage registration का timeline अलग होता है। यह state के marriage registration rules पर depend करता है, लेकिन आमतौर पर 15-30 दिन लग सकते हैं।
  > 
  > Certificate correction का timeline भी अलग है। इसके लिए Gazette notification apply करना पड़ता है, जिसमें 29 दिन का SLA है।
  > 
  > सभी timelines अलग-अलग हैं, इसलिए exact time के लिए respective department से contact करना बेहतर है।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       name change publication in gazette timeline vs marriage registration and certificate timeline
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       name change publication in gazette timeline vs marriage registration and certificate timeline
       ```
     * **Response**:
       ```json
       name change publication in gazette timeline vs marriage registration and certificate timeline
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       name change publication in gazette timeline vs marriage registration and certificate timeline
       ```
     * **Response**:
       ```json
       नाम परिवर्तन प्रकाशन राजपत्र समयरेखा बनाम विवाह पंजीकरण और प्रमाणपत्र समयरेखा
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "name change publication in gazette timeline vs marriage registration and certificate timeline",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the timeline for marriage registration and certificate?",
         "topic_summary": "User is asking about the timeline for a different service (marriage registration) compared to the previous topic (name change publication in gazette)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "name change publication in gazette timeline vs marriage registration and certificate timeline",
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
       Service ID: 201 के लिए gazette publication का timeline 29 दिन है। यह एक combined process है, जिसमें 29 दिन में सभी documents submit करने होते हैं।
       
       Marriage registration का timeline अलग होता है। यह state के marriage registration rules पर depend करता है, लेकिन आमतौर पर 15-30 दिन लग सकते हैं।
       
       Certificate correction का timeline भी अलग है। इसके लिए Gazette notification apply करना पड़ता है, जिसमें 29 दिन का SLA है।
       
       सभी timelines अलग-अलग हैं, इसलिए exact time के लिए respective department से contact करना बेहतर है।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nService ID: 201 के लिए gazette publication का timeline 29 दिन है। यह एक combined process है, जिसमें 29 दिन में सभी documents submit करने होते हैं।\n\nMarriage registration का timeline अलग होता है। यह state के marriage registration rules पर depend करता है, लेकिन आमतौर पर 15-30 दिन लग सकते हैं।\n\nCertificate correction का timeline भी अलग है। इसके लिए Gazette notification apply करना पड़ता है, जिसमें 29 दिन का SLA है।\n\nसभी timelines अलग-अलग हैं, इसलिए exact time के लिए respective department से contact करना बेहतर है।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       Service ID: 201 के लिए gazette publication का timeline 29 दिन है। यह एक combined process है, जिसमें 29 दिन में सभी documents submit करने होते हैं।
       
       Marriage registration का timeline अलग होता है। यह state के marriage registration rules पर depend करता है, लेकिन आमतौर पर 15-30 दिन लग सकते हैं।
       
       Certificate correction का timeline भी अलग है। इसके लिए Gazette notification apply करना पड़ता है, जिसमें 29 दिन का SLA है।
       
       सभी timelines अलग-अलग हैं, इसलिए exact time के लिए respective department से contact करना बेहतर है।
       ```
---
| 39 | `caste certificate offline tehsil office address for obc domicile` | 4 | 4 | ✅ MATCH | new_topic | 5.13s |

### Query 39 Details
* **Query**: `caste certificate offline tehsil office address for obc domicile`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `caste certificate offline tehsil office address for obc domicile`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र ऑफलाइन तहसील कार्यालय का पता ओ बी सी निवास के लिए`
* **Final Synthesized Response**:
  > मैं आपके लिए ऑफलाइन तहसील कार्यालय का पता बता सकता हूं।
  > 
  > ओ बी सी (OBC) और डी ओ एम (Domicile) प्रमाण पत्र के लिए आप अपने जिले के तहसील कार्यालय जा सकते हैं।
  > 
  > उदाहरण के लिए, अगर आप बिलासपुर जिले में हैं तो:
  > - बिलासपुर तहसील कार्यालय, सिविल लाइन, बिलासपुर, छत्तीसगढ़ - 401101
  > 
  > आप अपने जिले के तहसील कार्यालय के लिए गूगल पर "तहसील कार्यालय [आपके जिले का नाम]" सर्च कर सकते हैं।
  > 
  > Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
  > [Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate offline tehsil office address for obc domicile
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate offline tehsil office address for obc domicile
       ```
     * **Response**:
       ```json
       caste certificate offline tehsil office address for obc domicile
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate offline tehsil office address for obc domicile
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र ऑफलाइन तहसील कार्यालय का पता ओ बी सी निवास के लिए
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate offline tehsil office address for obc domicile",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the offline tehsil office address for an OBC domicile caste certificate?",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "caste certificate offline tehsil office address for obc domicile",
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
       मैं आपके लिए ऑफलाइन तहसील कार्यालय का पता बता सकता हूं।
       
       ओ बी सी (OBC) और डी ओ एम (Domicile) प्रमाण पत्र के लिए आप अपने जिले के तहसील कार्यालय जा सकते हैं।
       
       उदाहरण के लिए, अगर आप बिलासपुर जिले में हैं तो:
       - बिलासपुर तहसील कार्यालय, सिविल लाइन, बिलासपुर, छत्तीसगढ़ - 401101
       
       आप अपने जिले के तहसील कार्यालय के लिए गूगल पर "तहसील कार्यालय [आपके जिले का नाम]" सर्च कर सकते हैं।
       ```
  7. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "user",
           "content": "Convert the following text to Hinglish — Hindi written ONLY in Roman/Latin script. Replace ALL Devanagari characters with their Roman transliteration. Keep English words as-is. Keep the meaning and structure exactly the same. Do NOT add any extra text, do NOT translate to formal English, just transliterate Devanagari to Roman script.\n\nText to convert:\nमैं आपके लिए ऑफलाइन तहसील कार्यालय का पता बता सकता हूं।\n\nओ बी सी (OBC) और डी ओ एम (Domicile) प्रमाण पत्र के लिए आप अपने जिले के तहसील कार्यालय जा सकते हैं।\n\nउदाहरण के लिए, अगर आप बिलासपुर जिले में हैं तो:\n- बिलासपुर तहसील कार्यालय, सिविल लाइन, बिलासपुर, छत्तीसगढ़ - 401101\n\nआप अपने जिले के तहसील कार्यालय के लिए गूगल पर \"तहसील कार्यालय [आपके जिले का नाम]\" सर्च कर सकते हैं।\n\nRoman script output:"
         }
       ]
       ```
     * **Response**:
       ```json
       मैं आपके लिए ऑफलाइन तहसील कार्यालय का पता बता सकता हूं।
       
       ओ बी सी (OBC) और डी ओ एम (Domicile) प्रमाण पत्र के लिए आप अपने जिले के तहसील कार्यालय जा सकते हैं।
       
       उदाहरण के लिए, अगर आप बिलासपुर जिले में हैं तो:
       - बिलासपुर तहसील कार्यालय, सिविल लाइन, बिलासपुर, छत्तीसगढ़ - 401101
       
       आप अपने जिले के तहसील कार्यालय के लिए गूगल पर "तहसील कार्यालय [आपके जिले का नाम]" सर्च कर सकते हैं।
       ```
---
| 40 | `is notarized affidavit in Form-III for name change same as marriage affidavit?` | 201 | 201 | ✅ MATCH | new_topic | 3.16s |

### Query 40 Details
* **Query**: `is notarized affidavit in Form-III for name change same as marriage affidavit?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is a notarized affidavit in Form-III for name change the same as a marriage affidavit?`
* **Resolved Hindi Query**: `क्या फॉर्म-III में नोटरीकृत शपथ पत्र नाम परिवर्तन के लिए विवाह शपथ पत्र के समान है?`
* **Final Synthesized Response**:
  > No, the notarized affidavit in Form-III for name change is not the same as a marriage affidavit. The Form-III affidavit is specifically for name change purposes and requires details like old name, new name, and supporting documents. A marriage affidavit is used to prove marriage and typically includes information about both parties, their families, and the marriage ceremony. The two affidavits serve different legal purposes and have distinct requirements.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is notarized affidavit in Form-III for name change same as marriage affidavit?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is notarized affidavit in Form-III for name change same as marriage affidavit?
       ```
     * **Response**:
       ```json
       क्या फॉर्म-III में नोटरीकृत शपथ पत्र नाम परिवर्तन के लिए विवाह शपथ पत्र के समान है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is notarized affidavit in Form-III for name change same as marriage affidavit?
       ```
     * **Response**:
       ```json
       Is a notarized affidavit in Form-III for name change the same as a marriage affidavit?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is notarized affidavit in Form-III for name change same as marriage affidavit?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is notarized affidavit in Form-III for name change same as marriage affidavit?",
         "topic_summary": "Comparing two different government documents: Form-III affidavit for name change and marriage affidavit."
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
       No, the notarized affidavit in Form-III for name change is not the same as a marriage affidavit. The Form-III affidavit is specifically for name change purposes and requires details like old name, new name, and supporting documents. A marriage affidavit is used to prove marriage and typically includes information about both parties, their families, and the marriage ceremony. The two affidavits serve different legal purposes and have distinct requirements.
       ```
---
| 41 | `st caste praman patra verification with land documents and domicile certificate` | 4 | 4 | ✅ MATCH | new_topic | 2.18s |

### Query 41 Details
* **Query**: `st caste praman patra verification with land documents and domicile certificate`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the SC/ST Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       st caste certificate verification with land documents and domicile certificate
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       st caste certificate verification with land documents and domicile certificate
       ```
     * **Response**:
       ```json
       st caste certificate verification with land documents and domicile certificate
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       st caste certificate verification with land documents and domicile certificate
       ```
     * **Response**:
       ```json
       अनुसूचित जाति प्रमाण पत्र सत्यापन भूमि दस्तावेजों और निवास प्रमाण पत्र के साथ
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "st caste certificate verification with land documents and domicile certificate",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "caste certificate verification with land documents and domicile certificate",
         "topic_summary": "User is inquiring about the process for caste certificate verification, specifically mentioning required documents like land records and domicile certificate."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "st caste certificate verification with land documents and domicile certificate",
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
---
| 42 | `obc income certificate slab details for domicile students` | 5 | None | ❌ MISMATCH | new_topic | 2.75s |

### Query 42 Details
* **Query**: `obc income certificate slab details for domicile students`
* **Expected Service ID**: `5`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `obc income certificate slab details for domicile students`
* **Resolved Hindi Query**: `ओ बी सी आय एस एल प्रमाणपत्र स्लैब विवरण डोमिसाइल छात्रों के लिए`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       obc income certificate slab details for domicile students
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       obc income certificate slab details for domicile students
       ```
     * **Response**:
       ```json
       ओ बी सी आय एस एल प्रमाणपत्र स्लैब विवरण डोमिसाइल छात्रों के लिए
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       obc income certificate slab details for domicile students
       ```
     * **Response**:
       ```json
       obc income certificate slab details for domicile students
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "obc income certificate slab details for domicile students",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "obc income certificate slab details for domicile students",
         "topic_summary": "User is asking for specific details about the income certificate slab for OBC students with domicile status."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "obc income certificate slab details for domicile students",
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
---
| 43 | `can we apply for marriage certificate and name change together on sewasetu?` | 3 | None | ❌ MISMATCH | new_topic | 2.17s |

### Query 43 Details
* **Query**: `can we apply for marriage certificate and name change together on sewasetu?`
* **Expected Service ID**: `3`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `can we apply for marriage registration and certificate and name change together on sewasetu?`
* **Resolved Hindi Query**: `क्या हम विवाह पंजीकरण और प्रमाण पत्र तथा नाम परिवर्तन के लिए एक साथ SewaSetu पर आवेदन कर सकते हैं?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Jaankari uplabhd nahi hai.

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       can we apply for marriage registration and certificate and name change together on sewasetu?
       ```
     * **Response**:
       ```json
       can we apply for marriage registration and certificate and name change together on sewasetu?
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       can we apply for marriage registration and certificate and name change together on sewasetu?
       ```
     * **Response**:
       ```json
       क्या हम विवाह पंजीकरण और प्रमाण पत्र तथा नाम परिवर्तन के लिए एक साथ SewaSetu पर आवेदन कर सकते हैं?
       ```
  3. **Function**: `detect_query_language`
     * **Input**:
       ```json
       can we apply for marriage registration and certificate and name change together on sewasetu?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "can we apply for marriage registration and certificate and name change together on sewasetu?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Can we apply for marriage registration and certificate and name change together on SewaSetu?",
         "topic_summary": "User is asking about applying for multiple services (marriage registration, certificate, and name change) together on SewaSetu."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "can we apply for marriage registration and certificate and name change together on sewasetu?",
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
---
| 44 | `what are the documents for sc caste certificate list if i already have domicile?` | 4 | 4 | ✅ MATCH | new_topic | 2.88s |

### Query 44 Details
* **Query**: `what are the documents for sc caste certificate list if i already have domicile?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Kya aap SC/ST Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       what are the documents for sc caste certificate list if i already have domicile?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       what are the documents for sc caste certificate list if i already have domicile?
       ```
     * **Response**:
       ```json
       what are the documents for sc caste certificate list if i already have domicile?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       what are the documents for sc caste certificate list if i already have domicile?
       ```
     * **Response**:
       ```json
       sc जाति प्रमाण पत्र के लिए किन दस्तावेजों की आवश्यकता है यदि मेरे पास निवास प्रमाण पत्र है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "what are the documents for sc caste certificate list if i already have domicile?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What are the documents for SC caste certificate if I already have domicile?",
         "topic_summary": "User is asking about documents for SC caste certificate, which is a different service from any previous (non-existent) conversation. The aspect of 'documents' is carried over from the implied context of a government service query, but the service itself is new. The query is not about the chatbot's identity, is in-scope, and is a follow-up to the implicit context of a government service discussion, but since it's a different service, it's classified as new_topic."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "what are the documents for sc caste certificate list if i already have domicile?",
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
---
| 45 | `niwas praman patra rules for spouse of cg domicile person` | 7 | 7 | ✅ MATCH | new_topic | 2.32s |

### Query 45 Details
* **Query**: `niwas praman patra rules for spouse of cg domicile person`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `N/A`
* **Resolved Hindi Query**: `N/A`
* **Final Synthesized Response**:
  > Would you like to check your eligibility for the Domicile Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       domicile certificate rules for spouse of cg domicile person
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       domicile certificate rules for spouse of cg domicile person
       ```
     * **Response**:
       ```json
       domicile certificate rules for spouse of cg domicile person
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       domicile certificate rules for spouse of cg domicile person
       ```
     * **Response**:
       ```json
       What are the domicile certificate rules for the spouse of a CG domicile person?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "domicile certificate rules for spouse of cg domicile person",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "domicile certificate rules for spouse of cg domicile person",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "domicile certificate rules for spouse of cg domicile person",
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
| 46 | `fees of obc certificate vs ordinary gazette publication fee` | 5 | None | ❌ MISMATCH | new_topic | 2.27s |

### Query 46 Details
* **Query**: `fees of obc certificate vs ordinary gazette publication fee`
* **Expected Service ID**: `5`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `fees of obc certificate vs ordinary gazette publication fee`
* **Resolved Hindi Query**: `ओ बी सी प्रमाणपत्र की फीस बनाम सामान्य गजट प्रकाशन फीस`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       fees of obc certificate vs ordinary gazette publication fee
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       fees of obc certificate vs ordinary gazette publication fee
       ```
     * **Response**:
       ```json
       fees of obc certificate vs ordinary gazette publication fee
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       fees of obc certificate vs ordinary gazette publication fee
       ```
     * **Response**:
       ```json
       ओ बी सी प्रमाणपत्र की फीस बनाम सामान्य गजट प्रकाशन फीस
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "fees of obc certificate vs ordinary gazette publication fee",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the fee for an OBC certificate compared to an ordinary gazette publication fee?",
         "topic_summary": ""
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "fees of obc certificate vs ordinary gazette publication fee",
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
---
| 47 | `is voter id mandatory for st certificate if i have school study certificate?` | 4 | None | ❌ MISMATCH | new_topic | 2.55s |

### Query 47 Details
* **Query**: `is voter id mandatory for st certificate if i have school study certificate?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is voter ID mandatory for ST certificate if I have school study certificate?`
* **Resolved Hindi Query**: `क्या स्कूल अध्ययन प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Jaankari uplabhd nahi hai.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       is voter id mandatory for st certificate if i have school study certificate?
       ```
     * **Response**:
       ```json
       hinglish
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       is voter id mandatory for st certificate if i have school study certificate?
       ```
     * **Response**:
       ```json
       Is voter ID mandatory for ST certificate if I have school study certificate?
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       is voter id mandatory for st certificate if i have school study certificate?
       ```
     * **Response**:
       ```json
       क्या स्कूल अध्ययन प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "is voter id mandatory for st certificate if i have school study certificate?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Is voter ID mandatory for a caste certificate if I have a school study certificate?",
         "topic_summary": "Query about caste certificate requirements, specifically if voter ID is needed as an alternative to school study certificate."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "is voter id mandatory for st certificate if i have school study certificate?",
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
---
| 48 | `where to submit marriage certificate application if husband belongs to other state?` | 3 | 3 | ✅ MATCH | new_topic | 5.20s |

### Query 48 Details
* **Query**: `where to submit marriage certificate application if husband belongs to other state?`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `where to submit marriage registration and certificate application if husband belongs to other state?`
* **Resolved Hindi Query**: `कहां पर विवाह पंजीकरण और प्रमाणपत्र आवेदन जमा करना है यदि पति दूसरे राज्य से संबंधित है?`
* **Final Synthesized Response**:
  > Based on the Chhattisgarh Sewa Setu portal information, marriage registration must be submitted in the local area where the marriage was solemnized or performed, not at the couple's hometown or place of residence. The application should be submitted to the Local Authority of that local area (Gram Panchayat if rural; Municipality or Municipal Corporation if urban).
  > 
  > The specific office/authority to register the marriage is the Local Authority of the place where the marriage occurred. You must apply to the Sewa Setu Kendra for this process.
  > 
  > For online submission, you can access the application through the Chhattisgarh e-District portal at cgedistrict.cgstate.gov.in or directly through the Sewa Setu portal.
  > 
  > If you need to apply at a physical center, the nearest Sewa Setu Kendra is where you should submit your application.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       where to submit marriage registration and certificate application if husband belongs to other state?
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       where to submit marriage registration and certificate application if husband belongs to other state?
       ```
     * **Response**:
       ```json
       कहां पर विवाह पंजीकरण और प्रमाणपत्र आवेदन जमा करना है यदि पति दूसरे राज्य से संबंधित है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       where to submit marriage registration and certificate application if husband belongs to other state?
       ```
     * **Response**:
       ```json
       where to submit marriage registration and certificate application if husband belongs to other state?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "where to submit marriage registration and certificate application if husband belongs to other state?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "What is the process and required documents for marriage registration if the husband belongs to another state?",
         "topic_summary": "Marriage registration process for inter-state marriage, including document requirements and submission procedure."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "where to submit marriage registration and certificate application if husband belongs to other state?",
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
       Based on the Chhattisgarh Sewa Setu portal information, marriage registration must be submitted in the local area where the marriage was solemnized or performed, not at the couple's hometown or place of residence. The application should be submitted to the Local Authority of that local area (Gram Panchayat if rural; Municipality or Municipal Corporation if urban).
       
       The specific office/authority to register the marriage is the Local Authority of the place where the marriage occurred. You must apply to the Sewa Setu Kendra for this process.
       
       For online submission, you can access the application through the Chhattisgarh e-District portal at cgedistrict.cgstate.gov.in or directly through the Sewa Setu portal.
       
       If you need to apply at a physical center, the nearest Sewa Setu Kendra is where you should submit your application.
       ```
---
| 49 | `can a name change gazette be used to correct name in obc certificate?` | 201 | 201 | ✅ MATCH | new_topic | 3.22s |

### Query 49 Details
* **Query**: `can a name change gazette be used to correct name in obc certificate?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `can a name change gazette be used to correct name in obc certificate?`
* **Resolved Hindi Query**: `क्या नाम परिवर्तन गजट का उपयोग ओ बी सी प्रमाण पत्र में नाम सुधार करने के लिए किया जा सकता है?`
* **Final Synthesized Response**:
  > No, a name change gazette cannot be used to correct a name in an OBC certificate. The gazette notification is for publishing name changes in official government publications, but it does not have the authority to modify existing certificates. To correct a name in an OBC certificate, you must apply for a fresh OBC certificate with the correct name through the proper channels. The gazette process is separate and does not replace the need for a new certificate.
  > 
  > For more details and online application, please visit:
  > [Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

* **LLM Call Trace**:
  1. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       can a name change gazette be used to correct name in obc certificate?
       ```
     * **Response**:
       ```json
       can a name change gazette be used to correct name in obc certificate?
       ```
  2. **Function**: `detect_query_language`
     * **Input**:
       ```json
       can a name change gazette be used to correct name in obc certificate?
       ```
     * **Response**:
       ```json
       en
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       can a name change gazette be used to correct name in obc certificate?
       ```
     * **Response**:
       ```json
       क्या नाम परिवर्तन गजट का उपयोग ओ बी सी प्रमाण पत्र में नाम सुधार करने के लिए किया जा सकता है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "can a name change gazette be used to correct name in obc certificate?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "Can a name change gazette be used to correct name in OBC certificate?",
         "topic_summary": "User is asking about using a name change gazette for correcting an OBC certificate name."
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
       No, a name change gazette cannot be used to correct a name in an OBC certificate. The gazette notification is for publishing name changes in official government publications, but it does not have the authority to modify existing certificates. To correct a name in an OBC certificate, you must apply for a fresh OBC certificate with the correct name through the proper channels. The gazette process is separate and does not replace the need for a new certificate.
       ```
---
| 50 | `caste certificate validity timeline for married women` | 4 | 4 | ✅ MATCH | new_topic | 4.74s |

### Query 50 Details
* **Query**: `caste certificate validity timeline for married women`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `caste certificate validity timeline for married women`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र की वैधता अवधि`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > Information not available.

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       caste certificate validity timeline for married women
       ```
     * **Response**:
       ```json
       en
       ```
  2. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       caste certificate validity timeline for married women
       ```
     * **Response**:
       ```json
       caste certificate validity timeline for married women
       ```
  3. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       caste certificate validity timeline for married women
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र की वैधता अवधि
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "caste certificate validity timeline for married women",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {
         "intent": "new_topic",
         "resolved_query": "caste certificate validity timeline for married women",
         "topic_summary": "Query about the validity timeline for a specific government service (caste certificate) for a specific demographic (married women)."
       }
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "caste certificate validity timeline for married women",
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
       Based on the provided documents, the caste certificate validity timeline for married women is not explicitly mentioned. The documents specify that the SC/ST certificate is valid for 22 days from the date of application (SLA), but they do not provide information regarding its validity period after issuance, especially for married women. Therefore, I do not have sufficient information in my records to answer this specific question. Kripya Sewa Setu portal par check karein.
       ```
---
