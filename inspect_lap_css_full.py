script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

print("=== LAP CSS RULES ===")
pos = content.find('.grand-laptops-v-stage')
if pos != -1:
    print(content[pos:pos+1600].encode('ascii', 'ignore').decode())

print("\n=== MEDIA QUERIES FOR LAP ===")
pos_mq = content.find('@media (max-width: 768px)')
if pos_mq != -1:
    print(content[pos_mq:pos_mq+2000].encode('ascii', 'ignore').decode())
