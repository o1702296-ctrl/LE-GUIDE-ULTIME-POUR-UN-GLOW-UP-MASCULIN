script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Build native translation JS block
native_i18n_js = """    <!-- Native French / English Dual Translation Engine + Google Translate Fallback -->
    <script type="text/javascript">
        var i18nMap = {{
            "OFFRE SPÉCIALE D'ACCÈS IMMÉDIAT (9 900 FCFA AU LIEU DE 19 800 FCFA)  CETTE OFFRE EXPIRE DANS :": "SPECIAL IMMEDIATE ACCESS OFFER (9,900 FCFA INSTEAD OF 19,800 FCFA)  THIS OFFER EXPIRES IN:",
            "OFFRE -50% :": "50% OFF OFFER:",
            "OFFRE EXCLUSIVE — ACCÈS IMMÉDIAT": "EXCLUSIVE OFFER — IMMEDIATE ACCESS",
            "COMMENT SAUVER TON COUPLE ET RETAILLER L'HARMONIE SANS DISPUTES NI DISTANCE": "HOW TO SAVE YOUR RELATIONSHIP AND RESTORE HARMONY WITHOUT ARGUMENTS OR DISTANCE",
            "Le guide ultime pour l'homme moderne : désamorce les tensions, comprends la psychologie féminine et rebâtis une complicité solide en moins de 30 jours.": "The ultimate guide for the modern man: defuse tensions, understand female psychology, and rebuild a solid connection in less than 30 days.",
            "Ce programme est fait pour toi si :": "This program is made for you if:",
            "Tu sens de la distance ou de l'incompréhension dans ton couple.": "You feel distance or misunderstanding in your relationship.",
            "Les discussions finissent souvent en disputes ou en silence.": "Discussions often end in arguments or silence.",
            "Tu veux reprendre le contrôle émotionnel et sauver ta relation.": "You want to regain emotional control and save your relationship.",
            "ACCÈS NUMÉRIQUE IMMÉDIAT": "IMMEDIATE DIGITAL ACCESS",
            "GARANTIE 30 JOURS": "30-DAY GUARANTEE",
            "PAIEMENT SÉCURISÉ": "SECURE PAYMENT",
            "SEULEMENT": "ONLY",
            "AU LIEU DE": "INSTEAD OF",
            "SAUVER TON COUPLE — GUIDE OFFICIEL": "SAVE YOUR RELATIONSHIP — OFFICIAL GUIDE",
            "GUIDE PRINCIPAL (9 CHAPITRES)": "MAIN GUIDE (9 CHAPTERS)",
            "GUIDE OFFICIEL": "OFFICIAL GUIDE",
            "HOMME MODERNE": "MODERN MAN",
            "BONUS #1 : 10 PHRASES": "BONUS #1: 10 PHRASES",
            "M1 : DIAGNOSTIC": "M1: DIAGNOSIS",
            "M2 : INTIMITÉ & RESPECT": "M2: INTIMACY & RESPECT",
            "M3 : PLAN 30 JOURS": "M3: 30-DAY PLAN",
            "BONUS #2 : 12 ERREURS": "BONUS #2: 12 ERRORS",
            "FICHES D'ACTION": "ACTION SHEETS",
            "Guide Ultime": "Ultimate Guide",
            "Guide Complet (9 Chapitres)": "Complete Guide (9 Chapters)",
            "PLAN 30 JOURS & BONUS": "30-DAY PLAN & BONUSES",
            "Action & Désamorçage": "Action & Defusing",
            "10 Phrases + 12 Erreurs": "10 Phrases + 12 Errors",
            "DIAGNOSTIC & RÉALITÉ": "DIAGNOSIS & REALITY",
            "LES 3 ERREURS FATALES QUI DÉTRUISENT SILENCIEUSEMENT TON COUPLE": "THE 3 FATAL MISTAKES SILENTLY DESTROYING YOUR RELATIONSHIP",
            "La majorité des hommes commettent ces erreurs sans s'en rendre compte, pensant bien faire :": "Most men make these mistakes without realizing it, thinking they are doing the right thing:",
            "Erreur #1 : Vouloir tout résoudre par la logique brute": "Mistake #1: Trying to solve everything with raw logic",
            "Quand ta partenaire exprime une émotion, elle ne cherche pas immédiatement une solution technique. Ignorer l'émotion crée un sentiment d'incompréhension.": "When your partner expresses an emotion, she is not immediately looking for a technical solution. Ignoring the emotion creates a feeling of being misunderstood.",
            "Erreur #2 : Le retrait et le silence radio non maîtrisé": "Mistake #2: Withdrawal and uncontrolled silent treatment",
            "Fuir la discussion ou se fermer totalement pour éviter le conflit aggrave l'anxiété et la colère de l'autre, interprété comme du désintérêt.": "Fleeing discussion or shutting down completely to avoid conflict worsens anxiety and anger, interpreted as disinterest.",
            "Erreur #3 : Laisser les rancœurs s'accumuler": "Mistake #3: Letting resentment build up",
            "Ne pas désamorcer les petites frictions quotidiennes transforme des détails en crises majeures au bout de quelques mois.": "Failing to defuse small daily frictions turns minor details into major crises after a few months.",
            "UNE MÉTHODE STRUCTURÉE": "A STRUCTURED METHOD",
            "COMMENT CE PROGRAMME VA TRANSFORMER TA RELATION EN 3 ÉTAPES": "HOW THIS PROGRAM WILL TRANSFORM YOUR RELATIONSHIP IN 3 STEPS",
            "Un parcours clair, pragmatique et orienté résultats pour reprendre le contrôle :": "A clear, pragmatic, result-oriented roadmap to regain control:",
            "Étape 1 : Désamorcer les crises et stopper l'escalade": "Step 1: Defuse crises and stop escalation",
            "Apprends les phrases exactes et l'attitude émotionnelle pour apaiser immédiatement toute tension.": "Learn the exact phrases and emotional stance to instantly defuse any tension.",
            "Étape 2 : Comprendre la psychologie et restaurer l'attraction": "Step 2: Understand psychology and restore attraction",
            "Rétablis le respect mutuel, la communication profonde et ravive la complicité des débuts.": "Re-establish mutual respect, deep communication, and reignite early intimacy.",
            "Étape 3 : Ancrer une harmonie durable sur 30 jours": "Step 3: Anchor lasting harmony over 30 days",
            "Applique le plan d'action quotidien pour instaurer des habitudes saines et un foyer apaisé.": "Apply the daily action plan to establish healthy habits and a peaceful home.",
            "LE PROGRAMME DÉTAILLÉ": "THE DETAILED PROGRAM",
            "CONTENU DU GUIDE ULTIME \\"SAUVER TON COUPLE\\"": "CONTENT OF THE ULTIMATE GUIDE \\"SAVE YOUR RELATIONSHIP\\"",
            "9 chapitres puissants conçus pour agir rapidement et efficacement :": "9 powerful chapters designed for fast and effective action:",
            "Chapitre 1 : Le Diagnostic de la Relation": "Chapter 1: Relationship Diagnosis",
            "Identifier les vraies causes des tensions et faire un état des lieux lucide.": "Identify the real causes of tension and make a clear assessment.",
            "Chapitre 2 : Maîtriser ses Émotions sous Pression": "Chapter 2: Master Your Emotions Under Pressure",
            "Garder son calme, éviter la colère impulsive et projeter de la sérénité.": "Keep calm, avoid impulsive anger, and project serenity.",
            "Chapitre 3 : La Communication de Crise": "Chapter 3: Crisis Communication",
            "Les techniques pour écouter sans s'énerver et exprimer ses besoins clairement.": "Techniques to listen without getting angry and express your needs clearly.",
            "Chapitre 4 : Comprendre la Psychologie Féminine": "Chapter 4: Understand Female Psychology",
            "Décoder les attentes implicites et ce que recherche réellement ta partenaire.": "Decode implicit expectations and what your partner is truly looking for.",
            "Chapitre 5 : Désamorcer les Disputes Instantanément": "Chapter 5: Instantly Defuse Disputes",
            "Les 10 clés pour désarmer l'agressivité et transformer le conflit en dialogue.": "The 10 keys to disarm aggressiveness and turn conflict into dialogue.",
            "Chapitre 6 : Reconstruire la Confiance et le Respect": "Chapter 6: Rebuild Trust and Respect",
            "Effacer les rancœurs du passé et poser des bases saines et durables.": "Clear past resentment and set healthy, lasting foundations.",
            "Chapitre 7 : Rallumer l'Intimité et la Complicité": "Chapter 7: Reignite Intimacy and Connection",
            "Retrouver la séduction, l'attention et la chaleur dans le couple.": "Rediscover attraction, attentiveness, and warmth in the relationship.",
            "Chapitre 8 : Gérer les Situations Difficiles": "Chapter 8: Handle Difficult Situations",
            "Faire face au doute, à la distance et aux choix décisifs avec maturité.": "Face doubt, distance, and decisive choices with maturity.",
            "Chapitre 9 : Le Plan d'Action sur 30 Jours": "Chapter 9: The 30-Day Action Plan",
            "Un programme jour par jour pour appliquer la méthode et pérenniser les résultats.": "A day-by-day program to apply the method and sustain results.",
            "MAIS CE N'EST PAS TOUT !": "BUT THAT'S NOT ALL!",
            "VOICI LES BONUS EXCLUSIFS INCLUS DANS VOTRE PROGRAMME": "HERE ARE THE EXCLUSIVE BONUSES INCLUDED IN YOUR PROGRAM",
            "Des ressources complémentaires prêtes à l'emploi offertes aujourd'hui :": "Complementary ready-to-use resources offered today:",
            "GRATUIT": "FREE",
            "Valeur :": "Value:",
            "BONUS #1 : 10 phrases pour désamorcer un conflit immédiatement": "BONUS #1: 10 phrases to defuse a conflict immediately",
            "Un ensemble de phrases simples, prêtes à utiliser dans les moments tendus pour calmer une discussion, éviter l'escalade et reprendre le contrôle émotionnel au bon moment.": "A set of simple, ready-to-use phrases for tense moments to calm a discussion, avoid escalation, and regain emotional control at the right moment.",
            "BONUS #2 : Les 12 erreurs qui détruisent un couple sans s'en rendre compte": "BONUS #2: The 12 mistakes that destroy a relationship without realizing it",
            "Découvre les comportements les plus courants qui fragilisent une relation (mauvaises réactions en dispute, paroles blessantes, distance). Chaque erreur est accompagnée de sa solution.": "Discover the most common behaviors that weaken a relationship (bad reactions during arguments, hurtful words, distance). Each mistake comes with its solution.",
            "TÉMOIGNAGES & RÉSULTATS": "TESTIMONIALS & RESULTS",
            "ILS ONT CHANGER L'AMBIANCE DE LEUR FOYER GRÂCE À CE PROGRAMME": "THEY CHANGED THE ATMOSPHERE OF THEIR HOME THANKS TO THIS PROGRAM",
            "Découvre les retours d'hommes qui ont appliqué la méthode :": "Discover feedback from men who applied the method:",
            "UNE DÉCISION QUI PEUT TOUT CHANGER": "A DECISION THAT CAN CHANGE EVERYTHING",
            "Dans quelques semaines, vous regarderez en arrière et vous verrez ce moment comme un point de bascule. Soit vous aurez saisi cette opportunité de transformer votre communication et de rétablir le respect, soit vous aurez continué comme avant, en laissant les tensions s'accumuler. La décision vous appartient maintenant.": "In a few weeks, you will look back and see this moment as a turning point. Either you took this opportunity to transform your communication and restore respect, or you continued as before, letting tensions pile up. The decision is now yours.",
            "FOIRE AUX QUESTIONS": "FREQUENTLY ASKED QUESTIONS",
            "VOS QUESTIONS LES PLUS FRÉQUENTES": "YOUR MOST FREQUENT QUESTIONS",
            "Tout ce que vous devez savoir avant de commencer :": "Everything you need to know before starting:",
            "À qui est destinée cette formation ?": "Who is this program for?",
            "Comment vais-je recevoir le programme ?": "How will I receive the program?",
            "Combien de temps faut-il pour voir des résultats ?": "How long does it take to see results?",
            "Et si le programme ne convient pas ?": "What if the program doesn't suit me?",
            "GARANTIE SATISFAIT OU REMBOURSÉ": "MONEY BACK GUARANTEE",
            "RECAPITULATIF DE VOTRE COMMANDE": "SUMMARY OF YOUR ORDER",
            "Le Guide Ultime \\"SAUVER TON COUPLE\\" (9 Chapitres)": "The Ultimate Guide \\"SAVE YOUR RELATIONSHIP\\" (9 Chapters)",
            "BONUS #1 : 10 phrases de désamorçage immédiat": "BONUS #1: 10 immediate defusing phrases",
            "BONUS #2 : Les 12 erreurs destructrices à éviter": "BONUS #2: 12 destructive errors to avoid",
            "Le Plan d'Action sur 30 Jours (Exercices quotidiens)": "The 30-Day Action Plan (Daily exercises)",
            "VALEUR TOTALE DU PACK :": "TOTAL PACK VALUE:",
            "OFFRE SPÉCIALE AUJOURD'HUI :": "SPECIAL OFFER TODAY:",
            "Tous droits réservés": "All rights reserved",
            "Conditions Générales": "Terms & Conditions",
            "Politique de Confidentialité": "Privacy Policy",
            "Mentions Légales": "Legal Notice"
        }};

        var i18nReverseMap = {{}};
        for (var key in i18nMap) {{
            i18nReverseMap[i18nMap[key]] = key;
        }}

        function applyDOMTranslation(targetLang) {{
            var dict = (targetLang === 'en') ? i18nMap : i18nReverseMap;
            
            function walk(node) {{
                if (node.nodeType === Node.TEXT_NODE) {{
                    var text = node.nodeValue.trim();
                    if (text && dict[text]) {{
                        node.nodeValue = node.nodeValue.replace(text, dict[text]);
                    }}
                }} else if (node.nodeType === Node.ELEMENT_NODE && node.tagName !== 'SCRIPT' && node.tagName !== 'STYLE' && node.tagName !== 'SELECT') {{
                    for (var i = 0; i < node.childNodes.length; i++) {{
                        walk(node.childNodes[i]);
                    }}
                }}
            }}
            walk(document.body);

            // Also update CTA button texts if applicable
            var ctaSpans = document.querySelectorAll('.btn-eloquence span');
            ctaSpans.forEach(function(span) {{
                if (targetLang === 'en') {{
                    span.innerHTML = span.innerHTML.replace('JE REJOINS "SAUVER TON COUPLE" MAINTENANT', 'I JOIN "SAVE YOUR RELATIONSHIP" NOW');
                    span.innerHTML = span.innerHTML.replace('JE PROFITE DE L\'OFFRE MAINTENANT', 'I TAKE ADVANTAGE OF THE OFFER NOW');
                }} else {{
                    span.innerHTML = span.innerHTML.replace('I JOIN "SAVE YOUR RELATIONSHIP" NOW', 'JE REJOINS "SAUVER TON COUPLE" MAINTENANT');
                    span.innerHTML = span.innerHTML.replace('I TAKE ADVANTAGE OF THE OFFER NOW', 'JE PROFITE DE L\'OFFRE MAINTENANT');
                }}
            }});
        }}

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
                localStorage.setItem('selected_lang', 'fr');
                resetToFrenchDefault();
                applyDOMTranslation('fr');
                location.reload();
                return;
            }}

            localStorage.setItem('selected_lang', langCode);

            if (langCode === 'en') {{
                applyDOMTranslation('en');
                setTranslateCookie('en');
                return;
            }}

            setTranslateCookie(langCode);

            var googleSelect = document.querySelector('.goog-te-combo');
            if (googleSelect) {{
                googleSelect.value = langCode;
                googleSelect.dispatchEvent(new Event('change'));
            }}
            
            setTimeout(function() {{
                location.reload();
            }}, 300);
        }}

        function syncLanguageDropdown() {{
            var savedLang = localStorage.getItem('selected_lang');
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
                if (activeLang === 'en') {{
                    applyDOMTranslation('en');
                }}
            }}
        }}

        document.addEventListener('DOMContentLoaded', syncLanguageDropdown);
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>"""

start_tag = "<!-- Google Translate Script with Robust Synchronization -->"
end_tag = '<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>'

start_pos = content.find(start_tag)
end_pos = content.find(end_tag)

if start_pos != -1 and end_pos != -1:
    end_pos += len(end_tag)
    content = content[:start_pos] + native_i18n_js + content[end_pos:]
    print("Successfully replaced JS block with native i18n engine.")
else:
    print("Could not find start/end tags. start:", start_pos, "end:", end_pos)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully saved build script.")
