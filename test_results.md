# SewaSetu RAG API Server Validation - 50 Test Queries

This report details the progressive execution and validation of **50 test queries** covering basic inquiries, complex service jurisdiction and criteria logic, and out-of-scope requests, across English, Hindi, and Hinglish.

## Execution Summary (Progressive)
* **Total Queries Configured:** 50
* **Queries Executed So Far:** 50 / 50
* **Completed Successfully So Far:** 50
* **Average Time per Query So Far:** 5.94s
* **Last Updated:** 2026-07-01 16:42:52

---

## Detailed Test Log

### Query #1
* **Category:** Basic Info
* **Input Language:** English
* **Input Query:** `What are the documents needed for Domicile Certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `9.41s`

**Bot Response:**
Based on the information provided, here are the documents required for a Domicile Certificate in Chhattisgarh:

**Mandatory Documents:**

1.  **Affidavit**
    *   A sworn statement is required.

2.  **Proof of At Least 15 Years Stay**
    *   You must provide at least one of the following:
        *   Birth Certificate
        *   Father/Guardian Service Certificate
        *   Job Service Certificate / Identity Card (if the applicant is under government/semi-government)
        *   Voter's Identity Card
        *   Land and House Document
        *   Birth Information Form
        *   Certificate From Ward Member, Local MLA/MP
        *   Ration Card
        *   Electricity Bill

3.  **Educational Certificate**
        *   Middle School Certificate - 8th Standard
        *   Primary School Certificate - 5th Standard
        *   High School (10th) Certificate
        *   Higher Secondary School Certificate (12th)
        *   M.Phil/D.Lit./Ph.D. Certificate
        *   School Certificate (as a proof of 3 years continuous study)
        *   Post Graduation Certificate
        *   Certificate in Technical Subjects

**Optional Documents:**

*   **Proof of At Least 5 Years Stay**
    *   This is optional. You can provide:
        *   Person's Service Book.

**Important Notes:**

*   The minimum one proof of residence and one educational certificate are mandatory if you choose to provide them.
*   Documents marked as optional can be provided but are not required.
*   The file size for uploaded documents should not exceed 750kb.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #2
* **Category:** Basic Info
* **Input Language:** Hindi
* **Input Query:** `मूल निवासी प्रमाण पत्र के लिए कौन से दस्तावेज चाहिए?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `5.61s`

**Bot Response:**
मूल निवासी प्रमाण पत्र के लिए निम्नलिखित दस्तावेज आवश्यक हैं:

**अनिवार्य दस्तावेज:**

1. **शपथ पत्र** (अनिवार्य)
   - आवेदक द्वारा शपथ पत्र देना अनिवार्य है।

2. **15 वर्ष तक निवास का प्रमाण** (अनिवार्य)
   - जन्म प्रमाण पत्र
   - पिता/पालक का सेवा प्रमाण पत्र
   - रोजगार प्रमाणपत्र / पहचान पत्र (यदि सरकारी/अर्ध-सरकारी कर्मचारी हो)
   - वोटिंग कार्ड
   - घर या भूमि का दस्तावेज
   - जन्म सूचना प्रपत्र
   - वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र
   - राशन कार्ड
   - बिजली का बिल

3. **शैक्षणिक प्रमाण पत्र** (अनिवार्य)
   - माध्यमिक विद्यालय का प्रमाणपत्र - 8वीं कक्षा
   - प्राथमिक विद्यालय का प्रमाणपत्र - 5वीं कक्षा
   - हाई स्कूल (10वीं कक्षा) अंकसूची
   - उच्चतर माध्यमिक विधालय प्रमाण पत्र (12वीं कक्षा)
   - एम-फिल
   - स्कूल प्रमाणपत्र (3 साल की एक साक्ष्य निरंतर अध्ययन के रूप में)
   - स्नातकोत्तर प्रमाणपत्र
   - तकनीकी विषयों में प्रमाणपत्र

**वैकल्पिक दस्तावेज:**

1. **5 वर्ष निवास का प्रमाण** (अनिवार्य नहीं)
   - व्यक्ति की सेवा पुस्तिका

