import re

html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

dora_matches = re.findall(r'.{0,30}(?:dora|élysiane|elysiane).{0,30}', html, re.IGNORECASE)
print('Dora / Elysiane matches count in index.html:', len(dora_matches))
for m in dora_matches:
    print('  MATCH:', repr(m))

qui_est = 'QUI EST DORA' in html
print('Contains "QUI EST DORA":', qui_est)

checkout_links = re.findall(r'href=["\'](https?://[^\'"]+)["\']', html)
print('\nHref links in index.html:')
for link in set(checkout_links):
    print(' -', link)
