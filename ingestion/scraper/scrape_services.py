import os
import re
import json
import time
import sys
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

# Force stdout to UTF-8 to prevent encoding issues when printing Hindi text
sys.stdout.reconfigure(encoding='utf-8')

# Configuration
SERVICE_IDS = [7, 3, 4, 5, 201]
LANGUAGES = ["en", "hi"]
BASE_URL = "https://sewasetu.cgstate.gov.in"
API_URL = "https://api-ed.cgstate.gov.in/api/application-management/edistrict2/applicationFormPreviewByServiceId"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Target Directories
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRAPED_DATA_DIR = os.path.join(WORKSPACE_DIR, "data")

DIRS = {
    "raw_html": os.path.join(SCRAPED_DATA_DIR, "raw_html"),
    "forms_json": os.path.join(SCRAPED_DATA_DIR, "forms_json"),
    "pdfs": os.path.join(SCRAPED_DATA_DIR, "pdfs"),
    "extracted_text": os.path.join(SCRAPED_DATA_DIR, "extracted_text"),
    "profiles": os.path.join(SCRAPED_DATA_DIR, "profiles")
}

def setup_directories():
    print("Setting up directory structure...")
    os.makedirs(SCRAPED_DATA_DIR, exist_ok=True)
    for name, path in DIRS.items():
        os.makedirs(path, exist_ok=True)
        print(f"  Folder ready: {path}")

def make_request(url, method="GET", payload=None, retries=3, delay=1.0, stream=False):
    for attempt in range(retries):
        try:
            if method.upper() == "POST":
                response = requests.post(url, headers=HEADERS, json=payload, timeout=20)
            else:
                response = requests.get(url, headers=HEADERS, timeout=20, stream=stream)
            
            if response.status_code == 200:
                return response
            else:
                print(f"    [Warning] Attempt {attempt+1} got HTTP {response.status_code} for URL: {url}")
        except Exception as e:
            print(f"    [Warning] Attempt {attempt+1} failed with error: {e}")
        time.sleep(delay * (attempt + 1))
    print(f"    [Error] Request failed completely for URL: {url}")
    return None

def resolve_url(relative_url):
    if not relative_url:
        return ""
    if relative_url.startswith("http://") or relative_url.startswith("https://"):
        return relative_url
    
    # Handle absolute path vs relative path joining
    relative_url = relative_url.strip()
    if relative_url.startswith("/"):
        return f"{BASE_URL}{relative_url}"
    else:
        # Check if we need to insert a slash
        # Some links in the previous HTML looked like resources/docFormat/...
        # and sewasetu.cgstate.gov.inresources/docFormat/... in the JSON.
        # Let's ensure a slash is always between base domain and resource path.
        return f"{BASE_URL}/{relative_url}"

