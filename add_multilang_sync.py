import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Language Switcher CSS before </style>
lang_css = '''
        /* MULTI-LANGUAGE SYNCHRONIZATION SELECTOR */
        .lang-switcher-wrap {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(168, 85, 247, 0.25);
            border: 1px solid var(--accent-purple-bright);
            padding: 3px 10px;
            border-radius: var(--radius-full);
            box-shadow: 0 0 14px rgba(168, 85, 247, 0.5);
            margin-left: 10px;
        }

        .lang-icon {
            color: var(--accent-purple-glow);
            font-size: 0.9rem;
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
            padding: 6px;
        }

        /* Hide Google Translate top iframe banner to keep dark monarch theme pristine */
        body {
            top: 0 !important;
        }
        .goog-te-banner-frame {
            display: none !important;
        }
        .goog-te-gadget {
            display: none !important;
        }
        body > .skiptranslate {
            display: none !important;
        }
    </style>
'''
content = content.replace('    </style>', lang_css)

# 2. Add Language Selector to Sticky Urgency Header Top Bar
top_bar_old = '''        <div class="urgency-text" style="font-size:0.85rem; opacity: 0.95;">
            (OFFRE FLASH -50% : LIMITÉE AUX 50 PREMIÈRES PERSONNES)
        </div>
    </div>'''

top_bar_new = '''        <div class="urgency-text" style="font-size:0.85rem; opacity: 0.95;">
            (OFFRE FLASH -50% : LIMITÉE AUX 50 PREMIÈRES PERSONNES)
        </div>
        
        <!-- Multi-Language Selector Widget -->
        <div class="lang-switcher-wrap">
            <i class="fa-solid fa-globe lang-icon"></i>
            <select id="language-select" class="lang-select" onchange="translatePage(this.value)">
                <option value="fr" selected>🇫🇷 FR</option>
                <option value="en">🇬🇧 EN</option>
                <option value="es">🇪🇸 ES</option>
                <option value="de">🇩🇪 DE</option>
                <option value="pt">🇵🇹 PT</option>
                <option value="it">🇮🇹 IT</option>
                <option value="ar">🇸🇦 AR</option>
                <option value="zh-CN">🇨🇳 ZH</option>
                <option value="ru">🇷🇺 RU</option>
                <option value="ja">🇯🇵 JA</option>
            </select>
        </div>
    </div>'''

content = content.replace(top_bar_old, top_bar_new)

# 3. Add Google Translate Hidden Element & Sync Script before </body>
google_translate_script = '''
    <!-- GOOGLE TRANSLATE MULTI-LANGUAGE SYNCHRONIZATION ENGINE -->
    <div id="google_translate_element" style="display:none;"></div>
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'fr',
                includedLanguages: 'fr,en,es,de,pt,it,ar,zh-CN,ru,ja',
                autoDisplay: false
            }, 'google_translate_element');
        }

        function translatePage(langCode) {
            var select = document.querySelector('.goog-te-combo');
            if (select) {
                select.value = langCode;
                select.dispatchEvent(new Event('change'));
                localStorage.setItem('glowup_landing_lang', langCode);
            }
        }

        // Restore saved language preference on load
        window.addEventListener('load', function() {
            var savedLang = localStorage.getItem('glowup_landing_lang');
            if (savedLang && savedLang !== 'fr') {
                setTimeout(function() {
                    var langSelect = document.getElementById('language-select');
                    if (langSelect) langSelect.value = savedLang;
                    translatePage(savedLang);
                }, 1200);
            }
        });
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</body>
'''

content = content.replace('</body>', google_translate_script)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully integrated multi-language synchronization widget into landing page!")
