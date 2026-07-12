import sys
import os
from fastapi.testclient import TestClient

# Adjust path to import backend
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

client = TestClient(app)

def test_out_of_scope():
    sys.stdout.reconfigure(encoding='utf-8')
    
    payload = {
        "query": "narendra modi ke pass domicile certificate hoga?",
        "language": "hinglish",
        "detailed": True
    }
    
    print("Sending chat request for Narendra Modi out of scope validation...")
    response = client.post("/api/chat", json=payload)
    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(response.json())

if __name__ == "__main__":
    test_out_of_scope()
