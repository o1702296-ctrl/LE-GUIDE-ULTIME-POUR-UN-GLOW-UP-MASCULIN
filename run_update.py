# -*- coding: utf-8 -*-
import os
import re

html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'
with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Replace Dora Elysiane with Lina Rela
c = c.replace('Dora Elysiane', 'Lina Rela')
c = c.replace('Dora', 'Lina Rela')
c = c.replace('Elysiane', 'Lina Rela')

# Author sections
c = c.replace('<div class="lap-sub"></div>', '<div class="lap-sub">Lina Rela</div>')
c = c.replace('<div class="lap-screen-sub"></div>', '<div class="lap-screen-sub">Lina Rela</div>')
c = c.replace('<h3>Qui est  ?</h3>', '<h3>Qui est Lina Rela ?</h3>')
c = c.replace('<span class="subtext"></span>', '<span class="subtext">Lina Rela</span>')

# Document title & meta description
c = re.sub(r'<title>.*?</title>', '<title>SAUVER TON COUPLE SANS PERDRE TA DIGNITÉ — Lina Rela</title>', c)
c = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Guide premium de couple pour l\'homme moderne par Lina Rela. 10 chapitres, plan 30 jours, exercices pratiques et outils de communication pour transformer votre foyer.">', c)

# Correct encoding artifacts if any
c = c.replace('RSOUDRE', 'RÉSOUDRE').replace('DPASSS', 'DÉPASSÉS').replace('GRVE', 'GRÈVE').replace('INTIMIT', 'INTIMITÉ').replace('respetar', 'respecter')

destinations = [
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\index.html',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\landing_page.html',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\guide.html',
    html_path,
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\guide.html'
]

for dst in destinations:
    with open(dst, 'w', encoding='utf-8') as out_f:
        out_f.write(c)
    print("Successfully written:", dst, "Size:", len(c))
