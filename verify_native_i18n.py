html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("1. i18nMap present:", 'i18nMap' in html)
print("2. applyDOMTranslation present:", 'applyDOMTranslation' in html)
print("3. SPECIAL IMMEDIATE ACCESS OFFER present:", 'SPECIAL IMMEDIATE ACCESS OFFER' in html)

pos = html.find('i18nMap')
if pos != -1:
    print("\n=== SCRIPT SNIPPET ===")
    print(html[pos-100:pos+800].encode('ascii', 'ignore').decode())
