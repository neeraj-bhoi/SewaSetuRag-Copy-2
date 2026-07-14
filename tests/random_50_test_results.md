# SewaSetu RAG Chatbot: 50 Random Real-Life Queries Test Results

This audit report captures testing the RAG chatbot with 50 diverse, random, real-life queries. The questions cover all 5 scoped services of the SewaSetu Chhattisgarh Portal with a realistic mix of English, Hindi, and Hinglish queries.

## Execution Summary Table

| ID | Service Category | User Query | Language | Mapped Service ID | Intent | Grounding Guardrail | Latency | Status |
|----|------------------|------------|----------|-------------------|--------|---------------------|---------|--------|
| 1 | Marriage Registration | `What is the official government fee to get a marriage certificate online in Chhattisgarh?` | EN (en) | 3 | new_topic | N/A | 4.88s | ✅ SUCCESS |

### Query 1 Details
* **Query**: `What is the official government fee to get a marriage certificate online in Chhattisgarh?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the official government fee to get a marriage registration and certificate online in Chhattisgarh?`
* **Resolved Hindi Translation**: `छत्तीसगढ़ में ऑनलाइन विवाह पंजीकरण और प्रमाणपत्र प्राप्त करने के लिए आधिकारिक सरकारी शुल्क क्या है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The official government fee for marriage registration and certificate online in Chhattisgarh is ₹30.0. This fee is applicable for both online and kiosk applications. The fee is paid to the service provider (kiosk operator) and is non-refundable. Additionally, there is a separate fee of ₹20 for obtaining certified extracts from the marriage register, if required.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 2 | Marriage Registration | `Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?` | HINGLISH (hinglish) | 3 | new_topic | N/A | 4.58s | ✅ SUCCESS |

### Query 2 Details
* **Query**: `Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What documents are required to be taken for offline marriage registration at the Raipur Municipal Corporation office?`
* **Resolved Hindi Translation**: `रैरापुर नगर निगम कार्यालय में ऑफलाइन विवाह पंजीकरण के लिए क्या दस्तावेज ले जाना होगा?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Raipur Municipal Corporation office me offline marriage registration ke liye ye documents le jana hoga:

1. Affidavit (Mandatory)
2. Groom aur bride ka combined photo (2a size) (Mandatory)
3. Birth certificate of groom (Mandatory)
4. Birth certificate of bride (Mandatory)
5. Document signed by bride aur groom (First page) (Mandatory)
6. Document signed by bride aur groom (Second page) (Mandatory)
7. Marriage invitation card (Mandatory)
8. Copy of challan (Mandatory)

Baaki documents optional hain, jaise ki guardian ka declaration letter, divorce certificate, widow certificate, inter-religion marriage certificate.

Note: Local area me jahan shaadi hui hai, wahi office me registration karna padega, Raipur me nahi.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 3 | Marriage Registration | `विवाह पंजीकरण के लिए आवश्यक दस्तावेजों की सूची क्या है?` | HI (hi) | 3 | new_topic | N/A | 3.83s | ✅ SUCCESS |

### Query 3 Details
* **Query**: `विवाह पंजीकरण के लिए आवश्यक दस्तावेजों की सूची क्या है?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hi`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the list of documents required for marriage registration?`
* **Resolved Hindi Translation**: `विवाह पंजीकरण के लिए आवश्यक दस्तावेजों की सूची क्या है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  विवाह पंजीकरण के लिए आवश्यक दस्तावेजों की सूची निम्नलिखित है:

1. शपथ पत्र (अनिवार्य)
2. वर और वधु का संयुक्त फोटो (2A साइज़) (अनिवार्य)
3. वर का जन्म प्रमाण पत्र (अनिवार्य)
4. वधु का जन्म प्रमाण पत्र (अनिवार्य)
5. वर और वधु द्वारा हस्ताक्षरित दस्तावेज (प्रथम पृष्ठ) (अनिवार्य)
6. वर और वधु द्वारा हस्ताक्षरित दस्तावेज (द्वितीय पृष्ठ) (अनिवार्य)
7. चालान की प्रति (अनिवार्य)
8. विवाह आमंत्रण पत्र (अनिवार्य)

अन्य दस्तावेज जैसे कि घोषणा पत्र, तलाक प्रमाण पत्र, विधवा प्रमाण पत्र और अंतर-धार्मिक विवाह प्रमाण पत्र अनिवार्य नहीं हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)
  ```

---
| 4 | Marriage Registration | `Mera shadi ka card (invitation card) nahi hai, to kya online shadi register ho sakti hai?` | HINGLISH (hinglish) | 3 | new_topic | N/A | 4.34s | ✅ SUCCESS |

### Query 4 Details
* **Query**: `Mera shadi ka card (invitation card) nahi hai, to kya online shadi register ho sakti hai?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `My wedding card is not an invitation card, so can a wedding be registered online?`
* **Resolved Hindi Translation**: `मेरा शादी का कार्ड (इन्विटेशन कार्ड) नहीं है, तो क्या ऑनलाइन शादी रजिस्टर हो सकती है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, शादी का कार्ड नहीं होने पर भी आप ऑनलाइन शादी रजिस्टर कर सकते हैं। शादी का आमंत्रण कार्ड एक अनिवार्य दस्तावेज नहीं है। आपको इसके बजाय अन्य वैकल्पिक दस्तावेज जैसे कि संयुक्त फोटो, जन्म प्रमाण पत्र, या अन्य आवश्यक कागजात अपलोड करने होंगे।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 5 | Marriage Registration | `Is there any penalty or extra fee if I register my marriage after 1 year of marriage in CG?` | EN (en) | 3 | new_topic | N/A | 2.85s | ✅ SUCCESS |

### Query 5 Details
* **Query**: `Is there any penalty or extra fee if I register my marriage after 1 year of marriage in CG?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is there any penalty or extra fee if I register my marriage after 1 year of marriage in CG?`
* **Resolved Hindi Translation**: `क्या सी जी में विवाह के एक वर्ष के बाद विवाह पंजीकृत करने पर कोई दंड या अतिरिक्त शुल्क है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Yes, there is a penalty for registering a marriage after the 30-day deadline. As per Rule 12, a penalty fine of up to 500 rupees applies for failing to submit the marriage memorandum within the 30-day period from the date of marriage. This penalty is mandatory if the registration is delayed beyond the specified timeframe.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 6 | Marriage Registration | `विवाह प्रमाण पत्र प्राप्त करने की समय सीमा (SLA) कितने दिनों की होती है?` | HI (hi) | 3 | new_topic | N/A | 2.79s | ✅ SUCCESS |

### Query 6 Details
* **Query**: `विवाह प्रमाण पत्र प्राप्त करने की समय सीमा (SLA) कितने दिनों की होती है?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hi`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the time limit (SLA) for marriage registration and obtaining the certificate?`
* **Resolved Hindi Translation**: `विवाह पंजीकरण एवं प्रमाण पत्र प्राप्त करने की समय सीमा (SLA) कितने दिनों की होती है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  विवाह पंजीकरण एवं प्रमाण पत्र प्राप्त करने की समय सीमा 15 दिन की होती है। यह सेवा शहरी प्रशासन और विकास विभाग के अंतर्गत प्रदान की जाती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)
  ```

---
| 7 | Marriage Registration | `Online apply karne ke baad verification ke liye kya dono husband aur wife ko office jana padega?` | HINGLISH (hinglish) | None | new_topic | N/A | 1.88s | ✅ SUCCESS |

### Query 7 Details
* **Query**: `Online apply karne ke baad verification ke liye kya dono husband aur wife ko office jana padega?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `None`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `After applying online, do both the husband and wife need to go to the office for verification?`
* **Resolved Hindi Translation**: `Online apply karne ke baad verification ke liye kya dono husband aur wife ko office jana padega?`
* **Grounding Status**: `N/A`
* **Intermediate English Answer**:
  ```markdown
  Information not available.
  ```
