# -*- coding: utf-8 -*-
import os
import re

py_file = r'C:\Users\HP TTS\.gemini\antigravity\scratch\generate_full_guide_html.py'

with open(py_file, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Replace all occurrences of Dora Elysiane with Lina Rela
code = code.replace("Dora Elysiane", "Lina Rela")
code = code.replace("DORA ELYSIANE", "LINA RELA")
code = code.replace("dora_elysiane", "lina_rela")

# 2. Update CSS Color Palette to 100% Rich Violet / Purple
old_root = """        :root {
            --pdf-bg: #404448;
            --page-bg: #ffffff;
            --text-color: #2b2b2b;
            --text-heading: #5c183b;
            --accent-gold: #c68a27;
            --accent-gold-light: #fbbf24;
            --accent-pink: #d946ef;
            --accent-magenta: #701a40;
            --border-color: #f1d5e4;
            --box-gold-bg: #fffbeb;
            --box-sister-bg: #fdf2f8;
            --box-metaphor-bg: #f0f9ff;
            --font-main: 'Inter', sans-serif;
            --font-heading: 'Outfit', sans-serif;
        }"""

new_root = """        :root {
            --pdf-bg: #150529;
            --page-bg: #faf5ff;
            --text-color: #2b2b2b;
            --text-heading: #4c1d95;
            --accent-gold: #d97706;
            --accent-gold-light: #fbbf24;
            --accent-pink: #c084fc;
            --accent-magenta: #6b21a8;
            --border-color: #e9d5ff;
            --box-gold-bg: #fffbeb;
            --box-sister-bg: #fcf4ff;
            --box-metaphor-bg: #f3e8ff;
            --font-main: 'Inter', sans-serif;
            --font-heading: 'Outfit', sans-serif;
        }"""

code = code.replace(old_root, new_root)

# Replace any lingering old root definitions if present
code = re.sub(r'--pdf-bg:\s*#[a-fA-F0-9]+;', '--pdf-bg: #150529;', code)
code = re.sub(r'--page-bg:\s*#[a-fA-F0-9]+;', '--page-bg: #faf5ff;', code)
code = re.sub(r'--text-heading:\s*#[a-fA-F0-9]+;', '--text-heading: #4c1d95;', code)
code = re.sub(r'--accent-magenta:\s*#[a-fA-F0-9]+;', '--accent-magenta: #6b21a8;', code)
code = re.sub(r'--border-color:\s*#[a-fA-F0-9]+;', '--border-color: #e9d5ff;', code)

# Cover Page Violet Styling
code = code.replace("background: linear-gradient(135deg, #4a0d2d 0%, #2b061a 100%);", "background: linear-gradient(135deg, #3b0764 0%, #1e0538 60%, #120326 100%);")
code = code.replace("background: #1e1e22;", "background: #1a0636; border-bottom: 1.5px solid #a855f7;")

# Box Violet Headers & Backgrounds
code = code.replace("background: #9f1239;", "background: #7e22ce;")
code = code.replace("border: 1.5px solid #be123c;", "border: 1.5px solid #a855f7;")
code = code.replace("background: #0369a1;", "background: #581c87;")
code = code.replace("border: 1.5px solid #0284c7;", "border: 1.5px solid #7e22ce;")

with open(py_file, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate_full_guide_html.py with Lina Rela and Full Violet Theme!")
