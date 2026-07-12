# SewaSetu RAG Chatbot: 50 Random Real-Life Queries Test Results

This audit report captures testing the RAG chatbot with 50 diverse, random, real-life queries. The questions cover all 5 scoped services of the SewaSetu Chhattisgarh Portal with a realistic mix of English, Hindi, and Hinglish queries.

## Execution Summary Table

| ID | Service Category | User Query | Language | Mapped Service ID | Intent | Latency | Status |
|----|------------------|------------|----------|-------------------|--------|---------|--------|
| 1 | Marriage Registration | `What is the official government fee to get a marriage certificate online in Chhattisgarh?` | EN (en) | 3 | new_topic | 3.10s | ✅ SUCCESS |

### Query 1 Details
* **Query**: `What is the official government fee to get a marriage certificate online in Chhattisgarh?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the official government fee to get a marriage registration and certificate online in Chhattisgarh?`
* **Resolved Hindi Translation**: `छत्तीसगढ़ में ऑनलाइन विवाह पंजीकरण और प्रमाणपत्र प्राप्त करने के लिए आधिकारिक सरकारी शुल्क क्या है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The official government fee for marriage registration and certificate in Chhattisgarh is ₹30.0. This fee can be paid either online or at a kiosk. The online fee is ₹30.0, and the kiosk fee is also ₹30.0. The service is provided through the Sewa Setu portal.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 2 | Marriage Registration | `Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?` | HINGLISH (N/A) | 3 | new_topic | 1.95s | ✅ SUCCESS |

### Query 2 Details
* **Query**: `Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `N/A`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Kya aap Marriage Registration & Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?
  ```

---
| 3 | Marriage Registration | `विवाह पंजीकरण के लिए आवश्यक दस्तावेजों की सूची क्या है?` | HI (N/A) | 3 | new_topic | 1.43s | ✅ SUCCESS |

### Query 3 Details
* **Query**: `विवाह पंजीकरण के लिए आवश्यक दस्तावेजों की सूची क्या है?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `N/A`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  क्या आप विवाह पंजीकरण एवं प्रमाण पत्र दस्तावेज़ चेकलिस्ट का उपयोग करके अपनी पात्रता जांचना चाहते हैं, या विस्तृत पात्रता मानदंडों की जानकारी देखना चाहते हैं, या सीधे अपने प्रश्न का उत्तर चाहते हैं?
  ```

---
| 4 | Marriage Registration | `Mera shadi ka card (invitation card) nahi hai, to kya online shadi register ho sakti hai?` | HINGLISH (hinglish) | 3 | new_topic | 3.16s | ✅ SUCCESS |

### Query 4 Details
* **Query**: `Mera shadi ka card (invitation card) nahi hai, to kya online shadi register ho sakti hai?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `My wedding card is not an invitation card, so can a wedding be registered online?`
* **Resolved Hindi Translation**: `मेरा शादी का कार्ड (इन्विटेशन कार्ड) नहीं है, तो क्या ऑनलाइन शादी रजिस्टर हो सकती है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Nahi, shaadi ka card nahi hone par bhi online shaadi register ho sakti hai. shaadi ka card ek anivarya dastaavez nahi hai. aapko anya aavashyak dastaavez jaise var aur vadhu ke janm pramaan patra, sanyukt photo, ghoshana patra aur anya dastaavez upload karne honge.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 5 | Marriage Registration | `Is there any penalty or extra fee if I register my marriage after 1 year of marriage in CG?` | EN (en) | 3 | new_topic | 2.89s | ✅ SUCCESS |

### Query 5 Details
* **Query**: `Is there any penalty or extra fee if I register my marriage after 1 year of marriage in CG?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is there any penalty or extra fee if I register my marriage after 1 year of marriage in CG?`
* **Resolved Hindi Translation**: `क्या सी जी में विवाह के एक वर्ष के बाद विवाह पंजीकृत करने पर कोई दंड या अतिरिक्त शुल्क है?`
* **Intermediate English Answer**:
  ```markdown
  I do not have sufficient information in my records to answer this question. Please check the Sewa Setu portal.
  ```
* **Intermediate Hindi Answer**:
  ```markdown
  मेरे पास इस प्रश्न का उत्तर देने के लिए रिकॉर्ड में पर्याप्त जानकारी नहीं है। कृपया सेवा सेतु पोर्टल पर जांच करें।
  ```
* **Final Synthesized Chatbot Response**:
  ```markdown
  I do not have sufficient information in my records to answer this question. Please check the Sewa Setu portal.
  ```

---
| 6 | Marriage Registration | `विवाह प्रमाण पत्र प्राप्त करने की समय सीमा (SLA) कितने दिनों की होती है?` | HI (hi) | 3 | new_topic | 2.52s | ✅ SUCCESS |

### Query 6 Details
* **Query**: `विवाह प्रमाण पत्र प्राप्त करने की समय सीमा (SLA) कितने दिनों की होती है?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hi`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the time limit (SLA) for marriage registration and obtaining the certificate?`
* **Resolved Hindi Translation**: `विवाह पंजीकरण एवं प्रमाण पत्र प्राप्त करने की समय सीमा (SLA) कितने दिनों की होती है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  विवाह पंजीकरण एवं प्रमाण पत्र प्राप्त करने की समय सीमा 15 दिन है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)
  ```

---
| 7 | Marriage Registration | `Online apply karne ke baad verification ke liye kya dono husband aur wife ko office jana padega?` | HINGLISH (hinglish) | 3 | follow_up | 3.89s | ✅ SUCCESS |

### Query 7 Details
* **Query**: `Online apply karne ke baad verification ke liye kya dono husband aur wife ko office jana padega?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `3`
* **Classified Intent**: `follow_up`
* **Resolved English Translation**: `After applying online, do both husband and wife need to go to the office for verification?`
* **Resolved Hindi Translation**: `भवन में ऑनलाइन आवेदन करने के बाद, क्या पति और पत्नी दोनों को सत्यापन के लिए कार्यालय जाना आवश्यक है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Nahi, dono pati-patni ko office jaane ki zaroorat nahi hai. Online application ke baad, verification process online hi poora ho jaata hai. Agar kisi bhi kaaran se verification zaroori ho, to officer se contact kiya ja sakta hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 8 | Marriage Registration | `Who acts as the Registrar of Marriages in a small village or rural area in CG?` | EN (en) | 3 | new_topic | 2.50s | ✅ SUCCESS |

