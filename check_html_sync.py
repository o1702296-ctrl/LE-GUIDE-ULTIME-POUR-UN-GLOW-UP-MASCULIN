with open(r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("=== LANGUAGE SELECTOR IN HTML ===")
select_match = re.search(r'<select id="custom-language-select".*?</select>', html, re.DOTALL)
if select_match:
    print(select_match.group(0)[:500].encode('ascii', 'ignore').decode())

print("\n=== SCRIPT BLOCK IN HTML ===")
script_pos = html.find('function changePageLanguage')
if script_pos != -1:
    print(html[script_pos-300:script_pos+1800].encode('ascii', 'ignore').decode())
