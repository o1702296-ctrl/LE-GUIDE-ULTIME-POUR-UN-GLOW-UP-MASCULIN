script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

pos = content.find('.announcement-bar {')
if pos == -1:
    pos = content.find('.announcement-bar {{')

if pos != -1:
    print("=== ANNOUNCEMENT BAR DESKTOP CSS ===")
    print(content[pos:pos+1000].encode('ascii', 'ignore').decode())

pos_mobile = content.find('.announcement-bar')
while pos_mobile != -1:
    print("\n=== MATCH ===")
    print(content[pos_mobile:pos_mobile+500].encode('ascii', 'ignore').decode())
    pos_mobile = content.find('.announcement-bar', pos_mobile+1)
