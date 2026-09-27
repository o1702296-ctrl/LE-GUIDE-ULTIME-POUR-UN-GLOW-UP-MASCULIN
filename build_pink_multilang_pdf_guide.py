# -*- coding: utf-8 -*-
import os
import re

input_file = r"C:\Users\HP TTS\.gemini\antigravity\scratch\pdf_guide_lina_rela.html"
if not os.path.exists(input_file):
    input_file = r"C:\Users\HP TTS\.gemini\antigravity\scratch\pdf_guide_dora_elysiane.html"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace Dora Elysiane with Lina Rela
content = content.replace("Dora Elysiane", "Lina Rela")
content = content.replace("DORA ELYSIANE", "LINA RELA")
content = content.replace("dora_elysiane", "lina_rela")

# 2. Pink Theme CSS definition
pink_style = """
    <style>
        :root {
            --pdf-bg: #2b0b1c; /* Background of dark rose viewer */
            --page-bg: #ffffff; /* Clean page background */
            --text-color: #2b2b2b; /* Text color */
            --text-heading: #831843; /* Deep magenta heading */
            --accent-pink: #ec4899; /* Vibrant pink */
            --accent-pink-dark: #be185d; /* Dark vibrant rose */
            --accent-pink-light: #fbcfe8; /* Soft pink tint */
            --accent-rose-gold: #f472b6; /* Rose gold / light pink */
            --border-color: #fbcfe8; /* Pink border */
            --box-gold-bg: #fff0f5; /* Soft rose quote box */
            --box-sister-bg: #fce7f3; /* Pink sister advice box */
            --box-metaphor-bg: #fff1f2; /* Rose water metaphor box */
            --font-main: 'Inter', sans-serif;
            --font-heading: 'Outfit', sans-serif;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        html {
            background-color: var(--pdf-bg);
            font-family: var(--font-main);
            color: var(--text-color);
            line-height: 1.6;
            scroll-behavior: smooth;
        }

        body {
            top: 0px !important;
            position: static !important;
            padding-top: 65px;
            padding-bottom: 50px;
        }

        /* Hide Google Translate Top Banner */
        .goog-te-banner-frame, iframe.skiptranslate, .VIpgJd-Z44p5e-FW12eb-tjhup { display: none !important; }
        #goog-gt-tt { display: none !important; }
        .goog-text-highlight { background-color: transparent !important; box-shadow: none !important; }
        body { top: 0px !important; }

        /* Fixed PDF Navigation Toolbar - Dark Pink / Magenta Design */
        .pdf-toolbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: linear-gradient(90deg, #4a0e2e 0%, #701a40 50%, #4a0e2e 100%);
            border-bottom: 2px solid var(--accent-pink);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
            z-index: 2000;
            box-shadow: 0 4px 20px rgba(236, 72, 153, 0.35);
            flex-wrap: wrap;
            gap: 10px;
        }

        .pdf-title-info {
            display: flex;
            align-items: center;
            gap: 10px;
            font-family: var(--font-heading);
            font-weight: 700;
            font-size: 0.95rem;
            color: #ffffff;
            white-space: nowrap;
        }

        .pdf-title-info i { color: #f472b6; font-size: 1.15rem; }

        .pdf-controls-center {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .chapter-select {
            background: #701a40;
            border: 1px solid var(--accent-pink);
            color: #ffffff;
            padding: 7px 14px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            outline: none;
            cursor: pointer;
        }
        .chapter-select option { background: #4a0e2e; color: #ffffff; }

        .pdf-controls-right {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .pdf-lang-dropdown {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #701a40;
            padding: 6px 14px;
            border-radius: 20px;
            border: 1px solid var(--accent-pink);
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }

        #custom-language-select {
            background: transparent;
            border: none;
            color: #ffffff;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            outline: none;
        }
        #custom-language-select option { background: #4a0e2e; color: #ffffff; }

        .btn-pdf-print {
            background: linear-gradient(135deg, #ec4899, #be185d);
            color: #ffffff;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            transition: all 0.2s ease;
            box-shadow: 0 2px 10px rgba(236, 72, 153, 0.4);
        }
        .btn-pdf-print:hover {
            background: linear-gradient(135deg, #f472b6, #db2777);
            transform: translateY(-1px);
        }

        /* Document Layout */
        .pdf-document-container {
            max-width: 840px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .pdf-page {
            background: var(--page-bg);
            width: 100%;
            min-height: 1120px;
            box-shadow: 0 12px 40px rgba(0,0,0,0.4);
            border-radius: 6px;
            padding: 50px 60px 40px;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border: 1px solid var(--border-color);
        }

        .pdf-header {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            font-size: 0.85rem;
            color: var(--accent-pink-dark);
            font-style: italic;
            border-bottom: 1.5px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 30px;
            font-weight: 600;
        }

        .pdf-footer {
            border-top: 1.5px solid var(--border-color);
            padding-top: 12px;
            margin-top: 30px;
            text-align: center;
            font-size: 0.85rem;
            color: var(--accent-pink-dark);
            font-weight: 700;
        }

        .pdf-body { flex: 1; }

        /* Cover Page Styling - Full Pink & Rose Gold Gradient */
        .pdf-page.cover-page {
            background: linear-gradient(135deg, #be185d 0%, #831843 55%, #4c0519 100%);
            color: #ffffff;
            padding: 60px 40px 0px;
            text-align: center;
            justify-content: space-between;
            border: none;
        }

        .cover-top-header {
            font-family: var(--font-heading);
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 2.5px;
            color: #fbcfe8;
            text-transform: uppercase;
            margin-top: 15px;
        }

        .cover-main-title {
            font-size: 3.6rem;
            font-weight: 900;
            line-height: 1.05;
            margin: 30px 0 10px;
            letter-spacing: 1px;
            font-family: var(--font-heading);
            color: #ffffff;
            text-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        .cover-subtitle {
            font-size: 1.9rem;
            color: #fbcfe8;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-family: var(--font-heading);
        }

        .cover-stars { color: #f472b6; font-size: 1.4rem; margin: 15px 0; letter-spacing: 6px; }

        .cover-tagline { font-size: 1.1rem; font-style: italic; color: #fce7f3; max-width: 600px; margin: 0 auto 25px; }

        .cover-author-wrapper {
            border-top: 2px solid #f472b6;
            border-bottom: 2px solid #f472b6;
            padding: 12px 0;
            margin: 25px auto;
            max-width: 520px;
        }

        .cover-author-name {
            font-size: 2.3rem;
            font-weight: 800;
            color: #fbcfe8;
            font-style: italic;
            font-family: var(--font-heading);
            letter-spacing: 1px;
        }

        .cover-author-role { font-size: 0.95rem; color: #ffffff; margin-top: 4px; font-weight: 500; }

        .cover-badges-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            max-width: 650px;
            margin: 25px auto 30px;
        }

        .cover-badge-item {
            border: 1.5px solid rgba(244, 114, 182, 0.7);
            border-radius: 8px;
            padding: 10px 4px;
            font-size: 0.85rem;
            font-weight: 700;
            color: #ffffff;
            background: rgba(236, 72, 153, 0.25);
            backdrop-filter: blur(4px);
        }

        .cover-bottom-bar {
            background: #db2777;
            color: #ffffff;
            font-weight: 800;
            padding: 18px 20px;
            font-size: 0.95rem;
            margin-left: -40px;
            margin-right: -40px;
            letter-spacing: 0.5px;
        }

        /* Typography & Content Elements */
        h1.page-h1 {
            font-family: var(--font-heading);
            color: var(--text-heading);
            font-size: 2.2rem;
            margin-bottom: 8px;
            font-weight: 800;
        }

        h2.page-h2 {
            font-family: var(--font-heading);
            color: var(--accent-pink-dark);
            font-size: 1.5rem;
            margin: 24px 0 12px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 6px;
            font-weight: 700;
        }

        h3.page-h3 {
            font-family: var(--font-heading);
            color: var(--accent-pink-dark);
            font-size: 1.25rem;
            margin: 18px 0 8px;
            font-weight: 700;
        }

        .page-sub { color: #db2777; font-style: italic; font-size: 1.08rem; margin-bottom: 20px; font-weight: 600; }

        p.para { margin-bottom: 16px; text-align: justify; font-size: 0.98rem; line-height: 1.7; }

        /* Boxes & Components */
        .pdf-quote-box {
            border: 1.5px solid #f472b6;
            background: var(--box-gold-bg);
            padding: 22px 26px;
            border-radius: 8px;
            margin: 22px 0;
            text-align: center;
            box-shadow: 0 4px 12px rgba(244, 114, 182, 0.15);
        }

        .pdf-quote-text {
            font-size: 1.08rem;
            font-weight: 700;
            color: #831843;
            font-style: italic;
            line-height: 1.6;
        }

        .pdf-sister-box {
            border: 1.5px solid #ec4899;
            background: var(--box-sister-bg);
            padding: 20px;
            border-radius: 8px;
            margin: 22px 0;
            box-shadow: 0 4px 12px rgba(236, 72, 153, 0.12);
        }

        .pdf-sister-header {
            background: #db2777;
            color: #ffffff;
            font-weight: 800;
            font-size: 0.92rem;
            padding: 6px 14px;
            display: inline-block;
            margin-bottom: 12px;
            border-radius: 4px;
            letter-spacing: 0.5px;
        }

        .pdf-metaphor-box {
            border: 1.5px solid #f43f5e;
            background: var(--box-metaphor-bg);
            border-radius: 8px;
            overflow: hidden;
            margin: 22px 0;
            box-shadow: 0 4px 12px rgba(244, 63, 94, 0.12);
        }

        .pdf-metaphor-header {
            background: #be185d;
            color: #ffffff;
            font-weight: 800;
            padding: 10px 16px;
            font-size: 0.98rem;
            letter-spacing: 0.5px;
        }

        .pdf-metaphor-body { padding: 16px; font-size: 0.95rem; line-height: 1.65; color: #4c0519; }

        /* Table of Contents Clickable Items */
        .toc-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 15px;
        }

        .toc-item {
            display: block;
            text-decoration: none;
            border-bottom: 1px dashed #f472b6;
            padding-bottom: 8px;
            padding-top: 4px;
            transition: all 0.2s ease;
            cursor: pointer;
            border-radius: 4px;
        }

        .toc-item:hover {
            background: #fce7f3;
            padding-left: 10px;
        }

        .toc-title { font-weight: 800; color: var(--text-heading); font-size: 1.08rem; }
        .toc-desc { font-style: italic; color: #701a40; font-size: 0.92rem; margin-top: 2px; }

        /* Checklists */
        .checklist { list-style: none; margin: 16px 0; }
        .checklist li { position: relative; padding-left: 28px; margin-bottom: 10px; font-size: 0.96rem; line-height: 1.6; }
        .checklist li::before { content: "✓"; position: absolute; left: 0; color: #db2777; font-weight: 900; font-size: 1.1rem; }
        .checklist-cross li::before { content: "✗"; color: #e11d48; }

        .chapter-badge {
            background: linear-gradient(135deg, #db2777, #9d174d);
            color: #fff;
            padding: 5px 16px;
            border-radius: 4px;
            display: inline-block;
            font-weight: 800;
            font-size: 0.85rem;
            margin-bottom: 10px;
            letter-spacing: 0.5px;
            box-shadow: 0 2px 8px rgba(219, 39, 119, 0.3);
        }

        /* Print Styles */
        @media print {
            body { padding-top: 0; background: #fff; }
            .pdf-toolbar { display: none !important; }
            .pdf-document-container { padding: 0; max-width: 100%; gap: 0; }
            .pdf-page { box-shadow: none; border-radius: 0; page-break-after: always; min-height: 100vh; padding: 40px; border: none; }
        }

        /* Responsive Mobile Layout */
        @media (max-width: 768px) {
            .pdf-page { padding: 30px 20px 25px; }
            .cover-main-title { font-size: 2.5rem; }
            .cover-subtitle { font-size: 1.4rem; }
            .cover-badges-grid { grid-template-columns: repeat(2, 1fr); }
            .pdf-toolbar { height: auto; padding: 10px; justify-content: center; }
            .chapter-select { max-width: 100%; }
        }
    </style>
"""

