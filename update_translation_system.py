script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = "<!-- Google Translate Script with Robust Synchronization -->"
end_tag = '<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>'

start_pos = content.find(start_tag)
end_pos = content.find(end_tag)

if start_pos != -1 and end_pos != -1:
    end_pos += len(end_tag)
    new_js = """<!-- Google Translate Script with Robust Synchronization -->
    <script type="text/javascript">
        function resetToFrenchDefault() {{
            var domain = window.location.hostname;
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            document.cookie = "googtrans=/fr/fr; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=/fr/fr; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
        }}

        function setTranslateCookie(langCode) {{
            var domain = window.location.hostname;
            var cookieVal = "/fr/" + langCode;
            document.cookie = "googtrans=" + cookieVal + "; path=/;";
            if (domain && domain !== 'localhost' && domain !== '127.0.0.1') {{
                document.cookie = "googtrans=" + cookieVal + "; path=/; domain=" + domain + ";";
            }}
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

            setTranslateCookie(langCode);

            var googleSelect = document.querySelector('.goog-te-combo');
            if (googleSelect) {{
                googleSelect.value = langCode;
                googleSelect.dispatchEvent(new Event('change'));
            }}
            
            // Reload page to force Google Translate to translate full document seamlessly
            setTimeout(function() {{
                location.reload();
            }}, 300);
        }}

        function syncLanguageDropdown() {{
            var match = document.cookie.match(/(?:^|;\\s*)googtrans=([^;]*)/);
            var activeLang = 'fr';
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

        document.addEventListener('DOMContentLoaded', syncLanguageDropdown);
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>"""

    content = content[:start_pos] + new_js + content[end_pos:]
    print("Replaced script tags with double braces.")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated build script.")
