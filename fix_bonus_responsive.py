script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the single brace CSS if present
bad_css = """        /* Responsive Bonus Section */
        .bonus-cards-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
        }
        .bonus-card {
            background: var(--lavender-light);
            border: 2px solid var(--purple-glow);
            border-radius: 16px;
            padding: 35px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .bonus-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(124, 58, 237, 0.15);
        }
        @media (max-width: 768px) {
            .bonus-cards-grid {
                grid-template-columns: 1fr !important;
                gap: 20px !important;
            }
            .bonus-card {
                padding: 24px 20px !important;
            }
            .bonus-card h3 {
                font-size: 1.25rem !important;
                line-height: 1.35 !important;
            }
        }"""

good_css = """        /* Responsive Bonus Section */
        .bonus-cards-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
        }}
        .bonus-card {{
            background: var(--lavender-light);
            border: 2px solid var(--purple-glow);
            border-radius: 16px;
            padding: 35px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .bonus-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(124, 58, 237, 0.15);
        }}
        @media (max-width: 768px) {{
            .bonus-cards-grid {{
                grid-template-columns: 1fr !important;
                gap: 20px !important;
            }}
            .bonus-card {{
                padding: 24px 20px !important;
            }}
            .bonus-card h3 {{
                font-size: 1.25rem !important;
                line-height: 1.35 !important;
            }}
        }}"""

if bad_css in content:
    content = content.replace(bad_css, good_css)
elif '/* Responsive Bonus Section */' not in content:
    content = content.replace('/* Author Section */', good_css + '\n        /* Author Section */')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully fixed double braces for Bonus Section CSS.")