**नोट:** तारांकित (*) चिन्हित दस्तावेज अनिवार्य हैं। हैश (#) चिन्हित दस्तावेजों में निवास का न्यूनतम एक प्रमाण और शैक्षणिक प्रमाण पत्र प्रस्तुत करना अनिवार्य है। फाइल का अधिकतम आकार 750kb होना चाहिए।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

---

### Query #3
* **Category:** Basic Info
* **Input Language:** Hinglish
* **Input Query:** `domicile certificate ki list of documents kya hai?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `7.86s`

**Bot Response:**
Haan, aapke liye domicile certificate ke documents ki list yahan di gayi hai:

**15 saal ke residence proof ke liye documents:**

*   Janm praman patra (Birth Certificate)
*   Pitaji/Palak ka seva praman patra (Father/Guardian Service Certificate)
*   Udyog praman patra / Pehchan patra (If you are a government/semi-government employee)
*   Matdaan card (Voter ID Card)
*   Ghar ya zameen ka document (Land and House Document)
*   Janm jankari form (Birth Information Form)
*   Ward member, local MLA/MP se praman patra (Certificate from Ward Member, Local MLA/MP)
*   Ration card (Ration Card)
*   Bijli ka bill (Electricity Bill)

**Educational certificate ke liye documents:**

*   Madhyamik school praman patra (8th Standard)
*   Prathmik school praman patra (5th Standard)
*   High school (10th) ki ank-patti (10th Class Marksheet)
*   Uchchatar madhyamik vidyalaya praman patra (12th Class)
*   M.Phil/D.Lit./Ph.D. praman patra
*   School praman patra (3 saal ke continuous study ke proof ke liye)
*   Post graduation praman patra (Post Graduation Certificate)
*   Technical subjects mein praman patra (Certificate in Technical Subjects)

**Important points:**

*   Kam se kam ek residence proof aur ek educational certificate zaroori hai.
*   Agar aapke paas upar diye gaye documents nahi hain, toh aap alternative documents use kar sakte hain.
*   Documents ki maximum size 750kb tak ho sakti hai.
*   Jo documents asterisk (*) se mark hain, woh mandatory hain.
*   Jo documents hash (#) se mark hain, unmein kam se kam ek residence proof aur ek educational certificate hona zaroori hai.

Agar aapke paas koi specific document ke baare mein aur jaankari chahiye, toh please poochiye.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #4
* **Category:** Basic Info
* **Input Language:** English
* **Input Query:** `What is the fee for OBC Certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `5`
* **Response Latency:** `3.60s`

**Bot Response:**
Based on the information provided, the fee for an OBC Certificate is ₹30.0.

This fee is applicable for both in-person application at a Sewa Setu Kendra and online application.

Additionally, you can upload up to five scanned documents for free. Any additional documents beyond this limit may incur extra charges, though the specific details for such charges are not provided in the given context.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

---

### Query #5
* **Category:** Basic Info
* **Input Language:** Hindi
* **Input Query:** `अन्य पिछड़ा वर्ग प्रमाण पत्र की फीस कितनी है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `5`
* **Response Latency:** `4.58s`

**Bot Response:**
अन्य पिछड़ा वर्ग (ओबीसी) प्रमाण पत्र की फीस 30.0 रुपये है। यह फीस सेवा सेतु केंद्र और ऑनलाइन, दोनों माध्यमों से जमा की जा सकती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)

---

### Query #6
* **Category:** Basic Info
* **Input Language:** Hinglish
* **Input Query:** `obc certificate apply karne ka charge kitna hai?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `5`
* **Response Latency:** `6.90s`

**Bot Response:**
Haan, aapke sawal ka jawab deta hun.

OBC certificate apply karne ka charge ₹30.0 hai.

Yeh charge dono tarah se apply hota hai:
- Sewa Setu Kendra mein apply karne par
- Online apply karne par

Koi aur extra charge nahi lagta. Aap online apply kar sakte hain: https://sewasetu.cgstate.gov.in/home?lang=hi

Koi aur jaankari chahiye toh bataiye.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

---

### Query #7
* **Category:** Basic Info
* **Input Language:** English
* **Input Query:** `How many days does it take to get a Marriage Certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `3`
* **Response Latency:** `4.09s`

**Bot Response:**
Based on the information provided, it takes 15 days to get a marriage registration and certificate.

The processing time for marriage registration and certificate issuance is 15 days as per the official guidelines of the Seva Setu portal.

You can track the status of your application online using the receipt generated after successful submission. The application status can be monitored on the e-Sankirt portal. After the marriage is registered and the certificate is issued, you can also track its physical progress through the same portal.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

---

### Query #8
* **Category:** Basic Info
* **Input Language:** Hindi
* **Input Query:** `विवाह प्रमाण पत्र मिलने में कितने दिन का समय लगता है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `3`
* **Response Latency:** `5.15s`

**Bot Response:**
विवाह पंजीकरण और प्रमाण पत्र प्राप्त करने में 15 दिन का समय लगता है। यह जानकारी सेवा सेतु पोर्टल के आधिकारिक दिशा-निर्देशों के अनुसार है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)

---

### Query #9
* **Category:** Basic Info
* **Input Language:** Hinglish
* **Input Query:** `marriage registration certificate kitne din me milta hai?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `3`
* **Response Latency:** `3.76s`

**Bot Response:**
Haan, aapko marriage registration certificate 15 din ke andar mil jaata hai. Ye service level agreement (SLA) ke hisaab se hai. Agar aap online apply karte hain, toh certificate aapke registered email ya mobile number par bhi mil sakta hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

---

### Query #10
* **Category:** Basic Info
* **Input Language:** English
* **Input Query:** `Who is the issuing authority for SC/ST Certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `5.44s`

**Bot Response:**
Based on the information provided, the issuing authority for the SC/ST Certificate is the Department of Revenue and Disaster Management, Government of Chhattisgarh.

The process involves submitting your application to the Tehsil Office, where the Sub-Divisional Officer (Revenue) serves as the competent authority for most cases.

If you need further details about the specific process or authority for your application, please let me know. I can provide more information based on the context.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

---

### Query #11
* **Category:** Basic Info
* **Input Language:** Hindi
* **Input Query:** `अनुसूचित जाति प्रमाण पत्र कौन जारी करता है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `5.03s`

**Bot Response:**
अनुसूचित जाति प्रमाण पत्र का जारीकर्ता सक्षम प्राधिकारी होता है। यह प्रमाण पत्र राजस्व एवं आपदा प्रबंधन विभाग, छत्तीसगढ़ द्वारा जारी किया जाता है।

**विभिन्न पदों पर जारी होने वाले प्रमाण पत्र:**

*   **स्थायी प्रमाण पत्र:** इसके लिए सक्षम प्राधिकारी कलेक्टर होता है।
*   **अस्थायी प्रमाण पत्र:** इसके लिए सक्षम प्राधिकारी उप-मंडल अधिकारी (राजस्व) होता है।
*   **प्रवासी आवेदकों के लिए:** इसके लिए संबंधित राज्य के जिला मजिस्ट्रेट या सत्यापन समिति के माध्यम से प्रमाण पत्र जारी किया जाता है।

**प्रक्रिया:**
1.  आवेदक सक्षम प्राधिकारी को आवेदन प्रस्तुत करता है।
2.  आवेदक की सामाजिक स्थिति की जांच की जाती है।
3.  जांच के पश्चात, प्रमाण पत्र जारी किया जाता है।

**विशेष बिंदु:**
*   प्रमाण पत्र का जारी होना अनिवार्य है, विशेषकर उन स्थितियों में जहाँ बड़ी संख्या में प्रमाण पत्रों की आवश्यकता होती है।
*   प्रमाण पत्र की वैधता 6 महीने तक होती है, या जब तक स्थायी प्रमाण पत्र जारी न हो जाए।
*   अस्थायी प्रमाण पत्र के लिए 15 दिन के भीतर प्रमाण पत्र जारी किया जा सकता है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

---

### Query #12
* **Category:** Basic Info
* **Input Language:** Hinglish
* **Input Query:** `sc certificate kiske dwara issue kiya jata hai?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `3.90s`

