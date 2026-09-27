# -*- coding: utf-8 -*-
import os

py_file = r'C:\Users\HP TTS\.gemini\antigravity\scratch\generate_full_guide_html.py'

with open(py_file, 'r', encoding='utf-8') as f:
    code = f.read()

# Remove the print button markup
btn_markup = """            <button onclick="window.print()" class="btn-pdf-print">
                <i class="fa-solid fa-print"></i> Imprimer / PDF
            </button>"""

code = code.replace(btn_markup, "")

# Also hide .btn-pdf-print in CSS just in case
code = code.replace(".btn-pdf-print {", ".btn-pdf-print { display: none !important; ")

with open(py_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("Removed Imprimer / PDF button from generate_full_guide_html.py")
