with open(r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("google_translate_element in html:", 'google_translate_element' in html)
for line in html.splitlines():
    if 'google_translate_element' in line or 'goog-te' in line or 'changePageLanguage' in line:
        print(line[:150].encode('ascii', 'ignore').decode())
