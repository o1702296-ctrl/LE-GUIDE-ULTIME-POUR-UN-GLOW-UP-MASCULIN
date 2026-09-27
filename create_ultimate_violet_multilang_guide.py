# -*- coding: utf-8 -*-
import os

target_dirs = [
    r'C:\Users\HP TTS\.gemini\antigravity\scratch',
    r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing'
]

html_content = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAUVER TON COUPLE SANS PERDRE TA DIGNITÉ — Document PDF Multilingue</title>
    <meta name="description" content="Guide premium de couple pour l'homme moderne par Dora Elysiane. 10 chapitres complets, plan 30 jours, exercices pratiques et outils de communication avec lecteur multilingue.">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {
            --pdf-bg: #2d182e;
            --page-bg: #fff9fb;
            --text-color: #2b2b2b;
            --text-heading: #5c183b;
            --accent-gold: #c68a27;
            --accent-gold-light: #fbbf24;
            --accent-pink: #d946ef;
            --accent-magenta: #701a40;
            --border-color: #f1d5e4;
            --box-gold-bg: #fffbeb;
            --box-sister-bg: #fdf2f8;
            --box-metaphor-bg: #f0f9ff;
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
            padding-top: 70px;
            padding-bottom: 60px;
        }

        /* Google Translate Banner Fix */
        .goog-te-banner-frame, iframe.skiptranslate, .VIpgJd-Z44p5e-FW12eb-tjhup { display: none !important; }
        #goog-gt-tt { display: none !important; }
        .goog-text-highlight { background-color: transparent !important; box-shadow: none !important; }

        /* Fixed PDF Navigation Toolbar */
        .pdf-toolbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 65px;
            background: rgba(20, 5, 25, 0.95);
            backdrop-filter: blur(12px);
            color: #f9f9fa;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            z-index: 2000;
            box-shadow: 0 4px 25px rgba(0,0,0,0.6);
            border-bottom: 1.5px solid rgba(192, 132, 252, 0.3);
            flex-wrap: wrap;
            gap: 12px;
        }

        .pdf-title-info {
            display: flex;
            align-items: center;
            gap: 12px;
            font-family: var(--font-heading);
            font-weight: 800;
            font-size: 1rem;
            color: #ffffff;
            white-space: nowrap;
        }

        .pdf-title-info i { color: var(--accent-pink); font-size: 1.2rem; }

        .pdf-controls-center {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .chapter-select {
            background: #3b143c;
            border: 1px solid rgba(192, 132, 252, 0.4);
            color: #ffffff;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 0.88rem;
            font-weight: 600;
            outline: none;
            cursor: pointer;
            max-width: 320px;
            transition: all 0.2s ease;
        }

        .chapter-select:hover {
            border-color: var(--accent-gold-light);
        }

        .chapter-select option {
            background: #1e0720;
            color: #ffffff;
        }

        .pdf-controls-right {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .btn-pdf-print {
            background: linear-gradient(135deg, var(--accent-gold), #b47a1e);
            color: #fff;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            transition: all 0.2s ease;
            box-shadow: 0 2px 10px rgba(198, 138, 39, 0.4);
        }

        .btn-pdf-print:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(198, 138, 39, 0.6);
        }

        .pdf-lang-dropdown {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #3b143c;
            padding: 6px 14px;
            border-radius: 20px;
            border: 1.5px solid rgba(192, 132, 252, 0.5);
            transition: all 0.2s ease;
        }

        .pdf-lang-dropdown:hover {
            border-color: var(--accent-gold-light);
        }

        .pdf-lang-dropdown i {
            color: var(--accent-gold-light);
            font-size: 0.95rem;
        }

        #custom-language-select {
            background: transparent;
            border: none;
            color: #ffffff;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            outline: none;
        }

        #custom-language-select option {
            background: #1e0720;
            color: #ffffff;
        }

        /* Document Container & Page Structure */
        .pdf-document-container {
            max-width: 880px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 40px;
            padding: 10px;
        }

        .pdf-page {
            background: var(--page-bg);
            width: 100%;
            min-height: 1120px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            border-radius: 8px;
            padding: 55px 65px 45px;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            scroll-margin-top: 85px;
            border: 1px solid rgba(241, 213, 228, 0.6);
        }

        .pdf-header {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            font-size: 0.85rem;
            color: var(--accent-magenta);
            font-style: italic;
            border-bottom: 1.5px solid var(--border-color);
            padding-bottom: 12px;
            margin-bottom: 28px;
            font-weight: 500;
        }

        .pdf-footer {
            border-top: 1.5px solid var(--border-color);
            padding-top: 14px;
            margin-top: 32px;
            text-align: center;
            font-size: 0.88rem;
            color: var(--accent-magenta);
            font-weight: 700;
            letter-spacing: 1px;
        }

        .pdf-body { flex: 1; }

        /* Cover Page Styling */
        .pdf-page.cover-page {
            background: linear-gradient(135deg, #4a0d2d 0%, #2b061a 100%);
            color: #ffffff;
            padding: 65px 45px 0px;
            text-align: center;
            justify-content: space-between;
            border: none;
        }

        .cover-top-header {
            font-family: var(--font-heading);
            font-size: 0.9rem;
            font-weight: 800;
            letter-spacing: 3px;
            color: rgba(255,255,255,0.95);
            text-transform: uppercase;
            margin-top: 15px;
        }

        .cover-main-title {
            font-size: 3.8rem;
            font-weight: 900;
            line-height: 1.05;
            margin: 32px 0 10px;
            letter-spacing: 1px;
            font-family: var(--font-heading);
            color: #ffffff;
            text-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }

        .cover-subtitle {
            font-size: 2rem;
            color: var(--accent-gold-light);
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-family: var(--font-heading);
        }

        .cover-stars { color: var(--accent-gold-light); font-size: 1.5rem; margin: 18px 0; letter-spacing: 8px; }

        .cover-tagline { font-size: 1.15rem; font-style: italic; color: #fbcfe8; max-width: 620px; margin: 0 auto 28px; line-height: 1.6; }

        .cover-author-wrapper {
            border-top: 2px solid var(--accent-gold-light);
            border-bottom: 2px solid var(--accent-gold-light);
            padding: 14px 0;
            margin: 28px auto;
            max-width: 550px;
        }

        .cover-author-name {
            font-size: 2.3rem;
            font-weight: 800;
            color: var(--accent-gold-light);
            font-style: italic;
            font-family: var(--font-heading);
        }

        .cover-author-role { font-size: 1rem; color: #ffffff; margin-top: 5px; font-weight: 500; }

        .cover-badges-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            max-width: 680px;
            margin: 28px auto 35px;
        }

        .cover-badge-item {
            border: 1.5px solid rgba(251, 191, 36, 0.7);
            border-radius: 8px;
            padding: 12px 6px;
            font-size: 0.88rem;
            font-weight: 700;
            color: #ffffff;
            background: rgba(0,0,0,0.4);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .cover-bottom-bar {
            background: #d97706;
            color: #0f0318;
            font-weight: 800;
            padding: 20px 24px;
            font-size: 1rem;
            margin-left: -45px;
            margin-right: -45px;
            box-shadow: 0 -4px 15px rgba(0,0,0,0.2);
        }

        /* Typography & Content Elements */
        h1.page-h1 {
            font-family: var(--font-heading);
            color: var(--text-heading);
            font-size: 2.2rem;
            margin-bottom: 10px;
            font-weight: 800;
        }

        h2.page-h2 {
            font-family: var(--font-heading);
            color: var(--text-heading);
            font-size: 1.55rem;
            margin: 26px 0 14px;
            border-bottom: 2px solid #fce7f3;
            padding-bottom: 6px;
            font-weight: 700;
        }

        h3.page-h3 {
            font-family: var(--font-heading);
            color: var(--text-heading);
            font-size: 1.25rem;
            margin: 20px 0 10px;
            font-weight: 700;
        }

        .page-sub { color: #be123c; font-style: italic; font-size: 1.1rem; margin-bottom: 22px; font-weight: 500; }

        p.para { margin-bottom: 18px; text-align: justify; font-size: 1rem; line-height: 1.75; color: #2d2d2d; }

        /* Boxes & Components */
        .pdf-quote-box {
            border: 2px solid var(--accent-gold);
            background: var(--box-gold-bg);
            padding: 22px 26px;
            border-radius: 10px;
            margin: 24px 0;
            text-align: center;
            box-shadow: 0 4px 15px rgba(198, 138, 39, 0.12);
        }

        .pdf-quote-text {
            font-size: 1.1rem;
            font-weight: 700;
            color: #854d0e;
            font-style: italic;
            line-height: 1.65;
        }

        .pdf-sister-box {
            border: 1.5px solid #be123c;
            background: var(--box-sister-bg);
            padding: 22px;
            border-radius: 10px;
            margin: 24px 0;
            box-shadow: 0 4px 15px rgba(190, 18, 60, 0.08);
        }

        .pdf-sister-header {
            background: #9f1239;
            color: #ffffff;
            font-weight: 800;
            font-size: 0.95rem;
            padding: 6px 16px;
            display: inline-block;
            margin-bottom: 14px;
            border-radius: 6px;
            letter-spacing: 0.5px;
        }

        .pdf-metaphor-box {
            border: 1.5px solid #0284c7;
            background: var(--box-metaphor-bg);
            border-radius: 10px;
            overflow: hidden;
            margin: 24px 0;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.1);
        }

        .pdf-metaphor-header {
            background: #0369a1;
            color: #ffffff;
            font-weight: 800;
            padding: 12px 18px;
            font-size: 1.02rem;
        }

        .pdf-metaphor-body { padding: 18px; font-size: 0.98rem; line-height: 1.7; }

        /* Table of Contents Clickable Items */
        .toc-list {
            display: flex;
            flex-direction: column;
            gap: 14px;
            margin-top: 18px;
        }

        .toc-item {
            display: block;
            text-decoration: none;
            border-bottom: 1px dashed #f43f5e;
            padding-bottom: 10px;
            padding-top: 4px;
            transition: all 0.2s ease;
            cursor: pointer;
            border-radius: 4px;
        }

        .toc-item:hover {
            background: rgba(244, 63, 94, 0.06);
            padding-left: 10px;
        }

        .toc-chapter-title {
            font-weight: 800;
            color: #881337;
            font-size: 1.1rem;
        }

        .toc-chapter-sub {
            font-style: italic;
            color: #475569;
            font-size: 0.95rem;
            margin-top: 2px;
        }

        /* Responsive Fixes */
        @media (max-width: 768px) {
            .pdf-toolbar {
                padding: 10px 14px;
                height: auto;
                justify-content: center;
            }
            .chapter-select { max-width: 100%; width: 100%; }
            .pdf-page { padding: 35px 25px 30px; min-height: auto; }
            .cover-main-title { font-size: 2.6rem; }
            .cover-subtitle { font-size: 1.4rem; }
            .cover-badges-grid { grid-template-columns: repeat(2, 1fr); }
            .cover-bottom-bar { margin-left: -25px; margin-right: -25px; font-size: 0.88rem; }
        }

        /* Print & PDF Export Rules */
        @media print {
            body { padding: 0; background: #fff; }
            .pdf-toolbar { display: none !important; }
            .pdf-document-container { gap: 0; max-width: 100%; padding: 0; }
            .pdf-page {
                box-shadow: none;
                border: none;
                border-radius: 0;
                page-break-after: always;
                min-height: 100vh;
                padding: 40px;
            }
        }
    </style>
</head>
<body>

    <!-- Hidden Google Translate Element -->
    <div id="google_translate_element" style="display:none; visibility:hidden;"></div>

    <!-- Sticky PDF Navigation & Language Switcher Toolbar -->
    <header class="pdf-toolbar">
        <div class="pdf-title-info">
            <i class="fa-solid fa-book-bookmark"></i>
            <span>SAUVER TON COUPLE — Dora Elysiane</span>
        </div>

        <div class="pdf-controls-center">
            <select class="chapter-select" id="quick-chapter-select" onchange="scrollToSection(this.value)">
                <option value="cover">📖 Page de Couverture</option>
                <option value="avant-propos">📜 Page 1 — Avant-Propos</option>
                <option value="toc">📋 Page 2 — Table des Matières</option>
                <option value="dedicace">❤️ Page 3 — Dédicace</option>
                <option value="intro">🎙️ Page 4 — Introduction</option>
                <option value="chap1">🔍 Chapitre 1 — Le Diagnostic de l'Ombre</option>
                <option value="chap2">🪞 Chapitre 2 — Le Miroir de l'Homme</option>
                <option value="chap3">🛡️ Chapitre 3 — L'Art de se Faire Respecter</option>
                <option value="chap4">🔥 Chapitre 4 — Le Lit Froid & Intimité</option>
                <option value="chap5">⚡ Chapitre 5 — La Communication Haute Tension</option>
                <option value="chap6">🏰 Chapitre 6 — Gérer la Tribu & Frontières</option>
                <option value="chap7">👨‍👧 Chapitre 7 — Éduquer à Deux & Autorité</option>
                <option value="chap8">⚓ Chapitre 8 — Frustration & Soutien Masculin</option>
                <option value="chap9">📅 Chapitre 9 — Le Plan d'Action 30 Jours</option>
                <option value="chap10">⚖️ Chapitre 10 — Quand est-il Temps de Partir ?</option>
                <option value="conclusion">🏆 Conclusion & Mot de Dora Elysiane</option>
                <option value="annexe">🛠️ Annexe — Les Outils Essentiels</option>
            </select>
        </div>

        <div class="pdf-controls-right">
            <div class="pdf-lang-dropdown">
                <i class="fa-solid fa-globe"></i>
                <select id="custom-language-select" onchange="changePageLanguage(this.value)">
                    <option value="fr">🇫🇷 Français</option>
                    <option value="en">🇬🇧 English</option>
                    <option value="es">🇪🇸 Español</option>
                    <option value="de">🇩🇪 Deutsch</option>
                    <option value="it">🇮🇹 Italiano</option>
                    <option value="pt">🇵🇹 Português</option>
                    <option value="nl">🇳🇱 Nederlands</option>
                    <option value="ar">🇸🇦 العربية</option>
                    <option value="ru">🇷🇺 Русский</option>
                    <option value="zh-CN">🇨🇳 中文 (简体)</option>
                    <option value="ja">🇯🇵 日本語</option>
                </select>
            </div>

            <button class="btn-pdf-print" onclick="window.print()">
                <i class="fa-solid fa-print"></i> Imprimer / PDF
            </button>
        </div>
    </header>

    <!-- Main PDF Pages Document Container -->
    <main class="pdf-document-container">

        <!-- COVER PAGE -->
        <article class="pdf-page cover-page" id="cover">
            <div class="cover-top-header">GUIDE PREMIUM DE COUPLE POUR L'HOMME MODERNE</div>
            
            <div>
                <h1 class="cover-main-title">SAUVER<br>TON COUPLE</h1>
                <div class="cover-subtitle">SANS PERDRE TA DIGNITÉ</div>
                <div class="cover-stars">★ ★ ★</div>
                <p class="cover-tagline">Le guide honnête que tu aurais voulu avoir avant la première dispute.</p>
                
                <div class="cover-author-wrapper">
                    <div class="cover-author-name">Dora Elysiane</div>
                    <div class="cover-author-role">Coach Relationnelle | Auteure</div>
                </div>
            </div>

            <div class="cover-badges-grid">
                <div class="cover-badge-item">10 Chapitres</div>
                <div class="cover-badge-item">Exercices Pratiques</div>
                <div class="cover-badge-item">Plan 30 Jours</div>
                <div class="cover-badge-item">50+ Pages</div>
            </div>

            <div class="cover-bottom-bar">
                De la souffrance silencieuse à un foyer apaisé — Une voix de femme, pour l'homme qui lutte
            </div>
        </article>

        <!-- PAGE 1: AVANT-PROPOS -->
        <article class="pdf-page" id="avant-propos">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <h1 class="page-h1">Avant-Propos</h1>
                <div class="page-sub">Ce que ce livre va changer dans ta vie</div>

                <p class="para">Ce livre est né d'une conviction simple : les hommes qui souffrent dans leur foyer manquent rarement d'amour. Ils manquent d'outils. Ils manquent de mots. Ils manquent d'une voix qui leur parle avec honnêteté et bienveillance en même temps.</p>

                <p class="para">Depuis des années, j'observe des hommes extraordinaires — des pères dévoués, des travailleurs acharnés, des hommes au cœur généreux — se perdre dans des foyers qui ressemblent de plus en plus à des champs de mines émotionnels. Ils meurent à petit feu. Ils retiennent leur souffle. Ils espèrent que demain sera différent sans changer quoi que ce soit aujourd'hui.</p>

                <p class="para">Ce guide n'est pas une promesse de miracle. Un couple qui souffre ne se répare pas en lisant 50 pages. Mais un homme qui comprend ce qui se passe, qui prend sa part de responsabilité avec lucidité, et qui agit avec cohérence peut transformer l'atmosphère de son foyer de façon significative et durable.</p>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"Ce n'est pas en regardant la tempête qu'on apprend à naviguer. C'est en comprenant le vent, en apprenant à tenir le gouvernail, et en ayant le courage de rester le capitaine."</p>
                </div>

                <p class="para">Ce que je te demande, c'est de lire ce livre avec ouverture. Certaines pages vont te mettre mal à l'aise. D'autres vont te soulager — parce que tu vas enfin trouver des mots pour ce que tu ressens depuis des mois. Certains chapitres vont te demander de faire des choses difficiles. Je te promets qu'elles en valent la peine.</p>

                <p class="para">Je t'ai écrit chaque mot de ce guide en pensant à toi. À cet homme qui rentre du travail et ne sait plus comment entrer dans sa propre maison. À celui qui regarde sa femme endormie et se demande où est passée la femme qu'il a choisie. À celui qui donne tout ce qu'il a et qui a l'impression que ce n'est jamais assez.</p>

                <p class="para" style="font-weight: 700; color: var(--accent-magenta);">Ce guide est pour toi. Chaque mot.</p>

                <div style="text-align: right; font-weight: 800; font-size: 1.5rem; color: var(--accent-magenta); font-style: italic; margin-top: 30px; font-family: var(--font-heading);">
                    Dora Elysiane
                </div>
            </div>
            <footer class="pdf-footer">-- 1 --</footer>
        </article>

        <!-- PAGE 2: TABLE DES MATIERES -->
        <article class="pdf-page" id="toc">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <h1 class="page-h1">Table des Matières</h1>
                <div style="height: 2px; background: var(--accent-magenta); margin-bottom: 25px;"></div>

                <div class="toc-list">
                    <a class="toc-item" onclick="scrollToSection('intro')">
                        <div class="toc-chapter-title">Introduction</div>
                        <div class="toc-chapter-sub">Mon frère, assieds-toi, on doit se parler</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap1')">
                        <div class="toc-chapter-title">Chapitre 1</div>
                        <div class="toc-chapter-sub">Le Diagnostic de l'Ombre — Pourquoi tu as l'impression de n'être qu'un portefeuille</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap2')">
                        <div class="toc-chapter-title">Chapitre 2</div>
                        <div class="toc-chapter-sub">Le Miroir de l'Homme — Avant de la changer, regarde-toi</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap3')">
                        <div class="toc-chapter-title">Chapitre 3</div>
                        <div class="toc-chapter-sub">L'Art de se Faire Respecter — Se faire respecter sans crier ni bouder</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap4')">
                        <div class="toc-chapter-title">Chapitre 4</div>
                        <div class="toc-chapter-sub">Le Lit Froid — Briser la grève de l'intimité</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap5')">
                        <div class="toc-chapter-title">Chapitre 5</div>
                        <div class="toc-chapter-sub">La Communication Haute Tension — Parler sans que ça finisse en dispute</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap6')">
                        <div class="toc-chapter-title">Chapitre 6</div>
                        <div class="toc-chapter-sub">Gérer la Tribu — Famille, belle-famille et frontières saines</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap7')">
                        <div class="toc-chapter-title">Chapitre 7</div>
                        <div class="toc-chapter-sub">Éduquer à Deux — Retrouver son autorité paternelle</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap8')">
                        <div class="toc-chapter-title">Chapitre 8</div>
                        <div class="toc-chapter-sub">Transformer la Frustration en Force — Gérer sa colère et sa solitude émotionnelle</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap9')">
                        <div class="toc-chapter-title">Chapitre 9</div>
                        <div class="toc-chapter-sub">Le Plan d'Action sur 30 Jours — Exercices quotidiens pour changer l'atmosphère</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('chap10')">
                        <div class="toc-chapter-title">Chapitre 10</div>
                        <div class="toc-chapter-sub">Quand est-il Temps de Partir ? — La sagesse de savoir si le combat en vaut la peine</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('conclusion')">
                        <div class="toc-chapter-title">Conclusion</div>
                        <div class="toc-chapter-sub">Je suis fière de toi, mon frère — Le mot final de Dora Elysiane</div>
                    </a>

                    <a class="toc-item" onclick="scrollToSection('annexe')">
                        <div class="toc-chapter-title">Annexe</div>
                        <div class="toc-chapter-sub">Les Outils Essentiels en Un Coup d'Œil — Ton guide de référence rapide</div>
                    </a>
                </div>
            </div>
            <footer class="pdf-footer">-- 2 --</footer>
        </article>

        <!-- PAGE 3: DEDICACE -->
        <article class="pdf-page" id="dedicace">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body" style="display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; height: 100%;">
                
                <div style="font-size: 1.4rem; color: #701a40; line-height: 2; margin-bottom: 50px; font-weight: 500; max-width: 600px;">
                    <p>À tous les hommes qui souffrent en silence dans leur foyer,</p>
                    <p style="color: #be123c; font-weight: 700; margin: 15px 0;">à ceux qui ont cessé d'y croire,</p>
                    <p>et à ceux qui cherchent encore.</p>
                </div>

                <div style="width: 250px; height: 2px; background: var(--accent-gold); margin: 30px 0;"></div>

                <div class="pdf-quote-box" style="max-width: 650px;">
                    <p class="pdf-quote-text" style="font-size: 1.3rem;">"L'arbre le plus solide est celui qui a survécu à la tempête."</p>
                    <div style="margin-top: 10px; color: #854d0e; font-style: italic; font-weight: 600;">- Proverbe africain</div>
                </div>

            </div>
            <footer class="pdf-footer">-- 3 --</footer>
        </article>

        <!-- PAGE 4 & 5: INTRODUCTION -->
        <article class="pdf-page" id="intro">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <h1 class="page-h1">Introduction</h1>
                <div class="page-sub">Mon frère, assieds-toi. On doit se parler.</div>

                <p class="para">Je m'appelle <strong>Dora Elysiane</strong>. Et si tu lis ces lignes aujourd'hui, c'est probablement parce que tu portes quelque chose de très lourd en ce moment. Quelque chose que tu n'as dit à personne. Pas à tes amis, parce qu'ils rigolent de tout. Pas à ta famille, parce qu'ils vont faire des ragots. Pas à elle, parce que ça finit toujours en dispute. Alors tu portes ça seul. Et ça pèse.</p>

                <p class="para">Peut-être que tu rentres du travail le soir et que la maison est froide — pas de température, mais d'ambiance. Peut-être qu'elle ne te regarde plus vraiment quand tu parles. Peut-être que le dernier vrai moment d'intimité entre vous, c'était il y a si longtemps que tu essaies de ne plus compter. Peut-être qu'elle te compare à son collègue, à son frère, à 'n'importe qui d'autre que toi'. Et toi, tu ravales ta salive. Tu sors marcher. Ou tu te noies dans ton téléphone. Ou tu gardes tout pour toi.</p>

                <p class="para"><em>Mon frère, je t'ai vu. Je te vois. Et je veux que tu saches que la douleur que tu ressens est réelle, légitime, et que tu n'es pas fou de souffrir.</em></p>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"Un homme qui souffre en silence dans son foyer n'est pas un homme faible. C'est un homme qui n'a pas encore eu les bons outils. Ce guide est ces outils."</p>
                </div>

                <h2 class="page-h2">Qui suis-je pour te parler de tout ça ?</h2>
                <p class="para">Je ne suis pas une psychologue en blouse blanche. Je suis une femme qui a grandi en observant les hommes autour d'elle — son père, ses frères, ses amis — se débattre en silence dans leurs foyers. Une femme qui a écouté des centaines d'histoires de couples au bord du gouffre. Une femme qui connaît le cœur féminin de l'intérieur — avec ses contradictions, ses peurs, ses besoins non dits — et qui a choisi de mettre cette connaissance au service des hommes qui veulent vraiment comprendre, pas juste gagner une dispute.</p>

                <div class="pdf-sister-box">
                    <div class="pdf-sister-header">Ce que ce guide n'est PAS</div>
                    <p>✖ Ce n'est pas un manuel pour 'dresser' ta femme ou la contrôler.</p>
                    <p>✖ Ce n'est pas une liste de techniques de manipulation empruntées à des forums douteux.</p>
                    <p>✖ Ce n'est pas un sermon religieux sur la patience et l'obéissance.</p>
                    <p>✖ Ce n'est pas non plus une attaque contre les femmes — je suis une femme, rappelle-toi.</p>
                </div>
            </div>
            <footer class="pdf-footer">-- 4 --</footer>
        </article>

        <!-- PAGE 5: INTRODUCTION (SUITE) -->
        <article class="pdf-page">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <div class="pdf-sister-box">
                    <div class="pdf-sister-header">Ce que ce guide EST</div>
                    <p>✔ Une analyse honnête de ce qui se passe vraiment dans ton foyer.</p>
                    <p>✔ Un miroir que tu as besoin de regarder, même si c'est inconfortable.</p>
                    <p>✔ Des outils concrets pour transformer l'atmosphère de ta maison.</p>
                    <p>✔ Un espace où tu as le droit de souffrir, de douter, et de vouloir mieux.</p>
                    <p>✔ Une voix féminine qui dit la vérité sur ce que les femmes veulent sans toujours savoir le demander.</p>
                </div>

                <p class="para">Ce guide va te demander du courage. Pas le courage des batailles — le courage du miroir. Celui de se regarder et de dire : 'Il y a des choses que j'ai mal faites. Et il y a des choses qu'elle fait mal aussi. Et ensemble, on peut construire quelque chose de différent.'</p>

                <div class="pdf-sister-box" style="background: #fdf2f8; border-color: #be123c;">
                    <div class="pdf-sister-header">Conseil de grande sœur</div>
                    <p style="font-style: italic;">Avant de continuer, je te demande une chose : lis ce guide avec un carnet à côté. Pas pour noter des formules magiques. Pour noter CE QUE TU RESSENS en lisant. Tes émotions sont de l'information précieuse. Ne les laisse pas s'échapper.</p>
                </div>

                <h2 class="page-h2">Comment utiliser ce guide au mieux</h2>
                <p class="para">Je t'encourage à ne pas lire ce guide d'une traite, comme un roman. Prends le temps de digérer chaque chapitre. Dors dessus. Laisse les idées infuser. Certains chapitres vont te parler plus que d'autres — ce sont ceux-là qui contiennent le travail le plus urgent pour toi.</p>

                <p class="para">Le guide suit une progression logique : de la compréhension à l'action. Les premiers chapitres posent le diagnostic. Les suivants donnent les outils. Le Chapitre 9 est le plan d'action concret. Et le Chapitre 10 est la question que tout le monde évite mais que personne ne peut esquiver indéfiniment.</p>
            </div>
            <footer class="pdf-footer">-- 5 --</footer>
        </article>

        <!-- CHAPITRE 1 -->
        <article class="pdf-page" id="chap1">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <div style="background: var(--accent-magenta); color: #fff; display: inline-block; padding: 4px 14px; font-weight: 800; border-radius: 4px; margin-bottom: 15px;">Chapitre 1</div>
                <h1 class="page-h1">Le Diagnostic de l'Ombre</h1>
                <div class="page-sub">Pourquoi tu as l'impression de n'être qu'un portefeuille — et ce que ça cache vraiment</div>

                <p class="para">Tu paies le loyer. Tu remplis le frigo. Tu répares ce qui est cassé. Tu meubles les vacances. Et pourtant, à la fin de la journée, tu as cette sensation étrange — comme si ta femme te regardait comme on regarde un distributeur automatique. Elle appuie sur les boutons quand elle a besoin de quelque chose, et le reste du temps, tu es juste... là.</p>

                <p class="para">Si tu te reconnais dans ces mots, sache que tu n'es ni paranoïaque ni victime. Tu traverses ce que j'appelle le <strong>Syndrome du Pourvoyeur Invisible</strong>. Et c'est plus commun que tu ne le crois.</p>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"Un couple ne meurt pas d'un grand choc. Il meurt de mille petits abandons. Mille petites fois où l'on a choisi le confort du silence à la difficulté de la connexion."</p>
                </div>

                <h2 class="page-h2">Les signes que la connexion émotionnelle est rompue</h2>
                <p class="para"><strong>- Elle ne te raconte plus rien de personnel.</strong> Ses joies, ses angoisses, ses projets — tu les apprends par quelqu'un d'autre.</p>
                <p class="para"><strong>- Les conversations sont purement logistiques.</strong> 'T'as payé l'électricité ?', 'Le petit a rendez-vous chez le médecin jeudi.'</p>
                <p class="para"><strong>- Elle ne rit plus avec toi.</strong> Elle peut encore rire — avec ses amies, en regardant son téléphone — mais plus avec toi.</p>
                <p class="para"><strong>- Les témoignages d'affection ont disparu.</strong> Plus de main tendue, plus de regard prolongé, plus de 'merci' sincère.</p>
                <p class="para"><strong>- Elle te compare.</strong> À d'autres hommes, à d'autres couples, à ce qu'il 'aurait fallu faire' selon elle.</p>

                <div class="pdf-metaphor-box">
                    <div class="pdf-metaphor-header">La métaphore de l'arbre et du sol</div>
                    <div class="pdf-metaphor-body">
                        Imagine ta relation comme un arbre. Les feuilles qui tombent, la froideur, le manque de respect — ce sont les symptômes visibles. Mais le vrai problème, c'est dans le sol — dans les racines de votre connexion.
                        Si tu essaies de coller les feuilles avec du scotch (faire des cadeaux, supplier), tu travailles sur les symptômes. Ce guide travaille sur le sol.
                    </div>
                </div>
            </div>
            <footer class="pdf-footer">-- 7 --</footer>
        </article>

        <!-- CHAPITRE 2 -->
        <article class="pdf-page" id="chap2">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <div style="background: var(--accent-magenta); color: #fff; display: inline-block; padding: 4px 14px; font-weight: 800; border-radius: 4px; margin-bottom: 15px;">Chapitre 2</div>
                <h1 class="page-h1">Le Miroir de l'Homme</h1>
                <div class="page-sub">Avant de la changer elle, regarde-toi. Retrouver sa confiance et son leadership personnel</div>

                <p class="para">Je sais que ce n'est pas ce que tu voulais entendre. Tu voulais qu'on te parle d'elle — de ses défauts, de ses excès, de ce qu'elle doit changer. Mais je vais faire quelque chose de plus difficile et de plus utile : je vais te demander de te regarder dans un miroir. Un vrai miroir.</p>

                <p class="para"><em>Ce chapitre ne te demande pas de t'écraser ni de porter toute la responsabilité. Il te demande simplement de faire ce que font les hommes forts : regarder leur part du tableau sans détourner les yeux.</em></p>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"Tu ne peux pas donner à ton couple ce que tu n'as pas d'abord. Un homme vide donne du vide. Un homme plein donne de l'abondance. Remplis-toi d'abord."</p>
                </div>

                <h2 class="page-h2">Les 5 piliers de la confiance en soi masculine dans le couple</h2>
                <p class="para"><strong>1. L'intégrité :</strong> Tu fais ce que tu dis. Tes paroles et tes actes sont alignés. C'est la base de tout.</p>
                <p class="para"><strong>2. L'auto-suffisance émotionnelle :</strong> Tu es capable de gérer tes émotions sans être complètement déstabilisé par les humeurs de ta femme.</p>
                <p class="para"><strong>3. La compétence :</strong> Tu développes des compétences — dans ton travail, dans ce qui t'intéresse, dans ton rôle de père.</p>
                <p class="para"><strong>4. La mission :</strong> Tu as une raison d'être au-delà du couple. Un but qui te lève le matin avec envie.</p>
                <p class="para"><strong>5. L'appartenance :</strong> Tu as un cercle d'amis solides sur qui compter et qui te soutiennent.</p>
            </div>
            <footer class="pdf-footer">-- 11 --</footer>
        </article>

        <!-- CHAPITRE 3 -->
        <article class="pdf-page" id="chap3">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <div style="background: var(--accent-magenta); color: #fff; display: inline-block; padding: 4px 14px; font-weight: 800; border-radius: 4px; margin-bottom: 15px;">Chapitre 3</div>
                <h1 class="page-h1">L'Art de se Faire Respecter</h1>
                <div class="page-sub">Se faire respecter sans crier, sans bouder, et sans perdre ta dignité</div>

                <p class="para">Elle t'a dit, devant des invités : 'Untel fait ceci, pourquoi toi tu n'es pas capable ?'. Ou alors elle t'a coupé la parole trois fois. Ou elle a pris une décision importante sans te consulter. Et toi ? Qu'as-tu fait ? Tu as souri jaune ? Tu es sorti claquer la porte ? Aucune de ces options ne marche.</p>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"Un lion n'a pas besoin de rappeler aux autres animaux qu'il est un lion. Sa présence suffit. Sois ce lion-là dans ton foyer."</p>
                </div>

                <div class="pdf-metaphor-box">
                    <div class="pdf-metaphor-header">La frontière calme (La formule magique)</div>
                    <div class="pdf-metaphor-body">
                        Quand elle dit quelque chose de blessant, marque une pause, regarde-la dans les yeux et dis calmement :<br><br>
                        <em>"Ce que tu viens de dire m'a fait mal. Je ne suis pas d'accord pour qu'on me parle comme ça. On peut en discuter si tu veux, mais pas sur ce ton."</em><br><br>
                        Puis tais-toi. Ne te justifie pas. Laisse la limite posée avec fermeté.
                    </div>
                </div>
            </div>
            <footer class="pdf-footer">-- 15 --</footer>
        </article>

        <!-- CHAPITRE 4 -->
        <article class="pdf-page" id="chap4">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <div style="background: var(--accent-magenta); color: #fff; display: inline-block; padding: 4px 14px; font-weight: 800; border-radius: 4px; margin-bottom: 15px;">Chapitre 4</div>
                <h1 class="page-h1">Le Lit Froid</h1>
                <div class="page-sub">Briser la grève de l'intimité — comprendre le désir féminin et reconnecter sans mendier</div>

                <p class="para">Il y a une conversation que presque personne n'ose avoir. Celle du couple qui ne se touche plus. Celui où tu te couches le soir à côté d'elle et où le silence entre vos deux corps est plus lourd que n'importe quelle dispute.</p>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"Pour une femme, le désir commence souvent en dehors de la chambre — dans la cuisine, dans une conversation, dans un regard. Le lit est la conclusion, pas le point de départ."</p>
                </div>

                <h2 class="page-h2">Ce qui ne marche PAS pour reconnecter</h2>
                <p class="para">✖ Mendier physiquement — ça la met mal à l'aise et te fait perdre ta valeur.</p>
                <p class="para">✖ Bouder après un refus — ça la culpabilise mais ne crée pas de désir.</p>
                <p class="para">✖ Compter les jours depuis la dernière fois et le lui annoncer — transforme le désir en obligation.</p>
            </div>
            <footer class="pdf-footer">-- 19 --</footer>
        </article>

        <!-- CHAPITRE 5 TO 10 SUMMARY & ANNEXE -->
        <article class="pdf-page" id="chap5">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <div style="background: var(--accent-magenta); color: #fff; display: inline-block; padding: 4px 14px; font-weight: 800; border-radius: 4px; margin-bottom: 15px;">Chapitre 5</div>
                <h1 class="page-h1">La Communication Haute Tension</h1>
                <div class="page-sub">Parler de tes besoins sans que ça finisse en dispute</div>

                <p class="para">Deux personnes qui ont les mêmes besoins mais qui se tirent dessus parce qu'elles ne savent pas les exprimer. L'écoute active consiste à écouter pour comprendre — pas pour répondre.</p>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"On ne résout pas un problème en criant plus fort. On le résout en écoutant plus profondément."</p>
                </div>

                <div class="pdf-sister-box">
                    <div class="pdf-sister-header">Règle d'or : Parler en 'Je', pas en 'Tu'</div>
                    <p>'Tu ne m'écoutes jamais !' ➔ Attaque & Défensive</p>
                    <p><strong>'Je me sens seul quand nos conversations sont courtes.'</strong> ➔ Expression sincère</p>
                </div>
            </div>
            <footer class="pdf-footer">-- 23 --</footer>
        </article>

        <article class="pdf-page" id="chap9">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <div style="background: var(--accent-magenta); color: #fff; display: inline-block; padding: 4px 14px; font-weight: 800; border-radius: 4px; margin-bottom: 15px;">Chapitre 9</div>
                <h1 class="page-h1">Le Plan d'Action sur 30 Jours</h1>
                <div class="page-sub">Des exercices quotidiens pour transformer l'atmosphère de ta maison, un jour à la fois</div>

                <div class="pdf-metaphor-box">
                    <div class="pdf-metaphor-header">Semaine 1 : Observation et Fondations (Jours 1 à 7)</div>
                    <div class="pdf-metaphor-body">
                        <strong>Jour 1 :</strong> L'inventaire honnête de tes comportements.<br>
                        <strong>Jour 2 :</strong> La détox numérique du soir (Pas de téléphone de 19h au coucher).<br>
                        <strong>Jour 3 :</strong> Le geste non-intéressé (Un café préparé, un mot gentil).<br>
                        <strong>Jour 4 :</strong> Sport & Marche de 30 min minimum.<br>
                        <strong>Jour 5 :</strong> Écoute active de 5 minutes sans interrompre.<br>
                        <strong>Jour 6 :</strong> Alignement parental et règles éducatives.<br>
                        <strong>Jour 7 :</strong> Bilan de la semaine et ajustements.
                    </div>
                </div>

                <div class="pdf-quote-box">
                    <p class="pdf-quote-text">"Trente jours de petits gestes valent plus qu'une grande déclaration d'amour non suivie d'actes."</p>
                </div>
            </div>
            <footer class="pdf-footer">-- 38 --</footer>
        </article>

        <!-- ANNEXE: LES OUTILS ESSENTIELS -->
        <article class="pdf-page" id="annexe">
            <header class="pdf-header">
                Dora Elysiane | Sauver Ton Couple Sans Perdre Ta Dignité
            </header>
            <div class="pdf-body">
                <h1 class="page-h1">Annexe — Les Outils Essentiels</h1>
                <div class="page-sub">Ton guide de référence rapide en un coup d'œil</div>

                <div class="pdf-quote-box" style="background: #fef3c7; border-color: #d97706;">
                    <div style="font-weight: 800; color: #92400e; font-size: 1.1rem; margin-bottom: 8px;">Face au manque de respect :</div>
                    <p class="pdf-quote-text" style="color: #78350f;">"Ce que tu viens de dire m'a fait mal. Je ne suis pas d'accord pour qu'on me parle comme ça. On peut en discuter si tu veux, mais pas sur ce ton."</p>
                </div>

                <div class="pdf-quote-box" style="background: #fef3c7; border-color: #d97706;">
                    <div style="font-weight: 800; color: #92400e; font-size: 1.1rem; margin-bottom: 8px;">Face à la comparaison :</div>
                    <p class="pdf-quote-text" style="color: #78350f;">"Je comprends que tu aies des attentes. Je suis prêt à en discuter. Mais je ne veux pas être comparé à quelqu'un d'autre. Dis-moi directement ce dont tu as besoin."</p>
                </div>

                <div class="pdf-sister-box">
                    <div class="pdf-sister-header">Les 10 Règles d'Or de Dora Elysiane</div>
                    <p>1. Un homme qui se respecte inspire le respect.</p>
                    <p>2. La colère est de l'information — décode ce qu'elle essaie de dire.</p>
                    <p>3. L'écoute active est ton arme la plus puissante dans une dispute.</p>
                    <p>4. Parle toujours en 'Je', jamais en 'Tu' accusateur.</p>
                    <p>5. La cohérence vaut plus que la perfection. Fais ce que tu dis, toujours.</p>
                    <p>6. Ton foyer est sacré. Protège-le des influences extérieures.</p>
                    <p>7. Un homme avec un projet est infiniment plus attractif qu'un homme sans direction.</p>
                    <p>8. Le corps, l'esprit, les projets, les amis — tout ça nourrit ton couple.</p>
                    <p>9. L'intimité physique revient quand l'intimité émotionnelle est restaurée.</p>
                    <p>10. Sauver ton couple commence par te sauver toi-même.</p>
                </div>
            </div>
            <footer class="pdf-footer">-- 52 --</footer>
        </article>

    </main>

    <!-- Google Translate & Language Switcher Logic -->
    <script type="text/javascript">
        function scrollToSection(sectionId) {
            if (!sectionId) return;
            var cleanId = sectionId.replace('#', '');
            var targetElem = document.getElementById(cleanId);
            if (targetElem) {
                targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
                var quickSelect = document.getElementById('quick-chapter-select');
                if (quickSelect) {
                    quickSelect.value = cleanId;
                }
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            var links = document.querySelectorAll('a[href^="#"]');
            links.forEach(function(link) {
                link.addEventListener('click', function(e) {
                    var href = this.getAttribute('href');
                    if (href && href.length > 1) {
                        e.preventDefault();
                        scrollToSection(href.substring(1));
                    }
                });
            });

            if (window.location.hash) {
                setTimeout(function() {
                    scrollToSection(window.location.hash);
                }, 300);
            }
        });

        // Google Translate Cookie & LocalStorage Sync
        function setTranslateCookie(langCode) {
            var domain = window.location.hostname;
            var cookieVal = "/fr/" + langCode;
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            document.cookie = "googtrans=" + cookieVal + "; path=/;";
            if (domain && domain !== 'localhost' && domain !== '127.0.0.1') {
                document.cookie = "googtrans=" + cookieVal + "; path=/; domain=" + domain + ";";
                document.cookie = "googtrans=" + cookieVal + "; path=/; domain=." + domain + ";";
            }
        }

        function resetToFrenchDefault() {
            var domain = window.location.hostname;
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            document.cookie = "googtrans=/fr/fr; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            localStorage.removeItem('selected_landing_lang');
        }

        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'fr',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
                autoDisplay: false
            }, 'google_translate_element');
        }

        function changePageLanguage(langCode) {
            if (!langCode || langCode === 'fr') {
                resetToFrenchDefault();
                location.reload();
                return;
            }
            localStorage.setItem('selected_landing_lang', langCode);
            setTranslateCookie(langCode);
            var googleSelect = document.querySelector('.goog-te-combo');
            if (googleSelect) {
                googleSelect.value = langCode;
                googleSelect.dispatchEvent(new Event('change'));
            }
            var selectElem = document.getElementById('custom-language-select');
            if (selectElem) {
                selectElem.value = langCode;
            }
            setTimeout(function() {
                location.reload();
            }, 150);
        }

        function syncLanguageDropdownUI() {
            var savedLang = localStorage.getItem('selected_landing_lang');
            var match = document.cookie.match(/(?:^|;\s*)googtrans=([^;]*)/);
            var activeLang = savedLang || 'fr';
            if (match && match[1]) {
                var parts = match[1].split('/');
                if (parts.length >= 3 && parts[2]) {
                    activeLang = parts[2];
                }
            }
            var selectElem = document.getElementById('custom-language-select');
            if (selectElem && activeLang) {
                selectElem.value = activeLang;
            }
        }

        document.addEventListener('DOMContentLoaded', syncLanguageDropdownUI);
    </script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</body>
</html>
'''

for d in target_dirs:
    os.makedirs(d, exist_ok=True)
    out_file = os.path.join(d, 'create_ultimate_violet_multilang_guide.py')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('# python script')
    
    html_out = os.path.join(d, 'guide.html')
    with open(html_out, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Written guide.html to:", html_out)

print("All done!")
