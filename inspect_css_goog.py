with open(r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for line in html.splitlines():
    if '.goog' in line or 'translate' in line.lower():
        if len(line) < 200:
            print(line.encode('ascii', 'ignore').decode())
