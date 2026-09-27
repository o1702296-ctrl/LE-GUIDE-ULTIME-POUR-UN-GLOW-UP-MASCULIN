with open(r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py', 'r', encoding='utf-8') as f:
    content = f.read()

import re
select_block = re.search(r'<select id="custom-language-select".*?<\/select>', content, re.DOTALL)
if select_block:
    print(select_block.group(0).encode('ascii', 'ignore').decode())