### Query 8 Details
* **Query**: `Who acts as the Registrar of Marriages in a small village or rural area in CG?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Who acts as the Registrar of Marriages in a small village or rural area in CG?`
* **Resolved Hindi Translation**: `सी जी के किसी छोटे गाँव या ग्रामीण क्षेत्र में विवाह पंजीयक के रूप में कौन कार्य करता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  In a small village or rural area in Chhattisgarh, the Local Authority, specifically the Gram Panchayat, acts as the Registrar of Marriages. This is as per the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, which states that the Local Authority (Gram Panchayat, Municipality, or Municipal Corporation) is the registrar for its local area.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 9 | Marriage Registration | `क्या ग्रामीण क्षेत्रों में पंचायत सचिव विवाह का रजिस्ट्रेशन कर सकते हैं?` | HI (hi) | 3 | new_topic | 2.35s | ✅ SUCCESS |

### Query 9 Details
* **Query**: `क्या ग्रामीण क्षेत्रों में पंचायत सचिव विवाह का रजिस्ट्रेशन कर सकते हैं?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `hi`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can the Panchayat Secretary in rural areas register a marriage?`
* **Resolved Hindi Translation**: `क्या ग्रामीण क्षेत्रों में पंचायत सचिव विवाह का रजिस्ट्रेशन कर सकते हैं?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, ग्राम पंचायत सचिव विवाह का पंजीकरण नहीं कर सकते। विवाह का पंजीकरण स्थानीय क्षेत्र के रजिस्ट्रार द्वारा किया जाता है, जो ग्राम पंचायत, नगर पालिका या नगर निगम हो सकता है। यह सेवा शहरी प्रशासन और विकास विभाग के अंतर्गत आती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=hi)
  ```

---
| 10 | Marriage Registration | `I got married in a temple in Bhilai. Can I get a government marriage certificate?` | EN (en) | 3 | new_topic | 3.91s | ✅ SUCCESS |

### Query 10 Details
* **Query**: `I got married in a temple in Bhilai. Can I get a government marriage certificate?`
* **Service Category**: Marriage Registration (Target SNO: 1)
* **Detected Language**: `en`
* **Classified Service ID**: `3`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `I got married in a temple in Bhilai. Can I get a government marriage registration and certificate?`
* **Resolved Hindi Translation**: `मैं भी भील में एक मंदिर में शादी की है। क्या मुझे सरकारी विवाह पंजीकरण और प्रमाण पत्र मिल सकता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Yes, you can get a government marriage registration and certificate for your marriage in a temple in Bhilai.

Under the Chhattisgarh Compulsory Registration of Marriages Rules, you must register your marriage in the local area where it was solemnized, which is Bhilai in this case. The registration should be done at the Local Authority of that area, which would be the Gram Panchayat or Municipal Corporation depending on whether Bhilai is urban or rural.

The service is available through the Chhattisgarh Sewa Setu portal. The application process involves:
1. Creating an account on the Sewa Setu portal
2. Filling in the required details about your marriage
3. Uploading the mandatory documents
4. Paying the fee of ₹30 (either online or at a kiosk)
5. Submitting the application for verification

The required documents include:
- Affidavit (Mandatory)
- Combined photograph of groom and bride (2a size) (Mandatory)
- Birth certificate of groom (Mandatory)
- Birth certificate of bride (Mandatory)
- Document signed by both bride and groom (first page) (Mandatory)
- Document signed by both bride and groom (second page) (Mandatory)
- Copy of challan (Mandatory)
- Marriage invitation card (Mandatory)

The service has a time limit of 15 days for processing. After successful registration, you will receive a marriage certificate.

For more details, you can visit the Sewa Setu portal or contact the local registration office in Bhilai.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=3&lang=en)
  ```

---
| 11 | SC/ST Caste Certificate | `छत्तीसगढ़ में एससी एसटी जाति प्रमाण पत्र के लिए पात्रता मानदंड क्या हैं?` | HI (N/A) | 4 | new_topic | 1.52s | ✅ SUCCESS |

### Query 11 Details
* **Query**: `छत्तीसगढ़ में एससी एसटी जाति प्रमाण पत्र के लिए पात्रता मानदंड क्या हैं?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `N/A`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  क्या आप अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र दस्तावेज़ चेकलिस्ट का उपयोग करके अपनी पात्रता जांचना चाहते हैं, या विस्तृत पात्रता मानदंडों की जानकारी देखना चाहते हैं, या सीधे अपने प्रश्न का उत्तर चाहते हैं?
  ```

---
| 12 | SC/ST Caste Certificate | `Caste certificate st/sc ke liye kaun kaun se government documents mandatory hain?` | HINGLISH (N/A) | 4 | new_topic | 1.72s | ✅ SUCCESS |

### Query 12 Details
* **Query**: `Caste certificate st/sc ke liye kaun kaun se government documents mandatory hain?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `N/A`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Kya aap SC/ST Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?
  ```

---
| 13 | SC/ST Caste Certificate | `Is land record document (like B1/P2/Misal Bandobast) compulsory for SC certificate in CG?` | EN (N/A) | 4 | new_topic | 1.86s | ✅ SUCCESS |

### Query 13 Details
* **Query**: `Is land record document (like B1/P2/Misal Bandobast) compulsory for SC certificate in CG?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `N/A`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Would you like to check your eligibility for the SC/ST Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?
  ```

---
| 14 | SC/ST Caste Certificate | `Mera purana hand-written offline SC certificate hai. Use online digital cert me kaise convert karein?` | HINGLISH (hinglish) | 4 | new_topic | 3.92s | ✅ SUCCESS |

### Query 14 Details
* **Query**: `Mera purana hand-written offline SC certificate hai. Use online digital cert me kaise convert karein?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How to convert my old hand-written offline SC certificate to an online digital certificate?`
* **Resolved Hindi Translation**: `मेरा पुराना हस्तलिखित ऑफलाइन एस सी प्रमाणपत्र है। इसे ऑनलाइन डिजिटल प्रमाणपत्र में कैसे परिवर्तित करें?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, aapke purane hand-written SC certificate ko online digital certificate mein convert karne ke liye aapko Sewa Setu portal par apply karna hoga.

**Step-by-step process:**

1. **Portal par jayein:** https://sewasetu.cgstate.gov.in/home?lang=hi
2. **Login karein:** Apna account banayein ya existing account se login karein.
3. **Service select karein:** "SC/ST Certificate" (ID: 4) choose karein.
4. **Application form bharein:**
   - General details
   - Beneficiary details
   - Caste details (SC/ST)
   - Address details
5. **Documents upload karein:**
   - Purane hand-written certificate ki clear photo/scan upload karein.
   - Koi bhi supporting document (jaise domicile certificate, electricity bill) upload karein.
6. **Fee pay karein:** Rs. 30 ka online fee pay karein.
7. **Submit karein:** Form submit kar dein.

**Important points:**
- Application 22 days mein process ho jaata hai.
- Fee ek method se pay karna hai (online ya kiosk).
- Agar aapke paas purana certificate hai, toh uska clear scan zaroor upload karein.

Kya aapko application process ke kisi specific step mein help chahiye?

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 15 | SC/ST Caste Certificate | `क्या छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है?` | HI (hi) | 4 | new_topic | 3.25s | ✅ SUCCESS |

