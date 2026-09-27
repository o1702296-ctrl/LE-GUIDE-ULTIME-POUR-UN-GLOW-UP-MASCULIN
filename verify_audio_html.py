html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("1. audio-section present:", 'audio-section' in html)
print("2. L'AUDIO COMPLET DU PROGRAMME present:", "L'AUDIO COMPLET DU PROGRAMME" in html)
print("3. Waveform animation present:", 'audio-waveform' in html)

pos = html.find('audio-section')
if pos != -1:
    print("\n=== HTML SNIPPET ===")
    print(html[pos:pos+900].encode('ascii', 'ignore').decode())
