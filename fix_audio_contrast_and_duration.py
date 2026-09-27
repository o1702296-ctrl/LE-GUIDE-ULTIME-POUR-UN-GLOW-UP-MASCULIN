script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

bad_css = """        .audio-section .section-title {
            color: #ffffff !important;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }"""

good_css = """        .audio-section .section-title {{
            color: #ffffff !important;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}"""

if bad_css in content:
    content = content.replace(bad_css, good_css)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed braces in audio CSS override.")
