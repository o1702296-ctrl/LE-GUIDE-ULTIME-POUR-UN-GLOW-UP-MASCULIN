script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

print("=== SEARCHING BONUS SECTION HTML ===")
pos = content.find('BONUS #1')
if pos != -1:
    print(content[pos-400:pos+1500].encode('ascii', 'ignore').decode())

print("\n=== SEARCHING BONUS CSS CLASSES ===")
for line in content.splitlines():
    if any(k in line.lower() for k in ['bonus-grid', 'bonus-card', 'bonus-section', 'bonuses-grid', 'bonus_grid']):
        print(line[:150].encode('ascii', 'ignore').decode())
