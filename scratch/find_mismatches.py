import sys

# Force stdout to use utf-8 to avoid encoding crashes on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"c:\Users\hp\Desktop\sewa setu copies\SewaSetuRag - Copy (2)\tests\confused_queries_results_hindi.md", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find all lines with MISMATCH
mismatch_lines = []
for line in content.split("\n"):
    if "MISMATCH" in line:
        mismatch_lines.append(line)

print("\n--- FOUND MISMATCHES ---")
for ml in mismatch_lines:
    # Print safe ascii representations if console is not utf-8, but we forced it so it should be fine
    try:
        print(ml)
    except Exception:
        # Fallback to ascii representation
        print(ml.encode('ascii', errors='replace').decode('ascii'))
print("------------------------\n")