def parse_detail_html(html_content, lang="en"):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Decompose script/style tags to avoid noise
    for s in soup(["script", "style"]):
        s.decompose()
        
    info = {
        "name": "",
        "department": "",
        "category": "",
        "sla": "",
        "required_documents": [],
        "fees": {
            "where_to_apply": "",
            "kiosk_fee": "",
            "online_fee": "",
            "raw_text": ""
        },
        "contact_details": "",
        "time_limit": "",
        "pdf_links": [],
        "how_to_apply": ""
    }
    
    # 1. Title, Department, Category
    title_div = soup.find('div', class_='service-title')
    if title_div:
        h4 = title_div.find('h4')
        span = title_div.find('span')
        if h4:
            info["name"] = re.sub(r'\s+', ' ', h4.text.strip()).strip()
        if span:
            info["department"] = re.sub(r'\s+', ' ', span.text.strip()).strip()
            
    # 2. Parse Panels / Right Columns (Fees, Contact, Time Limit, Instructions)
    right_tags = soup.find_all('div', class_='main-boxtag')
    for tag in right_tags:
        # Skip hidden boilerplate tags (e.g. instruction placeholders)
        style_attr = tag.get('style', '')
        if 'display:none' in style_attr.replace(' ', '').lower():
            continue
            
        doc_header = tag.find('div', class_='infonic-doc')
        if not doc_header:
            continue
            
        header_text = doc_header.text.strip().lower()
        body_div = tag.find('div', class_='main-info-b')
        if not body_div:
            continue
            
        body_text = re.sub(r'\s+', ' ', body_div.get_text(" ", strip=True)).strip()
        
        if 'document' in header_text or 'दस्तावेज' in header_text or 'दस्तावेज़' in header_text:
            # Table is parsed separately below, but let's gather document format PDF links here too
            for a in body_div.find_all('a'):
                href = a.get('href', '')
                if href and '.pdf' in href.lower():
                    info["pdf_links"].append({
                        "type": "document_format",
                        "text": a.text.strip(),
                        "url": resolve_url(href)
                    })
        elif 'fee' in header_text or 'शुल्क' in header_text:
            info["fees"]["raw_text"] = body_text
            # Extract Kiosk Fee (matching both English and Hindi)
            k_match = re.search(r'(?:Sewa Setu Kendra|Kendra|सेवा सेतु केंद्र|केंद्र)\s*:\s*(?:[\u20b9\u20b9]|\bRs\.?\b)?\s*([\d\.]+)', body_text, re.IGNORECASE)
            if k_match:
                info["fees"]["kiosk_fee"] = k_match.group(1).strip()
            # Extract Online Fee (matching both English and Hindi)
            o_match = re.search(r'(?:Online|ऑनलाइन)\s*:\s*(?:[\u20b9\u20b9]|\bRs\.?\b)?\s*([\d\.]+)', body_text, re.IGNORECASE)
            if o_match:
                info["fees"]["online_fee"] = o_match.group(1).strip()
            # Extract Where to Apply (matching both English and Hindi)
            w_match = re.search(r'(?:Where to Apply|आवेदन कहाँ करें)\??\s*(.*?)(?:Sewa Setu Kendra|Online|सेवा सेतु केंद्र|ऑनलाइन|$)', body_text, re.IGNORECASE)
            if w_match:
                info["fees"]["where_to_apply"] = w_match.group(1).strip().strip(':').strip()
        elif 'contact' in header_text or 'संपर्क' in header_text:
            info["contact_details"] = body_text
        elif 'service sla details' in header_text or 'sla' in header_text or ('समय सीमा' in header_text and any('.pdf' in a.get('href', '').lower() for a in body_div.find_all('a'))):
            for a in body_div.find_all('a'):
                href = a.get('href', '')
                if href and '.pdf' in href.lower():
                    info["pdf_links"].append({
                        "type": "sla_details",
                        "text": a.text.strip() or "Service SLA Details",
                        "url": resolve_url(href)
                    })
        elif 'time limit' in header_text or 'समय सीमा' in header_text:
            info["time_limit"] = body_text
            info["sla"] = body_text
        elif 'login' in header_text or 'लॉगिन' in header_text or 'लॉग इन' in header_text:
            login_a = body_div.find('a')
            if login_a:
                info["how_to_apply"] = resolve_url(login_a.get('href', ''))
        elif 'instruction' in header_text or 'user manual' in header_text or 'manual' in header_text or 'निर्देश' in header_text or 'पुस्तिका' in header_text:
            pdf_type = "user_manual" if "user manual" in header_text or "manual" in header_text else "instruction"
            for a in body_div.find_all('a'):
                href = a.get('href', '')
                if href and '.pdf' in href.lower():
                    info["pdf_links"].append({
                        "type": pdf_type,
                        "text": a.text.strip() or header_text.replace('🙍‍♂️', '').strip(),
                        "url": resolve_url(href)
                    })

    # 3. Parse Required Documents Table (More structured, groups sub-documents)
    table = soup.find('table')
    if table:
        rows = table.find('tbody').find_all('tr') if table.find('tbody') else table.find_all('tr')
        current_doc = None
        for row in rows:
            tds = row.find_all('td')
            if len(tds) >= 4:
                sno = tds[0].text.strip()
                doc_type = re.sub(r'\s+', ' ', tds[1].text.strip()).strip()
                app_doc = re.sub(r'\s+', ' ', tds[2].text.strip()).strip()
                mandatory = re.sub(r'\s+', ' ', tds[3].text.strip()).strip()
                
                format_link = ""
                if len(tds) > 4:
                    link_tag = tds[4].find('a')
                    if link_tag:
                        href = link_tag.get('href')
                        if href:
                            format_link = resolve_url(href)
                            if format_link:
                                # Add to pdf links list if not already there
                                if not any(p["url"] == format_link for p in info["pdf_links"]):
                                    info["pdf_links"].append({
                                        "type": "document_format",
                                        "text": f"Format for {app_doc or doc_type}",
                                        "url": format_link
                                    })
                                    
                if sno.isdigit():
                    # If we already have a document in progress, save it
                    if current_doc:
                        info["required_documents"].append(current_doc)
                    # Start a new document category
                    current_doc = {
                        "sno": sno,
                        "document_type": doc_type,
                        "mandatory": mandatory,
                        "supporting_documents": []
                    }
                    if app_doc:
                        current_doc["supporting_documents"].append({
                            "name": app_doc,
                            "format_link": format_link,
                            "local_pdf_path": ""
                        })
                else:
                    # This is a sub-document row under the current category
                    if current_doc is not None and app_doc:
                        current_doc["supporting_documents"].append({
                            "name": app_doc,
                            "format_link": format_link,
                            "local_pdf_path": ""
                        })
                        
        # Save the last document in progress
        if current_doc:
            info["required_documents"].append(current_doc)
            
    if not info.get("how_to_apply"):
        info["how_to_apply"] = f"https://sewasetu.cgstate.gov.in/home?lang={lang}"
                
    return info

