script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

print("=== TOP BARS / ANNOUNCEMENT / HEADER HTML ===")
top_idx = content.find('<body')
if top_idx != -1:
    print(content[top_idx:top_idx+1500].encode('ascii', 'ignore').decode())

print("\n=== STICKY / FIXED CSS RULES ===")
for line in content.splitlines():
    if 'sticky' in line.lower() or 'fixed' in line.lower() or 'announcement-bar' in line.lower() or 'custom-lang' in line.lower():
        print(line[:150].encode('ascii', 'ignore').decode())