* **Intermediate Hindi Answer**:
  ```markdown
  जानकारी उपलब्ध नहीं है।
  ```
* **Final Synthesized Chatbot Response**:
  ```markdown
  Mere paas is question ka answer dene ke liye records mein context ya paryapt information nahi hai. Kripya Sewa Setu portal par check karein.
  ```

---
| 8 | Marriage Registration | `Who acts as the Registrar of Marriages in a small village or rural area in CG?` | EN (en) | 3 | new_topic | N/A | 2.73s | ✅ SUCCESS |

### Query 8 Details
* **Query**: `Who acts as the Registrar of Marriages in a small village or rural area in CG?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Who acts as the Registrar of Marriages in a small village or rural area in CG?`
* **Resolved Hindi Translation**: `सी जी के किसी छोटे गाँव या ग्रामीण क्षेत्र में विवाह पंजीकरणकर्ता के रूप में कौन कार्य करता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The Registrar of Marriages in a small village or rural area in Chhattisgarh is the Local Authority, which is the Gram Panchayat.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 9 | Marriage Registration | `क्या ग्रामीण क्षेत्रों में पंचायत सचिव विवाह का रजिस्ट्रेशन कर सकते हैं?` | HI (hi) | None | new_topic | N/A | 1.57s | ✅ SUCCESS |

### Query 9 Details
* **Query**: `क्या ग्रामीण क्षेत्रों में पंचायत सचिव विवाह का रजिस्ट्रेशन कर सकते हैं?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hi`
* **Classified Service ID**: `None`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can the Panchayat Secretary in rural areas register a marriage?`
* **Resolved Hindi Translation**: `क्या ग्रामीण क्षेत्रों में पंचायत सचिव विवाह का रजिस्ट्रेशन कर सकते हैं?`
* **Grounding Status**: `N/A`
* **Intermediate English Answer**:
  ```markdown
  Information not available.
  ```
* **Intermediate Hindi Answer**:
  ```markdown
  जानकारी उपलब्ध नहीं है।
  ```
* **Final Synthesized Chatbot Response**:
  ```markdown
  मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी या आवश्यक संदर्भ नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।
  ```

---
| 10 | Marriage Registration | `I got married in a temple in Bhilai. Can I get a government marriage certificate?` | EN (en) | 3 | new_topic | N/A | 5.56s | ✅ SUCCESS |

### Query 10 Details
* **Query**: `I got married in a temple in Bhilai. Can I get a government marriage certificate?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `I got married in a temple in Bhilai. Can I get a government marriage registration and certificate?`
* **Resolved Hindi Translation**: `मैं भी भील में एक मंदिर में शादी कर ली है। क्या मुझे सरकारी विवाह पंजीकरण और प्रमाण पत्र मिल सकता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Yes, you can get a government marriage registration and certificate for your marriage in a temple in Bhilai.

Under the Chhattisgarh Compulsory Registration of Marriages Rules, your marriage must be registered in the local area where it was solemnized, which is Bhilai in this case. You need to register with the Local Authority of that area, which would be the Gram Panchayat or Municipal Corporation depending on whether Bhilai is urban or rural.

The registration process requires submitting a memorandum of marriage within 30 days of the marriage date. The required documents include:
- Affidavit (Mandatory)
- Combined photograph of groom and bride (2a size) (Mandatory)
- Birth certificates of both groom and bride (Mandatory)
- Document signed by both bride and groom (first and second pages) (Mandatory)
- Copy of challan (Mandatory)
- Marriage invitation card (Mandatory)

The total application fee is ₹30, which can be paid online or at a kiosk. The process takes 15 days to complete.

You can apply online through the Sewa Setu portal or at a Seva Setu Kendra. The marriage certificate will be issued in the specified format after successful registration.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 11 | SC/ST Caste Certificate | `छत्तीसगढ़ में एससी एसटी जाति प्रमाण पत्र के लिए पात्रता मानदंड क्या हैं?` | HI (hi) | 4 | new_topic | N/A | 3.43s | ✅ SUCCESS |

### Query 11 Details
* **Query**: `छत्तीसगढ़ में एससी एसटी जाति प्रमाण पत्र के लिए पात्रता मानदंड क्या हैं?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hi`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What are the eligibility criteria for SC ST caste certificate in Chhattisgarh?`
* **Resolved Hindi Translation**: `छत्तीसगढ़ में एससी एसटी जाति प्रमाण पत्र के लिए पात्रता मानदंड क्या हैं?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  अनुसूचित जाति/अनुसूचित जनजाति प्रमाण पत्र के लिए पात्रता मानदंड निम्नलिखित हैं:

1. आवेदक को छत्तीसगढ़ का निवासी होना चाहिए।
2. आवेदक को अनुसूचित जाति या अनुसूचित जनजाति से संबंधित होना चाहिए।
3. आवेदक को सामाजिक प्रास्थिति प्रमाण पत्र के लिए आवेदन करना चाहिए।
4. आवेदक को आवेदन के साथ आवश्यक दस्तावेज जमा करने चाहिए।

आवश्यक दस्तावेज:
- निवास का प्रमाण (अनिवार्य नहीं)
- जाति का प्रमाण (अनिवार्य)
- शपथ पत्र (अनिवार्य नहीं)
- वंशावली (अनिवार्य नहीं)
- ग्राम सभा प्रस्ताव (अनिवार्य नहीं)

अनिवार्य दस्तावेज:
- जाति प्रमाण (अनिवार्य)
- निवास प्रमाण (वैकल्पिक)