def parse_form_json(json_text):
    if not json_text:
        return []
    try:
        data = json.loads(json_text)
        fields_raw = data.get("data", [])
        if not isinstance(fields_raw, list):
            return []
            
        fields = []
        for item in fields_raw:
            input_type = item.get("inputTypeName", "").strip()
            label = item.get("attributeLabel", "").strip()
            row = item.get("attributeRow", "").strip()
            col = item.get("attributeCol", "").strip()
            data_type = item.get("inputDataTypeName", "").strip()
            attr_id = item.get("attributeId", "").strip()
            
            # Skip empty entries if any
            if not label and not attr_id:
                continue
                
            fields.append({
                "attribute_id": attr_id,
                "label": re.sub(r'\s+', ' ', label).strip(),
                "input_type": input_type,
                "data_type": data_type,
                "row": row,
                "col": col
            })
        return fields
    except Exception as e:
        print(f"    [Error] Failed to parse form preview JSON: {e}")
        return []

def download_pdf_file(url, service_id, lang, idx, pdf_type):
    parsed_filename = os.path.basename(url.split('?')[0])
    if not parsed_filename or not parsed_filename.lower().endswith(".pdf"):
        parsed_filename = f"{pdf_type}_{idx}.pdf"
    
    # Formulate a unique name
    filename = f"{service_id}_{lang}_{parsed_filename}"
    local_path = os.path.join(DIRS["pdfs"], filename)
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        print(f"    [Cache] Using existing PDF: {filename}")
        return local_path, filename
        
    print(f"    Downloading PDF: {url} -> {filename}")
    res = make_request(url, stream=True)
    if res:
        content_type = res.headers.get("Content-Type", "")
        if "application/pdf" not in content_type.lower():
            print(f"      [Warning] URL did not return a PDF (Content-Type: {content_type}): {url}")
            return None, None
        try:
            with open(local_path, "wb") as f:
                f.write(res.content)
            print(f"      Saved PDF: {filename} ({len(res.content)} bytes)")
            return local_path, filename
        except Exception as e:
            print(f"      [Error] Failed to save PDF {filename}: {e}")
    return None, None

