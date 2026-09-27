html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("1. Complete Language Synchronization Engine:", 'Complete Language Synchronization' in html)
print("2. syncLanguageDropdownUI in DOMContentLoaded:", 'DOMContentLoaded' in html and 'syncLanguageDropdownUI()' in html)
print("3. syncLanguageDropdownUI in load event:", 'window.addEventListener(\'load\'' in html)

pos = html.find('Complete Language Synchronization')
if pos != -1:
    print("\n=== FULL JS SCRIPT IN INDEX.HTML ===")
    print(html[pos:pos+2500].encode('ascii', 'ignore').decode())