### Query 15 Details
* **Query**: `क्या छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hi`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a woman in Chhattisgarh obtain a caste certificate at her husband's address after marriage?`
* **Resolved Hindi Translation**: `क्या छत्तीसगढ़ में शादी के बाद किसी महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, शादी के बाद महिला को उसके पति के पते पर जाति प्रमाण पत्र मिल सकता है। इसके लिए आवेदन प्रक्रिया वही रहती है, बस पते का प्रमाण पत्र पति के पते पर होना चाहिए।

**मुख्य बिंदु:**
- आवेदन के लिए पति का पता अनिवार्य है।
- पते का प्रमाण पत्र (बिजली बिल, राशन कार्ड, आदि) पति के नाम पर होना चाहिए।
- आवेदन शुल्क 30 रुपये है, जो ऑनलाइन या सेवा सेतु केंद्र पर जमा किया जा सकता है।
- आवेदन की प्रक्रिया ई-डिस्ट्रिक्ट पोर्टल पर पूरी की जा सकती है।

**जरूरी दस्तावेज:**
- पति का पता प्रमाण पत्र (अनिवार्य)।
- जाति प्रमाण पत्र (अनिवार्य)।
- आवेदन फॉर्म में विवरण सही भरना।

**समय सीमा:**
- आवेदन जमा करने के 22 दिनों के भीतर प्रमाण पत्र जारी कर दिया जाएगा।

अगर आपके पास पति के पते का प्रमाण पत्र नहीं है, तो आप किसी भी सेवा सेतु केंद्र से इसे प्राप्त कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)
  ```

---
| 16 | SC/ST Caste Certificate | `How long does it take for the Tehsil office to issue a permanent ST caste certificate?` | EN (en) | 4 | new_topic | 3.11s | ✅ SUCCESS |

### Query 16 Details
* **Query**: `How long does it take for the Tehsil office to issue a permanent ST caste certificate?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `en`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How long does it take for the Tehsil office to issue a permanent ST caste certificate?`
* **Resolved Hindi Translation**: `\)`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the provided documents, the time limit for service delivery of a permanent ST caste certificate from the Tehsil office is 30 working days.

This information is found in the Chhattisgarh Lok Seva Guarantee Act, 2011 notification, which specifies the SLA details for various services, including the Permanent Caste Certificate (ST).

The relevant details are:
- **Service:** Permanent Caste Certificate (ST)
- **Office/Agency:** Tehsil Office
- **Time Limit for Service Delivery:** 30 Working Days
- **Competent Authority:** Collector

This applies to the issuance of a permanent ST caste certificate from the Tehsil office.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 17 | SC/ST Caste Certificate | `Caste certificate apply karne ke liye sewasetu portal ka direct link kya hai?` | HINGLISH (hinglish) | 4 | new_topic | 4.14s | ✅ SUCCESS |

### Query 17 Details
* **Query**: `Caste certificate apply karne ke liye sewasetu portal ka direct link kya hai?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the direct link for the Sewa Setu portal to apply for a caste certificate?`
* **Resolved Hindi Translation**: `Sewasetu पोर्टल पर जाति प्रमाण पत्र के लिए सीधा लिंक क्या है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Sewasetu portal पर caste certificate apply करने के लिए direct link यह है:

https://sewasetu.cgstate.gov.in/home?lang=hi

यह link Hindi language में है और आपको सीधे application form पर ले जाएगा। यहाँ पर आप online apply कर सकते हैं।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 18 | SC/ST Caste Certificate | `Which government officer is authorized to issue a permanent SC certificate in a district?` | EN (en) | 4 | new_topic | 4.06s | ✅ SUCCESS |

### Query 18 Details
* **Query**: `Which government officer is authorized to issue a permanent SC certificate in a district?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `en`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Which government officer is authorized to issue a permanent SC certificate in a district?`
* **Resolved Hindi Translation**: `कौन सा सरकारी अधिकारी किसी जिले में स्थायी एस सी प्रमाणपत्र जारी करने के लिए अधिकृत है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the provided documents, the authorized officer to issue a permanent SC certificate in a district is the Collector.

According to the SLA details in the source documents:
- For a Permanent Caste Certificate, the Competent Authority is the Collector.
- The Public Authority is the Sub-Divisional Officer (Revenue).

The relevant excerpt from the source documents states:
"2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):
   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)
   - Time Limit for Service Delivery (Working Days): 30 Working Days
   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)
   - Competent Authority: Collector (कलेक्टर)"

Therefore, the Collector is the competent authority who can issue the permanent SC certificate.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 19 | SC/ST Caste Certificate | `क्या जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर (digital signature) जरूरी है?` | HI (hi) | 4 | new_topic | 3.49s | ✅ SUCCESS |

### Query 19 Details
* **Query**: `क्या जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर (digital signature) जरूरी है?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hi`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is a digital signature required for the application of a caste certificate?`
* **Resolved Hindi Translation**: `क्या जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर (digital signature) जरूरी है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, जाति प्रमाण पत्र के आवेदन के लिए डिजिटल हस्ताक्षर अनिवार्य नहीं है। आप ऑनलाइन आवेदन के दौरान ई-हस्ताक्षर (e-sign) का उपयोग कर सकते हैं, लेकिन यह आवेदन जमा करने के लिए अनिवार्य शर्त नहीं है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=hi)
  ```

---
| 20 | SC/ST Caste Certificate | `SC caste praman patra online apply karne me portal aur kiosk charge kitna lagta hai?` | HINGLISH (hinglish) | 4 | new_topic | 3.54s | ✅ SUCCESS |

### Query 20 Details
* **Query**: `SC caste praman patra online apply karne me portal aur kiosk charge kitna lagta hai?`
* **Service Category**: SC/ST Caste Certificate (Target SNO: 2)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `4`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the portal and kiosk charge for applying for an SC caste certificate online?`
* **Resolved Hindi Translation**: `SC जाति प्रमाण पत्र ऑनलाइन आवेदन करने में पोर्टल और कियोस्क शुल्क कितना लगता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  SC/ST Certificate online apply करने के लिए portal और kiosk charge ₹30.0 है। यह fee online और kiosk दोनों जगह के लिए समान है।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=4&lang=en)
  ```

---
| 21 | OBC Caste Certificate | `OBC certificate banane ke liye creamy layer aur non-creamy layer ki income limit kitni hai?` | HINGLISH (hinglish) | 5 | new_topic | 2.90s | ✅ SUCCESS |