**Bot Response:**
SC certificate Chhattisgarh ke Revenue aur Disaster Management Department dwara issue kiya jata hai.

Iske liye ye authorities hain:
- Tehsildar / Naib Tehsildar (temporary certificate ke liye)
- Sub-Divisional Officer (Revenue) (permanent certificate ke liye)
- Collector (permanent certificate ke liye)

Ye certificate Chhattisgarh e-District portal (cgedistrict.cgstate.gov.in) par bhi mil sakta hai ya Sewa Setu Kendra se bhi le sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

---

### Query #13
* **Category:** Basic Info
* **Input Language:** English
* **Input Query:** `Where can I apply for Name Change in Gazette?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `201`
* **Response Latency:** `5.77s`

**Bot Response:**
Based on the information provided, you can apply for a Name Change in Gazette through the following methods:

**Where to Apply:**
- **Sewa Setu Kendra:** This is the physical location where you can submit your application.
- **Online:** You can also apply through the official Sewa Setu portal.

**Application Fee:**
- The fee for both the Sewa Setu Kendra and online application is ₹30.0.

**How to Apply Online:**
- You can access the online application form at: https://sewasetu.cgstate.gov.in/home?lang=en

**Important Note on Documents:**
The context lists several required documents for the application, including:
- A challan of ₹430/- from any State Bank of India branch
- A notarized affidavit in Form-III on a ₹50 non-judicial stamp paper
- The original copy of the publication of the notice for name change in Form-I in a local newspaper
- The original copy of the deed form in Form-II with the names, signatures, and addresses of two witnesses
- Old name and new name verification document
- All types of documents/identity cards/IDs mentioned in the affidavit
- Identity card of the applicant issued by the government
- Identity card of witnesses issued by the government

Please note that the context does not specify the exact process for obtaining these documents, only that they are required for the application.

For the most accurate and up-to-date information, it is recommended to visit the Sewa Setu Kendra or the official portal mentioned above.

**Seva Sanchar Kendras:**
- These are available at:
  - Municipal Corporation or Municipality in urban areas
  - Gram Panchayat in rural areas

You can apply online through Seva Sanchar Kendra. The application fee is Rs. 30, which has to be paid through both online and offline modes.

The time limit for the application is 29 days. You can complete the application process on the Seva Sanchar portal.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

---

### Query #14
* **Category:** Basic Info
* **Input Language:** Hindi
* **Input Query:** `नाम परिवर्तन के लिए आवेदन कहाँ करना होगा?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `201`
* **Response Latency:** `3.62s`

**Bot Response:**
नाम परिवर्तन के लिए आपको निम्नलिखित स्थानों पर आवेदन करना होगा:

**सेवा सेतु केंद्र**
- आप सेवा सेतु केंद्र में व्यक्तिगत रूप से आवेदन कर सकते हैं।

**ऑनलाइन**
- आप ऑनलाइन पोर्टल के माध्यम से भी आवेदन कर सकते हैं।
- इसके लिए आधिकारिक वेबसाइट पर जाएं: https://sewasetu.cgstate.gov.in/home?lang=hi

सेवा सेतु केंद्र पर आवेदन करने के लिए ₹30.0 शुल्क है, और ऑनलाइन आवेदन के लिए भी ₹30.0 शुल्क है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)

---

### Query #15
* **Category:** Basic Info
* **Input Language:** Hinglish
* **Input Query:** `name change gazette notification kaha se apply kare?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `201`
* **Response Latency:** `5.55s`

**Bot Response:**
Haan, aapke liye name change gazette notification apply karne ke do tarike hain:

**Offline Application:**
- Aap nearest Sewa Setu Kendra ja sakte hain
- Wahan se application form milega

**Online Application:**
- Official website par ja sakte hain: https://sewasetu.cgstate.gov.in/home?lang=hi
- Yahan se online apply kar sakte hain

Dono methods mein Rs. 30.00 ka fee lagega. Online process mein aapko Rs. 430 ka challan aur Rs. 50 ka stamp paper bhi chahiye hoga.

Kya aap kisi specific method ke baare mein aur jaankari chahte hain?

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)

---

### Query #16
* **Category:** Basic Info
* **Input Language:** English
* **Input Query:** `What is the validity of Domicile Certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `3.52s`

**Bot Response:**
Based on the information provided, the validity of a Domicile Certificate is 30 working days.

This certificate is issued by the Department of Revenue and Disaster Management and is obtained by applying at the Seva Bridge Center.

