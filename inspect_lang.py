import re

html_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("=== SEARCHING LANGUAGE BAR HTML ===")
start = html.find('language-selector')
if start != -1:
    print(html[start-100:start+1500])

print("\n=== SEARCHING GOOGLE TRANSLATE SCRIPT ===")
gt_idx = html.find('googleTranslateElementInit')
if gt_idx != -1:
    print(html[gt_idx-200:gt_idx+1500])