### Query 21 Details
* **Query**: `OBC certificate banane ke liye creamy layer aur non-creamy layer ki income limit kitni hai?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the income limit for the creamy layer and non-creamy layer for obtaining an OBC certificate?`
* **Resolved Hindi Translation**: `OBC प्रमाणपत्र बनाने के लिए क्रीमसी लेयर और नॉन-क्रीमसी लेयर की आय सीमा क्या है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  OBC certificate banane ke liye creamy layer aur non-creamy layer ki income limit alag-alag hoti hai. Creamy layer ki income limit ₹8 lakh per year hai, jabki non-creamy layer ki income limit ₹8 lakh se kam hoti hai. Agar aapki family income ₹8 lakh se zyada hai, toh aap creamy layer mein aate hain aur aapko OBC certificate nahi milega. Non-creamy layer ke liye income ₹8 lakh se kam honi chahiye. Ye limit state ke hisaab se bhi alag ho sakti hai, lekin Chhattisgarh mein ₹8 lakh ki limit standard hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 22 | OBC Caste Certificate | `ओबीसी जाति प्रमाण पत्र के लिए क्या निवास प्रमाण पत्र (domicile) जमा करना जरूरी है?` | HI (hi) | 5 | new_topic | 3.04s | ✅ SUCCESS |

### Query 22 Details
* **Query**: `ओबीसी जाति प्रमाण पत्र के लिए क्या निवास प्रमाण पत्र (domicile) जमा करना जरूरी है?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hi`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the original domicile certificate required for OBC caste certificate?`
* **Resolved Hindi Translation**: `ओबीसी जाति प्रमाण पत्र के लिए क्या मूल निवासी प्रमाण पत्र (domicile) जमा करना जरूरी है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, मूल निवासी प्रमाण पत्र (डोमिसाइल सर्टिफिकेट) ओबीसी प्रमाण पत्र के लिए अनिवार्य नहीं है।

स्रोत दस्तावेजों के अनुसार, मूल निवासी प्रमाण पत्र को "वैकल्पिक" (Optional) के रूप में सूचीबद्ध किया गया है। प्रमाण पत्र के लिए निवास का प्रमाण अनिवार्य है, लेकिन मूल निवासी प्रमाण पत्र को सहायक दस्तावेजों में से एक के रूप में ही शामिल किया गया है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)
  ```

---
| 23 | OBC Caste Certificate | `Can an OBC candidate apply for OBC certificate online on Sewa Setu portal?` | EN (hinglish) | 5 | new_topic | 3.66s | ✅ SUCCESS |

### Query 23 Details
* **Query**: `Can an OBC candidate apply for OBC certificate online on Sewa Setu portal?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can an OBC candidate apply for OBC certificate online on Sewa Setu portal?`
* **Resolved Hindi Translation**: `क्या एक ओ बी सी उम्मीदवार ऑनलाइन सेवा सेटू पोर्टल पर ओ बी सी प्रमाणपत्र के लिए आवेदन कर सकता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, aap Sewa Setu portal par online OBC certificate ke liye apply kar sakte hain.

Sewa Setu portal par OBC certificate ke liye online application ki facility available hai. Aap https://sewasetu.cgstate.gov.in/home?lang=hi par ja kar apply kar sakte hain.

Online application karne ke liye aapko kuch zaroori jaankari aur document ready rakhne honge, jaise:
- Aavedak ka vivaran
- Nivas ka praman
- Aay praman
- Anya pichhada varg ka praman

Kya aap application prakriya ke bare mein aur kuch jaanna chahte hain?

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 24 | OBC Caste Certificate | `OBC non-creamy layer praman patra ke liye self-declaration affidavit ka format kaisa hona chahiye?` | HINGLISH (hinglish) | 5 | new_topic | 5.13s | ✅ SUCCESS |

### Query 24 Details
* **Query**: `OBC non-creamy layer praman patra ke liye self-declaration affidavit ka format kaisa hona chahiye?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What should be the format of a self-declaration affidavit for an OBC non-creamy layer certificate?`
* **Resolved Hindi Translation**: `ओ बी सी नॉन-क्रीमी लेयर प्रमाण पत्र के लिए स्व-घोषणा शपथ पत्र का प्रारूप कैसा होना चाहिए?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  OBC non-creamy layer certificate के लिए self-declaration affidavit का format कुछ इस तरह होना चाहिए:

मैं श्री/श्रीमती/कुमारी [आवेदक का नाम] शपथपूर्वक यह कथन करता/करती हूं कि:

1. मैं [राज्य का नाम] का निवासी हूं और यहां [जिला/तहसील] में रह रहा/रही हूं।

2. मेरी सामाजिक स्थिति [जाति का नाम] है और मैं गैर-क्रीमी श्रेणी (non-creamy layer) से संबंधित हूं।

3. मैं यह प्रमाणित करता/करती हूं कि मैं क्रीमी श्रेणी की आय सीमा से नीचे हूं।

4. मैं यह भी प्रमाणित करता/करती हूं कि मेरे परिवार की वार्षिक आय [रकम] से अधिक नहीं है।

5. मैं यह घोषणा करता/करती हूं कि दी गई सभी जानकारी सत्य और सही है।

शपथकर्ता,
[आवेदक का नाम]
दिनांक: [दिनांक]
स्थान: [शहर/जिला]

यह affidavit नोटरी द्वारा notarized होना चाहिए।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 25 | OBC Caste Certificate | `छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि (validity period) कितनी होती है?` | HI (hi) | 5 | new_topic | 2.45s | ✅ SUCCESS |

### Query 25 Details
* **Query**: `छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि (validity period) कितनी होती है?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hi`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the validity period of Other Backward Class (OBC) certificate in Chhattisgarh?`
* **Resolved Hindi Translation**: `छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि (validity period) कितनी होती है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र की वैधता अवधि सेवा के समय से twenty-two दिन (22 दिन) होती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)
  ```

---
| 26 | OBC Caste Certificate | `What are the specific form fields and details required to be filled for OBC certificate application?` | EN (en) | 5 | new_topic | 4.78s | ✅ SUCCESS |

### Query 26 Details
* **Query**: `What are the specific form fields and details required to be filled for OBC certificate application?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `en`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What are the specific form fields and details required to be filled for OBC certificate application?`
* **Resolved Hindi Translation**: `ओ बी सी प्रमाणपत्र आवेदन के लिए किन विशिष्ट फॉर्म फील्ड्स और विवरणों को भरना आवश्यक है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the official specification, here are the specific form fields and details required for the OBC certificate application:

**General Details:**
- Beneficiary Guardian Type (Character)
- Beneficiary Guardian name (Text)
- Beneficiary Guardian Type in English (Character)
- Beneficiary Guardian name in English (Text)

**Personal Information:**
- Gender (Character)
- Marital Status (Character)
- Date of Birth (Date)
- Relation to Applicant (Character)

**Caste Information:**
- Caste OBC (Search)
- Category (Text)
- Caste In English (Text)
- Category In English (Text)
- Category Number (Text)

**Applicant Details:**
- Beneficiary name in English (Text)
- Present Address of Applicant (Section)
- Address (Textarea)
- PIN Code (Number)
- Post Box Number (Text)
- District (Character)
- Address In English (Textarea)
- Is Present Address and Permanent Address is same (Character)
- Permanent Address of Applicant (Section)