For any other questions or more detailed information, please feel free to ask.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #17
* **Category:** Basic Info
* **Input Language:** Hindi
* **Input Query:** `मूल निवासी प्रमाण पत्र की वैधता कितनी होती है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `6.38s`

**Bot Response:**
मूल निवासी प्रमाण पत्र की वैधता 10 वर्ष होती है। यह प्रमाण पत्र आवेदक के निवास के आधार पर जारी किया जाता है, और इसकी वैधता अवधि सेवा सेतु केंद्र या ऑनलाइन पोर्टल के माध्यम से जारी करने की तिथि से शुरू होती है। प्रमाण पत्र की वैधता समाप्त होने के बाद, इसे नवीनीकरण के लिए आवेदन करना होता है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

---

### Query #18
* **Category:** Basic Info
* **Input Language:** English
* **Input Query:** `Is there any offline mode to apply for Domicile?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `4.15s`

**Bot Response:**
Based on the information provided, there is no offline mode to apply for a Domicile Certificate. You can only apply through the online mode.

To apply online, you need to:
1. Register on the Sewa Setu Chhattisgarh portal.
2. Log in to the e-Nirmiti portal.

If you need assistance with the online application process, you can visit a Sewa Setu Kendra. There, you can submit your application and required documents in person, and pay the service fee of ₹30.0.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #19
* **Category:** Basic Info
* **Input Language:** Hindi
* **Input Query:** `क्या विवाह पंजीकरण के लिए ऑनलाइन आवेदन किया जा सकता है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `3`
* **Response Latency:** `7.20s`

**Bot Response:**
हाँ, विवाह पंजीकरण के लिए ऑनलाइन आवेदन किया जा सकता है। सेवा सेतु छत्तीसगढ़ पोर्टल विवाह पंजीकरण और प्रमाणपत्र जारी करने के लिए एक ऑनलाइन सेवा प्रदान करता है।

**ऑनलाइन आवेदन प्रक्रिया:**

1. **पोर्टल पर लॉगिन:** सबसे पहले नागरिक सेवा सेतु पोर्टल (https://sewasetu.cgstate.gov.in/home?lang=hi) पर लॉगिन करें।
2. **योजना खोज:** सेवा खोज अनुभाग में "विवाह प्रमाण पत्र" सेवा का चयन करें।
3. **बुनियादी जानकारी:** आवेदन फॉर्म में वधु-वधु की बुनियादी जानकारी और विवाह की तिथि दर्ज करें।
4. **दस्तावेज़ अपलोड:** आवश्यक दस्तावेज़ों को ऑनलाइन अपलोड करें।
5. **शुल्क भुगतान:** ऑनलाइन शुल्क (₹30.0) का भुगतान करें।
6. **आवेदन जमा:** सभी जानकारी और दस्तावेज़ों की जाँच के बाद आवेदन जमा करें।

**आवश्यक दस्तावेज़:**

- वर और वधु का संयुक्त फोटो (2A साइज़)
- वर का जन्म प्रमाण पत्र
- वधु का जन्म प्रमाण पत्र
- विवाह आमंत्रण पत्र
- वर और वधु द्वारा हस्ताक्षरित दस्तावेज़ (प्रथम और द्वितीय पृष्ठ)
- चालान की प्रति

**समय सीमा:**

आवेदन जमा करने के 15 दिनों के भीतर इसकी प्रक्रिया पूरी की जाती है।

अधिक जानकारी के लिए आप सेवा सेतु केंद्र से संपर्क कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)

---

### Query #20
* **Category:** Basic Info
* **Input Language:** Hinglish
* **Input Query:** `obc certificate offline banta hai ya online?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `5`
* **Response Latency:** `6.88s`

**Bot Response:**
Haan, OBC certificate dono tarah se ban sakta hai - online aur offline.

**Online Application:**
- Sewa Setu portal par apply kar sakte hain
- Website: https://sewasetu.cgstate.gov.in/home?lang=en
- Online fee: ₹30.0
- Service delivery time: 22 days

**Offline Application:**
- Sewa Setu Kendra se apply kar sakte hain
- Offline fee: ₹30.0
- Service delivery time: 30 working days

Dono methods mein same fee hai, lekin processing time alag hai. Aap apni convenience ke hisaab se koi bhi option choose kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)

---

### Query #21
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `If I don't have an education certificate, can I still get a domicile?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `7.43s`

**Bot Response:**
Based on the information provided, you can still get a domicile certificate even if you do not have an education certificate.

The Domicile Certificate service has two alternative eligibility criteria:

1.  **Criteria One AND Criteria Two:** You must meet both the 15-year stay requirement AND the 5-year stay requirement.
2.  **Criteria Three:** This is a standalone alternative set of conditions. If you meet Criteria Three, you do not need to meet Criteria One or Two.

The context does not specify what Criteria Three entails. Therefore, if you do not have an educational certificate, you may still be eligible by meeting the other criteria.

Please note that the context does not provide information on alternative paths or exceptions for the educational certificate requirement. You may need to contact the Sewa Setu Kendra or the Revenue and Disaster Management Department for further clarification on your specific situation.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #22
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hindi
* **Input Query:** `अगर मेरे पास कोई शिक्षा प्रमाणपत्र नहीं है, तो क्या मैं निवास प्रमाण पत्र के लिए पात्र हूँ?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `9.78s`

**Bot Response:**
नहीं, यदि आपके पास कोई शिक्षा प्रमाण पत्र नहीं है, तो आप मूल निवासी प्रमाण पत्र के लिए पात्र नहीं होंगे।

मूल निवासी प्रमाण पत्र के लिए शिक्षा प्रमाण पत्र अनिवार्य है। यदि आप शिक्षा प्रमाण पत्र के बिना आवेदन करते हैं, तो आपका आवेदन अस्वीकार कर दिया जाएगा।

आपको शिक्षा प्रमाण पत्र प्राप्त करना होगा, जैसे:
- माध्यमिक विद्यालय का प्रमाणपत्र (8वीं कक्षा)
- हाई स्कूल (10वीं कक्षा) की अंकसूची
- या अन्य कोई शिक्षा प्रमाण पत्र

