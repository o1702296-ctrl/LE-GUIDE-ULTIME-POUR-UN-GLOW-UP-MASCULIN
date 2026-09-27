# -*- coding: utf-8 -*-
import os
import re
import subprocess

def fix_script_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace unescaped n'est inside single quotes
    content = content.replace("alert('La synthèse vocale n'est pas supportée sur ce navigateur.');", 'alert("La synthèse vocale n\'est pas supportée sur ce navigateur.");')
    content = content.replace("n'est pas supportée", "n\'est pas supportée")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed single quotes in:", filepath)

generators = [
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\generate_full_guide_html.py',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_bonus1_html.py',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_bonus2_html.py',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\update_voice_engine_robust.py'
]

for g in generators:
    if os.path.exists(g):
        fix_script_quotes(g)

print("All generator python files updated!")