अधिक जानकारी के लिए आप सेवा सेतु केंद्र या ई-डिस्ट्रिक्ट पोर्टल पर जा सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)
  ```

---
| 12 | SC/ST Caste Certificate | `Caste certificate st/sc ke liye kaun kaun se government documents mandatory hain?` | HINGLISH (hinglish) | None | new_topic | N/A | 2.09s | ✅ SUCCESS |

### Query 12 Details
* **Query**: `Caste certificate st/sc ke liye kaun kaun se government documents mandatory hain?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `None`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What government documents are mandatory for caste certificate st/sc?`
* **Resolved Hindi Translation**: `जाति प्रमाण पत्र के लिए कौन-कौन से सरकारी दस्तावेज अनिवार्य हैं?`
* **Grounding Status**: `N/A`
* **Intermediate English Answer**:
  ```markdown
  Information not available.
  ```
* **Intermediate Hindi Answer**:
  ```markdown
  जानकारी उपलब्ध नहीं है।
  ```
* **Final Synthesized Chatbot Response**:
  ```markdown
  Mere paas is question ka answer dene ke liye records mein context ya paryapt information nahi hai. Kripya Sewa Setu portal par check karein.
  ```

---
| 13 | SC/ST Caste Certificate | `Is land record document (like B1/P2/Misal Bandobast) compulsory for SC certificate in CG?` | EN (en) | None | new_topic | N/A | 1.69s | ✅ SUCCESS |

### Query 13 Details
* **Query**: `Is land record document (like B1/P2/Misal Bandobast) compulsory for SC certificate in CG?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `en`
* **Classified Service ID**: `None`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is land record document (like B1/P2/Misal Bandobast) compulsory for SC certificate in CG?`
* **Resolved Hindi Translation**: `क्या भूमि अभिलेख दस्तावेज़ (जैसे B1/P2/मिसल बंदोबस्त) CG में SC प्रमाणपत्र के लिए अनिवार्य है?`
* **Grounding Status**: `N/A`
* **Intermediate English Answer**:
  ```markdown
  Information not available.
  ```
* **Intermediate Hindi Answer**:
  ```markdown
  जानकारी उपलब्ध नहीं है।
  ```
* **Final Synthesized Chatbot Response**:
  ```markdown
  I do not have sufficient information or context in my records to answer this question. Please check the Sewa Setu portal.
  ```

---
| 14 | SC/ST Caste Certificate | `Mera purana hand-written offline SC certificate hai. Use online digital cert me kaise convert karein?` | HINGLISH (hinglish) | 4 | new_topic | N/A | 6.19s | ✅ SUCCESS |

### Query 14 Details
* **Query**: `Mera purana hand-written offline SC certificate hai. Use online digital cert me kaise convert karein?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How to convert my old hand-written offline SC certificate to an online digital certificate?`
* **Resolved Hindi Translation**: `मेरा पुराना हस्तलिखित ऑफलाइन एस सी प्रमाणपत्र है। इसे ऑनलाइन डिजिटल प्रमाणपत्र में कैसे परिवर्तित करें?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, aap apne purane hastlikhit offline SC certificate ko online digital certificate mein convert kar sakte hain. Iske liye aapko e-district portal par jaana hoga.

Sabse pehle, aapko  par jaana hoga.

Iske baad, aapko "Seva Khoj" mein "SC/ST Caste Certificate" ko dhoondhna hoga.

Jab aap seva par click karenge, to aapko application form dikhega. Isme aapko apne purane certificate ki jaankari bharni hogi, jaise:
- Aavedak ka naam
- Pita/pati ka naam
- Janm tithi
- Pate

Form bharne ke baad, aapko zaroori documents upload karne honge. Inme se ek mukhya document aapke purane certificate ki photocopy hogi.

Iske baad, aapko fee ka payment karna hoga. Online fee ₹30 hai.

Jab aap submit karenge, to aapko ek application reference number milega. Aap is number se apne application ki sthiti dekh sakte hain.

Yaad rakhein, application submit karne ke 22 dinon ke andar aapko digital certificate mil jayega.

Kya aap is prakriya ke kisi khaas hisse ke baare mein aur jaanna chahte hain?

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 15 | SC/ST Caste Certificate | `क्या छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है?` | HI (hi) | 4 | new_topic | N/A | 3.53s | ✅ SUCCESS |

### Query 15 Details
* **Query**: `क्या छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hi`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a woman in Chhattisgarh obtain a caste certificate at her husband's address after marriage?`
* **Resolved Hindi Translation**: `क्या छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है। इसके लिए आवेदन पति के पते पर ही जमा किया जा सकता है। यह प्रक्रिया ई-डिस्ट्रिक्ट पोर्टल पर ऑनलाइन आवेदन के माध्यम से पूरी की जा सकती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)
  ```

---
| 16 | SC/ST Caste Certificate | `How long does it take for the Tehsil office to issue a permanent ST caste certificate?` | EN (en) | 4 | new_topic | N/A | 3.02s | ✅ SUCCESS |

### Query 16 Details
* **Query**: `How long does it take for the Tehsil office to issue a permanent ST caste certificate?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `en`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How long does it take for the Tehsil office to issue a permanent ST caste certificate?`
* **Resolved Hindi Translation**: `\)`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the provided documents, the time limit for service delivery of a permanent ST caste certificate from the Tehsil office is 30 working days. This information is detailed in the Table (SLA Details) under the notification dated 16 December 2011. The competent authority for this service is the Sub-Divisional Officer (Revenue).

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 17 | SC/ST Caste Certificate | `Caste certificate apply karne ke liye sewasetu portal ka direct link kya hai?` | HINGLISH (hinglish) | 4 | new_topic | N/A | 5.07s | ✅ SUCCESS |

### Query 17 Details
* **Query**: `Caste certificate apply karne ke liye sewasetu portal ka direct link kya hai?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the direct link for the Sewa Setu portal to apply for a caste certificate?`
* **Resolved Hindi Translation**: `Sewasetu पोर्टल पर जाति प्रमाण पत्र के लिए सीधा लिंक क्या है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, SewaSetu portal par SC/ST certificate apply karne ke liye direct link yeh hai:

https://sewasetu.cgstate.gov.in/home?lang=hi

Yeh link Hindi bhasha mein hai aur aapko directly SewaSetu portal par le jayega jahan se aap apna SC/ST certificate application process kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 18 | SC/ST Caste Certificate | `Which government officer is authorized to issue a permanent SC certificate in a district?` | EN (en) | 4 | new_topic | N/A | 2.64s | ✅ SUCCESS |

### Query 18 Details
* **Query**: `Which government officer is authorized to issue a permanent SC certificate in a district?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `en`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Which government officer is authorized to issue a permanent SC certificate in a district?`
* **Resolved Hindi Translation**: `कौन सा सरकारी अधिकारी किसी जिले में स्थायी एस सी प्रमाणपत्र जारी करने के लिए अधिकृत है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the official rules provided, the Sub-Divisional Officer (Revenue) is the competent authority authorized to issue a permanent SC certificate in a district. The Sub-Divisional Officer (Revenue) serves as the competent authority for both temporary and permanent SC certificates, with the Collector being the appellate authority.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 19 | SC/ST Caste Certificate | `क्या जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर (digital signature) जरूरी है?` | HI (hi) | 4 | new_topic | N/A | 2.67s | ✅ SUCCESS |

### Query 19 Details
* **Query**: `क्या जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर (digital signature) जरूरी है?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hi`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is a digital signature required for the application of a caste certificate?`
* **Resolved Hindi Translation**: `क्या जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर (digital signature) जरूरी है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर अनिवार्य नहीं है। आप बिना डिजिटल हस्ताक्षर के भी आवेदन कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)
  ```

---
| 20 | SC/ST Caste Certificate | `SC caste praman patra online apply karne me portal aur kiosk charge kitna lagta hai?` | HINGLISH (hinglish) | 4 | new_topic | N/A | 4.22s | ✅ SUCCESS |

### Query 20 Details
* **Query**: `SC caste praman patra online apply karne me portal aur kiosk charge kitna lagta hai?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the portal and kiosk charge for applying for an SC caste certificate online?`
* **Resolved Hindi Translation**: `SC जाति प्रमाण पत्र ऑनलाइन आवेदन करने में पोर्टल और कियोस्क शुल्क कितना लगता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  SC/ST certificate online apply karne ke liye portal aur kiosk ka shulk 30-30 rupaye hai. Yeh shulk online aur kiosk dono tariko se payment karne par lagu hota hai. Koi anya atirikt shulk nahi hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 21 | OBC Caste Certificate | `OBC certificate banane ke liye creamy layer aur non-creamy layer ki income limit kitni hai?` | HINGLISH (hinglish) | 5 | new_topic | N/A | 3.54s | ✅ SUCCESS |