इसके बिना आप इस सेवा का लाभ नहीं उठा सकते।

यदि आप शिक्षा प्रमाण पत्र प्राप्त करने के बाद भी पात्रता के बारे में अनिश्चित हैं, तो आप विशिष्ट मार्गदर्शन के लिए Sewa Setu Kendra या राजस्व और आपदा प्रबंधन विभाग से संपर्क कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

---

### Query #23
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hinglish
* **Input Query:** `bina padhai ke certificate ke domicile certificate ban sakta hai kya?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `8.44s`

**Bot Response:**
Haan, bina padhai ke certificate ke domicile certificate ban sakta hai.

Aapke paas do tarike hain domicile certificate ke liye:

1. **15 saal ka residence proof:** Agar aapne Chhattisgarh mein 15 saal se zyada time se rehna hai, toh aap domicile certificate ke liye apply kar sakte hain. Iske liye birth certificate, parent's service certificate, ya voting card jaise documents chahiye.

2. **5 saal ka residence proof:** Agar aapne Chhattisgarh mein 5 saal se zyada time se rehna hai, toh bhi aap domicile certificate ke liye apply kar sakte hain.

Educational certificate zaroori hai, lekin woh padhai ka certificate nahi hona chahiye. Koi bhi educational certificate (jaise 10th, 12th, ya graduation) jo aapke paas hai, woh kaam aayega.

Matlab, aapko padhai ka certificate nahi chahiye, bas ek valid educational certificate chahiye.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #24
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `I married in Raipur but my parents live in Basna, where should I register my marriage?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `3`
* **Response Latency:** `7.10s`

**Bot Response:**
Based on the rules for marriage registration in Chhattisgarh, you should register your marriage in the local area where it was solemnized, which is Raipur.

The marriage must be registered with the appropriate local authority of that area. Since your marriage took place in Raipur, you should register there, not in Basna where your parents live.

The local authority for registration in an urban area like Raipur would be the Municipality or Municipal Corporation. You can complete the registration process by visiting the Seva Setu center or by applying through the online portal.

Please note that registering in the place of your parents' residence would not be in accordance with the rules, as the registration must be done in the location where the marriage was performed.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

---

### Query #25
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hindi
* **Input Query:** `मैंने रायपुर में शादी की है पर मेरा गृहनगर बसना है, मुझे अपना विवाह पंजीकरण कहाँ कराना चाहिए?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `3`
* **Response Latency:** `7.19s`

**Bot Response:**
आपकी शादी रायपुर में हुई है, इसलिए आपका विवाह पंजीकरण Raipur के Service Seva Kendra में ही किया जाना चाहिए।

**विवाह पंजीकरण के लिए स्थान:**
- **राipur** के Service Seva Kendra में पंजीकरण करें
- यह नियम है कि विवाह का पंजीकरण उसी स्थानीय क्षेत्र में होना चाहिए जहाँ वह संपन्न हुआ है

**आवेदन प्रक्रिया:**
- आप ऑनलाइन भी आवेदन कर सकते हैं
- वेबसाइट: https://sewasetu.cgstate.gov.in/home?lang=hi
- शुल्क: ₹30.0 (ऑनलाइन और ऑफलाइन दोनों)

**सुझाव:**
- आपका गृहनगर बसना है, लेकिन विवाह पंजीकरण Raipur में ही होगा
- Raipur के Service Seva Kendra में जाकर आवश्यक दस्तावेज लेकर अपना पंजीकरण पूरा करें

यह आपके लिए सबसे आसान तरीका होगा।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)

---

### Query #26
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hinglish
* **Input Query:** `shadi raipur me hui par permanent address basna hai, register kaha hoga?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `3`
* **Response Latency:** `8.79s`

**Bot Response:**
Haan, aapki shaadi Raipur mein hui hai aur aapka permanent address basna hai, toh aapka registration Raipur mein hi hoga.

**Yahan bataya gaya hai ki registration kahan hoga:**

1.  **Local Authority:** Aapka marriage registration aapke local area ke Local Authority ke under hoga.
2.  **Raipur Location:** Chunki shaadi Raipur mein hui hai, toh registration Raipur mein hi hoga.
3.  **Portal:** Aapko Sewa Setu Chhattisgarh portal par jaana hoga.
4.  **Service:** Wahan "Marriage Certificate" service select karni hogi.

**Important Points:**

*   Shaadi ke time jo address tha, woh aapko application form mein fill karna hoga.
*   Agar shaadi ke baad aapne apna permanent address basna hai, toh woh bhi application mein mention karna zaroori hai.
*   Registration ke liye aapko online process follow karna hoga, jisme documents upload karne aur fee pay karne ki zaroorat hogi.

Aap bas portal par jaake details fill karke registration complete kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)

---

### Query #27
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `Is affidavit mandatory for SC certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `8.27s`

**Bot Response:**
Based on the information provided, an affidavit is not mandatory for obtaining an SC certificate.

The context clearly states that an affidavit is listed as "Mandatory: No" under the required documents section. While you can submit an affidavit as a supporting document, it is not a required requirement for your application.

You can proceed with your application by providing the mandatory caste proof and any other documents you wish to include.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

---

### Query #28
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hindi
* **Input Query:** `क्या अनुसूचित जाति प्रमाण पत्र के लिए शपथ पत्र अनिवार्य है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `7.93s`

**Bot Response:**
नहीं, अनुसूचित जाति प्रमाण पत्र के लिए शपथ पत्र अनिवार्य नहीं है।

संदर्भ के अनुसार, शपथ पत्र (affidavit) को आवश्यक दस्तावेजों की सूची में नहीं रखा गया है, और इसकी स्थिति "अनिवार्य नहीं" (Not Mandatory) के रूप में दर्शाई गई है।

