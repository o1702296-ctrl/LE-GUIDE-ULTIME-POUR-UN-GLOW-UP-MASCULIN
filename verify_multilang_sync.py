html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("1. Full Multi-Language Synchronization Engine:", 'Full Multi-Language Synchronization' in html)
print("2. user_selected_lang in html:", 'user_selected_lang' in html)
print("3. syncLanguageDropdown in html:", 'syncLanguageDropdown' in html)

pos = html.find('Full Multi-Language Synchronization')
if pos != -1:
    print("\n=== SCRIPT SNIPPET ===")
    print(html[pos:pos+900].encode('ascii', 'ignore').decode())
