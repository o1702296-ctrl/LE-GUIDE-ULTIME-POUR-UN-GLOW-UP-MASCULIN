import os
import re

script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 3D Mockups
content = content.replace('SAUVER TON COUPLE — DORA ÉLYSIANE', 'SAUVER TON COUPLE — GUIDE OFFICIEL')
content = content.replace('<div class="lap-screen-sub">Dora Élysiane</div>', '<div class="lap-screen-sub">Guide Ultime</div>')
content = content.replace('<div class="box3d-spine-left"><span>DORA ÉLYSIANE</span></div>', '<div class="box3d-spine-left"><span>HOMME MODERNE</span></div>')
content = content.replace('<p>DORA ÉLYSIANE</p>', '<p>HOMME MODERNE</p>')

# 2. Title & Meta
content = content.replace(' - Dora Élysiane</title>', '</title>')
content = content.replace(' Par Dora Élysiane.">', '">')

# 3. Footer copyright
content = content.replace('Copyright © 2026 - Dora Élysiane - Tous droits réservés', 'Copyright © 2026 - Tous droits réservés')
content = content.replace('/* Author Section (Qui est Dora Élysiane - Style Kaaramo) */', '/* Author Section */')

# 4. Remove Section 8 (QUI EST DORA ÉLYSIANE)
pattern = r'<!-- SECTION 8 : QUI EST DORA ÉLYSIANE.*?<\/section>'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# 5. Replace Checkout URL
content = content.replace('https://doraelysiane.com/prd_8yedvcr4/checkout', 'https://syalpfmx.mychariow.shop/prd_9n9ofrxp/checkout')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated build script.")
