# -*- coding: utf-8 -*-
import os

py_file = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_bonus1_html.py'

with open(py_file, 'r', encoding='utf-8') as f:
    code = f.read()

# Remove the Accueil button link
code = code.replace('<a href="index.html" class="pdf-nav-link"><i class="fa-solid fa-house"></i> Accueil</a>', '')

with open(py_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("Removed Accueil button from build_bonus1_html.py")
