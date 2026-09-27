html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("1. bonus-cards-grid in html:", 'bonus-cards-grid' in html)
print("2. bonus-card in html:", 'bonus-card' in html)

pos = html.find('bonus-cards-grid')
if pos != -1:
    print("\n=== HTML SNIPPET ===")
    print(html[pos-100:pos+800].encode('ascii', 'ignore').decode())
