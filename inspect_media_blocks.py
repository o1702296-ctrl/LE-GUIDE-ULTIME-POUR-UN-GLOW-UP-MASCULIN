script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

pos = content.find('@media (max-width: 900px)')
if pos != -1:
    print(content[pos:pos+2500].encode('ascii', 'ignore').decode())
