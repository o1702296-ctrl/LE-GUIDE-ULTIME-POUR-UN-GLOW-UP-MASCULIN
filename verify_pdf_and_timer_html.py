html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

import re
pdf_matches = re.findall(r'.{0,30}pdf.{0,30}', html, re.IGNORECASE)
print("PDF matches count in index.html:", len(pdf_matches))
for m in pdf_matches:
    print("  PDF MATCH:", repr(m))

print("Countdown badge in html:", '23:59:59' in html)
print("twentyFourHours in html:", 'twentyFourHours' in html)

pos = html.find('twentyFourHours')
if pos != -1:
    print("\n=== TIMER JS IN HTML ===")
    print(html[pos-300:pos+300].encode('ascii', 'ignore').decode())
