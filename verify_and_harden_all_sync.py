import os

output_dir = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing'
index_file = os.path.join(output_dir, 'index.html')
guide_file = os.path.join(output_dir, 'guide.html')

with open(index_file, 'r', encoding='utf-8') as f:
    index_html = f.read()

with open(guide_file, 'r', encoding='utf-8') as f:
    guide_html = f.read()

print("Index HTML size:", len(index_html))
print("Guide HTML size:", len(guide_html))

print("Index has syncLanguageDropdownUI:", 'syncLanguageDropdownUI' in index_html)
print("Guide has syncLanguageDropdownUI:", 'syncLanguageDropdownUI' in guide_html)
