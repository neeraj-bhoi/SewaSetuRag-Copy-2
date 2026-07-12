import sys
from fastapi.testclient import TestClient

# Force stdout to use utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Import app to test
sys.path.append(r"c:\Users\hp\Desktop\sewa setu copies\SewaSetuRag - Copy (2)")
from backend.main import app

client = TestClient(app)

# Simulate user clicking "Directly Answer My Question" on the options click
payload = {
    "messages": [
        {
            "role": "user",
            "content": "एसटी प्रमाण पत्र के दस्तावेजों में निवास प्रमाण पत्र लगता है क्या?"
        },
        {
            "role": "assistant",
            "content": "क्या आप अनुसूचित जाति / अनुसूचित जनजाति प्रमाण पत्र दस्तावेज़ चेकलिस्ट का उपयोग करके अपनी पात्रता जांचना चाहते हैं, या विस्तृत पात्रता मानदंडों की जानकारी देखना चाहते हैं, या सीधे अपने प्रश्न का उत्तर चाहते हैं?"
        },
        {
            "role": "user",
            "content": "सीधे अपने सवाल का जवाब पाएं"
        }
    ],
    "selected_sno": "2",  # Service SNo for SC/ST Certificate
    "language": "hi",
    "detailed": True,
    "interactive": True,
    "is_option_click": True
}

print("Sending chat request for ST Domicile validation...")
response = client.post("/api/chat", json=payload)
if response.status_code == 200:
    res_data = response.json()
    print("\nResponse:")
    print(res_data.get("response"))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
