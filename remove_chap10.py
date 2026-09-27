script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# 1. Remove Chapitre 10 HTML block
chap10_pattern = r'\s*<!-- Chapitre 10 -->\s*<div class="chapter-card">.*?<\/div>\s*<\/div>'
content = re.sub(chap10_pattern, '', content, flags=re.DOTALL)

# Fallback string replace if regex missed formatting
chap10_exact = """                <!-- Chapitre 10 -->
                <div class="chapter-card">
                    <div class="chapter-number">10</div>
                    <div>
                        <h3 class="chapter-title">Chapitre 10 : Quand est-il Temps de Partir ?</h3>
                        <p class="chapter-description">La sagesse de savoir si le combat en vaut encore la peine - et comment le décider avec dignité, lucidité et sans colère.</p>
                    </div>
                </div>"""

content = content.replace(chap10_exact, '')

# 2. Revert chapter counts from 10 to 9 on landing page
content = content.replace('GUIDE PRINCIPAL (10 CHAPITRES)', 'GUIDE PRINCIPAL (9 CHAPITRES)')
content = content.replace('10 chapitres puissants', '9 chapitres puissants')
content = content.replace('10 Chapitres', '9 Chapitres')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Build script updated: Chapitre 10 removed!")
