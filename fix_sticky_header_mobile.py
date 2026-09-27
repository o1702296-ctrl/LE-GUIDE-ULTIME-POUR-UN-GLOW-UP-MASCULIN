script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace overflow-x: hidden on html, body with overflow-x: clip
content = content.replace(
    'html, body {{\n                overflow-x: hidden;\n            }}',
    'html, body {{\n                overflow-x: clip;\n            }}'
)
content = content.replace(
    'html, body {\n                overflow-x: hidden;\n            }',
    'html, body {\n                overflow-x: clip;\n            }'
)

# 2. Add Mobile Fixed Sticky Header CSS rules
sticky_mobile_css = """
        /* Guaranteed Sticky Header on Mobile */
        .announcement-bar {{
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            width: 100% !important;
            z-index: 99999 !important;
            box-shadow: 0 4px 20px rgba(13, 2, 20, 0.6) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
        }}

        @media (max-width: 768px) {{
            body {{
                padding-top: 54px !important;
            }}
            .announcement-bar {{
                padding: 6px 10px !important;
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                justify-content: space-between !important;
                align-items: center !important;
                gap: 6px !important;
            }}
            .announcement-bar > span:first-child {{
                display: none !important; /* Hide long text on mobile to keep timer & lang selector visible & sleek */
            }}
            .announcement-bar-mobile-label {{
                display: inline-block !important;
                font-size: 0.78rem !important;
                font-weight: 800 !important;
                color: #ffffff !important;
                white-space: nowrap !important;
            }}
            .announcement-bar .timer-badge {{
                font-size: 0.85rem !important;
                padding: 3px 8px !important;
                margin: 0 !important;
            }}
            .custom-lang-dropdown {{
                padding: 3px 8px !important;
                font-size: 0.75rem !important;
            }}
            #custom-language-select {{
                font-size: 0.75rem !important;
            }}
        }}
"""

if '/* Guaranteed Sticky Header on Mobile */' not in content:
    content = content.replace('/* Author Section */', sticky_mobile_css + '\n        /* Author Section */')

# 3. Update announcement bar HTML to include compact mobile label
old_announcement_inner = '<span> OFFRE SPÉCIALE D\'ACCÈS IMMÉDIAT (<span class="price-no-wrap">9&nbsp;900&nbsp;FCFA</span> AU LIEU DE <span class="price-no-wrap">19&nbsp;800&nbsp;FCFA</span>)  CETTE OFFRE EXPIRE DANS :</span>'

new_announcement_inner = '<span class="desktop-only-text"> OFFRE SPÉCIALE D\'ACCÈS IMMÉDIAT (<span class="price-no-wrap">9&nbsp;900&nbsp;FCFA</span> AU LIEU DE <span class="price-no-wrap">19&nbsp;800&nbsp;FCFA</span>)  CETTE OFFRE EXPIRE DANS :</span><span class="announcement-bar-mobile-label" style="display:none;"><i class="fa-solid fa-bolt text-pink"></i> OFFRE -50% :</span>'

content = content.replace(old_announcement_inner, new_announcement_inner)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated sticky header mobile implementation.")