# Replace the existing <style>...</style> block with pink_style
content = re.sub(r'<style>.*?</style>', pink_style, content, flags=re.DOTALL)

# Check language dropdown inside content, ensure full language support
lang_dropdown_html = """
            <div class="pdf-lang-dropdown">
                <i class="fa-solid fa-globe" style="color: var(--accent-rose-gold);"></i>
                <select id="custom-language-select" onchange="changePageLanguage(this.value)">
                    <option value="fr">🇫🇷 Français</option>
                    <option value="en">🇬🇧 English</option>
                    <option value="es">🇪🇸 Español</option>
                    <option value="de">🇩🇪 Deutsch</option>
                    <option value="it">🇮🇹 Italiano</option>
                    <option value="pt">🇵🇹 Português</option>
                    <option value="nl">🇳🇱 Nederlands</option>
                    <option value="ar">🇸🇦 العربية</option>
                    <option value="tr">🇹🇷 Türkçe</option>
                    <option value="ru">🇷🇺 Русский</option>
                    <option value="zh-CN">🇨🇳 中文</option>
                </select>
            </div>
"""

# Check for scripts at bottom of body, add multi-lang switching script
multilang_js = """
    <div id="google_translate_element" style="display:none!important;"></div>
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'fr',
                includedLanguages: 'fr,en,es,de,it,pt,nl,ar,tr,ru,zh-CN',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
                autoDisplay: false
            }, 'google_translate_element');
        }
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

    <script>
        function changePageLanguage(langCode) {
            if (!langCode) return;
            localStorage.setItem('selected_pdf_language', langCode);
            var select = document.querySelector('.goog-te-combo');
            if (select) {
                select.value = langCode;
                select.dispatchEvent(new Event('change'));
            } else {
                var attempts = 0;
                var interval = setInterval(function() {
                    attempts++;
                    var s = document.querySelector('.goog-te-combo');
                    if (s) {
                        s.value = langCode;
                        s.dispatchEvent(new Event('change'));
                        clearInterval(interval);
                    }
                    if (attempts > 20) clearInterval(interval);
                }, 300);
            }
        }

        function scrollToSection(id) {
            var elem = document.getElementById(id);
            if (elem) {
                elem.scrollIntoView({ behavior: 'smooth' });
            }
        }

        window.addEventListener('DOMContentLoaded', function() {
            var savedLang = localStorage.getItem('selected_pdf_language');
            if (savedLang) {
                var langSelect = document.getElementById('custom-language-select');
                if (langSelect) langSelect.value = savedLang;
                setTimeout(function() {
                    changePageLanguage(savedLang);
                }, 1000);
            }
        });
    </script>
</body>
"""

content = content.replace("</body>", multilang_js)

# Write out transformed file to multiple target locations
target_paths = [
    r"C:\Users\HP TTS\.gemini\antigravity\scratch\pdf_guide_lina_rela.html",
    r"C:\Users\HP TTS\.gemini\antigravity\scratch\guide.html",
    r"C:\Users\HP TTS\.gemini\antigravity\scratch\index.html",
    r"C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\guide.html",
    r"C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\pdf_guide_lina_rela.html",
    r"C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing\index.html"
]

for tp in target_paths:
    os.makedirs(os.path.dirname(tp), exist_ok=True)
    with open(tp, "w", encoding="utf-8") as out:
        out.write(content)

print(f"Successfully written Pink Multi-Lang PDF Guide Lina Rela to {len(target_paths)} locations.")
