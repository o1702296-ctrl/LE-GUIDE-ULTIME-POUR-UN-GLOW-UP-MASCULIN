import re

with open('sauver-ton-couple-landing/guide.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("HTML Length:", len(html))

# Find title
title_match = re.search(r'<title>(.*?)</title>', html)
print("Title:", title_match.group(1) if title_match else "None")

# Find IDs
ids = re.findall(r'id=["\']([^"\']+)["\']', html)
print("IDs in document:", len(ids))
print("First 20 IDs:", ids[:20])

# Find anchor hrefs
anchors = re.findall(r'href=["\'](#[^"\']+)["\']', html)
print("Anchor hrefs count:", len(anchors))
print("Unique anchor hrefs:", sorted(list(set(anchors))))

# Check for panel click handlers or onclick
onclicks = re.findall(r'onclick=["\']([^"\']+)["\']', html)
print("Onclicks count:", len(onclicks))
print("Sample onclicks:", onclicks[:10])

# Check for #conclusion or chapter IDs
chapter_ids = [i for i in ids if 'chap' in i.lower() or 'intro' in i.lower() or 'concl' in i.lower() or 'toc' in i.lower()]
print("Chapter related IDs:", chapter_ids)

