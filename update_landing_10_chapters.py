script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update 9 Chapitres references to 10 Chapitres
content = content.replace('GUIDE PRINCIPAL (9 CHAPITRES)', 'GUIDE PRINCIPAL (10 CHAPITRES)')
content = content.replace('9 chapitres puissants', '10 chapitres puissants')
content = content.replace('9 Chapitres', '10 Chapitres')

# Add Chapter 10 to Section 3 in landing page if not present
chap10_html = """
                <!-- Chapitre 10 -->
                <div class="chapter-card">
                    <div class="chapter-number">10</div>
                    <div>
                        <h3 class="chapter-title">Chapitre 10 : Quand est-il Temps de Partir ?</h3>
                        <p class="chapter-description">La sagesse de savoir si le combat en vaut encore la peine - et comment le décider avec dignité, lucidité et sans colère.</p>
                    </div>
                </div>
"""

if 'Chapitre 10 : Quand est-il Temps de Partir ?' not in content:
    content = content.replace('<!-- SECTION 4 :', chap10_html + '\n                <!-- SECTION 4 :')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Landing page build script updated for 10 Chapters!")
