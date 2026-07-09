# SewaSetu Chatbot: 50 Confusing Queries Validation Results (Hindi Language)

This report captures validation runs of confusing queries typed directly in Devanagari Hindi.

| ID | Confusing Hindi User Query | Expected Service ID | Mapped Service ID | Match Status | Intent | Latency |
|----|----------------------------|---------------------|-------------------|--------------|--------|---------|
| 1 | `शादी के बाद नाम परिवर्तन कैसे करें?` | 201 | 201 | ✅ MATCH | new_topic | 4.53s |

### Query 1 Details
* **Query**: `शादी के बाद नाम परिवर्तन कैसे करें?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to change name after marriage?`
* **Resolved Hindi Query**: `शादी के बाद नाम परिवर्तन कैसे करें?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > शादी के बाद नाम परिवर्तन करने के लिए आपको साधारण राजपत्र अधिसूचना (आई डी 201) के लिए आवेदन करना होगा। इसके लिए निम्नलिखित अनिवार्य दस्तावेज चाहिए:
  > 
  > 1. 430 रुपये का भारतीय स्टेट बैंक का चालान
  > 2. 50 रुपये के नॉन ज्यूडिशियल स्टाम्प पेपर पर नोटराइज्ड शपथ पत्र (फॉर्म-III)
  > 3. स्थानीय समाचार पत्र में नाम परिवर्तन की सूचना (फॉर्म-I)
  > 4. दो गवाहों के हस्ताक्षर और पते के साथ प्ररूप-II
  > 5. पुराना नाम और नया नाम सत्यापन दस्तावेज़
  > 6. शपथ पत्र में उल्लिखित सभी प्रकार के पहचान पत्र
  > 
  > आवेदन की शुल्क 30 रुपये है, जिसे आप Sewa Setu केंद्र या ऑनलाइन पोर्टल के माध्यम से जमा कर सकते हैं। प्रक्रिया में 29 दिन का समय लगता है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "शादी के बाद नाम परिवर्तन कैसे करें?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "शादी के बाद नाम परिवर्तन कैसे करें?"
       ```
     * **Response**:
       ```json
       शादी के बाद नाम परिवर्तन कैसे करें?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "शादी के बाद नाम परिवर्तन कैसे करें?"
       ```
     * **Response**:
       ```json
       How to change name after marriage?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "शादी के बाद नाम परिवर्तन कैसे करें?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'How to change name after marriage?', 'topic_summary': 'User is asking about the process for name change after marriage, which is a different service from the general introduction of SewaSetu.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "शादी के बाद नाम परिवर्तन कैसे करें?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "शादी के बाद नाम परिवर्तन कैसे करें?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       शादी के बाद नाम परिवर्तन करने के लिए आपको साधारण राजपत्र अधिसूचना (आई डी 201) के लिए आवेदन करना होगा। इसके लिए निम्नलिखित अनिवार्य दस्तावेज चाहिए:
       
       1. 430 रुपये का भारतीय स्टेट बैंक का चालान
       2. 50 रुपये के नॉन ज्यूडिशियल स्टाम्प पेपर पर नोटराइज्ड शपथ पत्र (फॉर्म-III)
       3. स्थानीय समाचार पत्र में नाम परिवर्तन की सूचना (फॉर्म-I)
       4. दो गवाहों के हस्ताक्षर और पते के साथ प्ररूप-II
       5. पुराना नाम और नया नाम सत्यापन दस्तावेज़
       6. शपथ पत्र में उल्लिखित सभी प्रकार के पहचान पत्र
       
       आवेदन की शुल्क 30 रुपये है, जिसे आप Sewa Setu केंद्र या ऑनलाइन पोर्टल के माध्यम से जमा कर सकते हैं। प्रक्रिया में 29 दिन का समय लगता है।
       ```
| 2 | `क्या ओबीसी प्रमाणपत्र के लिए निवास प्रमाणपत्र आवश्यक है?` | 5 | 7 | ❌ MISMATCH | new_topic | 3.91s |

### Query 2 Details
* **Query**: `क्या ओबीसी प्रमाणपत्र के लिए निवास प्रमाणपत्र आवश्यक है?`
* **Expected Service ID**: `5`
* **Classified Service ID**: `7`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is the original residence certificate required for OBC certificate?`
* **Resolved Hindi Query**: `क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, मूल निवासी प्रमाण पत्र ओबीसी प्रमाणपत्र के लिए अनिवार्य नहीं है। ओबीसी प्रमाणपत्र के लिए अन्य दस्तावेजों की आवश्यकता होती है, जैसे कि जाति प्रमाण पत्र, निवास प्रमाण पत्र, और अन्य आवश्यक प्रमाण पत्र। मूल निवासी प्रमाण पत्र केवल निवास के प्रमाण के रूप में उपयोग किया जाता है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?"
       ```
     * **Response**:
       ```json
       क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?"
       ```
     * **Response**:
       ```json
       Is the original residence certificate required for OBC certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- ELIGIBILITY LOGIC RULE (Domicile): If a citizen asks about eligibility or exceptions for the Domicile Certificate, explain the rules strictly:\n  1. Main Path (Both Criteria One AND Criteria Two must be met): The applicant must satisfy AT LEAST ONE option from Criteria One (Criteria A) AND AT LEAST ONE option from Criteria Two (Criteria B).\n     * You MUST list Criteria One and Criteria Two under separate, clearly-labeled headers or bullet points.\n     * Criteria One (Criteria A) options: Birth in CG, parent resident for 25 years, parent is CG Government/PSU employee, or property in CG for 5 years.\n     * Criteria Two (Criteria B) options: 3 years of school study in CG, or passing Class 5, 8, 10, 12 board exam from CG.\n     * Never merge them into one list or omit the education requirements of Criteria Two.\n  2. Exceptions (Criteria Three / Criteria C): If they do not meet the Main Path (for example, if they lack 'Proof of 15 Years Stay' or did not study in CG), they can still get a Domicile Certificate under the exceptions of Criteria Three (C). For Criteria Three (C), Criteria A and B are NOT required. The exceptions are: (a) spouse is a domicile of CG, (b) applicant or spouse is a CG Government/PSU employee, or (c) applicant or parent is in All India Services and allotted CG Cadre.\n  3. Clarity: Never state that Criteria Three requires stay proof or education. Clearly explain that Criteria Three is a standalone set of exceptions that bypasses the need for the stay proof or CG education requirements of Criteria One and Two.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Domicile Certificate\nService ID: 7\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 7 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: Other (Mandatory: No)\n  * Supporting Document 1: Other Documents\n- SNo 3: Proof Of At Least 15 Years Stay (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate\n  * Supporting Document 2: Father/ Guardian Service Certificate\n  * Supporting Document 3: Job Service Certificate / Identity Card (If The Applicant Is Under Govt./Semi Govt.)\n  * Supporting Document 4: Voters Identity Card\n  * Supporting Document 5: Land And House Document\n  * Supporting Document 6: Birth Information Form\n  * Supporting Document 7: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 8: Ration Card\n  * Supporting Document 9: Electricity Bill\n- SNo 4: Educational Certificate (Mandatory: Yes)\n  * Supporting Document 1: Middle School Certificate - 8th Standard\n  * Supporting Document 2: Primary School Certificate - 5th Standard\n  * Supporting Document 3: High School(10th) Certificate\n  * Supporting Document 4: Higher Secondary School Certificate(12th)\n  * Supporting Document 5: M.Phil/D.Lit./Ph.D. Certificate\n  * Supporting Document 6: School Certificate (As A Proof Of 3 Years Continuous Study)\n  * Supporting Document 7: Post Graduation Certificate\n  * Supporting Document 8: Certificate In Technical Subjects\n- SNo 5: Proof Of At Least 5 Years Stay (Mandatory: No)\n  * Supporting Document 1: Land And House Document\n  * Supporting Document 2: Persons Service Book.\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Guardians Occupation of Beneficiary [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: Beneficiary place of Birth [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: Address Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 7, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: section lebel, Data: Charactar] (Row: 8, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: fieldset, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Beneficiary Details of Business or Service [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Beneficiary Details of Business or service [Type: fieldset, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Beneficiary Education Level [Type: section lebel, Data: Charactar] (Row: 12, Col: 1)\n- Field: Beneficiary Education Level [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Have Beneficiary Voter Id [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: District Name of Beneficiary [Type: drop down, Data: Charactar] (Row: 15, Col: 2)\n- Field: Living From in Years [Type: number, Data: Date] (Row: 16, Col: 1)\n- Field: Reason for application Domicile [Type: text, Data: Charactar] (Row: 16, Col: 2)\n- Field: Any other detail [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 17, Col: 2)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 7_en_7.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nउपयोगकर्ता मतगादर्शिकत \n \n  \nमूल निवतसी प्रमतण पत्र क े  र्लए ई-निस्ट्रिक्ट पोर्ाल पर ऑिलतइि आवेदि प्रक्रियत \n \nछत्तीसगढ़ इन्फोर्ेक प्रमोशि सोसतयर्ी\n\n--- Page 2 ---\nववषय सूची \nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर\n\n--- Source 2: [User Manual (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: official_document\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nOfficial Document Content: --- Page 1 (no rotation needed) ---\nCriteria for CG Domicille\n/. Criteria one: a. Born in CG (Birth Certificate) OR\n0 Either of the parents is a resident of CG for continuous २५ years. OR\nC\nEither of parents is an employee of CG Government or its undertaking. OR d. Either Of the parents or the applicant holds a property in CG for last 5yrs.\nB Criteria Two:\na\nThree yrs of formal education in CG. OR 0 Passed One of the board exams ( Class 5, 8, 10, 12) from CG.\nC. Criteria Threeः Apart from above the following persons will be considered eligible for CG Domicile if\na\nIf hislher spouse is a domicile of CG. 0 If the applicant or the spouse is an employee of CG Government or its PSU C If the applicant or his parentls is in all India services and has been allotted CG Cadre.\nNote: Criteria A and B together must be met to get the Certificate.\nFor Criteria C, Criteria A and B are not required.\nDocuments required:\n1. Application\n२. Affidavit\n३. Educational certificates\n४. Service Certificate if applicable\n5. Property docs if applicable\n६. Proof Of Residence for २५ yrs iaf applicable\n7 Birth Certificate if available.\n\n--- Source 3: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �िगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह पेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 4: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: 4.4: डनर्ाटररत बॉक्स पर क्लिक करक े  आर्ार प्रमाणीकरण हेतु सहमगत िें। \nचरण 4.5: “Authentication”  बटन पर क्लिक करें। \nचरण 4.6: आर्ार ई-प्रमाणीकरण क े  बाि “जमत करें” बटन पर क्लिक करें।  \nडनम्नानुसार पॉप-अप गविंिो खुलेगा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पू�\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: मूल निवासी प्रमाण पत्र\nService ID: 7\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 7 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य\n- SNo 3: १५ वर्ष तक निवास का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: जन्म प्रमाण पत्र\n  * Supporting Document 2: पिता/पालक का सेवा प्रमाण पत्र\n  * Supporting Document 3: नौकरी प्रमाणपत्र /पहचान पत्र (यदि आवेदक शासकीय /अर्ध शासकीय अधीनस्थ हो )\n  * Supporting Document 4: वोटिंग कार्ड\n  * Supporting Document 5: घर या भूमि का दस्तावेज़\n  * Supporting Document 6: जन्म सूचना प्रपत्र\n  * Supporting Document 7: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 8: राशन कार्ड\n  * Supporting Document 9: बिजली का बिल\n- SNo 4: शैक्षणिक प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: माध्यमिक विद्यालय का प्रमाणपत्र -8 कक्षा\n  * Supporting Document 2: प्राथमिक विद्यालय का प्रमाणपत्र - 5वीं कक्षा\n  * Supporting Document 3: हाई स्कूल(10वी कक्षा) अंकसूची\n  * Supporting Document 4: उच्चतर माध्यमिक विधालय प्रमाण पत्र(१२ वीं कक्षा)\n  * Supporting Document 5: एम-फिल\n  * Supporting Document 6: स्कूल प्रमाणपत्र (3 साल की एक सबूत निरंतर अध्ययन के रूप में)\n  * Supporting Document 7: स्नातकोत्तर प्रमाणपत्र\n  * Supporting Document 8: तकनीकी विषयों में प्रमाणपत्र\n- SNo 5: ५ साल निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: घर या भूमि का दस्तावेज़\n  * Supporting Document 2: व्यक्ति की सेवा पुस्तिका.\n\nAPPLICATION FORM FIELDS:\n- Field: सामान्य विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: हितग्राही के अभिभावक का प्रकार [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: हितग्राही के अभिभावक का नाम [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: हितग्राही के अभिभावक का व्यवसाय [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: हितग्राही का जन्म स्थान [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: लिंग [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: पता का विवरण [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: पता [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: पिन कोड [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: जिला [Type: drop down\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पूवतावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचर\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: । \n2. यूज़रिेम िजट करें। \n3. पतसविा िजट करें। \n4. “ओर्ीपी भेजें” पर क्लिक करें। \n5. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n6. लॉक्रगि बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजित खोज \nलॉगगन क े  पश्चात डनम्नानुसार योजना खोज पेज खुलेगा। \n \nचित्र क्रमांक 6 \n \nचरण 3.1: यहााँ डनर्ाटररत बॉक्स में पूछी गई जानकारी िजट करें और “खोजें” बटन पर क्लिक करें। \nचरण 3.2: सेवाओं की सूिी दिखाई िेगी, इसमें “Domicile Certificate” पर क्लिक करें। \nअब डनम्नानुसार पेज दिखाई िेगा। इस पेज पर, नीिे आवश्यक दस्ततवेज़़ों की सूिी िेखी जा सकती है। \n \n \nचित्र क्रमांक 7\n\n--- Page 7 ---\nचित्र क्रमांक 8 \n \nचरण 3.3: चित्र क्रमांक 7 क े  अनुसार प्रिचशित गविंिो में “आगे” बटन दिखाई िेगा, उस पर क्लिक करें।\n\n--- Page 8 ---\nचरण 4: आधतर ई-प्रमतणीकरण \nआर्ार ई-प्रमाणीकरण हेतु इस फॉमट में आवेिक की बुडनयािी जानकारी िजट करें। \n \nचित्र क्रमांक 9 \n \nचरण 4.1: आवेिक एवं दहतग्राही का नाम भरें। ड्रॉप-िाउन ललस्ट से िुनकर कायाटलय का नाम और पूरा पता िजट \nकरें। \nचरण 4.2: प्रमाणीकरण क े  ललए “Aadhaar e-authentication” पर क्लिक करें। डनम्नानुसार पॉप-अप \nगविंिो खुलेगा। \n \nचित्र क्रमांक 10\n\n--- Page 9 ---\nचरण 4.3: प्रमाणीकरण हेतु आर्ार संख्या एवं नाम (आर्ार कािट क े  अनुसार अ ं ग्रेज़ी में) िजट करें। \nचरण 4.4: डनर्ाटररत बॉक्स पर क्लिक करक े  आर्ार प्रमाणीकरण हेतु सहमगत िें। \nचरण 4.5: “Authentication”  बटन पर क्लिक करें। \nचरण 4.6: आर्ार ई-प्रमाणीकरण क े  बाि “जमत करें” बटन पर क्लिक करें।  \nडनम्नानुसार पॉप-अप गविंिो खुलेगा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_hi_citizenCharter.pdf (SLA_DETAILS)] ---\nछत्तीसगढ़ शासन\nराजस्व एवं आपदा प्रबंधन विभाग\nमंत्रालय\nमहानदी भवन नया रायपुर\n::: अधिसूचना :::\n\nरायपुर, दिनांक 16/05/2013\n\nक्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\nसारणी (SLA Details):\n1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n2. स्थाई जाति प्रमाण-पत्र (Permanent Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - सक्षम प्राधिकारी: कलेक्टर\n   - अपीलीय अधिकारी: कमिश्नर\n\n3. निवास प्रमाण-पत्र (Domicile Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्र\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या ओबीसी प्रमाणपत्र के लिए मूल निवासी प्रमाण पत्र आवश्यक है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, मूल निवासी प्रमाण पत्र ओबीसी प्रमाणपत्र के लिए अनिवार्य नहीं है। ओबीसी प्रमाणपत्र के लिए अन्य दस्तावेजों की आवश्यकता होती है, जैसे कि जाति प्रमाण पत्र, निवास प्रमाण पत्र, और अन्य आवश्यक प्रमाण पत्र। मूल निवासी प्रमाण पत्र केवल निवास के प्रमाण के रूप में उपयोग किया जाता है।
       ```
| 3 | `जाति प्रमाण पत्र के लिए निवास प्रमाण पत्र की पात्रता क्या है?` | 4 | 4 | ✅ MATCH | new_topic | 2.45s |

### Query 3 Details
* **Query**: `जाति प्रमाण पत्र के लिए निवास प्रमाण पत्र की पात्रता क्या है?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र के लिए मूल निवासी प्रमाण पत्र की पात्रता क्या है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र के लिए मूल निवासी प्रमाण पत्र की पात्रता क्या है?"
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र के लिए मूल निवासी प्रमाण पत्र की पात्रता क्या है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र के लिए मूल निवासी प्रमाण पत्र की पात्रता क्या है?"
       ```
     * **Response**:
       ```json
       What is the eligibility for a native certificate for a caste certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र के लिए मूल निवासी प्रमाण पत्र की पात्रता क्या है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the eligibility for original resident certificate for caste certificate?', 'topic_summary': 'User is asking about eligibility criteria for an original resident certificate, which is a different service from the general introduction of SewaSetu.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र के लिए मूल निवासी प्रमाण पत्र की पात्रता क्या है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
| 4 | `ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का निवास प्रमाण पत्र होना जरूरी है?` | 5 | 5 | ✅ MATCH | new_topic | 4.61s |

### Query 4 Details
* **Query**: `ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का निवास प्रमाण पत्र होना जरूरी है?`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is it necessary to be a native resident of Chhattisgarh to obtain a caste certificate?`
* **Resolved Hindi Query**: `ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, छत्तीसगढ़ का मूल निवासी प्रमाण पत्र ओबीसी प्रमाण पत्र बनाने के लिए अनिवार्य नहीं है।
  > 
  > स्रोत दस्तावेजों के अनुसार, मूल निवासी प्रमाण पत्र को सहायक दस्तावेजों में सूचीबद्ध किया गया है, लेकिन यह अनिवार्य (Mandatory) नहीं है। अन्य सहायक दस्तावेज जैसे वार्ड सदस्य/स्थानीय विधायक/सांसद से प्रमाण पत्र, भूमि/घर का दस्तावेज, राशन कार्ड, बिजली का बिल, जन्म प्रमाण पत्र, जन्म सूचना प्रपत्र, पिता/अभिभावक की सेवा प्रमाण पत्र/पहचान पत्र, अनैच्छिक प्रवजन का आदेश, शपथ पत्र, आय प्रमाण, अन्य पिछड़ा वर्ग का प्रमाण, वंशावली, और ग्राम सभा प्रस्ताव (ग्रामीण क्षेत्रों के लिए) भी सहायक दस्तावेजों के रूप में उपयोग किए जा सकते हैं।
  > 
  > ओबीसी प्रमाण पत्र के लिए निवास का प्रमाण अनिवार्य है, लेकिन यह विभिन्न दस्तावेजों के माध्यम से सिद्ध किया जा सकता है, जिनमें मूल निवासी प्रमाण पत्र भी शामिल है, लेकिन यह अनिवार्य नहीं है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?"
       ```
     * **Response**:
       ```json
       ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?"
       ```
     * **Response**:
       ```json
       Is it necessary to be a native resident of Chhattisgarh to obtain a caste certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the requirement for an OBC certificate in Chhattisgarh?', 'topic_summary': 'User is asking about the eligibility criteria for an OBC certificate in Chhattisgarh.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '3', 'service_id': '5'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- OBC RESIDENCY/DOMICILE RULE: If the citizen asks about Domicile or Residence rules/requirements for the OBC Certificate, explain clearly based on the context:\n  1. A Domicile Certificate (मूल निवासी प्रमाण पत्र) is NOT mandatory (it is listed as one of several optional supporting documents under 'Residential Proof').\n  2. To satisfy the residency requirement for the OBC Certificate, the applicant or their ancestors must have been residing in the geographical limits of Chhattisgarh since or before the OBC notification date, which is December 26, 1984 (२६ दिसम्बर १९८४).\n  3. List the alternative supporting documents for Residential Proof (such as Land/House documents, Ration Card, Electricity Bill, Ward Member/MLA/MP certificate, Birth Certificate).\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: OBC Certificate\nService ID: 5\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 2: Land And House Document\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Electricity Bill\n  * Supporting Document 5: Domicile Certificate\n  * Supporting Document 6: Birth Certificate\n  * Supporting Document 7: Birth Information Form\n  * Supporting Document 8: Service Certificate / Identity Card Of Father / Guardian\n  * Supporting Document 9: Order Of Involuntary Migration\n- SNo 2: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 3: Income Proof (Mandatory: Yes)\n  * Supporting Document 1: Certificate From Patwari/Sarpanch/Parshad\n  * Supporting Document 2: Income Certificate Employer/Form 16\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Income From Land/House\n  * Supporting Document 5: Other Documents\n  * Supporting Document 6: Application Form\n- SNo 4: Obc Proof (Mandatory: Yes)\n  * Supporting Document 1: Educational Certificate\n  * Supporting Document 2: Transfer Certificate Of Primary School Education\n  * Supporting Document 3: Obc Certificate Of Father\n  * Supporting Document 4: Obc Certificate From Sarpanch / Parshad\n  * Supporting Document 5: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 6: Misal\n  * Supporting Document 7: Adhikar Abhilekh\n  * Supporting Document 8: Jamabandi\n  * Supporting Document 9: Census Register Of 1931\n  * Supporting Document 10: Citizen Register Of 1949\n  * Supporting Document 11: Dakhil / Kharij Panji\n  * Supporting Document 12: Disability / Unavailability Proof\n- SNo 5: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 6: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 7: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste OBC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (\n\n--- Source 2: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ीं है।\n\n--- Page 14 ---\nचरण 9: पावर्ी सुरक्षिर् रखना \nआवेिन सफलतापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक िेखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट लेकर सुरलित रखें। \n \nचचत्र क्रमांक 20: पावर्ी एवं आवेदन संदभा क्रमांक \nआवेदन संदभा क्रमांक की सहायता से आवेिन की स्थस्थगत छत्तीसगढ़ ई-निस्ट्रिक्ट क े  पोटटल पर िेखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेिन जमा करने क े  बाि ननर्ाटररत 22 क्रिऩों की समय-सीमा क े  अ ं िर आवेिन का ननराकरण कर क्रिया जाता है। \n• ई-निस्ट्रिक्ट पोटटल पर आवेिन की स्थस्थगत िेखी जा सकती है। \n• अन्य क्रपछडा वगट प्रमाण पत्र जारी होने क े  उपरांत इसकी निजजटल प्रगत ई-निस्ट्रिक्ट पोटटल से िाउनलोि की जा सकती है।\n\n--- [Document: 5_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of\n\n--- Source 3: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �स्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 4: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉपगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉपगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: नवीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉपगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉपगन प्रपक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासविा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉपगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.2: खोजें पर क्लिक करें। \nचरण 3.3: सेवाओं की सूची खुलेगी। इसमें अन्य पपछडा वगा प्रमाण पत्र िेखें।  \nचरण 3.4: यक्रि यह सेवा सूची में शागमल नहीं है तो ऊपर क्रिए गए होम बटन पर क्लिक करें। ननम्नानुसार पेज \nखुलेगा। \n \nचचत्र क्रमांक 7: उपयोगकर्ाा होम पेज \nचरण 3.5: इस पेज पर “सभी सेवाए ँ  देखें” पर क्लिक करें। सेवाओं की\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अन्य पिछड़ा वर्ग प्रमाण पत्र\nService ID: 5\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 2: घर या भूमि का दस्तावेज़\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: बिजली का बिल\n  * Supporting Document 5: मूल निवासी प्रमाण पत्र\n  * Supporting Document 6: जन्म प्रमाण पत्र\n  * Supporting Document 7: जन्म सूचना प्रपत्र\n  * Supporting Document 8: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 9: अनैच्छिक प्रवजन का आदेश\n- SNo 2: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 3: आय प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: पटवारी/सरपंच/पार्षद से प्रमाण पत्र\n  * Supporting Document 2: नियोक्ता का आय प्रमाण पत्र/फार्म १६\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: भूमि/घर से आय\n  * Supporting Document 5: अन्य\n  * Supporting Document 6: आवेदन प्रपत्र\n- SNo 4: अन्य पिछड़ा वर्ग का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: शैक्षणिक प्रमाण - पत्र\n  * Supporting Document 2: प्राथमिक स्कूल शिक्षा के प्रमाण पत्र के लिए स्थानांतरण\n  * Supporting Document 3: पिता का अ.पि.व. प्रमाण पत्र\n  * Supporting Document 4: सरपंच / पार्षद से ओबीसी प्रमाणपत्र\n  * Supporting Document 5: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 6: मिसल\n  * Supporting Document 7: अधिकार अभिलेख\n  * Supporting Document 8: जमाबंदी\n  * Supporting Document 9: १९३१ का जनगणना पंजी\n  * Supporting Document 10: 1949 का नागरिक पंजी\n  * Supporting Document 11: दाखिल / ख़ारिज पंजी\n  * Supporting Document 12: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 5: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 6: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document 1: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए)\n- SNo 7: मध्यप्रदेश पुनर्गठन अधिनियम 2000(क्रमांक २६-सन २००० की धारा ६७ के अधीन छ. ग. राज्य संवर्ग आबंटन ) का प्रम\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ूप 3 घ\n[ नियम १६८२) देखिये ]\nकार्यालय जिला स्तरीय प्रमाणपत्र सत्यापन समिति जिला \"+-+k677+ छत्तीसगढ़ दिनाक आवेंदन पत्र की पावती\nआवक क्रमांक\nइस ज्ञाघन की मूल प्रति आवेदक को प्रदत्त की जावे तथा उसका प्रतिपर्ण कार्यालय में संधारित किया जावे)\nआज दिनांक कोश्री / श्रीमती / कुमारी अत्मज _ आसना व्यवसाय निवासी तहसाल जिला रम्य से सामाजिक प्रास्थिति प्रमाण पत्र सत्यापित्त करने हेतु आवेदन पत्र प्राप्त किया॰गया है॰ उक्त आदेदन पत्र के साथ निन्नांकित अभिलेख मूल / अभिप्रमाणित प्रति ऐं प्राप्त हुए है ४४ आवेदक अथवा आवेदक क पिता / पूर्दजों का निम्नांकित दस्तावेज जिसमें उसकी जाति अंकित है पूर्वजों क राजस्व दस्तावेज गिसल जमाबंदी सर्वेक्षण गिरदावरीः 8 आष्चयक बरंद बसमनिलेख (१९५४): जनगणना १९३१ ; छः दन विभाग को जमाबंदीः नागरिकों का राष्ट्रीय रजिस्टर १९४९ ; जन्म या मृत्यु की पंजीः ३ पिता अथदा पूर्वज क शिक्षित होने की स्थित्ति में॰ प्रवेश दाखि़ल / खारिज पंजी पिता पूर्वज अथग संबंधी नातेदार को पूर्व में जारी जाति प्रमाण प्रमाण पत्र की प्रति अन्यं दस्तावेज जिससे आवेदक क द्वारा दावा की गई जाति होना प्रगाणित होत्ता है दारह\n!2; ऐसे दस्तावज अथवा दस्तवेजों को सम्यक रूप से अभिप्रमाणित प्रतिलेिपि अथवा प्रलिलिपियॉ चिससे यह प्रमाणत हा सके कं आवंदक के पूवेज राष्ट्रपतीय अघेसूंचनाः नतिथि अथव अन्य पिेछड़ा वग़ को अघिसूचना तिथि ऊं पूर्व से छत्तीसगढ़ की भौगोलिक सीमा में निवांस करते थे। ` पूर्वजों से परंभ फर शापेदफ तावः पच्यारी से प्रदता नंशावली । आवदकं अथवा उसक पेता अथवा उसदः वैध पालक का शय२ प= प्ररूप २क क अनुस्तार मूल प्रति में दस्तावंज फ़िनत्ते नर्शित हा कि आवदक क पिता सज्य सरकार के अधकारी / फ॰ ारी हैं तथ राष्ट्रपत्तीय अधेसूचन\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ल निवास प्रमाण+पत्र अथचा अन्य कोई भी अभिलेख जिससे प्रमाणित हो सक कि आवदक क पूर्वज दिनांक 10 /08 /1550 अनु.जा.) 06 /09 / 1९५0 अनुःज.जा ) अथवा २६ / १२ / १९८४ अपि.व.॰॰ क पूर्व रे छत्तीसगढ़ की भौगोलिक सीमा के मूल निवासी थे। पूर्वजों से प्रारंभ कर जाति प्रमाणम्पत्र धारक तक पटवारी से प्रदत्त वंशावली । आवेदक क पिता यदि राज्य सरकार / केन्द्र सरकार केः कर्मचारी हैं / थे तथा अनु.जा. / अनु.ज.जा. / अ. पि.व क संबंध मं ंदिनांक 10 /08 /1950, 06 / 09 / 1950. 26 /12 /1984 के पूर्व वर्तमान नध्यप्रदश राज्य क्षेत्र के निवासी थे और राप्य पुनर्गठन क फलस्चरूप उन्हें छत्तीसगढ़ रज्य आवंटित हुआ है / था. संबंधी दस्तावेज यदि आवेदंक अपिव॰ से संबंधित है ततथा उसके पिता / माता शासकीय कर्मचारी है तों उनक पद एवं आय की पुष्टि से संबंधित अभिलेख एवं॰ आय प्रमाण-् पत्र अथवा पूर्व वित्तीय वर्ष के फार्म १६ को प्रति\nहॉ / नहों\n3\nहॉ / नहीं\nहॉ / नहीं\n5\nहॅॉ / नर्हीं\n6\nअवेदक का पूर्ण एवं सष्ट गत्ता लिखा हुआ लिफाफा जिसमें पर्याप्त डाक डटिकट लगी हा. प्रमाण-्पत्र क नामले में डाक क माध्यम से वांछित हं\nहॅ / नहीं\nआवंदक का शपथ पत्र प्रारूप 2 अ क अनुस्ाए\nहॅ /र्फी\nमैं शपथ घूर्वक कथन करता हूँ॰ कि इस आवेदन में मरे द्वारा प्रस्तुत को गईं समस्त जानकारी मेरे सर्वोत्तम ज्ञान के अनुसार र्त्य एवं सही है।\nस्थान\nदिनक\nभददीय\nआवेदक के हस्ताक्षर\n\n--- Page 23 (no rotation needed) ---\nछत्तीसगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\n788 (21)\nप्ररूप 2 क\n( नियमं ३३) (क देखियं ]\nसामाजिक प्रास्थिति प्रमाणपत्र जारी करने हेतु शपथ पत्र\nमैं श्री / श्रीमती / कुमारी आत्मज / आत्मजा उम्र वर्ष व्यवसाय निवास त्तहसाल जिला र््य एतदद्वारा शपथपूर्वक निम्नलिखित कथनं करता / करती हूॅ कि .-~\nछायाचित्र\nआवदक क हस्ताकर\nमेरेद्वारा कम प्र\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ोंता है आवेदक की जाति में माता क गाई मामा क लड़के / लड़कीं कं साथ क्या वैवाहिक संबंध होता है आवेदक कीं जाति गें वया वधु मूल्य प्रथा प्रचलितं है\n१४\n१९\n२०\n21\n2\n२३\nआवेदक की जाति में क्शा दहेज प्रथा प्रचलित है\n24\nआवेदंक की॰ जाति / गोत्र के साथ जिन जातियों / गोत्र का वैवाहिक संनंच ढता है॰ उनके नाम\n\n--- Page 21 (no rotation needed) ---\nछत्तीसगढ़ राजपंत्र दिनांक 2 सितम्बां २०१३\n788 .( ११ )\n2५\nआवेदक की जाति से जिन ज़ातियों का रोटी खान- पान) संबंध हैउन जातियों का नाम आवेदक की जाति की समकक्ष जातियों का नाम\n2५\n2७\nआवेदक का धर्म.\n28:\nआवेदक के पिता का धर्म\n२९. आवेदकं के संबंधियों रिश्तेदारों का विवरण\nस.क.\nविवरण\nपिता क भाई माता क भाई मात्ता र्कः बहन पिता की बहन चाचा मामा का पसि का पति फूफा मौसा\nपत्नी का पिता ससुर\n2 नाम\n15\n2\nजाति\n3.\nउपजाति\n5\nव्ययसाय\n6\nनिवास के ग्राम / शहर तहसील\n8\nजल\n३०. संलग्न दस्तावेज आवेदक के पिता / पूर्वजों का निम्नांकितं अभिलेख जिसमें उनकीं जाति अंकित हा क पूर्वजों के मिसल अभिलेख कस फाईल ख जमाबंदी सर्व गिरदावरी बी 1 ग राज्य बंदोबस्तः अथवा घ अधिकार अभिलेख १९५४ ; अथवा वन विभाग की जमाबंद / वन अधिकारपत्रः अथवा च शैक्षणिक संस्था क दाखि़ल खारिज पंजीः अथवा छ जन्म या मृत्यु पंजीः अथवा ज नागरिकों का राष्ट्रीय रजिस्टर १९४९ ः अथवा\n:1::\n\n--- Page 22 (no rotation needed) ---\n788`(20)\nछत्तीसगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\nझ\nपिता पूर्वज अथवा संबंधी को पूर्व में जारी जाति प्रमाण्पत्र की प्रति ; अथवा\nअ\nजनगणना १५३१\n२\nमूल निवास प्रमाण+पत्र अथचा अन्य कोई भी अभिलेख जिससे प्रमाणित हो सक कि आवदक क पूर्वज दिनांक 10 /08 /1550 अनु.जा.) 06 /09 / 1९५0 अनुःज.जा ) अथवा २६ / १२ / १९८४ अपि.व.॰॰ क पूर्व रे छत्तीसगढ़ की भौगोलि�\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "ओबीसी प्रमाण पत्र बनाने के लिए छत्तीसगढ़ का मूल निवासी प्रमाण पत्र होना जरूरी है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, छत्तीसगढ़ का मूल निवासी प्रमाण पत्र ओबीसी प्रमाण पत्र बनाने के लिए अनिवार्य नहीं है।
       
       स्रोत दस्तावेजों के अनुसार, मूल निवासी प्रमाण पत्र को सहायक दस्तावेजों में सूचीबद्ध किया गया है, लेकिन यह अनिवार्य (Mandatory) नहीं है। अन्य सहायक दस्तावेज जैसे वार्ड सदस्य/स्थानीय विधायक/सांसद से प्रमाण पत्र, भूमि/घर का दस्तावेज, राशन कार्ड, बिजली का बिल, जन्म प्रमाण पत्र, जन्म सूचना प्रपत्र, पिता/अभिभावक की सेवा प्रमाण पत्र/पहचान पत्र, अनैच्छिक प्रवजन का आदेश, शपथ पत्र, आय प्रमाण, अन्य पिछड़ा वर्ग का प्रमाण, वंशावली, और ग्राम सभा प्रस्ताव (ग्रामीण क्षेत्रों के लिए) भी सहायक दस्तावेजों के रूप में उपयोग किए जा सकते हैं।
       
       ओबीसी प्रमाण पत्र के लिए निवास का प्रमाण अनिवार्य है, लेकिन यह विभिन्न दस्तावेजों के माध्यम से सिद्ध किया जा सकता है, जिनमें मूल निवासी प्रमाण पत्र भी शामिल है, लेकिन यह अनिवार्य नहीं है।
       ```
| 5 | `शादी प्रमाणपत्र में नाम सुधार कैसे करें?` | 201 | 201 | ✅ MATCH | new_topic | 4.91s |

### Query 5 Details
* **Query**: `शादी प्रमाणपत्र में नाम सुधार कैसे करें?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to correct name in marriage registration and certificate?`
* **Resolved Hindi Query**: `विवाह पंजीकरण एवं प्रमाण पत्र में नाम सुधार कैसे करें?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > विवाह पंजीकरण और प्रमाण पत्र में नाम सुधार करने के लिए, आपको निम्नलिखित चरणों का पालन करना होगा:
  > 
  > 1. **नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)**:
  >    - यह सेवा नाम परिवर्तन के लिए राजपत्र अधिसूचना जारी करने हेतु है।
  >    - शुल्क: 30 रुपये (ऑनलाइन या कियोस्क पर)।
  > 
  > 2. **आवश्यक दस्तावेज**:
  >    - 430 रुपये का भारतीय स्टेट बैंक का चालान (अनिवार्य)।
  >    - 50 रुपये के नॉन-ज्यूडिशियल स्टाम्प पेपर पर नोटराइज्ड शपथ पत्र (अनिवार्य)।
  >    - स्थानीय समाचार पत्र में नाम परिवर्तन की सूचना का प्रकाशन (अनिवार्य)।
  >    - दो गवाहों के विवरण के साथ मूल प्रपत्र (अनिवार्य)।
  >    - पुराना नाम और नया नाम सत्यापन दस्तावेज (अनिवार्य)।
  >    - शपथ पत्र में उल्लिखित सभी दस्तावेजों की प्रतियां (अनिवार्य)।
  >    - आवेदक का पहचान पत्र (अनिवार्य)।
  >    - गवाहों का पहचान पत्र (अनिवार्य)।
  > 
  > 3. **आवेदन प्रक्रिया**:
  >    - Sewa Setu पोर्टल पर आवेदन करें।
  >    - फॉर्म में सभी आवश्यक विवरण भरें।
  >    - आवश्यक दस्तावेज अपलोड करें।
  >    - शुल्क का भुगतान करें।
  > 
  > 4. **समय सीमा**:
  >    - सेवा की समय सीमा 29 दिन है।
  > 
  > 5. **संपर्क**:
  >    - Sewa Setu केंद्र से संपर्क करें।
  > 
  > यह प्रक्रिया केवल नाम सुधार के लिए है, नए प्रमाण पत्र या पंजीकरण के लिए नहीं। यदि आपको विवाह प्रमाण पत्र में नाम सुधार करना है, तो यह सेवा सीधे लागू नहीं होती। आपको संबंधित विभाग से संपर्क करना होगा।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "विवाह पंजीकरण एवं प्रमाण पत्र में नाम सुधार कैसे करें?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "विवाह पंजीकरण एवं प्रमाण पत्र में नाम सुधार कैसे करें?"
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण एवं प्रमाण पत्र में नाम सुधार कैसे करें?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "विवाह पंजीकरण एवं प्रमाण पत्र में नाम सुधार कैसे करें?"
       ```
     * **Response**:
       ```json
       How to correct name in marriage registration and certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "विवाह पंजीकरण एवं प्रमाण पत्र में नाम सुधार कैसे करें?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'How to do marriage registration and name correction in certificates?', 'topic_summary': 'User is asking about two different government services: marriage registration and name correction in certificates.'}
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "विवाह पंजीकरण एवं प्रमाण पत्र में नाम सुधार कैसे करें?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण और प्रमाण पत्र में नाम सुधार करने के लिए, आपको निम्नलिखित चरणों का पालन करना होगा:
       
       1. **नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)**:
          - यह सेवा नाम परिवर्तन के लिए राजपत्र अधिसूचना जारी करने हेतु है।
          - शुल्क: 30 रुपये (ऑनलाइन या कियोस्क पर)।
       
       2. **आवश्यक दस्तावेज**:
          - 430 रुपये का भारतीय स्टेट बैंक का चालान (अनिवार्य)।
          - 50 रुपये के नॉन-ज्यूडिशियल स्टाम्प पेपर पर नोटराइज्ड शपथ पत्र (अनिवार्य)।
          - स्थानीय समाचार पत्र में नाम परिवर्तन की सूचना का प्रकाशन (अनिवार्य)।
          - दो गवाहों के विवरण के साथ मूल प्रपत्र (अनिवार्य)।
          - पुराना नाम और नया नाम सत्यापन दस्तावेज (अनिवार्य)।
          - शपथ पत्र में उल्लिखित सभी दस्तावेजों की प्रतियां (अनिवार्य)।
          - आवेदक का पहचान पत्र (अनिवार्य)।
          - गवाहों का पहचान पत्र (अनिवार्य)।
       
       3. **आवेदन प्रक्रिया**:
          - Sewa Setu पोर्टल पर आवेदन करें।
          - फॉर्म में सभी आवश्यक विवरण भरें।
          - आवश्यक दस्तावेज अपलोड करें।
          - शुल्क का भुगतान करें।
       
       4. **समय सीमा**:
          - सेवा की समय सीमा 29 दिन है।
       
       5. **संपर्क**:
          - Sewa Setu केंद्र से संपर्क करें।
       
       यह प्रक्रिया केवल नाम सुधार के लिए है, नए प्रमाण पत्र या पंजीकरण के लिए नहीं। यदि आपको विवाह प्रमाण पत्र में नाम सुधार करना है, तो यह सेवा सीधे लागू नहीं होती। आपको संबंधित विभाग से संपर्क करना होगा।
       ```
| 6 | `एसटी प्रमाण पत्र के दस्तावेजों में निवास प्रमाण पत्र लगता है क्या?` | 4 | 4 | ✅ MATCH | new_topic | 2.97s |

### Query 6 Details
* **Query**: `एसटी प्रमाण पत्र के दस्तावेजों में निवास प्रमाण पत्र लगता है क्या?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "एसटी प्रमाण पत्र के दस्तावेजों में मूल निवासी प्रमाण पत्र लगता है क्या?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "एसटी प्रमाण पत्र के दस्तावेजों में मूल निवासी प्रमाण पत्र लगता है क्या?"
       ```
     * **Response**:
       ```json
       एसटी प्रमाण पत्र के दस्तावेजों में मूल निवासी प्रमाण पत्र लगता है क्या?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "एसटी प्रमाण पत्र के दस्तावेजों में मूल निवासी प्रमाण पत्र लगता है क्या?"
       ```
     * **Response**:
       ```json
       Is the original certificate required in the documents for the ST certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "एसटी प्रमाण पत्र के दस्तावेजों में मूल निवासी प्रमाण पत्र लगता है क्या?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What are the documents required for a caste certificate in Chhattisgarh?', 'topic_summary': 'User is asking about documents for a caste certificate, which is a different service from the general government services discussed in the history.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "एसटी प्रमाण पत्र के दस्तावेजों में मूल निवासी प्रमाण पत्र लगता है क्या?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
| 7 | `निवास प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?` | 7 | 7 | ✅ MATCH | new_topic | 4.21s |

### Query 7 Details
* **Query**: `निवास प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Do I need a caste certificate for an original certificate?`
* **Resolved Hindi Query**: `मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र अनिवार्य नहीं है।
  > 
  > मूल निवासी प्रमाण पत्र के लिए निम्नलिखित अनिवार्य दस्तावेज हैं:
  > 1. शपथ पत्र (अनिवार्य)
  > 2. निवास का प्रमाण (अनिवार्य) - जिसमें जन्म प्रमाण पत्र, पिता/पालक का सेवा प्रमाण पत्र, वोटिंग कार्ड, राशन कार्ड, बिजली का बिल आदि शामिल हैं।
  > 3. शैक्षणिक प्रमाण पत्र (अनिवार्य) - जिसमें 8वीं कक्षा, 5वीं कक्षा, 10वीं कक्षा, 12वीं कक्षा के अंकपत्र शामिल हैं।
  > 
  > जाति प्रमाण पत्र (जैसे एससी/एसटी प्रमाणपत्र) मूल निवासी प्रमाण पत्र के लिए आवश्यक दस्तावेज नहीं है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?"
       ```
     * **Response**:
       ```json
       मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?"
       ```
     * **Response**:
       ```json
       Do I need a caste certificate for an original certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- ELIGIBILITY LOGIC RULE (Domicile): If a citizen asks about eligibility or exceptions for the Domicile Certificate, explain the rules strictly:\n  1. Main Path (Both Criteria One AND Criteria Two must be met): The applicant must satisfy AT LEAST ONE option from Criteria One (Criteria A) AND AT LEAST ONE option from Criteria Two (Criteria B).\n     * You MUST list Criteria One and Criteria Two under separate, clearly-labeled headers or bullet points.\n     * Criteria One (Criteria A) options: Birth in CG, parent resident for 25 years, parent is CG Government/PSU employee, or property in CG for 5 years.\n     * Criteria Two (Criteria B) options: 3 years of school study in CG, or passing Class 5, 8, 10, 12 board exam from CG.\n     * Never merge them into one list or omit the education requirements of Criteria Two.\n  2. Exceptions (Criteria Three / Criteria C): If they do not meet the Main Path (for example, if they lack 'Proof of 15 Years Stay' or did not study in CG), they can still get a Domicile Certificate under the exceptions of Criteria Three (C). For Criteria Three (C), Criteria A and B are NOT required. The exceptions are: (a) spouse is a domicile of CG, (b) applicant or spouse is a CG Government/PSU employee, or (c) applicant or parent is in All India Services and allotted CG Cadre.\n  3. Clarity: Never state that Criteria Three requires stay proof or education. Clearly explain that Criteria Three is a standalone set of exceptions that bypasses the need for the stay proof or CG education requirements of Criteria One and Two.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Domicile Certificate\nService ID: 7\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 7 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: Other (Mandatory: No)\n  * Supporting Document 1: Other Documents\n- SNo 3: Proof Of At Least 15 Years Stay (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate\n  * Supporting Document 2: Father/ Guardian Service Certificate\n  * Supporting Document 3: Job Service Certificate / Identity Card (If The Applicant Is Under Govt./Semi Govt.)\n  * Supporting Document 4: Voters Identity Card\n  * Supporting Document 5: Land And House Document\n  * Supporting Document 6: Birth Information Form\n  * Supporting Document 7: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 8: Ration Card\n  * Supporting Document 9: Electricity Bill\n- SNo 4: Educational Certificate (Mandatory: Yes)\n  * Supporting Document 1: Middle School Certificate - 8th Standard\n  * Supporting Document 2: Primary School Certificate - 5th Standard\n  * Supporting Document 3: High School(10th) Certificate\n  * Supporting Document 4: Higher Secondary School Certificate(12th)\n  * Supporting Document 5: M.Phil/D.Lit./Ph.D. Certificate\n  * Supporting Document 6: School Certificate (As A Proof Of 3 Years Continuous Study)\n  * Supporting Document 7: Post Graduation Certificate\n  * Supporting Document 8: Certificate In Technical Subjects\n- SNo 5: Proof Of At Least 5 Years Stay (Mandatory: No)\n  * Supporting Document 1: Land And House Document\n  * Supporting Document 2: Persons Service Book.\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Guardians Occupation of Beneficiary [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: Beneficiary place of Birth [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: Address Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 7, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: section lebel, Data: Charactar] (Row: 8, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: fieldset, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Beneficiary Details of Business or Service [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Beneficiary Details of Business or service [Type: fieldset, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Beneficiary Education Level [Type: section lebel, Data: Charactar] (Row: 12, Col: 1)\n- Field: Beneficiary Education Level [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Have Beneficiary Voter Id [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: District Name of Beneficiary [Type: drop down, Data: Charactar] (Row: 15, Col: 2)\n- Field: Living From in Years [Type: number, Data: Date] (Row: 16, Col: 1)\n- Field: Reason for application Domicile [Type: text, Data: Charactar] (Row: 16, Col: 2)\n- Field: Any other detail [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 17, Col: 2)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 7_en_7.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nउपयोगकर्ता मतगादर्शिकत \n \n  \nमूल निवतसी प्रमतण पत्र क े  र्लए ई-निस्ट्रिक्ट पोर्ाल पर ऑिलतइि आवेदि प्रक्रियत \n \nछत्तीसगढ़ इन्फोर्ेक प्रमोशि सोसतयर्ी\n\n--- Page 2 ---\nववषय सूची \nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर\n\n--- Source 2: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �िगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह पेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 3: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: 4.4: डनर्ाटररत बॉक्स पर क्लिक करक े  आर्ार प्रमाणीकरण हेतु सहमगत िें। \nचरण 4.5: “Authentication”  बटन पर क्लिक करें। \nचरण 4.6: आर्ार ई-प्रमाणीकरण क े  बाि “जमत करें” बटन पर क्लिक करें।  \nडनम्नानुसार पॉप-अप गविंिो खुलेगा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पू�\n\n--- Source 4: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पूवतावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचरण 7.2: घोषणत: घोर्षणा हेतु डनर्ाटररत बॉक्स पर क्लिक करें। \nचरण 7.3: घोर्षणा पर क्लिक करते ही “जमत करें” बटन दिखाई िेगा, इस पर क्लिक करें, इस तरह आवेिन \nजमा हो जाएगा। \n \nचित्र क्रमांक 19\n\n--- Page 15 ---\nचरण 8: शुल्क कत भुगर्ति \nइस पेज पर लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवा शुल्क एवं स्क ै डनिंग शुल्क का गववरण िेख सकते \nहैं। \n \nचित्र क्रमांक 15 \n \nचरण 8.1: डनर्ाटररत शुल्क का भुगतान करें। \nचरण 8.2: भुगतान क े  पश्चात् “जमत करें” बटन पर क्लिक करें। \n \nिोर्: \n• लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवत शुल्क रु. 30 डनर्ाटररत हैं। \n• सेवा शुल्क में  पताँच दस्ततवेज़़ों तक स्क ै डनिंग का शुल्क भी शागमल है। अगतररक्त िस्तावेज़़ों की स्क ै डनिंग का शुल्क पृथक से \nलोकसेवा क ें द्र/ सीएससी/डकयोस्क संिालक द्वारा ललया जा सकता है।\n\n--- Page 16 ---\nचरण 9: पतवर्ी सुरक्षिर् रखित \nआवेिन जमा करते ही चित्रानुसार पावती जेनरेट हो जाती है।  \nइस पावती में “आवेदि संदभा िमतंक” प्रिचशित होता है। \nभगवष्य की आवश्यकताओं और आवेिन की स्थिगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: मूल निवासी प्रमाण पत्र\nService ID: 7\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 7 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य\n- SNo 3: १५ वर्ष तक निवास का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: जन्म प्रमाण पत्र\n  * Supporting Document 2: पिता/पालक का सेवा प्रमाण पत्र\n  * Supporting Document 3: नौकरी प्रमाणपत्र /पहचान पत्र (यदि आवेदक शासकीय /अर्ध शासकीय अधीनस्थ हो )\n  * Supporting Document 4: वोटिंग कार्ड\n  * Supporting Document 5: घर या भूमि का दस्तावेज़\n  * Supporting Document 6: जन्म सूचना प्रपत्र\n  * Supporting Document 7: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 8: राशन कार्ड\n  * Supporting Document 9: बिजली का बिल\n- SNo 4: शैक्षणिक प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: माध्यमिक विद्यालय का प्रमाणपत्र -8 कक्षा\n  * Supporting Document 2: प्राथमिक विद्यालय का प्रमाणपत्र - 5वीं कक्षा\n  * Supporting Document 3: हाई स्कूल(10वी कक्षा) अंकसूची\n  * Supporting Document 4: उच्चतर माध्यमिक विधालय प्रमाण पत्र(१२ वीं कक्षा)\n  * Supporting Document 5: एम-फिल\n  * Supporting Document 6: स्कूल प्रमाणपत्र (3 साल की एक सबूत निरंतर अध्ययन के रूप में)\n  * Supporting Document 7: स्नातकोत्तर प्रमाणपत्र\n  * Supporting Document 8: तकनीकी विषयों में प्रमाणपत्र\n- SNo 5: ५ साल निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: घर या भूमि का दस्तावेज़\n  * Supporting Document 2: व्यक्ति की सेवा पुस्तिका.\n\nAPPLICATION FORM FIELDS:\n- Field: सामान्य विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: हितग्राही के अभिभावक का प्रकार [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: हितग्राही के अभिभावक का नाम [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: हितग्राही के अभिभावक का व्यवसाय [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: हितग्राही का जन्म स्थान [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: लिंग [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: पता का विवरण [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: पता [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: पिन कोड [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: जिला [Type: drop down\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_hi_citizenCharter.pdf (SLA_DETAILS)] ---\nछत्तीसगढ़ शासन\nराजस्व एवं आपदा प्रबंधन विभाग\nमंत्रालय\nमहानदी भवन नया रायपुर\n::: अधिसूचना :::\n\nरायपुर, दिनांक 16/05/2013\n\nक्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\nसारणी (SLA Details):\n1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n2. स्थाई जाति प्रमाण-पत्र (Permanent Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - सक्षम प्राधिकारी: कलेक्टर\n   - अपीलीय अधिकारी: कमिश्नर\n\n3. निवास प्रमाण-पत्र (Domicile Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्र\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: �ीय अधिकारी (राजस्व)\n   - सक्षम प्राधिकारी: कलेक्टर\n   - अपीलीय अधिकारी: कमिश्नर\n\n3. निवास प्रमाण-पत्र (Domicile Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n4. आय प्रमाण-पत्र (Income Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\nछत्तीसगढ़ के राज्यपाल के नाम से तथा आदेशानुसार\n(पी. निहलानी)\nसंयुक्त सचिव, छत्तीसगढ़ शासन, राजस्व एवं आपदा प्रबंधन विभाग\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पूवतावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचर\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र चाहिए?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, मूल निवासी प्रमाण पत्र के लिए जाति प्रमाण पत्र अनिवार्य नहीं है।
       
       मूल निवासी प्रमाण पत्र के लिए निम्नलिखित अनिवार्य दस्तावेज हैं:
       1. शपथ पत्र (अनिवार्य)
       2. निवास का प्रमाण (अनिवार्य) - जिसमें जन्म प्रमाण पत्र, पिता/पालक का सेवा प्रमाण पत्र, वोटिंग कार्ड, राशन कार्ड, बिजली का बिल आदि शामिल हैं।
       3. शैक्षणिक प्रमाण पत्र (अनिवार्य) - जिसमें 8वीं कक्षा, 5वीं कक्षा, 10वीं कक्षा, 12वीं कक्षा के अंकपत्र शामिल हैं।
       
       जाति प्रमाण पत्र (जैसे एससी/एसटी प्रमाणपत्र) मूल निवासी प्रमाण पत्र के लिए आवश्यक दस्तावेज नहीं है।
       ```
| 8 | `राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह प्रमाण पत्र अनिवार्य है?` | 201 | 201 | ✅ MATCH | new_topic | 4.27s |

### Query 8 Details
* **Query**: `राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह प्रमाण पत्र अनिवार्य है?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `क्या विवाह पंजीकरण और प्रमाण पत्र राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए अनिवार्य है?`
* **Resolved Hindi Query**: `राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, विवाह प्रमाण पत्र अनिवार्य नहीं है। नाम परिवर्तन के लिए विवाह प्रमाण पत्र की आवश्यकता नहीं होती है। केवल नाम परिवर्तन के लिए आवश्यक दस्तावेज हैं: 430 रुपये का SBI का चालान, नोटराइज्ड शपथ पत्र, स्थानीय समाचार पत्र में सूचना का प्रकाशन, दो गवाहों का विवरण, और पुराने एवं नए नाम का सत्यापन।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?"
       ```
     * **Response**:
       ```json
       राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?"
       ```
     * **Response**:
       ```json
       क्या विवाह पंजीकरण और प्रमाण पत्र राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए अनिवार्य है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the process for marriage registration and certificate for gazette name change?', 'topic_summary': 'User is asking about the process for marriage registration and certificate for gazette name change.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "राजपत्र अधिसूचना (गजट) नाम परिवर्तन के लिए विवाह पंजीकरण एवं प्रमाण पत्र अनिवार्य है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, विवाह प्रमाण पत्र अनिवार्य नहीं है। नाम परिवर्तन के लिए विवाह प्रमाण पत्र की आवश्यकता नहीं होती है। केवल नाम परिवर्तन के लिए आवश्यक दस्तावेज हैं: 430 रुपये का SBI का चालान, नोटराइज्ड शपथ पत्र, स्थानीय समाचार पत्र में सूचना का प्रकाशन, दो गवाहों का विवरण, और पुराने एवं नए नाम का सत्यापन।
       ```
| 9 | `छत्तीसगढ़ निवास प्रमाण पत्र में जाति सत्यापन नियम` | 7 | 7 | ✅ MATCH | new_topic | 2.92s |

### Query 9 Details
* **Query**: `छत्तीसगढ़ निवास प्रमाण पत्र में जाति सत्यापन नियम`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "छत्तीसगढ़ मूल निवासी प्रमाण पत्र में जाति सत्यापन नियम"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "छत्तीसगढ़ मूल निवासी प्रमाण पत्र में जाति सत्यापन नियम"
       ```
     * **Response**:
       ```json
       छत्तीसगढ़ मूल निवासी प्रमाण पत्र में जाति सत्यापन नियम
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "छत्तीसगढ़ मूल निवासी प्रमाण पत्र में जाति सत्यापन नियम"
       ```
     * **Response**:
       ```json
       Caste verification rules in Chhattisgarh domicile certificate
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "छत्तीसगढ़ मूल निवासी प्रमाण पत्र में जाति सत्यापन नियम",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'जाति सत्यापन नियम छत्तीसगढ़ मूल निवासी प्रमाण पत्र के लिए क्या हैं?', 'topic_summary': 'जाति सत्यापन नियम के बारे में जानकारी'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "छत्तीसगढ़ मूल निवासी प्रमाण पत्र में जाति सत्यापन नियम",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
| 10 | `क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके निवास प्रमाण पत्र के लिए आवेदन कर सकती है?` | 7 | 7 | ✅ MATCH | new_topic | 5.57s |

### Query 10 Details
* **Query**: `क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके निवास प्रमाण पत्र के लिए आवेदन कर सकती है?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Can a married woman apply for a domicile certificate using her father's address?`
* **Resolved Hindi Query**: `क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > हाँ, एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है। इसके लिए निम्नलिखित शर्तें लागू हैं:
  > 
  > 1. **मुख्य मार्ग (दोनों मानदंड एक और दो):**
  >    - मानदंड एक (A) के तहत: पिता/पालक का सेवा प्रमाण पत्र या 25 वर्ष का निवास प्रमाण।
  >    - मानदंड दो (B) के तहत: 3 वर्ष की स्कूली शिक्षा या 5वीं, 8वीं, 10वीं, 12वीं कक्षा की बोर्ड परीक्षा का अंकपत्र।
  > 
  > 2. **अपवाद (मानदंड तीन):**
  >    - यदि उपरोक्त मानदंड पूरे नहीं होते हैं, तो भी वह निम्नलिखित के आधार पर प्रमाण पत्र प्राप्त कर सकती है:
  >      - पति का मूल निवासी प्रमाण पत्र।
  >      - आवेदक या पति का सरकारी/अर्ध-सरकारी कर्मचारी होना।
  >      - आवेदक या माता-पिता का अखिल भारतीय सेवा (AIS) में होना और छत्तीसगढ़ कैडर आवंटित होना।
  > 
  > **आवश्यक दस्तावेज:**
  > - शपथ पत्र (अनिवार्य)।
  > - पिता/पालक का सेवा प्रमाण पत्र।
  > - 15 वर्ष के निवास का प्रमाण (जैसे जन्म प्रमाण पत्र, मतदाता पहचान पत्र, बिजली बिल)।
  > - शैक्षिक प्रमाण पत्र (जैसे 10वीं कक्षा का अंकपत्र)।
  > 
  > **आवेदन प्रक्रिया:**
  > 1. ई-डिस्ट्रिक्ट पोर्टल पर पंजीकरण करें।
  > 2. आवेदन पत्र भरें और आवश्यक दस्तावेज अपलोड करें।
  > 3. ई-प्रमाणीकरण (आधार-आधारित) करें।
  > 4. शुल्क का भुगतान करें (ऑनलाइन या कियोस्क पर 30 रुपये)।
  > 
  > **नोट:** यदि पिता का निवास प्रमाण पत्र नहीं है, तो अन्य दस्तावेजों (जैसे मतदाता पहचान पत्र, बिजली बिल) के माध्यम से 15 वर्ष के निवास का प्रमाण प्रस्तुत करना अनिवार्य है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?"
       ```
     * **Response**:
       ```json
       क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?"
       ```
     * **Response**:
       ```json
       Can a married woman apply for a domicile certificate using her father's address?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': "Can a married woman apply for a domicile certificate using her father's address?", 'topic_summary': "Domicile certificate application for a married woman using father's address"}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- ELIGIBILITY LOGIC RULE (Domicile): If a citizen asks about eligibility or exceptions for the Domicile Certificate, explain the rules strictly:\n  1. Main Path (Both Criteria One AND Criteria Two must be met): The applicant must satisfy AT LEAST ONE option from Criteria One (Criteria A) AND AT LEAST ONE option from Criteria Two (Criteria B).\n     * You MUST list Criteria One and Criteria Two under separate, clearly-labeled headers or bullet points.\n     * Criteria One (Criteria A) options: Birth in CG, parent resident for 25 years, parent is CG Government/PSU employee, or property in CG for 5 years.\n     * Criteria Two (Criteria B) options: 3 years of school study in CG, or passing Class 5, 8, 10, 12 board exam from CG.\n     * Never merge them into one list or omit the education requirements of Criteria Two.\n  2. Exceptions (Criteria Three / Criteria C): If they do not meet the Main Path (for example, if they lack 'Proof of 15 Years Stay' or did not study in CG), they can still get a Domicile Certificate under the exceptions of Criteria Three (C). For Criteria Three (C), Criteria A and B are NOT required. The exceptions are: (a) spouse is a domicile of CG, (b) applicant or spouse is a CG Government/PSU employee, or (c) applicant or parent is in All India Services and allotted CG Cadre.\n  3. Clarity: Never state that Criteria Three requires stay proof or education. Clearly explain that Criteria Three is a standalone set of exceptions that bypasses the need for the stay proof or CG education requirements of Criteria One and Two.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Domicile Certificate\nService ID: 7\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 7 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: Other (Mandatory: No)\n  * Supporting Document 1: Other Documents\n- SNo 3: Proof Of At Least 15 Years Stay (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate\n  * Supporting Document 2: Father/ Guardian Service Certificate\n  * Supporting Document 3: Job Service Certificate / Identity Card (If The Applicant Is Under Govt./Semi Govt.)\n  * Supporting Document 4: Voters Identity Card\n  * Supporting Document 5: Land And House Document\n  * Supporting Document 6: Birth Information Form\n  * Supporting Document 7: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 8: Ration Card\n  * Supporting Document 9: Electricity Bill\n- SNo 4: Educational Certificate (Mandatory: Yes)\n  * Supporting Document 1: Middle School Certificate - 8th Standard\n  * Supporting Document 2: Primary School Certificate - 5th Standard\n  * Supporting Document 3: High School(10th) Certificate\n  * Supporting Document 4: Higher Secondary School Certificate(12th)\n  * Supporting Document 5: M.Phil/D.Lit./Ph.D. Certificate\n  * Supporting Document 6: School Certificate (As A Proof Of 3 Years Continuous Study)\n  * Supporting Document 7: Post Graduation Certificate\n  * Supporting Document 8: Certificate In Technical Subjects\n- SNo 5: Proof Of At Least 5 Years Stay (Mandatory: No)\n  * Supporting Document 1: Land And House Document\n  * Supporting Document 2: Persons Service Book.\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Guardians Occupation of Beneficiary [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: Beneficiary place of Birth [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: Address Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 7, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: section lebel, Data: Charactar] (Row: 8, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: fieldset, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Beneficiary Details of Business or Service [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Beneficiary Details of Business or service [Type: fieldset, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Beneficiary Education Level [Type: section lebel, Data: Charactar] (Row: 12, Col: 1)\n- Field: Beneficiary Education Level [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Have Beneficiary Voter Id [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: District Name of Beneficiary [Type: drop down, Data: Charactar] (Row: 15, Col: 2)\n- Field: Living From in Years [Type: number, Data: Date] (Row: 16, Col: 1)\n- Field: Reason for application Domicile [Type: text, Data: Charactar] (Row: 16, Col: 2)\n- Field: Any other detail [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 17, Col: 2)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 7_en_7.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nउपयोगकर्ता मतगादर्शिकत \n \n  \nमूल निवतसी प्रमतण पत्र क े  र्लए ई-निस्ट्रिक्ट पोर्ाल पर ऑिलतइि आवेदि प्रक्रियत \n \nछत्तीसगढ़ इन्फोर्ेक प्रमोशि सोसतयर्ी\n\n--- Page 2 ---\nववषय सूची \nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर\n\n--- Source 2: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: 4.4: डनर्ाटररत बॉक्स पर क्लिक करक े  आर्ार प्रमाणीकरण हेतु सहमगत िें। \nचरण 4.5: “Authentication”  बटन पर क्लिक करें। \nचरण 4.6: आर्ार ई-प्रमाणीकरण क े  बाि “जमत करें” बटन पर क्लिक करें।  \nडनम्नानुसार पॉप-अप गविंिो खुलेगा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पू�\n\n--- Source 3: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �िगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह पेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 4: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ु लॉगगन कर सकते हैं। आपक े  पास पासविट बिलने का गवकल्प भी है।\n\n--- Page 5 ---\nचरण 2: पंजीक ृ र् यूज़र लॉक्रगि \nपंजीक ृ त यूज़सट डनम्न प्रदक्रया द्वारा लॉगगन करें। \n \nचित्र क्रमांक 5 \n \n1. भतषत का ियन करें। \n2. यूज़रिेम िजट करें। \n3. पतसविा िजट करें। \n4. “ओर्ीपी भेजें” पर क्लिक करें। \n5. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n6. लॉक्रगि बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजित खोज \nलॉगगन क े  पश्चात डनम्नानुसार योजना खोज पेज खुलेगा। \n \nचित्र क्रमांक 6 \n \nचरण 3.1: यहााँ डनर्ाटररत बॉक्स में पूछी गई जानकारी िजट करें और “खोजें” बटन पर क्लिक करें। \nचरण 3.2: सेवाओं की सूिी दिखाई िेगी, इसमें “Domicile Certificate” पर क्लिक करें। \nअब डनम्नानुसार पेज दिखाई िेगा। इस पेज पर, नीिे आवश्यक दस्ततवेज़़ों की सूिी िेखी जा सकती है। \n \n \nचित्र क्रमांक 7\n\n--- Page 7 ---\nचित्र क्रमांक 8 \n \nचरण 3.3: चित्र क्रमांक 7 क े  अनुसार प्रिचशित गविंिो में “आगे” बटन दिखाई िेगा, उस पर क्लिक करें।\n\n--- Page 8 ---\nचरण 4: आधतर ई-प्रमतणीकरण \nआर्ार ई-प्रमाणीकरण हेतु इस फॉमट में आवेिक की बुडनयािी जानकारी िजट करें। \n \nचित्र क्रमांक 9 \n \nचरण 4.1: आवेिक एवं दहतग्राही का नाम भरें। ड्रॉप-िाउन ललस्ट से िुनकर कायाटलय का नाम और पूरा पता िजट \nकरें। \nचरण 4.2: प्रमाणीकरण क े  ललए “Aadhaar e-authentication” पर क्लिक करें। डनम्नानुसार पॉप-अप \nगविंिो खुलेगा। \n \nचित्र क्रमांक 10\n\n--- Page 9 ---\nचरण 4.3: प्रमाणीकरण हेतु आर्ार संख्या एवं नाम (आर्ार कािट क े  अनुसार अ ं ग्रेज़ी में) िजट करें। \nचरण 4.4: डनर्ाटररत बॉक्स पर क्लिक करक े  आर्ार प्रमाणीकरण हेतु सहमगत िें। \nचरण 4.5: “Authentication”  बटन पर क्लिक करें। \nचरण 4.6: आर्ार ई-प्रमाणीकरण क े  बाि “जमत करें” बटन पर क्लिक करें।  \nडनम्नानुसार पॉप-अप गविंिो खुले�\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: मूल निवासी प्रमाण पत्र\nService ID: 7\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 7 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य\n- SNo 3: १५ वर्ष तक निवास का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: जन्म प्रमाण पत्र\n  * Supporting Document 2: पिता/पालक का सेवा प्रमाण पत्र\n  * Supporting Document 3: नौकरी प्रमाणपत्र /पहचान पत्र (यदि आवेदक शासकीय /अर्ध शासकीय अधीनस्थ हो )\n  * Supporting Document 4: वोटिंग कार्ड\n  * Supporting Document 5: घर या भूमि का दस्तावेज़\n  * Supporting Document 6: जन्म सूचना प्रपत्र\n  * Supporting Document 7: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 8: राशन कार्ड\n  * Supporting Document 9: बिजली का बिल\n- SNo 4: शैक्षणिक प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: माध्यमिक विद्यालय का प्रमाणपत्र -8 कक्षा\n  * Supporting Document 2: प्राथमिक विद्यालय का प्रमाणपत्र - 5वीं कक्षा\n  * Supporting Document 3: हाई स्कूल(10वी कक्षा) अंकसूची\n  * Supporting Document 4: उच्चतर माध्यमिक विधालय प्रमाण पत्र(१२ वीं कक्षा)\n  * Supporting Document 5: एम-फिल\n  * Supporting Document 6: स्कूल प्रमाणपत्र (3 साल की एक सबूत निरंतर अध्ययन के रूप में)\n  * Supporting Document 7: स्नातकोत्तर प्रमाणपत्र\n  * Supporting Document 8: तकनीकी विषयों में प्रमाणपत्र\n- SNo 5: ५ साल निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: घर या भूमि का दस्तावेज़\n  * Supporting Document 2: व्यक्ति की सेवा पुस्तिका.\n\nAPPLICATION FORM FIELDS:\n- Field: सामान्य विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: हितग्राही के अभिभावक का प्रकार [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: हितग्राही के अभिभावक का नाम [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: हितग्राही के अभिभावक का व्यवसाय [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: हितग्राही का जन्म स्थान [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: लिंग [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: पता का विवरण [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: पता [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: पिन कोड [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: जिला [Type: drop down\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पूवतावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचर\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: । \n2. यूज़रिेम िजट करें। \n3. पतसविा िजट करें। \n4. “ओर्ीपी भेजें” पर क्लिक करें। \n5. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n6. लॉक्रगि बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजित खोज \nलॉगगन क े  पश्चात डनम्नानुसार योजना खोज पेज खुलेगा। \n \nचित्र क्रमांक 6 \n \nचरण 3.1: यहााँ डनर्ाटररत बॉक्स में पूछी गई जानकारी िजट करें और “खोजें” बटन पर क्लिक करें। \nचरण 3.2: सेवाओं की सूिी दिखाई िेगी, इसमें “Domicile Certificate” पर क्लिक करें। \nअब डनम्नानुसार पेज दिखाई िेगा। इस पेज पर, नीिे आवश्यक दस्ततवेज़़ों की सूिी िेखी जा सकती है। \n \n \nचित्र क्रमांक 7\n\n--- Page 7 ---\nचित्र क्रमांक 8 \n \nचरण 3.3: चित्र क्रमांक 7 क े  अनुसार प्रिचशित गविंिो में “आगे” बटन दिखाई िेगा, उस पर क्लिक करें।\n\n--- Page 8 ---\nचरण 4: आधतर ई-प्रमतणीकरण \nआर्ार ई-प्रमाणीकरण हेतु इस फॉमट में आवेिक की बुडनयािी जानकारी िजट करें। \n \nचित्र क्रमांक 9 \n \nचरण 4.1: आवेिक एवं दहतग्राही का नाम भरें। ड्रॉप-िाउन ललस्ट से िुनकर कायाटलय का नाम और पूरा पता िजट \nकरें। \nचरण 4.2: प्रमाणीकरण क े  ललए “Aadhaar e-authentication” पर क्लिक करें। डनम्नानुसार पॉप-अप \nगविंिो खुलेगा। \n \nचित्र क्रमांक 10\n\n--- Page 9 ---\nचरण 4.3: प्रमाणीकरण हेतु आर्ार संख्या एवं नाम (आर्ार कािट क े  अनुसार अ ं ग्रेज़ी में) िजट करें। \nचरण 4.4: डनर्ाटररत बॉक्स पर क्लिक करक े  आर्ार प्रमाणीकरण हेतु सहमगत िें। \nचरण 4.5: “Authentication”  बटन पर क्लिक करें। \nचरण 4.6: आर्ार ई-प्रमाणीकरण क े  बाि “जमत करें” बटन पर क्लिक करें।  \nडनम्नानुसार पॉप-अप गविंिो खुलेगा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ाल ................................ ................................ ................................ ................................ .......... 2 \nचरण 1: ई-निस्ट्रिक्ट पोर्ाल पर पंजीयि ................................ ................................ ................................ ................................ ......... 3 \nचरण 2: पंजीक ृ र् यूज़र लॉक्रगि ................................ ................................ ................................ ................................ ........................... 4 \nचरण 5: मूल निवतसी प्रमतण पत्र के र्लए आवेदि ................................ ................................ ................................ .................... 9 \nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित ................................ ................................ ................................ ............................ 10 \nचरण 7: पूवतावलोकि और आवेदि जमत करित ................................ ................................ ................................ ........................ 12 \nचरण 8: शुल्क कत भुगर्ति ................................ ................................ ................................ ................................ ................................  14 \nचरण 9: पतवर्ी सुरक्षिर् रखित ................................ ................................ ................................ ................................ ....................... 15 \nचरण 10: आवेदि की स्थिवर् देखित ................................ ................................ ................................ ................................ ............. 16\n\n--- Page 3 ---\nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर्ाल \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें \ncgedistrict.cgstate.gov.in  \n \nछत्तीसगढ़ ई-डिस्ट्रिक्ट पोटटल का होमपेज खुलेगा। \n \nचचत्र िमतंक 1: ई-निस्ट्रिक्ट पोर्ाल कत होम पेज \nलॉगगन करने क े  ललए “ितगररक लॉक्रगि” बटन पर क्लिक करें। \n \nचचत्र िमतंक 2: ितगररक लॉक्रगि\n\n--- Page 4 ---\nचरण 1: ई-निस्ट्रिक्ट पोर्ाल पर पंजीयि \nचरण 1.1: यदि आप नए यूज़र हैं तो यहााँ क्लिक करें – “नया पंजीयन करने हेतु क्लिक करें”  \n \nचचत्र िमतंक 3:  \n \nचरण 1.2: ितगररक पंजीकरण पेज खुलेगा। \n \nचित्र क्रमांक 4 \n \nचरण 1.3: यूज़सा िेम और अन्य आवश्यक जानकाररयााँ िज़ट करें। \nचरण 1.4: “जमत करें” बटन पर क्लिक करें। \nपंजीयन स्वीकार होने क े  बाि आपक े  रचजस्टिट मोबाइल नंबर पर पासविट भेजा जाएगा। इस पासविट की सहायता \nसे आप मूल डनवासी प्रमाण पत्र हेतु लॉगगन कर सकते हैं। आपक े  पास पासविट बिलने का गवकल्प भी है।\n\n--- Page 5 ---\nचरण 2: पंजीक ृ र् यूज़र लॉक्रगि \nपंजीक ृ त यूज़सट डनम्न प्रदक्रया द्वारा लॉगगन करें। \n \nचित्र क्रमांक 5 \n \n1. भतषत का ियन करें। \n2. यूज़रिेम िजट करें। \n3. पतसविा िजट करें। \n4. “ओर्ीपी भेजें” पर क्लिक करें। \n5. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n6. लॉक्रगि बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजित खोज \nलॉ\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       हाँ, एक विवाहित महिला अपने पिता के पते का उपयोग करके मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकती है। इसके लिए निम्नलिखित शर्तें लागू हैं:
       
       1. **मुख्य मार्ग (दोनों मानदंड एक और दो):**
          - मानदंड एक (A) के तहत: पिता/पालक का सेवा प्रमाण पत्र या 25 वर्ष का निवास प्रमाण।
          - मानदंड दो (B) के तहत: 3 वर्ष की स्कूली शिक्षा या 5वीं, 8वीं, 10वीं, 12वीं कक्षा की बोर्ड परीक्षा का अंकपत्र।
       
       2. **अपवाद (मानदंड तीन):**
          - यदि उपरोक्त मानदंड पूरे नहीं होते हैं, तो भी वह निम्नलिखित के आधार पर प्रमाण पत्र प्राप्त कर सकती है:
            - पति का मूल निवासी प्रमाण पत्र।
            - आवेदक या पति का सरकारी/अर्ध-सरकारी कर्मचारी होना।
            - आवेदक या माता-पिता का अखिल भारतीय सेवा (AIS) में होना और छत्तीसगढ़ कैडर आवंटित होना।
       
       **आवश्यक दस्तावेज:**
       - शपथ पत्र (अनिवार्य)।
       - पिता/पालक का सेवा प्रमाण पत्र।
       - 15 वर्ष के निवास का प्रमाण (जैसे जन्म प्रमाण पत्र, मतदाता पहचान पत्र, बिजली बिल)।
       - शैक्षिक प्रमाण पत्र (जैसे 10वीं कक्षा का अंकपत्र)।
       
       **आवेदन प्रक्रिया:**
       1. ई-डिस्ट्रिक्ट पोर्टल पर पंजीकरण करें।
       2. आवेदन पत्र भरें और आवश्यक दस्तावेज अपलोड करें।
       3. ई-प्रमाणीकरण (आधार-आधारित) करें।
       4. शुल्क का भुगतान करें (ऑनलाइन या कियोस्क पर 30 रुपये)।
       
       **नोट:** यदि पिता का निवास प्रमाण पत्र नहीं है, तो अन्य दस्तावेजों (जैसे मतदाता पहचान पत्र, बिजली बिल) के माध्यम से 15 वर्ष के निवास का प्रमाण प्रस्तुत करना अनिवार्य है।
       ```
| 11 | `ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?` | None | None | ✅ MATCH | new_topic | 2.34s |

### Query 11 Details
* **Query**: `ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?`
* **Expected Service ID**: `None`
* **Classified Service ID**: `None`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the difference in fees between OBC certificate and SC ST certificate?`
* **Resolved Hindi Query**: `ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > जानकारी उपलब्ध नहीं है।

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?"
       ```
     * **Response**:
       ```json
       ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?"
       ```
     * **Response**:
       ```json
       What is the difference in fees between OBC certificate and SC ST certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the difference in fees between OBC certificate and SC/ST certificate?', 'topic_summary': 'Comparison of fees for OBC and SC/ST certificates.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र और एससी एसटी प्रमाण पत्र के शुल्क में क्या अंतर है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': None, 'service_id': None}
       ```
| 12 | `जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?` | 3 | 3 | ✅ MATCH | new_topic | 6.42s |

### Query 12 Details
* **Query**: `जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How to apply online for marriage registration and certificate using caste certificate details?`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन करने के लिए निम्नलिखित चरणों का पालन करें:
  > 
  > 1. **ई-डिस्ट्रिक्ट पोर्टल पर पंजीकरण करें**:
  >    - अपने कंप्यूटर या लैपटॉप में वेब ब्राउज़र खोलें और `cgedistrict.cgstate.gov.in` टाइप करें।
  >    - होमपेज पर "नागरिक लॉगिन" बटन पर क्लिक करें।
  >    - नए उपयोगकर्ता के रूप में पंजीकरण करने के लिए "नया पंजीकरण" लिंक पर क्लिक करें।
  >    - पंजीकरण फॉर्म में आवश्यक जानकारी भरें और "जमा करें" बटन पर क्लिक करें।
  > 
  > 2. **लॉगिन**:
  >    - लॉगिन पेज पर अपना यूजरनेम और पासवर्ड दर्ज करें।
  >    - "OTP भेजें" पर क्लिक करें और प्राप्त OTP को दर्ज करें।
  >    - लॉगिन करने के लिए "लॉगिन" बटन पर क्लिक करें।
  > 
  > 3. **सेवा खोजें**:
  >    - "योजना खोज" पेज पर जाएं।
  >    - सेवा सूची में "विवाह प्रमाण पत्र" पर क्लिक करें।
  >    - सेवा विवरण पेज पर आवश्यक दस्तावेजों की सूची देखें।
  > 
  > 4. **आवेदन भरें**:
  >    - आवेदन फॉर्म में विवाह से संबंधित जानकारी भरें:
  >      - विवाह की तिथि
  >      - विवाह का स्थान
  >      - विवाह का प्रकार
  >      - क्या विवाह पंजीकृत है
  >    - "सहेजें और पूर्ण सत्यापन" बटन पर क्लिक करें।
  > 
  > 5. **दस्तावेज अपलोड करें**:
  >    - आवश्यक दस्तावेज (जैसे वर और वधु का संयुक्त फोटो, जन्म प्रमाण पत्र, विवाह आमंत्रण पत्र) अपलोड करें।
  >    - "फाइल चुनें" पर क्लिक करके दस्तावेज चुनें और "अपलोड" करें।
  > 
  > 6. **सत्यापन**:
  >    - सभी जानकारी की जांच करें और "जमा करें" पर क्लिक करें।
  >    - आवेदन की स्थिति देखने के लिए "पूर्ण सत्यापन" पेज पर जाएं।
  > 
  > 7. **शुल्क भुगतान**:
  >    - ऑनलाइन शुल्क ₹30.0 या कियोस्क शुल्क ₹30.0 का भुगतान करें।
  > 
  > 8. **प्रमाण पत्र प्राप्त करें**:
  >    - प्रसंस्करण के बाद, विवाह प्रमाण पत्र डाउनलोड करें।
  > 
  > **महत्वपूर्ण बिंदु**:
  > - आवेदन शुल्क ₹30.0 है (ऑनलाइन या कियोस्क)।
  > - प्रसंस्करण समय 15 दिन है।
  > - सभी अनिवार्य दस्तावेज (जैसे वर और वधु का संयुक्त फोटो, जन्म प्रमाण पत्र) आवश्यक हैं।
  > 
  > अधिक जानकारी के लिए आप ई-डिस्ट्रिक्ट पोर्टल पर उपलब्ध "उपयोगकर्ता मार्गदर्शिका" देख सकते हैं।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?"
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?"
       ```
     * **Response**:
       ```json
       How to apply online for marriage registration and certificate using caste certificate details?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'How to apply online for marriage registration using caste certificate details and proof of marriage certificate?', 'topic_summary': 'Marriage registration process using caste certificate as a document.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '1', 'service_id': '3'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- MARRIAGE JURISDICTION RULE: Under the Chhattisgarh Compulsory Registration of Marriages Rules, a marriage MUST be registered in the local area where the marriage was solemnized or performed, NOT at the couple's hometown or place of residence. The registrar is the Local Authority of that local area (Gram Panchayat if rural; Municipality or Municipal Corporation if urban). State this clearly when citizens ask where or under which office/authority to register their marriage.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Marriage Registration & Certificate\nService ID: 3\nLanguage: EN\nDepartment: Urban Administration and development Department\nTime Limit / SLA: 15 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: At The Time Of Marriage Combined Photograph Of Groom And Bride(2a Size) (Mandatory: Yes)\n  * Supporting Document 1: At The Time Of Marriage Combined Photograph Of Groom And Bride(2a Size)\n- SNo 3: Declaration Letter From Guardian Of Married Couple (Mandatory: No)\n  * Supporting Document 1: Declaration Letter From Guardian Of Married Couple\n- SNo 4: Other (Mandatory: No)\n  * Supporting Document 1: Other\n- SNo 5: Necessary Documents (Mandatory: No)\n  * Supporting Document 1: Necessary Documents\n- SNo 6: Birth Certificate Of Groom (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate Of Groom\n- SNo 7: Birth Certificate Of Bride (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate Of Bride\n- SNo 8: Document Signed By The Bride And Groom (First Page) (Mandatory: Yes)\n  * Supporting Document 1: Document Signed By The Bride And Groom (First Page)\n- SNo 9: Document Signed By The Bride And Groom (Second Page) (Mandatory: Yes)\n  * Supporting Document 1: Document Signed By The Bride And Groom (Second Page)\n- SNo 10: Copy Of Challan (Mandatory: Yes)\n  * Supporting Document 1: Copy Of Challan\n- SNo 11: Marriage Invitation Card (Mandatory: Yes)\n  * Supporting Document 1: Marriage Invitation Card\n- SNo 12: Divorce Certifcate (Mandatory: No)\n  * Supporting Document 1: Divorce Certificate\n- SNo 13: Widow Certificate (Mandatory: No)\n  * Supporting Document 1: Widow Certificate\n- SNo 14: Inter Religion Marriage Certificate (Mandatory: No)\n  * Supporting Document 1: Inter Religion Marriage Certificate\n\nAPPLICATION FORM FIELDS:\n- Field: Marriage Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Date of Marriage [Type: date, Data: Date] (Row: 2, Col: 1)\n- Field: Place of Marriage [Type: textarea, Data: Alfa Numeric] (Row: 2, Col: 2)\n- Field: Type of Marriage [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Is marriage Registered [Type: drop down, Data: Charactar] (Row: 3, Col: 2)\n- Field: Registration Number [Type: text, Data: Number] (Row: 4, Col: 1)\n- Field: Other Details [Type: textarea, Data: Charactar] (Row: 4, Col: 2)\n- Field: Groom Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Name of Groom in Local Language [Type: text, Data: Charactar] (Row: 6, Col: 1)\n- Field: Name of Groom in English [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Date of Birth of Groom [Type: date, Data: Date] (Row: 7, Col: 1)\n- Field: Age at time of marriage [Type: text, Data: Number] (Row: 7, Col: 2)\n- Field: Father Name in local language [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Father Name in English [Type: textarea, Data: Charactar] (Row: 8, Col: 2)\n- Field: Marital Status of Groom [Type: drop down, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address Of Groom [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Present Address of groom in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Present Address of Groom in English [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 2)\n- Field: Permanent Address of Groom in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Permanent Address of Groom in English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 2)\n- Field: Witness Details of Groom Side [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Bride Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Name of Bride in local language [Type: text, Data: Charactar] (Row: 15, Col: 1)\n- Field: Name of Bride in English [Type: text, Data: Charactar] (Row: 15, Col: 2)\n- Field: Date of Birth of Bride [Type: date, Data: Date] (Row: 16, Col: 1)\n- Field: Bride Age at time of marriage [Type: text, Data: Number] (Row: 16, Col: 2)\n- Field: Fathers name of Bride in Local language [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: Fathers name of Bride in English [Type: text, Data: Charactar] (Row: 17, Col: 2)\n- Field: Marital Status of Bride [Type: drop down, Data: Charactar] (Row: 18, Col: 1)\n- Field: Address Of Bride [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: Present Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Present Address\n\n--- Source 2: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: Row: 16, Col: 1)\n- Field: Bride Age at time of marriage [Type: text, Data: Number] (Row: 16, Col: 2)\n- Field: Fathers name of Bride in Local language [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: Fathers name of Bride in English [Type: text, Data: Charactar] (Row: 17, Col: 2)\n- Field: Marital Status of Bride [Type: drop down, Data: Charactar] (Row: 18, Col: 1)\n- Field: Address Of Bride [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: Present Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Present Address of Bride in English [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: Permanent Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 1)\n- Field: Permanent Address of Bride in English [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 2)\n- Field: Witness Details of Bride Side [Type: fieldset, Data: Alfa Numeric] (Row: 22, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 3_en_3.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nवििाह पंजीकरण एिं प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nपर ऑनलाइन आिेदन\n\n--- Page 2 ---\nविषय सूची \nई-डिस्ट्रिक्ट: होम पेज ................................ ................................ ................................ ................................ ................................ .................. 2 \nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण ................................ ................................ ................................ ................................ ............... 3 \nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन ................................ ................................ ................................ ................................ .................... 4 \nचरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ .................. 5 \nचरण 4: आिेदक की बुडनयादी जानकारी ................................ ................................ ................................ ................................ ............... 6 \nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन ................................ ................................ ................................ ....................... 7 \nचरण 6: आिश्यक दस्तािेज़ अपलोि करना ................................ ................................ ................................ ................................ .......... 8 \nचरण 7: पूिाािलोकन और आिेदन जमा करना ................................ ................................ ................................ ................................ ...... 9 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 10 \nचरण 9: पािर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ................................  11\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉगगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉगगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nच\n\n--- Source 3: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉगगन प्रगक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासििा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \nचरण 3.2: खोजें पर क्लिक करें। सेवाओं की सूची खुलेगी। \n \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.3: सेवाओं की सूची में प्रिजशित वििाह प्रमाण पत्र (Marriage Certificate) पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। इस पेज पर आवश्यक िस्तावेज़़ों की सूची भी िेखी जा सकती है। \n \n \nचचत्र क्रमांक 7: सेिा पररचय एिं सहायक दस्तािेज़़ों की सूची \n \nचरण 3.4: “आगे” बटन पर क्लिक करें।\n\n--- Page 7 ---\nचरण 4: आिेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की\n\n--- Source 4: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की जांच सूची \n \nचरण 4.3: इस गविंिो में क्रिए गए “जमा” बटन पर क्लिक करें।\n\n--- Page 8 ---\nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन \nचरण 5.1: आवेिन फॉमट में वर से संबंजित आवश्यक जानकाररयााँ िजट करें। \n \n \nचचत्र क्रमांक 10: वििाह पंजीकरण हेर्ु आिेदन फॉमा – िर से संबंविर् वििरण \n \nचरण 5.2: आवेिन में विु से संबंजित जानकाररयााँ िजट करें। \n \nचचत्र क्रमांक 11: वििाह पंजीकरण हेर्ु आिेदन फॉमा – ििु से संबंविर् वििरण \n \nचरण 5.3: फॉमट भरने क े  बाि “सहेजें और पूिाािलोकन” बटन पर क्लिक करें।\n\n--- Page 9 ---\nचरण 6: आिश्यक दस्तािेज़ अपलोि करना \nअनुलग्नक का गववरण पेज खुलेगा। आवश्यक िस्तावेज़ अपलोि करने क े  ललए ननम्न प्रक्रिया का पालन करें। \n \n \nचचत्र क्रमांक 12: सहायक दस्तािेज़ अपलोि \nचरण 6.1: “Choose File”  पर क्लिक कर अपने कम्प्यूटर या लैपटॉप से िस्तावेज की स्क ै न कॉपी चुनें। \nचरण 6.2: फाइल चुनने क े बाि “UPLOAD”  पर क्लिक करें। \n \n \nचचत्र क्रमांक 13: अनुलग्नक सहेजना \n \nचरण 6.3: िस्तावेज अपलोि करने क े  बाि “अनुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुक्रिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें।\n\n--- Page 10 ---\nचरण 7: पूिाािलोकन और आिेदन जमा करना \nअनुलग्नक सहेजने क े  पश्चात् ननम्न जचत्रानुसार पूवाटवलोकन पेज खुलेगा। ध्यानपूवटक अपने आवेिन की जांच करें। \n \n \nचचत्र क्रमांक 14: पूिाािलोकन \n \n \nचचत्र क्रमांक 15: घोषणा एिं जमा \n \nचरण 7.1 घोषणा: घोषणा हेतु ननिाटररत बॉक्स पर क्लिक करें। \nचरण 7.2: घोषणा पर क्लिक करते ही “जमा करें” बटन क्रिखाई िेग\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: विवाह पंजीकरण एवं प्रमाण पत्र\nService ID: 3\nLanguage: HI\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nTime Limit / SLA: 15 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: वर एवं वधु का संयुक्त फोटो(2A साईज) प्रमाण पत्र के लिए (Mandatory: हाँ)\n  * Supporting Document 1: वर एवं वधु का संयुक्त फोटो(2A साईज) प्रमाण पत्र के लिए\n- SNo 3: प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: विवाह अनुस्थान संपन्न कराने वाले के सत्यापन के लिए उस समय उपस्थित पंडित /पादरी /मौलवी अथवा समाज का प्रमाण पत्र\n- SNo 4: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य कारण\n- SNo 5: आवश्यक दस्तावेज़ (Mandatory: नहीं)\n  * Supporting Document 1: आवश्यक दस्तावेज़\n- SNo 6: वर का जन्म प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: वर का जन्म प्रमाण पत्र\n- SNo 7: वधु का जन्म प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: वधु का जन्म प्रमाण पत्र\n- SNo 8: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (प्रथम पेज) (Mandatory: हाँ)\n  * Supporting Document 1: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (प्रथम पेज)\n- SNo 9: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (व्दितीय पेज) (Mandatory: हाँ)\n  * Supporting Document 1: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (व्दितीय पेज)\n- SNo 10: चालान की प्रति (Mandatory: हाँ)\n  * Supporting Document 1: चालान की प्रति\n- SNo 11: विवाह आमंत्रण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: विवाह आमंत्रण पत्र\n- SNo 12: तलाक प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: तलाक प्रमाण पत्र\n- SNo 13: विधवा प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: विधवा प्रमाण पत्र\n- SNo 14: अंतरधार्मिक विवाह प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: अंतरधार्मिक विवाह प्रमाण पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: वैवाहिक जानकारी [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: विवाह की तिथि [Type: date, Data: Date] (Row: 2, Col: 1)\n- Field: विवाह का स्थान [Type: textarea, Data: Alfa Numeric] (Row: 2, Col: 2)\n- Field: विवाह का प्रकार [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: क्या विवाह पंजीकृत है [Type: drop down, Data: Charactar] (Row: 3, Col: 2)\n- Field: पंजीयन क्रमांक [Type: text,\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: वधु का पता [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: वधु का वर्तमान पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: वधु का वर्तमान पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: वधु का स्थायी पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 1)\n- Field: वधु की स्थायी पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 2)\n- Field: वधु पक्ष के गवाह का विवरण [Type: fieldset, Data: Alfa Numeric] (Row: 22, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 3_hi_3.pdf (INSTRUCTION)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nवििाह पंजीकरण एिं प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nपर ऑनलाइन आिेदन\n\n--- Page 2 ---\nविषय सूची \nई-डिस्ट्रिक्ट: होम पेज ................................ ................................ ................................ ................................ ................................ .................. 2 \nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण ................................ ................................ ................................ ................................ ............... 3 \nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन ................................ ................................ ................................ ................................ .................... 4 \nचरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ .................. 5 \nचरण 4: आिेदक की बुडनयादी जानकारी ................................ ................................ ................................ ................................ ............... 6 \nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन ................................ ................................ ................................ ....................... 7 \nचरण 6: आिश्यक दस्तािेज़ अपलोि करना ................................ ................................ ................................ ................................ .......... 8 \nचरण 7: पूिाािलोकन और आिेदन जमा करना ................................ ................................ ................................ ................................ ...... 9 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 10 \nचरण 9: पािर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ................................  11\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉगगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉगगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: ्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की जांच सूची \n \nचरण 4.3: इस गविंिो में क्रिए गए “जमा” बटन पर क्लिक करें।\n\n--- Page 8 ---\nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन \nचरण 5.1: आवेिन फॉमट में वर से संबंजित आवश्यक जानकाररयााँ िजट करें। \n \n \nचचत्र क्रमांक 10: वििाह पंजीकरण हेर्ु आिेदन फॉमा – िर से संबंविर् वििरण \n \nचरण 5.2: आवेिन में विु से संबंजित जानकाररयााँ िजट करें। \n \nचचत्र क्रमांक 11: वििाह पंजीकरण हेर्ु आिेदन फॉमा – ििु से संबंविर् वििरण \n \nचरण 5.3: फॉमट भरने क े  बाि “सहेजें और पूिाािलोकन” बटन पर क्लिक करें।\n\n--- Page 9 ---\nचरण 6: आिश्यक दस्तािेज़ अपलोि करना \nअनुलग्नक का गववरण पेज खुलेगा। आवश्यक िस्तावेज़ अपलोि करने क े  ललए ननम्न प्रक्रिया का पालन करें। \n \n \nचचत्र क्रमांक 12: सहायक दस्तािेज़ अपलोि \nचरण 6.1: “Choose File”  पर क्लिक कर अपने कम्प्यूटर या लैपटॉप से िस्तावेज की स्क ै न कॉपी चुनें। \nचरण 6.2: फाइल चुनने क े बाि “UPLOAD”  पर क्लिक करें। \n \n \nचचत्र क्रमांक 13: अनुलग्नक सहेजना \n \nचरण 6.3: िस्तावेज अपलोि करने क े  बाि “अनुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुक्रिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें।\n\n--- Page 10 ---\nचरण 7: पूिाािलोकन और आिेदन जमा करना \nअनुलग्नक सहेजने क े  पश्चात् ननम्न जचत्रानुसार पूवाटवलोकन पेज खुलेगा। ध्यानपूवटक अपने आवेिन की जांच करें। \n \n \nचचत्र क्रमांक 14: पूिाािलोकन \n \n \nचचत्र क्रमांक 15: घोषणा एिं जमा \n \nचरण 7.1 घोषणा: घोषणा हेतु ननिाटररत बॉक्स पर क्लिक करें। \nचरण 7.2: घोषणा पर क्लिक करते ही “जमा करें” बटन क्रिखाई िेगा। इस पर क्ल\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: �्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉगगन प्रगक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासििा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \nचरण 3.2: खोजें पर क्लिक करें। सेवाओं की सूची खुलेगी। \n \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.3: सेवाओं की सूची में प्रिजशित वििाह प्रमाण पत्र (Marriage Certificate) पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। इस पेज पर आवश्यक िस्तावेज़़ों की सूची भी िेखी जा सकती है। \n \n \nचचत्र क्रमांक 7: सेिा पररचय एिं सहायक दस्तािेज़़ों की सूची \n \nचरण 3.4: “आगे” बटन पर क्लिक करें।\n\n--- Page 7 ---\nचरण 4: आिेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की जांच सूच\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "जाति प्रमाण पत्र के विवरण का उपयोग करके विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन कैसे करें?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण एवं प्रमाण पत्र के लिए ऑनलाइन आवेदन करने के लिए निम्नलिखित चरणों का पालन करें:
       
       1. **ई-डिस्ट्रिक्ट पोर्टल पर पंजीकरण करें**:
          - अपने कंप्यूटर या लैपटॉप में वेब ब्राउज़र खोलें और `cgedistrict.cgstate.gov.in` टाइप करें।
          - होमपेज पर "नागरिक लॉगिन" बटन पर क्लिक करें।
          - नए उपयोगकर्ता के रूप में पंजीकरण करने के लिए "नया पंजीकरण" लिंक पर क्लिक करें।
          - पंजीकरण फॉर्म में आवश्यक जानकारी भरें और "जमा करें" बटन पर क्लिक करें।
       
       2. **लॉगिन**:
          - लॉगिन पेज पर अपना यूजरनेम और पासवर्ड दर्ज करें।
          - "OTP भेजें" पर क्लिक करें और प्राप्त OTP को दर्ज करें।
          - लॉगिन करने के लिए "लॉगिन" बटन पर क्लिक करें।
       
       3. **सेवा खोजें**:
          - "योजना खोज" पेज पर जाएं।
          - सेवा सूची में "विवाह प्रमाण पत्र" पर क्लिक करें।
          - सेवा विवरण पेज पर आवश्यक दस्तावेजों की सूची देखें।
       
       4. **आवेदन भरें**:
          - आवेदन फॉर्म में विवाह से संबंधित जानकारी भरें:
            - विवाह की तिथि
            - विवाह का स्थान
            - विवाह का प्रकार
            - क्या विवाह पंजीकृत है
          - "सहेजें और पूर्ण सत्यापन" बटन पर क्लिक करें।
       
       5. **दस्तावेज अपलोड करें**:
          - आवश्यक दस्तावेज (जैसे वर और वधु का संयुक्त फोटो, जन्म प्रमाण पत्र, विवाह आमंत्रण पत्र) अपलोड करें।
          - "फाइल चुनें" पर क्लिक करके दस्तावेज चुनें और "अपलोड" करें।
       
       6. **सत्यापन**:
          - सभी जानकारी की जांच करें और "जमा करें" पर क्लिक करें।
          - आवेदन की स्थिति देखने के लिए "पूर्ण सत्यापन" पेज पर जाएं।
       
       7. **शुल्क भुगतान**:
          - ऑनलाइन शुल्क ₹30.0 या कियोस्क शुल्क ₹30.0 का भुगतान करें।
       
       8. **प्रमाण पत्र प्राप्त करें**:
          - प्रसंस्करण के बाद, विवाह प्रमाण पत्र डाउनलोड करें।
       
       **महत्वपूर्ण बिंदु**:
       - आवेदन शुल्क ₹30.0 है (ऑनलाइन या कियोस्क)।
       - प्रसंस्करण समय 15 दिन है।
       - सभी अनिवार्य दस्तावेज (जैसे वर और वधु का संयुक्त फोटो, जन्म प्रमाण पत्र) आवश्यक हैं।
       
       अधिक जानकारी के लिए आप ई-डिस्ट्रिक्ट पोर्टल पर उपलब्ध "उपयोगकर्ता मार्गदर्शिका" देख सकते हैं।
       ```
| 13 | `ओबीसी प्रमाण पत्र में निवास प्रमाण पत्र के नियम` | 5 | 5 | ✅ MATCH | new_topic | 2.27s |

### Query 13 Details
* **Query**: `ओबीसी प्रमाण पत्र में निवास प्रमाण पत्र के नियम`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र में मूल निवासी प्रमाण पत्र के नियम"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र में मूल निवासी प्रमाण पत्र के नियम"
       ```
     * **Response**:
       ```json
       ओबीसी प्रमाण पत्र में मूल निवासी प्रमाण पत्र के नियम
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र में मूल निवासी प्रमाण पत्र के नियम"
       ```
     * **Response**:
       ```json
       The rules for the original inhabitant certificate in OBC certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र में मूल निवासी प्रमाण पत्र के नियम",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What are the rules for OBC certificate and original residence certificate?', 'topic_summary': 'User is asking about rules for two different certificates: OBC certificate and original residence certificate.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र में मूल निवासी प्रमाण पत्र के नियम",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '3', 'service_id': '5'}
       ```
| 14 | `शादी प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र लगेगा?` | 201 | 201 | ✅ MATCH | new_topic | 6.27s |

### Query 14 Details
* **Query**: `शादी प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र लगेगा?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is an affidavit for name change with marriage registration and certificate required?`
* **Resolved Hindi Query**: `विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, विवाह प्रमाण पत्र के साथ नाम परिवर्तन के शपथ पत्र (affidavit) की आवश्यकता नहीं होती है। नाम परिवर्तन के लिए शपथ पत्र (affidavit) एक अलग दस्तावेज़ है, जो नाम परिवर्तन की अधिसूचना के लिए लगाया जाता है। विवाह प्रमाण पत्र और शपथ पत्र दो अलग-अलग प्रक्रियाएँ हैं।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?"
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?"
       ```
     * **Response**:
       ```json
       Is an affidavit for name change with marriage registration and certificate required?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the process for marriage registration and name change affidavit?', 'topic_summary': 'User is asking about the process for two different government services: marriage registration and name change affidavit.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "विवाह पंजीकरण एवं प्रमाण पत्र के साथ नाम परिवर्तन का शपथ पत्र (affidavit) (affidavit) लगेगा?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, विवाह प्रमाण पत्र के साथ नाम परिवर्तन के शपथ पत्र (affidavit) की आवश्यकता नहीं होती है। नाम परिवर्तन के लिए शपथ पत्र (affidavit) एक अलग दस्तावेज़ है, जो नाम परिवर्तन की अधिसूचना के लिए लगाया जाता है। विवाह प्रमाण पत्र और शपथ पत्र दो अलग-अलग प्रक्रियाएँ हैं।
       ```
| 15 | `निवास प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क` | None | 7 | ❌ MISMATCH | new_topic | 7.44s |

### Query 15 Details
* **Query**: `निवास प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क`
* **Expected Service ID**: `None`
* **Classified Service ID**: `7`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Native Certificate Fee Chhattisgarh vs Caste Certificate Fee`
* **Resolved Hindi Query**: `मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > मूल निवासी प्रमाण पत्र (डोमिसाइल सर्टिफिकेट) के लिए शुल्क 30 रुपये है।
  > 
  > जाति प्रमाण पत्र (कास्ट सर्टिफिकेट) के लिए शुल्क 30 रुपये है।
  > 
  > दोनों सेवाओं के लिए शुल्क समान है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क"
       ```
     * **Response**:
       ```json
       मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क"
       ```
     * **Response**:
       ```json
       Native Certificate Fee Chhattisgarh vs Caste Certificate Fee
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- ELIGIBILITY LOGIC RULE (Domicile): If a citizen asks about eligibility or exceptions for the Domicile Certificate, explain the rules strictly:\n  1. Main Path (Both Criteria One AND Criteria Two must be met): The applicant must satisfy AT LEAST ONE option from Criteria One (Criteria A) AND AT LEAST ONE option from Criteria Two (Criteria B).\n     * You MUST list Criteria One and Criteria Two under separate, clearly-labeled headers or bullet points.\n     * Criteria One (Criteria A) options: Birth in CG, parent resident for 25 years, parent is CG Government/PSU employee, or property in CG for 5 years.\n     * Criteria Two (Criteria B) options: 3 years of school study in CG, or passing Class 5, 8, 10, 12 board exam from CG.\n     * Never merge them into one list or omit the education requirements of Criteria Two.\n  2. Exceptions (Criteria Three / Criteria C): If they do not meet the Main Path (for example, if they lack 'Proof of 15 Years Stay' or did not study in CG), they can still get a Domicile Certificate under the exceptions of Criteria Three (C). For Criteria Three (C), Criteria A and B are NOT required. The exceptions are: (a) spouse is a domicile of CG, (b) applicant or spouse is a CG Government/PSU employee, or (c) applicant or parent is in All India Services and allotted CG Cadre.\n  3. Clarity: Never state that Criteria Three requires stay proof or education. Clearly explain that Criteria Three is a standalone set of exceptions that bypasses the need for the stay proof or CG education requirements of Criteria One and Two.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Domicile Certificate\nService ID: 7\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 7 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: Other (Mandatory: No)\n  * Supporting Document 1: Other Documents\n- SNo 3: Proof Of At Least 15 Years Stay (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate\n  * Supporting Document 2: Father/ Guardian Service Certificate\n  * Supporting Document 3: Job Service Certificate / Identity Card (If The Applicant Is Under Govt./Semi Govt.)\n  * Supporting Document 4: Voters Identity Card\n  * Supporting Document 5: Land And House Document\n  * Supporting Document 6: Birth Information Form\n  * Supporting Document 7: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 8: Ration Card\n  * Supporting Document 9: Electricity Bill\n- SNo 4: Educational Certificate (Mandatory: Yes)\n  * Supporting Document 1: Middle School Certificate - 8th Standard\n  * Supporting Document 2: Primary School Certificate - 5th Standard\n  * Supporting Document 3: High School(10th) Certificate\n  * Supporting Document 4: Higher Secondary School Certificate(12th)\n  * Supporting Document 5: M.Phil/D.Lit./Ph.D. Certificate\n  * Supporting Document 6: School Certificate (As A Proof Of 3 Years Continuous Study)\n  * Supporting Document 7: Post Graduation Certificate\n  * Supporting Document 8: Certificate In Technical Subjects\n- SNo 5: Proof Of At Least 5 Years Stay (Mandatory: No)\n  * Supporting Document 1: Land And House Document\n  * Supporting Document 2: Persons Service Book.\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Guardians Occupation of Beneficiary [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: Beneficiary place of Birth [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: Address Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 7, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: section lebel, Data: Charactar] (Row: 8, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: fieldset, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Beneficiary Details of Business or Service [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Beneficiary Details of Business or service [Type: fieldset, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Beneficiary Education Level [Type: section lebel, Data: Charactar] (Row: 12, Col: 1)\n- Field: Beneficiary Education Level [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Have Beneficiary Voter Id [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: District Name of Beneficiary [Type: drop down, Data: Charactar] (Row: 15, Col: 2)\n- Field: Living From in Years [Type: number, Data: Date] (Row: 16, Col: 1)\n- Field: Reason for application Domicile [Type: text, Data: Charactar] (Row: 16, Col: 2)\n- Field: Any other detail [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 17, Col: 2)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 7_en_7.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nउपयोगकर्ता मतगादर्शिकत \n \n  \nमूल निवतसी प्रमतण पत्र क े  र्लए ई-निस्ट्रिक्ट पोर्ाल पर ऑिलतइि आवेदि प्रक्रियत \n \nछत्तीसगढ़ इन्फोर्ेक प्रमोशि सोसतयर्ी\n\n--- Page 2 ---\nववषय सूची \nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर\n\n--- Source 2: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �िगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह पेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 3: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: 1 ---\nउपयोगकर्ता मतगादर्शिकत \n \n  \nमूल निवतसी प्रमतण पत्र क े  र्लए ई-निस्ट्रिक्ट पोर्ाल पर ऑिलतइि आवेदि प्रक्रियत \n \nछत्तीसगढ़ इन्फोर्ेक प्रमोशि सोसतयर्ी\n\n--- Page 2 ---\nववषय सूची \nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर्ाल ................................ ................................ ................................ ................................ .......... 2 \nचरण 1: ई-निस्ट्रिक्ट पोर्ाल पर पंजीयि ................................ ................................ ................................ ................................ ......... 3 \nचरण 2: पंजीक ृ र् यूज़र लॉक्रगि ................................ ................................ ................................ ................................ ........................... 4 \nचरण 5: मूल निवतसी प्रमतण पत्र के र्लए आवेदि ................................ ................................ ................................ .................... 9 \nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित ................................ ................................ ................................ ............................ 10 \nचरण 7: पूवतावलोकि और आवेदि जमत करित ................................ ................................ ................................ ........................ 12 \nचरण 8: शुल्क कत भुगर्ति ................................ ................................ ................................ ................................ ................................  14 \nचरण 9: पतवर्ी सुरक्षिर् रखित ................................ ................................ ................................ ................................ ....................... 15 \nचरण 10: आवेदि की स्थिवर् देखित ................................ ................................ ................................ ................................ ............. 16\n\n--- Page 3 ---\nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर्ाल \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें \ncgedistrict.cgstate.gov.in  \n \nछत्तीसगढ़ ई-डिस्ट्रिक्ट पोटटल का होमपेज खुलेगा। \n \nचचत्र िमतंक 1: ई-निस्ट्रिक्ट पोर्ाल कत होम पेज \nलॉगगन करने क े  ललए “ितगररक लॉक्रगि” बटन पर क्लिक करें। \n \nचचत्र िमतंक 2: ितगररक लॉक्रगि\n\n--- Page 4 ---\nचरण 1: ई-निस्ट्रिक्ट पोर्ाल पर पंजीयि \nचरण 1.1: यदि आप नए यूज़र हैं तो यहााँ क्लिक करें – “नया पंजीयन करने हेतु क्लिक करें”  \n \nचचत्र िमतंक 3:  \n \nचरण 1.2: ितगररक पंजीकरण पेज खुलेगा। \n \nचित्र क्रमांक 4 \n \nचरण 1.3: यूज़सा िेम और अन्य आवश्यक जानकाररयााँ िज़ट करें। \nचरण 1.4: “जमत करें” बटन पर क्लिक करें। \nपंजीयन स्वीकार होने क े  बाि आपक े  रचजस्टिट मोबाइल नंबर पर पासविट भेजा जाएगा। इस पासविट की सहायता \nसे आप मूल डनवासी प्रमाण पत्र हेतु लॉगगन कर सकते हैं। आपक े  पास पासविट बिलने का गवकल्प भी है।\n\n--- Page 5 ---\nचरण 2: पंजीक ृ र् यूज़र लॉक्रगि \nपंजीक ृ त यूज़सट डनम्न प्रदक्रया द्वारा लॉगगन करें। \n \nचित्र क्रमांक 5 \n \n1. भतषत का ियन करे�\n\n--- Source 4: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पूवतावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचरण 7.2: घोषणत: घोर्षणा हेतु डनर्ाटररत बॉक्स पर क्लिक करें। \nचरण 7.3: घोर्षणा पर क्लिक करते ही “जमत करें” बटन दिखाई िेगा, इस पर क्लिक करें, इस तरह आवेिन \nजमा हो जाएगा। \n \nचित्र क्रमांक 19\n\n--- Page 15 ---\nचरण 8: शुल्क कत भुगर्ति \nइस पेज पर लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवा शुल्क एवं स्क ै डनिंग शुल्क का गववरण िेख सकते \nहैं। \n \nचित्र क्रमांक 15 \n \nचरण 8.1: डनर्ाटररत शुल्क का भुगतान करें। \nचरण 8.2: भुगतान क े  पश्चात् “जमत करें” बटन पर क्लिक करें। \n \nिोर्: \n• लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवत शुल्क रु. 30 डनर्ाटररत हैं। \n• सेवा शुल्क में  पताँच दस्ततवेज़़ों तक स्क ै डनिंग का शुल्क भी शागमल है। अगतररक्त िस्तावेज़़ों की स्क ै डनिंग का शुल्क पृथक से \nलोकसेवा क ें द्र/ सीएससी/डकयोस्क संिालक द्वारा ललया जा सकता है।\n\n--- Page 16 ---\nचरण 9: पतवर्ी सुरक्षिर् रखित \nआवेिन जमा करते ही चित्रानुसार पावती जेनरेट हो जाती है।  \nइस पावती में “आवेदि संदभा िमतंक” प्रिचशित होता है। \nभगवष्य की आवश्यकताओं और आवेिन की स्थिगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: मूल निवासी प्रमाण पत्र\nService ID: 7\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 7 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य\n- SNo 3: १५ वर्ष तक निवास का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: जन्म प्रमाण पत्र\n  * Supporting Document 2: पिता/पालक का सेवा प्रमाण पत्र\n  * Supporting Document 3: नौकरी प्रमाणपत्र /पहचान पत्र (यदि आवेदक शासकीय /अर्ध शासकीय अधीनस्थ हो )\n  * Supporting Document 4: वोटिंग कार्ड\n  * Supporting Document 5: घर या भूमि का दस्तावेज़\n  * Supporting Document 6: जन्म सूचना प्रपत्र\n  * Supporting Document 7: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 8: राशन कार्ड\n  * Supporting Document 9: बिजली का बिल\n- SNo 4: शैक्षणिक प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: माध्यमिक विद्यालय का प्रमाणपत्र -8 कक्षा\n  * Supporting Document 2: प्राथमिक विद्यालय का प्रमाणपत्र - 5वीं कक्षा\n  * Supporting Document 3: हाई स्कूल(10वी कक्षा) अंकसूची\n  * Supporting Document 4: उच्चतर माध्यमिक विधालय प्रमाण पत्र(१२ वीं कक्षा)\n  * Supporting Document 5: एम-फिल\n  * Supporting Document 6: स्कूल प्रमाणपत्र (3 साल की एक सबूत निरंतर अध्ययन के रूप में)\n  * Supporting Document 7: स्नातकोत्तर प्रमाणपत्र\n  * Supporting Document 8: तकनीकी विषयों में प्रमाणपत्र\n- SNo 5: ५ साल निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: घर या भूमि का दस्तावेज़\n  * Supporting Document 2: व्यक्ति की सेवा पुस्तिका.\n\nAPPLICATION FORM FIELDS:\n- Field: सामान्य विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: हितग्राही के अभिभावक का प्रकार [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: हितग्राही के अभिभावक का नाम [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: हितग्राही के अभिभावक का व्यवसाय [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: हितग्राही का जन्म स्थान [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: लिंग [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: पता का विवरण [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: पता [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: पिन कोड [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: जिला [Type: drop down\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_hi_citizenCharter.pdf (SLA_DETAILS)] ---\nछत्तीसगढ़ शासन\nराजस्व एवं आपदा प्रबंधन विभाग\nमंत्रालय\nमहानदी भवन नया रायपुर\n::: अधिसूचना :::\n\nरायपुर, दिनांक 16/05/2013\n\nक्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\nसारणी (SLA Details):\n1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n2. स्थाई जाति प्रमाण-पत्र (Permanent Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - सक्षम प्राधिकारी: कलेक्टर\n   - अपीलीय अधिकारी: कमिश्नर\n\n3. निवास प्रमाण-पत्र (Domicile Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्र\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ाल ................................ ................................ ................................ ................................ .......... 2 \nचरण 1: ई-निस्ट्रिक्ट पोर्ाल पर पंजीयि ................................ ................................ ................................ ................................ ......... 3 \nचरण 2: पंजीक ृ र् यूज़र लॉक्रगि ................................ ................................ ................................ ................................ ........................... 4 \nचरण 5: मूल निवतसी प्रमतण पत्र के र्लए आवेदि ................................ ................................ ................................ .................... 9 \nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित ................................ ................................ ................................ ............................ 10 \nचरण 7: पूवतावलोकि और आवेदि जमत करित ................................ ................................ ................................ ........................ 12 \nचरण 8: शुल्क कत भुगर्ति ................................ ................................ ................................ ................................ ................................  14 \nचरण 9: पतवर्ी सुरक्षिर् रखित ................................ ................................ ................................ ................................ ....................... 15 \nचरण 10: आवेदि की स्थिवर् देखित ................................ ................................ ................................ ................................ ............. 16\n\n--- Page 3 ---\nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर्ाल \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें \ncgedistrict.cgstate.gov.in  \n \nछत्तीसगढ़ ई-डिस्ट्रिक्ट पोटटल का होमपेज खुलेगा। \n \nचचत्र िमतंक 1: ई-निस्ट्रिक्ट पोर्ाल कत होम पेज \nलॉगगन करने क े  ललए “ितगररक लॉक्रगि” बटन पर क्लिक करें। \n \nचचत्र िमतंक 2: ितगररक लॉक्रगि\n\n--- Page 4 ---\nचरण 1: ई-निस्ट्रिक्ट पोर्ाल पर पंजीयि \nचरण 1.1: यदि आप नए यूज़र हैं तो यहााँ क्लिक करें – “नया पंजीयन करने हेतु क्लिक करें”  \n \nचचत्र िमतंक 3:  \n \nचरण 1.2: ितगररक पंजीकरण पेज खुलेगा। \n \nचित्र क्रमांक 4 \n \nचरण 1.3: यूज़सा िेम और अन्य आवश्यक जानकाररयााँ िज़ट करें। \nचरण 1.4: “जमत करें” बटन पर क्लिक करें। \nपंजीयन स्वीकार होने क े  बाि आपक े  रचजस्टिट मोबाइल नंबर पर पासविट भेजा जाएगा। इस पासविट की सहायता \nसे आप मूल डनवासी प्रमाण पत्र हेतु लॉगगन कर सकते हैं। आपक े  पास पासविट बिलने का गवकल्प भी है।\n\n--- Page 5 ---\nचरण 2: पंजीक ृ र् यूज़र लॉक्रगि \nपंजीक ृ त यूज़सट डनम्न प्रदक्रया द्वारा लॉगगन करें। \n \nचित्र क्रमांक 5 \n \n1. भतषत का ियन करें। \n2. यूज़रिेम िजट करें। \n3. पतसविा िजट करें। \n4. “ओर्ीपी भेजें” पर क्लिक करें। \n5. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n6. लॉक्रगि बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजित खोज \nलॉ\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: तावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचरण 7.2: घोषणत: घोर्षणा हेतु डनर्ाटररत बॉक्स पर क्लिक करें। \nचरण 7.3: घोर्षणा पर क्लिक करते ही “जमत करें” बटन दिखाई िेगा, इस पर क्लिक करें, इस तरह आवेिन \nजमा हो जाएगा। \n \nचित्र क्रमांक 19\n\n--- Page 15 ---\nचरण 8: शुल्क कत भुगर्ति \nइस पेज पर लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवा शुल्क एवं स्क ै डनिंग शुल्क का गववरण िेख सकते \nहैं। \n \nचित्र क्रमांक 15 \n \nचरण 8.1: डनर्ाटररत शुल्क का भुगतान करें। \nचरण 8.2: भुगतान क े  पश्चात् “जमत करें” बटन पर क्लिक करें। \n \nिोर्: \n• लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवत शुल्क रु. 30 डनर्ाटररत हैं। \n• सेवा शुल्क में  पताँच दस्ततवेज़़ों तक स्क ै डनिंग का शुल्क भी शागमल है। अगतररक्त िस्तावेज़़ों की स्क ै डनिंग का शुल्क पृथक से \nलोकसेवा क ें द्र/ सीएससी/डकयोस्क संिालक द्वारा ललया जा सकता है।\n\n--- Page 16 ---\nचरण 9: पतवर्ी सुरक्षिर् रखित \nआवेिन जमा करते ही चित्रानुसार पावती जेनरेट हो जाती है।  \nइस पावती में “आवेदि संदभा िमतंक” प्रिचशित होता है। \nभगवष्य की आवश्यकताओं और आवेिन की स्थिगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह पेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आव\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "मूल निवासी प्रमाण पत्र छत्तीसगढ़ शुल्क बनाम जाति प्रमाण पत्र शुल्क\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       मूल निवासी प्रमाण पत्र (डोमिसाइल सर्टिफिकेट) के लिए शुल्क 30 रुपये है।
       
       जाति प्रमाण पत्र (कास्ट सर्टिफिकेट) के लिए शुल्क 30 रुपये है।
       
       दोनों सेवाओं के लिए शुल्क समान है।
       ```
| 16 | `राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र स्टाम्प पेपर` | 201 | None | ❌ MISMATCH | new_topic | 46.74s |

### Query 16 Details
* **Query**: `राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र स्टाम्प पेपर`
* **Expected Service ID**: `201`
* **Classified Service ID**: `None`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `The Gazette Notification Name Change Advertisement Stamp Paper vs. Marriage Affidavit (affidavit) (affidavit) Stamp Paper`
* **Resolved Hindi Query**: `राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र (affidavit) (affidavit) स्टाम्प पेपर`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > जानकारी उपलब्ध नहीं है।

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र (affidavit) (affidavit) स्टाम्प पेपर"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र (affidavit) (affidavit) स्टाम्प पेपर"
       ```
     * **Response**:
       ```json
       राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र (affidavit) (affidavit) स्टाम्प पेपर
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र (affidavit) (affidavit) स्टाम्प पेपर"
       ```
     * **Response**:
       ```json
       The Gazette Notification Name Change Advertisement Stamp Paper vs. Marriage Affidavit (affidavit) (affidavit) Stamp Paper
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र (affidavit) (affidavit) स्टाम्प पेपर",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the difference between Rajpatra publication name change affidavit stamp paper and marriage affidavit stamp paper?', 'topic_summary': 'User is asking about two different government documents: Rajpatra publication for name change and marriage affidavit. This is a new topic as it refers to a different service than any previous conversation (which is empty).'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "राजपत्र प्रकाशन नाम परिवर्तन विज्ञापन स्टाम्प पेपर बनाम विवाह शपथ पत्र (affidavit) (affidavit) स्टाम्प पेपर",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': None, 'service_id': None}
       ```
| 17 | `क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?` | None | None | ✅ MATCH | new_topic | 42.11s |

### Query 17 Details
* **Query**: `क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?`
* **Expected Service ID**: `None`
* **Classified Service ID**: `None`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?`
* **Resolved Hindi Query**: `क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > जानकारी उपलब्ध नहीं है।

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?"
       ```
     * **Response**:
       ```json
       क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?"
       ```
     * **Response**:
       ```json
       क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या हमें ओबीसी छात्रवृत्ति आवेदन के लिए एससी प्रमाण पत्र की आवश्यकता है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': None, 'service_id': None}
       ```
| 18 | `क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर निवास प्रमाण पत्र के समान है?` | None | 4 | ❌ MISMATCH | new_topic | 10.44s |

### Query 18 Details
* **Query**: `क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर निवास प्रमाण पत्र के समान है?`
* **Expected Service ID**: `None`
* **Classified Service ID**: `4`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is the digital signature of the SDM for the ST certificate the same as the original certificate?`
* **Resolved Hindi Query**: `क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान नहीं है। मूल निवासी प्रमाण पत्र के लिए आवेदक के हस्ताक्षर की आवश्यकता होती है, जबकि एसडीएम का डिजिटल हस्ताक्षर प्रमाण पत्र जारी करने वाले अधिकारी द्वारा किया जाता है। ये दोनों अलग-अलग उद्देश्यों के लिए उपयोग किए जाते हैं।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?"
       ```
     * **Response**:
       ```json
       क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?"
       ```
     * **Response**:
       ```json
       Is the digital signature of the SDM for the ST certificate the same as the original certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'digital signature of SDM for ST certificate', 'topic_summary': 'User is asking about the digital signature of an SDM for an ST certificate, which is a different service from the previous conversation history (which was about domicile certificate).'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: SC/ST Certificate\nService ID: 4\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Domicile Certificate\n  * Supporting Document 2: Electricity Bill\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Telephone Bill\n  * Supporting Document 5: Birth Certificate\n  * Supporting Document 6: Voters Identity Card\n  * Supporting Document 7: Bpl Certificate\n  * Supporting Document 8: Land And House Document\n  * Supporting Document 9: Driving License\n  * Supporting Document 10: Other Documents\n  * Supporting Document 11: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 12: Photo Identity Card\n  * Supporting Document 13: Service Certificate Of Father / Guardian\n  * Supporting Document 14: Order Of Involuntary Migration\n  * Supporting Document 15: Domicile Certificate\n- SNo 2: Caste Proof (Mandatory: Yes)\n  * Supporting Document 1: Sc/St Certificate Of Other State\n  * Supporting Document 2: Sc/St Certificate From Sarpanch / Parshad / Mla / Mp\n  * Supporting Document 3: Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo\n  * Supporting Document 4: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 5: Educational Certificate\n  * Supporting Document 6: Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family\n  * Supporting Document 7: Primary School Certificate\n  * Supporting Document 8: Birth Information Form\n  * Supporting Document 9: Misal\n  * Supporting Document 10: Adhikar Abhilekh\n  * Supporting Document 11: Jamabandi\n  * Supporting Document 12: Census Register Of 1931\n  * Supporting Document 13: Citizen Register Of 1949\n  * Supporting Document 14: Dakhil / Kharij Panji\n  * Supporting Document 15: Disability / Unavailability Proof\n- SNo 3: Affidavit (Mandatory: No)\n  * Supporting Document 1: Affidavit\n- SNo 4: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 5: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 6: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste STSC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number\n\n--- Source 2: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 15, Col: 1)\n- Field: Police Station [Type: search, Data: Search] (Row: 16, Col: 2)\n- Field: Permanent Address on or Before Date 10 August 1950 [Type: section lebel, Data: Charactar] (Row: 17, Col: 1)\n- Field: Village or Town [Type: text, Data: Charactar] (Row: 18, Col: 1)\n- Field: Patwari Halka Number [Type: text, Data: Number] (Row: 18, Col: 2)\n- Field: Tehsil [Type: text, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: Data List, Data: Charactar] (Row: 19, Col: 2)\n- Field: Name of Head Of Family on This Date [Type: text, Data: Charactar] (Row: 20, Col: 1)\n- Field: Applicant Relation to Head of Family [Type: drop down, Data: Charactar] (Row: 20, Col: 2)\n- Field: Address Details of Year 10 August 1950 SC or 06 September 1950 ST to till Date Applicant or his Father or Mother or Guardian [Type: section lebel, Data: Charactar] (Row: 21, Col: 1)\n- Field: Is Applicant or his Father or Mother or Guardian Year 1950 to till Date live in Chhattisgarh [Type: drop down, Data: Number] (Row: 22, Col: 1)\n- Field: Address Details of Applicants Guardian [Type: fieldset, Data: Alfa Numeric] (Row: 23, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 24, Col: 1)\n- Field: Have Applicant issued scst certificate before [Type: drop down, Data: Charactar] (Row: 25, Col: 1)\n- Field: Details of document to proof that Beneficiary belongs to SC ST [Type: textarea, Data: Charactar] (Row: 25, Col: 2)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 26, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 4_en_4.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nअनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर \nऑनलाइन आवेदन\n\n--- Page 2 ---\nतवषय सूिी \nहोम पेज: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल ................................ ................................ ................................ ................................ .......... 2 \nिरण 1: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर पंजीयन ................................ ................................ ................................ .................... 3 \nिरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन................................ ................................ ................................ ................................ ............ 4 \nिरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ ............. 5 \nिरण 4: आधार ई-प्रमाणीकरण ................................ ................................ ................................ ................................ ........................ 8 \nिरण 5: अनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र के र्लए आवेदन ................................ ................................ .. 9 \nिरण 6: आवश्यक दस्तावेज़ अपलोि करना ................................ ................................ ................................ ............................ 10 \nिरण 7: पूवाावलोकन और आवेदन जमा करना ................................ ................................ ................................ ......................... 11 \nिरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ .. 0 \nिरण 9: पावर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ..........................\n\n--- Source 3: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: दी गई जानकारी भरें। \nिरण 3.2: खोजें पर क्लिक करें। \n \nचित्र क्रमाांक 5 \n \nिरण 3.3: सेवाओां की सूिी खुिेगी। इसमें  अनुसूचिर् जातर् / अनुसूचिर् जनजातर् प्रमाण पत्र देखें।  \nिरण 3.4: यक्रद यह सेवा सूिी में शातमि नहीं है तो ऊपर क्रदए गए होम बटन पर क्लिक करें। डनम्नानुसार पेज \nखुिेगा। \n \nचित्र क्रमाांक 6\n\n--- Page 7 ---\nिरण 3.5: इस पेज पर “सभी सेवाए ँ  देखें” पर क्लिक करें। सेवाओां की सूिी खुिेगी। \n \nचित्र क्रमाांक 7 \n \nिरण 3.6: सेवाओां की सूिी में से अनुसूचित जातत/अनुसूचित जनजातत प्रमाण पत्र खोजने क े  लिए सिट बार में \nसेवा का नाम टाइप करें। \n \n \nचित्र क्रमाांक 8\n\n--- Page 8 ---\nिरण 3.7: अब चित्र क्रमाांक 8 क े  अनुसार अनुसूचित जाचत/अनुसूचित जनजाचत प्रमाण पत्र क े  सामने दिए गए \nबटन पर क्लिक करें। दनम्नानुसार पेज खुलेगा \n \n \nचित्र क्रमाांक 9 \nिरण 3.7: आधार ई-प्रमाणीकरण प्रक्रक्रया क े  लिए आगे बटन पर क्लिक करें। \nइस पेज पर अनुसूचित जातत/अनुसूचित जनजातत प्रमाण पत्र हेतु आवश्यक दस्तावेज़़ों की सूिी देखी सकती है। \n \nचित्र क्रमाांक 10\n\n--- Page 9 ---\nिरण 4: आधार ई-प्रमाणीकरण \nआधार ई-प्रमाणीकरण क े  लिए डनम्नलिखखत प्रक्रक्रया का पािन करें। \n \nचित्र क्रमाांक 11 \nिरण 4.1: फॉमट में पूछी गई जानकाररयााँ दजट कर Aadhaar e-Authentication पर क्लिक करें। डनम्नानुसार \nएक पॉप-अप तविंिो खुिेगा। \n \nचित्र क्रमाांक 12 \nिरण 4.2: आधार का तववरण भरें। \nिरण 4.3: सहमतत देने क े  लिए डनधाटररत बॉक्स पर क्लिक करें। \nिरण 4.4: जानकारी भरकर Authentication बटन पर क्लिक करें। \nिरण 4.5: चित्र क्रमाांक 11 क े  अनुसार पेज पर क्रदए गए जमा करें बटन पर क्लिक करें।\n\n--- Page 10 ---\nिरण 5: अनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र क े  र्लए आवेदन \nिरण 5.1: आवेदन फॉमट में सामान्य तववरण और वतटमान पता दजट करें। \n \nचित्र क्रमाांक 13 \n \nिरण 5.2: स्थायी पते का तवव\n\n--- Source 4: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: तररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट िेकर सुरलित रखें। \n \nचित्र क्रमाांक 20 \nआवेदन संदभा क्रमांक की सहायता से आवेदन की स्थस्थतत छत्तीसगढ़ ई-डिस्ट्रिक्ट क े  पोटटि पर देखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेदन जमा करने क े  बाद डनधाटररत 22 क्रदऩों की समय-सीमा क े  अ ां दर आवेदन का डनराकरण कर क्रदया जाता है। \n• ई-डिस्ट्रिक्ट पोटटि पर आवेदन की स्थस्थतत देखी जा सकती है। \n• अनुसूचित जातत अथवा जनजातत प्रमाण पत्र जारी होने क े  उपराांत इसकी डिचजटि प्रतत ई-डिस्ट्रिक्ट पोटटि से िाउनिोि की \nजा सकती है।\n\n--- [Document: 4_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र\nService ID: 4\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: मूल निवासी प्रमाण पत्र\n  * Supporting Document 2: बिजली का बिल\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: टेलीफोन बिल\n  * Supporting Document 5: जन्म प्रमाण पत्र\n  * Supporting Document 6: वोटिंग कार्ड\n  * Supporting Document 7: बी.पी.एल. प्रमाण पत्र\n  * Supporting Document 8: घर या भूमि का दस्तावेज़\n  * Supporting Document 9: ड्राइविंग लाइसेंस\n  * Supporting Document 10: अन्य\n  * Supporting Document 11: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 12: फोटो परिचय पत्र\n  * Supporting Document 13: पिता / पालक की नौकरी का प्रमाण - पत्र\n  * Supporting Document 14: अनैच्छिक प्रवजन का आदेश\n  * Supporting Document 15: मूल निवासी प्रमाण पत्र\n- SNo 2: जाति का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: अन्य राज्य के अनुसूचित जाति / जनजाति प्रमाणपत्र\n  * Supporting Document 2: सरपंच / पार्षद / विधायक / साँसद से जाति प्रमाण-पत्र\n  * Supporting Document 3: प्राथमिक शाला या जिला शिक्षा अधिकारी द्वारा प्रमाणित प्राथमिक शाला द्वारा जारी स्थानान्तरण प्रमाण-पत्र\n  * Supporting Document 4: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 5: शैक्षणिक प्रमाण पत्र\n  * Supporting Document 6: आवेदक को या उसके किसी परिवारजन को जारी हुआ जाति प्रमाण पत्र\n  * Supporting Document 7: प्राथमिक परीक्षा उत्तीर्ण प्रमाण-पत्र\n  * Supporting Document 8: जन्म सूचना प्रपत्र\n  * Supporting Document 9: मिसल\n  * Supporting Document 10: अधिकार अभिलेख\n  * Supporting Document 11: जमाबंदी\n  * Supporting Document 12: १९३१ का जनगणना पंजी\n  * Supporting Document 13: 1949 का नागरिक पंजी\n  * Supporting Document 14: दाखिल / ख़ारिज पंजी\n  * Supporting Document 15: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 3: शपथ पत्र (Mandatory: नहीं)\n  * Supporting Document 1: शपथ पत्र\n- SNo 4: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 5: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ्तरीय सामाजिक प्रांस्थिति प्रमाण पत्र सत्यापन सनिति क सनक्ष विहित परूप में प्रस्तुत्त आवेदन पत्र में गेरे द्वारा दो गई जानंकारी मेरी सर्वोत्तम जानकारी क अनुसार सत्य एवं सही है तथा उक्त णानका२ असन्य पाए जाने पर मेरे विरूद्घ छत्तीसगढ़ अनुसूचित जाति अनुसूचित जनजाति और अन्य पिछड़ा तर्गं सामाजिक प्रास्थितिं के प्रभाणीकरण का विनियमनः अधिनियभ २०१३ की धारा 8 से १३ में निर्दिष्ट का्यवाही की जा सकेगी\nसथान दिनाँक :\nहस्ताक्षर\nसत्यापन\nआ॰ / आत्मजा / पतिं\nसत्यापित करता हूॅ कि इस शपथ पत्र की कण्डिका १ से 4 को विषयवस्तु मेरी व्यक्तिगत जानकारी एवं विश्वास क अनुसार सत्य एवं सहों हें॰ जिसे में आज दिनाँक को छत्तीरगढ़ में सत्यापित एवं हस्ताक्षरित करता हूॅू।\nहस्त्ाक्षर\n\n--- Page 27 (no rotation needed) ---\nछत्तींसगढ़ राजपत्र, दिनंक 2 सितम्बर २०१३\n788 ( 25)\nप्ररूप 3 क नियम 5 देखिये\nसक्षन प्राधिकारी का कार्यालय मंडल जिला........ छत्तीसगढ\nआवर क्रमांक\nदिनाक\nआवेदन पत्र की अभिस्वीकृति पावती\nइस ज्ञापन की मूल प्रति आवेदक को प्रदत्त्त की जावे तथाः उसका प्रतिपर्ण कार्यालय में संधारित किया जावे आज दिनांक को श्री / श्रीमती / कुमारी ' आभण़ /पत्नीं वप व्यवसाय निवासी तहसील जिला रज्य से स्ामाजिक प्रास्थिति प्रमाणनपत्र जारो करने हेतु आवेदन पत्र प्राप्त किंया गया है। उक्त आवेदन पत्र के साथ निन्नांकित दस्तावेज मूल अभिप्रमाणित प्रति गें प्राप्त्त हुए है 1 आवेदक अथवा आवेदक क पिता / पूर्वजों का निम्नांकित दस्तातेज जिसमें उरकी जाति अंकित है पूर्वजों क राजस्व दस्तावेज भिरल) जनाबंदी सर्वेक्षण गिरदावरीः 8 आष्कबंदोबशनलेख (१९५६); जनगणना (1931); (छः) वन विभाग की जनाबंदी; रात नागरिकों का राष्ट्रीय रजिस्टर १९४९ ; आट जन्म या मृत्युं की पंजीः दैस ) थिता अथवा पूर्वज के शिक्षित होने की स्थि�\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: जिरामें पर्याप्त डाक टिकट लगी हा प्रमाण-्पत्र के मामले में डाक के माध्यम से वांछित है\nहॉ / नहीं\nहॉ / नहों\nहॉ / नहों\nहॉ / नहीं\nआवदक `ा शपथ पत्र प्रारूप 2 क क अनुसार\nहॉ / नहीं\nशपथं पूर्वक कथन करता हूॅ कि आवेदन में दी गई जानकारी मेरे विश्वास अनुंसार सत्य एवं सही है.\nआवेदक क हस्ताक्षर\nस्थान दिनक\n\"7/!\"#\n\n--- Page 16 (no rotation needed) ---\n788 ( १४ )\nछत्तीसगढ राजपत्र, दिनांक 2 सितम्बर २०१३\nप्ररूप ^ ख\nनियम १५ (१) देखिये ]\nका्यालय\nस॰क\nदिनांक\nप्रत\nअध्यक्ष जिला स्तरीय प्रमाणपत्र सत्यापन समिति जिला छत्तीसगढ़\nविषय\nश्री / श्रीमती / कु० निवासी. सत्यापन के संबंध मं । सक्षम प्राधिकारी जिला कमांक दिनांक\nआन्भण आत्मजा / पति. को समाजिक\nप्रास्थिति\nसंदर्भ\nद्वारा\nजारो सामाजिक प्रास्थिति प्रमाणफत्र\nमहोदर\nश्री / श्रीमती / कु० आत्मज आत्मजा / पति. निवासी. की॰ ७कषम प्राधिकारी शारा जारी सागाजिक प्राीस्थात प्रमाणपत्र क. देनांक क आधार चर इस संस्थान / स्थानीय प्राधिकारी / चिभाग = अनुसूचित जातियों / अनुसूचित जनजातियों / अन्य पिछड़ा वर्गों के लिए आरक्षित पदों / सीट क तिरूद्घ नियुक्ति / प्रवेश / चयन कियः गया था। 2 यह शशिकायत प्राप्त होने पर कि॰ प्रमाणपत्र त्रुटिपूर्वक या कपटपूर्वक प्राप्त. किया गया है एतदद्वारा, निर्णय क़िया गया है कि जिला स्तरीय प्रमाणपत्र सत्यापन सामिति द्वारा उघरोक्त प्रमाण पत्र का सत्यापन किया जाये 3. श्री / श्रीमती / कु० .क प्रंमाणपत्र की गूल / सत्यापित्त प्रति सलग्न हे कपया विहित रीति एवं समय में उपरोक्त प्रनाण पत्र का सत्यापन करे तथा निष्कर्ष का प्रतिवेदन इस कार्यालय को दे । 4. यदि समिति प्रथभदृष्ट्या यह पाती है कि उपरोक्त सामाजिक प्रास्थिति प्रमाणयत्र त्रुटिपूर्वक या कपटपूर्वक अभिग्राप्त किया #या था॰ तो कृपया सूचित करें ताकि संबंधित आवदक क उसके दावे के समर्शन में आपके समक्ष साक्�\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: �ी करने हेतु शपथ पत्र\nमैं श्री / श्रीमती / कुमारी आत्मज / आत्मजा उम्र वर्ष व्यवसाय निवास त्तहसाल जिला र््य एतदद्वारा शपथपूर्वक निम्नलिखित कथनं करता / करती हूॅ कि .-~\nछायाचित्र\nआवदक क हस्ताकर\nमेरेद्वारा कम प्राधिकारी क समक्ष प्ररूप दा क के अधींन विहित़ अनुसार सामाजिक प्रास्थिति प्रमाण- पत्र जारी करने हेतु आवेदन किया गया है जिसके समर्थन में यह शपथ पत्र एतदद्वारा प्रस्तुत हे. मरे द्वारा सक्षम प्राधिकारी क संमक्षं विहित प्ररूप अनुसार आवेदनःःपत्र के साथ दस्तावजों को नंकल संलग्न की गईं है॰ उक्त वर्णित दस्तावेज द्वार प्राधिकृत व्यक्ति से विधि पूर्वक प्राप्त किय गय हैं॰ तथा नेर द्वारा या मेरे किसी शुभचिंतक द्वारा - उवत दस्तावज या उसक मूल दस्तावेज भें अनाधिकृत रूप से कोई संशोधन / विलोपन / परिवर्धन नहीं किया गय है तथा मेरे सर्वात्तम ज्ञान एवं जानकारी में उक्त दस्तावेज / दस्तावेजों को किस्ी विद्वेषपूर्ण आशय से गढ़ा नहीं गया है मेरे द्वारा जिन रिश्तेदारों क वेधता प्रमाणपत्र इस आवेदन क सांथ संलग्न किया गया है उनक साथ संबंध दर्शान वाला वंशवृक्ष संलग्न है एतदद्वारा घोषणा करता हूॅ कि सामाजिक प्रास्थिति प्रमाणपत्र जारी करने हेतु सक्षम प्राधिकारी क समक्ष विहित प्रपत्र में प्रस्तुत आवेदन पत्र में मेर द्वारा दी गईं रमस्त जानकारी मेरे सर्वोत्तम ज्ञान एवं जानकारी क अनुस्तार सत्य हे तथा उक्त जांनकारी असत्य पाए जाने .पर॰ मेरे विरूद्घ छत्तीसगढ़ अनुसूचित जाति अनुसूचिंत जनजाति और अन्य पिछड़ा वर्ग सामाजिक प्रास्थिति क प्रमाणीकरण कः विनियमन , अधिनियंम २०१३ को धारा 8 स १३ के अनुसार कार्यवाहींः की जावे.\n2\nहस्ताक्षर आवदक का नाम\n\n--- Page 24 (no rotation needed) ---\n788:\"22!}\nछंत्तीसग़ढ़ रांजपत्र; दिनांक 2 सितम्बर २०१३\nसत्यापन\nमैं श्री / श्रीमती / कुमारी आक़्मज आन्मजा सत्यापित करत\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या एसटी प्रमाण पत्र के लिए एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, एसडीएम का डिजिटल हस्ताक्षर मूल निवासी प्रमाण पत्र के समान नहीं है। मूल निवासी प्रमाण पत्र के लिए आवेदक के हस्ताक्षर की आवश्यकता होती है, जबकि एसडीएम का डिजिटल हस्ताक्षर प्रमाण पत्र जारी करने वाले अधिकारी द्वारा किया जाता है। ये दोनों अलग-अलग उद्देश्यों के लिए उपयोग किए जाते हैं।
       ```
| 19 | `ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें` | 5 | 5 | ✅ MATCH | new_topic | 2.06s |

### Query 19 Details
* **Query**: `ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें"
       ```
     * **Response**:
       ```json
       ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें"
       ```
     * **Response**:
       ```json
       Residence conditions in OBC non-creamy layer certificate
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी नॉन-क्रीमी लेयर प्रमाण पत्र में निवास की शर्तें",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '3', 'service_id': '5'}
       ```
| 20 | `नाम बदलने के बाद विवाह प्रमाण पत्र अपडेट कैसे होगा?` | 201 | 201 | ✅ MATCH | new_topic | 4.62s |

### Query 20 Details
* **Query**: `नाम बदलने के बाद विवाह प्रमाण पत्र अपडेट कैसे होगा?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `How will marriage registration and certificate update after name change?`
* **Resolved Hindi Query**: `नाम बदलने के बाद विवाह पंजीकरण एवं प्रमाण पत्र अपडेट कैसे होगा?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नाम बदलने के बाद विवाह पंजीकरण और प्रमाण पत्र अपडेट करने की प्रक्रिया:
  > 
  > **विवाह पंजीकरण अपडेट:**
  > - विवाह पंजीकरण में नाम बदलने के लिए अलग से आवेदन करना होगा
  > - नाम परिवर्तन प्रमाण पत्र की प्रति और विवाह प्रमाण पत्र की प्रति संलग्न करनी होगी
  > - शुल्क: 30 रुपये (ऑनलाइन या कियोस्क पर)
  > 
  > **प्रमाण पत्र अपडेट:**
  > - नाम परिवर्तन प्रमाण पत्र के लिए साधारण राजपत्र अधिसूचना (ID: 201) लागू होती है
  > - 29 दिनों का समय सीमा है
  > - आवश्यक दस्तावेज: बैंक चालान (430 रुपये), नोटरीकृत शपथ पत्र (50 रुपये), समाचार पत्र विज्ञापन, गवाहों के दस्तावेज
  > 
  > **आवेदन प्रक्रिया:**
  > - सेवा सेतु केंद्र या ऑनलाइन पोर्टल पर आवेदन करें
  > - फॉर्म में पुराना नाम, नया नाम और परिवर्तन का विवरण भरें
  > - सभी अनिवार्य दस्तावेज अपलोड करें
  > 
  > **शुल्क:**
  > - ऑनलाइन शुल्क: 30 रुपये
  > - कियोस्क शुल्क: 30 रुपये
  > - कुल शुल्क: 30 रुपये (एक ही विधि से भुगतान)
  > 
  > अधिक जानकारी के लिए सेवा सेतु पोर्टल पर जांच करें।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "नाम बदलने के बाद विवाह पंजीकरण एवं प्रमाण पत्र अपडेट कैसे होगा?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "नाम बदलने के बाद विवाह पंजीकरण एवं प्रमाण पत्र अपडेट कैसे होगा?"
       ```
     * **Response**:
       ```json
       नाम बदलने के बाद विवाह पंजीकरण एवं प्रमाण पत्र अपडेट कैसे होगा?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "नाम बदलने के बाद विवाह पंजीकरण एवं प्रमाण पत्र अपडेट कैसे होगा?"
       ```
     * **Response**:
       ```json
       How will marriage registration and certificate update after name change?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "नाम बदलने के बाद विवाह पंजीकरण एवं प्रमाण पत्र अपडेट कैसे होगा?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'विवाह पंजीकरण एवं प्रमाण पत्र अपडेट के लिए नाम बदलने के बाद क्या प्रक्रिया होगी?', 'topic_summary': 'विवाह पंजीकरण और प्रमाण पत्र अपडेट की प्रक्रिया, नाम परिवर्तन के बाद।'}
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "नाम बदलने के बाद विवाह पंजीकरण एवं प्रमाण पत्र अपडेट कैसे होगा?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नाम बदलने के बाद विवाह पंजीकरण और प्रमाण पत्र अपडेट करने की प्रक्रिया:
       
       **विवाह पंजीकरण अपडेट:**
       - विवाह पंजीकरण में नाम बदलने के लिए अलग से आवेदन करना होगा
       - नाम परिवर्तन प्रमाण पत्र की प्रति और विवाह प्रमाण पत्र की प्रति संलग्न करनी होगी
       - शुल्क: 30 रुपये (ऑनलाइन या कियोस्क पर)
       
       **प्रमाण पत्र अपडेट:**
       - नाम परिवर्तन प्रमाण पत्र के लिए साधारण राजपत्र अधिसूचना (ID: 201) लागू होती है
       - 29 दिनों का समय सीमा है
       - आवश्यक दस्तावेज: बैंक चालान (430 रुपये), नोटरीकृत शपथ पत्र (50 रुपये), समाचार पत्र विज्ञापन, गवाहों के दस्तावेज
       
       **आवेदन प्रक्रिया:**
       - सेवा सेतु केंद्र या ऑनलाइन पोर्टल पर आवेदन करें
       - फॉर्म में पुराना नाम, नया नाम और परिवर्तन का विवरण भरें
       - सभी अनिवार्य दस्तावेज अपलोड करें
       
       **शुल्क:**
       - ऑनलाइन शुल्क: 30 रुपये
       - कियोस्क शुल्क: 30 रुपये
       - कुल शुल्क: 30 रुपये (एक ही विधि से भुगतान)
       
       अधिक जानकारी के लिए सेवा सेतु पोर्टल पर जांच करें।
       ```
| 21 | `ओबीसी प्रमाण पत्र की तुलना में निवास प्रमाण पत्र की समय सीमा क्या है?` | 7 | 7 | ✅ MATCH | new_topic | 4.03s |

### Query 21 Details
* **Query**: `ओबीसी प्रमाण पत्र की तुलना में निवास प्रमाण पत्र की समय सीमा क्या है?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the validity period of a native certificate compared to an OBC certificate?`
* **Resolved Hindi Query**: `ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > मूल निवासी प्रमाण पत्र की समय सीमा 7 दिन है।
  > 
  > ओबीसी प्रमाण पत्र की समय सीमा 30 कार्य दिवस है।
  > 
  > इसलिए, मूल निवासी प्रमाण पत्र की समय सीमा ओबीसी प्रमाण पत्र की तुलना में कम है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?"
       ```
     * **Response**:
       ```json
       ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?"
       ```
     * **Response**:
       ```json
       What is the validity period of a native certificate compared to an OBC certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the timeline for the original resident certificate compared to the OBC certificate?', 'topic_summary': 'Comparison of timelines for original resident certificate and OBC certificate.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- ELIGIBILITY LOGIC RULE (Domicile): If a citizen asks about eligibility or exceptions for the Domicile Certificate, explain the rules strictly:\n  1. Main Path (Both Criteria One AND Criteria Two must be met): The applicant must satisfy AT LEAST ONE option from Criteria One (Criteria A) AND AT LEAST ONE option from Criteria Two (Criteria B).\n     * You MUST list Criteria One and Criteria Two under separate, clearly-labeled headers or bullet points.\n     * Criteria One (Criteria A) options: Birth in CG, parent resident for 25 years, parent is CG Government/PSU employee, or property in CG for 5 years.\n     * Criteria Two (Criteria B) options: 3 years of school study in CG, or passing Class 5, 8, 10, 12 board exam from CG.\n     * Never merge them into one list or omit the education requirements of Criteria Two.\n  2. Exceptions (Criteria Three / Criteria C): If they do not meet the Main Path (for example, if they lack 'Proof of 15 Years Stay' or did not study in CG), they can still get a Domicile Certificate under the exceptions of Criteria Three (C). For Criteria Three (C), Criteria A and B are NOT required. The exceptions are: (a) spouse is a domicile of CG, (b) applicant or spouse is a CG Government/PSU employee, or (c) applicant or parent is in All India Services and allotted CG Cadre.\n  3. Clarity: Never state that Criteria Three requires stay proof or education. Clearly explain that Criteria Three is a standalone set of exceptions that bypasses the need for the stay proof or CG education requirements of Criteria One and Two.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Domicile Certificate\nService ID: 7\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 7 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: Other (Mandatory: No)\n  * Supporting Document 1: Other Documents\n- SNo 3: Proof Of At Least 15 Years Stay (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate\n  * Supporting Document 2: Father/ Guardian Service Certificate\n  * Supporting Document 3: Job Service Certificate / Identity Card (If The Applicant Is Under Govt./Semi Govt.)\n  * Supporting Document 4: Voters Identity Card\n  * Supporting Document 5: Land And House Document\n  * Supporting Document 6: Birth Information Form\n  * Supporting Document 7: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 8: Ration Card\n  * Supporting Document 9: Electricity Bill\n- SNo 4: Educational Certificate (Mandatory: Yes)\n  * Supporting Document 1: Middle School Certificate - 8th Standard\n  * Supporting Document 2: Primary School Certificate - 5th Standard\n  * Supporting Document 3: High School(10th) Certificate\n  * Supporting Document 4: Higher Secondary School Certificate(12th)\n  * Supporting Document 5: M.Phil/D.Lit./Ph.D. Certificate\n  * Supporting Document 6: School Certificate (As A Proof Of 3 Years Continuous Study)\n  * Supporting Document 7: Post Graduation Certificate\n  * Supporting Document 8: Certificate In Technical Subjects\n- SNo 5: Proof Of At Least 5 Years Stay (Mandatory: No)\n  * Supporting Document 1: Land And House Document\n  * Supporting Document 2: Persons Service Book.\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Guardians Occupation of Beneficiary [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: Beneficiary place of Birth [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: Address Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 7, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: section lebel, Data: Charactar] (Row: 8, Col: 1)\n- Field: Particulars of stay After Birth of Beneficiary [Type: fieldset, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Beneficiary Details of Business or Service [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Beneficiary Details of Business or service [Type: fieldset, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Beneficiary Education Level [Type: section lebel, Data: Charactar] (Row: 12, Col: 1)\n- Field: Beneficiary Education Level [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Have Beneficiary Voter Id [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: District Name of Beneficiary [Type: drop down, Data: Charactar] (Row: 15, Col: 2)\n- Field: Living From in Years [Type: number, Data: Date] (Row: 16, Col: 1)\n- Field: Reason for application Domicile [Type: text, Data: Charactar] (Row: 16, Col: 2)\n- Field: Any other detail [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 17, Col: 2)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 7_en_7.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nउपयोगकर्ता मतगादर्शिकत \n \n  \nमूल निवतसी प्रमतण पत्र क े  र्लए ई-निस्ट्रिक्ट पोर्ाल पर ऑिलतइि आवेदि प्रक्रियत \n \nछत्तीसगढ़ इन्फोर्ेक प्रमोशि सोसतयर्ी\n\n--- Page 2 ---\nववषय सूची \nहोम पेजः छत्तीसगढ़ ई-निस्ट्रिक्ट पोर\n\n--- Source 2: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �िगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह पेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 3: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: 4.4: डनर्ाटररत बॉक्स पर क्लिक करक े  आर्ार प्रमाणीकरण हेतु सहमगत िें। \nचरण 4.5: “Authentication”  बटन पर क्लिक करें। \nचरण 4.6: आर्ार ई-प्रमाणीकरण क े  बाि “जमत करें” बटन पर क्लिक करें।  \nडनम्नानुसार पॉप-अप गविंिो खुलेगा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पू�\n\n--- Source 4: [Official Specification (English)] ---\nService: Domicile Certificate (ID: 7)\nSection: combined_manual\nContent:\nService: Domicile Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पूवतावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचरण 7.2: घोषणत: घोर्षणा हेतु डनर्ाटररत बॉक्स पर क्लिक करें। \nचरण 7.3: घोर्षणा पर क्लिक करते ही “जमत करें” बटन दिखाई िेगा, इस पर क्लिक करें, इस तरह आवेिन \nजमा हो जाएगा। \n \nचित्र क्रमांक 19\n\n--- Page 15 ---\nचरण 8: शुल्क कत भुगर्ति \nइस पेज पर लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवा शुल्क एवं स्क ै डनिंग शुल्क का गववरण िेख सकते \nहैं। \n \nचित्र क्रमांक 15 \n \nचरण 8.1: डनर्ाटररत शुल्क का भुगतान करें। \nचरण 8.2: भुगतान क े  पश्चात् “जमत करें” बटन पर क्लिक करें। \n \nिोर्: \n• लोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  ललए सेवत शुल्क रु. 30 डनर्ाटररत हैं। \n• सेवा शुल्क में  पताँच दस्ततवेज़़ों तक स्क ै डनिंग का शुल्क भी शागमल है। अगतररक्त िस्तावेज़़ों की स्क ै डनिंग का शुल्क पृथक से \nलोकसेवा क ें द्र/ सीएससी/डकयोस्क संिालक द्वारा ललया जा सकता है।\n\n--- Page 16 ---\nचरण 9: पतवर्ी सुरक्षिर् रखित \nआवेिन जमा करते ही चित्रानुसार पावती जेनरेट हो जाती है।  \nइस पावती में “आवेदि संदभा िमतंक” प्रिचशित होता है। \nभगवष्य की आवश्यकताओं और आवेिन की स्थिगत िेखने क े  ललए आवेिक इस पावती का दप्रिंट आउट रख लें। \n \nचित्र क्रमांक 20\n\n--- Page 17 ---\nचरण 10: आवेदि की स्थिवर् देखित \nचरण 10.1: आवेिन की स्थिगत िेखने क े  ललए होम पेज पर आवेिन की स्थिगत मेन्यू पर क्लिक करें। \nयह\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: मूल निवासी प्रमाण पत्र\nService ID: 7\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 7 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य\n- SNo 3: १५ वर्ष तक निवास का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: जन्म प्रमाण पत्र\n  * Supporting Document 2: पिता/पालक का सेवा प्रमाण पत्र\n  * Supporting Document 3: नौकरी प्रमाणपत्र /पहचान पत्र (यदि आवेदक शासकीय /अर्ध शासकीय अधीनस्थ हो )\n  * Supporting Document 4: वोटिंग कार्ड\n  * Supporting Document 5: घर या भूमि का दस्तावेज़\n  * Supporting Document 6: जन्म सूचना प्रपत्र\n  * Supporting Document 7: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 8: राशन कार्ड\n  * Supporting Document 9: बिजली का बिल\n- SNo 4: शैक्षणिक प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: माध्यमिक विद्यालय का प्रमाणपत्र -8 कक्षा\n  * Supporting Document 2: प्राथमिक विद्यालय का प्रमाणपत्र - 5वीं कक्षा\n  * Supporting Document 3: हाई स्कूल(10वी कक्षा) अंकसूची\n  * Supporting Document 4: उच्चतर माध्यमिक विधालय प्रमाण पत्र(१२ वीं कक्षा)\n  * Supporting Document 5: एम-फिल\n  * Supporting Document 6: स्कूल प्रमाणपत्र (3 साल की एक सबूत निरंतर अध्ययन के रूप में)\n  * Supporting Document 7: स्नातकोत्तर प्रमाणपत्र\n  * Supporting Document 8: तकनीकी विषयों में प्रमाणपत्र\n- SNo 5: ५ साल निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: घर या भूमि का दस्तावेज़\n  * Supporting Document 2: व्यक्ति की सेवा पुस्तिका.\n\nAPPLICATION FORM FIELDS:\n- Field: सामान्य विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: हितग्राही के अभिभावक का प्रकार [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: हितग्राही के अभिभावक का नाम [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: हितग्राही के अभिभावक का व्यवसाय [Type: search, Data: Search] (Row: 3, Col: 1)\n- Field: हितग्राही का जन्म स्थान [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: लिंग [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 4, Col: 2)\n- Field: पता का विवरण [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: पता [Type: textarea, Data: Alfa Numeric] (Row: 6, Col: 1)\n- Field: पिन कोड [Type: text, Data: Number] (Row: 6, Col: 2)\n- Field: जिला [Type: drop down\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ेज खुलेगा – \n \nचित्र क्रमांक 21 \n \nचरण 10.2: आवेिन संिभट क्रमांक एवं चसस्टम प्रित्त क ै प्िा डनर्ाटररत िान पर िजट करें। \nचरण 10.3: स्थिवर् िैक करें बटन पर क्लिक करें। \nडनम्नानुसार गविंिो खुलेगा यहााँ आवेिक आवेिन की स्थिगत िेख सकते हैं। \n \nचित्र क्रमांक 22 \n \nचरण 10.4: डिचजटल प्रगत िाउनलोि – मूल डनवासी प्रमाण पत्र जारी होने क े  बाि उपरोक्त गविंिो में “देखें” बटन \nपर क्लिक कर िाउनलोि करें।\n\n--- [Document: 7_hi_citizenCharter.pdf (SLA_DETAILS)] ---\nछत्तीसगढ़ शासन\nराजस्व एवं आपदा प्रबंधन विभाग\nमंत्रालय\nमहानदी भवन नया रायपुर\n::: अधिसूचना :::\n\nरायपुर, दिनांक 16/05/2013\n\nक्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\nसारणी (SLA Details):\n1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n2. स्थाई जाति प्रमाण-पत्र (Permanent Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - सक्षम प्राधिकारी: कलेक्टर\n   - अपीलीय अधिकारी: कमिश्नर\n\n3. निवास प्रमाण-पत्र (Domicile Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्र\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: �ीय अधिकारी (राजस्व)\n   - सक्षम प्राधिकारी: कलेक्टर\n   - अपीलीय अधिकारी: कमिश्नर\n\n3. निवास प्रमाण-पत्र (Domicile Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n4. आय प्रमाण-पत्र (Income Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\nछत्तीसगढ़ के राज्यपाल के नाम से तथा आदेशानुसार\n(पी. निहलानी)\nसंयुक्त सचिव, छत्तीसगढ़ शासन, राजस्व एवं आपदा प्रबंधन विभाग\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: मूल निवासी प्रमाण पत्र (ID: 7)\nSection: combined_manual\nContent:\nService: मूल निवासी प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ा, चजसमें सहायक िस्तावेज़़ों क े ललए जााँि सूिी प्रिचशित है। \n \nचित्र क्रमांक 11 \n \nचरण 4.6: उपरोक्त गविंि़ों में “जमत” बटन पर क्लिक कर िें। \n \nनोट: मूल डनवासी प्रमाण पत्र बनवाने क े  ललए शपथ पत्र, फोटोग्राफ, 15 वर्षों क े  डनवास का प्रमाण, शैक्षलणक प्रमाण पत्र \nअडनवायट है।\n\n--- Page 10 ---\nचरण 5: मूल निवतसी प्रमतण पत्र क े  र्लए आवेदि \nचरण 5.1: मूल डनवासी प्रमाण पत्र क े  ललए आवेिन में पहले सामान्य गववरण, पता एवं दहतग्राही क े  जन्म क े  बाि \nडनवास का गववरण भरें। \n \nचित्र क्रमांक 12 \n \nचरण 5.2: दहतग्राही क े  रोज़गार, चशक्षा संबंर्ी एवं अन्य गववरण भरें। \n \nचित्र क्रमांक 13 \n \nचरण 5.3: सारे गववरण भरकर “सहेजें और पूवतावलोकि” बटन पर क्लिक करें।\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्ततवेज़ अपलोि करित \nभरा हुआ फॉमट सहेजने क े  बाि डनम्न चित्रानुसार पेज खुलेगा। \n \nचित्र क्रमांक 14 \nचरण 6.1: “Choose File” पर क्लिक करें और अपने कम्प्यूटर या लैपटॉप से फोटोग्राफ तथा संबंचर्त \nिस्तावेज़ों की स्क ै न की गई प्रगत का ियन करें। \nचरण 6.2: िस्तावेज़ िुनने क े  बाि “UPLOAD”  पर क्लिक करें। \nचरण 6.3: अपलोि प्रदक्रया क े  बाि “अिुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुदिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें। \n \n \nनोट: \n• तारांडकत (*) िस्तावेज़ अपलोि करना अडनवायट है। \n• हैश (#) चिह्ांडकत िस्तावेज़़ों में डनवास का न्यूनतम एक प्रमाण तथा शैक्षलणक प्रमाण पत्र प्रस्तुत करना अडनवायट है।  \n• फाइल का अचर्कतम आकार 750kb होना िादहए।\n\n--- Page 12 ---\n\n\n--- Page 13 ---\nचरण 7: पूवतावलोकि और आवेदि जमत करित \nपूवाटवलोकन पेज पर आवेिक की बुडनयािी जानकारी एवं सामान्य गववरण िेखे जा सकते हैं। \nचरण 7.1: अपने आवेिन की जांि करें। \n \nचित्र क्रमांक 16 \n \n \nचित्र क्रमांक 17\n\n--- Page 14 ---\nचित्र क्रमांक 18 \n \nचर\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "ओबीसी प्रमाण पत्र की तुलना में मूल निवासी प्रमाण पत्र की समय सीमा क्या है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       मूल निवासी प्रमाण पत्र की समय सीमा 7 दिन है।
       
       ओबीसी प्रमाण पत्र की समय सीमा 30 कार्य दिवस है।
       
       इसलिए, मूल निवासी प्रमाण पत्र की समय सीमा ओबीसी प्रमाण पत्र की तुलना में कम है।
       ```
| 22 | `जाति प्रमाण पत्र एसटी एससी वैधता बनाम निवास प्रमाण पत्र वैधता` | 4 | 4 | ✅ MATCH | new_topic | 3.74s |

### Query 22 Details
* **Query**: `जाति प्रमाण पत्र एसटी एससी वैधता बनाम निवास प्रमाण पत्र वैधता`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `The validity of caste certificate for ST/SC vs. original resident certificate validity.`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > अनुसूचित जाति/अनुसूचित जनजाति प्रमाण पत्र (एसटी/एससी प्रमाणपत्र) की वैधता 22 दिन है, जबकि मूल निवासी प्रमाण पत्र (डोमिसाइल प्रमाणपत्र) की वैधता 30 दिन है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता"
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता"
       ```
     * **Response**:
       ```json
       The validity of caste certificate for ST/SC vs. original resident certificate validity.
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'जाति प्रमाण पत्र और मूल निवासी प्रमाण पत्र की वैधता की तुलना', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: SC/ST Certificate\nService ID: 4\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Domicile Certificate\n  * Supporting Document 2: Electricity Bill\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Telephone Bill\n  * Supporting Document 5: Birth Certificate\n  * Supporting Document 6: Voters Identity Card\n  * Supporting Document 7: Bpl Certificate\n  * Supporting Document 8: Land And House Document\n  * Supporting Document 9: Driving License\n  * Supporting Document 10: Other Documents\n  * Supporting Document 11: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 12: Photo Identity Card\n  * Supporting Document 13: Service Certificate Of Father / Guardian\n  * Supporting Document 14: Order Of Involuntary Migration\n  * Supporting Document 15: Domicile Certificate\n- SNo 2: Caste Proof (Mandatory: Yes)\n  * Supporting Document 1: Sc/St Certificate Of Other State\n  * Supporting Document 2: Sc/St Certificate From Sarpanch / Parshad / Mla / Mp\n  * Supporting Document 3: Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo\n  * Supporting Document 4: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 5: Educational Certificate\n  * Supporting Document 6: Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family\n  * Supporting Document 7: Primary School Certificate\n  * Supporting Document 8: Birth Information Form\n  * Supporting Document 9: Misal\n  * Supporting Document 10: Adhikar Abhilekh\n  * Supporting Document 11: Jamabandi\n  * Supporting Document 12: Census Register Of 1931\n  * Supporting Document 13: Citizen Register Of 1949\n  * Supporting Document 14: Dakhil / Kharij Panji\n  * Supporting Document 15: Disability / Unavailability Proof\n- SNo 3: Affidavit (Mandatory: No)\n  * Supporting Document 1: Affidavit\n- SNo 4: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 5: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 6: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste STSC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number\n\n--- Source 2: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: तररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट िेकर सुरलित रखें। \n \nचित्र क्रमाांक 20 \nआवेदन संदभा क्रमांक की सहायता से आवेदन की स्थस्थतत छत्तीसगढ़ ई-डिस्ट्रिक्ट क े  पोटटि पर देखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेदन जमा करने क े  बाद डनधाटररत 22 क्रदऩों की समय-सीमा क े  अ ां दर आवेदन का डनराकरण कर क्रदया जाता है। \n• ई-डिस्ट्रिक्ट पोटटि पर आवेदन की स्थस्थतत देखी जा सकती है। \n• अनुसूचित जातत अथवा जनजातत प्रमाण पत्र जारी होने क े  उपराांत इसकी डिचजटि प्रतत ई-डिस्ट्रिक्ट पोटटि से िाउनिोि की \nजा सकती है।\n\n--- [Document: 4_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and\n\n--- Source 3: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �ारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 4: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �् जनजातर् प्रमाण पत्र के र्लए आवेदन ................................ ................................ .. 9 \nिरण 6: आवश्यक दस्तावेज़ अपलोि करना ................................ ................................ ................................ ............................ 10 \nिरण 7: पूवाावलोकन और आवेदन जमा करना ................................ ................................ ................................ ......................... 11 \nिरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ .. 0 \nिरण 9: पावर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ .......................... 1\n\n--- Page 3 ---\nहोम पेज: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nअनुसूचित जातत/अनुसूचित जनजातत प्रमाण पत्र क े  लिए ऑनिाइन आवेदन हेतु अपने कम्प्यूटर या िैपटॉप क े  \nवेब ब्राउज़र में टाइप करें \ncgedistrict.cgstate.gov.in \n \nछत्तीसगढ़ ई-डिस्ट्रिक्ट पोटटि का होम पेज खुिेगा। \n \nचित्र क्रमाांक 1\n\n--- Page 4 ---\nिरण 1: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर पंजीयन \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटटि पर डनम्न प्रक्रक्रया द्वारा रचजस्टर करें। \n \nचित्र क्रमाांक 2 \nिरण 1.1: नए पांजीयन हेतु क्रदए गए लििंक पर क्लिक करें, डनम्नानुसार नागररक पांजीकरण पेज खुिेगा। \n \nचित्र क्रमाांक 3 \n \nिरण 1.2: नागररक पांजीकरण पेज पर आवेदक उपयोगकताट नाम दजट करें। \nिरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ दजट करें। \nिरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रचजरिेशन प्रक्रक्रया पूणट होती है।\n\n--- Page 5 ---\nिरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nडनम्न प्रक्रक्रया द्वारा पांजीक ृ त उपयोगकताट िॉतगन करें। \n \nचित्र क्रमाांक 4 \n1. यूज़रनेम दजट करें। \n2. पासविा दजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पांजीक ृ त नांबर पर प्राप्त ओटीपी यहााँ दजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nिरण 3: योजना खोज \nिरण 3.1: योजना खोज पेज में दी गई जानकारी भरें। \nिरण 3.2: खोजें पर क्लिक करें। \n \nचित्र क्रमाांक 5 \n \nिरण 3.3: सेवाओां की सूिी खुिेगी। इसमें  अनुसूचिर् जातर् / अनुसूचिर् जनजातर् प्रमाण पत्र देखें।  \nिरण 3.4: यक्रद यह सेवा सूिी में शातम\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र\nService ID: 4\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: मूल निवासी प्रमाण पत्र\n  * Supporting Document 2: बिजली का बिल\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: टेलीफोन बिल\n  * Supporting Document 5: जन्म प्रमाण पत्र\n  * Supporting Document 6: वोटिंग कार्ड\n  * Supporting Document 7: बी.पी.एल. प्रमाण पत्र\n  * Supporting Document 8: घर या भूमि का दस्तावेज़\n  * Supporting Document 9: ड्राइविंग लाइसेंस\n  * Supporting Document 10: अन्य\n  * Supporting Document 11: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 12: फोटो परिचय पत्र\n  * Supporting Document 13: पिता / पालक की नौकरी का प्रमाण - पत्र\n  * Supporting Document 14: अनैच्छिक प्रवजन का आदेश\n  * Supporting Document 15: मूल निवासी प्रमाण पत्र\n- SNo 2: जाति का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: अन्य राज्य के अनुसूचित जाति / जनजाति प्रमाणपत्र\n  * Supporting Document 2: सरपंच / पार्षद / विधायक / साँसद से जाति प्रमाण-पत्र\n  * Supporting Document 3: प्राथमिक शाला या जिला शिक्षा अधिकारी द्वारा प्रमाणित प्राथमिक शाला द्वारा जारी स्थानान्तरण प्रमाण-पत्र\n  * Supporting Document 4: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 5: शैक्षणिक प्रमाण पत्र\n  * Supporting Document 6: आवेदक को या उसके किसी परिवारजन को जारी हुआ जाति प्रमाण पत्र\n  * Supporting Document 7: प्राथमिक परीक्षा उत्तीर्ण प्रमाण-पत्र\n  * Supporting Document 8: जन्म सूचना प्रपत्र\n  * Supporting Document 9: मिसल\n  * Supporting Document 10: अधिकार अभिलेख\n  * Supporting Document 11: जमाबंदी\n  * Supporting Document 12: १९३१ का जनगणना पंजी\n  * Supporting Document 13: 1949 का नागरिक पंजी\n  * Supporting Document 14: दाखिल / ख़ारिज पंजी\n  * Supporting Document 15: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 3: शपथ पत्र (Mandatory: नहीं)\n  * Supporting Document 1: शपथ पत्र\n- SNo 4: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 5: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ाए॰ सामाजिक प्रास्थिति प्रमाणपत्र जारी करेगा\nपरंतु जहां सक्षम प्राधिकारी का निष्कर्ष हो कि ऐसे प्रमाणपत्र के लिए आवेदन के निरस्त किये जाने का पर्याप्त कारण है॰ तो निरस्त करने के कारणों को लिखित में अभिलिखित करेगा तथा तदनुसार आवेदक को सूचित करेगा.\n(2)\nइस धारा की उप- धारा (१ ) के अधीन सक्षम प्राधिकारी द्वारा जारी सामाजिक प्रास्थिति प्रमाणपत्र, स्थायी प्रकृति का दस्तावेज होगाः जिसकी वैधता समय द्वारा सीमित नहीं होगीः\nपरन्तु जबं आवेदक मूल प्रमाणपत्र खो जाने की घोषणा करता है तब ही सक्षम प्राधिकारी द्वारा सामाजिक प्रास्थिति प्रमाणपत्र की डुप्लीकेट प्रति जारी की जा सकेगी.\n(3)\nसक्षम प्राधिकारी से भिन्न किसी व्यक्ति, अधिकारी या प्राधिकारी द्वारा जारी सामाजिक प्रास्थिति प्रमाणपत्र, किसी लोक नियोजन, शैक्षणिक संस्थान में प्रवेश या अनुसूचित जातियों या अनुसूचित जनजातियों या अन्य पिछड़े वर्गों को उपार्जित किसी लाभ के उपभोग के प्रयोजन के लिए स्वीकार नहीं किया जाएगाः\nअपील.\n5\n(1.)\nधारा 4 के अधीन सक्षम प्राधिकारी के आदेश से व्यथित कोई आवेदक ऐसे आदेश की प्राप्ति की तारीख से ३० दिवस के भीतर, अपीलीय प्राधिकारी के समक्ष अपील प्रस्तुत कर सकेगा\nपरन्तु अपीलीय प्राधिकारी लिखित में पर्याप्त कारण अभिलिखित करने के पश्चात् ऐसे अपील के प्रस्तुत होने में हुए विलंब को क्षम्य कर सकेगा.\n(2 )\nअपीलीय प्राधिकारी, तीन माह की कालावधि के भीतर, आवेदक को सुनवाई का युक्तियुक्त अवसर देने के पश्चात् ऐसे निर्देशों, जो कि समुचित समझे जायें, के साथ सक्षम प्राधिकारी के आदेश की या तो पुष्टिया अपास्त कर सकेगा़.\nअध्याय-्तीन\nसामाजिक प्रास्थिति प्रमाणपत्र का सत्यापन\nजिला स्तंरीय प्रमाणपत्र सत्यापन समिति तथा इसकी शक्तियां.\n6\n(1)\nराज्य शासन द्वारा अधिसूचित किए गए अनुसार, धारा 4 कें अधीन सक्षम प्राधिकारी द्वारा जारी सामाजिक प्रास्थिति प्रमाणपत्र के सत\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ो।\nप्राप्तकर्ता क हस्ताक्षर एवं पदमुद्रा\n\n--- Page 28 (no rotation needed) ---\n788 २६ २९-\nछत्तोसगढ़ राजपत्र टिनांक 2 सितम्बर २०१३\nप्ररूप 3 ख [ नियम ६२ ]\nसक्षम प्राधिकारी का कार्यालय\nआदेदन पत्र क वापसी का ज्ञापनं वापसी झापन)\n(इप् ज्ञापन की मूल प्रति आवेदक को प्रदत्त की जावे तथा उसूका प्रतिपर्ण कार्यालय में संधारित किया जावे\nकमांक\nदिनांक\nश्र श्रीमती / कुमारी आत्मज आन्मजा निवासी द्वारा सामाजिक प्रास्थिति प्रमाणन्पत्र जारी करने हेतु प्रस्तुत आवेदन पत्र में निम्नाकित अभिलेखों क अभाव है॰ अतः अवेदक को निर्देशित किया जाता है कि निम्नांकित अंभिलेख जिनमें सही * का निशान अंकित किया गया है आवेदन पत्र॰के साथ प्रस्तुत करने पर उसके सामाजिए प्रास्थिति प्रगाण-् पत्र जारी करने की कार्यवाही प्रारंभ कीजा सकगीः- (1 ) आवेदक अथवा आवेदक क पिता / पूर्वजों का निम्नांकित दस्तावेज जिसमें उसकी जाति अंकित है पूर्वजों के राजस्व दस्तावेज गिशल) जमाबंदी सर्वेक्षण गिरदावरीः 8 सष्चियबंदोबस्तिलेख (१९५ ; जनगणना (१९३१ ; (छः) वन विभाग की जमाबंदीः नागरिकों का राष्ट्रीय रजिस्टर (१९३९ ; ६ जन्म यां मृत्यु की पंजपीः पिता अथवा पूर्वज के शिक्षित होने को स्थिति में प्रवेश दाखिल / खारिज) पंजी पिताः पूर्वज अथवा संबंधी नातेदार को पूर्व में जारी जाति ग्रगाण प्रमाण-पत्र कों प्रात ग्राारह अन्य दस्तावे जिसस आवेदक क द्वारा दावा की गई जाति होनां प्रमाणित होता है बारह\n(2) ऐरो दस्तावेज अथवा दस्त्तावेजों की रूम्यक रूप सें अंभिप्रभाणित प्रतिलिपि अथवा प्रतिलिपियां जिससे यह प्रमाणित हो सके के आवेदक के पूर्वज राष्ट्रपतीय अधिसूचना तिथि अथवा अन्ग गिछड़ा वर्गकी अधिस्चना तिथि के पूर्व से छत्तीरागड की भैगोलिक सीमा में निवास करते थे। पूर्वजों सेः प्रारंभ कर आवेदक तक पटवारी से प्रदत्त वंशावली ( आवेदक अ�\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ूप 3 घ\n[ नियम १६८२) देखिये ]\nकार्यालय जिला स्तरीय प्रमाणपत्र सत्यापन समिति जिला \"+-+k677+ छत्तीसगढ़ दिनाक आवेंदन पत्र की पावती\nआवक क्रमांक\nइस ज्ञाघन की मूल प्रति आवेदक को प्रदत्त की जावे तथा उसका प्रतिपर्ण कार्यालय में संधारित किया जावे)\nआज दिनांक कोश्री / श्रीमती / कुमारी अत्मज _ आसना व्यवसाय निवासी तहसाल जिला रम्य से सामाजिक प्रास्थिति प्रमाण पत्र सत्यापित्त करने हेतु आवेदन पत्र प्राप्त किया॰गया है॰ उक्त आदेदन पत्र के साथ निन्नांकित अभिलेख मूल / अभिप्रमाणित प्रति ऐं प्राप्त हुए है ४४ आवेदक अथवा आवेदक क पिता / पूर्दजों का निम्नांकित दस्तावेज जिसमें उसकी जाति अंकित है पूर्वजों क राजस्व दस्तावेज गिसल जमाबंदी सर्वेक्षण गिरदावरीः 8 आष्चयक बरंद बसमनिलेख (१९५४): जनगणना १९३१ ; छः दन विभाग को जमाबंदीः नागरिकों का राष्ट्रीय रजिस्टर १९४९ ; जन्म या मृत्यु की पंजीः ३ पिता अथदा पूर्वज क शिक्षित होने की स्थित्ति में॰ प्रवेश दाखि़ल / खारिज पंजी पिता पूर्वज अथग संबंधी नातेदार को पूर्व में जारी जाति प्रमाण प्रमाण पत्र की प्रति अन्यं दस्तावेज जिससे आवेदक क द्वारा दावा की गई जाति होना प्रगाणित होत्ता है दारह\n!2; ऐसे दस्तावज अथवा दस्तवेजों को सम्यक रूप से अभिप्रमाणित प्रतिलेिपि अथवा प्रलिलिपियॉ चिससे यह प्रमाणत हा सके कं आवंदक के पूवेज राष्ट्रपतीय अघेसूंचनाः नतिथि अथव अन्य पिेछड़ा वग़ को अघिसूचना तिथि ऊं पूर्व से छत्तीसगढ़ की भौगोलिक सीमा में निवांस करते थे। ` पूर्वजों से परंभ फर शापेदफ तावः पच्यारी से प्रदता नंशावली । आवदकं अथवा उसक पेता अथवा उसदः वैध पालक का शय२ प= प्ररूप २क क अनुस्तार मूल प्रति में दस्तावंज फ़िनत्ते नर्शित हा कि आवदक क पिता सज्य सरकार के अधकारी / फ॰ ारी हैं तथ राष्ट्रपत्तीय अधेसूचन\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "जाति प्रमाण पत्र एसटी एससी वैधता बनाम मूल निवासी प्रमाण पत्र वैधता\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       अनुसूचित जाति/अनुसूचित जनजाति प्रमाण पत्र (एसटी/एससी प्रमाणपत्र) की वैधता 22 दिन है, जबकि मूल निवासी प्रमाण पत्र (डोमिसाइल प्रमाणपत्र) की वैधता 30 दिन है।
       ```
| 23 | `बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम` | 3 | 3 | ✅ MATCH | new_topic | 2.33s |

### Query 23 Details
* **Query**: `बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम"
       ```
     * **Response**:
       ```json
       बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम"
       ```
     * **Response**:
       ```json
       Marriage registration for out-of-state residence offline location Raipur Municipal Corporation rules
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'marriage registration offline location rules for residents from outside state in Raipur Municipal Corporation', 'topic_summary': 'Query about marriage registration process and location rules for non-resident Indians in Raipur Municipal Corporation.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "बाहरी राज्य के निवास के लिए विवाह पंजीकरण ऑफ़लाइन स्थान रायपुर नगर निगम के नियम",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '1', 'service_id': '3'}
       ```
| 24 | `तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम` | 201 | 201 | ✅ MATCH | new_topic | 2.48s |

### Query 24 Details
* **Query**: `तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम"
       ```
     * **Response**:
       ```json
       तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम"
       ```
     * **Response**:
       ```json
       The Gazette Notification Rules for Name Change after Divorce Decree
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'divorce ke faisle ke baad naam badalne ke liye rajpatra adhisuchana niyam', 'topic_summary': 'User is asking about the rules for issuing a government notification (rajpatra adhisuchana) for name change after a divorce.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "तलाक के फैसले के बाद नाम परिवर्तन के लिए राजपत्र अधिसूचना नियम",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
| 25 | `माता के निवास प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन` | 4 | 4 | ✅ MATCH | new_topic | 7.23s |

### Query 25 Details
* **Query**: `माता के निवास प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `SC certificate application with mother's native place certificate of origin.`
* **Resolved Hindi Query**: `माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > सेवा सेतु पोर्टल पर अनुसूचित जाति प्रमाण पत्र के लिए आवेदन करने के लिए, आपको निम्नलिखित दस्तावेजों की आवश्यकता होगी:
  > 
  > **आवश्यक दस्तावेज:**
  > 
  > 1. **निवास प्रमाण:**
  >    - मूल निवासी प्रमाण पत्र (अनिवार्य)
  >    - बिजली का बिल
  >    - राशन कार्ड
  >    - टेलीफोन बिल
  >    - जन्म प्रमाण पत्र
  >    - वोटर आई डी कार्ड
  >    - बी पी एल प्रमाण पत्र
  >    - भूमि और घर का दस्तावेज
  >    - ड्राइविंग लाइसेंस
  >    - अन्य दस्तावेज
  > 
  > 2. **जाति प्रमाण:**
  >    - अन्य राज्य के अनुसूचित जाति/जनजाति प्रमाण पत्र (अनिवार्य)
  >    - सरपंच/पार्षद/विधायक/सांसद से जाति प्रमाण-पत्र (अनिवार्य)
  >    - प्राथमिक स्कूल का स्थानांतरण प्रमाण-पत्र
  >    - पिता/अभिभावक की सेवा प्रमाण पत्र/पहचान पत्र
  >    - शैक्षणिक प्रमाण पत्र
  >    - आवेदक को जारी जाति प्रमाण पत्र (अनिवार्य)
  >    - प्राथमिक स्कूल का प्रमाण-पत्र
  >    - जन्म सूचना प्रपत्र
  >    - मिसल
  >    - अधिकार अभिलेख
  >    - जमाबंदी
  >    - जनगणना पंजी (1931)
  >    - नागरिक पंजी (1949)
  >    - दाखिल/खारिज पंजी
  >    - अक्षमता/अनुपलब्धता का प्रमाण
  > 
  > 3.   - शपथ पत्र (अनिवार्य नहीं)
  >    - वंशावली (अनिवार्य नहीं)
  >    - ग्राम सभा प्रस्ताव (ग्रामीण क्षेत्रों के लिए) (अनिवार्य नहीं)
  > 
  > **आवेदन प्रक्रिया:**
  > 
  > 1. सेवा सेतु पोर्टल पर पंजीकरण करें।
  > 2. आवेदन फॉर्म में सामान्य विवरण भरें।
  > 3. स्थायी पते का विवरण दजट करें और सहेजें।
  > 4. आवश्यक दस्तावेज अपलोड करें।
  > 5. आवेदन जमा करें।
  > 6. शुल्क का भुगतान करें (30 रुपये)।
  > 7. आवेदन की स्थिति ट्रैक करें।
  > 
  > **शुल्क:**
  > - सेवा शुल्क: 30 रुपये (ऑनलाइन या कियोस्क पर)।
  > - कुल शुल्क: 30 रुपये (एक ही भुगतान विधि)।
  > 
  > **समय सीमा:**
  > - आवेदन का समाधान: 22 दिन।
  > 
  > **महत्वपूर्ण:**
  > - सभी अनिवार्य दस्तावेज आवश्यक हैं।
  > - आवेदन जमा करने के बाद पावती प्राप्त होगी।
  > - आवेदन की स्थिति ऑनलाइन ट्रैक की जा सकती है।
  > - प्रमाण पत्र जारी होने के बाद इसकी प्रति ई-डिस्ट्रिक्ट पोर्टल से डाउनलोड की जा सकती है।
  > 
  > अधिक जानकारी के लिए सेवा सेतु पोर्टल पर जांच करें।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन"
       ```
     * **Response**:
       ```json
       माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन"
       ```
     * **Response**:
       ```json
       SC certificate application with mother's native place certificate of origin.
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': "What is the process for applying for an SC certificate with mother's native residence proof?", 'topic_summary': "User is inquiring about the application process for an SC certificate, specifically mentioning the mother's original residence proof as a required document."}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: SC/ST Certificate\nService ID: 4\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Domicile Certificate\n  * Supporting Document 2: Electricity Bill\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Telephone Bill\n  * Supporting Document 5: Birth Certificate\n  * Supporting Document 6: Voters Identity Card\n  * Supporting Document 7: Bpl Certificate\n  * Supporting Document 8: Land And House Document\n  * Supporting Document 9: Driving License\n  * Supporting Document 10: Other Documents\n  * Supporting Document 11: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 12: Photo Identity Card\n  * Supporting Document 13: Service Certificate Of Father / Guardian\n  * Supporting Document 14: Order Of Involuntary Migration\n  * Supporting Document 15: Domicile Certificate\n- SNo 2: Caste Proof (Mandatory: Yes)\n  * Supporting Document 1: Sc/St Certificate Of Other State\n  * Supporting Document 2: Sc/St Certificate From Sarpanch / Parshad / Mla / Mp\n  * Supporting Document 3: Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo\n  * Supporting Document 4: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 5: Educational Certificate\n  * Supporting Document 6: Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family\n  * Supporting Document 7: Primary School Certificate\n  * Supporting Document 8: Birth Information Form\n  * Supporting Document 9: Misal\n  * Supporting Document 10: Adhikar Abhilekh\n  * Supporting Document 11: Jamabandi\n  * Supporting Document 12: Census Register Of 1931\n  * Supporting Document 13: Citizen Register Of 1949\n  * Supporting Document 14: Dakhil / Kharij Panji\n  * Supporting Document 15: Disability / Unavailability Proof\n- SNo 3: Affidavit (Mandatory: No)\n  * Supporting Document 1: Affidavit\n- SNo 4: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 5: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 6: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste STSC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number\n\n--- Source 2: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 15, Col: 1)\n- Field: Police Station [Type: search, Data: Search] (Row: 16, Col: 2)\n- Field: Permanent Address on or Before Date 10 August 1950 [Type: section lebel, Data: Charactar] (Row: 17, Col: 1)\n- Field: Village or Town [Type: text, Data: Charactar] (Row: 18, Col: 1)\n- Field: Patwari Halka Number [Type: text, Data: Number] (Row: 18, Col: 2)\n- Field: Tehsil [Type: text, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: Data List, Data: Charactar] (Row: 19, Col: 2)\n- Field: Name of Head Of Family on This Date [Type: text, Data: Charactar] (Row: 20, Col: 1)\n- Field: Applicant Relation to Head of Family [Type: drop down, Data: Charactar] (Row: 20, Col: 2)\n- Field: Address Details of Year 10 August 1950 SC or 06 September 1950 ST to till Date Applicant or his Father or Mother or Guardian [Type: section lebel, Data: Charactar] (Row: 21, Col: 1)\n- Field: Is Applicant or his Father or Mother or Guardian Year 1950 to till Date live in Chhattisgarh [Type: drop down, Data: Number] (Row: 22, Col: 1)\n- Field: Address Details of Applicants Guardian [Type: fieldset, Data: Alfa Numeric] (Row: 23, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 24, Col: 1)\n- Field: Have Applicant issued scst certificate before [Type: drop down, Data: Charactar] (Row: 25, Col: 1)\n- Field: Details of document to proof that Beneficiary belongs to SC ST [Type: textarea, Data: Charactar] (Row: 25, Col: 2)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 26, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 4_en_4.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nअनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर \nऑनलाइन आवेदन\n\n--- Page 2 ---\nतवषय सूिी \nहोम पेज: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल ................................ ................................ ................................ ................................ .......... 2 \nिरण 1: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर पंजीयन ................................ ................................ ................................ .................... 3 \nिरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन................................ ................................ ................................ ................................ ............ 4 \nिरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ ............. 5 \nिरण 4: आधार ई-प्रमाणीकरण ................................ ................................ ................................ ................................ ........................ 8 \nिरण 5: अनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र के र्लए आवेदन ................................ ................................ .. 9 \nिरण 6: आवश्यक दस्तावेज़ अपलोि करना ................................ ................................ ................................ ............................ 10 \nिरण 7: पूवाावलोकन और आवेदन जमा करना ................................ ................................ ................................ ......................... 11 \nिरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ .. 0 \nिरण 9: पावर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ..........................\n\n--- Source 3: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: क्लिक करें।\n\n--- Page 10 ---\nिरण 5: अनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र क े  र्लए आवेदन \nिरण 5.1: आवेदन फॉमट में सामान्य तववरण और वतटमान पता दजट करें। \n \nचित्र क्रमाांक 13 \n \nिरण 5.2: स्थायी पते का तववरण दजट करें, सहेजें और पूवाावलोकन बटन पर क्लिक करें। \n \nचित्र क्रमाांक 14\n\n--- Page 11 ---\nिरण 6: आवश्यक दस्तावेज़ अपलोि करना \nअनुिग्नक का तववरण पेज खुिेगा, इसमें आवश्यक दस्तावेज़ अपिोि करने क े  लिए डनम्न प्रक्रक्रया का पािन करें। \n \nचित्र क्रमाांक 15 \n \n \nचित्र क्रमाांक 16 \nिरण 6.1: “Choose File”  पर क्लिक कर अपने कम्प्यूटर या िैपटॉप से दस्तावेज की स्क ै न कॉपी िुनें। \nिरण 6.2: फाइि सिेक्ट करने क े  बाद “UPLOAD”  पर क्लिक करें। \nिरण 6.3: दस्तावेज अपिोि करने क े  बाद “अनुलग्नक सहेजें” पर क्लिक करें। \nिरण 6.4: पुक्रिकरण क े  लिए िॉयिॉग बॉक्स खुिेगा, इसे ओक े कर दें।\n\n--- Page 12 ---\nिरण 7: पूवाावलोकन और आवेदन जमा करना \nशुल्क क े  भुगतान क े  पश्चात् डनम्न चित्रानुसार पेज खुिेगा। \n \nचित्र क्रमाांक 18 \n \n \nचित्र क्रमाांक 19 \nिरण 7.1 घोषणा: घोषणा हेतु डनधाटररत बॉक्स पर क्लिक करें। \nिरण 7.2: घोषणा पर क्लिक करते ही “जमा करें” बटन क्रदखाई देगा। इस पर क्लिक करते ही आपका फॉमट \nजमा हो जाएगा।\n\n--- Page 13 ---\nिरण 8: शुल्क का भुगर्ान \n \nचित्र क्रमाांक 17 \nिरण 8.1: डनधाटररत शुल्क का भुगतान करें। \nिरण 8.2: “जमा करें” पर क्लिक करें। \n \nनोट: \n• िोकसेवा क ें द्र/ सीएससी/डकयोस्क क े  लिए सेवा शुल्क रु. 30 डनधाटररत है। \n• अचधकतम पााँि दस्तावेज़़ों तक स्क ैडनिंग डनिःशुल्क है। \n• इसक े  अततररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट ि\n\n--- Source 4: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: तररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट िेकर सुरलित रखें। \n \nचित्र क्रमाांक 20 \nआवेदन संदभा क्रमांक की सहायता से आवेदन की स्थस्थतत छत्तीसगढ़ ई-डिस्ट्रिक्ट क े  पोटटि पर देखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेदन जमा करने क े  बाद डनधाटररत 22 क्रदऩों की समय-सीमा क े  अ ां दर आवेदन का डनराकरण कर क्रदया जाता है। \n• ई-डिस्ट्रिक्ट पोटटि पर आवेदन की स्थस्थतत देखी जा सकती है। \n• अनुसूचित जातत अथवा जनजातत प्रमाण पत्र जारी होने क े  उपराांत इसकी डिचजटि प्रतत ई-डिस्ट्रिक्ट पोटटि से िाउनिोि की \nजा सकती है।\n\n--- [Document: 4_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र\nService ID: 4\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: मूल निवासी प्रमाण पत्र\n  * Supporting Document 2: बिजली का बिल\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: टेलीफोन बिल\n  * Supporting Document 5: जन्म प्रमाण पत्र\n  * Supporting Document 6: वोटिंग कार्ड\n  * Supporting Document 7: बी.पी.एल. प्रमाण पत्र\n  * Supporting Document 8: घर या भूमि का दस्तावेज़\n  * Supporting Document 9: ड्राइविंग लाइसेंस\n  * Supporting Document 10: अन्य\n  * Supporting Document 11: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 12: फोटो परिचय पत्र\n  * Supporting Document 13: पिता / पालक की नौकरी का प्रमाण - पत्र\n  * Supporting Document 14: अनैच्छिक प्रवजन का आदेश\n  * Supporting Document 15: मूल निवासी प्रमाण पत्र\n- SNo 2: जाति का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: अन्य राज्य के अनुसूचित जाति / जनजाति प्रमाणपत्र\n  * Supporting Document 2: सरपंच / पार्षद / विधायक / साँसद से जाति प्रमाण-पत्र\n  * Supporting Document 3: प्राथमिक शाला या जिला शिक्षा अधिकारी द्वारा प्रमाणित प्राथमिक शाला द्वारा जारी स्थानान्तरण प्रमाण-पत्र\n  * Supporting Document 4: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 5: शैक्षणिक प्रमाण पत्र\n  * Supporting Document 6: आवेदक को या उसके किसी परिवारजन को जारी हुआ जाति प्रमाण पत्र\n  * Supporting Document 7: प्राथमिक परीक्षा उत्तीर्ण प्रमाण-पत्र\n  * Supporting Document 8: जन्म सूचना प्रपत्र\n  * Supporting Document 9: मिसल\n  * Supporting Document 10: अधिकार अभिलेख\n  * Supporting Document 11: जमाबंदी\n  * Supporting Document 12: १९३१ का जनगणना पंजी\n  * Supporting Document 13: 1949 का नागरिक पंजी\n  * Supporting Document 14: दाखिल / ख़ारिज पंजी\n  * Supporting Document 15: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 3: शपथ पत्र (Mandatory: नहीं)\n  * Supporting Document 1: शपथ पत्र\n- SNo 4: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 5: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ो।\nप्राप्तकर्ता क हस्ताक्षर एवं पदमुद्रा\n\n--- Page 28 (no rotation needed) ---\n788 २६ २९-\nछत्तोसगढ़ राजपत्र टिनांक 2 सितम्बर २०१३\nप्ररूप 3 ख [ नियम ६२ ]\nसक्षम प्राधिकारी का कार्यालय\nआदेदन पत्र क वापसी का ज्ञापनं वापसी झापन)\n(इप् ज्ञापन की मूल प्रति आवेदक को प्रदत्त की जावे तथा उसूका प्रतिपर्ण कार्यालय में संधारित किया जावे\nकमांक\nदिनांक\nश्र श्रीमती / कुमारी आत्मज आन्मजा निवासी द्वारा सामाजिक प्रास्थिति प्रमाणन्पत्र जारी करने हेतु प्रस्तुत आवेदन पत्र में निम्नाकित अभिलेखों क अभाव है॰ अतः अवेदक को निर्देशित किया जाता है कि निम्नांकित अंभिलेख जिनमें सही * का निशान अंकित किया गया है आवेदन पत्र॰के साथ प्रस्तुत करने पर उसके सामाजिए प्रास्थिति प्रगाण-् पत्र जारी करने की कार्यवाही प्रारंभ कीजा सकगीः- (1 ) आवेदक अथवा आवेदक क पिता / पूर्वजों का निम्नांकित दस्तावेज जिसमें उसकी जाति अंकित है पूर्वजों के राजस्व दस्तावेज गिशल) जमाबंदी सर्वेक्षण गिरदावरीः 8 सष्चियबंदोबस्तिलेख (१९५ ; जनगणना (१९३१ ; (छः) वन विभाग की जमाबंदीः नागरिकों का राष्ट्रीय रजिस्टर (१९३९ ; ६ जन्म यां मृत्यु की पंजपीः पिता अथवा पूर्वज के शिक्षित होने को स्थिति में प्रवेश दाखिल / खारिज) पंजी पिताः पूर्वज अथवा संबंधी नातेदार को पूर्व में जारी जाति ग्रगाण प्रमाण-पत्र कों प्रात ग्राारह अन्य दस्तावे जिसस आवेदक क द्वारा दावा की गई जाति होनां प्रमाणित होता है बारह\n(2) ऐरो दस्तावेज अथवा दस्त्तावेजों की रूम्यक रूप सें अंभिप्रभाणित प्रतिलिपि अथवा प्रतिलिपियां जिससे यह प्रमाणित हो सके के आवेदक के पूर्वज राष्ट्रपतीय अधिसूचना तिथि अथवा अन्ग गिछड़ा वर्गकी अधिस्चना तिथि के पूर्व से छत्तीरागड की भैगोलिक सीमा में निवास करते थे। पूर्वजों सेः प्रारंभ कर आवेदक तक पटवारी से प्रदत्त वंशावली ( आवेदक अ�\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: दि समिति प्रथभदृष्ट्या यह पाती है कि उपरोक्त सामाजिक प्रास्थिति प्रमाणयत्र त्रुटिपूर्वक या कपटपूर्वक अभिग्राप्त किया #या था॰ तो कृपया सूचित करें ताकि संबंधित आवदक क उसके दावे के समर्शन में आपके समक्ष साक्ष्श प्रस्तुत करने क लिए निर्देशित किया जा सके\nसलग्न उपरोक्तानुसार सामाजिक प्रास्थिति प्रमाणपत्र की मूल / सत्यापित प्रतिः\nहसताक्षर\nनाम एवं नोहर\n\n--- Page 17 (no rotation needed) ---\nछत्तीसगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\n७88 ( १५ )\nप्ररूप- +ग\n[ नियम १६ (३ एवं 4 देखिय ]\nजिला स्तरीय सामाजिक प्रमाण पत्र सत्यापन समिति क समक्ष आवेदन पत्र\nअध्यक्ष जिला स्तंरीय प्रमाण पत्र सत्यापन समिति\nदिग़य\nअनुसूचित जाति / अनुसूचित जनजाति / अन्य पिछड़ा वर्ग़ के प्रमाण - पत्र कं सत्यापन क संबंघ में '\nमहादय,\nमैं अधाहस्ताक्षरकर्ता\nपिता / पति कः नाम\nविभाग\nएतद्द्वारा , श्री / श्रीमती / कुमारी का वर्तमान सामाजिक प्रास्थिति प्रमाण पत्र\nआवेदक का नाम पिता / पति का नाम\nमूल / छायाप्रति सत्यापन. हेतु सत्यापन समिति / अनावेदक\nलोक नियोजंक / शेक्षणिक\nसंस्था / संवैधानिक निकायं / राज्य शासन / कन्द्र शासन के दिशा निर्देश अनुसार प्रस्तुत कर रहा हू॰ # श्रीमती / कुमारी क दावे की पुष्टि के लिए निम्नांकित दस्तावेज संलग्न\nकर रहा . हूँ :\nआवदक का नाम ऐवं उपनाम\n२\nआवेदक कं पितां का नाम एवं उपनाम\n3\nआवेदक क पिता क पिता दादा) का नाम एवं उपनम आदेदक की माता का नाम एवं उपनाम\n5\nआवेदक की माता क पिता नना का नाम एवं उपनामः : आवेदक यदि महिला है॰ तो उसके पति कानाम एवं उपनम आवेदक की जन्म तिथि\nनिवास स्थान ०\n\n--- Page 18 (no rotation needed) ---\n७88 { १६ )\nछत्तीसगढ़ राजपत्र दिनांक 2 सितम्बर २०१३\nस फ\nनिवास स्थान\nमोहल्ला / ग्राम / तहसाल वार्ड कमांक कस्बा / शहर\nजिला निवास करने की एवं ततिथि राज्य अथवा वर्ष\nआवदक का वर्तमान निवास स्थान 2 अवदक का घत्त्तापगढ़\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: � स्वायत्त संस्थानों एवं निकायों नगर निगनों सर लिका॰ ग्राम पंचायत इत्यादि को उनके रिकार्ड के लिए तथा जिला सूचना केन्द्रों के गाध्यभ से निधः =्ञ वेबसाइट पर प्रदर्शित करने हेतु भो भेजेगी : {2) सक्षभ प्राधिकारी परनागात्र जार्र ५९ तथा आवेढनें को निरत फरन रक जानका प्रतिवर्ष ३१ दिराम्बर तक विहित प्ररूग ७क में राज्य शासन कोमी प्रेषित्त करेगी। (3) सत्यापन समिति प्रमाणप्त्रों फ सत्यापन करने॰ आवेदनों क निरस्त्त करने छानबी समिति को प्रकरणों को अग्रेषित करभें को जानकारी प्रतिवर्ष ३१ दिसम्बर तक विहित़. श्ररूप-ख में ाज्य शासन को श्रेषित करेगी ।\n(४ ) छानबीन समिति राज्य शासन तणा सत्यापन सभेतियों क द्वारा निर्दिष्ट शिकायतों - जॉच एवं प्रमाणपत्र क निरस्तीकरण संबंधी जानकारीं प्रतिवर्ष ३१ दिसभ्बर तक विहित प्ररुूप ७ग में ज्य शासन को प्रेषित्त करगी ।\nछत्तीसगढ़ के राज्यपाल के नाम से तथा आदेश नुसार मनोज कुमार पिं॰आ॰ सचिव\n\n--- Page 13 (no rotation needed) ---\nछत्तीसगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\n788 ( 11)\nप्ररूप १क\nनियम 3 १ देखिये ]\nसामाजिक प्रास्थिति प्रमाणपत्र हेतु आवेदन- पत्र\nप्रति,\nसक्षन प्राधिकारी उपखण्ड जिला\nमहादय\nनिवेदन है कि मुझे / मेरे पुत्र / मेरी पुत्री को अनुसूचित जाति / अनुसूचित जनजाति / अन्य पिछड़ा वर्ग़ को उपलब्ध सुविधाओं का लाभ पाने के कम में सामाजिक प्रास्थिति प्रमाण-्पत्र की आवश्यकता है इस संबंध में निम्नानुसार जानकारी प्रस्तुत है, अर्थात् आवदक का पूरा नाम 2 आवेदक क पिता का नाम 3 आवेदक की वैवाहिक स्थिति विवाहित / अविवाहित 4 का नाग महिला आवेदक के मामले में 5 आवेदक की जन्म तिथि 6 जाति (केवल अनुसूचित जाति आवेदक के .- 7 वर्तमान पूरा पता मोहल्ला / वार्ड ग्राम / करचा / शहर विखं तहसीलं जिला राज्य स्थाईं पता मोहल्ला / वार्ड\nग्राम / करचा / शहर वि.खं तहसीलं जिला रज्य मोहल्ला / �\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "माता के मूल निवासी प्रमाण पत्र के साथ एससी प्रमाण पत्र का आवेदन\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       सेवा सेतु पोर्टल पर अनुसूचित जाति प्रमाण पत्र के लिए आवेदन करने के लिए, आपको निम्नलिखित दस्तावेजों की आवश्यकता होगी:
       
       **आवश्यक दस्तावेज:**
       
       1. **निवास प्रमाण:**
          - मूल निवासी प्रमाण पत्र (अनिवार्य)
          - बिजली का बिल
          - राशन कार्ड
          - टेलीफोन बिल
          - जन्म प्रमाण पत्र
          - वोटर आई डी कार्ड
          - बी पी एल प्रमाण पत्र
          - भूमि और घर का दस्तावेज
          - ड्राइविंग लाइसेंस
          - अन्य दस्तावेज
       
       2. **जाति प्रमाण:**
          - अन्य राज्य के अनुसूचित जाति/जनजाति प्रमाण पत्र (अनिवार्य)
          - सरपंच/पार्षद/विधायक/सांसद से जाति प्रमाण-पत्र (अनिवार्य)
          - प्राथमिक स्कूल का स्थानांतरण प्रमाण-पत्र
          - पिता/अभिभावक की सेवा प्रमाण पत्र/पहचान पत्र
          - शैक्षणिक प्रमाण पत्र
          - आवेदक को जारी जाति प्रमाण पत्र (अनिवार्य)
          - प्राथमिक स्कूल का प्रमाण-पत्र
          - जन्म सूचना प्रपत्र
          - मिसल
          - अधिकार अभिलेख
          - जमाबंदी
          - जनगणना पंजी (1931)
          - नागरिक पंजी (1949)
          - दाखिल/खारिज पंजी
          - अक्षमता/अनुपलब्धता का प्रमाण
       
       3.   - शपथ पत्र (अनिवार्य नहीं)
          - वंशावली (अनिवार्य नहीं)
          - ग्राम सभा प्रस्ताव (ग्रामीण क्षेत्रों के लिए) (अनिवार्य नहीं)
       
       **आवेदन प्रक्रिया:**
       
       1. सेवा सेतु पोर्टल पर पंजीकरण करें।
       2. आवेदन फॉर्म में सामान्य विवरण भरें।
       3. स्थायी पते का विवरण दजट करें और सहेजें।
       4. आवश्यक दस्तावेज अपलोड करें।
       5. आवेदन जमा करें।
       6. शुल्क का भुगतान करें (30 रुपये)।
       7. आवेदन की स्थिति ट्रैक करें।
       
       **शुल्क:**
       - सेवा शुल्क: 30 रुपये (ऑनलाइन या कियोस्क पर)।
       - कुल शुल्क: 30 रुपये (एक ही भुगतान विधि)।
       
       **समय सीमा:**
       - आवेदन का समाधान: 22 दिन।
       
       **महत्वपूर्ण:**
       - सभी अनिवार्य दस्तावेज आवश्यक हैं।
       - आवेदन जमा करने के बाद पावती प्राप्त होगी।
       - आवेदन की स्थिति ऑनलाइन ट्रैक की जा सकती है।
       - प्रमाण पत्र जारी होने के बाद इसकी प्रति ई-डिस्ट्रिक्ट पोर्टल से डाउनलोड की जा सकती है।
       
       अधिक जानकारी के लिए सेवा सेतु पोर्टल पर जांच करें।
       ```
| 26 | `जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें` | 5 | 5 | ✅ MATCH | new_topic | 5.14s |

### Query 26 Details
* **Query**: `जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `OBC certificate online download using caste registry credentials`
* **Resolved Hindi Query**: `जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > अन्य पिछड़ा वर्ग (ओबीसी) प्रमाण पत्र ऑनलाइन डाउनलोड करने के लिए, आपको सेवा सेतु पोर्टल पर जाना होगा। यहाँ चरण-दर-चरण प्रक्रिया दी गई है:
  > 
  > 1. **सेवा सेतु पोर्टल पर लॉगिन करें**: https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं और लॉगिन करें।
  > 2. **आवेदन की स्थिति जांचें**: लॉगिन करने के बाद, "आवेदन की स्थिति" (Application Status) विकल्प चुनें।
  > 3. **प्रमाण पत्र डाउनलोड करें**: यदि आपका आवेदन स्वीकृत हो गया है, तो प्रमाण पत्र डाउनलोड करने का विकल्प दिखाई देगा।
  > 4. **आवश्यक विवरण दर्ज करें**: प्रमाण पत्र डाउनलोड करने के लिए आवेदन संख्या और जन्म तिथि दर्ज करें।
  > 5. **प्रमाण पत्र प्राप्त करें**: डाउनलोड लिंक पर क्लिक करें और प्रमाण पत्र को अपने डिवाइस में सहेजें।
  > 
  > **महत्वपूर्ण बिंदु**:
  > - प्रमाण पत्र डाउनलोड करने के लिए आवेदन की स्थिति "स्वीकृत" (Approved) होनी चाहिए।
  > - यदि स्थिति "लंबित" (Pending) है, तो प्रतीक्षा करें या सेवा केंद्र से संपर्क करें।
  > - डाउनलोड के लिए आधार कार्ड या आवेदन संख्या की आवश्यकता हो सकती है।
  > 
  > **सहायता**:
  > - सेवा केंद्र पर जाकर सहायता प्राप्त की जा सकती है।
  > - हेल्पलाइन नंबर: 1800-180-0000 (यदि उपलब्ध हो)।
  > 
  > यह प्रक्रिया पूरी तरह से ऑनलाइन है, इसलिए किसी भौतिक दस्तावेज़ की आवश्यकता नहीं है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें"
       ```
     * **Response**:
       ```json
       जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें"
       ```
     * **Response**:
       ```json
       OBC certificate online download using caste registry credentials
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'जाति प्रमाण पत्र के लिए ऑनलाइन डाउनलोड प्रक्रिया', 'topic_summary': 'उपयोगकर्ता अब जाति प्रमाण पत्र डाउनलोड करने की प्रक्रिया के बारे में पूछ रहा है, जो नाम परिवर्तन या निवास प्रमाण पत्र जैसे पिछले विषय से एक अलग सेवा है।'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '3', 'service_id': '5'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- OBC RESIDENCY/DOMICILE RULE: If the citizen asks about Domicile or Residence rules/requirements for the OBC Certificate, explain clearly based on the context:\n  1. A Domicile Certificate (मूल निवासी प्रमाण पत्र) is NOT mandatory (it is listed as one of several optional supporting documents under 'Residential Proof').\n  2. To satisfy the residency requirement for the OBC Certificate, the applicant or their ancestors must have been residing in the geographical limits of Chhattisgarh since or before the OBC notification date, which is December 26, 1984 (२६ दिसम्बर १९८४).\n  3. List the alternative supporting documents for Residential Proof (such as Land/House documents, Ration Card, Electricity Bill, Ward Member/MLA/MP certificate, Birth Certificate).\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: OBC Certificate\nService ID: 5\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 2: Land And House Document\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Electricity Bill\n  * Supporting Document 5: Domicile Certificate\n  * Supporting Document 6: Birth Certificate\n  * Supporting Document 7: Birth Information Form\n  * Supporting Document 8: Service Certificate / Identity Card Of Father / Guardian\n  * Supporting Document 9: Order Of Involuntary Migration\n- SNo 2: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 3: Income Proof (Mandatory: Yes)\n  * Supporting Document 1: Certificate From Patwari/Sarpanch/Parshad\n  * Supporting Document 2: Income Certificate Employer/Form 16\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Income From Land/House\n  * Supporting Document 5: Other Documents\n  * Supporting Document 6: Application Form\n- SNo 4: Obc Proof (Mandatory: Yes)\n  * Supporting Document 1: Educational Certificate\n  * Supporting Document 2: Transfer Certificate Of Primary School Education\n  * Supporting Document 3: Obc Certificate Of Father\n  * Supporting Document 4: Obc Certificate From Sarpanch / Parshad\n  * Supporting Document 5: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 6: Misal\n  * Supporting Document 7: Adhikar Abhilekh\n  * Supporting Document 8: Jamabandi\n  * Supporting Document 9: Census Register Of 1931\n  * Supporting Document 10: Citizen Register Of 1949\n  * Supporting Document 11: Dakhil / Kharij Panji\n  * Supporting Document 12: Disability / Unavailability Proof\n- SNo 5: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 6: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 7: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste OBC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (\n\n--- Source 2: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ीं है।\n\n--- Page 14 ---\nचरण 9: पावर्ी सुरक्षिर् रखना \nआवेिन सफलतापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक िेखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट लेकर सुरलित रखें। \n \nचचत्र क्रमांक 20: पावर्ी एवं आवेदन संदभा क्रमांक \nआवेदन संदभा क्रमांक की सहायता से आवेिन की स्थस्थगत छत्तीसगढ़ ई-निस्ट्रिक्ट क े  पोटटल पर िेखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेिन जमा करने क े  बाि ननर्ाटररत 22 क्रिऩों की समय-सीमा क े  अ ं िर आवेिन का ननराकरण कर क्रिया जाता है। \n• ई-निस्ट्रिक्ट पोटटल पर आवेिन की स्थस्थगत िेखी जा सकती है। \n• अन्य क्रपछडा वगट प्रमाण पत्र जारी होने क े  उपरांत इसकी निजजटल प्रगत ई-निस्ट्रिक्ट पोटटल से िाउनलोि की जा सकती है।\n\n--- [Document: 5_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of\n\n--- Source 3: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �रण 3.4: यक्रि यह सेवा सूची में शागमल नहीं है तो ऊपर क्रिए गए होम बटन पर क्लिक करें। ननम्नानुसार पेज \nखुलेगा। \n \nचचत्र क्रमांक 7: उपयोगकर्ाा होम पेज \nचरण 3.5: इस पेज पर “सभी सेवाए ँ  देखें” पर क्लिक करें। सेवाओं की सूची खुलेगी।\n\n--- Page 7 ---\nचचत्र क्रमांक 8: सेवाओ ं  की सूची \nचरण 3.6: सेवाओं की सूची में से अन्य पपछडा वगा प्रमाण पत्र क े  सामने क्रिए गए बटन पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। \n \nचचत्र क्रमांक 9: सेवा पररचय एवं आगे बटन \nचरण 3.6: “आगे” बटन पर क्लिक करें।\n\n--- Page 8 ---\nइस पेज पर आप आवश्यक िस्तावेज़़ों की सूची भी िेख सकते हैं। \n \nचचत्र क्रमांक 10: आवश्यक सहायक दस्तावेज़़ों की सूची\n\n--- Page 9 ---\nचरण 4: आवेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 11: आवेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 12: सहायक दस्तावेज़़ों की जांच सूची \n \nचरण 4.3: इस गविंिो में क्रिए गए “जमा” बटन पर क्लिक करें।\n\n--- Page 10 ---\nचरण 5: अन्य पपछडा वगा प्रमाण पत्र क े  र्लए आवेदन \nचरण 5.1: आवेिन फॉमट में सामान्य गववरण और वतटमान पता िजट करें। \n \nचचत्र क्रमांक 13: अन्य पपछडा वगा आवेदन फॉमा भाग एक व दो \n \nचरण 5.2: स्थायी पते का गववरण िजट करें, सहेजें और पूवाावलोकन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 14: अन्य पपछडा वगा आवेदन फॉमा भाग र्ीन, चार व पाँच\n\n--- Page 11 ---\nचरण 6: आवश्यक दस्तावेज़ अपलोि करना \nअनुलग्नक का गववरण पेज खुलेगा, इसमें आवश्यक िस्तावेज़ अपलोि करने क े  ललए ननम्न प्रक्रिया का पालन करें। \n \nचचत्र क्रमांक 15: सहायक दस्तावेज़ अपलोि \nचरण 6.1: “Choose File”  पर क्लिक कर अपन\n\n--- Source 4: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �स्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अन्य पिछड़ा वर्ग प्रमाण पत्र\nService ID: 5\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 2: घर या भूमि का दस्तावेज़\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: बिजली का बिल\n  * Supporting Document 5: मूल निवासी प्रमाण पत्र\n  * Supporting Document 6: जन्म प्रमाण पत्र\n  * Supporting Document 7: जन्म सूचना प्रपत्र\n  * Supporting Document 8: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 9: अनैच्छिक प्रवजन का आदेश\n- SNo 2: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 3: आय प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: पटवारी/सरपंच/पार्षद से प्रमाण पत्र\n  * Supporting Document 2: नियोक्ता का आय प्रमाण पत्र/फार्म १६\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: भूमि/घर से आय\n  * Supporting Document 5: अन्य\n  * Supporting Document 6: आवेदन प्रपत्र\n- SNo 4: अन्य पिछड़ा वर्ग का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: शैक्षणिक प्रमाण - पत्र\n  * Supporting Document 2: प्राथमिक स्कूल शिक्षा के प्रमाण पत्र के लिए स्थानांतरण\n  * Supporting Document 3: पिता का अ.पि.व. प्रमाण पत्र\n  * Supporting Document 4: सरपंच / पार्षद से ओबीसी प्रमाणपत्र\n  * Supporting Document 5: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 6: मिसल\n  * Supporting Document 7: अधिकार अभिलेख\n  * Supporting Document 8: जमाबंदी\n  * Supporting Document 9: १९३१ का जनगणना पंजी\n  * Supporting Document 10: 1949 का नागरिक पंजी\n  * Supporting Document 11: दाखिल / ख़ारिज पंजी\n  * Supporting Document 12: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 5: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 6: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document 1: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए)\n- SNo 7: मध्यप्रदेश पुनर्गठन अधिनियम 2000(क्रमांक २६-सन २००० की धारा ६७ के अधीन छ. ग. राज्य संवर्ग आबंटन ) का प्रम\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: र्ाटररत शुल्क का भुगतान करें। \nचरण 7.2: “जमा करें” पर क्लिक करते ही आवेिन जमा हो जाएगा। \n \nनोट: \n• लोकसेवा क ें द्र/ सीएससी/नकयोस्क क े  ललए सेवा शुल्क रु. 30 ननर्ाटररत हैं। \n• पााँच िस्तावेज़़ों तक स्क ै ननिंग ननिःशुल्क है। \n• इसक े  अगतररक्त और कोई शुल्क िेय नहीं है।\n\n--- Page 14 ---\nचरण 9: पावर्ी सुरक्षिर् रखना \nआवेिन सफलतापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक िेखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट लेकर सुरलित रखें। \n \nचचत्र क्रमांक 20: पावर्ी एवं आवेदन संदभा क्रमांक \nआवेदन संदभा क्रमांक की सहायता से आवेिन की स्थस्थगत छत्तीसगढ़ ई-निस्ट्रिक्ट क े  पोटटल पर िेखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेिन जमा करने क े  बाि ननर्ाटररत 22 क्रिऩों की समय-सीमा क े  अ ं िर आवेिन का ननराकरण कर क्रिया जाता है। \n• ई-निस्ट्रिक्ट पोटटल पर आवेिन की स्थस्थगत िेखी जा सकती है। \n• अन्य क्रपछडा वगट प्रमाण पत्र जारी होने क े  उपरांत इसकी निजजटल प्रगत ई-निस्ट्रिक्ट पोटटल से िाउनलोि की जा सकती है।\n\n--- [Document: 5_hi_citizenCharter.pdf (SLA_DETAILS)] ---\nछत्तीसगढ़ शासन\nराजस्व एवं आपदा प्रबंधन विभाग\nमंत्रालय\nमहानदी भवन नया रायपुर\n::: अधिसूचना :::\n\nरायपुर, दिनांक 16/05/2013\n\nक्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\nसारणी (SLA Details):\n1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ............... 8 \nचरण 5: अन्य पपछडा वगा प्रमाण पत्र के र्लए आवेदन ................................ ................................ ................................ ......................... 9 \nचरण 6: आवश्यक दस्तावेज़ अपलोि करना ................................ ................................ ................................ ................................ ........ 10 \nचरण 7: पूवाावलोकन और आवेदन जमा करना ................................ ................................ ................................ ................................ ..... 11 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 12 \nचरण 9: पावर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ...............................  13\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉपगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉपगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: नवीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉपगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉपगन प्रपक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासविा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉपगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.2: खोजें पर क्लिक करें। \nचरण 3.3: से�\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ी यहााँ िजट करें।  \n5. लॉपगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.2: खोजें पर क्लिक करें। \nचरण 3.3: सेवाओं की सूची खुलेगी। इसमें अन्य पपछडा वगा प्रमाण पत्र िेखें।  \nचरण 3.4: यक्रि यह सेवा सूची में शागमल नहीं है तो ऊपर क्रिए गए होम बटन पर क्लिक करें। ननम्नानुसार पेज \nखुलेगा। \n \nचचत्र क्रमांक 7: उपयोगकर्ाा होम पेज \nचरण 3.5: इस पेज पर “सभी सेवाए ँ  देखें” पर क्लिक करें। सेवाओं की सूची खुलेगी।\n\n--- Page 7 ---\nचचत्र क्रमांक 8: सेवाओ ं  की सूची \nचरण 3.6: सेवाओं की सूची में से अन्य पपछडा वगा प्रमाण पत्र क े  सामने क्रिए गए बटन पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। \n \nचचत्र क्रमांक 9: सेवा पररचय एवं आगे बटन \nचरण 3.6: “आगे” बटन पर क्लिक करें।\n\n--- Page 8 ---\nइस पेज पर आप आवश्यक िस्तावेज़़ों की सूची भी िेख सकते हैं। \n \nचचत्र क्रमांक 10: आवश्यक सहायक दस्तावेज़़ों की सूची\n\n--- Page 9 ---\nचरण 4: आवेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 11: आवेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 12: सहायक दस्तावेज़़ों की जांच सूची \n \nचरण 4.3: इस गविंिो में क्रिए गए “जमा” बटन पर क्लिक करें।\n\n--- Page 10 ---\nचरण 5: अन्य पपछडा वगा प्रमाण पत्र क े  र्लए आवेदन \nचरण 5.1: आवेिन फॉमट में सामान्य गववरण और वतटमान पता िजट करें। \n \nचचत्र क्रमांक 13: अन्य पपछडा वगा आवेदन फॉमा भाग एक व दो \n \nचरण 5.2: स्थायी पते का गववरण िजट करें, सहेजें और पूवाावलोकन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 14: अ\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "जाति रजिस्ट्री क्रेडेंशियल्स का उपयोग करके ओबीसी प्रमाण पत्र ऑनलाइन डाउनलोड करें\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       अन्य पिछड़ा वर्ग (ओबीसी) प्रमाण पत्र ऑनलाइन डाउनलोड करने के लिए, आपको सेवा सेतु पोर्टल पर जाना होगा। यहाँ चरण-दर-चरण प्रक्रिया दी गई है:
       
       1. **सेवा सेतु पोर्टल पर लॉगिन करें**: https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं और लॉगिन करें।
       2. **आवेदन की स्थिति जांचें**: लॉगिन करने के बाद, "आवेदन की स्थिति" (Application Status) विकल्प चुनें।
       3. **प्रमाण पत्र डाउनलोड करें**: यदि आपका आवेदन स्वीकृत हो गया है, तो प्रमाण पत्र डाउनलोड करने का विकल्प दिखाई देगा।
       4. **आवश्यक विवरण दर्ज करें**: प्रमाण पत्र डाउनलोड करने के लिए आवेदन संख्या और जन्म तिथि दर्ज करें।
       5. **प्रमाण पत्र प्राप्त करें**: डाउनलोड लिंक पर क्लिक करें और प्रमाण पत्र को अपने डिवाइस में सहेजें।
       
       **महत्वपूर्ण बिंदु**:
       - प्रमाण पत्र डाउनलोड करने के लिए आवेदन की स्थिति "स्वीकृत" (Approved) होनी चाहिए।
       - यदि स्थिति "लंबित" (Pending) है, तो प्रतीक्षा करें या सेवा केंद्र से संपर्क करें।
       - डाउनलोड के लिए आधार कार्ड या आवेदन संख्या की आवश्यकता हो सकती है।
       
       **सहायता**:
       - सेवा केंद्र पर जाकर सहायता प्राप्त की जा सकती है।
       - हेल्पलाइन नंबर: 1800-180-0000 (यदि उपलब्ध हो)।
       
       यह प्रक्रिया पूरी तरह से ऑनलाइन है, इसलिए किसी भौतिक दस्तावेज़ की आवश्यकता नहीं है।
       ```
| 27 | `छत्तीसगढ़ के गैर-निवासी के लिए शादी प्रमाण पत्र की पात्रता` | 3 | 3 | ✅ MATCH | new_topic | 2.67s |

### Query 27 Details
* **Query**: `छत्तीसगढ़ के गैर-निवासी के लिए शादी प्रमाण पत्र की पात्रता`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "छत्तीसगढ़ के गैर-निवासी के लिए विवाह पंजीकरण एवं प्रमाण पत्र की पात्रता"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "छत्तीसगढ़ के गैर-निवासी के लिए विवाह पंजीकरण एवं प्रमाण पत्र की पात्रता"
       ```
     * **Response**:
       ```json
       छत्तीसगढ़ के गैर-निवासी के लिए विवाह पंजीकरण एवं प्रमाण पत्र की पात्रता
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "छत्तीसगढ़ के गैर-निवासी के लिए विवाह पंजीकरण एवं प्रमाण पत्र की पात्रता"
       ```
     * **Response**:
       ```json
       Marriage registration and certificate eligibility for non-resident of Chhattisgarh
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "छत्तीसगढ़ के गैर-निवासी के लिए विवाह पंजीकरण एवं प्रमाण पत्र की पात्रता",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'marriage registration and certificate eligibility for non-resident in Chhattisgarh', 'topic_summary': 'User is inquiring about marriage registration and certificate eligibility for a non-resident in Chhattisgarh, which is a different service from any previous context.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "छत्तीसगढ़ के गैर-निवासी के लिए विवाह पंजीकरण एवं प्रमाण पत्र की पात्रता",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '1', 'service_id': '3'}
       ```
| 28 | `जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप` | 201 | 201 | ✅ MATCH | new_topic | 4.30s |

### Query 28 Details
* **Query**: `जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Caste Certificate Correction Name Change Application Format`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > सेवा सेतु पोर्टल पर जाति प्रमाण पत्र सुधार के लिए नाम परिवर्तन आवेदन प्रारूप:
  > 
  > **आवश्यक दस्तावेज:**
  > 1. मूल चालान की प्रति (430 रुपये)
  > 2. नोटराइज्ड शपथ पत्र (50 रुपये)
  > 3. स्थानीय समाचार पत्र में प्रकाशन की प्रति
  > 4. दो गवाहों के विवरण
  > 5. पुराना नाम और नया नाम सत्यापन
  > 6. सभी पहचान पत्र
  > 
  > **आवेदन प्रक्रिया:**
  > - सेवा सेतु केंद्र पर आवेदन करें
  > - ऑनलाइन शुल्क 30 रुपये
  > - समय सीमा 29 दिन
  > 
  > **फॉर्म विवरण:**
  > - आवेदक का पूरा नाम
  > - जन्म तिथि
  > - लिंग
  > - पिता/माता/पति का नाम
  > - पुत्र/पुत्री का नाम (पहले और बाद में)
  > - जिला, गाँव/शहर, तहसील, पिन कोड
  > 
  > **महत्वपूर्ण निर्देश:**
  > - सभी दस्तावेज मूल होने चाहिए
  > - शपथ पत्र 3 महीने से पुराना नहीं होना चाहिए
  > - आवेदन शुल्क 30 रुपये है (ऑनलाइन या कियोस्क पर)
  > 
  > अधिक जानकारी के लिए सेवा सेतु पोर्टल पर जांच करें।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप"
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप"
       ```
     * **Response**:
       ```json
       Caste Certificate Correction Name Change Application Format
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप', 'topic_summary': ''}
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "जाति प्रमाण पत्र सुधार नाम परिवर्तन आवेदन प्रारूप\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       सेवा सेतु पोर्टल पर जाति प्रमाण पत्र सुधार के लिए नाम परिवर्तन आवेदन प्रारूप:
       
       **आवश्यक दस्तावेज:**
       1. मूल चालान की प्रति (430 रुपये)
       2. नोटराइज्ड शपथ पत्र (50 रुपये)
       3. स्थानीय समाचार पत्र में प्रकाशन की प्रति
       4. दो गवाहों के विवरण
       5. पुराना नाम और नया नाम सत्यापन
       6. सभी पहचान पत्र
       
       **आवेदन प्रक्रिया:**
       - सेवा सेतु केंद्र पर आवेदन करें
       - ऑनलाइन शुल्क 30 रुपये
       - समय सीमा 29 दिन
       
       **फॉर्म विवरण:**
       - आवेदक का पूरा नाम
       - जन्म तिथि
       - लिंग
       - पिता/माता/पति का नाम
       - पुत्र/पुत्री का नाम (पहले और बाद में)
       - जिला, गाँव/शहर, तहसील, पिन कोड
       
       **महत्वपूर्ण निर्देश:**
       - सभी दस्तावेज मूल होने चाहिए
       - शपथ पत्र 3 महीने से पुराना नहीं होना चाहिए
       - आवेदन शुल्क 30 रुपये है (ऑनलाइन या कियोस्क पर)
       
       अधिक जानकारी के लिए सेवा सेतु पोर्टल पर जांच करें।
       ```
| 29 | `क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?` | 5 | 5 | ✅ MATCH | new_topic | 2.73s |

### Query 29 Details
* **Query**: `क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?"
       ```
     * **Response**:
       ```json
       क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?"
       ```
     * **Response**:
       ```json
       Is the 15-year residence rule for OBC certificate applicable?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या ओबीसी प्रमाण पत्र के लिए 15 वर्ष प्रवास का निवास नियम लागू है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '3', 'service_id': '5'}
       ```
| 30 | `नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह प्रमाण पत्र ऑनलाइन शुल्क` | 201 | 201 | ✅ MATCH | new_topic | 3.48s |

### Query 30 Details
* **Query**: `नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह प्रमाण पत्र ऑनलाइन शुल्क`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `The Gazette notification cost for name change versus marriage registration and certificate online fees.`
* **Resolved Hindi Query**: `नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नाम परिवर्तन के लिए राजपत्र अधिसूचना की लागत 30 रुपये है। विवाह पंजीकरण और प्रमाण पत्र ऑनलाइन शुल्क के बारे में दी गई जानकारी में इस सेवा के लिए शुल्क का विवरण उपलब्ध नहीं है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क"
       ```
     * **Response**:
       ```json
       नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क"
       ```
     * **Response**:
       ```json
       The Gazette notification cost for name change versus marriage registration and certificate online fees.
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the cost for marriage registration?', 'topic_summary': 'The user is asking about the cost for marriage registration, which is a different service from the previous one discussed (name change). This is a new topic query about a different government service.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "नाम परिवर्तन के लिए राजपत्र अधिसूचना लागत बनाम विवाह पंजीकरण एवं प्रमाण पत्र ऑनलाइन शुल्क\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नाम परिवर्तन के लिए राजपत्र अधिसूचना की लागत 30 रुपये है। विवाह पंजीकरण और प्रमाण पत्र ऑनलाइन शुल्क के बारे में दी गई जानकारी में इस सेवा के लिए शुल्क का विवरण उपलब्ध नहीं है।
       ```
| 31 | `क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?` | 4 | 4 | ✅ MATCH | new_topic | 5.81s |

### Query 31 Details
* **Query**: `क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Can married daughters apply for an ST certificate using their father's caste certificate?`
* **Resolved Hindi Query**: `क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, विवाहित बेटियाँ पिता के जाति प्रमाण का उपयोग करके एस टी प्रमाण पत्र के लिए आवेदन नहीं कर सकती हैं। एस टी प्रमाण पत्र के लिए आवेदक का स्वयं का जाति प्रमाण होना अनिवार्य है। पिता के जाति प्रमाण का उपयोग करना इस प्रक्रिया के लिए मान्य नहीं है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?"
       ```
     * **Response**:
       ```json
       क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?"
       ```
     * **Response**:
       ```json
       Can married daughters apply for an ST certificate using their father's caste certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': "Can married daughters use father's caste certificate for ST certificate application?", 'topic_summary': "Query about using father's caste certificate for ST certificate application for married daughters."}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: SC/ST Certificate\nService ID: 4\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Domicile Certificate\n  * Supporting Document 2: Electricity Bill\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Telephone Bill\n  * Supporting Document 5: Birth Certificate\n  * Supporting Document 6: Voters Identity Card\n  * Supporting Document 7: Bpl Certificate\n  * Supporting Document 8: Land And House Document\n  * Supporting Document 9: Driving License\n  * Supporting Document 10: Other Documents\n  * Supporting Document 11: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 12: Photo Identity Card\n  * Supporting Document 13: Service Certificate Of Father / Guardian\n  * Supporting Document 14: Order Of Involuntary Migration\n  * Supporting Document 15: Domicile Certificate\n- SNo 2: Caste Proof (Mandatory: Yes)\n  * Supporting Document 1: Sc/St Certificate Of Other State\n  * Supporting Document 2: Sc/St Certificate From Sarpanch / Parshad / Mla / Mp\n  * Supporting Document 3: Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo\n  * Supporting Document 4: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 5: Educational Certificate\n  * Supporting Document 6: Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family\n  * Supporting Document 7: Primary School Certificate\n  * Supporting Document 8: Birth Information Form\n  * Supporting Document 9: Misal\n  * Supporting Document 10: Adhikar Abhilekh\n  * Supporting Document 11: Jamabandi\n  * Supporting Document 12: Census Register Of 1931\n  * Supporting Document 13: Citizen Register Of 1949\n  * Supporting Document 14: Dakhil / Kharij Panji\n  * Supporting Document 15: Disability / Unavailability Proof\n- SNo 3: Affidavit (Mandatory: No)\n  * Supporting Document 1: Affidavit\n- SNo 4: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 5: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 6: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste STSC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number\n\n--- Source 2: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: तररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट िेकर सुरलित रखें। \n \nचित्र क्रमाांक 20 \nआवेदन संदभा क्रमांक की सहायता से आवेदन की स्थस्थतत छत्तीसगढ़ ई-डिस्ट्रिक्ट क े  पोटटि पर देखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेदन जमा करने क े  बाद डनधाटररत 22 क्रदऩों की समय-सीमा क े  अ ां दर आवेदन का डनराकरण कर क्रदया जाता है। \n• ई-डिस्ट्रिक्ट पोटटि पर आवेदन की स्थस्थतत देखी जा सकती है। \n• अनुसूचित जातत अथवा जनजातत प्रमाण पत्र जारी होने क े  उपराांत इसकी डिचजटि प्रतत ई-डिस्ट्रिक्ट पोटटि से िाउनिोि की \nजा सकती है।\n\n--- [Document: 4_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and\n\n--- Source 3: [User Manual (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: official_document\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nOfficial Document Content: 31. Kaur 32. Keot, Keyot 33. Khaira 34. Khatik 35. Koch 36. Konai 37. Konwar 38. Kotal 39. Kurariar 40. Lalbegi 41. Lohar 42. Mahar 43. Mal\n१. Ins. by Act 1० of २००३ $ 3 and the First Sch २. Subs. by S. 3 and the First Sch., ibid. , for entry ४६. ३. Subs. by Act २५ of २००२ , s. 2, for entry २२.\nConstitution (Scheduled Castes) Order, १९५० PART IlL. Rules and Orders under the Constitution)\n\n--- Page 15 (no rotation needed) ---\n162 44. Mallah 45. Musahar 46. Namasudra 47. Nat 48. Nuniya 49. Paliya 50. Pan, Sawasi 51. Pasi\n52. Patni 53. Pod, Poundra 54. Rajbanshi 55. Rajwar 56. Sarki (epali) 57. Sunri excluding Saha) 58. Tiyar 59. Turi. १[६0. Chain (in Malda, Murshidabad, Nadia and Dakhin Dinajpur districts) ]\n२TPART XX. -lizoram\n1. Bansphor 2. Bhuinmali or Mali 3. Brittial Bania or Bania + Dhupi or Dhobi 5. Dugla or Dholi 6. Hira 7. Jalkeot 8 Jhalo, Malo or Jhalo Malo\n9 Kaibartta or Jaliya १०. Lalbegi 11 Mahara 12. Mehtar or Bhangi 13. Muchi or Rishi 14. Namasudra 15. Patni १६. Sutradhar ]\nJ[PART XZYI. Arunachal Pradesh\n४ *\nS[PART XYII-Goa\n1. Bhangi (Hadi) 2 Chambhar 3. Mahar\n4 Mahyavanshi (Vankar) 5 Mang ]\n१. Ins. by Act २५ of २००२ , २ २. Ins. by Act ३४ of १९८६, s. १३ and the First Sch (W.e.f. 20-2-1987) ३. Ins. by Act 69 of १९८६, s. १६ and the First Sch W.e.f. 20-2-1987) ४. Omitted by Act ६१ of २००२, s. 2 and First Sch 5. Ins by Act १8 of 1९८७ , 5. 19 and the First Sch wee.f. 30-5-1987).\nConstitution (Scheduled Castes ) Order, १९५० (PART III. Rules and Orders under the Constitution)\nPART XYIIL. Chhattisgarh\n\n--- Page 16 (no rotation needed) ---\n163\n१. Audhelia २२. Dohor २. Bagri, Bagdi २३. Dom, Dumar, Dome, Domar, Doris ३. Bahna, Bahana २४. Ganda, Gandi ४. Balahi Balai २५. Ghasi, Ghasia ५. Banchada २६. Holiya ६. Barahar, Basod २७. Kanjar ७. Bargunda २८. Katia, Patharia 8. Basor, Burud, Bansor, Bansodi, Bansphor, Basar २९. Khatik ९. Bedia ३०. Koli, Kori १०. Beldar, Sunkar ३१. Khangar, Kanera, Mirdha ११. Bhangi, Mehtar, Balmiki, Lalbegi, Dharkar ३२. Kuchbandhia १२. Bhanumati ३३. Mahar, Mehra, Mehar १३. Chadar 34. Mang Mang Garodi, Mang Garudi, Dankhani Mang 14. Chamar, Chamari, Bairwa, Bhambhi, Jatav, Mochi, Mang Mahasi, Madari, Garudi, Radhe Mang Regar, Nona, Rohidas, Ramnami Satnami ३५. Meghwal Surjyabanshi, Surjyaramnami, Ahirwar, Chamar, ३६. Moghia Mangan, Raidas ३७. Muskhan १५. Chidar ३८. Nat, Kalbelia, Sapera, Navdigar, Kubutar १६. Chikwa, Chikvi ३९. Pasi १७. Chitar ४०. Rujjhar १८. Dahait, Dahayat, Dahat ४१. Sansi, Sansia १९. Dewar ४२. Silawat २०. Dhanuk 43 Zamral. ] २१. Dhed, Dher\n२TPART XYIV Uttaranchal\n1. agaria २. Badhik ३. Badi 4 Baheliya ५. Baiga 6. Baiswar ७. Bajaniya 8. Bajgi ९. Balhar १०. Balai ११. Balmiki १२. Bangali १३. Banmanus १४. Bansphor १५. Barwar १६. Basor १७. Bawariya १८. Beldar १९. Beriya २०. Bhantu २१. Bhuiya २२. Bhuyiar २३. Boria २४. Ch\n\n--- Source 4: [User Manual (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: official_document\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nOfficial Document Content: Baira 8. Bakuda १ * * * १०. Bathada १* * * २[1२. Bharathar (other than Parathar), Paravan] १ * * * १४. Chakkiliyan 15. Chamar, Muchi 16. Chandala 17. Cheruman 18. Domban १ * * * १* * * १ * * *\n45. Pallan 46. Palluvan 47. Pambada 48. Panan\n22. Gosangi 23. Hasla २४. Holeya 25. Kadaiyan 2 12६. Kakkalan, Kakkan] 27. Kalladi २ [28. Kanakkan, Padanna, Padannan] 3 * * * २[३0. Kavara (other than Telugu speaking or Tamil speaking Balija, Kavarai, Gavarai, Gavarai Naidu, Balija Naidu, Gajalu Balija or Valai Chetty)] 31. Koosa 32. Kootan, Koodan\n२[५0. Paraiyan, Parayan, Sambavar, Sambavan, Sambava, Paraya, Paraiya, Parayar] < र\n% %\n२[५४. Pulayan, Cheramar, Pulaya, Pulayar, Cherama, Cheraman, Wayanad Pulayan, Wayanadan Pulayan, Matha, Matha Pulayan] * *\n56. Puthirai Vannan ५७. Raneva ५8. Samagara\n१. Omitted by Act ६१ of २००२, s. 2 and the First Sch २. Subs. by S. २ and the First Sch ibid . for entry 1२ ३. Omitted by Act १० of २००३ , s. 3 and the First Sch\nConstitution Scheduled Castes ) Order, १९५० (PART IIL. Rules and Orders under the Constitution )\n\n--- Page 8 (no rotation needed) ---\n155 59. Samban 1[60. Semman, Chemaman, Chemmar] 61. Thandan 62. Thoti 63. Vallon 64. Valluvan\n# *\n1*\n67. Vetan 1[68. Vettuvan, Pulaya Vettuvan (in the areas of erstwhile Cochin State only) ६९ . Nerian]\nPART I. Madhya Pradesh 1. Audhelia 28. Kanjar २ Bagri, Bagdi 29. Katia, Patharia 3. Bahna, Bahana 30. Khatik 4 Balahi, Balai 31. Koli, Kori 5. Banchada 32. Kotwal (in Bhind, Dhar, Dewas, Guna, 6. Barahar Basod Gwalior, Indore, Jhabua, Khargone, Mandsaur, 7. Bargunda Morena, Rajgarh, Ratlam, Shajapur, Shivpuri 8. Basor, Burud, Bansor, Bansodi, Bansphor, Basar Ujjain and Vidisha Districts ) ० Bedia ३३. Khangar, Kanera, Mirdha 10. Beldar, Sunkar 34. Kuchbandhia ११. Bhangi, Mehtar, Balmiki, Lalbegi, Dharkar 35. Kumar (in Chhatarpur, Datia, Panna, Rewa, 12. Bhanumati Satna, Shahdol, Sidhi and Tikamgarh districts) 13. Chadar 1[36. Mahar, Mehra, Mehar, Mahara] 14. Chamar, Chamari, Bairwa, Bhambhi, Jatav, 37. Mang, Mang Garodi, Mang Garudi, Dankhani Mochi, Regar, Nona, Rohidas, Ramnami, Mang, Mang Mahasi, Madari, Garudi, Radhe Satnami, Surjyabanshi, surjyaramnami, Mang Ahirwar, Chamar, Mangan, Raidas 38. Meghwal 15. Chidar 39. Moghia 16. Chikwa, Chikvi 40. Muskhan 17. Chitar ४१. Nat, Kalbelia, Sapera, Navdigar, Kubutar १८. Dahait, Dahayat Dahat 42. Pardhi (in Bhind, Dhar, Dewas, Guna, 19. Dewar Gwalior, Indore, Jhabua, Khargone, Mandsaur, 20. Dhanuh Morena, Rajgarh, Ratlam, Shajapur, Shivpuri, 21. Dhed, Dher Ujjain and Vidisha Distircts) 22. Dhobi (in Bhopal, Raisen and Sehore distirct) 43. Pasi 23. Dohor ४४. Rujjhar २४. Dom Dumar, Dome, Domar, Doris 45. Sansi, Sansia २५. Ganda, Gandi 46. Silawat 26. Ghasi, Ghasia 47. Zamral 27. Holiya ३[४8. Sargara ]\nPART Z. Maharashtra १०. Bedar ११ . Bhambi Bhambhi Asadaru, Asodi, Chamadia, Chamar, Chamari, Chambhar, Chamgar, Haralayya, Harali, Khalpa, Machigar Mochigar, Madar, Madig, Mochi, Telegu Mochi, Kamati Mochi, Ranigar, Rohidas, Nona, Ramnami, Rohit, Samgar, Samagara, Satnami, Surjyabanshi, Surjyaramnami.\n1. Ager २ Anamuk 3. Aray Mala 4 Arwa Mala 5. Bahna, Bahana 6 Bakad, Bant 7. Balahi, Balai 8. Basor, Burud, Bansor, Bansodi 9 Beda Jangam, Budga Jangam\n१. Subs. by Act ६१ of २००२ , s. 2 and theFirst Sch., for entry 6�\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र\nService ID: 4\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: मूल निवासी प्रमाण पत्र\n  * Supporting Document 2: बिजली का बिल\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: टेलीफोन बिल\n  * Supporting Document 5: जन्म प्रमाण पत्र\n  * Supporting Document 6: वोटिंग कार्ड\n  * Supporting Document 7: बी.पी.एल. प्रमाण पत्र\n  * Supporting Document 8: घर या भूमि का दस्तावेज़\n  * Supporting Document 9: ड्राइविंग लाइसेंस\n  * Supporting Document 10: अन्य\n  * Supporting Document 11: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 12: फोटो परिचय पत्र\n  * Supporting Document 13: पिता / पालक की नौकरी का प्रमाण - पत्र\n  * Supporting Document 14: अनैच्छिक प्रवजन का आदेश\n  * Supporting Document 15: मूल निवासी प्रमाण पत्र\n- SNo 2: जाति का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: अन्य राज्य के अनुसूचित जाति / जनजाति प्रमाणपत्र\n  * Supporting Document 2: सरपंच / पार्षद / विधायक / साँसद से जाति प्रमाण-पत्र\n  * Supporting Document 3: प्राथमिक शाला या जिला शिक्षा अधिकारी द्वारा प्रमाणित प्राथमिक शाला द्वारा जारी स्थानान्तरण प्रमाण-पत्र\n  * Supporting Document 4: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 5: शैक्षणिक प्रमाण पत्र\n  * Supporting Document 6: आवेदक को या उसके किसी परिवारजन को जारी हुआ जाति प्रमाण पत्र\n  * Supporting Document 7: प्राथमिक परीक्षा उत्तीर्ण प्रमाण-पत्र\n  * Supporting Document 8: जन्म सूचना प्रपत्र\n  * Supporting Document 9: मिसल\n  * Supporting Document 10: अधिकार अभिलेख\n  * Supporting Document 11: जमाबंदी\n  * Supporting Document 12: १९३१ का जनगणना पंजी\n  * Supporting Document 13: 1949 का नागरिक पंजी\n  * Supporting Document 14: दाखिल / ख़ारिज पंजी\n  * Supporting Document 15: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 3: शपथ पत्र (Mandatory: नहीं)\n  * Supporting Document 1: शपथ पत्र\n- SNo 4: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 5: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ावली । आवदकं अथवा उसक पेता अथवा उसदः वैध पालक का शय२ प= प्ररूप २क क अनुस्तार मूल प्रति में दस्तावंज फ़िनत्ते नर्शित हा कि आवदक क पिता सज्य सरकार के अधकारी / फ॰ ारी हैं तथ राष्ट्रपत्तीय अधेसूचना तिथि अथवा अन्य पिछड़ वर्ग अधिसूचना तिथि को अथवः उसुके पूर्व # वर्तमान् मघ्यंप्रदेश नख्यं श्ेन क निदासी थे और राजः पुनगठन क फलस्वरूप उन्हें छत्ःीसगदः राज्य आदंटित हुा है। (6! अन्य रिघूड़ा वर्ग हेतु आवेदक के ऐिता का पूर्व चितीथ वर्ष का आय प्रमाणंच 7 अथदा फर्॰ १६ फः अमिप्रमाणित प्रति ! 7 आदेदक का पूर्ण एवं स्फ्ट पता लिखा हुआ लिफाफा जिस्ूमें यथेष्ट डाक टिकट लगी हो।\nप्राष्कर्ता के हस्ताक्षर एतं एद्नुत्ः\n\n--- Page 31 (no rotation needed) ---\nछत्तीसगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\n788 (२१ }\n8० ११\nप्ररूप ४ क १ नियम ९ देखिय)\nसक्षम प्राधिकारी का कार्यालय मंडल जिला. -bee==4= छत्तीसगढ़\nपुस्तक कमांक सरल क्रमांक.\nदिनाक\nसामाजिक प्रास्थिति प्रनाण+्पत्र अनुसूचित जाति के लिए\nहल्क नीले आसमानी) रंग के कागज मे\nएलदद्वार प्रमाणित किया जाता है कि॰ श्री / श्रीमती / कुगारी आस्म्ज आत्नज निवास ग्राभ तहसाल. पला छत्तीसगढ़ जाति का /की सदस्य है और संविधान के अनुच्छेद ३४१ के अध्यधीन इस जाति को छत्तीत्तगढ़ राज्य के संबंध में अनुसूचित जाति के रूप में विनिर्दिष्ट किया गया है और यह जाति मध्यप्रदेश पुर्नगठन अधिनियम॰ २००० की धारः १९ को तृतीय अनुसूची कें अनुकमांक पर अंकित है॰ अतः श्री / श्रीमती / कूमारी पिता ; पति श्री॰ अनुसूचित जाति का/ की है। 2+ यह प्रमाण+्पत्र इन उपबंधों क अधीन जारी किया गया है कि यदि जिला स्तरीय प्रमाणपत्र सत्यग़्पन संभिति अथवा उच्च स्तरीय प्रमाणीकरण छानदीन समिति के द्वारां अपनी जॉच / निरीक्षण में आवेदक\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: कमांक पर अंकित हैl॰ अतः श्री / श्रीमती / कुमारी पिता / पति श्री॰ अन्य पिछड़ा चर्ग का /को है !\n2- यह भी प्रमाणित किया जाता है कि श्री / श्रीमती / कुमारी कीमीलेयर सम्पन्न वर्ग व्यक्तियों / वर्गा की श्रेणी में नहीं आते हैं॰ जिसंकाः उल्लेंख भारत सरकार कार्मिक एवं प्रशिक्षण विभाग क पारपत्र संख्या 36012 /2२ /93 /स्था एससीटी ) दिनांक 8=9--93 यथा संशोधित परिपत्र संख्या 36033/3 /2004-स्था आरक्षण दिनांक .14=1t=2008 नथा सभान्य प्रशासन. विभाग के परिपत्र कमांक एफ-9-3 /२001 /१-३ दिनांक २४ 6 २००९ के कालम 3 में किया गया है\n3-\nयह प्रमाण-पत्र इन उपबंधों क अधीन जारीं किया ग़या है कि यदि जिला स्तरीय प्रमाणपत्र सत्यापन समिति अथव उच्द स्तरीय प्रनाणीकरणः छानबीन - समिति क द्वार अपनी जॉच / निरीक्षण सें आवदक श्री / श्रीमतीं / कुमारी क द्वारा प्रस्तुत सामाजिक प्रास्थिति क दावा असत्य अथवा कपटपूर्ण पाया जाता है तो`यह प्रमाण पत्र तत्कालं प्रभाव से निरस्त माना जावेगा तथा तत्समय प्रवृत्त किसी अन्य विधि में अंतर्दिष्ट क़िसी बातः के होते हुए भी छत्तीसगढ़ अनुसूचित जाति अनुसूचित जनजाति और अन्य पिछंड़ा वर्ग सामाजिक प्रास्थिति क प्रमाणीकरण का विनियमनः अधिनियम २०१३ की धारः 8 से १३ के अधीन कार्यवाही कीं जावेगी ;\nहस्ताक्षर\nप्रमाणीकरण अधिकारी का नाम पदनाम / पदमुद्रा\n\n--- Page 34 (no rotation needed) ---\n763 3२\nछत्तीसगढ़ राजपत्र. दिनक 2 सितम्बर २०१३\n# i t५t\nप्ररूतप 4 ख\n(नियम १० देखिए\nसक्षम प्राधिकारीं का कार्यालय\nएस्र ऋम्श सरत क्रमाक\nदिनंक\nअस्थायी रःगाजिक प्रास्थिति प्रभाण-्पत्र सफेद रंग क कागस में केवल प्राथमिल गाध्यमिक स्तर की शैक्षणिक संस्थाओं में प्रवेश तथा छात्रवृत्ति / शिष्यवृत्ति / अन्य प्रयोजनों फ सचीकृति हेतु मान्य )\nअ्रमणल किया ग़ज़ात है कि श्री / श्रीमती / कुमारी आभज आत्मजा न्यास ग्राम त्तहसील. जिला\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: vcilage City State Bicck eisii\n4\n5\nDistrict ' State\n१०. Inforatio ? relating t० Property: Sllic :mmovable Frea propaTty Agricaltural Laiia Louse Shon Others 2` (3` Cn Pppiicart 3 Fetict $ iia७२ 2 Ua ApPiicant $ Pateraal Crandiathcr $ Piarre 3 Oa Appiicant $ Lateinai Gendiather 5 !iame\nPH :l RZC Teisii Disiric Year 0ः Gbtaining buying property (4 *5` ८८\n\n--- Page 66 (no rotation needed) ---\n27888'642\nछत्तीसगढ रजपत्र दिनांक 2 सितम्बर २०१३\n१l. informatior felaring to Caste: S.}10, Reiative Caste\nSub- Caste\nCian (Gotra )\nCian Sign (Gotra Chinnha\nLite (Totem )\n४l )\n2\n(3\n(5)\n(6)\nCoplicant 5 Father Applicant 5 Hother 5 Fathier If Applicant is a Lady then her Husoand\n2\n3\n१२. Information relating Occupation: S.N0. Relative *1 ` *2) + Aoplicant 5 occupaticr 2 Occupation of Applicant s Fatier 3 Occupation Of Arnlic\"nr 47 Paterna Grandfainer 4 Occupation Of Arplicaia 5 क़ateral Grandiatner Occupation or _zzii t s soase\nTraditional Occupation (3}\nPresert Occupation (4`\n13. 14.\nAppiicant $ Mother tongie फ Appiicant $ caste has parate dialect. ihen tame of txe dialect 1$. Applicant s Caste has Cod Goddess tlie name of mne God Goadess 16. :ame of importani Gods Jdlaesses of Applicant $ caste 17. .ams Of Foik Dances of Apolicani s Caste 18. !ame of Folk Songs of Applicant s Caste 19. Name of importait festivais of Applicant $ Caste 20. Whetner matrimonial relatior Vith son dalghter of father $ sisier is permitted in Applicants Caste? 21. Whether matrimonial relation with son daughter of mother 5 brother is petmnitted in Applicant 5 Caste? 22. Whethe; Custom of Bridc Pricins is pevalent In Applicant 5 Caste? 23. ihether custom of dowry is prevalent in Appiicant s Casre? २4 Name of those Castes Clans MYit h whom marriages of Applicant s Caste Clan are possible 25. Name of those Castes with Whom Applicant s Caste has the relation of Roti (Bread 26. Name of Castes those are equivalent to Applicant ' $ Caste 27 Applicant $ Religion 28 Religion of Applicant s father 29. Detaiis of Applicant s Relatives\n\n--- Page 67 (no rotation needed) ---\nछत्तींसगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\n^288855)\nSlio.\nDetail\nFatheri 5 Brother (Paternai Uncie ) (3`\nMotter 5 Brother Aaternai Uncle) (४ `\nHusband of Husbaitso noiieफ़ifers Mother 5 Father 5 Father Sisier Sister (Fainer in- law , (5 (6)\n(2) }aine\n]\n2\nCaste\n3\nSub- Caste\n4\nCian ( Gotra )\n5\nOccupatior Willage Toun of Resiaence\n0\nTehsil\n8\nDistrici\n30. Attached aocuments\n(] ' Below mentiछaed documents of Applicant s father ancestors netitior ing thear casie:- Revenue docurent of ancestors (case fiie)\n]-\nJamtia-3andi Suivey) Or Giriawari bl\nStaie Settienert; OR\nDociment af Rigats (19S४); OR Sur ey of Foresi Department Forest Rights Certificate; OR Admission Rczisier of educationat institutioa; OR Register of Birih or Leath; OR !ationai Register Of Citizens ५४9 ; OR Cc: of Caste Certificaie, issued earlier to Father, Aacestor Or tl Teiative; Di\n+\n=\n#ी\nCerus (!9२ ): Sth domiciie certificate or any otier document verifying that al! * stors २f Le applicani TTCic residing in tlie geographical iiasit Qf ChnattisgaTii before the daie lmtt !9५{ Scग़eduiea Castc ), 6/09/1950 Sः `edhgled ?rice) G! २८४]२/9S४ (Other Backward Class .\n_\n\n--- Page 68 (no rotation needed) ---\n२९३ ४७९ }\nछित्तोसगढ़ राजपत्र . दिनांक 2 सितम्बर २०१३\n3\nFamily Trec commencing from ancestors io Caste certificate TeaLio hoider as obtained by Patwari. lf applicant = $ iainer isrwere dn employee Of Yes No Staie Govemment and in relation to SCISTIOBC, before dated 10/08!1950, 06/09/1950, 26/12/1984 Where resident of existing Staic of Madhya Pradesh and were allocated to the Statc of Chhattisgarh ७n State ReOrganiration, related documents If the applicant belongs to OBC and his father mother is ३ Yes No govemnment employee, document verifying their post aTId income certificate TT cpy of Form 1० of the preceding financial year\nEnveiopc haviang full and legibie adoress of the Applicant bearing adeqiaie postage stamnps tin Case tne ceniricaie is besired rough post) Affidavit Gf te Applicant (prescrined in Fora २A )\nYes Lic\nYes Nio\nhcreby sOlemniy afirm that tie iniormation Contziined in tne application is truc and corrcct to the test Of my kewiccge ard celier (\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या विवाहित बेटियां पिता के जाति प्रमाण का उपयोग करके एसटी प्रमाण पत्र के लिए आवेदन कर सकती हैं?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, विवाहित बेटियाँ पिता के जाति प्रमाण का उपयोग करके एस टी प्रमाण पत्र के लिए आवेदन नहीं कर सकती हैं। एस टी प्रमाण पत्र के लिए आवेदक का स्वयं का जाति प्रमाण होना अनिवार्य है। पिता के जाति प्रमाण का उपयोग करना इस प्रक्रिया के लिए मान्य नहीं है।
       ```
| 32 | `क्या निवास प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?` | 7 | 7 | ✅ MATCH | new_topic | 3.08s |

### Query 32 Details
* **Query**: `क्या निवास प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या मूल निवासी प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या मूल निवासी प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?"
       ```
     * **Response**:
       ```json
       क्या मूल निवासी प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या मूल निवासी प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?"
       ```
     * **Response**:
       ```json
       Is the 3-year school study rule for original resident certificate also applicable for OBC in Chhattisgarh?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या मूल निवासी प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the 3-year school study rule for original resident proof in Chhattisgarh for OBC?', 'topic_summary': 'Query about the 3-year school study rule for original resident proof in Chhattisgarh for OBC.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या मूल निवासी प्रमाण पत्र के लिए छत्तीसगढ़ में स्कूल अध्ययन का 3 साल का नियम ओबीसी के लिए भी है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
| 33 | `जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति` | None | 4 | ❌ MISMATCH | new_topic | 5.53s |

### Query 33 Details
* **Query**: `जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति`
* **Expected Service ID**: `None`
* **Classified Service ID**: `4`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Digital Signature Verification of Caste Certificate vs. Residence Verification Status`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन और निवास सत्यापन स्थिति के संबंध में:
  > 
  > **डिजिटल हस्ताक्षर सत्यापन:**
  > - आवेदन के समय डिजिटल हस्ताक्षर अनिवार्य है
  > - ई-डिस्ट्रिक्ट पोर्टल पर आवेदन जमा करने के बाद पावती जनरेट होती है
  > - आवेदन संख्या के आधार पर आवेदन की स्थिति देखी जा सकती है
  > - 22 दिनों के भीतर प्रमाण पत्र जारी किया जाता है
  > 
  > **निवास सत्यापन स्थिति:**
  > - निवास प्रमाण अनिवार्य नहीं है
  > - वैकल्पिक दस्तावेजों में बिजली बिल, राशन कार्ड, जन्म प्रमाण पत्र शामिल हैं
  > - आवेदन जमा करने के बाद सत्यापन प्रक्रिया शुरू होती है
  > - प्रमाण पत्र जारी होने के बाद ई-डिस्ट्रिक्ट पोर्टल से डाउनलोड किया जा सकता है
  > 
  > **मुख्य अंतर:**
  > - डिजिटल हस्ताक्षर आवेदन की वैधता सुनिश्चित करता है
  > - निवास सत्यापन वैकल्पिक है और आवेदन के बाद होता है
  > - दोनों प्रक्रियाएं एक साथ चलती हैं लेकिन सत्यापन के समय भिन्न होती हैं
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति"
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति"
       ```
     * **Response**:
       ```json
       Digital Signature Verification of Caste Certificate vs. Residence Verification Status
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: SC/ST Certificate\nService ID: 4\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Domicile Certificate\n  * Supporting Document 2: Electricity Bill\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Telephone Bill\n  * Supporting Document 5: Birth Certificate\n  * Supporting Document 6: Voters Identity Card\n  * Supporting Document 7: Bpl Certificate\n  * Supporting Document 8: Land And House Document\n  * Supporting Document 9: Driving License\n  * Supporting Document 10: Other Documents\n  * Supporting Document 11: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 12: Photo Identity Card\n  * Supporting Document 13: Service Certificate Of Father / Guardian\n  * Supporting Document 14: Order Of Involuntary Migration\n  * Supporting Document 15: Domicile Certificate\n- SNo 2: Caste Proof (Mandatory: Yes)\n  * Supporting Document 1: Sc/St Certificate Of Other State\n  * Supporting Document 2: Sc/St Certificate From Sarpanch / Parshad / Mla / Mp\n  * Supporting Document 3: Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo\n  * Supporting Document 4: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 5: Educational Certificate\n  * Supporting Document 6: Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family\n  * Supporting Document 7: Primary School Certificate\n  * Supporting Document 8: Birth Information Form\n  * Supporting Document 9: Misal\n  * Supporting Document 10: Adhikar Abhilekh\n  * Supporting Document 11: Jamabandi\n  * Supporting Document 12: Census Register Of 1931\n  * Supporting Document 13: Citizen Register Of 1949\n  * Supporting Document 14: Dakhil / Kharij Panji\n  * Supporting Document 15: Disability / Unavailability Proof\n- SNo 3: Affidavit (Mandatory: No)\n  * Supporting Document 1: Affidavit\n- SNo 4: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 5: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 6: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste STSC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number\n\n--- Source 2: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: तररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट िेकर सुरलित रखें। \n \nचित्र क्रमाांक 20 \nआवेदन संदभा क्रमांक की सहायता से आवेदन की स्थस्थतत छत्तीसगढ़ ई-डिस्ट्रिक्ट क े  पोटटि पर देखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेदन जमा करने क े  बाद डनधाटररत 22 क्रदऩों की समय-सीमा क े  अ ां दर आवेदन का डनराकरण कर क्रदया जाता है। \n• ई-डिस्ट्रिक्ट पोटटि पर आवेदन की स्थस्थतत देखी जा सकती है। \n• अनुसूचित जातत अथवा जनजातत प्रमाण पत्र जारी होने क े  उपराांत इसकी डिचजटि प्रतत ई-डिस्ट्रिक्ट पोटटि से िाउनिोि की \nजा सकती है।\n\n--- [Document: 4_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and\n\n--- Source 3: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �् जनजातर् प्रमाण पत्र के र्लए आवेदन ................................ ................................ .. 9 \nिरण 6: आवश्यक दस्तावेज़ अपलोि करना ................................ ................................ ................................ ............................ 10 \nिरण 7: पूवाावलोकन और आवेदन जमा करना ................................ ................................ ................................ ......................... 11 \nिरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ .. 0 \nिरण 9: पावर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ .......................... 1\n\n--- Page 3 ---\nहोम पेज: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nअनुसूचित जातत/अनुसूचित जनजातत प्रमाण पत्र क े  लिए ऑनिाइन आवेदन हेतु अपने कम्प्यूटर या िैपटॉप क े  \nवेब ब्राउज़र में टाइप करें \ncgedistrict.cgstate.gov.in \n \nछत्तीसगढ़ ई-डिस्ट्रिक्ट पोटटि का होम पेज खुिेगा। \n \nचित्र क्रमाांक 1\n\n--- Page 4 ---\nिरण 1: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर पंजीयन \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटटि पर डनम्न प्रक्रक्रया द्वारा रचजस्टर करें। \n \nचित्र क्रमाांक 2 \nिरण 1.1: नए पांजीयन हेतु क्रदए गए लििंक पर क्लिक करें, डनम्नानुसार नागररक पांजीकरण पेज खुिेगा। \n \nचित्र क्रमाांक 3 \n \nिरण 1.2: नागररक पांजीकरण पेज पर आवेदक उपयोगकताट नाम दजट करें। \nिरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ दजट करें। \nिरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रचजरिेशन प्रक्रक्रया पूणट होती है।\n\n--- Page 5 ---\nिरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nडनम्न प्रक्रक्रया द्वारा पांजीक ृ त उपयोगकताट िॉतगन करें। \n \nचित्र क्रमाांक 4 \n1. यूज़रनेम दजट करें। \n2. पासविा दजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पांजीक ृ त नांबर पर प्राप्त ओटीपी यहााँ दजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nिरण 3: योजना खोज \nिरण 3.1: योजना खोज पेज में दी गई जानकारी भरें। \nिरण 3.2: खोजें पर क्लिक करें। \n \nचित्र क्रमाांक 5 \n \nिरण 3.3: सेवाओां की सूिी खुिेगी। इसमें  अनुसूचिर् जातर् / अनुसूचिर् जनजातर् प्रमाण पत्र देखें।  \nिरण 3.4: यक्रद यह सेवा सूिी में शातम\n\n--- Source 4: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: दी गई जानकारी भरें। \nिरण 3.2: खोजें पर क्लिक करें। \n \nचित्र क्रमाांक 5 \n \nिरण 3.3: सेवाओां की सूिी खुिेगी। इसमें  अनुसूचिर् जातर् / अनुसूचिर् जनजातर् प्रमाण पत्र देखें।  \nिरण 3.4: यक्रद यह सेवा सूिी में शातमि नहीं है तो ऊपर क्रदए गए होम बटन पर क्लिक करें। डनम्नानुसार पेज \nखुिेगा। \n \nचित्र क्रमाांक 6\n\n--- Page 7 ---\nिरण 3.5: इस पेज पर “सभी सेवाए ँ  देखें” पर क्लिक करें। सेवाओां की सूिी खुिेगी। \n \nचित्र क्रमाांक 7 \n \nिरण 3.6: सेवाओां की सूिी में से अनुसूचित जातत/अनुसूचित जनजातत प्रमाण पत्र खोजने क े  लिए सिट बार में \nसेवा का नाम टाइप करें। \n \n \nचित्र क्रमाांक 8\n\n--- Page 8 ---\nिरण 3.7: अब चित्र क्रमाांक 8 क े  अनुसार अनुसूचित जाचत/अनुसूचित जनजाचत प्रमाण पत्र क े  सामने दिए गए \nबटन पर क्लिक करें। दनम्नानुसार पेज खुलेगा \n \n \nचित्र क्रमाांक 9 \nिरण 3.7: आधार ई-प्रमाणीकरण प्रक्रक्रया क े  लिए आगे बटन पर क्लिक करें। \nइस पेज पर अनुसूचित जातत/अनुसूचित जनजातत प्रमाण पत्र हेतु आवश्यक दस्तावेज़़ों की सूिी देखी सकती है। \n \nचित्र क्रमाांक 10\n\n--- Page 9 ---\nिरण 4: आधार ई-प्रमाणीकरण \nआधार ई-प्रमाणीकरण क े  लिए डनम्नलिखखत प्रक्रक्रया का पािन करें। \n \nचित्र क्रमाांक 11 \nिरण 4.1: फॉमट में पूछी गई जानकाररयााँ दजट कर Aadhaar e-Authentication पर क्लिक करें। डनम्नानुसार \nएक पॉप-अप तविंिो खुिेगा। \n \nचित्र क्रमाांक 12 \nिरण 4.2: आधार का तववरण भरें। \nिरण 4.3: सहमतत देने क े  लिए डनधाटररत बॉक्स पर क्लिक करें। \nिरण 4.4: जानकारी भरकर Authentication बटन पर क्लिक करें। \nिरण 4.5: चित्र क्रमाांक 11 क े  अनुसार पेज पर क्रदए गए जमा करें बटन पर क्लिक करें।\n\n--- Page 10 ---\nिरण 5: अनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र क े  र्लए आवेदन \nिरण 5.1: आवेदन फॉमट में सामान्य तववरण और वतटमान पता दजट करें। \n \nचित्र क्रमाांक 13 \n \nिरण 5.2: स्थायी पते का तवव\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र\nService ID: 4\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: मूल निवासी प्रमाण पत्र\n  * Supporting Document 2: बिजली का बिल\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: टेलीफोन बिल\n  * Supporting Document 5: जन्म प्रमाण पत्र\n  * Supporting Document 6: वोटिंग कार्ड\n  * Supporting Document 7: बी.पी.एल. प्रमाण पत्र\n  * Supporting Document 8: घर या भूमि का दस्तावेज़\n  * Supporting Document 9: ड्राइविंग लाइसेंस\n  * Supporting Document 10: अन्य\n  * Supporting Document 11: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 12: फोटो परिचय पत्र\n  * Supporting Document 13: पिता / पालक की नौकरी का प्रमाण - पत्र\n  * Supporting Document 14: अनैच्छिक प्रवजन का आदेश\n  * Supporting Document 15: मूल निवासी प्रमाण पत्र\n- SNo 2: जाति का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: अन्य राज्य के अनुसूचित जाति / जनजाति प्रमाणपत्र\n  * Supporting Document 2: सरपंच / पार्षद / विधायक / साँसद से जाति प्रमाण-पत्र\n  * Supporting Document 3: प्राथमिक शाला या जिला शिक्षा अधिकारी द्वारा प्रमाणित प्राथमिक शाला द्वारा जारी स्थानान्तरण प्रमाण-पत्र\n  * Supporting Document 4: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 5: शैक्षणिक प्रमाण पत्र\n  * Supporting Document 6: आवेदक को या उसके किसी परिवारजन को जारी हुआ जाति प्रमाण पत्र\n  * Supporting Document 7: प्राथमिक परीक्षा उत्तीर्ण प्रमाण-पत्र\n  * Supporting Document 8: जन्म सूचना प्रपत्र\n  * Supporting Document 9: मिसल\n  * Supporting Document 10: अधिकार अभिलेख\n  * Supporting Document 11: जमाबंदी\n  * Supporting Document 12: १९३१ का जनगणना पंजी\n  * Supporting Document 13: 1949 का नागरिक पंजी\n  * Supporting Document 14: दाखिल / ख़ारिज पंजी\n  * Supporting Document 15: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 3: शपथ पत्र (Mandatory: नहीं)\n  * Supporting Document 1: शपथ पत्र\n- SNo 4: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 5: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: �ी करने हेतु शपथ पत्र\nमैं श्री / श्रीमती / कुमारी आत्मज / आत्मजा उम्र वर्ष व्यवसाय निवास त्तहसाल जिला र््य एतदद्वारा शपथपूर्वक निम्नलिखित कथनं करता / करती हूॅ कि .-~\nछायाचित्र\nआवदक क हस्ताकर\nमेरेद्वारा कम प्राधिकारी क समक्ष प्ररूप दा क के अधींन विहित़ अनुसार सामाजिक प्रास्थिति प्रमाण- पत्र जारी करने हेतु आवेदन किया गया है जिसके समर्थन में यह शपथ पत्र एतदद्वारा प्रस्तुत हे. मरे द्वारा सक्षम प्राधिकारी क संमक्षं विहित प्ररूप अनुसार आवेदनःःपत्र के साथ दस्तावजों को नंकल संलग्न की गईं है॰ उक्त वर्णित दस्तावेज द्वार प्राधिकृत व्यक्ति से विधि पूर्वक प्राप्त किय गय हैं॰ तथा नेर द्वारा या मेरे किसी शुभचिंतक द्वारा - उवत दस्तावज या उसक मूल दस्तावेज भें अनाधिकृत रूप से कोई संशोधन / विलोपन / परिवर्धन नहीं किया गय है तथा मेरे सर्वात्तम ज्ञान एवं जानकारी में उक्त दस्तावेज / दस्तावेजों को किस्ी विद्वेषपूर्ण आशय से गढ़ा नहीं गया है मेरे द्वारा जिन रिश्तेदारों क वेधता प्रमाणपत्र इस आवेदन क सांथ संलग्न किया गया है उनक साथ संबंध दर्शान वाला वंशवृक्ष संलग्न है एतदद्वारा घोषणा करता हूॅ कि सामाजिक प्रास्थिति प्रमाणपत्र जारी करने हेतु सक्षम प्राधिकारी क समक्ष विहित प्रपत्र में प्रस्तुत आवेदन पत्र में मेर द्वारा दी गईं रमस्त जानकारी मेरे सर्वोत्तम ज्ञान एवं जानकारी क अनुस्तार सत्य हे तथा उक्त जांनकारी असत्य पाए जाने .पर॰ मेरे विरूद्घ छत्तीसगढ़ अनुसूचित जाति अनुसूचिंत जनजाति और अन्य पिछड़ा वर्ग सामाजिक प्रास्थिति क प्रमाणीकरण कः विनियमन , अधिनियंम २०१३ को धारा 8 स १३ के अनुसार कार्यवाहींः की जावे.\n2\nहस्ताक्षर आवदक का नाम\n\n--- Page 24 (no rotation needed) ---\n788:\"22!}\nछंत्तीसग़ढ़ रांजपत्र; दिनांक 2 सितम्बर २०१३\nसत्यापन\nमैं श्री / श्रीमती / कुमारी आक़्मज आन्मजा सत्यापित करत\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ो।\nप्राप्तकर्ता क हस्ताक्षर एवं पदमुद्रा\n\n--- Page 28 (no rotation needed) ---\n788 २६ २९-\nछत्तोसगढ़ राजपत्र टिनांक 2 सितम्बर २०१३\nप्ररूप 3 ख [ नियम ६२ ]\nसक्षम प्राधिकारी का कार्यालय\nआदेदन पत्र क वापसी का ज्ञापनं वापसी झापन)\n(इप् ज्ञापन की मूल प्रति आवेदक को प्रदत्त की जावे तथा उसूका प्रतिपर्ण कार्यालय में संधारित किया जावे\nकमांक\nदिनांक\nश्र श्रीमती / कुमारी आत्मज आन्मजा निवासी द्वारा सामाजिक प्रास्थिति प्रमाणन्पत्र जारी करने हेतु प्रस्तुत आवेदन पत्र में निम्नाकित अभिलेखों क अभाव है॰ अतः अवेदक को निर्देशित किया जाता है कि निम्नांकित अंभिलेख जिनमें सही * का निशान अंकित किया गया है आवेदन पत्र॰के साथ प्रस्तुत करने पर उसके सामाजिए प्रास्थिति प्रगाण-् पत्र जारी करने की कार्यवाही प्रारंभ कीजा सकगीः- (1 ) आवेदक अथवा आवेदक क पिता / पूर्वजों का निम्नांकित दस्तावेज जिसमें उसकी जाति अंकित है पूर्वजों के राजस्व दस्तावेज गिशल) जमाबंदी सर्वेक्षण गिरदावरीः 8 सष्चियबंदोबस्तिलेख (१९५ ; जनगणना (१९३१ ; (छः) वन विभाग की जमाबंदीः नागरिकों का राष्ट्रीय रजिस्टर (१९३९ ; ६ जन्म यां मृत्यु की पंजपीः पिता अथवा पूर्वज के शिक्षित होने को स्थिति में प्रवेश दाखिल / खारिज) पंजी पिताः पूर्वज अथवा संबंधी नातेदार को पूर्व में जारी जाति ग्रगाण प्रमाण-पत्र कों प्रात ग्राारह अन्य दस्तावे जिसस आवेदक क द्वारा दावा की गई जाति होनां प्रमाणित होता है बारह\n(2) ऐरो दस्तावेज अथवा दस्त्तावेजों की रूम्यक रूप सें अंभिप्रभाणित प्रतिलिपि अथवा प्रतिलिपियां जिससे यह प्रमाणित हो सके के आवेदक के पूर्वज राष्ट्रपतीय अधिसूचना तिथि अथवा अन्ग गिछड़ा वर्गकी अधिस्चना तिथि के पूर्व से छत्तीरागड की भैगोलिक सीमा में निवास करते थे। पूर्वजों सेः प्रारंभ कर आवेदक तक पटवारी से प्रदत्त वंशावली ( आवेदक अ�\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ्तरीय सामाजिक प्रांस्थिति प्रमाण पत्र सत्यापन सनिति क सनक्ष विहित परूप में प्रस्तुत्त आवेदन पत्र में गेरे द्वारा दो गई जानंकारी मेरी सर्वोत्तम जानकारी क अनुसार सत्य एवं सही है तथा उक्त णानका२ असन्य पाए जाने पर मेरे विरूद्घ छत्तीसगढ़ अनुसूचित जाति अनुसूचित जनजाति और अन्य पिछड़ा तर्गं सामाजिक प्रास्थितिं के प्रभाणीकरण का विनियमनः अधिनियभ २०१३ की धारा 8 से १३ में निर्दिष्ट का्यवाही की जा सकेगी\nसथान दिनाँक :\nहस्ताक्षर\nसत्यापन\nआ॰ / आत्मजा / पतिं\nसत्यापित करता हूॅ कि इस शपथ पत्र की कण्डिका १ से 4 को विषयवस्तु मेरी व्यक्तिगत जानकारी एवं विश्वास क अनुसार सत्य एवं सहों हें॰ जिसे में आज दिनाँक को छत्तीरगढ़ में सत्यापित एवं हस्ताक्षरित करता हूॅू।\nहस्त्ाक्षर\n\n--- Page 27 (no rotation needed) ---\nछत्तींसगढ़ राजपत्र, दिनंक 2 सितम्बर २०१३\n788 ( 25)\nप्ररूप 3 क नियम 5 देखिये\nसक्षन प्राधिकारी का कार्यालय मंडल जिला........ छत्तीसगढ\nआवर क्रमांक\nदिनाक\nआवेदन पत्र की अभिस्वीकृति पावती\nइस ज्ञापन की मूल प्रति आवेदक को प्रदत्त्त की जावे तथाः उसका प्रतिपर्ण कार्यालय में संधारित किया जावे आज दिनांक को श्री / श्रीमती / कुमारी ' आभण़ /पत्नीं वप व्यवसाय निवासी तहसील जिला रज्य से स्ामाजिक प्रास्थिति प्रमाणनपत्र जारो करने हेतु आवेदन पत्र प्राप्त किंया गया है। उक्त आवेदन पत्र के साथ निन्नांकित दस्तावेज मूल अभिप्रमाणित प्रति गें प्राप्त्त हुए है 1 आवेदक अथवा आवेदक क पिता / पूर्वजों का निम्नांकित दस्तातेज जिसमें उरकी जाति अंकित है पूर्वजों क राजस्व दस्तावेज भिरल) जनाबंदी सर्वेक्षण गिरदावरीः 8 आष्कबंदोबशनलेख (१९५६); जनगणना (1931); (छः) वन विभाग की जनाबंदी; रात नागरिकों का राष्ट्रीय रजिस्टर १९४९ ; आट जन्म या मृत्युं की पंजीः दैस ) थिता अथवा पूर्वज के शिक्षित होने की स्थि�\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन बनाम निवास सत्यापन स्थिति\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र डिजिटल हस्ताक्षर सत्यापन और निवास सत्यापन स्थिति के संबंध में:
       
       **डिजिटल हस्ताक्षर सत्यापन:**
       - आवेदन के समय डिजिटल हस्ताक्षर अनिवार्य है
       - ई-डिस्ट्रिक्ट पोर्टल पर आवेदन जमा करने के बाद पावती जनरेट होती है
       - आवेदन संख्या के आधार पर आवेदन की स्थिति देखी जा सकती है
       - 22 दिनों के भीतर प्रमाण पत्र जारी किया जाता है
       
       **निवास सत्यापन स्थिति:**
       - निवास प्रमाण अनिवार्य नहीं है
       - वैकल्पिक दस्तावेजों में बिजली बिल, राशन कार्ड, जन्म प्रमाण पत्र शामिल हैं
       - आवेदन जमा करने के बाद सत्यापन प्रक्रिया शुरू होती है
       - प्रमाण पत्र जारी होने के बाद ई-डिस्ट्रिक्ट पोर्टल से डाउनलोड किया जा सकता है
       
       **मुख्य अंतर:**
       - डिजिटल हस्ताक्षर आवेदन की वैधता सुनिश्चित करता है
       - निवास सत्यापन वैकल्पिक है और आवेदन के बाद होता है
       - दोनों प्रक्रियाएं एक साथ चलती हैं लेकिन सत्यापन के समय भिन्न होती हैं
       ```
| 34 | `जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण` | 3 | 3 | ✅ MATCH | new_topic | 26.79s |

### Query 34 Details
* **Query**: `जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Village Marriage Registrar for Caste Certificate Holders in the Village`
* **Resolved Hindi Query**: `जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > जाति प्रमाण पत्र धारकों के लिए विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण"
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण"
       ```
     * **Response**:
       ```json
       Village Marriage Registrar for Caste Certificate Holders in the Village
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'marriage registration in village for caste certificate holders', 'topic_summary': 'User is asking about marriage registration process for caste certificate holders in a village, which is a different service from the general government services discussed previously.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '1', 'service_id': '3'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- MARRIAGE JURISDICTION RULE: Under the Chhattisgarh Compulsory Registration of Marriages Rules, a marriage MUST be registered in the local area where the marriage was solemnized or performed, NOT at the couple's hometown or place of residence. The registrar is the Local Authority of that local area (Gram Panchayat if rural; Municipality or Municipal Corporation if urban). State this clearly when citizens ask where or under which office/authority to register their marriage.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Marriage Registration & Certificate\nService ID: 3\nLanguage: EN\nDepartment: Urban Administration and development Department\nTime Limit / SLA: 15 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: At The Time Of Marriage Combined Photograph Of Groom And Bride(2a Size) (Mandatory: Yes)\n  * Supporting Document 1: At The Time Of Marriage Combined Photograph Of Groom And Bride(2a Size)\n- SNo 3: Declaration Letter From Guardian Of Married Couple (Mandatory: No)\n  * Supporting Document 1: Declaration Letter From Guardian Of Married Couple\n- SNo 4: Other (Mandatory: No)\n  * Supporting Document 1: Other\n- SNo 5: Necessary Documents (Mandatory: No)\n  * Supporting Document 1: Necessary Documents\n- SNo 6: Birth Certificate Of Groom (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate Of Groom\n- SNo 7: Birth Certificate Of Bride (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate Of Bride\n- SNo 8: Document Signed By The Bride And Groom (First Page) (Mandatory: Yes)\n  * Supporting Document 1: Document Signed By The Bride And Groom (First Page)\n- SNo 9: Document Signed By The Bride And Groom (Second Page) (Mandatory: Yes)\n  * Supporting Document 1: Document Signed By The Bride And Groom (Second Page)\n- SNo 10: Copy Of Challan (Mandatory: Yes)\n  * Supporting Document 1: Copy Of Challan\n- SNo 11: Marriage Invitation Card (Mandatory: Yes)\n  * Supporting Document 1: Marriage Invitation Card\n- SNo 12: Divorce Certifcate (Mandatory: No)\n  * Supporting Document 1: Divorce Certificate\n- SNo 13: Widow Certificate (Mandatory: No)\n  * Supporting Document 1: Widow Certificate\n- SNo 14: Inter Religion Marriage Certificate (Mandatory: No)\n  * Supporting Document 1: Inter Religion Marriage Certificate\n\nAPPLICATION FORM FIELDS:\n- Field: Marriage Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Date of Marriage [Type: date, Data: Date] (Row: 2, Col: 1)\n- Field: Place of Marriage [Type: textarea, Data: Alfa Numeric] (Row: 2, Col: 2)\n- Field: Type of Marriage [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Is marriage Registered [Type: drop down, Data: Charactar] (Row: 3, Col: 2)\n- Field: Registration Number [Type: text, Data: Number] (Row: 4, Col: 1)\n- Field: Other Details [Type: textarea, Data: Charactar] (Row: 4, Col: 2)\n- Field: Groom Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Name of Groom in Local Language [Type: text, Data: Charactar] (Row: 6, Col: 1)\n- Field: Name of Groom in English [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Date of Birth of Groom [Type: date, Data: Date] (Row: 7, Col: 1)\n- Field: Age at time of marriage [Type: text, Data: Number] (Row: 7, Col: 2)\n- Field: Father Name in local language [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Father Name in English [Type: textarea, Data: Charactar] (Row: 8, Col: 2)\n- Field: Marital Status of Groom [Type: drop down, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address Of Groom [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Present Address of groom in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Present Address of Groom in English [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 2)\n- Field: Permanent Address of Groom in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Permanent Address of Groom in English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 2)\n- Field: Witness Details of Groom Side [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Bride Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Name of Bride in local language [Type: text, Data: Charactar] (Row: 15, Col: 1)\n- Field: Name of Bride in English [Type: text, Data: Charactar] (Row: 15, Col: 2)\n- Field: Date of Birth of Bride [Type: date, Data: Date] (Row: 16, Col: 1)\n- Field: Bride Age at time of marriage [Type: text, Data: Number] (Row: 16, Col: 2)\n- Field: Fathers name of Bride in Local language [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: Fathers name of Bride in English [Type: text, Data: Charactar] (Row: 17, Col: 2)\n- Field: Marital Status of Bride [Type: drop down, Data: Charactar] (Row: 18, Col: 1)\n- Field: Address Of Bride [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: Present Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Present Address\n\n--- Source 2: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: Row: 16, Col: 1)\n- Field: Bride Age at time of marriage [Type: text, Data: Number] (Row: 16, Col: 2)\n- Field: Fathers name of Bride in Local language [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: Fathers name of Bride in English [Type: text, Data: Charactar] (Row: 17, Col: 2)\n- Field: Marital Status of Bride [Type: drop down, Data: Charactar] (Row: 18, Col: 1)\n- Field: Address Of Bride [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: Present Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Present Address of Bride in English [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: Permanent Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 1)\n- Field: Permanent Address of Bride in English [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 2)\n- Field: Witness Details of Bride Side [Type: fieldset, Data: Alfa Numeric] (Row: 22, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 3_en_3.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nवििाह पंजीकरण एिं प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nपर ऑनलाइन आिेदन\n\n--- Page 2 ---\nविषय सूची \nई-डिस्ट्रिक्ट: होम पेज ................................ ................................ ................................ ................................ ................................ .................. 2 \nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण ................................ ................................ ................................ ................................ ............... 3 \nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन ................................ ................................ ................................ ................................ .................... 4 \nचरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ .................. 5 \nचरण 4: आिेदक की बुडनयादी जानकारी ................................ ................................ ................................ ................................ ............... 6 \nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन ................................ ................................ ................................ ....................... 7 \nचरण 6: आिश्यक दस्तािेज़ अपलोि करना ................................ ................................ ................................ ................................ .......... 8 \nचरण 7: पूिाािलोकन और आिेदन जमा करना ................................ ................................ ................................ ................................ ...... 9 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 10 \nचरण 9: पािर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ................................  11\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉगगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉगगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nच\n\n--- Source 3: [User Manual (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: official_document\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nOfficial Document Content: --- Page 1 (no rotation needed) ---\nTHE CHHATTISGARH COMPULSORY REGISTRATION OF MARRIAGES RULES, २००६\nTHE CHHATTISGARH COMPULSORY REGISTRATION OF MARRIAGES RULES, 2006\nRule\n1. Short title, extent and commencement\n(1) These Rules may be called the Chhattisgarh Compulsory Registration of Marriages Rules, २००६.\n(२) It extends to the whole State of Chhattisgarh.\n(3) It shall come into force from the date of its publication in the Official Gazette\nRule २. Definitions.\nIn these rules, unless the context otherwise, requires\n(a) \"Chief Registrar\" means Chief Registrar appointed under Rule 3;\n(b) \"Government\" means State Government of Chhattisgarh;\n(C) \"Local area\" means the area comprising of Gram Panchayat or Municipality or Municipal Corporation as the case may be;\n(d) \"Local Authority\" means Gram Panchayat or Municipality Or a Municipal Corporation as the case may be;\n(el \"Marriage\" means and includes all marriages solemnized performed or contracted between a male and a female, irrespective of the religion Or caste of either party to the marriage, and also includes marriages performed as per law, custom practice or any tradition of either party to the marriage and includes a remarriage;\n(f) Memorandum means a memorandum of marriage referred to in Rule-4;\n(g) \"Priest\" means any person who solemnizes marriage;\n(h) \"Register\" means the Register of marriages maintained under the Rules;\n(i) \"Registrar\" means Registrar under the provision of subrule (२) of Rule ३ of the Rule\nRule\n3. Appointment of Chief Registrar and Registrar.\n(२) The State Government may by notification appoint any officer as Chief Registrar for the State\n(2) Local Authority shall be the registrar for its local area for the purpose of these Rules.\nRule\n4. Registration of Marriage\n(1) (a) From the date of coming into forceof these Rules every marriage solemnized in the State shall be registered.\n(b) The parties to a marriage shall submit a memorandum in the Form specified in Schedule \"A and shall deliver or send by registered post in duplicate to the Registrar of the area where marriage is\nlegitquest\" (Page 1 of ७) Inlotntiono Insihhollilellgtikt\nPrinted For: 10-04-20२6 at 1२:O३:PM\n\n--- Page 2 (no rotation needed) ---\nTHE CHHATTISGARH COMPULSORY REGISTRATION OF MARRIAGES RULES, २००६\nsolemnized Or performed within a period of thirty days from the date of marriage.\n(C ) The Registrar of Marriage may accept memorandum of the marriage beyond the limitation prescribed, if party to the marriage establishes that he was prevented by any cause beyond his control.\n(d) After examining the memorandum submitted by the parties Registrar shall enter the entries of the memorandum in the register specified in Schedule \"C\".\n(e) Each memorandum filled in the Register shall be treated as 6 separate entry and each entry shall be numbered in a consecuting series which will commence and terminate with each calendar year, a fresh series being commenced with the beginning of each year.\n(f) The Registrar shall send me records of all marriages in form specified in schedule \"B\" to the Chief Registrar.\n(2) Where the Registrar before whom the memorandum is submitted on scrutiny of the documents submitted with the memorandum Or, On the other facts noticed or brought to his notice is satisfied 0r has reasons to believe that:\n(al the marriage between the parties is not performed in accordance with any law for the time being in force; 0r\n(b ) the marriage between the parties is not performed in accordance with the personal law of the parties; Or\n(c) the identity of the parties or the witnesses or the persons testifying the identity of the parties and the solemnization of the marriage is not established beyond reasonable doubt; 0r\n(d) the documents tendered before him do not prove the marital status of the parties.\nhe may, after hearing the parties and recording the reasons in writing refuse to register the marriage and may\n(i) call upon the parties to produce such further information 0r documents as deemed necessary, for establishing the identity of the parties and the witnesses 0r correctness of the information 0r documents presented to him, Or\n(iil if deemed necessary, also paper the papers to the local police station within whose jurisdiction the parties reside, for verification.\n(3) Where on further verification as provided in sub rule (२) the Registrar is satisfied that there is no objection to register the marriage he may register the same. If in the opinion of the Registrar, the marriage is not fit for registration, he may pass an order of refusal in writing, recording the reasons and send the duplicate copy t० the Chief Registrar.\nRule 5. Appeal to Chief Registrar\n(1) Any person aggrieved by the order of the Registrar refusing to register the marriage under Rule 4 may within a period of thirty days from the date of receipt of such order, appeal to the Chief Registrar accompanied by fees of Rs. 30/-.\nlegitquest\" (Page 2 of ७) Inlotntiono Insihhollilellgtikt\nPrinted For: 10-04-20२6 at 1२:O३:PM\n\n--- Page 3 (no rotation needed) ---\nTHE CHHATTISGARH COMPULSORY REGISTRATION OF MARRIAGES RULES, २००६\n(2) The Chief Registrar after giving an opportunity of being heard to the parties pass an order in writing, recording the reasons, directing the Registrar to register the marriage or confirm the order of the Registrar.\nRule 6. Appeal to District Judge.\nAny person aggrieved by the order of the Chief Registrar may within a period of thirty days from the date of the order, appeal to the District Judge within the local limits of whose jurisdiction the Registrar of Marriages has his office and the decision of the District Judge shall be final.\nRule\n७. Register of Marriages. (1) The Registrar shall maintain a Register of marriages solemnized performed in the local area for which he is appointed, in such form as specified in schedule \"C\" and enter description given by parties in memorandum and authenticate the same and send a copy of the entry to the Chief Registrar.\n(2) The Registrar shall issue a certificate of the Registration of the marriage to the parties in the form shown in the schedule \"D\"\nRule 8. Register to be open for public inspection\nThe Register of marriages shall , at all reasonable times, be open to inspection and the certified extracts there from shall, On application, be given by the Registrar to the applicant on payment of tees of Rs. 20/-.\nRule\n9. Non Registration of marriages. No marriage performed to which these Rules apply shall\n\n--- Source 4: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉगगन प्रगक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासििा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \nचरण 3.2: खोजें पर क्लिक करें। सेवाओं की सूची खुलेगी। \n \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.3: सेवाओं की सूची में प्रिजशित वििाह प्रमाण पत्र (Marriage Certificate) पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। इस पेज पर आवश्यक िस्तावेज़़ों की सूची भी िेखी जा सकती है। \n \n \nचचत्र क्रमांक 7: सेिा पररचय एिं सहायक दस्तािेज़़ों की सूची \n \nचरण 3.4: “आगे” बटन पर क्लिक करें।\n\n--- Page 7 ---\nचरण 4: आिेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: विवाह पंजीकरण एवं प्रमाण पत्र\nService ID: 3\nLanguage: HI\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nTime Limit / SLA: 15 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: वर एवं वधु का संयुक्त फोटो(2A साईज) प्रमाण पत्र के लिए (Mandatory: हाँ)\n  * Supporting Document 1: वर एवं वधु का संयुक्त फोटो(2A साईज) प्रमाण पत्र के लिए\n- SNo 3: प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: विवाह अनुस्थान संपन्न कराने वाले के सत्यापन के लिए उस समय उपस्थित पंडित /पादरी /मौलवी अथवा समाज का प्रमाण पत्र\n- SNo 4: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य कारण\n- SNo 5: आवश्यक दस्तावेज़ (Mandatory: नहीं)\n  * Supporting Document 1: आवश्यक दस्तावेज़\n- SNo 6: वर का जन्म प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: वर का जन्म प्रमाण पत्र\n- SNo 7: वधु का जन्म प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: वधु का जन्म प्रमाण पत्र\n- SNo 8: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (प्रथम पेज) (Mandatory: हाँ)\n  * Supporting Document 1: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (प्रथम पेज)\n- SNo 9: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (व्दितीय पेज) (Mandatory: हाँ)\n  * Supporting Document 1: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (व्दितीय पेज)\n- SNo 10: चालान की प्रति (Mandatory: हाँ)\n  * Supporting Document 1: चालान की प्रति\n- SNo 11: विवाह आमंत्रण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: विवाह आमंत्रण पत्र\n- SNo 12: तलाक प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: तलाक प्रमाण पत्र\n- SNo 13: विधवा प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: विधवा प्रमाण पत्र\n- SNo 14: अंतरधार्मिक विवाह प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: अंतरधार्मिक विवाह प्रमाण पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: वैवाहिक जानकारी [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: विवाह की तिथि [Type: date, Data: Date] (Row: 2, Col: 1)\n- Field: विवाह का स्थान [Type: textarea, Data: Alfa Numeric] (Row: 2, Col: 2)\n- Field: विवाह का प्रकार [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: क्या विवाह पंजीकृत है [Type: drop down, Data: Charactar] (Row: 3, Col: 2)\n- Field: पंजीयन क्रमांक [Type: text,\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: वधु का पता [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: वधु का वर्तमान पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: वधु का वर्तमान पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: वधु का स्थायी पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 1)\n- Field: वधु की स्थायी पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 2)\n- Field: वधु पक्ष के गवाह का विवरण [Type: fieldset, Data: Alfa Numeric] (Row: 22, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 3_hi_3.pdf (INSTRUCTION)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nवििाह पंजीकरण एिं प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nपर ऑनलाइन आिेदन\n\n--- Page 2 ---\nविषय सूची \nई-डिस्ट्रिक्ट: होम पेज ................................ ................................ ................................ ................................ ................................ .................. 2 \nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण ................................ ................................ ................................ ................................ ............... 3 \nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन ................................ ................................ ................................ ................................ .................... 4 \nचरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ .................. 5 \nचरण 4: आिेदक की बुडनयादी जानकारी ................................ ................................ ................................ ................................ ............... 6 \nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन ................................ ................................ ................................ ....................... 7 \nचरण 6: आिश्यक दस्तािेज़ अपलोि करना ................................ ................................ ................................ ................................ .......... 8 \nचरण 7: पूिाािलोकन और आिेदन जमा करना ................................ ................................ ................................ ................................ ...... 9 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 10 \nचरण 9: पािर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ................................  11\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉगगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉगगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: Data: Charactar] (Row: 1, Col: 1)\n- Field: विवाह की तिथि [Type: date, Data: Date] (Row: 2, Col: 1)\n- Field: विवाह का स्थान [Type: textarea, Data: Alfa Numeric] (Row: 2, Col: 2)\n- Field: विवाह का प्रकार [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: क्या विवाह पंजीकृत है [Type: drop down, Data: Charactar] (Row: 3, Col: 2)\n- Field: पंजीयन क्रमांक [Type: text, Data: Number] (Row: 4, Col: 1)\n- Field: अन्य जानकारी [Type: textarea, Data: Charactar] (Row: 4, Col: 2)\n- Field: वर का विवरण [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: वर का नाम स्थानीय भाषा में [Type: text, Data: Charactar] (Row: 6, Col: 1)\n- Field: वर का नाम अंग्रेजी में [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: वर का जन्म तिथि [Type: date, Data: Date] (Row: 7, Col: 1)\n- Field: विवाह के समय उम्र [Type: text, Data: Number] (Row: 7, Col: 2)\n- Field: पिता का नाम स्थानीय भाषा में [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: पिता का नाम अंग्रेजी में [Type: textarea, Data: Charactar] (Row: 8, Col: 2)\n- Field: वर की वैवाहिक स्थिति [Type: drop down, Data: Charactar] (Row: 9, Col: 1)\n- Field: वर का पता [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: वर का वर्तमान पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: वर का वर्तमान पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 2)\n- Field: वर का स्थाई पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: वर का स्थाई पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 2)\n- Field: वर पक्ष के गवाह का विवरण [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: वधु का विवरण [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: वधु का नाम स्थानीय भाषा में [Type: text, Data: Charactar] (Row: 15, Col: 1)\n- Field: वधु का नाम अंग्रेजी में [Type: text, Data: Charactar] (Row: 15, Col: 2)\n- Field: वधु की जन्म तिथि [Type: date, Data: Date] (Row: 16, Col: 1)\n- Field: विवाह के समय वधु की उम्र [Type: text, Data: Number] (Row: 16, Col: 2)\n- Field: वधु के पिता का नाम स्थानीय भाषा में [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: वधु के पिता का नाम अंग्रेजी में [Type: text, Data: Charactar] (Row: 17, Col: 2)\n- Field: वधु की वैवाहिक स्थिति [Type: drop down, Data: Charactar] (Row: 18, Col: 1)\n- Field: वधु का पता [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: वधु का वर्तमान पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: वधु का वर्तमान पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: वधु का स्थायी पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 21,\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: �्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉगगन प्रगक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासििा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \nचरण 3.2: खोजें पर क्लिक करें। सेवाओं की सूची खुलेगी। \n \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.3: सेवाओं की सूची में प्रिजशित वििाह प्रमाण पत्र (Marriage Certificate) पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। इस पेज पर आवश्यक िस्तावेज़़ों की सूची भी िेखी जा सकती है। \n \n \nचचत्र क्रमांक 7: सेिा पररचय एिं सहायक दस्तािेज़़ों की सूची \n \nचरण 3.4: “आगे” बटन पर क्लिक करें।\n\n--- Page 7 ---\nचरण 4: आिेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की जांच सूच\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "जाति प्रमाण पत्र धारकों के लिए गांव में विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र धारकों के लिए विवाह रजिस्ट्रार स्थानीय क्षेत्र प्राधिकरण
       ```
| 35 | `क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?` | 201 | 201 | ✅ MATCH | new_topic | 4.95s |

### Query 35 Details
* **Query**: `क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is it mandatory to submit a marriage invitation card for name change in the gazette?`
* **Resolved Hindi Query**: `क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, विवाह निमंत्रण पत्र राजपत्र में नाम परिवर्तन के लिए अनिवार्य नहीं है। नाम परिवर्तन के लिए आवश्यक दस्तावेज निम्नलिखित हैं:
  > 
  > 1. 430 रुपये का भारतीय स्टेट बैंक का चालान
  > 2. 50 रुपये के नॉन ज्यूडिशियल स्टाम्प पेपर पर नोटराइज्ड शपथ पत्र
  > 3. स्थानीय समाचार पत्र में नाम परिवर्तन की सूचना का प्रकाशन
  > 4. दो गवाहों के हस्ताक्षर और पते के साथ मूल प्ररूप-दो
  > 5. पुराना नाम और नया नाम सत्यापन दस्तावेज़
  > 6. शपथ पत्र में उल्लिखित सभी प्रकार के पहचान पत्र
  > 
  > इनमें से कोई भी एक दस्तावेज अनिवार्य है, लेकिन विवाह निमंत्रण पत्र इनमें शामिल नहीं है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?"
       ```
     * **Response**:
       ```json
       क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?"
       ```
     * **Response**:
       ```json
       Is it mandatory to submit a marriage invitation card for name change in the gazette?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the requirement for submitting a marriage invitation letter in the Rajpatra for name change?', 'topic_summary': 'User is asking about the requirement for a marriage invitation letter in the Rajpatra for name change, which is a different service than the previous query about name change process.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या राजपत्र में नाम परिवर्तन के लिए विवाह निमंत्रण पत्र जमा करना अनिवार्य है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, विवाह निमंत्रण पत्र राजपत्र में नाम परिवर्तन के लिए अनिवार्य नहीं है। नाम परिवर्तन के लिए आवश्यक दस्तावेज निम्नलिखित हैं:
       
       1. 430 रुपये का भारतीय स्टेट बैंक का चालान
       2. 50 रुपये के नॉन ज्यूडिशियल स्टाम्प पेपर पर नोटराइज्ड शपथ पत्र
       3. स्थानीय समाचार पत्र में नाम परिवर्तन की सूचना का प्रकाशन
       4. दो गवाहों के हस्ताक्षर और पते के साथ मूल प्ररूप-दो
       5. पुराना नाम और नया नाम सत्यापन दस्तावेज़
       6. शपथ पत्र में उल्लिखित सभी प्रकार के पहचान पत्र
       
       इनमें से कोई भी एक दस्तावेज अनिवार्य है, लेकिन विवाह निमंत्रण पत्र इनमें शामिल नहीं है।
       ```
| 36 | `ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क` | 5 | 5 | ✅ MATCH | new_topic | 4.37s |

### Query 36 Details
* **Query**: `ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क`
* **Expected Service ID**: `5`
* **Classified Service ID**: `5`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Online payment of OBC certificate fee in Chhattisgarh State vs. SC ST certificate online fee`
* **Resolved Hindi Query**: `ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > छत्तीसगढ़ में ओबीसी प्रमाण पत्र और एससी/एसटी प्रमाण पत्र ऑनलाइन शुल्क का विवरण:
  > 
  > **ओबीसी प्रमाण पत्र ऑनलाइन शुल्क:**
  > - आवेदन शुल्क: ₹30.0
  > - शुल्क भुगतान के लिए ऑनलाइन और कियोस्क, दोनों विकल्प उपलब्ध हैं
  > 
  > **एससी/एसटी प्रमाण पत्र ऑनलाइन शुल्क:**
  > - ऑनलाइन शुल्क: ₹30.0
  > - कियोस्क शुल्क: ₹30.0
  > 
  > **कुल शुल्क:**
  > - दोनों प्रमाण पत्रों के लिए कुल शुल्क ₹30.0 ही है
  > - यह शुल्क ऑनलाइन या कियोस्क, किसी भी माध्यम से भुगतान किया जा सकता है
  > 
  > शुल्क भुगतान की प्रक्रिया के लिए सेवा सेतु केंद्र या ई-डिस्ट्रिक्ट पोर्टल का उपयोग किया जा सकता है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क"
       ```
     * **Response**:
       ```json
       ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क"
       ```
     * **Response**:
       ```json
       Online payment of OBC certificate fee in Chhattisgarh State vs. SC ST certificate online fee
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the fee for OBC certificate payment online in Chhattisgarh state?', 'topic_summary': 'User is asking about the fee for OBC certificate payment online in Chhattisgarh state.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '3', 'service_id': '5'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- OBC RESIDENCY/DOMICILE RULE: If the citizen asks about Domicile or Residence rules/requirements for the OBC Certificate, explain clearly based on the context:\n  1. A Domicile Certificate (मूल निवासी प्रमाण पत्र) is NOT mandatory (it is listed as one of several optional supporting documents under 'Residential Proof').\n  2. To satisfy the residency requirement for the OBC Certificate, the applicant or their ancestors must have been residing in the geographical limits of Chhattisgarh since or before the OBC notification date, which is December 26, 1984 (२६ दिसम्बर १९८४).\n  3. List the alternative supporting documents for Residential Proof (such as Land/House documents, Ration Card, Electricity Bill, Ward Member/MLA/MP certificate, Birth Certificate).\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: OBC Certificate\nService ID: 5\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 2: Land And House Document\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Electricity Bill\n  * Supporting Document 5: Domicile Certificate\n  * Supporting Document 6: Birth Certificate\n  * Supporting Document 7: Birth Information Form\n  * Supporting Document 8: Service Certificate / Identity Card Of Father / Guardian\n  * Supporting Document 9: Order Of Involuntary Migration\n- SNo 2: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 3: Income Proof (Mandatory: Yes)\n  * Supporting Document 1: Certificate From Patwari/Sarpanch/Parshad\n  * Supporting Document 2: Income Certificate Employer/Form 16\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Income From Land/House\n  * Supporting Document 5: Other Documents\n  * Supporting Document 6: Application Form\n- SNo 4: Obc Proof (Mandatory: Yes)\n  * Supporting Document 1: Educational Certificate\n  * Supporting Document 2: Transfer Certificate Of Primary School Education\n  * Supporting Document 3: Obc Certificate Of Father\n  * Supporting Document 4: Obc Certificate From Sarpanch / Parshad\n  * Supporting Document 5: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 6: Misal\n  * Supporting Document 7: Adhikar Abhilekh\n  * Supporting Document 8: Jamabandi\n  * Supporting Document 9: Census Register Of 1931\n  * Supporting Document 10: Citizen Register Of 1949\n  * Supporting Document 11: Dakhil / Kharij Panji\n  * Supporting Document 12: Disability / Unavailability Proof\n- SNo 5: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 6: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 7: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste OBC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (\n\n--- Source 2: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ीं है।\n\n--- Page 14 ---\nचरण 9: पावर्ी सुरक्षिर् रखना \nआवेिन सफलतापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक िेखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट लेकर सुरलित रखें। \n \nचचत्र क्रमांक 20: पावर्ी एवं आवेदन संदभा क्रमांक \nआवेदन संदभा क्रमांक की सहायता से आवेिन की स्थस्थगत छत्तीसगढ़ ई-निस्ट्रिक्ट क े  पोटटल पर िेखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेिन जमा करने क े  बाि ननर्ाटररत 22 क्रिऩों की समय-सीमा क े  अ ं िर आवेिन का ननराकरण कर क्रिया जाता है। \n• ई-निस्ट्रिक्ट पोटटल पर आवेिन की स्थस्थगत िेखी जा सकती है। \n• अन्य क्रपछडा वगट प्रमाण पत्र जारी होने क े  उपरांत इसकी निजजटल प्रगत ई-निस्ट्रिक्ट पोटटल से िाउनलोि की जा सकती है।\n\n--- [Document: 5_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of\n\n--- Source 3: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �स्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 4: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉपगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉपगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: नवीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉपगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉपगन प्रपक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासविा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉपगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.2: खोजें पर क्लिक करें। \nचरण 3.3: सेवाओं की सूची खुलेगी। इसमें अन्य पपछडा वगा प्रमाण पत्र िेखें।  \nचरण 3.4: यक्रि यह सेवा सूची में शागमल नहीं है तो ऊपर क्रिए गए होम बटन पर क्लिक करें। ननम्नानुसार पेज \nखुलेगा। \n \nचचत्र क्रमांक 7: उपयोगकर्ाा होम पेज \nचरण 3.5: इस पेज पर “सभी सेवाए ँ  देखें” पर क्लिक करें। सेवाओं की\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अन्य पिछड़ा वर्ग प्रमाण पत्र\nService ID: 5\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 2: घर या भूमि का दस्तावेज़\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: बिजली का बिल\n  * Supporting Document 5: मूल निवासी प्रमाण पत्र\n  * Supporting Document 6: जन्म प्रमाण पत्र\n  * Supporting Document 7: जन्म सूचना प्रपत्र\n  * Supporting Document 8: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 9: अनैच्छिक प्रवजन का आदेश\n- SNo 2: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 3: आय प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: पटवारी/सरपंच/पार्षद से प्रमाण पत्र\n  * Supporting Document 2: नियोक्ता का आय प्रमाण पत्र/फार्म १६\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: भूमि/घर से आय\n  * Supporting Document 5: अन्य\n  * Supporting Document 6: आवेदन प्रपत्र\n- SNo 4: अन्य पिछड़ा वर्ग का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: शैक्षणिक प्रमाण - पत्र\n  * Supporting Document 2: प्राथमिक स्कूल शिक्षा के प्रमाण पत्र के लिए स्थानांतरण\n  * Supporting Document 3: पिता का अ.पि.व. प्रमाण पत्र\n  * Supporting Document 4: सरपंच / पार्षद से ओबीसी प्रमाणपत्र\n  * Supporting Document 5: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 6: मिसल\n  * Supporting Document 7: अधिकार अभिलेख\n  * Supporting Document 8: जमाबंदी\n  * Supporting Document 9: १९३१ का जनगणना पंजी\n  * Supporting Document 10: 1949 का नागरिक पंजी\n  * Supporting Document 11: दाखिल / ख़ारिज पंजी\n  * Supporting Document 12: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 5: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 6: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document 1: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए)\n- SNo 7: मध्यप्रदेश पुनर्गठन अधिनियम 2000(क्रमांक २६-सन २००० की धारा ६७ के अधीन छ. ग. राज्य संवर्ग आबंटन ) का प्रम\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: र्ाटररत शुल्क का भुगतान करें। \nचरण 7.2: “जमा करें” पर क्लिक करते ही आवेिन जमा हो जाएगा। \n \nनोट: \n• लोकसेवा क ें द्र/ सीएससी/नकयोस्क क े  ललए सेवा शुल्क रु. 30 ननर्ाटररत हैं। \n• पााँच िस्तावेज़़ों तक स्क ै ननिंग ननिःशुल्क है। \n• इसक े  अगतररक्त और कोई शुल्क िेय नहीं है।\n\n--- Page 14 ---\nचरण 9: पावर्ी सुरक्षिर् रखना \nआवेिन सफलतापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक िेखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट लेकर सुरलित रखें। \n \nचचत्र क्रमांक 20: पावर्ी एवं आवेदन संदभा क्रमांक \nआवेदन संदभा क्रमांक की सहायता से आवेिन की स्थस्थगत छत्तीसगढ़ ई-निस्ट्रिक्ट क े  पोटटल पर िेखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेिन जमा करने क े  बाि ननर्ाटररत 22 क्रिऩों की समय-सीमा क े  अ ं िर आवेिन का ननराकरण कर क्रिया जाता है। \n• ई-निस्ट्रिक्ट पोटटल पर आवेिन की स्थस्थगत िेखी जा सकती है। \n• अन्य क्रपछडा वगट प्रमाण पत्र जारी होने क े  उपरांत इसकी निजजटल प्रगत ई-निस्ट्रिक्ट पोटटल से िाउनलोि की जा सकती है।\n\n--- [Document: 5_hi_citizenCharter.pdf (SLA_DETAILS)] ---\nछत्तीसगढ़ शासन\nराजस्व एवं आपदा प्रबंधन विभाग\nमंत्रालय\nमहानदी भवन नया रायपुर\n::: अधिसूचना :::\n\nरायपुर, दिनांक 16/05/2013\n\nक्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\nसारणी (SLA Details):\n1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: --- Page 1 (no rotation needed) ---\nबिजनेस पोस्ट के अन्तर्गत डाक शुल्क के नगद भुगता (बिना डाक टिकट ) के प्रेषण हेतु नुमत. क्रमांक जी. २२२२ छत्तीसगढ जिय ३८ सि॰ से. भिलाई , दिनांक ३०~६ 2001.`\nपंजोयन क्रमांक\nक :1\" 'छत्तीसगढ दुर्ग/09/2012~2015.' ?[<\nछत्तीसगढ़ राजपत्र असाधारण ) प्राधिकार से प्रकाशित\nक्रमांक ३१४ ]\nरायपुर सोमवार , दिनांक 2 सितम्बर २०१३ - भाद्र ११ शक १९३५\nसामान्य प्रशासन विभाग\nमंत्रालय, महानदी भवन, नया रायपुर\nनया रायपुर दिनांक 2 सितम्बर, २०१३\nअधिसूचना\nरमाऊ -फ 13+23/2012/अ. प्र. /१-३. छत्तीसगढ अनुसूचित जाति अनुसूचित जनजाति ओर अन्य पिछड़ा वगं सामाजिक प्रास्थिति क प्रमाणीकरण का विनियमन) अधिनियम॰ २०१३ क्रभांक १३ सन् 2013) की धारा १९ द्वा [ प्रदत्त शक्तियों को प्रयोग में लाते हु९॰ राज्य सरकार एतदद्वारा निग्नलिखित्त नियम बनाती है॰ अर्थात् नियम\nअध्याय -रक\nप्रारंभिक\n4\nरक्षिप्त नफ नथ प्रारंभ १ ये नियम छत्तीसगढ़ अनुसूचित जाति,. अनुसूचित जनजाति और अन्य पिछड़ा वर्ग सामाजिक प्रास्थिति के प्रमाणीकरण का विनियमनः नियम. २०१३ कहलाएंगे।\n(२\nनियम राजपत्र मं इनक प्रकाशन की ताशेख से प्रवृत्त होंगे।\n787\n\n--- Page 2 (no rotation needed) ---\n788:6`\nछत्तीरगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\n2. *].` परिभाषाएं. - क़) इन नियमों में जब तक कि संदर्भ से अन्यथा अपेक्षित न हो - क 'अधिनियम से अभिप्रेत हे छत्तीसगढ़ अनुसूचित जाति, अनुसूचित जनजाति और अन्य पिछड़ा वर्ग सामाजिक प्रास्थिति क प्रमाणीकरण क विनिथभन) अधिनियम, २०१३ कमांक १३ सन् २०१३ ; ख \"आवदक ' से अभिप्रेत है॰ विहित रीति में प्रमाणपत्र सत्यागन प्रमाणपत्र क लिए आवेदन करने वाला व्यक्ति ऐसा व्यक्ति जिसका प्रमाणपत्र जिला स्तरीय प्रमाणपत्र सत्याप्न समिति द्वार विनिश्चित अनुसार सत्यापित किया जानां हा या\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ित कोई सीट अथवा अनुसूचित जाति्योँ, अनुसूचित जनजातियों या अन्य पिछड़े वर्गों यथास्थिति, से संबंधित व्यक्तियों के लिए किसी संवैधानिक निकाय चाहे वह निर्वाचन की प्रक्रिया के द्वारा, नामांकन के द्वारा या अन्यथा भरा जाये, में आरक्षित कोई सोट;\n* अनुसूचित जाति ' से अभिप्रेत है भारत के संविधान के अनुच्छेद ३४१ के अधीन छत्तीसगढ़ राज्य के संबंध में यथा विनिर्दिष्ट अनुसूचित ज़ातिः\n(ढ )\n\" अनुसूचित जनजाति * से अभिप्रेत है भारत के संविधान के अनुच्छेद ३४२ के अधीन छत्तीसगढ़ राज्य के संबंध में यथा विनिर्दिष्ट अनुसूचित जनजाति;\n( ण)\n*सामाजिक प्रास्थिति प्रमाणपत्र से अभिप्रेत है सक्षम प्राधिकारी द्वारा आवेदक को जारी ऐसा प्रमाणपत्र जिससे यह दर्शित होःकि ऐंसा आवेदक अनुसूचित जाति या अनुसूचित जनजाति या॰ अन्य पिछड़ा वर्ग, यथास्थिति, से संबंधित है;\n(त\nराज्य ` से अभिप्रेत है छत्तीसगढ़ राज्य.\nअध्याय-्दो\nसामाजिकं प्रास्यिति प्रमाणपत्र का जारी किया जाना\nअनुसूचित जाति या अनुसूचित जनजाति या अन्य पिछड़े वर्ग का कोई भी॰व्यक्ति सामाजिक प्रास्थिति सामाजिक प्रास्थिति प्रमाणपत्र जारी करने के लिये सक्षम प्राधिकारी को ऐसे प्ररूप तथा ऐसी रीति में आवेदन करेगा, जैसा कि प्रमाणपत्र जारी करने के लिए आवेदन. विहित किया जाये\n\n--- Page 7 (rotated 270deg) ---\n344 (4)\nछत्तीसगढ़ राजपत्र, दिनांक २१ अप्रैल २०१३\nसामाजिक प्रास्थिति प्रमाणपत्र जारी करने के लिये प्रकिया.\n4.\n(1)\nसक्षम प्राधिकारी , धारा 3 के अधीन आवेदन के प्राप्त होने पर, ऐसी जांच करने के पश्चात्, जैसी विहित की जाए॰ सामाजिक प्रास्थिति प्रमाणपत्र जारी करेगा\nपरंतु जहां सक्षम प्राधिकारी का निष्कर्ष हो कि ऐसे प्रमाणपत्र के लिए आवेदन के निरस्त किये जाने का पर्याप्त कारण है॰ तो निरस्त करने के कारणों को लिखित में अभिलिखित करेगा तथा तदन\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "ओबीसी प्रमाण पत्र शुल्क भुगतान ऑनलाइन छत्तीसगढ़ राज्य बनाम एससी एसटी प्रमाण पत्र ऑनलाइन शुल्क\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       छत्तीसगढ़ में ओबीसी प्रमाण पत्र और एससी/एसटी प्रमाण पत्र ऑनलाइन शुल्क का विवरण:
       
       **ओबीसी प्रमाण पत्र ऑनलाइन शुल्क:**
       - आवेदन शुल्क: ₹30.0
       - शुल्क भुगतान के लिए ऑनलाइन और कियोस्क, दोनों विकल्प उपलब्ध हैं
       
       **एससी/एसटी प्रमाण पत्र ऑनलाइन शुल्क:**
       - ऑनलाइन शुल्क: ₹30.0
       - कियोस्क शुल्क: ₹30.0
       
       **कुल शुल्क:**
       - दोनों प्रमाण पत्रों के लिए कुल शुल्क ₹30.0 ही है
       - यह शुल्क ऑनलाइन या कियोस्क, किसी भी माध्यम से भुगतान किया जा सकता है
       
       शुल्क भुगतान की प्रक्रिया के लिए सेवा सेतु केंद्र या ई-डिस्ट्रिक्ट पोर्टल का उपयोग किया जा सकता है।
       ```
| 37 | `केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए निवास प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड` | 7 | 7 | ✅ MATCH | new_topic | 2.38s |

### Query 37 Details
* **Query**: `केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए निवास प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए मूल निवासी प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए मूल निवासी प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड"
       ```
     * **Response**:
       ```json
       केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए मूल निवासी प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए मूल निवासी प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड"
       ```
     * **Response**:
       ```json
       The original domicile certificate eligibility criteria for central government employees versus Chhattisgarh state ST employees
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए मूल निवासी प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What are the eligibility criteria for a domicile certificate for central government employees versus Chhattisgarh state ST employees?', 'topic_summary': 'Eligibility criteria for domicile certificate for two different employee categories.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "केंद्र सरकार के कर्मचारियों बनाम छत्तीसगढ़ राज्य एसटी कर्मचारियों के लिए मूल निवासी प्रमाण पत्र छत्तीसगढ़ पात्रता मानदंड",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
| 38 | `राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह प्रमाण पत्र की समय सीमा` | 201 | 201 | ✅ MATCH | new_topic | 3.38s |

### Query 38 Details
* **Query**: `राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह प्रमाण पत्र की समय सीमा`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `The deadline for publishing name change in the Gazette versus the deadline for marriage registration and certificate.`
* **Resolved Hindi Query**: `राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > राजपत्र में नाम परिवर्तन के प्रकाशन की समय सीमा 29 दिन है। विवाह पंजीकरण और प्रमाण पत्र की समय सीमा अलग-अलग होती है, जो संबंधित विभाग और प्रक्रिया पर निर्भर करती है। प्रत्येक सेवा की अपनी विशिष्ट समय सीमा और प्रक्रिया होती है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा"
       ```
     * **Response**:
       ```json
       राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा"
       ```
     * **Response**:
       ```json
       The deadline for publishing name change in the Gazette versus the deadline for marriage registration and certificate.
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the timeline for marriage registration and its certificate?', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "राजपत्र में नाम परिवर्तन प्रकाशन की समय सीमा बनाम विवाह पंजीकरण एवं प्रमाण पत्र की समय सीमा\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       राजपत्र में नाम परिवर्तन के प्रकाशन की समय सीमा 29 दिन है। विवाह पंजीकरण और प्रमाण पत्र की समय सीमा अलग-अलग होती है, जो संबंधित विभाग और प्रक्रिया पर निर्भर करती है। प्रत्येक सेवा की अपनी विशिष्ट समय सीमा और प्रक्रिया होती है।
       ```
| 39 | `ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता` | 4 | 5 | ❌ MISMATCH | new_topic | 4.19s |

### Query 39 Details
* **Query**: `ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता`
* **Expected Service ID**: `4`
* **Classified Service ID**: `5`
* **Match Status**: ❌ MISMATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `What is the offline tehsil office address for OBC residence certificate?`
* **Resolved Hindi Query**: `ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > सेवा केंद्र: अन्य पिछड़ा वर्ग (ओबीसी) प्रमाण पत्र हेतु निवास प्रमाण हेतु ऑफलाइन तहसील कार्यालय का पता।
  > 
  > तहसील कार्यालय: राजस्व और आपदा प्रबंधन विभाग, तहसील कार्यालय, जिला - [जिला का नाम], छत्तीसगढ़।
  > 
  > सेवा केंद्र: सेवा सेतु केंद्र, [तहसील का नाम]।
  > 
  > निवास प्रमाण हेतु ऑफलाइन आवेदन करने के लिए आवेदक को संबंधित तहसील कार्यालय या सेवा सेतु केंद्र जाना होगा।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता"
       ```
     * **Response**:
       ```json
       ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता"
       ```
     * **Response**:
       ```json
       What is the offline tehsil office address for OBC residence certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the address of the offline tehsil office for OBC residence certificate?', 'topic_summary': 'Query about the address of the offline tehsil office for OBC residence certificate.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '3', 'service_id': '5'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- OBC RESIDENCY/DOMICILE RULE: If the citizen asks about Domicile or Residence rules/requirements for the OBC Certificate, explain clearly based on the context:\n  1. A Domicile Certificate (मूल निवासी प्रमाण पत्र) is NOT mandatory (it is listed as one of several optional supporting documents under 'Residential Proof').\n  2. To satisfy the residency requirement for the OBC Certificate, the applicant or their ancestors must have been residing in the geographical limits of Chhattisgarh since or before the OBC notification date, which is December 26, 1984 (२६ दिसम्बर १९८४).\n  3. List the alternative supporting documents for Residential Proof (such as Land/House documents, Ration Card, Electricity Bill, Ward Member/MLA/MP certificate, Birth Certificate).\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: OBC Certificate\nService ID: 5\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 2: Land And House Document\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Electricity Bill\n  * Supporting Document 5: Domicile Certificate\n  * Supporting Document 6: Birth Certificate\n  * Supporting Document 7: Birth Information Form\n  * Supporting Document 8: Service Certificate / Identity Card Of Father / Guardian\n  * Supporting Document 9: Order Of Involuntary Migration\n- SNo 2: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 3: Income Proof (Mandatory: Yes)\n  * Supporting Document 1: Certificate From Patwari/Sarpanch/Parshad\n  * Supporting Document 2: Income Certificate Employer/Form 16\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Income From Land/House\n  * Supporting Document 5: Other Documents\n  * Supporting Document 6: Application Form\n- SNo 4: Obc Proof (Mandatory: Yes)\n  * Supporting Document 1: Educational Certificate\n  * Supporting Document 2: Transfer Certificate Of Primary School Education\n  * Supporting Document 3: Obc Certificate Of Father\n  * Supporting Document 4: Obc Certificate From Sarpanch / Parshad\n  * Supporting Document 5: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 6: Misal\n  * Supporting Document 7: Adhikar Abhilekh\n  * Supporting Document 8: Jamabandi\n  * Supporting Document 9: Census Register Of 1931\n  * Supporting Document 10: Citizen Register Of 1949\n  * Supporting Document 11: Dakhil / Kharij Panji\n  * Supporting Document 12: Disability / Unavailability Proof\n- SNo 5: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 6: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 7: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste OBC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (\n\n--- Source 2: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ीं है।\n\n--- Page 14 ---\nचरण 9: पावर्ी सुरक्षिर् रखना \nआवेिन सफलतापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक िेखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट लेकर सुरलित रखें। \n \nचचत्र क्रमांक 20: पावर्ी एवं आवेदन संदभा क्रमांक \nआवेदन संदभा क्रमांक की सहायता से आवेिन की स्थस्थगत छत्तीसगढ़ ई-निस्ट्रिक्ट क े  पोटटल पर िेखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेिन जमा करने क े  बाि ननर्ाटररत 22 क्रिऩों की समय-सीमा क े  अ ं िर आवेिन का ननराकरण कर क्रिया जाता है। \n• ई-निस्ट्रिक्ट पोटटल पर आवेिन की स्थस्थगत िेखी जा सकती है। \n• अन्य क्रपछडा वगट प्रमाण पत्र जारी होने क े  उपरांत इसकी निजजटल प्रगत ई-निस्ट्रिक्ट पोटटल से िाउनलोि की जा सकती है।\n\n--- [Document: 5_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of\n\n--- Source 3: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �स्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 4: [Official Specification (English)] ---\nService: OBC Certificate (ID: 5)\nSection: combined_manual\nContent:\nService: OBC Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 15, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 15, Col: 2)\n- Field: Police Station [Type: search, Data: Search] (Row: 16, Col: 1)\n- Field: Address Before or on Date 26/12/1984 [Type: section lebel, Data: Charactar] (Row: 17, Col: 1)\n- Field: Village or Town [Type: text, Data: Charactar] (Row: 18, Col: 1)\n- Field: Patwari Halka Number [Type: text, Data: Number] (Row: 18, Col: 2)\n- Field: Tehsil [Type: text, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: Data List, Data: Charactar] (Row: 19, Col: 2)\n- Field: Name of Head Of Family on This Date [Type: text, Data: Charactar] (Row: 20, Col: 1)\n- Field: Applicant Relation to Head of Family [Type: drop down, Data: Charactar] (Row: 20, Col: 2)\n- Field: Address Details of Applicant/his Father / Mother/ Guardian from Year 26/12/1984 to till Date [Type: section lebel, Data: Alfa Numeric] (Row: 21, Col: 1)\n- Field: Address Details of Applicants Guardian [Type: fieldset, Data: Alfa Numeric] (Row: 22, Col: 1)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 22, Col: 2)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 5_en_5.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nअन्य पपछडा वगा प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर \nऑनलाइन आवेदन\n\n--- Page 2 ---\nविषय सूची \nई-डिस्ट्रिक्ट: होम पेज ................................ ................................ ................................ ................................ ................................ .................. 2 \nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण ................................ ................................ ................................ ................................ ............... 3 \nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉपगन ................................ ................................ ................................ ................................ .................... 4 \nचरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ .................. 5 \nचरण 4: आवेदक की बुडनयादी जानकारी ................................ ................................ ................................ ................................ ............... 8 \nचरण 5: अन्य पपछडा वगा प्रमाण पत्र के र्लए आवेदन ................................ ................................ ................................ ......................... 9 \nचरण 6: आवश्यक दस्तावेज़ अपलोि करना ................................ ................................ ................................ ................................ ........ 10 \nचरण 7: पूवाावलोकन और आवेदन जमा करना ................................ ................................ ................................ ................................ ..... 11 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 12 \nचरण 9: पावर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ...............................  13\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉपगन बटन पर क्लिक करें\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: combined_manual\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अन्य पिछड़ा वर्ग प्रमाण पत्र\nService ID: 5\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 2: घर या भूमि का दस्तावेज़\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: बिजली का बिल\n  * Supporting Document 5: मूल निवासी प्रमाण पत्र\n  * Supporting Document 6: जन्म प्रमाण पत्र\n  * Supporting Document 7: जन्म सूचना प्रपत्र\n  * Supporting Document 8: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 9: अनैच्छिक प्रवजन का आदेश\n- SNo 2: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 3: आय प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: पटवारी/सरपंच/पार्षद से प्रमाण पत्र\n  * Supporting Document 2: नियोक्ता का आय प्रमाण पत्र/फार्म १६\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: भूमि/घर से आय\n  * Supporting Document 5: अन्य\n  * Supporting Document 6: आवेदन प्रपत्र\n- SNo 4: अन्य पिछड़ा वर्ग का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: शैक्षणिक प्रमाण - पत्र\n  * Supporting Document 2: प्राथमिक स्कूल शिक्षा के प्रमाण पत्र के लिए स्थानांतरण\n  * Supporting Document 3: पिता का अ.पि.व. प्रमाण पत्र\n  * Supporting Document 4: सरपंच / पार्षद से ओबीसी प्रमाणपत्र\n  * Supporting Document 5: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 6: मिसल\n  * Supporting Document 7: अधिकार अभिलेख\n  * Supporting Document 8: जमाबंदी\n  * Supporting Document 9: १९३१ का जनगणना पंजी\n  * Supporting Document 10: 1949 का नागरिक पंजी\n  * Supporting Document 11: दाखिल / ख़ारिज पंजी\n  * Supporting Document 12: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 5: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 6: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document 1: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए)\n- SNo 7: मध्यप्रदेश पुनर्गठन अधिनियम 2000(क्रमांक २६-सन २००० की धारा ६७ के अधीन छ. ग. राज्य संवर्ग आबंटन ) का प्रम\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: �ेदक की जन्म तिथि 6 जाति (केवल अनुसूचित जाति आवेदक के .- 7 वर्तमान पूरा पता मोहल्ला / वार्ड ग्राम / करचा / शहर विखं तहसीलं जिला राज्य स्थाईं पता मोहल्ला / वार्ड\nग्राम / करचा / शहर वि.खं तहसीलं जिला रज्य मोहल्ला / वार्ड ग्राम / कस्बा / शहर\n$\nआवेदक की जन्म तिथि क यदि अनु॰ जाति के लिए 10 /08 /1950 तथा अनु. जन जाति क लिए ०६ / ०९ / १९५० के॰पूर्व की हैः ख यददि अन्य पिछडा वर्ग क लिए २६ / १२ / १९८४ के पूर्व की हैः तों अवेदक क जन्म स्थान अथवा यदि इस तिथि क बाद हे तो . उसके पिता / पूर्वज क निवास स्थान का स्थाई पता\nचि.खं\nतहसीलं\nजिला\nराज्यं\n\n--- Page 14 (no rotation needed) ---\n788 < १२ )\nछत्तीसगढ़ रजपत्र, दिनांक 2 सितम्बर २०१३\n10 उल्लिखित तिथि को उपर्युक्त पते पर निवास करने वाले परिवार का मुखिया\nआवदक क साथ संबंध\n11\nआवेदक / उसके - पिता / पूर्वज 10 /08 / 1950 अनु. जाति क सदर्भ में ०६ / ०९ / १९५० अनु. जन जांति के संदर्भ में॰ एवं २६ / १२ / १९८४ अन्य पिछड़ा वर्ग क संदर्भ में से वर्तमान तिथि तक किन-्किन स्थानों पर रहा / रहे है उसका विवरण ^2 आवेदक की जाति / जनजाति. उपजाति सहित ^3 क्या मध्यप्रदेश पुनर्गठन अधिनियम, २००० क अंतर्गत पिछड़ा वर्ग क लिए यथा संशोधित अधिसूचना दिनांक 26 / 1२ /1384 क द्वारा वह राज्य / जिले के लिए विहित निर्धारित) हैं? यदि हॉ तो उराका सरल कमांक १4 निम्नांकित अभिलेख की अभिप्रमाणित प्रति संलग्न कर 1 ) आवेदक क पिता / पूर्वजां को निभ्नायित्त अभिलेख जिसमें उनकी जाति उल्लिखित् अंकित हाो -- क पूर्वजों के रांजस्व दस्तावेज (मिसल ; ख जभाबंदी सर्वे} या गिरदावरी बी 1; .ग) राज्य बंदोबरअधव घ॰ अधिवःार अभिलेख १९५४ ; अथवा (ड. ) वन विभाग कीं जमाबंद सर्वे / वन अधिकारपत्र, अथवा च शैक्षणिक रांरथा के दाखि़ल खारिज पंजीः अथता (छ जन्भ\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: �ीसगढ़ राजपत्र दिनांक 2 सितम्बर २०१३\nस फ\nनिवास स्थान\nमोहल्ला / ग्राम / तहसाल वार्ड कमांक कस्बा / शहर\nजिला निवास करने की एवं ततिथि राज्य अथवा वर्ष\nआवदक का वर्तमान निवास स्थान 2 अवदक का घत्त्तापगढ़ राज्य नंनिवास स्थान यदि अवदक को जन्म तिथि 10 /08 /1950 अनु. जाति / 06 /09 / 1950 अनु. जन जातिं / 26 /12 /1984 ३० पि॰ व॰ कोया उससे पूर्व की है॰ तो ऐसी तिथि पर आवेदक का स्थायी निवास स्थान यदे अवदक को जन्म तिथि 10 /08 / 1950 अनु. जाति / 06 /09 /1950 अनु. जन जातिं / 26 /12 /1984 अ० पि० व०॰ क बाद को है॰ तो ऐसी तिथि पर आवेदकं क पिता / पूर्वज का स्थायी निवासः स्थान 4 आवदक क पिता का छत्तसगढ़ राज्य क्षेत्र नें निवास स्थान ६ आवदक क दादा का स्थायी निवास सथोग\n९शैक्षणिक जानकारी\nस. क\nआवेदक की शैक्षणिक जानकारा\nप्राथमिक\nपूर्व माध्यनिक उच्चतर माध्यमिक महाविद्यालयीन\n(3)\n(5)\n\"६,\n4\nशिक्षा का वष 2 संस्थान का नाम 3 ग्राम / कस्व / शहर 4 यिकास खण्ड / तहसील 5 जिला / राज्य\nस. क\nआवेदक क पिता को शेक्षणिक जानकारों\nप्राथमिक\nपूर्द माध्यनिक उच्चत्तर नध्यामक महाविद्यालयीन\n*3.\n५\n6)\n.^\nशिक्षा का चर्ष २ संस्थान का नाम 3 ग्राम / करवा / शहर 4 विकास खण्ड / तहसील 5. जिला / राज्य\niltii 6 ;liic\n\n--- Page 19 (no rotation needed) ---\nछत्तीसगढ़ राजपत्र दिनांक 2 सितम्बर २०१३\n-788 ( १७ )\nस. क\nआवदक कौ माता की शैक्षणिक जानकारी\nप्राथमिक\nपूर्व माध्यमिक\nसच्यतर मध्यामक\nमहाविद्यालयीन\n२\n(५\n६;\nशिक्षा कांवर्ष\n2\nसंस्थान का नम\n3\nग्राम / कम्चवा / शहर\nविकास खण्ड / त्तहसील\n5\nजिला / राज्य\nआवेदक क पित्ता के पिता की शैक्षणिक जञानकारी\nप्राथभक\nपूर्व माध्यमिक\nउच्चतर माध्यमक\nमहाविद्यालयीन\nझ.\n२ 1 शिक्षा का वर्ष\n3\n*।5;\n६६\n2\nसंस्थान का नाम\n$\nग्राम / कसचा / शहर 4 विकास खण्ड / त्तहसील\n5. जिला / राज्य\n१० संपत्ति तंबंधी जानका�\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)\nSection: official_document\nContent:\nService: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ो।\nप्राप्तकर्ता क हस्ताक्षर एवं पदमुद्रा\n\n--- Page 28 (no rotation needed) ---\n788 २६ २९-\nछत्तोसगढ़ राजपत्र टिनांक 2 सितम्बर २०१३\nप्ररूप 3 ख [ नियम ६२ ]\nसक्षम प्राधिकारी का कार्यालय\nआदेदन पत्र क वापसी का ज्ञापनं वापसी झापन)\n(इप् ज्ञापन की मूल प्रति आवेदक को प्रदत्त की जावे तथा उसूका प्रतिपर्ण कार्यालय में संधारित किया जावे\nकमांक\nदिनांक\nश्र श्रीमती / कुमारी आत्मज आन्मजा निवासी द्वारा सामाजिक प्रास्थिति प्रमाणन्पत्र जारी करने हेतु प्रस्तुत आवेदन पत्र में निम्नाकित अभिलेखों क अभाव है॰ अतः अवेदक को निर्देशित किया जाता है कि निम्नांकित अंभिलेख जिनमें सही * का निशान अंकित किया गया है आवेदन पत्र॰के साथ प्रस्तुत करने पर उसके सामाजिए प्रास्थिति प्रगाण-् पत्र जारी करने की कार्यवाही प्रारंभ कीजा सकगीः- (1 ) आवेदक अथवा आवेदक क पिता / पूर्वजों का निम्नांकित दस्तावेज जिसमें उसकी जाति अंकित है पूर्वजों के राजस्व दस्तावेज गिशल) जमाबंदी सर्वेक्षण गिरदावरीः 8 सष्चियबंदोबस्तिलेख (१९५ ; जनगणना (१९३१ ; (छः) वन विभाग की जमाबंदीः नागरिकों का राष्ट्रीय रजिस्टर (१९३९ ; ६ जन्म यां मृत्यु की पंजपीः पिता अथवा पूर्वज के शिक्षित होने को स्थिति में प्रवेश दाखिल / खारिज) पंजी पिताः पूर्वज अथवा संबंधी नातेदार को पूर्व में जारी जाति ग्रगाण प्रमाण-पत्र कों प्रात ग्राारह अन्य दस्तावे जिसस आवेदक क द्वारा दावा की गई जाति होनां प्रमाणित होता है बारह\n(2) ऐरो दस्तावेज अथवा दस्त्तावेजों की रूम्यक रूप सें अंभिप्रभाणित प्रतिलिपि अथवा प्रतिलिपियां जिससे यह प्रमाणित हो सके के आवेदक के पूर्वज राष्ट्रपतीय अधिसूचना तिथि अथवा अन्ग गिछड़ा वर्गकी अधिस्चना तिथि के पूर्व से छत्तीरागड की भैगोलिक सीमा में निवास करते थे। पूर्वजों सेः प्रारंभ कर आवेदक तक पटवारी से प्रदत्त वंशावली ( आवेदक अ�\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "ओबीसी निवास के लिए जाति प्रमाण पत्र ऑफ़लाइन तहसील कार्यालय का पता\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       सेवा केंद्र: अन्य पिछड़ा वर्ग (ओबीसी) प्रमाण पत्र हेतु निवास प्रमाण हेतु ऑफलाइन तहसील कार्यालय का पता।
       
       तहसील कार्यालय: राजस्व और आपदा प्रबंधन विभाग, तहसील कार्यालय, जिला - [जिला का नाम], छत्तीसगढ़।
       
       सेवा केंद्र: सेवा सेतु केंद्र, [तहसील का नाम]।
       
       निवास प्रमाण हेतु ऑफलाइन आवेदन करने के लिए आवेदक को संबंधित तहसील कार्यालय या सेवा सेतु केंद्र जाना होगा।
       ```
| 40 | `क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र विवाह शपथ पत्र के समान है?` | 201 | 201 | ✅ MATCH | new_topic | 3.78s |

### Query 40 Details
* **Query**: `क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र विवाह शपथ पत्र के समान है?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is the verified affidavit in Form III for name change the same as the marriage affidavit?`
* **Resolved Hindi Query**: `क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) विवाह शपथ पत्र (affidavit) के समान नहीं है। नाम परिवर्तन के लिए शपथ पत्र में आवेदक के पुराने और नए नाम, परिवर्तन का कारण और शपथ पत्र पर हस्ताक्षरकर्ता के विवरण की आवश्यकता होती है। विवाह शपथ पत्र का उपयोग विवाह के प्रमाण के लिए किया जाता है। दोनों के उद्देश्य और सामग्री अलग-अलग हैं।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?"
       ```
     * **Response**:
       ```json
       क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?"
       ```
     * **Response**:
       ```json
       Is the verified affidavit in Form III for name change the same as the marriage affidavit?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र विवाह शपथ पत्र के समान है?', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '5', 'service_id': '201'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) (affidavit) विवाह शपथ पत्र (affidavit) (affidavit) के समान है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, नाम परिवर्तन के लिए प्रारूप-III में सत्यापित शपथ पत्र (affidavit) विवाह शपथ पत्र (affidavit) के समान नहीं है। नाम परिवर्तन के लिए शपथ पत्र में आवेदक के पुराने और नए नाम, परिवर्तन का कारण और शपथ पत्र पर हस्ताक्षरकर्ता के विवरण की आवश्यकता होती है। विवाह शपथ पत्र का उपयोग विवाह के प्रमाण के लिए किया जाता है। दोनों के उद्देश्य और सामग्री अलग-अलग हैं।
       ```
| 41 | `भूमि दस्तावेजों और निवास प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन` | 4 | 4 | ✅ MATCH | new_topic | 3.18s |

### Query 41 Details
* **Query**: `भूमि दस्तावेजों और निवास प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "भूमि दस्तावेजों और मूल निवासी प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "भूमि दस्तावेजों और मूल निवासी प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन"
       ```
     * **Response**:
       ```json
       भूमि दस्तावेजों और मूल निवासी प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "भूमि दस्तावेजों और मूल निवासी प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन"
       ```
     * **Response**:
       ```json
       Validate ST caste certificate with land records and original resident certificate.
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "भूमि दस्तावेजों और मूल निवासी प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the process for verifying a caste certificate with land documents and original residence proof?', 'topic_summary': 'User is inquiring about the verification process for a caste certificate, specifically mentioning land documents and original residence proof. This is a new service query, distinct from any previous conversation history.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "भूमि दस्तावेजों और मूल निवासी प्रमाण पत्र के साथ एसटी जाति प्रमाण पत्र का सत्यापन",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
| 42 | `निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण` | None | None | ✅ MATCH | new_topic | 2.25s |

### Query 42 Details
* **Query**: `निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण`
* **Expected Service ID**: `None`
* **Classified Service ID**: `None`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `OBC income certificate slab details for resident students`
* **Resolved Hindi Query**: `निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > जानकारी उपलब्ध नहीं है।

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण"
       ```
     * **Response**:
       ```json
       निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण"
       ```
     * **Response**:
       ```json
       OBC income certificate slab details for resident students
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'OBC income certificate slab details for students living in residence', 'topic_summary': 'Query about OBC income certificate slab for students in residence'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "निवास करने वाले छात्रों के लिए ओबीसी आय प्रमाण पत्र स्लैब विवरण",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': None, 'service_id': None}
       ```
| 43 | `क्या हम सेवासेतु पर विवाह प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?` | None | None | ✅ MATCH | new_topic | 2.57s |

### Query 43 Details
* **Query**: `क्या हम सेवासेतु पर विवाह प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?`
* **Expected Service ID**: `None`
* **Classified Service ID**: `None`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Can we apply together for marriage registration and certificate and name change at Sevasetu?`
* **Resolved Hindi Query**: `क्या हम सेवासेतु पर विवाह पंजीकरण एवं प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > जानकारी उपलब्ध नहीं है।

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या हम सेवासेतु पर विवाह पंजीकरण एवं प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या हम सेवासेतु पर विवाह पंजीकरण एवं प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?"
       ```
     * **Response**:
       ```json
       क्या हम सेवासेतु पर विवाह पंजीकरण एवं प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या हम सेवासेतु पर विवाह पंजीकरण एवं प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?"
       ```
     * **Response**:
       ```json
       Can we apply together for marriage registration and certificate and name change at Sevasetu?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या हम सेवासेतु पर विवाह पंजीकरण एवं प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'Can we apply for marriage registration and certificate along with name change on SewaSetu?', 'topic_summary': 'User is asking about applying for multiple services (marriage registration and name change) on the SewaSetu platform.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या हम सेवासेतु पर विवाह पंजीकरण एवं प्रमाण पत्र और नाम परिवर्तन के लिए एक साथ आवेदन कर सकते हैं?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': None, 'service_id': None}
       ```
| 44 | `यदि मेरे पास पहले से ही निवास प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?` | 4 | 4 | ✅ MATCH | new_topic | 2.41s |

### Query 44 Details
* **Query**: `यदि मेरे पास पहले से ही निवास प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "यदि मेरे पास पहले से ही मूल निवासी प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "यदि मेरे पास पहले से ही मूल निवासी प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?"
       ```
     * **Response**:
       ```json
       यदि मेरे पास पहले से ही मूल निवासी प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "यदि मेरे पास पहले से ही मूल निवासी प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?"
       ```
     * **Response**:
       ```json
       If I already have the original resident certificate, what are the documents required for the SC caste certificate list?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "यदि मेरे पास पहले से ही मूल निवासी प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What are the documents required for SC caste certificate if I already have a native certificate?', 'topic_summary': "User is asking about documents for SC caste certificate, which is a different service from any previous (non-existent) history. This is a new service query, not a follow-up on a specific process. The query is about a government service, so it's not out_of_scope. It's not about the chatbot's identity. It's not a simple greeting, farewell, or thanks. It's not a follow-up on a specific aspect of a service because there is no history. It's a new_topic query about a specific government service (SC caste certificate)."}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "यदि मेरे पास पहले से ही मूल निवासी प्रमाण पत्र है तो एससी जाति प्रमाण पत्र सूची के लिए कौन से दस्तावेज हैं?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
| 45 | `छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए निवास प्रमाण पत्र के नियम` | 7 | 7 | ✅ MATCH | new_topic | 2.50s |

### Query 45 Details
* **Query**: `छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए निवास प्रमाण पत्र के नियम`
* **Expected Service ID**: `7`
* **Classified Service ID**: `7`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: ``
* **Resolved Hindi Query**: ``
* **Intermediate English Answer**:
  > 
* **Intermediate Hindi Answer**:
  > 
* **Final Synthesized Response**:
  > 

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए मूल निवासी प्रमाण पत्र के नियम"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए मूल निवासी प्रमाण पत्र के नियम"
       ```
     * **Response**:
       ```json
       छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए मूल निवासी प्रमाण पत्र के नियम
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए मूल निवासी प्रमाण पत्र के नियम"
       ```
     * **Response**:
       ```json
       Rules for Original Residence Certificate for the spouse of a resident of Chhattisgarh
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए मूल निवासी प्रमाण पत्र के नियम",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What are the rules for an original resident certificate for a spouse in Chhattisgarh?', 'topic_summary': 'User is asking about the rules for an original resident certificate for a spouse in Chhattisgarh.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "छत्तीसगढ़ के निवासी व्यक्ति के जीवनसाथी के लिए मूल निवासी प्रमाण पत्र के नियम",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '4', 'service_id': '7'}
       ```
| 46 | `ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क` | None | None | ✅ MATCH | new_topic | 2.23s |

### Query 46 Details
* **Query**: `ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क`
* **Expected Service ID**: `None`
* **Classified Service ID**: `None`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `OBC certificate fee vs general gazette publication fee`
* **Resolved Hindi Query**: `ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > जानकारी उपलब्ध नहीं है।

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क"
       ```
     * **Response**:
       ```json
       ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क"
       ```
     * **Response**:
       ```json
       OBC certificate fee vs general gazette publication fee
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'What is the fee for OBC certificate vs general Rajpatra publication fee?', 'topic_summary': 'Comparison of fees for OBC certificate and general Rajpatra publication fee.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "ओबीसी प्रमाण पत्र का शुल्क बनाम सामान्य राजपत्र प्रकाशन शुल्क",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': None, 'service_id': None}
       ```
| 47 | `क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?` | 4 | 4 | ✅ MATCH | new_topic | 4.20s |

### Query 47 Details
* **Query**: `क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Is voter ID mandatory for an ST certificate if I have a school study certificate?`
* **Resolved Hindi Query**: `क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, मतदाता पहचान पत्र अनिवार्य नहीं है यदि आपके पास स्कूल अध्ययन प्रमाण पत्र है। स्कूल अध्ययन प्रमाण पत्र जाति प्रमाण के लिए एक सहायक दस्तावेज के रूप में उपयोग किया जा सकता है। हालांकि, जाति प्रमाण के लिए अन्य अनिवार्य दस्तावेज भी हो सकते हैं, जैसे कि सरपंच/पार्षद/विधायक/सांसद से जाति प्रमाण पत्र, प्राथमिक विद्यालय द्वारा जारी स्थानान्तरण प्रमाण पत्र, या अन्य राज्य के अनुसूचित जाति/जनजाति प्रमाणपत्र। आपको आवेदन के समय आवश्यक दस्तावेजों की पूरी सूची की जांच करनी चाहिए।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?"
       ```
     * **Response**:
       ```json
       क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?"
       ```
     * **Response**:
       ```json
       Is voter ID mandatory for an ST certificate if I have a school study certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'Is voter ID mandatory for ST certificate if I have school study certificate?', 'topic_summary': 'User is asking about the eligibility criteria for an ST certificate, specifically if a voter ID is required when they have a school study certificate.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: SC/ST Certificate\nService ID: 4\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Domicile Certificate\n  * Supporting Document 2: Electricity Bill\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Telephone Bill\n  * Supporting Document 5: Birth Certificate\n  * Supporting Document 6: Voters Identity Card\n  * Supporting Document 7: Bpl Certificate\n  * Supporting Document 8: Land And House Document\n  * Supporting Document 9: Driving License\n  * Supporting Document 10: Other Documents\n  * Supporting Document 11: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 12: Photo Identity Card\n  * Supporting Document 13: Service Certificate Of Father / Guardian\n  * Supporting Document 14: Order Of Involuntary Migration\n  * Supporting Document 15: Domicile Certificate\n- SNo 2: Caste Proof (Mandatory: Yes)\n  * Supporting Document 1: Sc/St Certificate Of Other State\n  * Supporting Document 2: Sc/St Certificate From Sarpanch / Parshad / Mla / Mp\n  * Supporting Document 3: Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo\n  * Supporting Document 4: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 5: Educational Certificate\n  * Supporting Document 6: Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family\n  * Supporting Document 7: Primary School Certificate\n  * Supporting Document 8: Birth Information Form\n  * Supporting Document 9: Misal\n  * Supporting Document 10: Adhikar Abhilekh\n  * Supporting Document 11: Jamabandi\n  * Supporting Document 12: Census Register Of 1931\n  * Supporting Document 13: Citizen Register Of 1949\n  * Supporting Document 14: Dakhil / Kharij Panji\n  * Supporting Document 15: Disability / Unavailability Proof\n- SNo 3: Affidavit (Mandatory: No)\n  * Supporting Document 1: Affidavit\n- SNo 4: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 5: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 6: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste STSC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number\n\n--- Source 2: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 14, Col: 2)\n- Field: District [Type: drop down, Data: Charactar] (Row: 15, Col: 1)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 15, Col: 1)\n- Field: Police Station [Type: search, Data: Search] (Row: 16, Col: 2)\n- Field: Permanent Address on or Before Date 10 August 1950 [Type: section lebel, Data: Charactar] (Row: 17, Col: 1)\n- Field: Village or Town [Type: text, Data: Charactar] (Row: 18, Col: 1)\n- Field: Patwari Halka Number [Type: text, Data: Number] (Row: 18, Col: 2)\n- Field: Tehsil [Type: text, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: Data List, Data: Charactar] (Row: 19, Col: 2)\n- Field: Name of Head Of Family on This Date [Type: text, Data: Charactar] (Row: 20, Col: 1)\n- Field: Applicant Relation to Head of Family [Type: drop down, Data: Charactar] (Row: 20, Col: 2)\n- Field: Address Details of Year 10 August 1950 SC or 06 September 1950 ST to till Date Applicant or his Father or Mother or Guardian [Type: section lebel, Data: Charactar] (Row: 21, Col: 1)\n- Field: Is Applicant or his Father or Mother or Guardian Year 1950 to till Date live in Chhattisgarh [Type: drop down, Data: Number] (Row: 22, Col: 1)\n- Field: Address Details of Applicants Guardian [Type: fieldset, Data: Alfa Numeric] (Row: 23, Col: 1)\n- Field: Other Details [Type: section lebel, Data: Charactar] (Row: 24, Col: 1)\n- Field: Have Applicant issued scst certificate before [Type: drop down, Data: Charactar] (Row: 25, Col: 1)\n- Field: Details of document to proof that Beneficiary belongs to SC ST [Type: textarea, Data: Charactar] (Row: 25, Col: 2)\n- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time. [Type: drop down, Data: Alfa Numeric] (Row: 26, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 4_en_4.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nअनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर \nऑनलाइन आवेदन\n\n--- Page 2 ---\nतवषय सूिी \nहोम पेज: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल ................................ ................................ ................................ ................................ .......... 2 \nिरण 1: छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर पंजीयन ................................ ................................ ................................ .................... 3 \nिरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन................................ ................................ ................................ ................................ ............ 4 \nिरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ ............. 5 \nिरण 4: आधार ई-प्रमाणीकरण ................................ ................................ ................................ ................................ ........................ 8 \nिरण 5: अनुसूचिर् जातर्/अनुसूचिर् जनजातर् प्रमाण पत्र के र्लए आवेदन ................................ ................................ .. 9 \nिरण 6: आवश्यक दस्तावेज़ अपलोि करना ................................ ................................ ................................ ............................ 10 \nिरण 7: पूवाावलोकन और आवेदन जमा करना ................................ ................................ ................................ ......................... 11 \nिरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ .. 0 \nिरण 9: पावर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ..........................\n\n--- Source 3: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: तररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट िेकर सुरलित रखें। \n \nचित्र क्रमाांक 20 \nआवेदन संदभा क्रमांक की सहायता से आवेदन की स्थस्थतत छत्तीसगढ़ ई-डिस्ट्रिक्ट क े  पोटटि पर देखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेदन जमा करने क े  बाद डनधाटररत 22 क्रदऩों की समय-सीमा क े  अ ां दर आवेदन का डनराकरण कर क्रदया जाता है। \n• ई-डिस्ट्रिक्ट पोटटि पर आवेदन की स्थस्थतत देखी जा सकती है। \n• अनुसूचित जातत अथवा जनजातत प्रमाण पत्र जारी होने क े  उपराांत इसकी डिचजटि प्रतत ई-डिस्ट्रिक्ट पोटटि से िाउनिोि की \nजा सकती है।\n\n--- [Document: 4_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and\n\n--- Source 4: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �ारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र\nService ID: 4\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: मूल निवासी प्रमाण पत्र\n  * Supporting Document 2: बिजली का बिल\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: टेलीफोन बिल\n  * Supporting Document 5: जन्म प्रमाण पत्र\n  * Supporting Document 6: वोटिंग कार्ड\n  * Supporting Document 7: बी.पी.एल. प्रमाण पत्र\n  * Supporting Document 8: घर या भूमि का दस्तावेज़\n  * Supporting Document 9: ड्राइविंग लाइसेंस\n  * Supporting Document 10: अन्य\n  * Supporting Document 11: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 12: फोटो परिचय पत्र\n  * Supporting Document 13: पिता / पालक की नौकरी का प्रमाण - पत्र\n  * Supporting Document 14: अनैच्छिक प्रवजन का आदेश\n  * Supporting Document 15: मूल निवासी प्रमाण पत्र\n- SNo 2: जाति का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: अन्य राज्य के अनुसूचित जाति / जनजाति प्रमाणपत्र\n  * Supporting Document 2: सरपंच / पार्षद / विधायक / साँसद से जाति प्रमाण-पत्र\n  * Supporting Document 3: प्राथमिक शाला या जिला शिक्षा अधिकारी द्वारा प्रमाणित प्राथमिक शाला द्वारा जारी स्थानान्तरण प्रमाण-पत्र\n  * Supporting Document 4: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 5: शैक्षणिक प्रमाण पत्र\n  * Supporting Document 6: आवेदक को या उसके किसी परिवारजन को जारी हुआ जाति प्रमाण पत्र\n  * Supporting Document 7: प्राथमिक परीक्षा उत्तीर्ण प्रमाण-पत्र\n  * Supporting Document 8: जन्म सूचना प्रपत्र\n  * Supporting Document 9: मिसल\n  * Supporting Document 10: अधिकार अभिलेख\n  * Supporting Document 11: जमाबंदी\n  * Supporting Document 12: १९३१ का जनगणना पंजी\n  * Supporting Document 13: 1949 का नागरिक पंजी\n  * Supporting Document 14: दाखिल / ख़ारिज पंजी\n  * Supporting Document 15: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 3: शपथ पत्र (Mandatory: नहीं)\n  * Supporting Document 1: शपथ पत्र\n- SNo 4: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 5: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document\n\n--- Source 2: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: कमांक पर अंकित हैl॰ अतः श्री / श्रीमती / कुमारी पिता / पति श्री॰ अन्य पिछड़ा चर्ग का /को है !\n2- यह भी प्रमाणित किया जाता है कि श्री / श्रीमती / कुमारी कीमीलेयर सम्पन्न वर्ग व्यक्तियों / वर्गा की श्रेणी में नहीं आते हैं॰ जिसंकाः उल्लेंख भारत सरकार कार्मिक एवं प्रशिक्षण विभाग क पारपत्र संख्या 36012 /2२ /93 /स्था एससीटी ) दिनांक 8=9--93 यथा संशोधित परिपत्र संख्या 36033/3 /2004-स्था आरक्षण दिनांक .14=1t=2008 नथा सभान्य प्रशासन. विभाग के परिपत्र कमांक एफ-9-3 /२001 /१-३ दिनांक २४ 6 २००९ के कालम 3 में किया गया है\n3-\nयह प्रमाण-पत्र इन उपबंधों क अधीन जारीं किया ग़या है कि यदि जिला स्तरीय प्रमाणपत्र सत्यापन समिति अथव उच्द स्तरीय प्रनाणीकरणः छानबीन - समिति क द्वार अपनी जॉच / निरीक्षण सें आवदक श्री / श्रीमतीं / कुमारी क द्वारा प्रस्तुत सामाजिक प्रास्थिति क दावा असत्य अथवा कपटपूर्ण पाया जाता है तो`यह प्रमाण पत्र तत्कालं प्रभाव से निरस्त माना जावेगा तथा तत्समय प्रवृत्त किसी अन्य विधि में अंतर्दिष्ट क़िसी बातः के होते हुए भी छत्तीसगढ़ अनुसूचित जाति अनुसूचित जनजाति और अन्य पिछंड़ा वर्ग सामाजिक प्रास्थिति क प्रमाणीकरण का विनियमनः अधिनियम २०१३ की धारः 8 से १३ के अधीन कार्यवाही कीं जावेगी ;\nहस्ताक्षर\nप्रमाणीकरण अधिकारी का नाम पदनाम / पदमुद्रा\n\n--- Page 34 (no rotation needed) ---\n763 3२\nछत्तीसगढ़ राजपत्र. दिनक 2 सितम्बर २०१३\n# i t५t\nप्ररूतप 4 ख\n(नियम १० देखिए\nसक्षम प्राधिकारीं का कार्यालय\nएस्र ऋम्श सरत क्रमाक\nदिनंक\nअस्थायी रःगाजिक प्रास्थिति प्रभाण-्पत्र सफेद रंग क कागस में केवल प्राथमिल गाध्यमिक स्तर की शैक्षणिक संस्थाओं में प्रवेश तथा छात्रवृत्ति / शिष्यवृत्ति / अन्य प्रयोजनों फ सचीकृति हेतु मान्य )\nअ्रमणल किया ग़ज़ात है कि श्री / श्रीमती / कुमारी आभज आत्मजा न्यास ग्राम त्तहसील. जिला\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: मिल गाध्यमिक स्तर की शैक्षणिक संस्थाओं में प्रवेश तथा छात्रवृत्ति / शिष्यवृत्ति / अन्य प्रयोजनों फ सचीकृति हेतु मान्य )\nअ्रमणल किया ग़ज़ात है कि श्री / श्रीमती / कुमारी आभज आत्मजा न्यास ग्राम त्तहसील. जिला .के द्वारा पस्तुत पपथ- पत्र के अनुसार बह जात्ि जनजाति / अन्य पिछड़ा वर्ग अन्य पिछड़ा वर्ग के कीमीलेयर में सम्मिलित नहों॰ का /की सदरुः है और संविधान के अनुच्छेद ३४१ / ३४२ / राज्य शासन ्कः अधिसूचना रार इर जगत्ति को छत्तीसगढ राज्य क संबंध मं अनुसूचित जाति / अनुसूचित जनजात्ति / अन्र तिछड़ा बर्ग क रूाए मं चिनि्दिष्? किया गया है और यह जाति / जनजाति मध्यप्रदेश पुर्नगठन अधिनिरः- Zteफ धारा १९ े सत्तर्गत्त अनुसूची ३/उक्त अधिनियम को धार २० क अंतर्गत अनुसूची ४ /गर7 शासन फ! . #क िलछ दगं क़ी सूचो में अनुकमांक पर अंकित्त ह और श्री / श्रीमतः / कूमाी .क पिता / पते का नIम .अनुसूचित जागत मुशचा -:\"Atl अन्य ऐिछदः वर्ः! का /की है।\nश्रनाणित किया जाता है कि श्री / श्रीमती / कुभारी ह\nक एरिवार की कुल\nवार्षिक जय\n3= सह प्रमागमपत्र कवल भाररत सरकार / राज़्य सरकार क द्वारा प्रदत्त को जाने वाली छतत्रवृः / शिष्यवृतत को प्राप्त करन क तात्कालिक भ्रथोजन के लिए र किया गयः है और रस एनणत्र की वैधता जारी दिनांक = झंगल 6 माह अथवा स्थाई सागाजिक प्रस्थिति प्रनाण-्पत्र जारी होने तक॰ जो भी पहले हो, कं लिए है\nहस्त्ाक्ष:\nप्रमाणीकरण अधिकारी का नाम पदनाम\nपदमुद्रा( सील!\nrsgil/ n! : ffiitफ़iA * !a ! 0 i०i * :\n\n--- Page 35 (no rotation needed) ---\nछत्तासगढ राजपत्र, दिनांक 2 सिंतम्बर २०१३\n७४8 ( ३३ )\nप्रप 4 7 नियम ११ देखिए)\nसक्षम प्राधिकारी का का्यालय मडल जिला छत्तीसगर\nपस्तक कमांद परल कम्कत.\nदिनाक SOCIAL CASTE CERTIFICAIE (MIGRANT)\nThis is to Certif; tlat Shri Shrimati K umari .Son Daughier :7 of Triilage Towin -11]- District Livrisior O६ te State nioi Teritcr O~ Aa beiongs t१ tne Castc TriD \"1i1c!1 ६ recognisci 7,\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: �) The Scrutiny Committee while pRssing order under sub rule (२) shali authorise an officer of the employer, educational institutiol, local authority the Cenirai Goverment +[ tne Staie Government to fiie complaint under suo section (Z)of section IO of the Act and forward attested copies ofall documents related tothe case to such officer for further proceedings (4) The Scrutiny Committee while passing order under sub rule (२) of this Rule shall issue instructior to the concemed Collector t investigate whether the the Competeni Authority knowingly O१ having knowledge that such certificate was false has issued such False Social Status Certiricate or any Other person has abetted such offence anditne Collector shall forward his report tO :ie State Govemment, within three months (S) The Scrutiny Commiitee after passing the order of cancellation of False Sociai Status Certificate Shaii confiscate ii and detaiis shall ce eteted in tne register as prescribed in FormSi and such Certifcate shali be impressed as \" Cancelled and Confiscated (६) Copies of the order passed by tne Scrutiny Committee shall be sent tO the Non pplicant if any, and i८ the Applicant by registered post immediately arter passing such order If tne Applicant or any ther persor present in the oifice demands copy of the order the same shall be supplied ta the person on payment of appropriate fee २४ Action 8gainst faise Certificate hokler - The officer of the public empioyer, educational institution of a statutor ; body the State Govemnment or Central Govemment as the case may be, who is authorised by the Scrutiny Commitiee shall on the basis of the attested copy of the decision nassed by the Scrutiny Committee; shall fiie 8 written compiaint in the Police Station under subsection (1 of Section IS४ of Criminal Procedure Code, १९७३ (Act no.2 of १९७४) against Ihe said False Social Status Cetificaie holder.\n\n--- Page 58 (no rotation needed) ---\n788 5०\nछत्तोसगढ़ राजपत्र, दिनांक 2 सितम्बर २०१३\n2 Action against the abettor and Competent Aathtority issuing False Social Status Certificate - The Coilector Df the concerned district shall file written complaint egainst the Competent Authority issuing False Social Status Certificaie and tbe abettor of the offence.\nCHAPTER \"\nMISCELLANEOUS\n2६\nProcedure for issuing duplicate of Certificaie and Verificatian Certificate Where an original certificate or verification certificate reiating to an Applicant has been lost Or stolen or destroyed due १० natural calamities like floods, earthquake etc or on request and after depositing fee as piescribed by the State Govemnent, Competent Authority or Verification Committee as the case may bभ : ma y issue the duplicate on the basis of originai document kepi in such office There shall be a clear mention of \" Duplicate Copy ८6 70 on such Cartificate or Verification Certiificate 27 Notice regarding Issuancc, Verification or Cancellation of Certificate (l) Competent Authority Verification Commitiee and Scrutiny Conmiitee as the case may be, shall display the information regarding issuance, varification or cancellation of Certificnte erer y month beforeithe Fifth ca ; of tne miontn oL tiie office Nciice Board and shall alst send the iniormatin t० local aui2TOTICYuE institutions and bodies municipal corporation municipality. village panchayat ete for their records AEid क़hail also sen the information through District Information Centres in order t० display it on ascertained tebsite (२) Competent Authority shall diso send the information regarding issue Of certificate Jid cancellation of applications, every year by ३१\" December to the State Governient in prescribed Form-7 .\n(3) Terificatin Committze stati sept tne information regarving verificatioi Of ceitificates, cancellation of application, cases forwarded to $ utiny Committee every rear by ३l\" December to thc Statc Govemment, inl prescribed Form- ७B (४) Scrutiny Committee shall send the information regarding inquiry on the complaints referred by the State Government and Verification Corrimittees and cancellation ol Certificate every year by ३१\"t Deceinber to tnhe State Govemment in prescribed Form7C.\nBy order and in the name of the Govemor of Chhattisgarh, MANOJ KUMAR PINGUA, Secrctary.\nil::*.: ]^\n\n--- Page 59 (no rotation needed) ---\nछत्तीसगढ़ राजपत्र दिनांक 2 सितम्बर २०१३ 4}:\n788 ( 57 )\nForrn - IA\n(See Ruie ३(1 )\nApplication For Social Status Certificate\nTo, Competent Authority; Sub Division. District.\nSir\nbeg t० State that in order to avail facilities given to Scheduled Castes Scheduled Tribes Other Backward Classes Lग़y son daughter requires Certificate of Sociai Status in this coniection foliowing information is being submitied, namely: - Name of the Applicant 2 Father $ Name Of the Applicant - Applicait $ maritai status Liarried nmarried 4 Name of the Husband (in case Of femaie appiicant) 5 Date of Birth of Applicant + Caste ( For SC only ) 7 Present Address in full: Mohalla Tard\nVillage Town City Block. Yehsii.....\nDistrict .\nState.\nठ\nPermaneड़t Address in fuit: Mohatia Ward\nVillage Town City. Bicci Tehsil\nDistrict.\nStie ..\n3\nApplicaड़it 5 Dare of Birth: (a)if beiore !O/O३ SO for SC and 6l९l५० for ST; Mohalia Tr ard (b) if before Zb/1२ ८4 far OBC Village Town City then. piace of ङirth of applicani; OT if after taese dates ten Block . Tensil permnansnt resitcntiai acdress of his Father Ancesior Disirici.. .+ Siate. १० Head nf the Faग़ily resicing on ihe above mentioned address +lame on Tac abore ientioned daie Keiation \"itli the\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या एसटी प्रमाण पत्र के लिए मतदाता पहचान पत्र अनिवार्य है यदि मेरे पास स्कूल अध्ययन प्रमाण पत्र है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, मतदाता पहचान पत्र अनिवार्य नहीं है यदि आपके पास स्कूल अध्ययन प्रमाण पत्र है। स्कूल अध्ययन प्रमाण पत्र जाति प्रमाण के लिए एक सहायक दस्तावेज के रूप में उपयोग किया जा सकता है। हालांकि, जाति प्रमाण के लिए अन्य अनिवार्य दस्तावेज भी हो सकते हैं, जैसे कि सरपंच/पार्षद/विधायक/सांसद से जाति प्रमाण पत्र, प्राथमिक विद्यालय द्वारा जारी स्थानान्तरण प्रमाण पत्र, या अन्य राज्य के अनुसूचित जाति/जनजाति प्रमाणपत्र। आपको आवेदन के समय आवश्यक दस्तावेजों की पूरी सूची की जांच करनी चाहिए।
       ```
| 48 | `यदि पति दूसरे राज्य से संबंधित है तो विवाह प्रमाण पत्र का आवेदन कहां जमा करें?` | 3 | 3 | ✅ MATCH | new_topic | 4.29s |

### Query 48 Details
* **Query**: `यदि पति दूसरे राज्य से संबंधित है तो विवाह प्रमाण पत्र का आवेदन कहां जमा करें?`
* **Expected Service ID**: `3`
* **Classified Service ID**: `3`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Where should I submit the application for marriage registration and certificate if the husband is from another state?`
* **Resolved Hindi Query**: `यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन पति के दूसरे राज्य से संबंधित होने पर भी स्थानीय क्षेत्र में ही जमा करना होगा, जहाँ विवाह संपन्न हुआ है। विवाह का पंजीकरण उसी स्थान पर होना चाहिए जहाँ विवाह संपन्न हुआ है, न कि जोड़े के निवास स्थान पर। स्थानीय प्राधिकरण (ग्राम पंचायत या नगर पालिका) ही इस आवेदन की प्रक्रिया पूरी करेगा।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?"
       ```
     * **Response**:
       ```json
       यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?"
       ```
     * **Response**:
       ```json
       Where should I submit the application for marriage registration and certificate if the husband is from another state?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'Where to submit the application for marriage registration and certificate if the husband is from a different state?', 'topic_summary': 'Marriage registration and certificate application for a spouse from a different state.'}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '1', 'service_id': '3'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- MARRIAGE JURISDICTION RULE: Under the Chhattisgarh Compulsory Registration of Marriages Rules, a marriage MUST be registered in the local area where the marriage was solemnized or performed, NOT at the couple's hometown or place of residence. The registrar is the Local Authority of that local area (Gram Panchayat if rural; Municipality or Municipal Corporation if urban). State this clearly when citizens ask where or under which office/authority to register their marriage.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Marriage Registration & Certificate\nService ID: 3\nLanguage: EN\nDepartment: Urban Administration and development Department\nTime Limit / SLA: 15 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Affidavit (Mandatory: Yes)\n  * Supporting Document 1: Affidavit\n- SNo 2: At The Time Of Marriage Combined Photograph Of Groom And Bride(2a Size) (Mandatory: Yes)\n  * Supporting Document 1: At The Time Of Marriage Combined Photograph Of Groom And Bride(2a Size)\n- SNo 3: Declaration Letter From Guardian Of Married Couple (Mandatory: No)\n  * Supporting Document 1: Declaration Letter From Guardian Of Married Couple\n- SNo 4: Other (Mandatory: No)\n  * Supporting Document 1: Other\n- SNo 5: Necessary Documents (Mandatory: No)\n  * Supporting Document 1: Necessary Documents\n- SNo 6: Birth Certificate Of Groom (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate Of Groom\n- SNo 7: Birth Certificate Of Bride (Mandatory: Yes)\n  * Supporting Document 1: Birth Certificate Of Bride\n- SNo 8: Document Signed By The Bride And Groom (First Page) (Mandatory: Yes)\n  * Supporting Document 1: Document Signed By The Bride And Groom (First Page)\n- SNo 9: Document Signed By The Bride And Groom (Second Page) (Mandatory: Yes)\n  * Supporting Document 1: Document Signed By The Bride And Groom (Second Page)\n- SNo 10: Copy Of Challan (Mandatory: Yes)\n  * Supporting Document 1: Copy Of Challan\n- SNo 11: Marriage Invitation Card (Mandatory: Yes)\n  * Supporting Document 1: Marriage Invitation Card\n- SNo 12: Divorce Certifcate (Mandatory: No)\n  * Supporting Document 1: Divorce Certificate\n- SNo 13: Widow Certificate (Mandatory: No)\n  * Supporting Document 1: Widow Certificate\n- SNo 14: Inter Religion Marriage Certificate (Mandatory: No)\n  * Supporting Document 1: Inter Religion Marriage Certificate\n\nAPPLICATION FORM FIELDS:\n- Field: Marriage Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Date of Marriage [Type: date, Data: Date] (Row: 2, Col: 1)\n- Field: Place of Marriage [Type: textarea, Data: Alfa Numeric] (Row: 2, Col: 2)\n- Field: Type of Marriage [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Is marriage Registered [Type: drop down, Data: Charactar] (Row: 3, Col: 2)\n- Field: Registration Number [Type: text, Data: Number] (Row: 4, Col: 1)\n- Field: Other Details [Type: textarea, Data: Charactar] (Row: 4, Col: 2)\n- Field: Groom Details [Type: section lebel, Data: Charactar] (Row: 5, Col: 1)\n- Field: Name of Groom in Local Language [Type: text, Data: Charactar] (Row: 6, Col: 1)\n- Field: Name of Groom in English [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Date of Birth of Groom [Type: date, Data: Date] (Row: 7, Col: 1)\n- Field: Age at time of marriage [Type: text, Data: Number] (Row: 7, Col: 2)\n- Field: Father Name in local language [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Father Name in English [Type: textarea, Data: Charactar] (Row: 8, Col: 2)\n- Field: Marital Status of Groom [Type: drop down, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address Of Groom [Type: section lebel, Data: Charactar] (Row: 10, Col: 1)\n- Field: Present Address of groom in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: Present Address of Groom in English [Type: textarea, Data: Alfa Numeric] (Row: 11, Col: 2)\n- Field: Permanent Address of Groom in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Permanent Address of Groom in English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 2)\n- Field: Witness Details of Groom Side [Type: fieldset, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Bride Details [Type: section lebel, Data: Charactar] (Row: 14, Col: 1)\n- Field: Name of Bride in local language [Type: text, Data: Charactar] (Row: 15, Col: 1)\n- Field: Name of Bride in English [Type: text, Data: Charactar] (Row: 15, Col: 2)\n- Field: Date of Birth of Bride [Type: date, Data: Date] (Row: 16, Col: 1)\n- Field: Bride Age at time of marriage [Type: text, Data: Number] (Row: 16, Col: 2)\n- Field: Fathers name of Bride in Local language [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: Fathers name of Bride in English [Type: text, Data: Charactar] (Row: 17, Col: 2)\n- Field: Marital Status of Bride [Type: drop down, Data: Charactar] (Row: 18, Col: 1)\n- Field: Address Of Bride [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: Present Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Present Address\n\n--- Source 2: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की जांच सूची \n \nचरण 4.3: इस गविंिो में क्रिए गए “जमा” बटन पर क्लिक करें।\n\n--- Page 8 ---\nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन \nचरण 5.1: आवेिन फॉमट में वर से संबंजित आवश्यक जानकाररयााँ िजट करें। \n \n \nचचत्र क्रमांक 10: वििाह पंजीकरण हेर्ु आिेदन फॉमा – िर से संबंविर् वििरण \n \nचरण 5.2: आवेिन में विु से संबंजित जानकाररयााँ िजट करें। \n \nचचत्र क्रमांक 11: वििाह पंजीकरण हेर्ु आिेदन फॉमा – ििु से संबंविर् वििरण \n \nचरण 5.3: फॉमट भरने क े  बाि “सहेजें और पूिाािलोकन” बटन पर क्लिक करें।\n\n--- Page 9 ---\nचरण 6: आिश्यक दस्तािेज़ अपलोि करना \nअनुलग्नक का गववरण पेज खुलेगा। आवश्यक िस्तावेज़ अपलोि करने क े  ललए ननम्न प्रक्रिया का पालन करें। \n \n \nचचत्र क्रमांक 12: सहायक दस्तािेज़ अपलोि \nचरण 6.1: “Choose File”  पर क्लिक कर अपने कम्प्यूटर या लैपटॉप से िस्तावेज की स्क ै न कॉपी चुनें। \nचरण 6.2: फाइल चुनने क े बाि “UPLOAD”  पर क्लिक करें। \n \n \nचचत्र क्रमांक 13: अनुलग्नक सहेजना \n \nचरण 6.3: िस्तावेज अपलोि करने क े  बाि “अनुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुक्रिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें।\n\n--- Page 10 ---\nचरण 7: पूिाािलोकन और आिेदन जमा करना \nअनुलग्नक सहेजने क े  पश्चात् ननम्न जचत्रानुसार पूवाटवलोकन पेज खुलेगा। ध्यानपूवटक अपने आवेिन की जांच करें। \n \n \nचचत्र क्रमांक 14: पूिाािलोकन \n \n \nचचत्र क्रमांक 15: घोषणा एिं जमा \n \nचरण 7.1 घोषणा: घोषणा हेतु ननिाटररत बॉक्स पर क्लिक करें। \nचरण 7.2: घोषणा पर क्लिक करते ही “जमा करें” बटन क्रिखाई िेग\n\n--- Source 3: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: ढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉगगन प्रगक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासििा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \nचरण 3.2: खोजें पर क्लिक करें। सेवाओं की सूची खुलेगी। \n \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.3: सेवाओं की सूची में प्रिजशित वििाह प्रमाण पत्र (Marriage Certificate) पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। इस पेज पर आवश्यक िस्तावेज़़ों की सूची भी िेखी जा सकती है। \n \n \nचचत्र क्रमांक 7: सेिा पररचय एिं सहायक दस्तािेज़़ों की सूची \n \nचरण 3.4: “आगे” बटन पर क्लिक करें।\n\n--- Page 7 ---\nचरण 4: आिेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की\n\n--- Source 4: [Official Specification (English)] ---\nService: Marriage Registration & Certificate (ID: 3)\nSection: combined_manual\nContent:\nService: Marriage Registration & Certificate\nDepartment: Urban Administration and development Department\nCombined Manual Content: Row: 16, Col: 1)\n- Field: Bride Age at time of marriage [Type: text, Data: Number] (Row: 16, Col: 2)\n- Field: Fathers name of Bride in Local language [Type: text, Data: Charactar] (Row: 17, Col: 1)\n- Field: Fathers name of Bride in English [Type: text, Data: Charactar] (Row: 17, Col: 2)\n- Field: Marital Status of Bride [Type: drop down, Data: Charactar] (Row: 18, Col: 1)\n- Field: Address Of Bride [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: Present Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Present Address of Bride in English [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: Permanent Address of Bride in Local Language [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 1)\n- Field: Permanent Address of Bride in English [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 2)\n- Field: Witness Details of Bride Side [Type: fieldset, Data: Alfa Numeric] (Row: 22, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 3_en_3.pdf (USER_MANUAL)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nवििाह पंजीकरण एिं प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nपर ऑनलाइन आिेदन\n\n--- Page 2 ---\nविषय सूची \nई-डिस्ट्रिक्ट: होम पेज ................................ ................................ ................................ ................................ ................................ .................. 2 \nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण ................................ ................................ ................................ ................................ ............... 3 \nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन ................................ ................................ ................................ ................................ .................... 4 \nचरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ .................. 5 \nचरण 4: आिेदक की बुडनयादी जानकारी ................................ ................................ ................................ ................................ ............... 6 \nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन ................................ ................................ ................................ ....................... 7 \nचरण 6: आिश्यक दस्तािेज़ अपलोि करना ................................ ................................ ................................ ................................ .......... 8 \nचरण 7: पूिाािलोकन और आिेदन जमा करना ................................ ................................ ................................ ................................ ...... 9 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 10 \nचरण 9: पािर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ................................  11\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉगगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉगगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nच\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: विवाह पंजीकरण एवं प्रमाण पत्र\nService ID: 3\nLanguage: HI\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nTime Limit / SLA: 15 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: शपथ पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शपथ पत्र\n- SNo 2: वर एवं वधु का संयुक्त फोटो(2A साईज) प्रमाण पत्र के लिए (Mandatory: हाँ)\n  * Supporting Document 1: वर एवं वधु का संयुक्त फोटो(2A साईज) प्रमाण पत्र के लिए\n- SNo 3: प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: विवाह अनुस्थान संपन्न कराने वाले के सत्यापन के लिए उस समय उपस्थित पंडित /पादरी /मौलवी अथवा समाज का प्रमाण पत्र\n- SNo 4: अन्य कारण (Mandatory: नहीं)\n  * Supporting Document 1: अन्य कारण\n- SNo 5: आवश्यक दस्तावेज़ (Mandatory: नहीं)\n  * Supporting Document 1: आवश्यक दस्तावेज़\n- SNo 6: वर का जन्म प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: वर का जन्म प्रमाण पत्र\n- SNo 7: वधु का जन्म प्रमाण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: वधु का जन्म प्रमाण पत्र\n- SNo 8: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (प्रथम पेज) (Mandatory: हाँ)\n  * Supporting Document 1: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (प्रथम पेज)\n- SNo 9: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (व्दितीय पेज) (Mandatory: हाँ)\n  * Supporting Document 1: वर एव वधु द्वारा हस्ताक्षरित दस्तावेज (व्दितीय पेज)\n- SNo 10: चालान की प्रति (Mandatory: हाँ)\n  * Supporting Document 1: चालान की प्रति\n- SNo 11: विवाह आमंत्रण पत्र (Mandatory: हाँ)\n  * Supporting Document 1: विवाह आमंत्रण पत्र\n- SNo 12: तलाक प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: तलाक प्रमाण पत्र\n- SNo 13: विधवा प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: विधवा प्रमाण पत्र\n- SNo 14: अंतरधार्मिक विवाह प्रमाण पत्र (Mandatory: नहीं)\n  * Supporting Document 1: अंतरधार्मिक विवाह प्रमाण पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: वैवाहिक जानकारी [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: विवाह की तिथि [Type: date, Data: Date] (Row: 2, Col: 1)\n- Field: विवाह का स्थान [Type: textarea, Data: Alfa Numeric] (Row: 2, Col: 2)\n- Field: विवाह का प्रकार [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: क्या विवाह पंजीकृत है [Type: drop down, Data: Charactar] (Row: 3, Col: 2)\n- Field: पंजीयन क्रमांक [Type: text,\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: ्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की जांच सूची \n \nचरण 4.3: इस गविंिो में क्रिए गए “जमा” बटन पर क्लिक करें।\n\n--- Page 8 ---\nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन \nचरण 5.1: आवेिन फॉमट में वर से संबंजित आवश्यक जानकाररयााँ िजट करें। \n \n \nचचत्र क्रमांक 10: वििाह पंजीकरण हेर्ु आिेदन फॉमा – िर से संबंविर् वििरण \n \nचरण 5.2: आवेिन में विु से संबंजित जानकाररयााँ िजट करें। \n \nचचत्र क्रमांक 11: वििाह पंजीकरण हेर्ु आिेदन फॉमा – ििु से संबंविर् वििरण \n \nचरण 5.3: फॉमट भरने क े  बाि “सहेजें और पूिाािलोकन” बटन पर क्लिक करें।\n\n--- Page 9 ---\nचरण 6: आिश्यक दस्तािेज़ अपलोि करना \nअनुलग्नक का गववरण पेज खुलेगा। आवश्यक िस्तावेज़ अपलोि करने क े  ललए ननम्न प्रक्रिया का पालन करें। \n \n \nचचत्र क्रमांक 12: सहायक दस्तािेज़ अपलोि \nचरण 6.1: “Choose File”  पर क्लिक कर अपने कम्प्यूटर या लैपटॉप से िस्तावेज की स्क ै न कॉपी चुनें। \nचरण 6.2: फाइल चुनने क े बाि “UPLOAD”  पर क्लिक करें। \n \n \nचचत्र क्रमांक 13: अनुलग्नक सहेजना \n \nचरण 6.3: िस्तावेज अपलोि करने क े  बाि “अनुलग्नक सहेजें” पर क्लिक करें। \nचरण 6.4: पुक्रिकरण क े  ललए िॉयलॉग बॉक्स खुलेगा, इसे ओक े कर िें।\n\n--- Page 10 ---\nचरण 7: पूिाािलोकन और आिेदन जमा करना \nअनुलग्नक सहेजने क े  पश्चात् ननम्न जचत्रानुसार पूवाटवलोकन पेज खुलेगा। ध्यानपूवटक अपने आवेिन की जांच करें। \n \n \nचचत्र क्रमांक 14: पूिाािलोकन \n \n \nचचत्र क्रमांक 15: घोषणा एिं जमा \n \nचरण 7.1 घोषणा: घोषणा हेतु ननिाटररत बॉक्स पर क्लिक करें। \nचरण 7.2: घोषणा पर क्लिक करते ही “जमा करें” बटन क्रिखाई िेगा। इस पर क्ल\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: वधु का पता [Type: section lebel, Data: Charactar] (Row: 19, Col: 1)\n- Field: वधु का वर्तमान पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: वधु का वर्तमान पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: वधु का स्थायी पता स्थानीय भाषा में [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 1)\n- Field: वधु की स्थायी पता अंग्रेजी में [Type: textarea, Data: Alfa Numeric] (Row: 21, Col: 2)\n- Field: वधु पक्ष के गवाह का विवरण [Type: fieldset, Data: Alfa Numeric] (Row: 22, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 3_hi_3.pdf (INSTRUCTION)] ---\n--- Page 1 ---\nछत्तीसगढ़ इन्फोटेक प्रमोशन सोसायटी        \nउपयोगकर्ाा मागादर्शिका \n \n  \nवििाह पंजीकरण एिं प्रमाण पत्र हेर्ु छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल \nपर ऑनलाइन आिेदन\n\n--- Page 2 ---\nविषय सूची \nई-डिस्ट्रिक्ट: होम पेज ................................ ................................ ................................ ................................ ................................ .................. 2 \nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण ................................ ................................ ................................ ................................ ............... 3 \nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन ................................ ................................ ................................ ................................ .................... 4 \nचरण 3: योजना खोज ................................ ................................ ................................ ................................ ................................ .................. 5 \nचरण 4: आिेदक की बुडनयादी जानकारी ................................ ................................ ................................ ................................ ............... 6 \nचरण 5: वििाह पंजीकरण एिं प्रमाण पत्र हेर्ु आिेदन ................................ ................................ ................................ ....................... 7 \nचरण 6: आिश्यक दस्तािेज़ अपलोि करना ................................ ................................ ................................ ................................ .......... 8 \nचरण 7: पूिाािलोकन और आिेदन जमा करना ................................ ................................ ................................ ................................ ...... 9 \nचरण 8: शुल्क का भुगर्ान ................................ ................................ ................................ ................................ ................................ ....... 10 \nचरण 9: पािर्ी सुरक्षिर् रखना ................................ ................................ ................................ ................................ ................................  11\n\n--- Page 3 ---\nई-डिस्ट्रिक्ट: होम पेज \nअपने कम्प्यूटर या लैपटॉप क े  वेब ब्राउज़र में टाइप करें – cgedistrict.cgstate.gov.in   \nननम्नानुसार होमपेज खुलेगा। \n \nचचत्र क्रमांक 1: छ्त्त्तीसगढ़ ई-डिस्ट्रिक्ट होम पेज \n \nलॉगगन करने क े  ललए होम पेज पर नागररक लॉगगन बटन पर क्लिक करें। \n \nचचत्र क्रमांक 2: नागररक लॉगगन बटन\n\n--- Page 4 ---\nचरण 1: ई-डिस्ट्रिक्ट पोटाल पर पंजीकरण \nअगर आप नए यूज़र हैं तो छत्तीसगढ़ ई-निस्ट्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक\n\n--- Source 4: [Official Specification (Hindi)] ---\nService: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)\nSection: combined_manual\nContent:\nService: विवाह पंजीकरण एवं प्रमाण पत्र\nDepartment: नगरीय प्रशासन एवं विकास विभाग\nCombined Manual Content: �्रिक्ट पोटटल पर ननम्न प्रक्रिया द्वारा रजजस्टर करें। \n \nचचत्र क्रमांक 3: निीन उपयोगकर्ाा पंजीयन \n \nचरण 1.1: नए पंजीयन हेतु क्रिए गए ललिंक पर क्लिक करें, ननम्नानुसार नागररक पंजीकरण पेज खुलेगा। \n \nचचत्र क्रमांक 4: नागररक पंजीकरण पेज \n \nचरण 1.2: नागररक पंजीकरण पेज पर आवेिक उपयोगकताट नाम िजट करें। \nचरण 1.2: फॉमट में पूछी गई ज़रूरी जानकाररयााँ िजट करें। \nचरण 1.2: “जमा करें” बटन पर क्लिक करें। इस तरह रजजरिेशन प्रक्रिया पूणट होती है।\n\n--- Page 5 ---\nचरण 3: पंजीक ृ र् उपयोगकर्ाा लॉगगन \nपंजीक ृ त उपयोगकताट ननम्न प्रक्रिया द्वारा लॉगगन करें। \n \nचचत्र क्रमांक 5: उपयोगकर्ाा लॉगगन प्रगक्रया \n \n1. यूज़रनेम िजट करें। \n2. पासििा िजट करें। \n3. “ओटीपी भेजें” पर क्लिक करें। \n4. अपने पंजीक ृ त नंबर पर प्राप्त ओटीपी यहााँ िजट करें।  \n5. लॉगगन बटन पर क्लिक करें।\n\n--- Page 6 ---\nचरण 3: योजना खोज \nचरण 3.1: योजना खोज पेज में िी गई जानकारी भरें। \nचरण 3.2: खोजें पर क्लिक करें। सेवाओं की सूची खुलेगी। \n \n \nचचत्र क्रमांक 6: योजना खोज पेज \n \nचरण 3.3: सेवाओं की सूची में प्रिजशित वििाह प्रमाण पत्र (Marriage Certificate) पर क्लिक करें। \nननम्नानुसार सेवा का पररचय पेज खुलेगा। इस पेज पर आवश्यक िस्तावेज़़ों की सूची भी िेखी जा सकती है। \n \n \nचचत्र क्रमांक 7: सेिा पररचय एिं सहायक दस्तािेज़़ों की सूची \n \nचरण 3.4: “आगे” बटन पर क्लिक करें।\n\n--- Page 7 ---\nचरण 4: आिेदक की बुडनयादी जानकारी \nचरण 4.1: ननम्नानुसार फॉमट में पूछी गई जानकाररयााँ िजट करें।   \n \nचचत्र क्रमांक 8: आिेदक की बुडनयादी जानकारी \n \nचरण 4.2: फॉमट भरने क े  बाि “जमा करें” बटन पर क्लिक करें। ननम्नानुसार िस्तावेज़़ों की जांच सूची क्रिखाई \nिेगी। \n \nचचत्र क्रमांक 9: सहायक दस्तािेज़़ों की जांच सूच\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "यदि पति दूसरे राज्य से संबंधित है तो विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन कहां जमा करें?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       विवाह पंजीकरण एवं प्रमाण पत्र का आवेदन पति के दूसरे राज्य से संबंधित होने पर भी स्थानीय क्षेत्र में ही जमा करना होगा, जहाँ विवाह संपन्न हुआ है। विवाह का पंजीकरण उसी स्थान पर होना चाहिए जहाँ विवाह संपन्न हुआ है, न कि जोड़े के निवास स्थान पर। स्थानीय प्राधिकरण (ग्राम पंचायत या नगर पालिका) ही इस आवेदन की प्रक्रिया पूरी करेगा।
       ```
| 49 | `क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?` | 201 | 201 | ✅ MATCH | new_topic | 2.88s |

### Query 49 Details
* **Query**: `क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?`
* **Expected Service ID**: `201`
* **Classified Service ID**: `201`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `Can the name change gazette be used for name correction in OBC certificate?`
* **Resolved Hindi Query**: `क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?`
* **Intermediate English Answer**:
  > N/A
* **Intermediate Hindi Answer**:
  > N/A
* **Final Synthesized Response**:
  > नहीं, नाम परिवर्तन राजपत्र का उपयोग ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नहीं किया जा सकता है। नाम परिवर्तन राजपत्र केवल नाम परिवर्तन के लिए होता है, जबकि प्रमाण पत्र में नाम सुधारने के लिए अलग से आवेदन करना पड़ता है।
  > 
  > अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
  > [सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?"
       ```
     * **Response**:
       ```json
       क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?"
       ```
     * **Response**:
       ```json
       Can the name change gazette be used for name correction in OBC certificate?
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'Can OBC proof be used for name change gazette in the context of OBC certificate?', 'topic_summary': 'Query about using OBC proof for name change gazette, a different service from the general process of name change.'}
       ```
  5. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n- EXCEPTIONS FOR ISSUED CERTIFICATE CORRECTIONS: If the user query is about correcting a name or spelling mistake on an ALREADY ISSUED certificate or document (such as a Domicile Certificate, Caste Certificate, or Marriage Certificate):\n  1. Do NOT output 'Information not available.'\n  2. Explain that the official and only method to correct a spelling mistake or change a name on an already issued certificate in Chhattisgarh is by applying for an Ordinary Gazette Notification for Name Change.\n  3. Detail the required steps and documents (SBI challan of Rs 430, notarized affidavit of Rs 50, newspaper advertisement, deed form with 2 witnesses) from the Gazette context, stating that this process is required to correct the name on the requested certificate.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: Ordinary Gazette Notification for Name Change\nService ID: 201\nLanguage: EN\nDepartment: Government Printing and Stationery Department\nTime Limit / SLA: 29 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of A Challan Of ₹ 430/- From Any Branch Of The State Bank Of India. (Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts).\n- SNo 2: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper(Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper(Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)\n  * Supporting Document 1: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)\n  * Supporting Document 1: Other Document 2\n  * Supporting Document 2: Other Document 1 [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: Old Name & New Name Verification Document (Mandatory: Yes)\n  * Supporting Document 1: Old Name & New Name Verification Document\n- SNo 6: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit. (Mandatory: Yes)\n  * Supporting Document 1: All Types Of Documents/Identity Cards/Ids That Have Been Mentioned In The Affidavit.\n- SNo 7: Identity card of the applicant issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of the applicant issued by the government\n- SNo 8: Identity card of witnesses issued by the government (Mandatory: Yes)\n  * Supporting Document 1: Identity card of witnesses issued by the government\n\nAPPLICATION FORM FIELDS:\n- Field: Applicant Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Relationship of guardian to beneficiary [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: Full Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: Full Name (Before Change) In English [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: Challn Number [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: Gender [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: Father/Mother/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: Father/Mother/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: Change applicable to [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: Wife/Husband Name In Hindi [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: Wife/Husband Name In English [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: Son/Daughter Name (before change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Son/Daughter Name (Before Change) In English [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: Son/Daughter Name (after change) in Hindi [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: Son/Daughter Name (after change) in English [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: Full Name (After Change) In Hindi [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop\n\n--- Source 2: [Official Specification (English)] ---\nService: Ordinary Gazette Notification for Name Change (ID: 201)\nSection: combined_manual\nContent:\nService: Ordinary Gazette Notification for Name Change\nDepartment: Government Printing and Stationery Department\nCombined Manual Content: Alfa Numeric] (Row: 14, Col: 1)\n- Field: Full Name (After Change) In English [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: Contact Information [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: Residential Address [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: District [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: Village/City [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: Tehsil [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: PIN Code [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_en_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_en_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_en_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nService ID: 201\nLanguage: HI\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nTime Limit / SLA: 29 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां) (Mandatory: हाँ)\n  * Supporting Document 1: 430 रू. (चार सौ तीस रुपये मात्र) का भारतीय स्टेट बैंक की किसी भी शाखा से चालान की मूल प्रति।(हेड – 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां)\n- SNo 2: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: 50 रू. के नॉन ज्यूडिशियल स्टाम्प पेपर में प्ररूप-तीन में नोटराइज्ड शपथ पत्र (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf]\n- SNo 3: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। (Mandatory: हाँ)\n  * Supporting Document 1: स्थानीय समाचार पत्र में नाम परिवर्तन के प्ररूप-एक में सूचना के प्रकाशन की मूल प्रति (आवेदन की तारीख से तीन माह से अधिक पुराना ना हो)। [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf]\n- SNo 4: दो गवाहों के नाम, हस्ताक्षर एवं पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति। (Mandatory: हाँ)\n  * Supporting Document 1: अन्य दस्तावेज़ २\n  * Supporting Document 2: अन्य दस्तावेज़ १ [Format: https://sewasetu.cgstate.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory:\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: state.gov.in/resources/docFormat/23848.pdf]\n- SNo 5: पुराना नाम और नया नाम सत्यापन दस्तावेज़ (Mandatory: हाँ)\n  * Supporting Document 1: पुराना नाम और नया नाम सत्यापन दस्तावेज़\n- SNo 6: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो। (Mandatory: हाँ)\n  * Supporting Document 1: सभी प्रकार के दस्तावेज/पहचान पत्र/आई.डी., जिनका शपथ पत्र में उल्लेख किया गया हो।\n- SNo 7: शासन द्वारा जारी आवेदक का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी आवेदक का पहचान पत्र\n- SNo 8: शासन द्वारा जारी गवाहों का पहचान पत्र (Mandatory: हाँ)\n  * Supporting Document 1: शासन द्वारा जारी गवाहों का पहचान पत्र\n\nAPPLICATION FORM FIELDS:\n- Field: आवेदक विवरण [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: अधिसूचना प्रकाशन की भाषा [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)\n- Field: परिवर्तन प्रकार [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: अभिभावक का हितग्राही से संबंध [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)\n- Field: हितग्राही का पूरा नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 1)\n- Field: हितग्राही का पूरा नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 4, Col: 2)\n- Field: चालान नंबर [Type: text, Data: Alfa Numeric] (Row: 5, Col: 1)\n- Field: जन्म तिथि [Type: date, Data: Date] (Row: 6, Col: 1)\n- Field: लिंग [Type: drop down, Data: Alfa Numeric] (Row: 6, Col: 2)\n- Field: पिता/माता/पति का नाम हिंदी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 1)\n- Field: पिता/माता/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 7, Col: 2)\n- Field: परिवर्तन किसके लिए है [Type: drop down, Data: Alfa Numeric] (Row: 8, Col: 1)\n- Field: पत्नी/पति का नाम हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 1)\n- Field: पत्नी/पति का नाम अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 9, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव से पहले) अंग्रेजी में [Type: text, Data: Charactar] (Row: 12, Col: 2)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदला�\n\n--- Source 3: [Official Specification (Hindi)] ---\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (ID: 201)\nSection: combined_manual\nContent:\nService: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना\nDepartment: शासकीय मुद्रण एवं लेखन सामग्री विभाग\nCombined Manual Content: �) हिंदी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 1)\n- Field: पुत्र / पुत्री का नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 13, Col: 2)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) हिन्दी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: हितग्राही का पूरा नाम (बदलाव के बाद) अंग्रेजी में [Type: text, Data: Alfa Numeric] (Row: 14, Col: 2)\n- Field: नाम परिवर्तन संबंधित दस्तावेजों का विवरण [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)\n- Field: संपर्क जानकारी [Type: section lebel, Data: Alfa Numeric] (Row: 18, Col: 1)\n- Field: आवासीय पता [Type: textarea, Data: Charactar] (Row: 19, Col: 1)\n- Field: जिला [Type: drop down, Data: Alfa Numeric] (Row: 19, Col: 2)\n- Field: गाँव /शहर [Type: text, Data: Alfa Numeric] (Row: 20, Col: 1)\n- Field: तहसील [Type: drop down, Data: Alfa Numeric] (Row: 20, Col: 2)\n- Field: पिन कोड [Type: text, Data: Alfa Numeric] (Row: 21, Col: 1)\n\n\n==================================================\nEXTRACTED PDF DOCUMENT TEXTS\n==================================================\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- [Document: 201_hi_23842.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\nAffix Photo\n\n--- Page 2 ---\n52 (4) \n \n \nफोटो संलग्न करें\n\n--- [Document: 201_hi_23843.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (7)\n\n--- Page 2 ---\n52 (2)\n\n--- [Document: 201_hi_23848.pdf (DOCUMENT_FORMAT)] ---\n--- Page 1 ---\n52 (8)\n\n--- Page 2 ---\n52 (3)\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "क्या ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नाम परिवर्तन राजपत्र का उपयोग किया जा सकता है?\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       नहीं, नाम परिवर्तन राजपत्र का उपयोग ओबीसी प्रमाण पत्र में नाम सुधारने के लिए नहीं किया जा सकता है। नाम परिवर्तन राजपत्र केवल नाम परिवर्तन के लिए होता है, जबकि प्रमाण पत्र में नाम सुधारने के लिए अलग से आवेदन करना पड़ता है।
       ```
| 50 | `विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा` | 4 | 4 | ✅ MATCH | new_topic | 4.16s |

### Query 50 Details
* **Query**: `विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा`
* **Expected Service ID**: `4`
* **Classified Service ID**: `4`
* **Match Status**: ✅ MATCH
* **Classified Intent**: `new_topic`
* **Resolved English Query**: `The validity period of caste certificate for married women`
* **Resolved Hindi Query**: `विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा`
* **Intermediate English Answer**:
  > Information not available.
* **Intermediate Hindi Answer**:
  > जानकारी उपलब्ध नहीं है।
* **Final Synthesized Response**:
  > जानकारी उपलब्ध नहीं है।

* **LLM Call Trace**:
  1. **Function**: `detect_query_language`
     * **Input**:
       ```json
       "विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा"
       ```
     * **Response**:
       ```json
       hi
       ```
  2. **Function**: `translate_query_to_hindi`
     * **Input**:
       ```json
       "विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा"
       ```
     * **Response**:
       ```json
       विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा
       ```
  3. **Function**: `translate_query_to_english`
     * **Input**:
       ```json
       "विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा"
       ```
     * **Response**:
       ```json
       The validity period of caste certificate for married women
       ```
  4. **Function**: `classify_query_intent`
     * **Input**:
       ```json
       {
         "query": "विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा",
         "recent_history": []
       }
       ```
     * **Response**:
       ```json
       {'intent': 'new_topic', 'resolved_query': 'जाति प्रमाण पत्र की वैधता और समय सीमा', 'topic_summary': ''}
       ```
  5. **Function**: `classify_service`
     * **Input**:
       ```json
       {
         "query": "विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा",
         "use_llm_only": false
       }
       ```
     * **Response**:
       ```json
       {'sno': '2', 'service_id': '4'}
       ```
  6. **Function**: `generate_answer`
     * **Input**:
       ```json
       [
         {
           "role": "system",
           "content": "STRICT ANSWER-ONLY RULE (HIGHEST PRIORITY — READ THIS FIRST):\nYour ENTIRE response must address ONLY the specific question the citizen asked. Adding ANY unrequested information is STRICTLY FORBIDDEN.\n- If asked about fees → respond ONLY with fee details. Do NOT mention documents, eligibility, process, or timelines.\n- If asked about eligibility → respond ONLY with eligibility criteria. Do NOT mention documents, fees, process, or timelines.\n- If asked about documents → respond ONLY with document information. Do NOT mention eligibility, fees, process, or timelines.\n- If asked about timeline/SLA → respond ONLY with the timeline/SLA number. Do NOT list documents, fees, process, or anything else.\n- If asked about how to apply → respond ONLY with application process. Do NOT mention documents, eligibility, fees, or timelines.\n- If asked about a single specific document → answer ONLY about that document. Do NOT list all documents.\n\nBREVITY RULE: A short, precise, focused answer is ALWAYS better than a long one.\n- For single-aspect questions (like \"how many days?\" or \"what is the fee?\"), your answer should be 2-5 lines MAX.\n- NEVER dump the full service overview when only one aspect is asked.\n\nYou are SewaSetu AI Assistant — a polite government services assistant for the Chhattisgarh Sewa Setu portal.\n- LANGUAGE AND SCRIPT RULES: You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet.\n- Be warm, respectful, and citizen-friendly.\n\n- MANDATORY DOCUMENTS: If a citizen asks about bypassing a mandatory document, clearly state 'No, you cannot apply without this document' and guide them on how to obtain it.\n- FEE INTERPRETATION: 'Online Fee/Portal Fee' and 'Kiosk Fee/Center Fee' are ALTERNATIVE payment methods (apply online OR at kiosk), NOT cumulative. Total application fee = fee for ONE method. If the citizen asks about total cost and the required documents mention monetary costs (challans, stamp paper, notarization), mention those as additional costs.\n- STRICT GROUNDING RULE (NO EXTRAPOLATION): You must ONLY answer using the facts directly stated in the ENGLISH SOURCE DOCUMENTS or HINDI SOURCE DOCUMENTS. Do NOT assume, extrapolate, or use external knowledge. If the provided source documents do not contain enough information to answer the user's specific query, you MUST reply EXACTLY with: \"I do not have sufficient information in my records to answer this question. Kripya Sewa Setu portal par check karein.\" (or its equivalent translation based on the query language: \"मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।\" for Hindi, and \"Mere paas is question ka answer dene ke liye records mein पर्याप्त information nahi hai. Kripya Sewa Setu portal par check karein.\" for Hinglish).\n- Ignore any contradictions in conversation history.\n\nFORMATTING: Use markdown with bold text and bullet points. Keep it clean and scannable.\n\nCRITICAL: Never mention 'RAG', 'English Source', 'Hindi Source', 'context', or the synthesis process.\n\n--- ENGLISH SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: SC/ST Certificate\nService ID: 4\nLanguage: EN\nDepartment: Revenue and disaster management Department\nTime Limit / SLA: 22 Days\nContact Details: Sewa Setu Kendra\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: Where to Apply? Sewa Setu Kendra : ₹30.0 Online : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: Residential Proof (Mandatory: No)\n  * Supporting Document 1: Domicile Certificate\n  * Supporting Document 2: Electricity Bill\n  * Supporting Document 3: Ration Card\n  * Supporting Document 4: Telephone Bill\n  * Supporting Document 5: Birth Certificate\n  * Supporting Document 6: Voters Identity Card\n  * Supporting Document 7: Bpl Certificate\n  * Supporting Document 8: Land And House Document\n  * Supporting Document 9: Driving License\n  * Supporting Document 10: Other Documents\n  * Supporting Document 11: Certificate From Ward Member, Local Mla/Mp\n  * Supporting Document 12: Photo Identity Card\n  * Supporting Document 13: Service Certificate Of Father / Guardian\n  * Supporting Document 14: Order Of Involuntary Migration\n  * Supporting Document 15: Domicile Certificate\n- SNo 2: Caste Proof (Mandatory: Yes)\n  * Supporting Document 1: Sc/St Certificate Of Other State\n  * Supporting Document 2: Sc/St Certificate From Sarpanch / Parshad / Mla / Mp\n  * Supporting Document 3: Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo\n  * Supporting Document 4: Father/Guardians Service Certificate/Identity Card\n  * Supporting Document 5: Educational Certificate\n  * Supporting Document 6: Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family\n  * Supporting Document 7: Primary School Certificate\n  * Supporting Document 8: Birth Information Form\n  * Supporting Document 9: Misal\n  * Supporting Document 10: Adhikar Abhilekh\n  * Supporting Document 11: Jamabandi\n  * Supporting Document 12: Census Register Of 1931\n  * Supporting Document 13: Citizen Register Of 1949\n  * Supporting Document 14: Dakhil / Kharij Panji\n  * Supporting Document 15: Disability / Unavailability Proof\n- SNo 3: Affidavit (Mandatory: No)\n  * Supporting Document 1: Affidavit\n- SNo 4: Vanshavali (Mandatory: No)\n  * Supporting Document 1: Vanshavali\n  * Supporting Document 2: Vanshavali 1\n  * Supporting Document 3: Vanshavali 2\n  * Supporting Document 4: Vanshavali 3\n  * Supporting Document 5: Vanshavali 4\n- SNo 5: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)\n  * Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)\n- SNo 6: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)\n  * Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof\n\nAPPLICATION FORM FIELDS:\n- Field: General Details [Type: section lebel, Data: Charactar] (Row: 1, Col: 1)\n- Field: Beneficiary Guardian Type [Type: drop down, Data: Charactar] (Row: 2, Col: 1)\n- Field: Beneficiary Guardian name [Type: text, Data: Charactar] (Row: 2, Col: 2)\n- Field: Beneficiary Guardian Type in English [Type: drop down, Data: Charactar] (Row: 3, Col: 1)\n- Field: Beneficiary Guardian name in English [Type: text, Data: Charactar] (Row: 3, Col: 2)\n- Field: Gender [Type: drop down, Data: Charactar] (Row: 4, Col: 1)\n- Field: Marital Status [Type: drop down, Data: Charactar] (Row: 4, Col: 2)\n- Field: Date of Birth [Type: date, Data: Date] (Row: 5, Col: 1)\n- Field: Relation to Applicant [Type: drop down, Data: Charactar] (Row: 5, Col: 2)\n- Field: Caste STSC [Type: search, Data: Search] (Row: 6, Col: 1)\n- Field: Category [Type: text, Data: Charactar] (Row: 6, Col: 2)\n- Field: Caste In English [Type: text, Data: Charactar] (Row: 7, Col: 1)\n- Field: Category In English [Type: text, Data: Charactar] (Row: 7, Col: 2)\n- Field: Category Number [Type: text, Data: Charactar] (Row: 8, Col: 1)\n- Field: Beneficiary name in English [Type: text, Data: Charactar] (Row: 8, Col: 2)\n- Field: Present Address of Applicant [Type: section lebel, Data: Charactar] (Row: 9, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 10, Col: 1)\n- Field: PIN Code [Type: text, Data: Number] (Row: 10, Col: 2)\n- Field: Post Box Number [Type: text, Data: Alfa Numeric] (Row: 11, Col: 1)\n- Field: District [Type: drop down, Data: Charactar] (Row: 11, Col: 2)\n- Field: Address In English [Type: textarea, Data: Alfa Numeric] (Row: 12, Col: 1)\n- Field: Is Present Address and Permanent Address is same [Type: drop down, Data: Charactar] (Row: 12, Col: 2)\n- Field: Permanent Address of Applicant [Type: section lebel, Data: Charactar] (Row: 13, Col: 1)\n- Field: Address [Type: textarea, Data: Alfa Numeric] (Row: 14, Col: 1)\n- Field: PIN Code [Type: text, Data: Number\n\n--- Source 2: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: तररक्त और कोई शुल्क देय नहीं है।\n\n--- Page 14 ---\nिरण 9: पावर्ी सुरक्षिर् रखना \nआवेदन सफितापूवटक जमा होने क े  पश्चात् पावती जेनरेट होती है। इसमें आवेदन संदभा क्रमांक देखा जा सकता \nहै। इस पावती का क्रप्रिंट आउट िेकर सुरलित रखें। \n \nचित्र क्रमाांक 20 \nआवेदन संदभा क्रमांक की सहायता से आवेदन की स्थस्थतत छत्तीसगढ़ ई-डिस्ट्रिक्ट क े  पोटटि पर देखी जा सकती \nहै। \n \nउपयोगी जानकारी: \n• आवेदन जमा करने क े  बाद डनधाटररत 22 क्रदऩों की समय-सीमा क े  अ ां दर आवेदन का डनराकरण कर क्रदया जाता है। \n• ई-डिस्ट्रिक्ट पोटटि पर आवेदन की स्थस्थतत देखी जा सकती है। \n• अनुसूचित जातत अथवा जनजातत प्रमाण पत्र जारी होने क े  उपराांत इसकी डिचजटि प्रतत ई-डिस्ट्रिक्ट पोटटि से िाउनिोि की \nजा सकती है।\n\n--- [Document: 4_en_citizenCharter.pdf (SLA_DETAILS)] ---\nGovernment of Chhattisgarh\nRevenue and Disaster Management Department\nMantralaya\nMahanadi Bhawan, Naya Raipur\n::: Notification :::\n\nRaipur, Date: 16/05/2013\n\nNo. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\nTable (SLA Details):\n1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Competent Authority: Collector (कलेक्टर)\n   - Appellate Authority: Commissioner (कमिशनर)\n\n3. Domicile Certificate (निवास प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and\n\n--- Source 3: [Official Specification (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: combined_manual\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nCombined Manual Content: �ारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\n4. Income Certificate (आय प्रमाण-पत्र):\n   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n   - Time Limit for Service Delivery (Working Days): 30 Working Days\n   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n   - Appellate Authority: Collector (कलेक्टर)\n\nBy order and in the name of the Governor of Chhattisgarh,\n(P. Nihalani)\nJoint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department\n\n--- Source 4: [User Manual (English)] ---\nService: SC/ST Certificate (ID: 4)\nSection: official_document\nContent:\nService: SC/ST Certificate\nDepartment: Revenue and disaster management Department\nOfficial Document Content: --- Page 1 (no rotation needed) ---\n148\nTHE CONSTITUTION (SCHEDULED CASTES) ORDER, १९५० C.0. 19\nIn exercise of the powers conferred by clause (l) of article ३४१ of the Constitution of India, the President, after consultation with the Governors and Rajpramukhs of the States concerned, is pleased to make the following Order, namelyः\n1. This Order may be called the Constitution (Scheduled Castes) Order, १९५०.\n2\nSubject to the provisions of this Order, the castes, races or tribes 0r parts of, or groups within, castes or tribes specified in Parts to JXXIVJJ of the Schedule to this Order shall, in relation to the States to which those Parts respectively relate, be deemed to be Scheduled Castes so far as regards member thereof resident in the localities specified in relation to them in those Parts of that Schedule.\nA[३. Notwithstanding anything contained in paragraph 2, no person who professes ० religion different from the Hindu SL, the Sikh 0f the Buddhist] religion shall be deemed to be a member of १ Scheduled Caste ]\n6[4. +ny reference in this Order to a State or to ० district or other territorial division thereof shall be construed as 0 reference to the State, district or other territorial division as constituted on the lst day of Ma , 1976.]\n१. Published with the Ministry of Law Notification No SR.0 ३८५ , dated the lOth August, १९५०, Gazette of India, Extraordinary, १९५०, Part I[ Section 3 , page 1६३. २. Subs by the Scheduled Castes and Scheduled Tribes Lists ( Modification) Order, 1९५६. 3 The figure XYI has been successfully subs. by Act 18८ of 1९८७, $ १९ and Ist Sch. (we.f. 30.5.87), by Act २८ of २०००, $ १9 and ३rd Sch ( W.e.f. 1.11.2००0) and by Act २९ of २००० , 5. २४ and Sth Sch (w.e.f. 9.१1 २OO०) to read as above. ४. Subs. by Act 6३ of 1९५६, S. 3 and First Sch. for paragraph 3 5. Subs. by Act 1५ of १९९०, S. २, for \"or the Sikh\" 6. Subs by Act १०8 of १९७६, S. 3 and the First Sch., for paragraph ४ (w.e.f. 27-7-1977).\n\n--- Page 2 (no rotation needed) ---\n149\nConstitution (Scheduled Castes) Order, १९५० PART IlL. Rules and Orders under the Constitution )\nI[THE SCHEDULE PART L Andhra Pradesh\n1 Adi Andhra 31. Madasi Kuruva, Madari Kuruva 2 Adi Dravida 3२ Madiga 3. Anamuk 33. Madiga Dasu, Mashteen 4 Fray Mala 34. Mahar 5. Arundhatiya २[३5. Mala, Mala Ayawaru] 6 Arwa Mala 36. Mala Dasari 7. Bariki 37. Mala Dasu 8 Bavuri 38. Mala Hannai 2[9 . Beda (Budga) Jangam (in the districts of Hyderabad, Ranga 39. Malajangam Reddy, Mahbubnagar, Adilabad, Nizamabad, Medak, 40. Mala Masti Karimnagar, Warangal, Khammam and Nalgonda)] 41. Mala Sale, Nethani १०. Bindla 42. Mala Sanyasi २[१1. Byagara, Byagari] ४३. Mang १२. Chachati 44 Mang Garodi १३. Chalavadi 45. Manne २[1४. Chamar, Mochi, Muchi, Chamar Ravidas, Chamar Rohidas] 46. Mashti १५. Chambhar ४७. Matangi 16. Chandala 48. Mehtar 17. Dakkal, Dokkalwar 49. Mitha Ayyalvar 18. Dandasi 50. Mundala 19. Dhor ५१. Paky, Moti, Thoti 20. Dom, Dombara, Paidi, Pano २१. Ellamalawar, Yellammalawandlu 22. Ghasi, Haddi, Relli, Chanchandi 53. Pamidi २[२३. Godagali, Godagula (in the districts of Srikakulam, 54. Panchama, Pariah Vizianagaram and Vishakhapatanam)] 55. Relli 24. Godari 56. Samagara २५. Gosangi 57. Samban २६. Holeya 58. Sapru २७. Holeya Dasari 59. Sindhollu, Chindollu २८. Jaggali ४[60. Yatala 29. Jambuvulu ६१ . Valluvan. ] २[३0. Kolupulvandlu, Pambada, Pambanda, Pambala]\nPART IL. Assam\n1 Bansphor 2 Bhuinmali, Mali 3 Brittial Bania, Bania 4 Bhupi, Dhobi 5. Dugla, Dholi 6 Hira 7. Jalkeot 8 Jhalo, Malo, Jhalo Malo\n9 Kaibartta, Jaliya १०. Lalbegi 11. Mahara 1२ Mehtar, Bhangi 13. Muchi, Rishi 14. Namasudra 15. Patni 16. Sutradhar.\n1. Subs by Act १०८\n\n--- END ENGLISH SOURCE DOCUMENTS ---\n\n--- HINDI SOURCE DOCUMENTS ---\n--- Source 1: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: ==================================================\nSERVICE DETAILS MANUAL: अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र\nService ID: 4\nLanguage: HI\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nTime Limit / SLA: 22 दिन\nContact Details: सेवा सेतु केंद्र\nKiosk Fee: 30.0\nOnline Fee: 30.0\nWhere to Apply: \nRaw Fees Text: आवेदन कहाँ करें? सेवा सेतु केंद्र : ₹30.0 ऑनलाइन : ₹30.0\nHow to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=hi\n==================================================\n\nREQUIRED DOCUMENTS:\n- SNo 1: निवास का प्रमाण (Mandatory: नहीं)\n  * Supporting Document 1: मूल निवासी प्रमाण पत्र\n  * Supporting Document 2: बिजली का बिल\n  * Supporting Document 3: राशन कार्ड\n  * Supporting Document 4: टेलीफोन बिल\n  * Supporting Document 5: जन्म प्रमाण पत्र\n  * Supporting Document 6: वोटिंग कार्ड\n  * Supporting Document 7: बी.पी.एल. प्रमाण पत्र\n  * Supporting Document 8: घर या भूमि का दस्तावेज़\n  * Supporting Document 9: ड्राइविंग लाइसेंस\n  * Supporting Document 10: अन्य\n  * Supporting Document 11: वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र\n  * Supporting Document 12: फोटो परिचय पत्र\n  * Supporting Document 13: पिता / पालक की नौकरी का प्रमाण - पत्र\n  * Supporting Document 14: अनैच्छिक प्रवजन का आदेश\n  * Supporting Document 15: मूल निवासी प्रमाण पत्र\n- SNo 2: जाति का प्रमाण (Mandatory: हाँ)\n  * Supporting Document 1: अन्य राज्य के अनुसूचित जाति / जनजाति प्रमाणपत्र\n  * Supporting Document 2: सरपंच / पार्षद / विधायक / साँसद से जाति प्रमाण-पत्र\n  * Supporting Document 3: प्राथमिक शाला या जिला शिक्षा अधिकारी द्वारा प्रमाणित प्राथमिक शाला द्वारा जारी स्थानान्तरण प्रमाण-पत्र\n  * Supporting Document 4: पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र\n  * Supporting Document 5: शैक्षणिक प्रमाण पत्र\n  * Supporting Document 6: आवेदक को या उसके किसी परिवारजन को जारी हुआ जाति प्रमाण पत्र\n  * Supporting Document 7: प्राथमिक परीक्षा उत्तीर्ण प्रमाण-पत्र\n  * Supporting Document 8: जन्म सूचना प्रपत्र\n  * Supporting Document 9: मिसल\n  * Supporting Document 10: अधिकार अभिलेख\n  * Supporting Document 11: जमाबंदी\n  * Supporting Document 12: १९३१ का जनगणना पंजी\n  * Supporting Document 13: 1949 का नागरिक पंजी\n  * Supporting Document 14: दाखिल / ख़ारिज पंजी\n  * Supporting Document 15: असमर्थता / अनुपलब्धता का प्रमाण\n- SNo 3: शपथ पत्र (Mandatory: नहीं)\n  * Supporting Document 1: शपथ पत्र\n- SNo 4: वंशावली (Mandatory: नहीं)\n  * Supporting Document 1: वंशावली\n  * Supporting Document 2: वंशावली १\n  * Supporting Document 3: वंशावली २\n  * Supporting Document 4: वंशावली ४\n  * Supporting Document 5: वंशावली 3\n- SNo 5: ग्राम सभा प्रस्ताव(ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory: नहीं)\n  * Supporting Document\n\n--- Source 2: [Official Specification (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: combined_manual\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nCombined Manual Content: �पुर\n::: अधिसूचना :::\n\nरायपुर, दिनांक 16/05/2013\n\nक्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\nसारणी (SLA Details):\n1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n2. स्थाई जाति प्रमाण-पत्र (Permanent Caste Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - सक्षम प्राधिकारी: कलेक्टर\n   - अपीलीय अधिकारी: कमिश्नर\n\n3. निवास प्रमाण-पत्र (Domicile Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\n4. आय प्रमाण-पत्र (Income Certificate):\n   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n   - अपीलीय अधिकारी: कलेक्टर\n\nछत्तीसगढ़ के राज्यपाल के नाम से तथा आदेशानुसार\n(पी. निहलानी)\nसंयुक्त सचिव, छत्तीसगढ\n\n--- Source 3: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ्तावेजों के अतिरिक्त स्थानीय संस्थाओं यथा ग्राम पंचायत्त जनपद पंचायत जिला पंचायत नगर पंचायतः नगर पाालका तथा नगर पालिक निगम॰ क दस्तावेजों की भी जॉच कर सकगा ।\n(३ जॉचकर्ता अधिकारी ग्राम कोटवार ग्राम सरपंच हल्का पटवारी स्थानीय पर्षद॰ क्षेत्र के अन्य जनप्रतिनिधियों वहां क रहने वाले राजपत्रित अधिकारियों ऐसे स्थानीय सदस्यों जो उस॰ जाति क पहले से प्रमाणपत्रधारी हैं नथा आवेदक को भली- भॉति ज़ानते हैं॰ क मौखिक कथन भी साक्ष्य के रूप में अभिलिखित कर सकेगा ।\nजॉचकर्ता अधिकारी जहॉ वह स्वयं सक्षम प्राधिकारी नहीं है जॉच उयरांतं दस्तावजी साक्ष्यों एव अभिलिखित किए गए मौखिक कथनों क साथ अपना लिखित प्रतिवेदन स्पष्ट निष्कष क साथ जॉच आदेश प्राप्त हाने के १५ दिवस क भीतर सक्षम प्राधिकारी को प्रस्तुत करेगा ।\n#l फ :\nशा7\n} १ `\n*{*;\n\n--- Page 6 (no rotation needed) ---\n788=\nछत्तीसगढ़ राजपत्र , दिनांक 2 सितम्बर २०१३\n9\nसागाजिक प्रास्थिति प्रमाणपत्र सक्षम प्राधिकारी. नियम 3 के उप-नियम १) क अधीन आवेदन पत्र प्राप्त होने पर नियभ 8 क अधीन जॉच कर और जहॉं वह स्वंयं जॉचकर्ता अधिकारी नहीं है॰ जॉचकर्ता अधिकारी के प्रतिवेदन एवं संलग्न दस्तावेजों से स्वयं संतुष्ट होने के उपरांत आवेदन की प्राप्ति क एक माह के अंदर अनुसूचित जाति के आवेदक को प्ररूप ४क १) में अनुसूचित जनजाति के आवेदक को प्ररूप ४क २) में तथा अन्य पिछड़ा वर्ग क़ आवेदक को प्ररूप ४क ३) में प्रमाणपत्र जारी करेगा। +0: अस्थायी प्रमाणपत्र - (१ कक्षा दसवीं तक शेक्षणिक संस्थान में प्रवेश प्राप्त क़रने के प्रयोजन क लिए अथवा ऐसे स्तर पर छात्रवृत्ति अथवा शिष्यवृत्ति प्रदान करने हेतु अंथवा ऐसे अन्य प्रयोजनों हेतु जिहां बड़ी़ संख्या में प्रमाणपत्र की अपरिहार्यता है एवॅं ऐसे प्रमाणपत्र यथा समय जारी किया जाना संभव नहीं है॰ त\n\n--- Source 4: [User Manual (Hindi)] ---\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4)\nSection: official_document\nContent:\nService: अनुसूचित जाति/जनजाति प्रमाण पत्र\nDepartment: राजस्व एवं आपदा प्रबंधन विभाग\nOfficial Document Content: ा ऐसे स्तर पर छात्रवृत्ति अथवा शिष्यवृत्ति प्रदान करने हेतु अंथवा ऐसे अन्य प्रयोजनों हेतु जिहां बड़ी़ संख्या में प्रमाणपत्र की अपरिहार्यता है एवॅं ऐसे प्रमाणपत्र यथा समय जारी किया जाना संभव नहीं है॰ तो आवेदक क द्वारा प्ररूप २क में दिए गए शपथ पत्र क आधार पर सक्षम प्राधिकारी प्ररूप ४ख में॰ आवेदन की तिथि से पन्द्रह दिवस क अंदर अस्थायी प्रमाणपत्र जारी कर सकेगाः\nपरन्तु सक्षम प्राधिकारी प्ररूप 5ख में जारी अस्थरायी प्रमाणपत्र का विवरण संधारित करेगा । (२ अस्थायी. प्रमाणपत्र कंवल छः माह की अवधि के लिए अथवा स्थाई प्रमाण पत्र जारी होने की तिथि॰ जो मी पहले हो तक क लिए वैध होगा । अन्य. राज्य से छत्तीसगढ़ राज्य में प्रवासित आवेदक के लिए प्रमाणपत्र.- ऐसे मामले में जहां आवेदक अन्य राज्यों 7 प्रवासी हो, सक्षम अधकार 7 राज्य म॰ र्यादै आवश्यक हो॰ तो संबंधित राज्य क जिला मजिस्ट्रेट या सत्यापन समिति या सतर्कता प्रकोष्ठ के माध्यम से उसकी सामाजिक प्रास्थिति क संबंध में विस्तृत जाँच पड़ताल करने के उपरांत प्ररूप ४ग में प्रमाण पत्र जारी करेगाः परन्तु ऐसे प्रमाणपत्र धारक उस राज्य जिससे वह प्रवासित है॰ में यथास्थिति अनुसूचित जाति अनुसूचित जनजाति अथवा अन्य पिछड़ा वर्ग को प्रदत्त सुविधाओं का लाभ लेने के लिए पात्र होंगे । अस्तेच्छिक प्रवास- अविगाजित मध्यप्रदेश कें शासकीय सेवक तथा निगम॰ आथोग मण्डल एवं सार्वजनिक उपकन के ऐसे अन्य अधिकारी एवं कर्मचारीगण जो भध्यप्रदेश पुनर्गठन अधिनियम २००० मांक २८ सन् २०००) क अधीन मध्यप्रदेश राज्य \"्वं छत्तासगढ़ राज्य के बींच कैडर विभाजन के फलस्चरूप छत्तीसगढ़ राज्य में आवंटित हुये हैं॰ ऐसे कर्मचारी तथाः उनके परिवार के सदस्य यदि दे ७त्तीरगढ राज्य गें अनुसूंचेत जाति अथवा अनुसूचित जनजात्ति अथ\n\n--- END HINDI SOURCE DOCUMENTS ---\n"
         },
         {
           "role": "user",
           "content": "विवाहित महिलाओं के लिए जाति प्रमाण पत्र की वैधता समय सीमा\n\nIMPORTANT: You MUST respond ENTIRELY in Hindi. You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि).\n- Do NOT write in English or use Roman alphabet/Latin characters (a-z, A-Z).\n- Every single word must be written in Devanagari.\n- If the reference context contains English terms (such as 'affidavit', 'SC/ST certificate', 'mandatory', 'optional'), you MUST translate them to Hindi Devanagari (e.g. 'शपथ पत्र', 'एससी/एसटी प्रमाणपत्र', 'अनिवार्य', 'वैकल्पिक') in your final output. Do NOT leave English words in the Roman alphabet."
         }
       ]
       ```
     * **Response**:
       ```json
       जाति प्रमाण पत्र की वैधता अवधि सामान्यतः 5 वर्ष होती है। हालांकि, विवाहित महिलाओं के लिए यह वैधता अवधि राज्य सरकार के नियमों पर निर्भर करती है। कुछ राज्यों में विवाह के बाद प्रमाण पत्र की वैधता समाप्त हो सकती है, जबकि अन्य में यह 5 वर्ष तक बनी रहती है।
       
       सेवा सेतु पोर्टल पर इस संबंध में विशिष्ट जानकारी उपलब्ध नहीं है। आपको संबंधित विभाग से संपर्क करना चाहिए या आधिकारिक वेबसाइट पर जांच करनी चाहिए।
       ```

## Summary Metrics
- Total Test Cases: 50
- Passed Matches: 44
- Accuracy: 88.00%
