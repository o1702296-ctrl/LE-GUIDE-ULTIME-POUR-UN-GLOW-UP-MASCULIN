html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("Mobile Pixel-Perfect Responsiveness present:", 'Mobile Pixel-Perfect Responsiveness' in html)

pos = html.find('Mobile Pixel-Perfect Responsiveness')
if pos != -1:
    print("\n=== CSS RULES IN INDEX.HTML ===")
    print(html[pos:pos+1200].encode('ascii', 'ignore').decode())
