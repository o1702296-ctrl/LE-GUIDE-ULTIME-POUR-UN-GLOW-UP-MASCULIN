html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("Guaranteed Sticky Header present:", 'Guaranteed Sticky Header' in html)

pos = html.find('Guaranteed Sticky Header')
if pos != -1:
    print("\n=== CSS RULES IN INDEX.HTML ===")
    print(html[pos:pos+1000].encode('ascii', 'ignore').decode())
