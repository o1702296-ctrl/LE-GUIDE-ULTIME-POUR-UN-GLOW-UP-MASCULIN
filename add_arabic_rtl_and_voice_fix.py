# -*- coding: utf-8 -*-
import os
import re

arabic_css = r"""
        /* Arabic RTL Layout Support */
        html[dir="rtl"] body {
            direction: rtl;
            text-align: right;
        }

        html[dir="rtl"] .pdf-header {
            justify-content: flex-start;
        }

        html[dir="rtl"] .pdf-title-info {
            flex-direction: row-reverse;
        }

        html[dir="rtl"] .toc-item:hover {
            padding-left: 0;
            padding-right: 10px;
        }

        html[dir="rtl"] .intro-box {
            border-left: none;
            border-right: 4px solid #7e22ce;
        }

        html[dir="rtl"] .phrase-card, html[dir="rtl"] .error-card {
            flex-direction: row-reverse;
        }

        html[dir="rtl"] .error-details {
            padding-left: 0;
            padding-right: 48px;
        }

        html[dir="rtl"] p.para {
            text-align: right;
        }

        html[dir="rtl"] .cover-badges-grid {
            direction: rtl;
        }
"""

rtl_js_sync = r"""
        function updateRTLState() {
            var savedLang = localStorage.getItem('selected_landing_lang');
            var match = document.cookie.match(/(?:^|;\s*)googtrans=([^;]*)/);
            var activeLang = savedLang || 'fr';
            if (match && match[1]) {
                var parts = match[1].split('/');
                if (parts.length >= 3 && parts[2]) {
                    activeLang = parts[2];
                }
            }
            if (activeLang === 'ar') {
                document.documentElement.setAttribute('dir', 'rtl');
            } else {
                document.documentElement.setAttribute('dir', 'ltr');
            }
        }

        document.addEventListener('DOMContentLoaded', updateRTLState);
        window.addEventListener('load', updateRTLState);
"""

# Sentence splitter regex enhancement for Arabic punctuation (؟ ، . !)
old_sentence_split = r"var parts = text.split(/(?<=[.!?])\s+/);"
new_sentence_split = r"var parts = text.split(/(?<=[.!?؟،])\s+/);"

def update_generator_for_arabic(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add RTL CSS
    if '/* Arabic RTL Layout Support */' not in content:
        content = content.replace('</style>', arabic_css + '\n    </style>')

    # Add RTL JS state sync
    if 'updateRTLState' not in content:
        content = content.replace('document.addEventListener(\'DOMContentLoaded\', syncLanguageDropdownUI);', rtl_js_sync + '\n        document.addEventListener(\'DOMContentLoaded\', syncLanguageDropdownUI);')

    # Update sentence splitter for Arabic punctuation
    content = content.replace(old_sentence_split, new_sentence_split)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Arabic RTL & Speech support in:", filepath)

update_generator_for_arabic(r'C:\Users\HP TTS\.gemini\antigravity\scratch\generate_full_guide_html.py')
update_generator_for_arabic(r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_bonus1_html.py')
update_generator_for_arabic(r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_bonus2_html.py')

print("Arabic enhancements completed!")
