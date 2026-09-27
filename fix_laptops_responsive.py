script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Mobile Overrides for Laptops & Hero 3D Stage
laptop_responsive_css = """
        /* Mobile Pixel-Perfect Responsiveness for 3D Laptops & Hero Mockups */
        @media (max-width: 768px) {{
            .grand-laptops-v-stage {{
                margin-top: -15px;
            }}
            .grand-lap {{
                width: 220px !important;
                margin: 0 -10px !important;
            }}
            .lap-bezel {{
                padding: 6px !important;
                border-width: 2px !important;
            }}
            .lap-screen {{
                height: 185px !important;
                padding: 10px 6px !important;
                justify-content: space-between !important;
            }}
            .lap-screen-title {{
                font-size: 0.9rem !important;
                line-height: 1.2 !important;
                margin-bottom: 2px !important;
            }}
            .lap-screen-sub {{
                font-size: 0.72rem !important;
                margin-bottom: 4px !important;
            }}
            .lap-screen i {{
                font-size: 1.3rem !important;
                margin: 2px 0 !important;
            }}
            .lap-screen-tag {{
                font-size: 0.68rem !important;
                padding: 3px 8px !important;
                margin-top: 2px !important;
                white-space: nowrap !important;
                max-width: 95% !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
            }}
        }}

        @media (max-width: 480px) {{
            .grand-lap {{
                width: 170px !important;
                margin: 0 -8px !important;
            }}
            .lap-bezel {{
                padding: 4px !important;
            }}
            .lap-screen {{
                height: 155px !important;
                padding: 8px 4px !important;
            }}
            .lap-screen-title {{
                font-size: 0.75rem !important;
                letter-spacing: -0.2px !important;
            }}
            .lap-screen-sub {{
                font-size: 0.65rem !important;
            }}
            .lap-screen i {{
                font-size: 1.1rem !important;
            }}
            .lap-screen-tag {{
                font-size: 0.6rem !important;
                padding: 2px 6px !important;
                border-radius: 8px !important;
            }}
        }}
"""

if '/* Mobile Pixel-Perfect Responsiveness for 3D Laptops & Hero Mockups */' not in content:
    content = content.replace('/* Author Section */', laptop_responsive_css + '\n        /* Author Section */')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied laptop responsive CSS rules.")
