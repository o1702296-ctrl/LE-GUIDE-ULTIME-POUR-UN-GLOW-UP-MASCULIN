script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
inside_html_content = False

for line in lines:
    if 'html_content = f' in line:
        inside_html_content = True

    if inside_html_content and '/* Google Translate Seamless Integration */' in line:
        # Replace unescaped single braces in this block
        line = line.replace('display: none !important;', 'display: none !important;')

    new_lines.append(line)

content = "".join(lines)

# Fix the CSS block specifically
bad_css = """        /* Google Translate Seamless Integration */
        .goog-te-banner-frame.skiptranslate,
        .goog-te-banner-frame,
        iframe.goog-te-banner-frame {
            display: none !important;
            visibility: hidden !important;
        }
        body {
            top: 0px !important;
            position: static !important;
        }
        .goog-tooltip, .goog-tooltip:hover {
            display: none !important;
        }
        .goog-text-highlight {
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }
        #goog-gt-tt, .goog-te-balloon-frame {
            display: none !important;
        }
        .skiptranslate {
            display: inline !important;
        }"""

good_css = """        /* Google Translate Seamless Integration */
        .goog-te-banner-frame.skiptranslate,
        .goog-te-banner-frame,
        iframe.goog-te-banner-frame {{
            display: none !important;
            visibility: hidden !important;
        }}
        body {{
            top: 0px !important;
            position: static !important;
        }}
        .goog-tooltip, .goog-tooltip:hover {{
            display: none !important;
        }}
        .goog-text-highlight {{
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }}
        #goog-gt-tt, .goog-te-balloon-frame {{
            display: none !important;
        }}
        .skiptranslate {{
            display: inline !important;
        }}"""

content = content.replace(bad_css, good_css)
content = content.replace(r'match = document.cookie.match(/(?:^|;\s*)googtrans=([^;]*)/);', r'match = document.cookie.match(/(?:^|;\\s*)googtrans=([^;]*)/);')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed CSS braces in build script.")
