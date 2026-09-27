script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

print("=== SEARCHING LAPTOPS HTML ===")
pos = content.find('grand-laptops-v-stage')
if pos != -1:
    print(content[pos-100:pos+1500].encode('ascii', 'ignore').decode())

print("\n=== SEARCHING LAPTOPS CSS ===")
for line in content.splitlines():
    if any(k in line for k in ['.grand-lap', '.lap-screen', '.lap-bezel', '.lap-keyboard', '.lap-screen-title', '.lap-screen-tag']):
        print(line.encode('ascii', 'ignore').decode())
