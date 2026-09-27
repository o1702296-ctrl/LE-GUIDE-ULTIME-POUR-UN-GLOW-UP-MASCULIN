import re

with open('sauver-ton-couple-landing/guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Verifying guide.html...")
print("Length:", len(html))

# Check required section IDs
required_ids = [
    'couverture', 'avant-propos', 'toc', 'dedicace', 'introduction',
    'chapitre-1', 'chapitre-2', 'chapitre-3', 'chapitre-4', 'chapitre-5',
    'chapitre-6', 'chapitre-7', 'chapitre-8', 'chapitre-9', 'chapitre-10',
    'conclusion', 'annexe'
]

missing_ids = []
for rid in required_ids:
    if f'id="{rid}"' not in html and f"id='{rid}'" not in html:
        missing_ids.append(rid)

if missing_ids:
    print("MISSING IDs:", missing_ids)
else:
    print("ALL required IDs are present in guide.html!")

# Check TOC links
toc_hrefs = re.findall(r'<a href="#([^"]+)" class="toc-item">', html)
print("Found TOC links count:", len(toc_hrefs))
print("TOC target IDs:", toc_hrefs)

# Check dropdown options
dropdown_vals = re.findall(r'<option value="#?([^"]+)">', html)
print("Found dropdown option values count:", len(dropdown_vals))

# Check JS redirection functions
has_scroll = 'function scrollToSection' in html
has_hash_load = "window.location.hash" in html
has_translate_sync = "function changePageLanguage" in html

print("JS scrollToSection:", "OK" if has_scroll else "MISSING")
print("JS hash load handler:", "OK" if has_hash_load else "MISSING")
print("JS translate sync:", "OK" if has_translate_sync else "MISSING")


