# -*- coding: utf-8 -*-
import os

files_to_fix = [
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\generate_full_guide_html.py',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\guide.html',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\guide.html',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\pdf_guide_lina_rela.html',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\add_voice_to_all.py',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\update_voice_engine_robust.py'
]

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix unescaped single quote in alert string
        content = content.replace("alert('La synthèse vocale n'est pas supportée sur ce navigateur.');", 'alert("La synthèse vocale n\'est pas supportée sur ce navigateur.");')
        content = content.replace("alert('La synthèse vocale n\'est pas supportée sur ce navigateur.');", 'alert("La synthèse vocale n\'est pas supportée sur ce navigateur.");')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed quotes in:", filepath)

print("Direct fix completed!")