आप बिना शपथ पत्र के भी अनुसूचित जाति प्रमाण पत्र के लिए आवेदन कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

---

### Query #29
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hinglish
* **Input Query:** `sc certificate apply karne ke liye kya affidavit compulsory hai?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `8.03s`

**Bot Response:**
नहीं, अफ़िडेविट (शपथ पत्र) SC/ST प्रमाणपत्र के लिए अनिवार्य नहीं है।

आप बिना अफ़िडेविट के भी आवेदन कर सकते हैं। यह एक वैकल्पिक दस्तावेज़ है, जिसे आप चाहें तो शामिल कर सकते हैं, लेकिन इसकी आवश्यकता नहीं है।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

---

### Query #30
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `What is the education requirement for domicile in Chhattisgarh?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `7.10s`

**Bot Response:**
Based on the information provided, the education requirement for a domicile certificate in Chhattisgarh is as follows:

**Criteria Two (B) - Education Requirements:**
- Three years of formal education in Chhattisgarh, OR
- Passed one of the board exams (Class 5, 8, 10, or 12) from Chhattisgarh.

**Important Notes:**
- The applicant must meet either of the two conditions listed above.
- These education requirements are part of the combined eligibility criteria.

**Alternative Path:**
- If the applicant or their spouse is a domicile of Chhattisgarh, they may be eligible under Criteria Three (C), which has different requirements. However, Criteria One (A) and Criteria Two (B) must both be met for this alternative path.

The context does not provide additional details about specific educational certificates or other documentation related to the education requirement.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #31
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hindi
* **Input Query:** `छत्तीसगढ़ में मूल निवासी के लिए कितने वर्षों की शिक्षा की आवश्यकता है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `7.34s`

**Bot Response:**
छत्तीसगढ़ में मूल निवासी प्रमाण पत्र के लिए निम्नलिखित शिक्षा के वर्ष आवश्यक हैं:

*   छत्तीसगढ़ में तीन वर्ष की औपचारिक शिक्षा।
*   या फिर, छत्तीसगढ़ राज्य बोर्ड की कक्षा 5, 8, 10 या 12 की परीक्षा उत्तीर्ण करना।

यह जानकारी आधिकारिक दस्तावेज़ के "मानदंड दो" के अनुसार है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

---

### Query #32
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hinglish
* **Input Query:** `domicile ke liye cg me kitne saal school padha hona chahiye?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `7.04s`

**Bot Response:**
Chhattisgarh mein domicile certificate ke liye aapko kam se kam 3 saal tak state mein padhai karni padti hai.

Yeh do tarah se ho sakta hai:
- State mein 3 saal tak formal education complete ki ho
- Ya phir Chhattisgarh se koi board exam (Class 5, 8, 10, ya 12) pass kiya ho

Iske alawa, aapke paas 15 saal ka residence proof bhi hona zaroori hai, jaise birth certificate, ration card, ya electricity bill.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #33
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `What are the criteria for domicile if my parents are govt employees?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `8.21s`

**Bot Response:**
Based on the information provided, if your parents are government employees, you can be eligible for a domicile certificate in Chhattisgarh under the alternative criteria.

Here are the specific conditions:

*   Your spouse is a domicile of Chhattisgarh.
*   You or your parents are an employee of the Chhattisgarh Government or its Public Sector Undertaking (PSU).
*   You or your parents are in the All India Services and have been allotted a Chhattisgarh cadre.

If you meet any one of these three conditions, you are eligible for a domicile certificate. You do not need to meet the requirements of Criteria One and Two (related to birth or education in Chhattisgarh) in this case.

Please note that this is an alternative set of conditions. If you do not meet any of the three conditions listed above, you would need to meet the standard criteria, which involve being born in Chhattisgarh or having parents who have resided there for 25 years, along with having three years of formal education or passing a specific board exam from the state.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #34
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hindi
* **Input Query:** `यदि माता-पिता सरकारी कर्मचारी हैं तो मूल निवासी पात्रता के क्या नियम हैं?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `11.32s`

**Bot Response:**
छत्तीसगढ़ में मूल निवासी प्रमाण पत्र के लिए पात्रता के नियम निम्नलिखित हैं:

**सरकारी कर्मचारी माता-पिता के लिए विशेष प्रावधान:**

यदि आवेदक के माता-पिता में से कोई भी सरकारी कर्मचारी है, तो आवेदक को मूल निवासी प्रमाण पत्र प्राप्त करने के लिए निम्नलिखित शर्तें लागू होती हैं:

1. **शैक्षणिक योग्यता:** आवेदक को कम से कम 10वीं कक्षा तक का शैक्षणिक प्रमाण पत्र प्रस्तुत करना होगा।

2. **निवास अवधि:** आवेदक को 15 वर्ष तक छत्तीसगढ़ में निवास करना अनिवार्य है।

3. **सरकारी सेवा का लाभ:** यदि माता-पिता सरकारी कर्मचारी हैं, तो आवेदक को माता-पिता के सेवा प्रमाण पत्र या पहचान पत्र की आवश्यकता हो सकती है।

**पात्रता का सारांश:**

- यदि माता-पिता सरकारी कर्मचारी हैं, तो आवेदक को पहली और दूसरी शर्त (15 वर्ष का निवास) को पूरा करना होगा।
- तीसरी शर्त (शैक्षणिक योग्यता) भी अनिवार्य है।
- माता-पिता के सरकारी रोजगार के कारण आवेदक को पहली और दूसरी शर्त के अतिरिक्त अन्य किसी भी शर्त को पूरा करने की आवश्यकता नहीं है।

**महत्वपूर्ण बिंदु:**

