# -*- coding: utf-8 -*-
import os

html_head = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAUVER TON COUPLE SANS PERDRE TA DIGNITÉ — Document PDF — Lina Rela</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        :root {
            --pdf-bg: #525659;
            --page-bg: #ffffff;
            --text-color: #2b2b2b;
            --text-heading: #5c183b;
            --accent-gold: #c68a27;
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
        html { background-color: var(--pdf-bg); font-family: var(--font-main); color: var(--text-color); line-height: 1.6; }
        body { top: 0px !important; position: static !important; padding-top: 65px; padding-bottom: 40px; }
        .goog-te-banner-frame, iframe.skiptranslate, .VIpgJd-Z44p5e-FW12eb-tjhup { display: none !important; }
        #goog-gt-tt { display: none !important; }
        .goog-text-highlight { background-color: transparent !important; box-shadow: none !important; }
        .pdf-toolbar { position: fixed; top: 0; left: 0; right: 0; height: 56px; background: #2a2a2e; color: #f9f9fa; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; z-index: 2000; box-shadow: 0 2px 12px rgba(0,0,0,0.4); border-bottom: 1px solid #444; }
        .pdf-title-info { display: flex; align-items: center; gap: 12px; font-family: var(--font-heading); font-weight: 700; font-size: 0.95rem; }
        .pdf-title-info i { color: var(--accent-pink); }
        .pdf-controls-right { display: flex; align-items: center; gap: 16px; }
        .btn-pdf-print { background: linear-gradient(135deg, var(--accent-gold), #b47a1e); color: #fff; border: none; padding: 8px 16px; border-radius: 6px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; font-size: 0.85rem; }
        .pdf-lang-dropdown { display: inline-flex; align-items: center; gap: 8px; background: #1e1e22; padding: 6px 14px; border-radius: 20px; border: 1px solid #555; }
        #custom-language-select { background: transparent; border: none; color: #ffffff; font-size: 0.85rem; font-weight: 600; cursor: pointer; outline: none; }
        #custom-language-select option { background: #2a2a2e; color: #ffffff; }
        .pdf-document-container { max-width: 820px; margin: 0 auto; display: flex; flex-direction: column; gap: 30px; }
        .pdf-page { background: var(--page-bg); width: 100%; min-height: 1120px; box-shadow: 0 12px 35px rgba(0,0,0,0.3); border-radius: 4px; padding: 50px 60px 40px; position: relative; display: flex; flex-direction: column; justify-content: space-between; }
        .pdf-header { display: flex; align-items: center; justify-content: flex-end; font-size: 0.85rem; color: var(--accent-magenta); font-style: italic; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; margin-bottom: 30px; }
        .pdf-footer { border-top: 1px solid var(--border-color); padding-top: 12px; margin-top: 30px; text-align: center; font-size: 0.85rem; color: var(--accent-magenta); font-weight: 600; }
        .pdf-body { flex: 1; }
        .pdf-page.cover-page { background: linear-gradient(135deg, #4a0d2d 0%, #2b061a 100%); color: #ffffff; padding: 60px 40px 0px; text-align: center; justify-content: space-between; }
        .cover-top-header { font-family: var(--font-heading); font-size: 0.85rem; font-weight: 700; letter-spacing: 2.5px; color: rgba(255,255,255,0.9); text-transform: uppercase; margin-top: 20px; }
        .cover-main-title { font-size: 3.8rem; font-weight: 900; line-height: 1; margin: 35px 0 10px; letter-spacing: 1px; font-family: var(--font-heading); }
        .cover-subtitle { font-size: 2rem; color: #fbbf24; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; font-family: var(--font-heading); }
        .cover-stars { color: #fbbf24; font-size: 1.4rem; margin: 15px 0; letter-spacing: 6px; }
        .cover-tagline { font-size: 1.1rem; font-style: italic; color: #fbcfe8; max-width: 600px; margin: 0 auto 30px; }
        .cover-author-wrapper { border-top: 2px solid #fbbf24; border-bottom: 2px solid #fbbf24; padding: 12px 0; margin: 25px auto; max-width: 500px; }
        .cover-author-name { font-size: 2.2rem; font-weight: 800; color: #fbbf24; font-style: italic; font-family: var(--font-heading); }
        .cover-author-role { font-size: 0.95rem; color: #ffffff; margin-top: 4px; }
        .cover-badges-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; max-width: 650px; margin: 25px auto 35px; }
        .cover-badge-item { border: 1.5px solid rgba(251, 191, 36, 0.6); border-radius: 8px; padding: 10px 4px; font-size: 0.8rem; font-weight: 700; color: #ffffff; background: rgba(0,0,0,0.3); }
        .cover-bottom-bar { background: #d97706; color: #0f0318; font-weight: 800; padding: 18px 20px; font-size: 0.95rem; margin-left: -40px; margin-right: -40px; }
        h1.page-h1 { font-family: var(--font-heading); color: var(--text-heading); font-size: 2.2rem; margin-bottom: 8px; }
        h2.page-h2 { font-family: var(--font-heading); color: var(--text-heading); font-size: 1.6rem; margin: 25px 0 12px; }
        h3.page-h3 { font-family: var(--font-heading); color: var(--text-heading); font-size: 1.25rem; margin: 18px 0 8px; }
        .page-sub { color: #be123c; font-style: italic; font-size: 1.1rem; margin-bottom: 20px; }
        p.para { margin-bottom: 16px; text-align: justify; font-size: 1rem; line-height: 1.7; }
        .pdf-quote-box { border: 1.5px solid var(--accent-gold); background: var(--box-gold-bg); padding: 20px 24px; border-radius: 8px; margin: 25px 0; text-align: center; }
        .pdf-quote-text { font-size: 1.1rem; font-weight: 700; color: #854d0e; font-style: italic; line-height: 1.6; }
        .pdf-sister-box { border: 1.5px solid #be123c; background: var(--box-sister-bg); padding: 20px; border-radius: 8px; margin: 25px 0; }
        .pdf-sister-header { background: #9f1239; color: #ffffff; font-weight: 800; font-size: 0.95rem; padding: 6px 14px; display: inline-block; margin-bottom: 12px; border-radius: 4px; }
        .pdf-metaphor-box { border: 1.5px solid #0284c7; background: var(--box-metaphor-bg); border-radius: 8px; overflow: hidden; margin: 25px 0; }
        .pdf-metaphor-header { background: #0369a1; color: #ffffff; font-weight: 800; padding: 10px 16px; font-size: 1rem; }
        .pdf-metaphor-body { padding: 16px; font-size: 0.95rem; line-height: 1.65; }
        .toc-list { display: flex; flex-direction: column; gap: 14px; margin-top: 20px; }
        .toc-item { border-bottom: 1px dashed #f43f5e; padding-bottom: 8px; }
        .toc-title { font-weight: 800; color: var(--text-heading); font-size: 1.1rem; }
        .toc-desc { font-style: italic; color: #666; font-size: 0.95rem; margin-top: 2px; }
        .checklist { list-style: none; margin: 16px 0; }
        .checklist li { position: relative; padding-left: 28px; margin-bottom: 10px; font-size: 0.98rem; }
        .checklist li::before { content: "✓"; position: absolute; left: 0; color: #be123c; font-weight: 900; font-size: 1.1rem; }
        .checklist-cross li::before { content: "✗"; color: #dc2626; }
        @media print {
            body { padding-top: 0; background: #fff; }
            .pdf-toolbar { display: none !important; }
            .pdf-page { box-shadow: none; border-radius: 0; page-break-after: always; min-height: 100vh; }
        }
    </style>
</head>
<body>
    <div class="pdf-toolbar">
        <div class="pdf-title-info">
            <i class="fa-solid fa-file-pdf"></i> SAUVER TON COUPLE SANS PERDRE TA DIGNITÉ — Document PDF Visuel (Lina Rela)
        </div>
        <div class="pdf-controls-right">
            <div class="pdf-lang-dropdown">
                <i class="fa-solid fa-globe" style="color: var(--accent-pink);"></i>
                <select id="custom-language-select" onchange="changePageLanguage(this.value)">
                    <option value="fr">🇫🇷 Français</option>
                    <option value="en">🇬🇧 English</option>
                    <option value="es">🇪🇸 Español</option>
                    <option value="de">🇩🇪 Deutsch</option>
                    <option value="it">🇮🇹 Italiano</option>
                    <option value="pt">🇵🇹 Português</option>
                    <option value="nl">🇳🇱 Nederlands</option>
                    <option value="ar">🇸🇦 العربية</option>
                </select>
            </div>
            <button onclick="window.print()" class="btn-pdf-print">
                <i class="fa-solid fa-print"></i> Imprimer / Sauvegarder PDF
            </button>
        </div>
    </div>
    <div id="google_translate_element" style="display:none!important;"></div>
    <div class="pdf-document-container">
"""

html_pages = """
        <!-- PAGE 1: COVER PAGE -->
        <div class="pdf-page cover-page" id="page-1">
            <div class="cover-top-header">GUIDE PREMIUM DE COUPLE POUR L'HOMME MODERNE</div>
            <div>
                <h1 class="cover-main-title">SAUVER<br>TON COUPLE</h1>
                <div class="cover-subtitle">SANS PERDRE TA DIGNITÉ</div>
                <div class="cover-stars">★ ★ ★</div>
                <p class="cover-tagline">Le guide honnête que tu aurais voulu avoir avant la première dispute.</p>
                <div style="color: #f43f5e; font-size: 1.2rem; margin-bottom: 10px;">♥ ♥ ♥</div>
                <div class="cover-author-wrapper">
                    <div class="cover-author-name">Lina Rela</div>
                    <div class="cover-author-role">Coach Relationnelle | Auteure</div>
                </div>
                <div class="cover-badges-grid">
                    <div class="cover-badge-item">10 Chapitres</div>
                    <div class="cover-badge-item">Exercices Pratiques</div>
                    <div class="cover-badge-item">Plan 30 jours</div>
                    <div class="cover-badge-item">50 Pages</div>
                </div>
            </div>
            <div class="cover-bottom-bar">
                De la souffrance silencieuse à un foyer apaisé - Une voix de femme, pour l'homme qui lutte
            </div>
        </div>

        <!-- PAGE 2: AVANT-PROPOS -->
        <div class="pdf-page" id="page-2">
            <div>
                <div class="pdf-header">Lina Rela | Sauver Ton Couple Sans Perdre Ta Dignité</div>
                <div class="pdf-body">
                    <h1 class="page-h1">Avant-Propos</h1>
                    <div class="page-sub">Ce que ce livre va changer dans ta vie</div>
                    <p class="para">Ce livre est né d'une conviction simple : les hommes qui souffrent dans leur foyer manquent rarement d'amour. Ils manquent d'outils. Ils manquent de mots. Ils manquent d'une voix qui leur parle avec honnêteté et bienveillance en même temps.</p>
                    <p class="para">Depuis des années, j'observe des hommes extraordinaires - des pères dévoués, des travailleurs acharnés, des hommes au cœur généreux - se perdre dans des foyers qui ressemblent de plus en plus à des champs de mines émotionnels. Ils marchent sur des œufs. Ils retiennent leur souffle. Ils espèrent que demain sera différent sans changer quoi que ce soit aujourd'hui.</p>
                    <p class="para">Ce guide n'est pas une promesse de miracle. Un couple qui souffre ne se répare pas en lisant 50 pages. Mais un homme qui comprend ce qui se passe, qui prend sa part de responsabilité avec lucidité, et qui agit avec cohérence peut transformer l'atmosphère de son foyer de façon significative et durable.</p>
                    <div class="pdf-quote-box">
                        <p class="pdf-quote-text">"Ce n'est pas en regardant la tempête qu'on apprend à naviguer. C'est en comprenant le vent, en apprenant à tenir le gouvernail, et en ayant le courage de rester le capitaine."</p>
                    </div>
                    <p class="para">Ce que je te demande, c'est de lire ce livre avec ouverture. Certaines pages vont te mettre mal à l'aise. D'autres vont te soulager - parce que tu vas enfin trouver des mots pour ce que tu ressens depuis des mois.</p>
                    <div style="text-align: right; margin-top: 30px; font-weight: 800; font-size: 1.4rem; color: var(--accent-magenta); font-style: italic;">Lina Rela</div>
                </div>
            </div>
            <div class="pdf-footer">-- 1 --</div>
        </div>

        <!-- PAGE 3: TABLE DES MATIÈRES -->
        <div class="pdf-page" id="page-3">
            <div>
                <div class="pdf-header">Lina Rela | Sauver Ton Couple Sans Perdre Ta Dignité</div>
                <div class="pdf-body">
                    <h1 class="page-h1">Table des Matières</h1>
                    <div style="width: 100%; height: 2px; background: #be123c; margin-bottom: 25px;"></div>
                    <div class="toc-list">
                        <div class="toc-item"><div class="toc-title">Introduction</div><div class="toc-desc">Mon frère, assieds-toi, on doit se parler</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 1</div><div class="toc-desc">Le Diagnostic de l'Ombre - Pourquoi tu as l'impression de n'être qu'un portefeuille</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 2</div><div class="toc-desc">Le Miroir de l'Homme - Avant de la changer, regarde-toi</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 3</div><div class="toc-desc">L'Art de se Faire Respecter - Se faire respecter sans crier ni bouder</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 4</div><div class="toc-desc">Le Lit Froid - Briser la grève de l'intimité</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 5</div><div class="toc-desc">La Communication Haute Tension - Parler sans que ça finisse en dispute</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 6</div><div class="toc-desc">Gérer la Tribu - Famille, belle-famille et frontières saines</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 7</div><div class="toc-desc">Éduquer à Deux - Retrouver son autorité paternelle</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 8</div><div class="toc-desc">Transformer la Frustration en Force - Gérer sa colère et sa solitude émotionnelle</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 9</div><div class="toc-desc">Le Plan d'Action sur 30 Jours - Exercices quotidiens pour changer l'atmosphère</div></div>
                        <div class="toc-item"><div class="toc-title">Chapitre 10</div><div class="toc-desc">Quand est-il Temps de Partir ? - La sagesse de savoir si le combat en vaut la peine</div></div>
                        <div class="toc-item"><div class="toc-title">Conclusion</div><div class="toc-desc">Je suis fière de toi, mon frère - Le mot final de Lina Rela</div></div>
                    </div>
                </div>
            </div>
            <div class="pdf-footer">-- 2 --</div>
        </div>

        <!-- PAGE 4: INTRODUCTION -->
        <div class="pdf-page" id="page-4">
            <div>
                <div class="pdf-header">Lina Rela | Sauver Ton Couple Sans Perdre Ta Dignité</div>
                <div class="pdf-body">
                    <h1 class="page-h1">Introduction</h1>
                    <div class="page-sub">Mon frère, assieds-toi. On doit se parler.</div>
                    <p class="para">Je m'appelle <strong>Lina Rela</strong>. Et si tu lis ces lignes aujourd'hui, c'est probablement parce que tu portes quelque chose de très lourd en ce moment. Quelque chose que tu n'as dit à personne. Pas à tes amis, parce qu'ils rigolent de tout. Pas à ta famille, parce qu'ils vont faire des ragots. Pas à elle, parce que ça finit toujours en dispute. Alors tu portes ça seul. Et ça pèse.</p>
                    <div class="pdf-sister-box">
                        <div class="pdf-sister-header">Conseil de grande sœur par Lina Rela</div>
                        <p style="font-size: 0.95rem; color: #4c0519;">Un homme qui souffre en silence dans son foyer n'est pas un homme faible. C'est un homme qui n'a pas encore eu les bons outils. Ce guide est ces outils.</p>
                    </div>
                    <h3 class="page-h3">Qui suis-je pour te parler de tout ça ?</h3>
                    <p class="para">Je ne suis pas une psychologue en blouse blanche. Je suis une femme qui a grandi en observant les hommes autour d'elle - son père, ses frères, ses amis - se débattre en silence dans leurs foyers. Une femme qui a écouté des centaines d'histoires de couples au bord du gouffre. Une femme qui connaît le cœur féminin de l'intérieur et qui a choisi de mettre cette connaissance au service des hommes qui veulent vraiment comprendre.</p>
                    <h3 class="page-h3">Ce que ce guide n'est PAS</h3>
                    <ul class="checklist checklist-cross">
                        <li>Ce n'est pas un manuel pour 'dresser' ta femme ou la contrôler.</li>
                        <li>Ce n'est pas une liste de techniques de manipulation empruntées à des forums douteux.</li>
                        <li>Ce n'est pas un sermon religieux sur la patience et l'obéissance.</li>
                        <li>Ce n'est pas non plus une attaque contre les femmes - je suis une femme, rappelle-toi.</li>
                    </ul>
                </div>
            </div>
            <div class="pdf-footer">-- 4 --</div>
        </div>

        <!-- PAGE 5: CHAPITRE 1 -->
        <div class="pdf-page" id="page-5">
            <div>
                <div class="pdf-header">Lina Rela | Sauver Ton Couple Sans Perdre Ta Dignité</div>
                <div class="pdf-body">
                    <div style="background: #9f1239; color: #fff; padding: 4px 12px; border-radius: 4px; display: inline-block; font-weight: 700; font-size: 0.85rem; margin-bottom: 10px;">Chapitre 1</div>
                    <h1 class="page-h1">Le Diagnostic de l'Ombre</h1>
                    <div class="page-sub">Pourquoi tu as l'impression de n'être qu'un portefeuille - et ce que ça cache vraiment</div>
                    <p class="para">Tu paies le loyer. Tu remplis le frigo. Tu répares ce qui est cassé. Tu meures d'envie de rendre ta famille heureuse. Et pourtant, à la fin de la journée, tu as cette sensation étrange - comme si ta femme te regardait comme on regarde un distributeur automatique. Elle appuie sur les boutons quand elle a besoin de quelque chose, et le reste du temps, tu es juste... là.</p>
                    <div class="pdf-metaphor-box">
                        <div class="pdf-metaphor-header"><i class="fa-solid fa-tree"></i> La métaphore de l'arbre et du sol</div>
                        <div class="pdf-metaphor-body">Imagine ta relation comme un arbre. Les feuilles qui tombent, la froideur, le manque de respect - ce sont les symptômes visibles. Mais le vrai problème, c'est dans le sol - dans les racines de votre connexion.</div>
                    </div>
                    <div class="pdf-quote-box">
                        <p class="pdf-quote-text">"Un couple ne meurt pas d'un grand choc. Il meurt de mille petits abandons. Mille petites fois où l'on a choisi le confort du silence à la difficulté de la connexion."</p>
                    </div>
                </div>
            </div>
            <div class="pdf-footer">-- 7 --</div>
        </div>

        <!-- PAGE 6: ANNEXE & REGLES D'OR -->
        <div class="pdf-page" id="page-6">
            <div>
                <div class="pdf-header">Lina Rela | Sauver Ton Couple Sans Perdre Ta Dignité</div>
                <div class="pdf-body">
                    <h1 class="page-h1">Annexe - Les Outils Essentiels</h1>
                    <div class="page-sub">Les 10 règles d'or de Lina Rela</div>
                    <ul class="checklist">
                        <li><strong>1.</strong> Un homme qui se respecte inspire le respect. Un homme qui s'efface l'invite à disparaître.</li>
                        <li><strong>2.</strong> La colère est de l'information. Avant d'exploser, demande-toi ce qu'elle essaie de te dire.</li>
                        <li><strong>3.</strong> L'écoute active est ton arme la plus puissante dans une dispute.</li>
                        <li><strong>4.</strong> Parle toujours en 'Je', jamais en 'Tu' accusateur.</li>
                        <li><strong>5.</strong> La cohérence vaut plus que la perfection. Fais ce que tu dis, toujours.</li>
                        <li><strong>6.</strong> Ton foyer est sacré. Protège-le des influences extérieures.</li>
                        <li><strong>7.</strong> Un homme avec un projet est infiniment plus attractif qu'un homme sans direction.</li>
                        <li><strong>8.</strong> Le corps, l'esprit, les projets, les amis - tout ça nourrit ton couple.</li>
                        <li><strong>9.</strong> L'intimité physique revient quand l'intimité émotionnelle est restaurée.</li>
                        <li><strong>10.</strong> Sauver ton couple commence par te sauver toi-même.</li>
                    </ul>
                    <div class="pdf-sister-box" style="margin-top: 30px;">
                        <div class="pdf-sister-header">Une dernière pensée de Lina Rela</div>
                        <p style="font-size: 1.05rem; font-style: italic; color: #4c0519;">"Dans chaque foyer où j'ai vu des choses changer, ça a commencé par un homme qui a décidé de se lever un matin et de faire autrement. Pas d'un coup, pas parfaitement. Mais délibérément. Avec intention. Avec amour. Ce matin-là, c'était peut-être aujourd'hui pour toi."</p>
                        <div style="text-align: right; font-weight: 800; font-size: 1.2rem; color: var(--accent-magenta); margin-top: 10px;">Lina Rela — Coach Relationnelle & Auteure</div>
                    </div>
                </div>
            </div>
            <div class="pdf-footer">-- 52 --</div>
        </div>
"""

html_foot = """
    </div>
    <script type="text/javascript">
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
            var match = document.cookie.match(/(?:^|;\\s*)googtrans=([^;]*)/);
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
"""

full_html = html_head + html_pages + html_foot

scratch_dir = r'C:\Users\HP TTS\.gemini\antigravity\scratch'
brain_dir = r'C:\Users\HP TTS\.gemini\antigravity\brain\95daf908-a857-4874-9abc-4693869bfe05'
os.makedirs(brain_dir, exist_ok=True)

p1 = os.path.join(scratch_dir, 'pdf_guide_lina_rela.html')
p2 = os.path.join(brain_dir, 'sauver_ton_couple_pdf_visual_lina_rela.html')

with open(p1, 'w', encoding='utf-8') as f:
    f.write(full_html)

with open(p2, 'w', encoding='utf-8') as f:
    f.write(full_html)

print("PDF HTML view written successfully to:", p1)
print("Artifact PDF HTML view written successfully to:", p2)
