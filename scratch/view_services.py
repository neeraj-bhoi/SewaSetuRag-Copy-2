import json
import sys

# Force stdout to use utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"c:\Users\hp\Desktop\sewa setu copies\SewaSetuRag - Copy (2)\data\rag_kb_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

for s in manifest["services"]:
    print(f"SNo: {s['sno']}, Service ID: {s['service_id']}, Name: {s['name_en']}")
