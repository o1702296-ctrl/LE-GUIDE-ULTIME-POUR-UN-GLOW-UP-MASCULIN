# -*- coding: utf-8 -*-
import os

filepath = r'C:\Users\HP TTS\.gemini\antigravity\scratch\generate_full_guide_html.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Clean fix for single quote inside alert
content = content.replace("alert('La synthèse vocale n'est pas supportée sur ce navigateur.');", 'alert("La synthèse vocale n\'est pas supportée sur ce navigateur.");')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Permanently fixed alert quote in generate_full_guide_html.py!")