**Additional Fields:**
- Police Station (Search)
- Address Before or on Date 26/12/1984 (Section)
- Village or Town (Text)
- Patwari Halka Number (Number)
- Tehsil (Text)
- District (Data List)
- Name of Head Of Family on This Date (Text)
- Applicant Relation to Head of Family (Character)
- Address Details of Applicant/his Father / Mother/ Guardian from Year 26/12/1984 to till Date (Section)
- Address Details of Applicants Guardian (Fieldset)
- I, hereby give my consent to automatic filing of a complaint/Appeal on my behalf before the Competent Officer under Rule 6 of the Lok Seva Guarantee Rules, 2011, in the event that the applied service is not delivered within the stipulated time (Character)

**Application Process:**
1. Register on the e-District portal
2. Search for the service
3. Fill in basic applicant information
4. Fill in permanent address details
5. Fill in OBC certificate application form (Part 1 and 2)
6. Upload required documents
7. Preview and submit application
8. Pay fee (₹30.0)
9. Save acknowledgment

**Time Limit:** 22 days for service delivery.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 27 | OBC Caste Certificate | `OBC certificate apply karte waqt lok seva kendra ya kiosk center me kitna extra charge liya jata hai?` | HINGLISH (hinglish) | 5 | new_topic | 2.57s | ✅ SUCCESS |

### Query 27 Details
* **Query**: `OBC certificate apply karte waqt lok seva kendra ya kiosk center me kitna extra charge liya jata hai?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How much extra charge is taken at the Lok Seva Kendra or Kiosk Center while applying for an OBC certificate?`
* **Resolved Hindi Translation**: `लोक सेवा केंद्र या कियोस्क सेंटर में OBC प्रमाणपत्र आवेदन के दौरान कितना अतिरिक्त शुल्क लिया जाता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  OBC certificate apply karne ke liye lok seva kendra ya kiosk center mein ₹30.0 extra charge liya jata hai. Yeh fee online aur dono tarah se apply karne ke liye same hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 28 | OBC Caste Certificate | `क्या किसी निजी स्कूल (private school) का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त है?` | HI (hi) | 5 | new_topic | 3.32s | ✅ SUCCESS |

### Query 28 Details
* **Query**: `क्या किसी निजी स्कूल (private school) का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त है?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hi`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is a private school's study certificate sufficient for OBC certificate?`
* **Resolved Hindi Translation**: `क्या किसी निजी स्कूल (private school) का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, निजी स्कूल का पढ़ाई प्रमाण पत्र ओबीसी प्रमाण पत्र के लिए पर्याप्त नहीं है।

OBC प्रमाण पत्र के लिए शैक्षणिक प्रमाण पत्र अनिवार्य है, लेकिन यह प्रमाण पत्र किसी मान्यता प्राप्त स्कूल या बोर्ड से होना चाहिए। निजी स्कूल का प्रमाण पत्र तभी मान्य माना जाता है जब वह स्कूल राज्य सरकार द्वारा मान्यता प्राप्त हो और उसका पाठ्यक्रम बोर्ड द्वारा निर्धारित हो।

यदि निजी स्कूल मान्यता प्राप्त नहीं है, तो अन्य प्रमाण जैसे:
- 10वीं कक्षा का प्रमाण पत्र
- 12वीं कक्षा का प्रमाण पत्र
- स्कूल छोड़ने का प्रमाण पत्र (Migration Certificate)

उपयोग किया जा सकता है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=hi)
  ```

---
| 29 | OBC Caste Certificate | `Is a separate income certificate mandatory to get a non-creamy layer OBC certificate?` | EN (en) | None | new_topic | 2.04s | ✅ SUCCESS |

### Query 29 Details
* **Query**: `Is a separate income certificate mandatory to get a non-creamy layer OBC certificate?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `en`
* **Classified Service ID**: `None`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is a separate income certificate mandatory to get a non-creamy layer OBC certificate?`
* **Resolved Hindi Translation**: `क्या एक अलग आय प्रमाण पत्र गैर-क्रीमी परत ओ बी सी प्रमाण पत्र प्राप्त करने के लिए अनिवार्य है?`
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
  I do not have sufficient information in my records to answer this question. Please check the Sewa Setu portal.
  ```

---
| 30 | OBC Caste Certificate | `Bhai, agar parivar ki salana aamdani 8 lakh se jyada hai, to kya OBC certificate mil sakta hai?` | HINGLISH (hinglish) | 5 | new_topic | 3.34s | ✅ SUCCESS |

### Query 30 Details
* **Query**: `Bhai, agar parivar ki salana aamdani 8 lakh se jyada hai, to kya OBC certificate mil sakta hai?`
* **Service Category**: OBC Caste Certificate (Target SNO: 3)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `5`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `If the annual income of the family is more than 8 lakh, can an OBC certificate be obtained?`
* **Resolved Hindi Translation**: `भाई, अगर परिवार की वार्षिक आय 8 लाख से अधिक है, तो क्या ओ बी सी प्रमाणपत्र मिल सकता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Nahi, agar parivar ki salana aamdani 8 lakh se jyada hai to OBC certificate nahi mil sakta. OBC certificate ke liye income limit 8 lakh se kam honi chahiye. Agar aapki aamdani 8 lakh se zyada hai to aap OBC certificate ke liye apply nahi kar sakte. Aapko income certificate ki zaroorat hogi jo batayega ki aapki aamdani kitni hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=5&lang=en)
  ```

---
| 31 | Domicile Certificate | `What is the exact residency criteria or years of stay required to get a Domicile Certificate in Chhattisgarh?` | EN (N/A) | 7 | new_topic | 2.07s | ✅ SUCCESS |

### Query 31 Details
* **Query**: `What is the exact residency criteria or years of stay required to get a Domicile Certificate in Chhattisgarh?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `N/A`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Would you like to check your eligibility for the Domicile Certificate using the interactive document checklist, view the detailed criteria rules, or get a direct answer to your question?
  ```

---
| 32 | Domicile Certificate | `Niwas praman patra cg ke liye exceptions kya hain? Jaise central govt employees ke liye?` | HINGLISH (N/A) | 7 | new_topic | 2.02s | ✅ SUCCESS |

### Query 32 Details
* **Query**: `Niwas praman patra cg ke liye exceptions kya hain? Jaise central govt employees ke liye?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `N/A`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Kya aap Domicile Certificate ke document checklist se apni eligibility check karna chahte hain, ya detailed eligibility criteria rules dekhna chahte hain, ya directly apne sawal ka jawab chahte hain?
  ```

---
| 33 | Domicile Certificate | `क्या छत्तीसगढ़ का निवास प्रमाण पत्र राज्य सरकार के सेवानिवृत्त (retired) कर्मचारियों के बच्चों को मिल सकता है?` | HI (hi) | 7 | new_topic | 3.42s | ✅ SUCCESS |

### Query 33 Details
* **Query**: `क्या छत्तीसगढ़ का निवास प्रमाण पत्र राज्य सरकार के सेवानिवृत्त (retired) कर्मचारियों के बच्चों को मिल सकता है?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hi`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a domicile certificate of Chhattisgarh be obtained by the children of retired government employees?`
* **Resolved Hindi Translation**: `क्या छत्तीसगढ़ का मूल निवासी प्रमाण पत्र राज्य सरकार के सेवानिवृत्त (retired) कर्मचारियों के बच्चों को मिल सकता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, छत्तीसगढ़ का मूल निवासी प्रमाण पत्र राज्य सरकार के सेवानिवृत्त कर्मचारियों के बच्चों को मिल सकता है।

सेवानिवृत्त सरकारी कर्मचारियों के बच्चों के लिए मूल निवासी प्रमाण पत्र हेतु पात्रता मानदंड निम्नलिखित हैं:

1. **मानदंड A (निवास):**
   - आवेदक का जन्म छत्तीसगढ़ में हुआ हो।
   - या आवेदक के माता-पिता में से कोई 25 वर्ष से अधिक समय से छत्तीसगढ़ में निवासी हो।
   - या आवेदक के माता-पिता में से कोई छत्तीसगढ़ सरकार/सार्वजनिक क्षेत्र के उपक्रम (PSU) का कर्मचारी हो।
   - या आवेदक के पास छत्तीसगढ़ में 5 वर्ष से अधिक समय से संपत्ति हो।

2. **मानदंड B (शिक्षा):**
   - आवेदक ने छत्तीसगढ़ में कम से कम 3 वर्ष की स्कूली शिक्षा पूरी की हो।
   - या आवेदक ने छत्तीसगढ़ बोर्ड से कक्षा 5, 8, 10, या 12 की परीक्षा उत्तीर्ण की हो।

सेवानिवृत्त सरकारी कर्मचारियों के बच्चों के लिए मानदंड A और B दोनों का पालन करना अनिवार्य है। यदि वे इन मानदंडों को पूरा करते हैं, तो वे मूल निवासी प्रमाण पत्र के लिए आवेदन कर सकते हैं।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)
  ```

