import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for language switcher flag badge
lang_flag_css = '''
        /* MULTI-LANGUAGE SYNCHRONIZATION SELECTOR WITH CRISP HD COUNTRY FLAGS */
        .lang-switcher-wrap {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(168, 85, 247, 0.25);
            border: 1px solid var(--accent-purple-bright);
            padding: 4px 12px;
            border-radius: var(--radius-full);
            box-shadow: 0 0 14px rgba(168, 85, 247, 0.5);
            margin-left: 10px;
        }

        .lang-flag-badge {
            width: 22px;
            height: 15px;
            object-fit: cover;
            border-radius: 2px;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
            display: inline-block;
        }

        .lang-select {
            background: transparent;
            border: none;
            color: #ffffff;
            font-size: 0.85rem;
            font-weight: 800;
            cursor: pointer;
            outline: none;
            font-family: var(--font-main);
        }

        .lang-select option {
            background: #0e091a;
            color: #ffffff;
            padding: 8px;
        }
'''

content = re.sub(r'/\* MULTI-LANGUAGE SYNCHRONIZATION SELECTOR \*/.*?\/\* Hide Google Translate', lang_flag_css + '\n        /* Hide Google Translate', content, flags=re.DOTALL)

# 2. Update HTML for language switcher with explicit country flag image
new_lang_html = '''        <!-- Multi-Language Selector Widget with HD Country Flags -->
        <div class="lang-switcher-wrap">
            <img id="selected-lang-flag" src="https://flagcdn.com/w40/fr.png" alt="Drapeau Langue" class="lang-flag-badge">
            <select id="language-select" class="lang-select" onchange="translatePage(this.value)">
                <option value="fr" data-flag="https://flagcdn.com/w40/fr.png" selected>Français (FR)</option>
                <option value="en" data-flag="https://flagcdn.com/w40/gb.png">English (UK)</option>
                <option value="es" data-flag="https://flagcdn.com/w40/es.png">Español (ES)</option>
                <option value="de" data-flag="https://flagcdn.com/w40/de.png">Deutsch (DE)</option>
                <option value="pt" data-flag="https://flagcdn.com/w40/pt.png">Português (PT)</option>
                <option value="it" data-flag="https://flagcdn.com/w40/it.png">Italiano (IT)</option>
                <option value="ar" data-flag="https://flagcdn.com/w40/sa.png">العربية (AR)</option>
                <option value="zh-CN" data-flag="https://flagcdn.com/w40/cn.png">中文 (ZH)</option>
                <option value="ru" data-flag="https://flagcdn.com/w40/ru.png">Русский (RU)</option>
                <option value="ja" data-flag="https://flagcdn.com/w40/jp.png">日本語 (JA)</option>
            </select>
        </div>'''

content = re.sub(r'<!-- Multi-Language Selector Widget -->\s*<div class="lang-switcher-wrap">.*?</div>', new_lang_html, content, flags=re.DOTALL)

# 3. Update translatePage JS function to synchronize flag image
new_translate_js = '''
        function translatePage(langCode) {
            var select = document.querySelector('.goog-te-combo');
            if (select) {
                select.value = langCode;
                select.dispatchEvent(new Event('change'));
                localStorage.setItem('glowup_landing_lang', langCode);
            }
            updateLanguageFlagBadge(langCode);
        }

        function updateLanguageFlagBadge(langCode) {
            var flagImg = document.getElementById('selected-lang-flag');
            var langSelect = document.getElementById('language-select');
            if (flagImg && langSelect) {
                var selectedOption = langSelect.options[langSelect.selectedIndex];
                if (selectedOption) {
                    var flagUrl = selectedOption.getAttribute('data-flag');
                    if (flagUrl) {
                        flagImg.src = flagUrl;
                    }
                }
            }
        }

        // Restore saved language preference on load
        window.addEventListener('load', function() {
            var savedLang = localStorage.getItem('glowup_landing_lang');
            if (savedLang) {
                setTimeout(function() {
                    var langSelect = document.getElementById('language-select');
                    if (langSelect) {
                        langSelect.value = savedLang;
                        updateLanguageFlagBadge(savedLang);
                    }
                    if (savedLang !== 'fr') {
                        translatePage(savedLang);
                    }
                }, 1200);
            }
        });
'''

content = re.sub(r'function translatePage\(langCode\).*?\}\);\s*</script>', new_translate_js.strip() + '\n    </script>', content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added HD country flag image synchronization to language selector!")