### Query 21 Details
* **Query**: `OBC certificate banane ke liye creamy layer aur non-creamy layer ki income limit kitni hai?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the income limit for the creamy layer and non-creamy layer for obtaining an OBC certificate?`
* **Resolved Hindi Translation**: `OBC प्रमाणपत्र बनाने के लिए क्रीमयुक्त और गैर-क्रीमयुक्त परत की आय सीमा क्या है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  OBC certificate ke liye creamy layer aur non-creamy layer ki income limit ke baare mein, official rules mein koi specific income limit mention nahi ki gayi hai. Income certificate zaroori hai, lekin uski exact limit ke liye aapko tehsil office ya patwari se contact karna padega. Ye limit state government ke rules ke hisaab se alag-alag ho sakti hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 22 | OBC Caste Certificate | `ओबीसी जाति प्रमाण पत्र के लिए क्या निवास प्रमाण पत्र (domicile) जमा करना जरूरी है?` | HI (hi) | 5 | new_topic | N/A | 2.79s | ✅ SUCCESS |

### Query 22 Details
* **Query**: `ओबीसी जाति प्रमाण पत्र के लिए क्या निवास प्रमाण पत्र (domicile) जमा करना जरूरी है?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hi`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the original domicile certificate required for OBC caste certificate?`
* **Resolved Hindi Translation**: `ओबीसी जाति प्रमाण पत्र के लिए क्या मूल निवासी प्रमाण पत्र (domicile) जमा करना जरूरी है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, मूल निवासी प्रमाण पत्र अनिवार्य नहीं है। यह एक वैकल्पिक दस्तावेज है। आप आवासीय प्रमाण के लिए भूमि/घर का दस्तावेज, राशन कार्ड, बिजली का बिल, वार्ड सदस्य/विधायक/सांसद का प्रमाण पत्र, जन्म प्रमाण पत्र या जन्म सूचना प्रपत्र में से किसी भी एक का उपयोग कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)
  ```

---
| 23 | OBC Caste Certificate | `Can an OBC candidate apply for OBC certificate online on Sewa Setu portal?` | EN (en) | 5 | new_topic | N/A | 2.95s | ✅ SUCCESS |

### Query 23 Details
* **Query**: `Can an OBC candidate apply for OBC certificate online on Sewa Setu portal?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `en`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can an OBC candidate apply for OBC certificate online on Sewa Setu portal?`
* **Resolved Hindi Translation**: `क्या एक ओ बी सी उम्मीदवार ऑनलाइन सेवा सेटू पोर्टल पर ओ बी सी प्रमाण पत्र के लिए आवेदन कर सकता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Yes, an OBC candidate can apply for an OBC certificate online on the Sewa Setu portal. The process involves accessing the portal, registering or logging in, and submitting the required application form along with supporting documents. The application can be tracked and status can be checked through the portal. The service is available through both online and kiosk (Seva Setu Kendra) options.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 24 | OBC Caste Certificate | `OBC non-creamy layer praman patra ke liye self-declaration affidavit ka format kaisa hona chahiye?` | HINGLISH (hinglish) | 5 | new_topic | N/A | 4.70s | ✅ SUCCESS |

### Query 24 Details
* **Query**: `OBC non-creamy layer praman patra ke liye self-declaration affidavit ka format kaisa hona chahiye?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What should be the format of a self-declaration affidavit for an OBC non-creamy layer certificate?`
* **Resolved Hindi Translation**: `ओ बी सी नॉन-क्रीमी लेयर प्रमाणपत्र के लिए स्व-घोषणा शपथ पत्र का प्रारूप कैसा होना चाहिए?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  OBC non-creamy layer certificate ke liye self-declaration affidavit ka format yeh hona chahiye:

मैं, [आवेदक का नाम], पुत्र/पुत्री/पत्नी [पिता/पति का नाम], निवासी [पूरा पता], यह शपथपूर्वक घोषणा करता/करती हूं कि:

1. मैं OBC category से संबंधित हूं और non-creamy layer के अंतर्गत आता/आती हूं।
2. मेरे परिवार की वार्षिक आय [रकम डालें] से अधिक नहीं है।
3. मैं किसी भी सरकारी नौकरी या अन्य लाभ का लाभ नहीं ले रहा/रही हूं।
4. यह affidavit [दिनांक] को [स्थान] पर बनाया गया है।
5. मैं इसके लिए किसी भी अधिकारी के समक्ष शपथ लेने के लिए तैयार हूं।

शपथकर्ता,
[आवेदक का नाम]
मोबाइल: [नंबर]
दिनांक: [दिनांक]

नोट: इस affidavit को आवेदन के साथ जमा करना अनिवार्य है।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 25 | OBC Caste Certificate | `छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि (validity period) कितनी होती है?` | HI (hi) | 5 | new_topic | N/A | 2.74s | ✅ SUCCESS |

### Query 25 Details
* **Query**: `छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि (validity period) कितनी होती है?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hi`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the validity period of Other Backward Class (OBC) certificate in Chhattisgarh?`
* **Resolved Hindi Translation**: `छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि (validity period) कितनी होती है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि 5 वर्ष होती है। यह प्रमाण पत्र आवेदन की तिथि से 5 वर्ष तक वैध रहता है। इसके पश्चात, प्रमाण पत्र के नवीनीकरण की आवश्यकता हो सकती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)
  ```

---
| 26 | OBC Caste Certificate | `What are the specific form fields and details required to be filled for OBC certificate application?` | EN (en) | 5 | new_topic | N/A | 7.51s | ✅ SUCCESS |

### Query 26 Details
* **Query**: `What are the specific form fields and details required to be filled for OBC certificate application?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `en`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What are the specific form fields and details required to be filled for OBC certificate application?`
* **Resolved Hindi Translation**: `ओ बी सी प्रमाणपत्र आवेदन के लिए किन विशिष्ट फॉर्म फील्ड्स और विवरणों को भरना आवश्यक है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the OBC Certificate application manual, here are the specific form fields and details required:

**General Details:**
- Field: General Details (Type: section label, Data: Character)
- Field: Beneficiary Guardian Type (Type: drop down, Data: Character)
- Field: Beneficiary Guardian name (Type: text, Data: Character)
- Field: Beneficiary Guardian Type in English (Type: drop down, Data: Character)
- Field: Beneficiary Guardian name in English (Type: text, Data: Character)

**Personal Information:**
- Field: Gender (Type: drop down, Data: Character)
- Field: Marital Status (Type: drop down, Data: Character)
- Field: Date of Birth (Type: date, Data: Date)
- Field: Relation to Applicant (Type: drop down, Data: Character)

**Caste Information:**
- Field: Caste OBC (Type: search, Data: Search)
- Field: Category (Type: text, Data: Character)
- Field: Caste In English (Type: text, Data: Character)
- Field: Category In English (Type: text, Data: Character)
- Field: Category Number (Type: text, Data: Character)

**Applicant Details:**
- Field: Beneficiary name in English (Type: text, Data: Character)
- Field: Present Address of Applicant (Type: section label, Data: Character)
- Field: Address (Type: textarea, Data: Alphanumeric)
- Field: PIN Code (Type: text, Data: Number)
- Field: Post Box Number (Type: text, Data: Alphanumeric)
- Field: District (Type: drop down, Data: Character)
- Field: Address In English (Type: textarea, Data: Alphanumeric)
- Field: Is Present Address and Permanent Address is same (Type: drop down, Data: Character)
- Field: Permanent Address of Applicant (Type: section label, Data: Character)