---
| 34 | Domicile Certificate | `Kya domicile praman patra ke liye school study cg me minimum 3 saal hona zaroori hai?` | HINGLISH (hinglish) | 7 | new_topic | 3.73s | ✅ SUCCESS |

### Query 34 Details
* **Query**: `Kya domicile praman patra ke liye school study cg me minimum 3 saal hona zaroori hai?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is it necessary to have a minimum of 3 years of school study in CG for a domicile certificate?`
* **Resolved Hindi Translation**: `क्या domicile certificate के लिए school study cg me minimum 3 saal hona zaroori hai?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, domicile certificate ke liye school study CG mein minimum 3 saal hona zaroori hai. Ye Criteria Two (B) ke under aata hai.

Service details manual ke according, Criteria Two (B) options hain:
- 3 years of school study in CG
- Class 5, 8, 10, 12 board exam from CG

Agar aap ye criteria meet karte hain to aap domicile certificate ke liye apply kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 35 | Domicile Certificate | `How many days (SLA) does it take to issue a domicile certificate in Chhattisgarh?` | EN (en) | 7 | new_topic | 2.90s | ✅ SUCCESS |

### Query 35 Details
* **Query**: `How many days (SLA) does it take to issue a domicile certificate in Chhattisgarh?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How many days (SLA) does it take to issue a domicile certificate in Chhattisgarh?`
* **Resolved Hindi Translation**: `कितने दिन (एस एल ए) छत्तीसगढ़ में निवास प्रमाण पत्र जारी करने में लगते हैं?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The Domicile Certificate in Chhattisgarh takes 7 days to issue. This is specified as the Time Limit / SLA in the service details.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 36 | Domicile Certificate | `Niwas praman patra ke liye voter ID card stay ka proof ban sakta hai kya?` | HINGLISH (hinglish) | 7 | new_topic | 3.55s | ✅ SUCCESS |

### Query 36 Details
* **Query**: `Niwas praman patra ke liye voter ID card stay ka proof ban sakta hai kya?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a voter ID card be proof of stay for a domicile certificate?`
* **Resolved Hindi Translation**: `क्या मतदाता पहचान पत्र किसी निवास प्रमाण पत्र के लिए निवास प्रमाण के रूप में कार्य कर सकता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नहीं, voter ID card stay का proof नहीं बन सकता। Voter ID card सिर्फ address proof के लिए होता है, residence proof के लिए नहीं।

Stay का proof के लिए ये documents चाहिए:
- Birth Certificate
- Father/Guardian Service Certificate
- Job Service Certificate/Identity Card (अगर सरकारी/सरकारी के नीचे हो)
- Voters Identity Card (सिर्फ address proof के लिए)
- Land And House Document
- Ration Card
- Electricity Bill

Voter ID card में सिर्फ address होता है, stay का proof नहीं।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 37 | Domicile Certificate | `निवास प्रमाण पत्र के लिए ऑनलाइन आवेदन शुल्क कितना है?` | HI (hi) | 7 | new_topic | 2.42s | ✅ SUCCESS |

### Query 37 Details
* **Query**: `निवास प्रमाण पत्र के लिए ऑनलाइन आवेदन शुल्क कितना है?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hi`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the online application fee for a native certificate?`
* **Resolved Hindi Translation**: `मूल निवासी प्रमाण पत्र के लिए ऑनलाइन आवेदन शुल्क कितना है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  ऑनलाइन आवेदन शुल्क 30.0 रुपये है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=hi)
  ```

---
| 38 | Domicile Certificate | `Can a student born in CG but studying college in Delhi apply for CG domicile certificate?` | EN (en) | 7 | new_topic | 3.07s | ✅ SUCCESS |

### Query 38 Details
* **Query**: `Can a student born in CG but studying college in Delhi apply for CG domicile certificate?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `en`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can a student born in CG but studying college in Delhi apply for CG domicile certificate?`
* **Resolved Hindi Translation**: `क्या CG में पैदा हुए छात्र, जो दिल्ली में कॉलेज पढ़ रहे हैं, CG निवास प्रमाण पत्र के लिए आवेदन कर सकते हैं?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Based on the eligibility criteria for a CG Domicile Certificate, a student born in CG who is currently studying in Delhi can apply for the certificate.

The eligibility is determined by meeting at least one option from Criteria One (A) and at least one option from Criteria Two (B).

1.  **Criteria One (A) - Residence in CG:** The applicant was born in CG, which satisfies the first option under Criteria One.
2.  **Criteria Two (B) - Education in CG:** The applicant has completed their schooling in CG. The criteria require either three years of formal education in CG or passing a board exam (Class 5, 8, 10, 12) from CG.

Since the applicant meets both the residence and education requirements, they are eligible to apply for the CG Domicile Certificate.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 39 | Domicile Certificate | `Domicile certificate apply karne ka offline form pdf kahan se download karein?` | HINGLISH (hinglish) | 7 | new_topic | 3.71s | ✅ SUCCESS |

### Query 39 Details
* **Query**: `Domicile certificate apply karne ka offline form pdf kahan se download karein?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `7`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Where to download the offline form pdf for applying a domicile certificate?`
* **Resolved Hindi Translation**: `Domicile certificate apply karne ka offline form pdf kahan se download karein?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  आप domicile certificate के offline form pdf यहाँ से डाउनलोड कर सकते हैं:

