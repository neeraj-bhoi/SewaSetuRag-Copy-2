import os
import sys
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

client = TestClient(app)

def test_late_fee_with_history():
    print("=== Testing Marriage Registration Late Fee with History Context ===")
    
    # 1. Ask about documents
    payload1 = {
        "messages": [
            {"role": "user", "content": "Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?"}
        ],
        "selected_sno": "1",
        "language": "en",
        "detailed": True,
        "interactive": True,
        "is_option_click": False
    }
    
    print("\nSending Turn 1: Document Query...")
    res1 = client.post("/api/chat", json=payload1)
    if res1.status_code != 200:
        print(f"Failed at Turn 1: {res1.status_code}")
        return
    data1 = res1.json()
    print(f"Turn 1 Response Type: {data1.get('mode')}")
    
    # 2. Click "Directly Answer My Question"
    payload2 = {
        "messages": [
            {"role": "user", "content": "Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?"},
            {"role": "assistant", "content": "Kya aap Marriage Registration & Certificate ke document checklist se apni eligibility check karna chahte hain..."},
            {"role": "user", "content": "Directly Answer My Question"}
        ],
        "selected_sno": "1",
        "language": "en",
        "detailed": True,
        "interactive": True,
        "is_option_click": True
    }
    
    print("\nSending Turn 2: Option Click...")
    res2 = client.post("/api/chat", json=payload2)
    if res2.status_code != 200:
        print(f"Failed at Turn 2: {res2.status_code}")
        return
    data2 = res2.json()
    response2_text = data2.get("response", "")
    print(f"Turn 2 Answer Length: {len(response2_text)}")
    print(f"Turn 2 Response Snippet: {response2_text[:100]}...")
    
    # 3. Ask about late fee
    payload3 = {
        "messages": [
            {"role": "user", "content": "Raipur Municipal Corporation office me offline marriage registration ke liye kya document le jana hoga?"},
            {"role": "assistant", "content": "Kya aap Marriage Registration & Certificate ke document checklist se apni eligibility check karna chahte hain..."},
            {"role": "user", "content": "Directly Answer My Question"},
            {"role": "assistant", "content": response2_text},
            {"role": "user", "content": "marriage registration late fee?"}
        ],
        "selected_sno": "1",
        "language": "en",
        "detailed": True,
        "interactive": True,
        "is_option_click": False
    }
    
    print("\nSending Turn 3: Late Fee Query with History...")
    res3 = client.post("/api/chat", json=payload3)
    if res3.status_code != 200:
        print(f"Failed at Turn 3: {res3.status_code}")
        return
    data3 = res3.json()
    response3_text = data3.get("response", "")
    print(f"\nFinal Chatbot Response:\n{response3_text}")
    print("\nLLM Trace Log:")
    for idx, call in enumerate(data3.get("llm_calls_trace", [])):
        print(f"  {idx+1}. Function: {call['function']}")
        print(f"     Output: {call['output']}")

if __name__ == "__main__":
    test_late_fee_with_history()
