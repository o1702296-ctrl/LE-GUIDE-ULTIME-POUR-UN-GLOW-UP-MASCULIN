import os

build_landing = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'
build_guide = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_violet_guide.py'

master_sync_js = """<!-- Master Language Synchronization & Translation Engine -->
    <div id="google_translate_element" style="position: absolute; left: -9999px; top: -9999px; opacity: 0; pointer-events: none;"></div>
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
            localStorage.removeItem('landing_selected_lang');
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

            localStorage.setItem('landing_selected_lang', langCode);
            setTranslateCookie(langCode);

            // Update custom dropdown UI immediately
            var selectElem = document.getElementById('custom-language-select');
            if (selectElem) {{
                selectElem.value = langCode;
            }}

            // Attempt to trigger GT combo directly if available
            var googleSelect = document.querySelector('.goog-te-combo');
            if (googleSelect) {{
                googleSelect.value = langCode;
                googleSelect.dispatchEvent(new Event('change'));
            }}

            // Refresh page so Google Translate processes the cookie cleanly across the document
            setTimeout(function() {{
                location.reload();
            }}, 150);
        }}

        function syncLanguageDropdownUI() {{
            var savedLang = localStorage.getItem('landing_selected_lang');
            var match = document.cookie.match(/(?:^|;\\s*)googtrans=([^;]*)/);
            var activeLang = savedLang || 'fr';

            if (match && match[1]) {{
                var parts = match[1].split('/');
                if (parts.length >= 3 && parts[2]) {{
                    activeLang = parts[2];
                }}
            }}

            var selectElem = document.getElementById('custom-language-select');
            if (selectElem && activeLang && selectElem.value !== activeLang) {{
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

        // Event Listeners for Bulletproof Sync
        document.addEventListener('DOMContentLoaded', function() {{
            syncLanguageDropdownUI();
            hideGTBanner();
        }});
        window.addEventListener('load', function() {{
            syncLanguageDropdownUI();
            hideGTBanner();
        }});
        setInterval(syncLanguageDropdownUI, 500);
        setInterval(hideGTBanner, 100);
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>"""

# 1. Update landing build script
with open(build_landing, 'r', encoding='utf-8') as f:
    landing_code = f.read()

start_tag = "<!-- Complete Language Synchronization & Translation Engine -->"
end_tag = '<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>'

sp = landing_code.find(start_tag)
ep = landing_code.find(end_tag)

if sp != -1 and ep != -1:
    ep += len(end_tag)
    landing_code = landing_code[:sp] + master_sync_js + landing_code[ep:]
    with open(build_landing, 'w', encoding='utf-8') as f:
        f.write(landing_code)
    print("Master sync applied to landing build script.")

# 2. Update guide build script
with open(build_guide, 'r', encoding='utf-8') as f:
    guide_code = f.read()

sp_g = guide_code.find('<!-- Complete Multi-Language Synchronization Engine -->')
if sp_g == -1:
    sp_g = guide_code.find('<div id="google_translate_element"')

ep_g = guide_code.find('<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>')

if sp_g != -1 and ep_g != -1:
    ep_g += len(ep_g_tag := end_tag)
    guide_code = guide_code[:sp_g] + master_sync_js + guide_code[ep_g:]
    with open(build_guide, 'w', encoding='utf-8') as f:
        f.write(guide_code)
    print("Master sync applied to guide build script.")