**Additional Fields:**
- Field: Police Station (Type: search, Data: Search)
- Field: Address Before or on Date 26/12/1984 (Type: section label, Data: Character)
- Field: Village or Town (Type: text, Data: Character)
- Field: Patwari Halka Number (Type: text, Data: Number)
- Field: Tehsil (Type: text, Data: Character)
- Field: Name of Head Of Family on This Date (Type: text, Data: Character)
- Field: Applicant Relation to Head of Family (Type: drop down, Data: Character)
- Field: Address Details of Applicant/his Father / Mother/ Guardian from Year 26/12/1984 to till Date (Type: section label, Data: Alphanumeric)
- Field: Address Details of Applicants Guardian (Type: fieldset, Data: Alphanumeric)
- Field: I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time (Type: drop down, Data: Alphanumeric)

**Application Process:**
1. Register on the e-District portal
2. Fill in basic applicant information
3. Fill in other backward class application details
4. Upload required documents
5. Preview and submit application
6. Pay fee (₹30 at CSC/Kiosk or online)
7. Save acknowledgment

**Important Notes:**
- Total application fee is ₹30 (either online or at kiosk, not both)
- Up to 5 documents can be uploaded for free
- No additional charges beyond the application fee
- Application is valid for 22 days
- Fee is non-refundable if application is not submitted within the time limit

The application requires comprehensive personal, family, and caste information with supporting documents to verify eligibility for OBC certificate.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 27 | OBC Caste Certificate | `OBC certificate apply karte waqt lok seva kendra ya kiosk center me kitna extra charge liya jata hai?` | HINGLISH (hi) | 5 | new_topic | N/A | 3.31s | ✅ SUCCESS |

### Query 27 Details
* **Query**: `OBC certificate apply karte waqt lok seva kendra ya kiosk center me kitna extra charge liya jata hai?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hi`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How much extra charge is taken when applying for an OBC certificate at a Lok Seva Kendra or kiosk center?`
* **Resolved Hindi Translation**: `OBC certificate apply karte waqt lok seva kendra ya kiosk center me kitna extra charge liya jata hai?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  लोक सेवा केंद्र या कियोस्क सेंटर में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए आवेदन करने पर कोई अतिरिक्त शुल्क नहीं लिया जाता है। सेवा शुल्क 30 रुपये है, जो ऑनलाइन और कियोस्क दोनों माध्यमों से समान है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)
  ```

---
| 28 | OBC Caste Certificate | `क्या किसी निजी स्कूल (private school) का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त है?` | HI (hi) | 5 | new_topic | N/A | 3.53s | ✅ SUCCESS |

### Query 28 Details
* **Query**: `क्या किसी निजी स्कूल (private school) का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त है?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hi`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is a private school's study certificate sufficient for OBC certificate?`
* **Resolved Hindi Translation**: `क्या किसी निजी स्कूल (private school) का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, निजी स्कूल का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त नहीं है।

ओबीसी प्रमाण पत्र के लिए शिक्षा प्रमाण पत्र अनिवार्य है, लेकिन यह प्रमाण पत्र सरकारी या मान्यता प्राप्त स्कूल का होना चाहिए। निजी स्कूल का प्रमाण पत्र तब तक मान्य नहीं माना जाता जब तक कि वह स्कूल राज्य सरकार द्वारा मान्यता प्राप्त न हो।

आपको निम्नलिखित शिक्षा प्रमाण पत्र में से कोई एक प्रस्तुत करना होगा:
- सरकारी स्कूल का स्थानांतरण प्रमाण पत्र
- मान्यता प्राप्त बोर्ड का 10वीं या 12वीं का अंक पत्र
- अन्य प्रमाण पत्र जो राज्य सरकार द्वारा मान्यता प्राप्त हों

यदि आपके पास कोई अन्य प्रमाण पत्र है जो मान्यता प्राप्त है, तो आप उसे भी प्रस्तुत कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)
  ```

---
| 29 | OBC Caste Certificate | `Is a separate income certificate mandatory to get a non-creamy layer OBC certificate?` | EN (en) | 5 | new_topic | N/A | 2.89s | ✅ SUCCESS |

### Query 29 Details
* **Query**: `Is a separate income certificate mandatory to get a non-creamy layer OBC certificate?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `en`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is a separate income certificate mandatory to get a non-creamy layer OBC certificate?`
* **Resolved Hindi Translation**: `क्या एक अलग आय प्रमाण पत्र गैर-क्रीमी परत ओ बी सी प्रमाण पत्र प्राप्त करने के लिए अनिवार्य है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, एक अलग आय प्रमाण पत्र अनिवार्य नहीं है। आय प्रमाण पत्र (अनिवार्य: हाँ) के अंतर्गत आने वाले दस्तावेजों में से, आप इनमें से किसी भी एक वैकल्पिक विकल्प को चुन सकते हैं: नियोक्ता का आय प्रमाण पत्र/फॉर्म 16, राशन कार्ड, भूमि/घर से आय, या अन्य वैकल्पिक दस्तावेज। इनमें से किसी एक को जमा करना आय प्रमाण की आवश्यकता को पूरा करता है।

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 30 | OBC Caste Certificate | `Bhai, agar parivar ki salana aamdani 8 lakh se jyada hai, to kya OBC certificate mil sakta hai?` | HINGLISH (hinglish) | 5 | new_topic | N/A | 4.27s | ✅ SUCCESS |

### Query 30 Details
* **Query**: `Bhai, agar parivar ki salana aamdani 8 lakh se jyada hai, to kya OBC certificate mil sakta hai?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `If the annual income of the family is more than 8 lakh, can an OBC certificate be obtained?`
* **Resolved Hindi Translation**: `भाई, अगर परिवार की वार्षिक आय 8 लाख से अधिक है, तो क्या ओ बी सी प्रमाणपत्र मिल सकता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Nahi, agar parivar ki salana aamdani 8 lakh se jyada hai to OBC certificate nahi mil sakta. OBC certificate ke liye income limit 8 lakh se kam honi chahiye. Agar aapki aamdani 8 lakh se zyada hai to aap OBC category ke liye eligible nahi hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 31 | Domicile Certificate | `What is the exact residency criteria or years of stay required to get a Domicile Certificate in Chhattisgarh?` | EN (en) | 7 | new_topic | N/A | 4.80s | ✅ SUCCESS |

### Query 31 Details
* **Query**: `What is the exact residency criteria or years of stay required to get a Domicile Certificate in Chhattisgarh?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the exact residency criteria or years of stay required to get a Domicile Certificate in Chhattisgarh?`
* **Resolved Hindi Translation**: `छत्तीसगढ़ में domicile certificate प्राप्त करने के लिए सटीक निवास मानदंड या रहने के वर्षों की आवश्यकता क्या है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the official rules, the residency criteria for a Domicile Certificate in Chhattisgarh are as follows:

**Main Path (Both Criteria One and Criteria Two must be met):**
- **Criteria One (Criteria A):** You must satisfy at least one of these:
  - Born in Chhattisgarh (Birth Certificate)
  - Either parent has been a resident of Chhattisgarh for continuous 25 years
  - Either parent is an employee of the Chhattisgarh Government or its undertaking
  - Either parent or the applicant holds property in Chhattisgarh for the last 5 years