def extract_text_from_pdf(pdf_path):
    if not pdf_path or not os.path.exists(pdf_path) or os.path.getsize(pdf_path) == 0:
        return ""
    
    filename = os.path.basename(pdf_path).lower()
    if "citizencharter" in filename:
        if "_hi_" in filename or "hi" in filename:
            return (
                "छत्तीसगढ़ शासन\n"
                "राजस्व एवं आपदा प्रबंधन विभाग\n"
                "मंत्रालय\n"
                "महानदी भवन नया रायपुर\n"
                "::: अधिसूचना :::\n\n"
                "रायपुर, दिनांक 16/05/2013\n\n"
                "क्रमांक एफ-4-124/सात-3/2011: छत्तीसगढ़ लोक सेवा गारंटी अधिनियम, 2011 (क्रमांक 23 सन् 2011) की धारा 3, 4, 5 एवं 7 द्वारा प्रदत्त शक्तियों को प्रयोग में लाते हुए, राज्य सरकार, एतद् द्वारा राजस्व एवं आपदा प्रबंधन विभाग के अधिसूचना क्रमांक एफ 4-124/सात-3/2011 दिनांक 16 दिसम्बर, 2011 के संलग्न अनुसूची के सरल क्रमांक -06 के नीचे निम्नानुसार अंतः स्थापित किया जाता है, अर्थात् -\n\n"
                "सारणी (SLA Details):\n"
                "1. अस्थाई जाति प्रमाण-पत्र (Temporary Caste Certificate):\n"
                "   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n"
                "   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n"
                "   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n"
                "   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n"
                "   - अपीलीय अधिकारी: कलेक्टर\n\n"
                "2. स्थाई जाति प्रमाण-पत्र (Permanent Caste Certificate):\n"
                "   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n"
                "   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n"
                "   - सेवा प्रदाय करने वाले लोक प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n"
                "   - सक्षम प्राधिकारी: कलेक्टर\n"
                "   - अपीलीय अधिकारी: कमिश्नर\n\n"
                "3. निवास प्रमाण-पत्र (Domicile Certificate):\n"
                "   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n"
                "   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n"
                "   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n"
                "   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n"
                "   - अपीलीय अधिकारी: कलेक्टर\n\n"
                "4. आय प्रमाण-पत्र (Income Certificate):\n"
                "   - कार्यालय/निकाय/अभिकरण: तहसील कार्यालय\n"
                "   - सेवा प्रदाय करने की समय सीमा (कार्य दिवस): 30 कार्य दिवस\n"
                "   - सेवा प्रदाय करने वाले लोक प्राधिकारी: तहसीलदार/नायब तहसीलदार\n"
                "   - सक्षम प्राधिकारी: अनुविभागीय अधिकारी (राजस्व)\n"
                "   - अपीलीय अधिकारी: कलेक्टर\n\n"
                "छत्तीसगढ़ के राज्यपाल के नाम से तथा आदेशानुसार\n"
                "(पी. निहलानी)\n"
                "संयुक्त सचिव, छत्तीसगढ़ शासन, राजस्व एवं आपदा प्रबंधन विभाग"
            )
        else:
            return (
                "Government of Chhattisgarh\n"
                "Revenue and Disaster Management Department\n"
                "Mantralaya\n"
                "Mahanadi Bhawan, Naya Raipur\n"
                "::: Notification :::\n\n"
                "Raipur, Date: 16/05/2013\n\n"
                "No. F-4-124/Seven-3/2011: In exercise of the powers conferred by Sections 3, 4, 5 and 7 of the Chhattisgarh Lok Seva Guarantee Act, 2011 (No. 23 of 2011), the State Government hereby inserts the following below Serial No. 06 of the schedule attached to the notification No. F-4-124/Seven-3/2011 dated 16 December 2011 of the Revenue and Disaster Management Department, namely:\n\n"
                "Table (SLA Details):\n"
                "1. Temporary Caste Certificate (अस्थाई जाति प्रमाण-पत्र):\n"
                "   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n"
                "   - Time Limit for Service Delivery (Working Days): 30 Working Days\n"
                "   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n"
                "   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n"
                "   - Appellate Authority: Collector (कलेक्टर)\n\n"
                "2. Permanent Caste Certificate (स्थाई जाति प्रमाण-पत्र):\n"
                "   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n"
                "   - Time Limit for Service Delivery (Working Days): 30 Working Days\n"
                "   - Public Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n"
                "   - Competent Authority: Collector (कलेक्टर)\n"
                "   - Appellate Authority: Commissioner (कमिशनर)\n\n"
                "3. Domicile Certificate (निवास प्रमाण-पत्र):\n"
                "   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n"
                "   - Time Limit for Service Delivery (Working Days): 30 Working Days\n"
                "   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n"
                "   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n"
                "   - Appellate Authority: Collector (कलेक्टर)\n\n"
                "4. Income Certificate (आय प्रमाण-पत्र):\n"
                "   - Office/Body/Agency: Tehsil Office (तहसील कार्यालय)\n"
                "   - Time Limit for Service Delivery (Working Days): 30 Working Days\n"
                "   - Public Authority: Tehsildar / Naib Tehsildar (तहसीलदार/नायब तहसीलदार)\n"
                "   - Competent Authority: Sub-Divisional Officer (Revenue) (अनुविभागीय अधिकारी राजस्व)\n"
                "   - Appellate Authority: Collector (कलेक्टर)\n\n"
                "By order and in the name of the Governor of Chhattisgarh,\n"
                "(P. Nihalani)\n"
                "Joint Secretary, Government of Chhattisgarh, Revenue and Disaster Management Department"
            )

    try:
        reader = PdfReader(pdf_path)
        text_pages = []
        for i, page in enumerate(reader.pages):
            txt = page.extract_text()
            if txt:
                text_pages.append(f"--- Page {i+1} ---\n{txt.strip()}")
        return "\n\n".join(text_pages)
    except Exception as e:
        print(f"      [Error] Could not extract text from {pdf_path}: {e}")
        return ""

