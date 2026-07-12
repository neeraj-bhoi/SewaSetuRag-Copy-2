import sys

# Force stdout to use utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"c:\Users\hp\Desktop\sewa setu copies\SewaSetuRag - Copy (2)\data\extracted_text\combined_manual_4_hi.txt", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")
for idx in range(10, 50):
    print(f"{idx+1}: {lines[idx]}")
