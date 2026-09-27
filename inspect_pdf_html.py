import re

with open('pdf_guide_lina_rela.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("pdf_guide_lina_rela.html Length:", len(html))

# Find title
title_match = re.search(r'<title>(.*?)</title>', html)
print("Title:", title_match.group(1) if title_match else "None")

# Find IDs
ids = re.findall(r'id=["\']([^"\']+)["\']', html)
print("IDs in pdf_guide_lina_rela.html:", len(ids))
print("First 20 IDs:", ids[:30])

# Find anchor hrefs
anchors = re.findall(r'href=["\'](#[^"\']+)["\']', html)
print("Anchor hrefs count:", len(anchors))
print("Unique anchor hrefs:", sorted(list(set(anchors))))

# Check for panel click handlers or onclick
onclicks = re.findall(r'onclick=["\']([^"\']+)["\']', html)
print("Onclicks count:", len(onclicks))
print("Sample onclicks:", onclicks[:20])

