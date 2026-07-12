import sys

# Force stdout to use utf-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"c:\Users\hp\Desktop\sewa setu copies\SewaSetuRag - Copy (2)\tests\confused_queries_results_hindi.md", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")

# Find line numbers of Query Details for 2, 15, 39
queries_to_find = [2, 15, 39]

for q_id in queries_to_find:
    query_header = f"### Query {q_id} Details"
    for idx, line in enumerate(lines):
        if query_header in line:
            print(f"Found {query_header} at line {idx+1}:")
            # print the next 25 lines
            for i in range(idx, min(idx + 25, len(lines))):
                try:
                    print(f"  {i+1}: {lines[i]}")
                except Exception:
                    print(f"  {i+1}: " + lines[i].encode('ascii', errors='replace').decode('ascii'))
            print("-" * 50)
