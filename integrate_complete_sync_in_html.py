script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire script section at the bottom of build script
start_tag = "<!-- Google Translate 100% Reliable Synchronization Engine -->"
end_tag = '<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>'

start_pos = content.find(start_tag)
end_pos = content.find(end_tag)

if start_pos != -1 and end_pos != -1:
    end_pos += len(end_tag)

    complete_sync_js = """<!-- Complete Language Synchronization & Translation Engine -->
    <script type="text/javascript">
        function setTranslateCookie(langCode) {{
            var domain = window.location.hostname;
            var cookieVal = "/fr/" + langCode;
            
            // Clear old cookies across paths and domains
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            
            // Set new cookie
            document.cookie = "googtrans=" + cookieVal + "; path=/;";
            if (domain && domain !== 'localhost' && domain !== '127.0.0.1') {{
                document.cookie = "googtrans=" + cookieVal + "; path=/; domain=" + domain + ";";
                document.cookie = "googtrans=" + cookieVal + "; path=/; domain=." + domain + ";";
            }}
        }}

        function resetToFrenchDefault() {{
            var domain = window.location.hostname;
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            document.cookie = "googtrans=/fr/fr; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=/fr/fr; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            localStorage.removeItem('selected_landing_lang');
        }}

        function googleTranslateElementInit() {{
            new google.translate.TranslateElement({{
                pageLanguage: 'fr',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
                autoDisplay: false
            }}, 'google_translate_element');
        }}

        function changePageLanguage(langCode) {{
            if (!langCode || langCode === 'fr') {{
                resetToFrenchDefault();
                location.reload();
                return;
            }}

            localStorage.setItem('selected_landing_lang', langCode);
            setTranslateCookie(langCode);

            // Attempt to change GT combo directly if initialized
            var googleSelect = document.querySelector('.goog-te-combo');
            if (googleSelect) {{
                googleSelect.value = langCode;
                googleSelect.dispatchEvent(new Event('change'));
            }}

            // Synchronize custom dropdown immediately
            var selectElem = document.getElementById('custom-language-select');
            if (selectElem) {{
                selectElem.value = langCode;
            }}

            // Reload page so Google Translate processes the new cookie cleanly across the whole document
            setTimeout(function() {{
                location.reload();
            }}, 150);
        }}

        function syncLanguageDropdownUI() {{
            var savedLang = localStorage.getItem('selected_landing_lang');
            var match = document.cookie.match(/(?:^|;\\s*)googtrans=([^;]*)/);
            var activeLang = savedLang || 'fr';

            if (match && match[1]) {{
                var parts = match[1].split('/');
                if (parts.length >= 3 && parts[2]) {{
                    activeLang = parts[2];
                }}
            }}

            var selectElem = document.getElementById('custom-language-select');
            if (selectElem && activeLang) {{
                selectElem.value = activeLang;
            }}
        }}

        function hideGTBanner() {{
            var banners = document.querySelectorAll('.goog-te-banner-frame, iframe.skiptranslate, .VIpgJd-Z44p5e-FW12eb-tjhup');
            banners.forEach(function(b) {{
                b.style.display = 'none';
                b.style.visibility = 'hidden';
            }});
            if (document.body.style.top !== '0px') {{
                document.body.style.top = '0px';
            }}
        }}

        // Attach event listeners for synchronization and banner hiding
        document.addEventListener('DOMContentLoaded', function() {{
            syncLanguageDropdownUI();
            hideGTBanner();
        }});
        window.addEventListener('load', function() {{
            syncLanguageDropdownUI();
            hideGTBanner();
        }});
        setInterval(hideGTBanner, 100);
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>"""

    content = content[:start_pos] + complete_sync_js + content[end_pos:]
    print("Successfully replaced JS block with complete synchronization engine.")
else:
    print("Could not find start/end tags. start:", start_pos, "end:", end_pos)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved build script.")
