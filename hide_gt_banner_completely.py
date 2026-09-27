script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

bad_js_fix = """        function hideGTBanner() {
            var banners = document.querySelectorAll('.goog-te-banner-frame, iframe.skiptranslate, .VIpgJd-Z44p5e-FW12eb-tjhup');
            banners.forEach(function(b) {
                b.style.display = 'none';
                b.style.visibility = 'hidden';
            });
            if (document.body.style.top !== '0px') {
                document.body.style.top = '0px';
            }
        }
        setInterval(hideGTBanner, 100);"""

good_js_fix = """        function hideGTBanner() {{
            var banners = document.querySelectorAll('.goog-te-banner-frame, iframe.skiptranslate, .VIpgJd-Z44p5e-FW12eb-tjhup');
            banners.forEach(function(b) {{
                b.style.display = 'none';
                b.style.visibility = 'hidden';
            }});
            if (document.body.style.top !== '0px') {{
                document.body.style.top = '0px';
            }}
        }}
        setInterval(hideGTBanner, 100);"""

if bad_js_fix in content:
    content = content.replace(bad_js_fix, good_js_fix)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed braces in hideGTBanner JS.")