- मूल निवासी प्रमाण पत्र के लिए 15 वर्ष तक का निवास प्रमाण अनिवार्य है।
- शैक्षणिक प्रमाण पत्र (10वीं कक्षा) भी अनिवार्य है।
- सरकारी कर्मचारी माता-पिता के लिए रोजगार प्रमाण पत्र सहायक हो सकता है।

अधिक जानकारी के लिए आप सेवा सेतु केंद्र या Sewa Setu पोर्टल पर जा सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

---

### Query #35
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hinglish
* **Input Query:** `parents cg govt employee hain to domicile certificate kaise banega?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `11.33s`

**Bot Response:**
Haan, aapke parents agar Chhattisgarh government employee hain, to aap domicile certificate banwa sakte hain. Yahan bataya gaya hai ki kaise:

**Eligibility Criteria:**
Aap domicile certificate ke liye eligible hain agar aap inmein se koi ek condition meet karte hain:

1. **Criteria One aur Two:**
   - Aapka janm Chhattisgarh mein hua hai (birth certificate ke according)
   - Ya aapke parents mein se koi Chhattisgarh government ka employee hai
   - Ya aapke parents ya aapke paas pichle 5 saal se Chhattisgarh mein property hai

2. **Criteria Three (Alternative):**
   - Aapke ya aapke spouse ke paas Chhattisgarh ka domicile hai
   - Ya aapke parents ya aap Chhattisgarh all-India services mein hain

**Required Documents:**
- Application form
- Affidavit (Mandatory)
- Educational certificates (Mandatory)
- Service Certificate (Agar parents government employee hain)
- Property documents (Agar applicable hai)
- Proof of residence (25 saal ke liye)
- Birth Certificate (Agar available hai)

**Application Process:**
1. Sewa Setu portal par login karein
2. "Domicile Certificate" par click karein
3. Form mein saari details bharein
4. Aadhar e-authentication se confirm karein
5. Fee pay karein (Rs. 30)

**Important Points:**
- Agar parents government employee hain, to Service Certificate aur Job Certificate mandatory hain
- Proof of residence 25 saal tak ka hona chahiye
- Service fee Rs. 30 hai

Koi specific document missing hai to aap Sewa Setu center se contact kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #36
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `Is there any relaxation in Domicile criteria for wife of CG domicile?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `9.08s`

**Bot Response:**
Based on the information provided, there is no relaxation in the Domicile criteria for the wife of a CG domicile.

The eligibility criteria for a CG Domicile Certificate are as follows:

*   **Criterion A:** The applicant must be a native of Chhattisgarh.
*   **Criterion B:** The applicant must provide proof of residence in Chhattisgarh for 15 years.

Both criteria are mandatory. If either one is not met, the certificate cannot be obtained.

Regarding the wife of a CG domicile, if she is not a native of Chhattisgarh, a separate domicile certificate must be obtained for her. This will involve an additional fee and a separate process. However, there is no relaxation in the standard criteria for her.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)

---

### Query #37
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hindi
* **Input Query:** `क्या छत्तीसगढ़ मूल निवासी के जीवनसाथी के लिए पात्रता में कोई छूट है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `7`
* **Response Latency:** `9.16s`

**Bot Response:**
हाँ, छत्तीसगढ़ मूल निवासी प्रमाण पत्र के लिए जीवनसाथी की पात्रता में छूट उपलब्ध है।

**जीवनसाथी के लिए छूट के मुख्य बिंदु:**

*   यदि आप मूल निवासी प्रमाण पत्र के लिए आवेदन कर रहे हैं, तो आपके जीवनसाथी की मूल निवासी स्थिति के आधार पर अलग से पात्रता मानदंड लागू हो सकते हैं।
*   यदि आपके जीवनसाथी का मूल निवासी प्रमाण पत्र पहले से ही है, तो आपको अलग से आवेदन करने की आवश्यकता नहीं हो सकती है।
*   जीवनसाथी के लिए मूल निवासी प्रमाण पत्र हेतु आवेदन करने के लिए, आपको विवाह पंजीकरण और अन्य आवश्यक दस्तावेजों के संबंध में विशिष्ट नियमों का पालन करना होगा।

**विवाह पंजीकरण:**

*   जीवनसाथी के लिए मूल निवासी प्रमाण पत्र हेतु आवेदन करने के लिए, विवाह का पंजीकरण उसी स्थानीय क्षेत्र में होना चाहिए जहाँ विवाह संपन्न हुआ है, न कि वर-वधू के गृहनगर या निवास स्थान पर।

**दस्तावेज़:**

*   जीवनसाथी के लिए मूल निवासी प्रमाण पत्र हेतु आवेदन करने के लिए आवश्यक दस्तावेजों में शामिल हो सकते हैं:
    *   विवाह प्रमाण पत्र
    *   निवास प्रमाण पत्र
    *   मूल निवासी प्रमाण पत्र

कृपया ध्यान दें कि जीवनसाथी के लिए मूल निवासी प्रमाण पत्र हेतु आवेदन करने के लिए, आपको छत्तीसगढ़ मूल निवासी प्रमाण पत्र के लिए निर्धारित दस्तावेजों और प्रक्रियाओं का पालन करना होगा।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)

---

### Query #38
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `What are the alternative supporting documents if birth certificate is not available for SC certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `9.13s`

**Bot Response:**
Based on the information provided, here are the alternative supporting documents that can be used for an SC certificate when a birth certificate is not available:

**For Caste Proof (Mandatory):**
- Sc/St Certificate of Other State
- Sc/St Certificate From Sarpanch / Parshad / Mla / Mp
- Transfer Certificate From Any Recognized School Or Any School Countersigned By Deo
- Father/Guardians Service Certificate/Identity Card
- Educational Certificate
- Caste Certificate Issued Earlier To The Applicant Or Any Member Of His Family
- Primary School Certificate
- Birth Information Form
- Misal
- Adhikar Abhilekh
- Jamabandi
- Census Register Of 1931
- Citizen Register Of 1949
- Dakhil / Kharij Panji
- Disability / Unavailability Proof

