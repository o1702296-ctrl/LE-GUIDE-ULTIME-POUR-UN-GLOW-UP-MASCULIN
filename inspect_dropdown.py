with open(r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
selects = re.findall(r'<select.*?>.*?</select>', html, re.DOTALL)
print("SELECT ELEMENTS FOUND:", len(selects))
for s in selects:
    print(s[:300].encode('ascii', 'ignore').decode())

print("\n=== SEARCHING FOR LANG DROPDOWN CONTAINER ===")
for line in html.splitlines():
    if 'changePageLanguage' in line or 'traduc' in line.lower():
        print(line[:150].encode('ascii', 'ignore').decode())