1. **Sewa Setu Portal**: https://sewasetu.cgstate.gov.in/home?lang=hi पर जाएं
2. **Sewa Setu Kendra**: अपने नजदीकी Sewa Setu Kendra पर जाकर form प्राप्त करें
3. **Revenue Department Office**: राजस्व विभाग के कार्यालय से form प्राप्त कर सकते हैं

ये सभी स्थान पर form उपलब्ध है। आप इनमें से किसी भी स्थान से form डाउनलोड कर सकते हैं।

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=7&lang=en)
  ```

---
| 40 | Domicile Certificate | `छत्तीसगढ़ के मूल निवासी प्रमाण पत्र के लिए सक्षम प्राधिकारी कौन है?` | HI (N/A) | N/A | identity | 1.05s | ✅ SUCCESS |

### Query 40 Details
* **Query**: `छत्तीसगढ़ के मूल निवासी प्रमाण पत्र के लिए सक्षम प्राधिकारी कौन है?`
* **Service Category**: Domicile Certificate (Target SNO: 4)
* **Detected Language**: `N/A`
* **Classified Service ID**: `N/A`
* **Classified Intent**: `identity`
* **Resolved English Translation**: `N/A`
* **Resolved Hindi Translation**: `N/A`
* **Final Synthesized Chatbot Response**:
  ```markdown
  मैं **सेवासेतु एआई सहायक** 🤖 हूँ — छत्तीसगढ़ सेवा सेतु पोर्टल पर उपलब्ध **सरकारी सेवाओं** में नागरिकों की मदद करने के लिए बनाया गया चैटबॉट।

मैं इनमें मदद कर सकता/सकती हूँ:
- 📄 किसी भी सेवा के लिए **आवश्यक दस्तावेज़**
- 💰 **शुल्क** और भुगतान के तरीके
- ✅ **पात्रता** मानदंड
- 🕐 सेवा वितरण की **समयसीमा** (SLA)
- 📝 **आवेदन प्रक्रिया**

कृपया इन सेवाओं के बारे में कुछ भी पूछें!
  ```

---
| 41 | Name Change | `Naam badalne ka gazette notification (Ordinary Gazette) ke liye kya step-by-step process hai?` | HINGLISH (hinglish) | 201 | new_topic | 4.04s | ✅ SUCCESS |

### Query 41 Details
* **Query**: `Naam badalne ka gazette notification (Ordinary Gazette) ke liye kya step-by-step process hai?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the step-by-step process for changing a name in the Ordinary Gazette?`
* **Resolved Hindi Translation**: `नाम बदलने का गजट नोटिफिकेशन (ऑर्डिनरी गजट) के लिए क्या स्टेप-बाय-स्टेप प्रोसेस है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Namaste! Naam badalne ke liye ordinary gazette notification ka step-by-step process yeh hai:

**Step 1: Required Documents taiyaar karein**
- SBI ka ₹430 ka challan (mandatory)
- ₹50 ka non-judicial stamp paper par notarized affidavit (Form-III)
- Local newspaper mein notice ka publication (Form-I) (3 mahine purana)
- Do witnesses ke saath deed form (Form-II)
- Old name aur new name verification document
- Sabhi documents ka reference (affidavit mein mention)
- Government-issued ID card (applicant)
- Government-issued ID card (witnesses)

**Step 2: Online Application karein**
- Sewa Setu portal par jayein: https://sewasetu.cgstate.gov.in/home?lang=hi
- Application form bharein (sabhi required fields fill karein)
- Documents upload karein (scanned copies)

**Step 3: Fee Payment karein**
- Online fee: ₹30 (kiosk fee: ₹30)
- Payment gateway se pay karein

**Step 4: Document Verification**
- Sabhi documents check karein
- Original documents verification ke liye ready rakhein

**Step 5: Processing**
- Application submit karein
- 29 days ke andar processing hogi

**Step 6: Gazette Notification**
- Gazette notification publish hoga
- Name change officially update ho jayega

Koi specific step ke baare mein aur jaankari chahiye?

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 42 | Name Change | `What is the exact advertisement fee for publication of name change in Ordinary Gazette?` | EN (en) | 201 | new_topic | 2.62s | ✅ SUCCESS |

### Query 42 Details
* **Query**: `What is the exact advertisement fee for publication of name change in Ordinary Gazette?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the exact advertisement fee for publication of name change in Ordinary Gazette?`
* **Resolved Hindi Translation**: `विज्ञापन शुल्क की सटीक राशि क्या है? साधारण राजपत्र (ऑर्डिनरी गजट) में नाम परिवर्तन के प्रकाशन के लिए?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The exact advertisement fee for publication of name change in Ordinary Gazette is ₹30.0. This fee is applicable whether you apply online or at a Sewa Setu Kendra. The advertisement must be published in a local newspaper and should not be more than 3 months old from the date of application.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 43 | Name Change | `नाम बदलने के लिए विज्ञापन प्रकाशन हेतु कितने गवाहों (witnesses) की आवश्यकता होती है?` | HI (hi) | 201 | new_topic | 2.20s | ✅ SUCCESS |

### Query 43 Details
* **Query**: `नाम बदलने के लिए विज्ञापन प्रकाशन हेतु कितने गवाहों (witnesses) की आवश्यकता होती है?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hi`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How many witnesses are required for a name change publication?`
* **Resolved Hindi Translation**: `नाम बदलने के लिए विज्ञापन प्रकाशन हेतु कितने गवाहों (witnesses) की आवश्यकता होती है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  नाम परिवर्तन के लिए विज्ञापन प्रकाशन हेतु दो गवाहों की आवश्यकता होती है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)
  ```

---
| 44 | Name Change | `Gazette notification me name change ke liye stamp paper par affidavit kahan se notary karwayein?` | HINGLISH (hinglish) | 201 | new_topic | 3.13s | ✅ SUCCESS |