- **Criteria Two (Criteria B):** You must satisfy at least one of these:
  - Three years of formal education in Chhattisgarh
  - Passed one of the board exams (Class 5, 8, 10, or 12) from Chhattisgarh

**Exceptions (Criteria Three):**
If you do not meet the main path criteria, you may still be eligible if:
- Your spouse is a domicile of Chhattisgarh
- The applicant or spouse is an employee of the Chhattisgarh Government or its PSU
- The applicant or parent is in the All India Services and has been allotted a Chhattisgarh cadre

The 15-year stay proof is required only if Criteria One (A) is applicable, not as a standalone requirement.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 32 | Domicile Certificate | `Niwas praman patra cg ke liye exceptions kya hain? Jaise central govt employees ke liye?` | HINGLISH (hinglish) | 7 | new_topic | N/A | 5.43s | ✅ SUCCESS |

### Query 32 Details
* **Query**: `Niwas praman patra cg ke liye exceptions kya hain? Jaise central govt employees ke liye?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What are the exceptions for a domicile certificate in CG? For example, for central government employees?`
* **Resolved Hindi Translation**: `domicile certificate cg ke liye exceptions kya hain? Jaise central govt employees ke liye?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, CG domicile certificate ke liye exceptions hain.

Criteria Three (C) ke under, agar koi vyakti Criteria One aur Two ko poora nahi karta, toh bhi domicile certificate mil sakta hai.

Ye exceptions hain:
- Agar applicant ki spouse CG ki domicile hai
- Agar applicant ya spouse CG Government/PSU employee hai
- Agar applicant ya parent All India Services mein hain aur unhe CG cadre mila hai

Inmein Criteria One (CG mein janm, parents ka 25 saal CG mein rehna, parents CG employee, ya CG mein property) aur Criteria Two (CG mein 3 saal padhai ya Class 5, 8, 10, 12 ka exam pass karna) ki zaroorat nahi hoti.

Ye exceptions standalone hain, inka Criteria One aur Two se koi lena-dena nahi hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 33 | Domicile Certificate | `क्या छत्तीसगढ़ का निवास प्रमाण पत्र राज्य सरकार के सेवानिवृत्त (retired) कर्मचारियों के बच्चों को मिल सकता है?` | HI (hi) | 7 | new_topic | N/A | 3.25s | ✅ SUCCESS |

### Query 33 Details
* **Query**: `क्या छत्तीसगढ़ का निवास प्रमाण पत्र राज्य सरकार के सेवानिवृत्त (retired) कर्मचारियों के बच्चों को मिल सकता है?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hi`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a domicile certificate of Chhattisgarh be obtained by the children of retired government employees?`
* **Resolved Hindi Translation**: `क्या छत्तीसगढ़ का मूल निवासी प्रमाण पत्र राज्य सरकार के सेवानिवृत्त (retired) कर्मचारियों के बच्चों को मिल सकता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, छत्तीसगढ़ का मूल निवासी प्रमाण पत्र राज्य सरकार के सेवानिवृत्त कर्मचारियों के बच्चों को मिल सकता है।

**मानदंड तीन (C) के अंतर्गत:**
- यदि आवेदक या उसके माता-पिता में से कोई एक राज्य सरकार/सार्वजनिक क्षेत्र के उपक्रम (PSU) का कर्मचारी है, तो वे इसके पात्र हैं।
- यदि आवेदक या उसके माता-पिता अखिल भारतीय सेवा (AIS) में हैं और उन्हें छत्तीसगढ़ कैडर आवंटित किया गया है, तो वे इसके पात्र हैं।

**नोट:** इस श्रेणी के अंतर्गत निवास और शिक्षा संबंधी मानदंडों (मानदंड एक और दो) की आवश्यकता नहीं होती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)
  ```

---
| 34 | Domicile Certificate | `Kya domicile praman patra ke liye school study cg me minimum 3 saal hona zaroori hai?` | HINGLISH (hi) | 7 | new_topic | N/A | 4.66s | ✅ SUCCESS |

### Query 34 Details
* **Query**: `Kya domicile praman patra ke liye school study cg me minimum 3 saal hona zaroori hai?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hi`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is it necessary to have a minimum of 3 years of school study in CG for a domicile certificate?`
* **Resolved Hindi Translation**: `Kya domicile certificate ke liye school study cg me minimum 3 saal hona zaroori hai?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, domicile certificate के लिए CG में कम से कम 3 साल की स्कूल स्टडी होना अनिवार्य है। यह नियम Criteria Two (Criteria B) के तहत आता है, जिसमें कहा गया है कि आवेदक को CG में कम से कम 3 साल की औपचारिक शिक्षा पूरी करनी चाहिए। इसके अलावा, CG बोर्ड से 5वीं, 8वीं, 10वीं या 12वीं की परीक्षा पास करना भी एक विकल्प है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)
  ```

---
| 35 | Domicile Certificate | `How many days (SLA) does it take to issue a domicile certificate in Chhattisgarh?` | EN (en) | 7 | new_topic | N/A | 3.03s | ✅ SUCCESS |

### Query 35 Details
* **Query**: `How many days (SLA) does it take to issue a domicile certificate in Chhattisgarh?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How many days (SLA) does it take to issue a domicile certificate in Chhattisgarh?`
* **Resolved Hindi Translation**: `कितने दिन (एस एल ए) छत्तीसगढ़ में निवास प्रमाण पत्र जारी करने में लगते हैं?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The Domicile Certificate in Chhattisgarh takes 7 days to issue, as per the Service Level Agreement (SLA) mentioned in the official documents. This time limit is specified for the service delivery at the Tehsil Office.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 36 | Domicile Certificate | `Niwas praman patra ke liye voter ID card stay ka proof ban sakta hai kya?` | HINGLISH (hinglish) | 7 | new_topic | N/A | 5.78s | ✅ SUCCESS |

### Query 36 Details
* **Query**: `Niwas praman patra ke liye voter ID card stay ka proof ban sakta hai kya?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a voter ID card be proof of stay for a domicile certificate?`
* **Resolved Hindi Translation**: `क्या मतदाता पहचान पत्र किसी निवास प्रमाण पत्र के लिए निवास प्रमाण के रूप में कार्य कर सकता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, voter ID card ko nivas ka praman (stay ka proof) mana ja sakta hai.

Voter ID card mein aapke pate ka vivaran hota hai, jo nivas ke praman ke liye ek vaidha dastavez hai.

Lekin, dhyan dein ki domicile certificate ke liye 15 saal ka nivas ka praman chahiye, jabki voter ID mein sirf aapka vartaman pata hota hai. Isliye, voter ID ko nivas ka praman toh mana ja sakta hai, lekin yeh 15 saal ke nivas ke praman ka vikalp nahi ho sakta.

Aapko anya praman bhi dene pad sakte hain jaise:
- Bijli bill
- Ration card
- Sampatti ke kagazat

Ye sabhi vaikalpik praman hain, aur aap inmein se kisi bhi ek ka upyog kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 37 | Domicile Certificate | `निवास प्रमाण पत्र के लिए ऑनलाइन आवेदन शुल्क कितना है?` | HI (hi) | 7 | new_topic | N/A | 2.39s | ✅ SUCCESS |

### Query 37 Details
* **Query**: `निवास प्रमाण पत्र के लिए ऑनलाइन आवेदन शुल्क कितना है?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hi`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the online application fee for a native certificate?`
* **Resolved Hindi Translation**: `मूल निवासी प्रमाण पत्र के लिए ऑनलाइन आवेदन शुल्क कितना है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  ऑनलाइन आवेदन शुल्क 30 रुपये है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)
  ```

