script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
inline_grids = re.findall(r'style="[^"]*grid-template-columns:[^"]*"', content)
print("INLINE GRIDS FOUND:", len(inline_grids))
for g in set(inline_grids):
    print(" -", g.encode('ascii', 'ignore').decode())
