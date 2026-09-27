script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

pos = content.find('BONUS #1 : 10 phrases pour')
if pos != -1:
    print(content[pos-600:pos+1500].encode('ascii', 'ignore').decode())
