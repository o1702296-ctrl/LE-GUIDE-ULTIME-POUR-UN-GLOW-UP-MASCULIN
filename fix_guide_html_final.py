# -*- coding: utf-8 -*-
import os

filepath = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\guide.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the single quote inside alert string
bad_str = "alert('La synthèse vocale n'est pas supportée sur ce navigateur.');"
good_str = 'alert("La synthèse vocale n\'est pas supportée sur ce navigateur.");'

content = content.replace(bad_str, good_str)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed guide.html directly!")