### Query 44 Details
* **Query**: `Gazette notification me name change ke liye stamp paper par affidavit kahan se notary karwayein?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Where to get an affidavit on stamp paper notarized for a name change in Gazette notification?`
* **Resolved Hindi Translation**: `गेज़ट अधिसूचना में नाम परिवर्तन के लिए स्टैम्प पेपर पर अफ़िडेविट कहाँ से नोटरी करवाएँ?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Aapki naam parivartan ki affidavit ke liye aap kisi bhi bank ki branch mein jaakar notarization karwa sakte hain. Yahan par aapko ₹50 ka non-judicial stamp paper lena hoga, jo 3 mahine se purana nahi hona chahiye. Iske baad aap bank mein jaakar affidavit ko notarize karwa sakte hain. Yeh process bahut aasaan hai aur aap ise kisi bhi SBI branch mein kar sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 45 | Name Change | `What is the SLA timeline for the publication of name change in CG Ordinary Gazette?` | EN (en) | 201 | new_topic | 2.37s | ✅ SUCCESS |

### Query 45 Details
* **Query**: `What is the SLA timeline for the publication of name change in CG Ordinary Gazette?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the SLA timeline for the publication of name change in CG Ordinary Gazette?`
* **Resolved Hindi Translation**: `CG साधारण राजपत्र में नाम परिवर्तन के प्रकाशन के लिए एस एल ए समय-सीमा क्या है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  The SLA timeline for the publication of name change in CG Ordinary Gazette is 29 days.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 46 | Name Change | `Gazette publication name change advertisement ke liye Form-I aur Form-II kahan se milega?` | HINGLISH (hinglish) | 201 | new_topic | 2.58s | ✅ SUCCESS |

### Query 46 Details
* **Query**: `Gazette publication name change advertisement ke liye Form-I aur Form-II kahan se milega?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Where can I get Form-I and Form-II for Gazette publication name change advertisement?`
* **Resolved Hindi Translation**: `गेज़ेट प्रकाशन नाम परिवर्तन विज्ञापन के लिए फॉर्म-I और फॉर्म-II कहाँ से मिलेगा?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Form-I aur Form-II Gazette publication name change advertisement ke liye aapko Sewa Setu portal se download kar sakte hain. 

Sewa Setu portal par jaake "Ordinary Gazette Notification for Name Change" service select karke required forms milega. Forms ka direct link aapke application process mein provide kiya gaya hai.

Agar aapko forms download karne mein koi dikkat aa rahi hai to Sewa Setu Kendra se bhi help le sakte hain.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 47 | Name Change | `क्या किसी नाबालिग बच्चे (minor child) का नाम बदलने के लिए उसके माता-पिता आवेदन कर सकते हैं?` | HI (hi) | 201 | new_topic | 2.04s | ✅ SUCCESS |

### Query 47 Details
* **Query**: `क्या किसी नाबालिग बच्चे (minor child) का नाम बदलने के लिए उसके माता-पिता आवेदन कर सकते हैं?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hi`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Can parents apply to change the name of a minor child?`
* **Resolved Hindi Translation**: `क्या किसी नाबालिग बच्चे (minor child) का नाम बदलने के लिए उसके माता-पिता आवेदन कर सकते हैं?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  हाँ, माता-पिता अपने नाबालिग बच्चे का नाम बदलने के लिए आवेदन कर सकते हैं। इसके लिए माता-पिता को बच्चे के नाम परिवर्तन की अधिसूचना के लिए आवश्यक सभी दस्तावेजों के साथ आवेदन करना होगा।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)
  ```

---
| 48 | Name Change | `How can I download a digital copy of the published gazette notification for my name change?` | EN (en) | 201 | new_topic | 3.70s | ✅ SUCCESS |

### Query 48 Details
* **Query**: `How can I download a digital copy of the published gazette notification for my name change?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `en`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `How can I download a digital copy of the published gazette notification for my name change?`
* **Resolved Hindi Translation**: `डिजिटल प्रतिलिपि प्रकाशित राजपत्र अधिसूचना डाउनलोड कैसे कर सकते हैं?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  To download a digital copy of the published gazette notification for your name change, you can access it through the Sewa Setu portal. The notification is published in a local newspaper and is available for download from the portal's resources section.

You can find the gazette notification in the "Resources" section of the Sewa Setu portal. The notification will be in Form-I and should be no more than three months old from the date of application.

Additionally, you can download the required documents, including the publication of the notice for name change, from the following links:
- Publication of the notice in Form-I: https://sewasetu.cgstate.gov.in/resources/docFormat/23843.pdf
- Deed Form in Form-Ii: https://sewasetu.gov.in/resources/docFormat/23848.pdf

These documents are essential for completing the name change process. Ensure you have all the required documents before attempting to download or apply.

For more details and online application, please visit:
[Apply on Sewa Setu Portal](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 49 | Name Change | `Name change advertisement ke liye local newspaper me chhapwana compulsory hai kya?` | HINGLISH (hinglish) | 201 | new_topic | 2.34s | ✅ SUCCESS |

### Query 49 Details
* **Query**: `Name change advertisement ke liye local newspaper me chhapwana compulsory hai kya?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hinglish`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `Is it compulsory to get a name change advertisement printed in a local newspaper?`
* **Resolved Hindi Translation**: `क्या स्थानीय समाचार पत्र में नाम परिवर्तन के विज्ञापन के लिए छपना अनिवार्य है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  Haan, local newspaper me name change ka advertisement chhapwana compulsory hai. Ye service ke liye required document hai. Ye advertisement 3 mahine purana nahi hona chahiye aur local newspaper me publish karna zaroori hai. Ye process ka ek important step hai.

Adhik jaankari aur online apply karne ke liye, kripya is link par jayein:
[Sewa Setu Portal par Apply karein](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=en)
  ```

---
| 50 | Name Change | `राजपत्र (gazette) में नाम परिवर्तन प्रकाशन के लिए कुल कितना सरकारी खर्च आता है?` | HI (hi) | 201 | new_topic | 2.20s | ✅ SUCCESS |

### Query 50 Details
* **Query**: `राजपत्र (gazette) में नाम परिवर्तन प्रकाशन के लिए कुल कितना सरकारी खर्च आता है?`
* **Service Category**: Name Change (Target SNO: 5)
* **Detected Language**: `hi`
* **Classified Service ID**: `201`
* **Classified Intent**: `new_topic`
* **Resolved English Translation**: `What is the total government expenditure for publishing a name change in the gazette?`
* **Resolved Hindi Translation**: `राजपत्र (gazette) में नाम परिवर्तन प्रकाशन के लिए कुल कितना सरकारी खर्च आता है?`
* **Final Synthesized Chatbot Response**:
  ```markdown
  राजपत्र (गैजेट) में नाम परिवर्तन के प्रकाशन के लिए कुल सरकारी खर्च 30 रुपये है। यह शुल्क ऑनलाइन और कियोस्क, दोनों माध्यमों से लागू होता है।

अधिक जानकारी और ऑनलाइन आवेदन के लिए, कृपया यहाँ जाएँ:
[सेवा सेतु पोर्टल पर आवेदन करें](https://sewasetu.cgstate.gov.in/instractionPageNew.do?serviceId=201&lang=hi)
  ```

---
