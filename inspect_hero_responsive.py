script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

mq_matches = [m.start() for m in re.finditer(r'@media', content)]
print("Total @media matches:", len(mq_matches))
for i, pos in enumerate(mq_matches):
    print(f"\n--- @MEDIA MATCH {i+1} ---")
    print(content[pos:pos+800].encode('ascii', 'ignore').decode())