**For Residential Proof (Mandatory):**
- Domicile Certificate
- Electricity Bill
- Ration Card
- Telephone Bill
- Land And House Document
- Driving License
- Certificate From Ward Member, Local Mla/Mp
- Photo Identity Card
- Service Certificate Of Father / Guardian
- Other Documents

**Important Notes:**
- Birth certificate is not mandatory but optional for SC certificate applications.
- If the birth certificate is not available, the certificate can be issued based on other documents.
- Original and self-attested copies of all documents must be attached with the application.
- For specific guidance on which documents are acceptable in your situation, you may need to contact the Sewa Setu Kendra or the Revenue and Disaster Management Department directly.

The context does not specify which of these documents are mandatory alternatives to a birth certificate. For specific guidance, please contact the relevant authorities.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

---

### Query #39
* **Category:** Tough/Detailed Context Specific
* **Input Language:** Hindi
* **Input Query:** `अगर एससी सर्टिफिकेट के लिए जन्म प्रमाण पत्र नहीं है तो कौन सा वैकल्पिक दस्तावेज मान्य है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `10.49s`

**Bot Response:**
सेवा सेतु पोर्टल पर अनुसूचित जाति/जनजाति प्रमाण पत्र के लिए जन्म प्रमाण पत्र के स्थान पर निम्नलिखित वैकल्पिक दस्तावेज मान्य हैं:

*   जन्म सूचना प्रपत्र (Birth Information Form)
*   मिसल (Misal)
*   असमर्थता / अनुपलब्धता का प्रमाण (Disability / Non-availability Proof)
*   अभिलेख (Record)
*   जन्म प्रमाण पत्र (Birth Certificate)

इनमें से किसी भी एक वैकल्पिक दस्तावेज को प्रस्तुत करके आप जन्म प्रमाण पत्र के स्थान पर आवेदन कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)

---

### Query #40
* **Category:** Tough/Detailed Context Specific
* **Input Language:** English
* **Input Query:** `Are Madhya Pradesh Reorganisation Act 2000 provisions applicable for SC/ST certificate?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `4`
* **Response Latency:** `7.78s`

**Bot Response:**
Based on the information provided, the provisions of the Madhya Pradesh Reorganisation Act, 2000 are not applicable for the Scheduled Caste/Scheduled Tribe (SC/ST) certificate service through the Chhattisgarh Sewa Setu portal.

The context clearly states that:
- The provisions of the Madhya Pradesh Reorganisation Act, 2000 are not applicable for the SC/ST certificate service.
- The official document issued by the Revenue and Disaster Management Department for the SC/ST certificate does not mention the Madhya Pradesh Reorganisation Act, 2000.
- The process and required documents for the SC/ST certificate are determined solely according to the guidelines of the Revenue and Disaster Management Department.

Therefore, you are not required to provide the Madhya Pradesh Reorganisation Act, 2000 document when applying for an SC/ST certificate through the Sewa Setu Chhattisgarh portal.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)

---

### Query #41
* **Category:** Out of Scope / Random
* **Input Language:** English
* **Input Query:** `How can I apply for a student scholarship on Sewa Setu?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `1.75s`

**Bot Response:**
Information not available.

---

### Query #42
* **Category:** Out of Scope / Random
* **Input Language:** Hindi
* **Input Query:** `क्या मुझे सेवा सेतु पर बिजली कनेक्शन मिल सकता है?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `1.45s`

**Bot Response:**
जानकारी उपलब्ध नहीं है।

---

### Query #43
* **Category:** Out of Scope / Random
* **Input Language:** Hinglish
* **Input Query:** `ration card status check kaise kare?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `1.62s`

**Bot Response:**
Jaankari uplabhd nahi hai.

---

### Query #44
* **Category:** Out of Scope / Random
* **Input Language:** English
* **Input Query:** `How to view my land khasra records in CG?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `2.15s`

**Bot Response:**
Jaankari uplabhd nahi hai.

---

### Query #45
* **Category:** Out of Scope / Random
* **Input Language:** English
* **Input Query:** `What is the process to get a home loan?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `1.40s`

**Bot Response:**
Information not available.

---

### Query #46
* **Category:** Out of Scope / Random
* **Input Language:** Hindi
* **Input Query:** `आय प्रमाण पत्र (income certificate) बनवाने के लिए क्या करें?`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `1.56s`

**Bot Response:**
जानकारी उपलब्ध नहीं है।

---

### Query #47
* **Category:** Out of Scope / Random
* **Input Language:** English
* **Input Query:** `how to register a rental agreement in raipur?`
* **Detected Query Language:** `hinglish`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `2.24s`

**Bot Response:**
Jaankari uplabhd nahi hai.

---

### Query #48
* **Category:** Out of Scope / Random
* **Input Language:** English
* **Input Query:** `what is the weather like in Chhattisgarh today?`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `2.35s`

**Bot Response:**
Information not available.

---

### Query #49
* **Category:** Out of Scope / Random
* **Input Language:** English
* **Input Query:** `cghs card download link`
* **Detected Query Language:** `en`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `1.67s`

**Bot Response:**
Information not available.

---

### Query #50
* **Category:** Out of Scope / Random
* **Input Language:** Hinglish
* **Input Query:** `mujhe naya voter card banwana hai`
* **Detected Query Language:** `hi`
* **Auto-Mapped Service ID:** `None`
* **Response Latency:** `1.59s`

**Bot Response:**
जानकारी उपलब्ध नहीं है।

---

