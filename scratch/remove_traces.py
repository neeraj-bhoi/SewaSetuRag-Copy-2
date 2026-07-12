import re
import os

def clean_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
        
    print(f"Cleaning file: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    cleaned_lines = []
    skipping = False
    
    for idx, line in enumerate(lines):
        stripped = line.strip()
        # Detect start of LLM Call Trace
        if stripped.startswith("* **LLM Call Trace**:") or stripped.startswith("* **LLM Call Trace**"):
            skipping = True
            # Also strip any empty lines immediately preceding the trace if they exist
            while cleaned_lines and cleaned_lines[-1].strip() == "":
                cleaned_lines.pop()
            continue
            
        # Detect end of trace section (starts with next table row or summary metrics)
        if skipping:
            if stripped.startswith("|") and re.match(r"^\|\s*\d+\s*\|", stripped):
                skipping = False
            elif stripped.startswith("##"):
                skipping = False
                
        if not skipping:
            cleaned_lines.append(line)
            
    # Write back the cleaned lines
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)
    print(f"Successfully cleaned {file_path}. New line count: {len(cleaned_lines)}")

if __name__ == "__main__":
    paths = [
        r"c:\Users\hp\Desktop\sewa setu copies\SewaSetuRag - Copy (2)\tests\confused_queries_results_hindi.md",
        r"c:\Users\hp\.gemini\antigravity-ide\brain\55237c9e-8b00-4d88-8655-df822faac3f6\confused_queries_results_hindi.md"
    ]
    for p in paths:
        clean_file(p)