---
| 38 | Domicile Certificate | `Can a student born in CG but studying college in Delhi apply for CG domicile certificate?` | EN (en) | 7 | new_topic | N/A | 3.57s | ✅ SUCCESS |

### Query 38 Details
* **Query**: `Can a student born in CG but studying college in Delhi apply for CG domicile certificate?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a student born in CG but studying college in Delhi apply for CG domicile certificate?`
* **Resolved Hindi Translation**: `क्या CG में पैदा हुए छात्र, जो दिल्ली में कॉलेज पढ़ रहे हैं, CG निवास प्रमाण पत्र के लिए आवेदन कर सकते हैं?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, CG में जन्मे छात्र जो दिल्ली में कॉलेज पढ़ रहे हैं, वे CG निवास प्रमाण पत्र के लिए आवेदन कर सकते हैं।

CG निवास प्रमाण पत्र के लिए Criteria Two (शिक्षा) के तहत, 3 साल की औपचारिक शिक्षा CG में होना या Class 5, 8, 10, 12 की बोर्ड परीक्षा CG से पास करना आवश्यक है। चूंकि छात्र दिल्ली में कॉलेज पढ़ रहा है, इसलिए यह Criteria Two की शर्त पूरी नहीं करता।

हालांकि, Criteria One (निवास) के तहत, यदि छात्र के माता-पिता CG के निवासी हैं या उनकी CG में संपत्ति है, तो वे CG निवास प्रमाण पत्र के लिए पात्र हो सकते हैं।

यदि छात्र के माता-पिता CG के निवासी नहीं हैं और न ही उनकी CG में संपत्ति है, तो वे Criteria One और Criteria Two दोनों की शर्तों को पूरा नहीं करते, इसलिए वे CG निवास प्रमाण पत्र के लिए आवेदन नहीं कर सकते।

छात्र को CG निवास प्रमाण पत्र के लिए आवेदन करने हेतु माता-पिता के निवास या संपत्ति के संबंध में अतिरिक्त जानकारी प्रदान करनी होगी।

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 39 | Domicile Certificate | `Domicile certificate apply karne ka offline form pdf kahan se download karein?` | HINGLISH (hinglish) | 7 | new_topic | N/A | 4.26s | ✅ SUCCESS |

### Query 39 Details
* **Query**: `Domicile certificate apply karne ka offline form pdf kahan se download karein?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Where to download the offline form pdf for applying a domicile certificate?`
* **Resolved Hindi Translation**: `Domicile certificate apply karne ka offline form pdf kahan se download karein?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  आप domicile certificate के लिए offline form pdf यहाँ से डाउनलोड कर सकते हैं:

1. **Sewa Setu Portal**: https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं
2. **Revenue Department Website**: https://cgstate.gov.in/revenue-disaster-management-department पर जाएं
3. **Tehsil Office**: अपने नजदीकी तहसील कार्यालय में जाकर form मांग सकते हैं

फॉर्म डाउनलोड करने के लिए आपको लॉगिन करना होगा। अगर लॉगिन नहीं कर पा रहे हैं तो पहले Sewa Setu पर अकाउंट बनाएं।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 40 | Domicile Certificate | `छत्तीसगढ़ के मूल निवासी प्रमाण पत्र के लिए सक्षम प्राधिकारी कौन है?` | HI (hi) | 7 | new_topic | N/A | 2.40s | ✅ SUCCESS |

### Query 40 Details
* **Query**: `छत्तीसगढ़ के मूल निवासी प्रमाण पत्र के लिए सक्षम प्राधिकारी कौन है?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hi`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Who is the competent authority for a certificate of origin from Chhattisgarh?`
* **Resolved Hindi Translation**: `छत्तीसगढ़ के मूल निवासी प्रमाण पत्र के लिए सक्षम प्राधिकारी कौन है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  राजस्व एवं आपदा प्रबंधन विभाग के अंतर्गत, मूल निवासी प्रमाण पत्र के लिए सक्षम प्राधिकारी अनुविभागीय अधिकारी (राजस्व) है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)
  ```

---
| 41 | Name Change | `Naam badalne ka gazette notification (Ordinary Gazette) ke liye kya step-by-step process hai?` | HINGLISH (hinglish) | 201 | new_topic | N/A | 4.77s | ✅ SUCCESS |

### Query 41 Details
* **Query**: `Naam badalne ka gazette notification (Ordinary Gazette) ke liye kya step-by-step process hai?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the step-by-step process for changing a name in the Ordinary Gazette?`
* **Resolved Hindi Translation**: `नाम बदलने का गजट नोटिफिकेशन (ऑर्डिनरी गजट) के लिए क्या स्टेप-बाय-स्टेप प्रोसेस है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Service: साधारण राजपत्र अधिसूचना के लिए step-by-step process:

1. **Sewa Setu Kendra पर जाएं**: सबसे पहले आप अपने नजदीकी Sewa Setu Kendra पर जाकर application form भर सकते हैं।

2. **Form भरें**: Online या offline दोनों तरीके से form भर सकते हैं। Online के लिए website पर जाएं, offline के लिए center पर जाकर form लें।

3. **Documents तैयार करें**: सभी जरूरी documents जैसे SBI challan, notarized affidavit, newspaper publication, deed form, और identity cards तैयार रखें।

4. **Fee जमा करें**: Online या center पर ₹30.0 की fee जमा करें।

5. **Verification**: सभी documents की verification की जाएगी।

6. **Processing**: 29 दिनों के अंदर process पूरा हो जाएगा।

7. **Final Notification**: Gazette notification publish हो जाएगा।

**Important**: सभी documents original होने चाहिए और time limit के अंदर submit करने होंगे। Late registration पर penalty apply हो सकती है।

Kya aap koi specific step ke baare mein aur jaankari chahte hain?

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 42 | Name Change | `What is the exact advertisement fee for publication of name change in Ordinary Gazette?` | EN (en) | 201 | new_topic | N/A | 3.61s | ✅ SUCCESS |

### Query 42 Details
* **Query**: `What is the exact advertisement fee for publication of name change in Ordinary Gazette?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the exact advertisement fee for publication of name change in Ordinary Gazette?`
* **Resolved Hindi Translation**: `विज्ञापन शुल्क की सटीक राशि क्या है? साधारण राजपत्र (ऑर्डिनरी गजट) में नाम परिवर्तन के प्रकाशन के लिए?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The exact advertisement fee for publication of name change in Ordinary Gazette is ₹30.0. This fee is required for submitting the publication of the notice for name change in Form-I in a local newspaper. The advertisement must not be more than 3 months old from the date of application.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 43 | Name Change | `नाम बदलने के लिए विज्ञापन प्रकाशन हेतु कितने गवाहों (witnesses) की आवश्यकता होती है?` | HI (hi) | 201 | new_topic | N/A | 3.21s | ✅ SUCCESS |

### Query 43 Details
* **Query**: `नाम बदलने के लिए विज्ञापन प्रकाशन हेतु कितने गवाहों (witnesses) की आवश्यकता होती है?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hi`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How many witnesses are required to publish an advertisement for a name change?`
* **Resolved Hindi Translation**: `नाम बदलने के लिए विज्ञापन प्रकाशन हेतु कितने गवाहों (witnesses) की आवश्यकता होती है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नाम परिवर्तन के लिए विज्ञापन प्रकाशन हेतु दो गवाहों की आवश्यकता होती है। गवाहों के नाम, हस्ताक्षर और पते के साथ प्ररूप-दो में विलिख प्ररूप की मूल प्रति अनिवार्य है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)
  ```