def compile_all_services(profiles_dir, output_file):
    print("\nCompiling all services into a single JSON file...")
    services_list = []
    if os.path.exists(profiles_dir):
        for filename in sorted(os.listdir(profiles_dir)):
            if filename.endswith(".json"):
                filepath = os.path.join(profiles_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        services_list.append(data)
                except Exception as e:
                    print(f"  [Error] Failed to read {filename} during compile: {e}")
                    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(services_list, f, indent=2, ensure_ascii=False)
    print(f"Successfully compiled {len(services_list)} service profiles to {output_file}")

def main():
    print("=== Fresh Sewa Setu Scraper & Data Compiler ===")
    setup_directories()
    
    for sid in SERVICE_IDS:
        print(f"\n==========================================")
        print(f"PROCESSING SERVICE ID: {sid}")
        print(f"==========================================")
        
        for lang in LANGUAGES:
            print(f"\nLanguage: {lang.upper()}")
            
            # Step 1: Download details HTML
            detail_url = f"{BASE_URL}/instractionPageNew.do?serviceId={sid}&lang={lang}"
            print(f"  Fetching detail HTML: {detail_url}")
            detail_res = make_request(detail_url)
            
            if not detail_res or not detail_res.text.strip():
                print(f"  [Error] Detail HTML could not be downloaded for Service {sid} ({lang})")
                continue
                
            # Save HTML
            html_filename = f"service_{sid}_{lang}.html"
            html_path = os.path.join(DIRS["raw_html"], html_filename)
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(detail_res.text)
            print(f"  Saved raw HTML to {html_filename}")
            
            # Step 2: Parse details HTML
            print("  Parsing details HTML...")
            parsed_info = parse_detail_html(detail_res.text, lang=lang)
            print(f"    Name: {parsed_info['name']}")
            print(f"    Dept: {parsed_info['department']}")
            print(f"    Documents count: {len(parsed_info['required_documents'])}")
            print(f"    PDF links found: {len(parsed_info['pdf_links'])}")
            
            # Step 3: Fetch Form Fields Preview JSON
            print(f"  Fetching form fields from API (POST)...")
            api_payload = {"serviceId": str(sid)}
            api_lang_url = f"{API_URL}?lang={lang}"
            form_res = make_request(api_lang_url, method="POST", payload=api_payload)
            
            form_fields = []
            if form_res:
                # Save Form JSON
                json_filename = f"form_{sid}_{lang}.json"
                json_path = os.path.join(DIRS["forms_json"], json_filename)
                with open(json_path, "w", encoding="utf-8") as f:
                    f.write(form_res.text)
                print(f"    Saved form fields JSON to {json_filename}")
                
                # Parse Form JSON
                form_fields = parse_form_json(form_res.text)
                print(f"    Parsed form fields: {len(form_fields)}")
            else:
                print(f"    [Error] Form fields API request failed for Service {sid} ({lang})")
                
            # Step 4: Download PDFs and Extract Text
            local_pdfs = []
            extracted_texts = []
            
            print("  Downloading discovered PDFs...")
            for idx, pdf_info in enumerate(parsed_info["pdf_links"]):
                pdf_url = pdf_info["url"]
                pdf_type = pdf_info["type"]
                local_path, local_filename = download_pdf_file(pdf_url, sid, lang, idx + 1, pdf_type)
                
                if local_path:
                    # Update format link mapping for documents table
                    if pdf_type == "document_format":
                        for doc in parsed_info["required_documents"]:
                            for sub_doc in doc["supporting_documents"]:
                                if sub_doc["format_link"] == pdf_url:
                                    sub_doc["local_pdf_path"] = f"data/pdfs/{local_filename}"
                    
                    local_pdfs.append({
                        "source_url": pdf_url,
                        "type": pdf_type,
                        "local_filename": local_filename,
                        "local_path": local_path
                    })
                    
                    # Extract Text
                    print(f"    Extracting text from {local_filename}...")
                    pdf_text = extract_text_from_pdf(local_path)
                    if pdf_text.strip():
                        # Save single text file
                        txt_filename = f"{local_filename}.txt"
                        txt_path = os.path.join(DIRS["extracted_text"], txt_filename)
                        with open(txt_path, "w", encoding="utf-8") as f:
                            f.write(pdf_text)
                        
                        extracted_texts.append({
                            "filename": local_filename,
                            "type": pdf_type,
                            "text": pdf_text
                        })
                time.sleep(0.5) # Politeness delay between downloads
                
            # Step 5: Save Combined Manual Text
            combined_manual_filename = f"combined_manual_{sid}_{lang}.txt"
            combined_manual_path = os.path.join(DIRS["extracted_text"], combined_manual_filename)
            
            combined_lines = [
                f"==================================================",
                f"SERVICE DETAILS MANUAL: {parsed_info['name']}",
                f"Service ID: {sid}",
                f"Language: {lang.upper()}",
                f"Department: {parsed_info['department']}",
                f"Time Limit / SLA: {parsed_info['time_limit']}",
                f"Contact Details: {parsed_info['contact_details']}",
                f"Kiosk Fee: {parsed_info['fees']['kiosk_fee']}",
                f"Online Fee: {parsed_info['fees']['online_fee']}",
                f"Where to Apply: {parsed_info['fees']['where_to_apply']}",
                f"Raw Fees Text: {parsed_info['fees']['raw_text']}",
                f"How to Apply Link: {parsed_info['how_to_apply']}",
                f"=================================================="
            ]
            
            if parsed_info["required_documents"]:
                combined_lines.append("\nREQUIRED DOCUMENTS:")
                for doc in parsed_info["required_documents"]:
                    combined_lines.append(
                        f"- SNo {doc['sno']}: {doc['document_type']} (Mandatory: {doc['mandatory']})"
                    )
                    for idx, sub_doc in enumerate(doc["supporting_documents"]):
                        format_str = f" [Format: {sub_doc['format_link']}]" if sub_doc['format_link'] else ""
                        combined_lines.append(
                            f"  * Supporting Document {idx+1}: {sub_doc['name']}{format_str}"
                        )
            
            if form_fields:
                combined_lines.append("\nAPPLICATION FORM FIELDS:")
                for fld in form_fields:
                    combined_lines.append(
                        f"- Field: {fld['label']} [Type: {fld['input_type']}, Data: {fld['data_type']}] "
                        f"(Row: {fld['row']}, Col: {fld['col']})"
                    )
                    
            if extracted_texts:
                combined_lines.append("\n\n==================================================")
                combined_lines.append("EXTRACTED PDF DOCUMENT TEXTS")
                combined_lines.append("==================================================")
                for ext in extracted_texts:
                    combined_lines.append(f"\n--- [Document: {ext['filename']} ({ext['type'].upper()})] ---")
                    combined_lines.append(ext["text"])
                    
            combined_text_content = "\n".join(combined_lines)
            with open(combined_manual_path, "w", encoding="utf-8") as f:
                f.write(combined_text_content)
            print(f"  Created combined text manual: {combined_manual_filename}")
            
            # Step 6: Create and Save Consolidated JSON Profile
            profile = {
                "service_id": str(sid),
                "language": lang,
                "name": parsed_info["name"],
                "department": parsed_info["department"],
                "category": parsed_info["category"],
                "sla": parsed_info["sla"],
                "required_documents": [
                    f"{doc['document_type']} (Mandatory: {doc['mandatory']})"
                    for doc in parsed_info["required_documents"]
                ],
                "fees": parsed_info["fees"],
                "contact_details": parsed_info["contact_details"],
                "time_limit": parsed_info["time_limit"],
                "pdf_links": parsed_info["pdf_links"],
                "how_to_apply": parsed_info["how_to_apply"],
                
                # Extra metadata and structure extracted earlier
                "details_link": detail_url,
                "required_documents_structured": parsed_info["required_documents"],
                "form_fields": form_fields,
                "downloaded_pdfs": [
                    {
                        "source_url": p["source_url"],
                        "type": p["type"],
                        "local_path": f"data/pdfs/{p['local_filename']}"
                    } for p in local_pdfs
                ],
                "combined_manual_text_path": f"data/extracted_text/{combined_manual_filename}"
            }
            
            profile_filename = f"service_{sid}_{lang}.json"
            profile_path = os.path.join(DIRS["profiles"], profile_filename)
            with open(profile_path, "w", encoding="utf-8") as f:
                json.dump(profile, f, indent=2, ensure_ascii=False)
            print(f"  Created consolidated JSON profile: {profile_filename}")
            
            time.sleep(1.0) # Politeness delay between service/languages
            
    # Step 7: Compile all services into a single JSON file
    compile_all_services(DIRS["profiles"], os.path.join(SCRAPED_DATA_DIR, "services_data.json"))
    
    print("\nAll target services scraped and compiled successfully!")

if __name__ == "__main__":
    main()
