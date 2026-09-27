import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update all checkout URLs
content = content.replace('https://doraelysiane.com/prd_j93t2b/checkout', 'https://syalpfmx.mychariow.shop/prd_9gal1zvj/checkout')

# 2. Update Desktop CSS for seamless full-page background image
desktop_bg_css = '''
        /* HIGH-PRECISION DESKTOP RESPONSIVE DESIGN SYSTEM WITH FULL-PAGE CONTINUOUS BACKGROUND */
        @media (min-width: 993px) {
            body {
                position: relative;
                background-color: var(--bg-void);
            }
            body::before {
                content: '';
                position: fixed;
                inset: 0;
                background-image: url('images/peaky_blinders_hero_man.png');
                background-size: cover;
                background-position: center 15%;
                background-repeat: no-repeat;
                filter: blur(1px) brightness(0.70) contrast(1.1);
                z-index: 0;
                pointer-events: none;
            }

            /* Remove per-section background breaks so body background covers ALL sections continuously */
            .bg-section-blur::before {
                display: none !important;
            }

            .bg-section-blur::after {
                background: linear-gradient(180deg, rgba(3, 2, 6, 0.72) 0%, rgba(7, 5, 13, 0.55) 50%, rgba(3, 2, 6, 0.80) 100%);
            }

            .container {
                max-width: 1160px;
                padding: 0 32px;
            }
'''

content = re.sub(r'/\* HIGH-PRECISION DESKTOP RESPONSIVE DESIGN SYSTEM \*/\s*@media \(min-width: 993px\) \{\s*\.container \{', desktop_bg_css + '\n            .container {', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated checkout URLs and set continuous full-page background image for desktop!")
