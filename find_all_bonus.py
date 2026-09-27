script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

matches = [m.start() for m in re.finditer(r'BONUS #1', content)]
print("Total BONUS #1 matches:", len(matches))
for i, pos in enumerate(matches):
    print(f"\n--- MATCH {i+1} ---")
    print(content[pos-100:pos+800].encode('ascii', 'ignore').decode())
