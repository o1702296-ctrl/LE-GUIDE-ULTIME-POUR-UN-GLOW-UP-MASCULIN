html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("1. google_translate_element:", 'google_translate_element' in html)
print("2. https://translate.google.com:", 'https://translate.google.com' in html)
print("3. syncLanguageDropdown:", 'syncLanguageDropdown' in html)
print("4. setTranslateCookie:", 'setTranslateCookie' in html)

gt_idx = html.find('Google Translate Script with Robust Synchronization')
if gt_idx != -1:
    print("\n=== GENERATED SCRIPT IN HTML ===")
    print(html[gt_idx:gt_idx+1500])