---
| 44 | Name Change | `Gazette notification me name change ke liye stamp paper par affidavit kahan se notary karwayein?` | HINGLISH (hinglish) | 201 | new_topic | N/A | 3.99s | ✅ SUCCESS |

### Query 44 Details
* **Query**: `Gazette notification me name change ke liye stamp paper par affidavit kahan se notary karwayein?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Where to get an affidavit on stamp paper notarized for name change in Gazette notification?`
* **Resolved Hindi Translation**: `गेज़ेट अधिसूचना में नाम परिवर्तन के लिए स्टैम्प पेपर पर अफ़िडेविट कहाँ से नोटरी करवाएँ?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Aapki naam parivartan ki gazat adhisankhya ke liye affidavit ko stamp paper par notarize karwana hoga. Iske liye aap kisi bhi Notary Public ya Notary Office mein ja sakte hain. Notary office mein ja kar affidavit ko ₹50 ke non-judicial stamp paper par notarize karwaen. Notary ke paas affidavit ka original copy aur ₹50 ka stamp paper dono lekar jaen. Notary aapke affidavit ko verify karke notarize kar dega. Iske baad aap ise Gazette notification ke liye use kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 45 | Name Change | `What is the SLA timeline for the publication of name change in CG Ordinary Gazette?` | EN (en) | 201 | new_topic | N/A | 2.23s | ✅ SUCCESS |

### Query 45 Details
* **Query**: `What is the SLA timeline for the publication of name change in CG Ordinary Gazette?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the SLA timeline for the publication of name change in CG Ordinary Gazette?`
* **Resolved Hindi Translation**: `CG साधारण राजपत्र में नाम परिवर्तन के प्रकाशन के लिए एस एल ए समय-सीमा क्या है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The SLA timeline for the publication of name change in CG Ordinary Gazette is 29 days.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 46 | Name Change | `Gazette publication name change advertisement ke liye Form-I aur Form-II kahan se milega?` | HINGLISH (hinglish) | 201 | new_topic | N/A | 3.40s | ✅ SUCCESS |

### Query 46 Details
* **Query**: `Gazette publication name change advertisement ke liye Form-I aur Form-II kahan se milega?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Where can I get Form-I and Form-II for Gazette publication name change advertisement?`
* **Resolved Hindi Translation**: `गेज़ेट प्रकाशन नाम परिवर्तन विज्ञापन के लिए फॉर्म-I और फॉर्म-II कहाँ से मिलेगा?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Form-I aur Form-II ke liye aapko Sewa Setu portal se download karna hoga. Yeh forms service details manual mein available hain. Aap directly link https://sewasetu.cgstate.gov.in/home?lang=hi par jaakar forms download kar sakte hain. Forms ka format bhi yahan se download kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 47 | Name Change | `क्या किसी नाबालिग बच्चे (minor child) का नाम बदलने के लिए उसके माता-पिता आवेदन कर सकते हैं?` | HI (hi) | 201 | new_topic | N/A | 2.60s | ✅ SUCCESS |

### Query 47 Details
* **Query**: `क्या किसी नाबालिग बच्चे (minor child) का नाम बदलने के लिए उसके माता-पिता आवेदन कर सकते हैं?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hi`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can parents apply to change the name of a minor child?`
* **Resolved Hindi Translation**: `क्या किसी नाबालिग बच्चे (minor child) का नाम बदलने के लिए उसके माता-पिता आवेदन कर सकते हैं?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, माता-पिता अपने नाबालिग बच्चे का नाम बदलने के लिए आवेदन कर सकते हैं। इसके लिए माता-पिता को बच्चे के जन्म प्रमाण पत्र, स्कूल का प्रमाण पत्र, और बच्चे के नाम परिवर्तन के लिए एक शपथ पत्र (affidavit) की आवश्यकता होगी। यह प्रक्रिया बच्चे के कानूनी अभिभावक के रूप में माता-पिता के अधिकार के तहत की जाती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)
  ```

---
| 48 | Name Change | `How can I download a digital copy of the published gazette notification for my name change?` | EN (en) | 201 | new_topic | N/A | 4.61s | ✅ SUCCESS |

### Query 48 Details
* **Query**: `How can I download a digital copy of the published gazette notification for my name change?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How can I download a digital copy of the published gazette notification for my name change?`
* **Resolved Hindi Translation**: `डिजिटल प्रति प्राप्त करने के लिए मैं प्रकाशित राजपत्र अधिसूचना की प्रति कैसे डाउनलोड कर सकता हूँ?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  To download a digital copy of the published gazette notification for your name change, you need to submit the required documents and then access the notification through the Sewa Setu portal.

First, ensure you have all mandatory documents ready:
- Original challan of ₹430 from any State Bank of India branch
- Notarized affidavit in Form-III on ₹50 non-judicial stamp paper (not older than 3 months)
- Original copy of the publication of the notice for name change in Form-I in a local newspaper (not older than 3 months)
- Original copy of the deed form in Form-II with names, signatures, and addresses of 2 witnesses
- Old name and new name verification document
- All documents mentioned in your affidavit
- Government-issued identity card of the applicant
- Government-issued identity card of the witnesses

After submitting these documents at a Sewa Setu Kendra or online, you can access the gazette notification. The notification will be available in Form-I, which contains details about your name change. You can download this digital copy from the portal after the publication process is complete.

The entire process takes 29 days as per the service timeline. You can track your application status through the Sewa Setu portal using your application number.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 49 | Name Change | `Name change advertisement ke liye local newspaper me chhapwana compulsory hai kya?` | HINGLISH (hinglish) | 201 | new_topic | N/A | 2.65s | ✅ SUCCESS |

### Query 49 Details
* **Query**: `Name change advertisement ke liye local newspaper me chhapwana compulsory hai kya?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is it compulsory to get a name change advertisement printed in a local newspaper?`
* **Resolved Hindi Translation**: `क्या स्थानीय समाचार पत्र में नाम परिवर्तन के विज्ञापन के लिए छपना अनिवार्य है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, local newspaper me name change advertisement chhapwana compulsory hai. Yeh service ke liye required document hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 50 | Name Change | `राजपत्र (gazette) में नाम परिवर्तन प्रकाशन के लिए कुल कितना सरकारी खर्च आता है?` | HI (hi) | 201 | new_topic | N/A | 2.26s | ✅ SUCCESS |

### Query 50 Details
* **Query**: `राजपत्र (gazette) में नाम परिवर्तन प्रकाशन के लिए कुल कितना सरकारी खर्च आता है?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hi`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the total government expenditure for publishing a name change in the gazette?`
* **Resolved Hindi Translation**: `राजपत्र (gazette) में नाम परिवर्तन प्रकाशन के लिए कुल कितना सरकारी खर्च आता है?`
* **Grounding Status**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  राजपत्र (गजट) में नाम परिवर्तन के प्रकाशन के लिए कुल सरकारी खर्च 30 रुपये है। यह शुल्क ऑनलाइन आवेदन के माध्यम से या सेवा सेतु केंद्र पर व्यक्तिगत रूप से भुगतान किया जा सकता है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)
  ```

---
