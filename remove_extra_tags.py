import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove bonus-3d-author divs
content = re.sub(r'\s*<div class="bonus-3d-author">.*?</div>', '', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script successfully!")
