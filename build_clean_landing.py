import os

output_dir = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing'
os.makedirs(output_dir, exist_ok=True)
html_file = os.path.join(output_dir, 'index.html')

def make_mockup_svg(title, num, theme_color='#8b5cf6'):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 320" width="100%" height="100%">
      <defs>
        <radialGradient id="goldGlow-{num}" cx="40%" cy="45%" r="55%">
          <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.95" />
          <stop offset="60%" stop-color="{theme_color}" stop-opacity="0.75" />
          <stop offset="100%" stop-color="#0f0716" stop-opacity="0" />
        </radialGradient>
        <linearGradient id="boxFront-{num}" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stop-color="#231038" />
          <stop offset="100%" stop-color="#0b0412" />
        </linearGradient>
        <linearGradient id="boxSpine-{num}" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="{theme_color}" />
          <stop offset="100%" stop-color="#6d28d9" />
        </linearGradient>
        <linearGradient id="laptopScreen-{num}" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#2d1348" />
          <stop offset="100%" stop-color="#0b0412" />
        </linearGradient>
        <filter id="dropShadow-{num}" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#000" flood-opacity="0.6"/>
        </filter>
      </defs>

      <!-- Golden Circle Glow Backdrop -->
      <circle cx="190" cy="150" r="135" fill="url(#goldGlow-{num})" />

      <g filter="url(#dropShadow-{num})">
        <!-- 3D Software Box (Back Right) -->
        <g id="software-box">
          <polygon points="230,50 270,30 350,45 310,65" fill="#fbbf24" />
          <polygon points="230,50 310,65 310,210 230,195" fill="url(#boxSpine-{num})" />
          <text x="270" y="130" fill="#ffffff" font-size="10" font-weight="bold" font-family="sans-serif" transform="rotate(62 270 130)" text-anchor="middle">HOMME MODERNE</text>
          <polygon points="310,65 350,45 350,190 310,210" fill="url(#boxFront-{num})" stroke="rgba(252,211,77,0.4)" stroke-width="1" />
          <text x="330" y="110" fill="#f59e0b" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">CHAPITRE {num}</text>
          <text x="330" y="130" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">{title[:14]}</text>
        </g>

        <!-- 3D Book Cover (Middle) -->
        <g id="book-stand">
          <polygon points="280,110 310,95 370,105 340,120" fill="#f59e0b" />
          <polygon points="280,110 340,120 340,240 280,230" fill="#7c3aed" />
          <polygon points="340,120 370,105 370,225 340,240" fill="#150824" />
          <text x="310" y="170" fill="#ffffff" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">{title[:12]}</text>
        </g>

        <!-- 3D Silver Laptop (Foreground Left) -->
        <g id="laptop-perspective">
          <polygon points="40,110 220,90 230,220 50,240" fill="#1e293b" stroke="#cbd5e1" stroke-width="2" />
          <polygon points="48,118 212,100 222,212 58,230" fill="url(#laptopScreen-{num})" />
          <rect x="70" y="130" width="130" height="20" rx="4" fill="{theme_color}" transform="skewY(-5)" />
          <text x="135" y="144" fill="#ffffff" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle" transform="skewY(-5)">CHAPITRE {num}</text>
          <text x="135" y="172" fill="#fde047" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle" transform="skewY(-5)">{title}</text>
          <text x="135" y="192" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" transform="skewY(-5)">DORA ÉLYSIANE</text>
          
          <!-- Base -->
          <polygon points="50,240 230,220 270,250 20,275" fill="#e2e8f0" />
          <polygon points="20,275 270,250 270,258 20,283" fill="#64748b" />
          <polygon points="120,252 170,246 175,257 125,263" fill="#94a3b8" />
        </g>
      </g>
    </svg>'''

def make_hero_bundle_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 420" width="100%" height="100%">
      <defs>
        <radialGradient id="heroGoldGlow" cx="50%" cy="45%" r="55%">
          <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.95" />
          <stop offset="50%" stop-color="#8b5cf6" stop-opacity="0.75" />
          <stop offset="100%" stop-color="#0f0716" stop-opacity="0" />
        </radialGradient>
        <filter id="heroShadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="18" stdDeviation="15" flood-color="#000" flood-opacity="0.7"/>
        </filter>
      </defs>

      <!-- Golden Sphere Glow -->
      <circle cx="475" cy="210" r="200" fill="url(#heroGoldGlow)" />

      <g filter="url(#heroShadow)">
        <!-- Stack of Software Boxes Behind -->
        <g id="bg-boxes">
          <!-- Box 1 -->
          <polygon points="160,80 190,60 250,75 220,95" fill="#d4af37" />
          <polygon points="160,80 220,95 220,220 160,205" fill="#7c3aed" />
          <polygon points="220,95 250,75 250,200 220,220" fill="#0f0716" />
          <text x="190" y="150" fill="#fff" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">CHAPITRES</text>

          <!-- Box 2 (Center High) -->
          <polygon points="410,40 450,20 530,35 490,55" fill="#fbbf24" />
          <polygon points="410,40 490,55 490,190 410,175" fill="#6d28d9" />
          <polygon points="490,55 530,35 530,170 490,190" fill="#1e1030" />
          <text x="450" y="110" fill="#fff" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">HOMME MODERNE</text>

          <!-- Box 3 -->
          <polygon points="700,80 730,60 790,75 760,95" fill="#d4af37" />
          <polygon points="700,80 760,95 760,220 700,205" fill="#9333ea" />
          <polygon points="760,95 790,60 790,200 760,220" fill="#0f0716" />
          <text x="730" y="150" fill="#fff" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">BONUS 1 & 2</text>
        </g>

        <!-- Left 3D Laptop Open -->
        <g id="left-laptop">
          <polygon points="80,160 340,130 355,310 95,340" fill="#1e293b" stroke="#cbd5e1" stroke-width="2" />
          <polygon points="90,170 330,143 343,298 103,325" fill="#0f172a" />
          <!-- Screen Banner -->
          <rect x="120" y="195" width="190" height="30" rx="4" fill="#7c3aed" transform="skewY(-6)" />
          <text x="215" y="215" fill="#ffffff" font-size="12" font-weight="900" font-family="sans-serif" text-anchor="middle" transform="skewY(-6)">GUIDE DE RÉSOLUTION</text>
          <text x="215" y="250" fill="#fde047" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle" transform="skewY(-6)">POUR L'HOMME MODERNE</text>
          
          <!-- Base -->
          <polygon points="95,340 355,310 420,355 30,390" fill="#e2e8f0" />
          <polygon points="30,390 420,355 420,365 30,400" fill="#64748b" />
        </g>

        <!-- Right 3D Laptop Open -->
        <g id="right-laptop">
          <polygon points="500,140 760,160 745,340 485,310" fill="#1e293b" stroke="#cbd5e1" stroke-width="2" />
          <polygon points="510,153 750,170 737,325 497,298" fill="#0f172a" />
          <!-- Screen Banner -->
          <rect x="530" y="195" width="190" height="30" rx="4" fill="#a855f7" transform="skewY(4)" />
          <text x="625" y="215" fill="#ffffff" font-size="13" font-weight="900" font-family="sans-serif" text-anchor="middle" transform="skewY(4)">ACCÈS IMMÉDIAT</text>
          <text x="625" y="250" fill="#fde047" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle" transform="skewY(4)">9 CHAPITRES + 2 BONUS</text>
          
          <!-- Base -->
          <polygon points="485,310 745,340 810,390 420,355" fill="#e2e8f0" />
          <polygon points="420,355 810,390 810,400 420,365" fill="#64748b" />
        </g>
      </g>
    </svg>'''

# Generate SVGs
svg_m1 = make_mockup_svg("Diagnostic Ombre", 1, "#a855f7")
svg_m2 = make_mockup_svg("Miroir de l'Homme", 2, "#8b5cf6")
svg_m3 = make_mockup_svg("Se Faire Respecter", 3, "#7c3aed")
svg_m4 = make_mockup_svg("Le Lit Froid", 4, "#9333ea")
svg_m5 = make_mockup_svg("Haute Tension", 5, "#c084fc")
svg_m6 = make_mockup_svg("Gérer la Tribu", 6, "#6d28d9")
svg_m7 = make_mockup_svg("Frustration en Force", 7, "#7e22ce")
svg_m8 = make_mockup_svg("Plan d'Action", 8, "#a855f7")
svg_m9 = make_mockup_svg("Temps de Partir", 9, "#6b21a8")

svg_b1 = make_mockup_svg("10 Phrases", "B1", "#a855f7")
svg_b2 = make_mockup_svg("12 Erreurs", "B2", "#7c3aed")

svg_hero_bundle = make_hero_bundle_svg()
svg_guarantee_bundle = make_mockup_svg("Garantie 30 Jours", "GARANTIE", "#8b5cf6")

html_content = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guide de résolution des crises de couple pour l’homme moderne | Dora Élysiane</title>
    <meta name="description" content="Découvre les stratégies de communication qui transforment une discussion tendue en échange apaisé et constructif. Avec Dora Élysiane.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {{
            --purple-primary: #7c3aed;
            --purple-light: #a855f7;
            --purple-dark: #5b21b6;
            --purple-gradient: linear-gradient(135deg, #a855f7 0%, #7c3aed 50%, #6d28d9 100%);
            --purple-hover: linear-gradient(135deg, #6d28d9 0%, #5b21b6 100%);
            --gold-glow: #f59e0b;
            --dark-bg: #0f0716;
            --dark-surface: #170b24;
            --dark-card: #201030;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --border-radius: 16px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --shadow-sm: 0 4px 6px -1px rgba(0,0,0,0.05);
            --shadow-md: 0 10px 30px -5px rgba(124, 58, 237, 0.15);
            --shadow-lg: 0 20px 40px -15px rgba(124, 58, 237, 0.35);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
            font-family: 'Inter', sans-serif;
            color: var(--text-dark);
            background-color: #ffffff;
            line-height: 1.6;
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            line-height: 1.25;
        }}

        .container {{
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        .text-center {{ text-align: center; }}
        .text-purple {{ color: var(--purple-primary); }}

        /* Top Bar Urgency */
        .announcement-bar {{
            background: var(--purple-gradient);
            color: #ffffff;
            text-align: center;
            padding: 12px 15px;
            font-size: 0.95rem;
            font-weight: 700;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 12px rgba(124, 58, 237, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .announcement-bar .timer-badge {{
            background: rgba(0,0,0,0.35);
            padding: 4px 14px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.3);
            font-family: monospace;
            font-size: 1.05rem;
            color: #fde047;
            font-weight: 800;
        }}

        /* Buttons matching Karamo Eloquence 2.0 CTA in LUXURY PURPLE */
        .btn-eloquence {{
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px 42px;
            border-radius: 12px;
            font-family: 'Outfit', sans-serif;
            font-size: 1.35rem;
            font-weight: 900;
            text-decoration: none;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            width: 100%;
            max-width: 680px;
            text-align: center;
            background: var(--purple-gradient);
            color: #ffffff;
            box-shadow: 0 15px 35px rgba(124, 58, 237, 0.4);
        }}

        .btn-eloquence:hover {{
            transform: translateY(-3px) scale(1.02);
            background: var(--purple-hover);
            box-shadow: 0 20px 45px rgba(124, 58, 237, 0.55);
        }}

        .btn-subtext {{
            font-size: 0.85rem;
            font-weight: 500;
            opacity: 0.95;
            margin-top: 4px;
        }}

        /* Hero Section */
        .hero {{
            padding: 70px 0 90px;
            background: linear-gradient(180deg, #170b24 0%, #09030e 100%);
            color: #ffffff;
            position: relative;
            overflow: hidden;
        }}

        .hero-badge {{
            display: inline-block;
            background: rgba(168, 85, 247, 0.15);
            border: 1px solid rgba(168, 85, 247, 0.4);
            color: #c084fc;
            padding: 8px 22px;
            border-radius: 30px;
            font-size: 0.88rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 24px;
        }}

        .hero-title {{
            font-size: 3rem;
            line-height: 1.2;
            margin-bottom: 24px;
            color: #ffffff;
            font-weight: 900;
        }}

        .hero-title span {{
            color: #a855f7;
        }}

        .hero-subtitle {{
            font-size: 1.2rem;
            color: #cbd5e1;
            max-width: 860px;
            margin: 0 auto 36px;
            line-height: 1.6;
        }}

        .hero-target-box {{
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(168, 85, 247, 0.25);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 22px 30px;
            max-width: 880px;
            margin: 0 auto 40px;
            font-size: 1.05rem;
            color: #e2e8f0;
        }}

        .hero-target-box strong {{
            color: #ffffff;
        }}

        .hero-mockup-wrapper {{
            max-width: 950px;
            margin: 40px auto 40px;
        }}

        /* Proof Bar */
        .proof-bar {{
            background: #ffffff;
            padding: 35px 0;
            border-bottom: 1px solid #e2e8f0;
        }}

        .proof-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
            text-align: center;
        }}

        .proof-item h3 {{
            font-size: 2.3rem;
            color: var(--purple-primary);
            margin-bottom: 4px;
        }}

        .proof-item p {{
            color: var(--text-muted);
            font-size: 0.98rem;
            font-weight: 600;
        }}

        /* Problem vs Solution */
        .transformation-section {{
            padding: 90px 0;
            background: #ffffff;
        }}

        .section-header {{
            text-align: center;
            max-width: 840px;
            margin: 0 auto 60px;
        }}

        .section-title {{
            font-size: 2.4rem;
            color: var(--text-dark);
            margin-bottom: 16px;
            font-weight: 900;
        }}

        .section-subtitle {{
            font-size: 1.15rem;
            color: var(--text-muted);
        }}

        .compare-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-top: 40px;
        }}

        .compare-card {{
            border-radius: var(--border-radius);
            padding: 40px;
            box-shadow: var(--shadow-md);
        }}

        .compare-card.problem {{
            background: #fff5f5;
            border-left: 6px solid #ef4444;
        }}

        .compare-card.solution {{
            background: #fdf4ff;
            border-left: 6px solid var(--purple-primary);
        }}

        .compare-card h3 {{
            font-size: 1.6rem;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .compare-list {{
            list-style: none;
        }}

        .compare-list li {{
            padding: 12px 0;
            border-bottom: 1px dashed rgba(0,0,0,0.08);
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 1.05rem;
        }}

        .compare-list li:last-child {{
            border-bottom: none;
        }}

        /* MODULE CARDS MATCHING SCREENSHOT 1 IN PURPLE */
        .curriculum-section {{
            padding: 90px 0;
            background: #fafafa;
        }}

        .modules-list {{
            display: flex;
            flex-direction: column;
            gap: 35px;
            margin-top: 50px;
        }}

        .module-card-eloquence {{
            background: #ffffff;
            border: 2px solid #a855f7;
            border-radius: 16px;
            padding: 35px;
            box-shadow: 0 10px 30px rgba(124, 58, 237, 0.08);
            display: grid;
            grid-template-columns: 380px 1fr;
            gap: 40px;
            align-items: center;
        }}

        .module-mockup-side {{
            width: 100%;
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .module-info-side h3 {{
            font-size: 1.8rem;
            font-style: italic;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 24px;
            line-height: 1.3;
        }}

        .module-bullets {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}

        .module-bullets li {{
            font-size: 1.1rem;
            color: #1e293b;
            display: flex;
            align-items: flex-start;
            gap: 12px;
            line-height: 1.5;
        }}

        .purple-arrow-icon {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 24px;
            height: 24px;
            background: #7c3aed;
            color: #ffffff;
            border-radius: 50%;
            font-size: 0.8rem;
            flex-shrink: 0;
            margin-top: 2px;
        }}

        /* BONUS CARDS IN PURPLE */
        .bonus-section {{
            padding: 90px 0;
            background: #0f0716;
            color: #ffffff;
        }}

        .bonus-cards-stack {{
            display: flex;
            flex-direction: column;
            gap: 45px;
            margin-top: 50px;
            max-width: 960px;
            margin-left: auto;
            margin-right: auto;
        }}

        .bonus-card-eloquence {{
            background: #09030e;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(168, 85, 247, 0.4);
            box-shadow: 0 20px 40px rgba(0,0,0,0.8);
        }}

        .bonus-header-banner {{
            background: var(--purple-gradient);
            color: #ffffff;
            padding: 18px 24px;
            text-align: center;
        }}

        .bonus-header-banner h3 {{
            font-size: 1.6rem;
            font-weight: 900;
            margin-bottom: 4px;
        }}

        .bonus-header-banner .bonus-val-tag {{
            font-size: 1.25rem;
            font-weight: 800;
            color: #fde047;
        }}

        .bonus-body-content {{
            padding: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }}

        .bonus-mockup-center {{
            max-width: 440px;
            width: 100%;
            height: 260px;
            margin-bottom: 24px;
        }}

        .bonus-text-desc {{
            font-size: 1.15rem;
            color: #e2e8f0;
            line-height: 1.7;
            max-width: 800px;
        }}

        /* GUARANTEE SECTION IN PURPLE */
        .guarantee-section-eloquence {{
            padding: 90px 0;
            background: linear-gradient(180deg, #170b24 0%, #09030e 100%);
            color: #ffffff;
        }}

        .guarantee-grid-layout {{
            display: grid;
            grid-template-columns: 420px 1fr;
            gap: 50px;
            align-items: center;
            max-width: 1000px;
            margin: 0 auto;
        }}

        .guarantee-mockup-side {{
            width: 100%;
            height: 280px;
        }}

        .guarantee-text-side h2 {{
            font-size: 2.2rem;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 24px;
        }}

        .guarantee-text-side p {{
            font-size: 1.15rem;
            color: #cbd5e1;
            line-height: 1.7;
            margin-bottom: 20px;
        }}

        .guarantee-closing {{
            font-size: 1.25rem;
            font-weight: 800;
            color: #ffffff;
            margin-top: 10px;
        }}

        /* PRICING STACK */
        .pricing-section {{
            padding: 100px 0;
            background: #ffffff;
        }}

        .pricing-box {{
            max-width: 820px;
            margin: 0 auto;
            background: #ffffff;
            border: 3px solid var(--purple-primary);
            border-radius: 24px;
            box-shadow: 0 25px 60px rgba(124, 58, 237, 0.18);
            overflow: hidden;
        }}

        .pricing-header {{
            background: var(--purple-gradient);
            color: #ffffff;
            padding: 30px;
            text-align: center;
        }}

        .pricing-header h3 {{
            font-size: 1.9rem;
            font-weight: 900;
            margin-bottom: 8px;
        }}

        .pricing-body {{
            padding: 40px;
        }}

        .stack-list {{
            list-style: none;
            margin-bottom: 30px;
        }}

        .stack-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 0;
            border-bottom: 1px solid #f1f5f9;
            font-size: 1.1rem;
        }}

        .stack-item span.item-val {{
            font-weight: 800;
            color: var(--purple-primary);
        }}

        .price-total-box {{
            background: #fdf4ff;
            border-radius: 16px;
            padding: 26px;
            text-align: center;
            margin-bottom: 30px;
            border: 2px dashed var(--purple-primary);
        }}

        .old-price {{
            font-size: 1.35rem;
            color: #94a3b8;
            text-decoration: line-through;
            margin-bottom: 4px;
            font-weight: 600;
        }}

        .new-price {{
            font-size: 3.6rem;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            color: var(--purple-primary);
            line-height: 1;
            margin-bottom: 8px;
        }}

        .new-price small {{
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-dark);
        }}

        .payment-methods {{
            display: flex;
            flex-direction: column;
            gap: 16px;
            align-items: center;
            margin-top: 30px;
        }}

        /* Testimonials */
        .testimonials-section {{
            padding: 90px 0;
            background: #fafafa;
        }}

        .testimonials-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }}

        .testimonial-card {{
            background: #ffffff;
            border-radius: 16px;
            padding: 30px;
            box-shadow: var(--shadow-sm);
            border: 1px solid #e2e8f0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .stars {{
            color: #f59e0b;
            margin-bottom: 14px;
            font-size: 1.1rem;
        }}

        .testimonial-quote {{
            font-style: italic;
            color: #334155;
            font-size: 1.05rem;
            margin-bottom: 20px;
        }}

        .client-info {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .client-avatar {{
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: var(--purple-primary);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.1rem;
        }}

        .client-details h4 {{
            font-size: 1.05rem;
            color: var(--text-dark);
        }}

        .client-details span {{
            font-size: 0.85rem;
            color: var(--text-muted);
        }}

        /* Author Section */
        .author-section {{
            padding: 100px 0;
            background: #ffffff;
        }}

        .author-grid-brand {{
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 50px;
            align-items: center;
        }}

        .author-brand-emblem {{
            width: 100%;
            height: 320px;
            background: linear-gradient(145deg, #170b24 0%, #09030e 100%);
            border: 2px solid var(--purple-primary);
            border-radius: 24px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            box-shadow: var(--shadow-lg);
            text-align: center;
            padding: 30px;
        }}

        .author-monogram {{
            font-family: 'Outfit', sans-serif;
            font-size: 4rem;
            font-weight: 900;
            color: var(--purple-light);
            line-height: 1;
            margin-bottom: 10px;
        }}

        /* FAQ Accordion */
        .faq-section {{
            padding: 90px 0;
            background: #fafafa;
        }}

        .faq-accordion {{
            max-width: 840px;
            margin: 50px auto 0;
        }}

        .faq-item {{
            background: #ffffff;
            border-radius: 12px;
            margin-bottom: 16px;
            border: 1px solid #e2e8f0;
            overflow: hidden;
        }}

        .faq-question {{
            padding: 22px 28px;
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-dark);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: var(--transition);
        }}

        .faq-question:hover {{
            background: #fdf4ff;
            color: var(--purple-primary);
        }}

        .faq-answer {{
            padding: 0 28px 22px;
            color: var(--text-muted);
            font-size: 1.05rem;
            display: none;
            line-height: 1.6;
        }}

        .faq-item.active .faq-answer {{
            display: block;
        }}

        .faq-item.active .faq-icon {{
            transform: rotate(180deg);
            color: var(--purple-primary);
        }}

        /* Mobile Sticky CTA */
        .mobile-sticky-bar {{
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #ffffff;
            padding: 12px 16px;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
            z-index: 999;
            border-top: 1px solid #e2e8f0;
        }}

        @media (max-width: 992px) {{
            .hero-title {{ font-size: 2.2rem; }}
            .compare-grid {{ grid-template-columns: 1fr; }}
            .module-card-eloquence {{ grid-template-columns: 1fr; text-align: center; }}
            .module-bullets li {{ text-align: left; }}
            .guarantee-grid-layout {{ grid-template-columns: 1fr; text-align: center; }}
            .author-grid-brand {{ grid-template-columns: 1fr; text-align: center; }}
            .author-brand-emblem {{ max-width: 320px; margin: 0 auto; height: 260px; }}
        }}

        @media (max-width: 768px) {{
            .announcement-bar {{ font-size: 0.85rem; padding: 10px; }}
            .hero {{ padding: 40px 0 60px; }}
            .hero-title {{ font-size: 1.85rem; }}
            .hero-subtitle {{ font-size: 1.05rem; }}
            .btn-eloquence {{ font-size: 1.15rem; padding: 16px 24px; }}
            .mobile-sticky-bar {{ display: flex; align-items: center; justify-content: space-between; }}
            .mobile-sticky-bar .btn-eloquence {{ font-size: 1rem; padding: 12px 20px; width: 100%; }}
        }}
    </style>
</head>
<body>

    <!-- Top Bar Urgency -->
    <div class="announcement-bar">
        <span>🔥 UNE PROMOTION SPÉCIALE POUR CETTE SEMAINE — CLÔTURE DANS :</span>
        <div class="timer-badge" id="top-timer">22:45:18</div>
    </div>

    <!-- Hero Section -->
    <section class="hero text-center">
        <div class="container">
            <div class="hero-badge">
                <i class="fa-solid fa-shield-halved"></i> GUIDE DE RÉSOLUTION DES CRISES DE COUPLE
            </div>
            
            <h1 class="hero-title">
                Tu en as marre des tensions qui s’accumulent et de ne <span>jamais savoir quoi dire au bon moment</span> ?
            </h1>
            
            <p class="hero-subtitle">
                Avec le <strong>“Guide de résolution des crises de couple pour l’homme moderne”</strong>, tu apprends exactement comment réagir, quoi dire et comment apaiser les conflits pour rétablir une communication saine et renforcer ton couple.
            </p>

            <!-- GIANT HERO BUNDLE SHOWCASE -->
            <div class="hero-mockup-wrapper">
                {svg_hero_bundle}
            </div>

            <!-- CTA Button -->
            <a href="#commander" class="btn-eloquence">
                <span>Obtenir maintenant</span>
                <span class="btn-subtext">Accès Immédiat au Guide + 2 Bonus • Seulement 9 900 FCFA (~15.5 €)</span>
            </a>
            
            <p style="font-size: 0.92rem; color: #cbd5e1; margin-top: 16px;">
                <i class="fa-solid fa-lock text-purple"></i> Paiement 100% Sécurisé (Wave, Orange Money, MTN, Moov, Carte)
            </p>

            <div class="hero-target-box" style="margin-top: 40px;">
                Découvre les stratégies de communication qui transforment une discussion tendue en échange apaisé et constructif. Deviens cet homme calme, posé et clair dans ses mots, capable de gérer les tensions, restaurer la connexion et renforcer le respect sans forcer.
            </div>
        </div>
    </section>

    <!-- Social Proof Bar -->
    <section class="proof-bar">
        <div class="container">
            <div class="proof-grid">
                <div class="proof-item">
                    <h3>+5 000</h3>
                    <p>Hommes Accompagnés</p>
                </div>
                <div class="proof-item">
                    <h3>98%</h3>
                    <p>Satisfaction Client</p>
                </div>
                <div class="proof-item">
                    <h3>4.9 / 5</h3>
                    <p>Note Moyenne</p>
                </div>
                <div class="proof-item">
                    <h3>9 Chapitres</h3>
                    <p>Guide Pratique</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Problem & Transformation Section -->
    <section class="transformation-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Passe de la confusion au contrôle, et fais en sorte que vos échanges redeviennent naturels, fluides et équilibrés.</h2>
                <p class="section-subtitle">Rends-toi compte...</p>
            </div>

            <div class="compare-grid">
                <!-- Problem Card -->
                <div class="compare-card problem">
                    <h3><i class="fa-solid fa-circle-xmark text-purple"></i> 📌 Le problème</h3>
                    <ul class="compare-list">
                        <li>
                            <i class="fa-solid fa-xmark text-purple"></i>
                            <span>Au début, tout allait bien. Puis les tensions ont commencé à apparaître.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-purple"></i>
                            <span>Discussions qui tournent mal, silences lourds, distance émotionnelle.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-purple"></i>
                            <span>Tu ne sais pas quoi dire au bon moment quand la tension monte.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-purple"></i>
                            <span>Tu as peur d’aggraver la situation et tu te retrouves souvent incompris.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-purple"></i>
                            <span>Résultat : la connexion s’affaiblit, et la relation devient de plus en plus fragile.</span>
                        </li>
                    </ul>
                </div>

                <!-- Solution Card -->
                <div class="compare-card solution">
                    <h3><i class="fa-solid fa-circle-check text-purple"></i> ✅ La solution : un guide clair et structuré</h3>
                    <ul class="compare-list">
                        <li>
                            <i class="fa-solid fa-check text-purple"></i>
                            <span>Gérer les conflits avec plus de calme et de contrôle.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-purple"></i>
                            <span>Communiquer de manière plus claire et efficace sans tension.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-purple"></i>
                            <span>Comprendre ce qui se joue réellement dans une dispute.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-purple"></i>
                            <span>Réparer la connexion après une tension et réinstaurer le respect.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-purple"></i>
                            <span>Tu ne réagis plus au hasard : tu comprends et tu maîtrises.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- MODULES / CHAPTERS SECTION -->
    <section class="curriculum-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">📘 Ce que contient le guide</h2>
                <p class="section-subtitle">Découvre les 9 chapitres conçus pour l'homme moderne :</p>
            </div>

            <div class="modules-list">
                
                <!-- CHAPITRE 1 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m1}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 1 : Le Diagnostic de l'Ombre</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Pourquoi tu as l'impression de n'être qu'un portefeuille ?</li>
                            <li><span class="purple-arrow-icon">➔</span> Analyser la perte de connexion émotionnelle dans le couple</li>
                            <li><span class="purple-arrow-icon">➔</span> Comprendre les causes profondes des tensions accumulées</li>
                            <li><span class="purple-arrow-icon">➔</span> Identifier les signaux d'alerte avant qu'il ne soit trop tard</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 2 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m2}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 2 : Le Miroir de l'Homme</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Avant de la changer elle, regarde-toi</li>
                            <li><span class="purple-arrow-icon">➔</span> Retrouver sa confiance en soi et son leadership personnel</li>
                            <li><span class="purple-arrow-icon">➔</span> Ajuster certaines réactions sans changer qui tu es</li>
                            <li><span class="purple-arrow-icon">➔</span> Agir avec plus de calme, de maîtrise et de maturité émotionnelle</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 3 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m3}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 3 : L'Art de se faire respecter (Sans crier)</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Comment réagir face au mépris ou à la comparaison</li>
                            <li><span class="purple-arrow-icon">➔</span> Réagir sans entrer dans la violence ou le silence boudeur</li>
                            <li><span class="purple-arrow-icon">➔</span> Fixer des limites claires et poser le respect naturellement</li>
                            <li><span class="purple-arrow-icon">➔</span> Garder son sang-froid dans les moments les plus tendus</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 4 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m4}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 4 : Le Lit Froid – Briser la Grève de l'Intimité</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Comprendre le désir féminin et ses mécanismes</li>
                            <li><span class="purple-arrow-icon">➔</span> Reconnecter physiquement sans mendier l'attention</li>
                            <li><span class="purple-arrow-icon">➔</span> Retrouver une complicité chaleureuse et naturelle</li>
                            <li><span class="purple-arrow-icon">➔</span> Rétablir la passion et le rapprochement corporel</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 5 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m5}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 5 : La Communication "Haute Tension"</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Comment parler de tes besoins sans que ça finisse en dispute</li>
                            <li><span class="purple-arrow-icon">➔</span> Apprendre l'écoute active et l'affirmation de soi</li>
                            <li><span class="purple-arrow-icon">➔</span> Désamorcer une discussion explosive avant l'escalade</li>
                            <li><span class="purple-arrow-icon">➔</span> Rendre les échanges plus clairs et efficaces</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 6 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m6}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 6 : Gérer la "Tribu" (Famille et Belle-famille)</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Mettre des frontières saines entre ton foyer et les influences extérieures</li>
                            <li><span class="purple-arrow-icon">➔</span> Gérer les pressions de la belle-famille sans créer de rancœur</li>
                            <li><span class="purple-arrow-icon">➔</span> Protéger l'intimité et les décisions du couple</li>
                            <li><span class="purple-arrow-icon">➔</span> Maintenir l'unité et la solidarité dans le foyer</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 7 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m7}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 7 : Transformer la frustration en force</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Gérer sa propre colère et sa solitude émotionnelle</li>
                            <li><span class="purple-arrow-icon">➔</span> Trouver ses propres soutiens et piliers d'équilibre</li>
                            <li><span class="purple-arrow-icon">➔</span> Transformer les moments difficiles en moteur d'évolution</li>
                            <li><span class="purple-arrow-icon">➔</span> Conserver sa sérénité en toutes circonstances</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 8 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m8}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 8 : Le Plan d'Action sur 30 jours</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> Des exercices concrets et quotidiens</li>
                            <li><span class="purple-arrow-icon">➔</span> Changer progressivement l'atmosphère de la maison</li>
                            <li><span class="purple-arrow-icon">➔</span> Mettre en pratique les conseils jour après jour</li>
                            <li><span class="purple-arrow-icon">➔</span> Obtenir des améliorations durables et perceptibles</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 9 -->
                <div class="module-card-eloquence">
                    <div class="module-mockup-side">
                        {svg_m9}
                    </div>
                    <div class="module-info-side">
                        <h3>Chapitre 9 : Quand est-il temps de partir ?</h3>
                        <ul class="module-bullets">
                            <li><span class="purple-arrow-icon">➔</span> La sagesse de savoir si le combat en vaut encore la peine</li>
                            <li><span class="purple-arrow-icon">➔</span> Évaluer la situation avec lucidité et sérénité</li>
                            <li><span class="purple-arrow-icon">➔</span> Prendre les bonnes décisions pour son avenir</li>
                            <li><span class="purple-arrow-icon">➔</span> Préserver son respect et sa dignité</li>
                        </ul>
                    </div>
                </div>

            </div>

            <!-- CTA Under Curriculum -->
            <div class="text-center" style="margin-top: 50px;">
                <a href="#commander" class="btn-eloquence">
                    <span>Obtenir maintenant</span>
                </a>
            </div>
        </div>
    </section>

    <!-- BONUS SECTION -->
    <section class="bonus-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title" style="color:#fff;">Et c'est pas fini !</h2>
                <p class="section-subtitle" style="color:#cbd5e1;">Obtiens ces bonus GRATUITEMENT avec ton guide aujourd'hui :</p>
            </div>

            <div class="bonus-cards-stack">
                <!-- Bonus 1 Card -->
                <div class="bonus-card-eloquence">
                    <div class="bonus-header-banner">
                        <h3>Bonus 1 : 10 phrases pour désamorcer un conflit immédiatement</h3>
                        <div class="bonus-val-tag">Valeur 10 € / 6 387 FCFA (GRATUIT)</div>
                    </div>
                    <div class="bonus-body-content">
                        <div class="bonus-mockup-center">
                            {svg_b1}
                        </div>
                        <p class="bonus-text-desc">
                            👉 Un ensemble de phrases simples, prêtes à utiliser dans les moments tendus pour <strong>calmer une discussion, éviter l’escalade et reprendre le contrôle émotionnel</strong>. Tu sauras quoi dire au bon moment pour apaiser ta partenaire, réduire la pression et ramener la conversation vers quelque chose de plus constructif.
                        </p>
                    </div>
                </div>

                <!-- Bonus 2 Card -->
                <div class="bonus-card-eloquence">
                    <div class="bonus-header-banner">
                        <h3>Bonus 2 : Les 12 erreurs qui détruisent un couple sans s’en rendre compte</h3>
                        <div class="bonus-val-tag">Valeur 12 € / 7 664 FCFA (GRATUIT)</div>
                    </div>
                    <div class="bonus-body-content">
                        <div class="bonus-mockup-center">
                            {svg_b2}
                        </div>
                        <p class="bonus-text-desc">
                            👉 Tu vas découvrir les <strong>comportements les plus courants qui fragilisent une relation</strong> : mauvaises réactions en dispute, manque d’écoute, paroles blessantes, attitudes qui créent de la distance… Chaque erreur est expliquée avec une solution claire pour l’éviter et préserver une relation plus saine et stable.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- GUARANTEE SECTION -->
    <section class="guarantee-section-eloquence">
        <div class="container">
            <div class="guarantee-grid-layout">
                <div class="guarantee-mockup-side">
                    {svg_guarantee_bundle}
                </div>
                <div class="guarantee-text-side">
                    <h2>Méthode Simple & Concrète</h2>
                    <p>
                        Ce guide te donne une méthode simple pour gérer les conflits avec plus de calme et de contrôle, communiquer de manière plus claire et réparer la connexion après une tension.
                    </p>
                    <p>
                        La stabilité du couple ne dépend plus du hasard : elle devient le résultat de tes actions et de ta compréhension.
                    </p>
                    <p class="guarantee-closing">
                        Tu ne réagis plus au hasard. Tu comprends et tu maîtrises.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- PRICING SECTION -->
    <section class="pricing-section" id="commander">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Tout ce que tu vas trouver à l’intérieur :</h2>
                <p class="section-subtitle">Obtiens le guide complet et les bonus offerts aujourd'hui.</p>
            </div>

            <div class="pricing-box">
                <div class="pricing-header">
                    <h3>RÉCAPITULATIF DE TON PACK</h3>
                    <p>Accès numérique direct après paiement</p>
                </div>

                <div class="pricing-body">
                    <ul class="stack-list">
                        <li class="stack-item">
                            <span>📘 Guide complet : Résolution des crises de couple</span>
                            <span class="item-val">15,5 € / 9 900 FCFA</span>
                        </li>
                        <li class="stack-item">
                            <span>🎁 Bonus 1 : 10 phrases pour désamorcer un conflit</span>
                            <span class="item-val">10 € / 6 387 FCFA</span>
                        </li>
                        <li class="stack-item">
                            <span>🎁 Bonus 2 : Les 12 erreurs qui détruisent un couple</span>
                            <span class="item-val">12 € / 7 664 FCFA</span>
                        </li>
                        <li class="stack-item" style="font-weight: 800; background: #fdf4ff; padding: 14px;">
                            <span>💎 Valeur totale :</span>
                            <span style="text-decoration: line-through; color: #64748b;">52 € / 34 320 FCFA</span>
                        </li>
                    </ul>

                    <div class="price-total-box">
                        <div class="old-price">Valeur normale : 19 900 FCFA</div>
                        <div class="new-price">9 900 <small>FCFA</small></div>
                        <p style="color: var(--purple-primary); font-weight: 900; font-size: 1.05rem;">
                            🔥 DISPONIBLE AUJOURD'HUI SEULEMENT POUR 9 900 FCFA (~15,5 €)
                        </p>
                    </div>

                    <div class="payment-methods">
                        <!-- Mobile Money CTA -->
                        <a href="https://doraelysiane.com/prd_eqioqv/checkout" class="btn-eloquence">
                            <span>Payer maintenant par Wave, MTN, Orange, Moov</span>
                            <span class="btn-subtext">Paiement Mobile Money (9 900 FCFA)</span>
                        </a>

                        <!-- Card CTA -->
                        <a href="https://doraelysiane.com/prd_eqioqv/checkout" class="btn-eloquence" style="background: linear-gradient(135deg, #1e1030, #0f0716); margin-top: 10px;">
                            <span>Payer par Carte Bancaire</span>
                            <span class="btn-subtext">Paiement 100% Sécurisé (9 900 FCFA)</span>
                        </a>
                    </div>

                    <div style="text-align: center; margin-top: 24px; color: var(--text-muted); font-size: 0.9rem; display:flex; justify-content:center; gap:20px;">
                        <span><i class="fa-solid fa-lock text-purple"></i> Cryptage SSL 256-bit</span>
                        <span><i class="fa-solid fa-bolt text-purple"></i> Téléchargement Direct</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Ils étaient dans la même situation que toi :</h2>
                <p class="section-subtitle">Découvre les retours d'expériences de ceux qui ont suivi le guide.</p>
            </div>

            <div class="testimonials-grid">
                <!-- Client 1 -->
                <div class="testimonial-card">
                    <div>
                        <div class="stars">
                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                        </div>
                        <p class="testimonial-quote">
                            “On se disputait souvent pour rien, et ça finissait toujours mal. Grâce au guide, j’ai appris à mieux communiquer et à calmer les tensions. Aujourd’hui, on arrive à se comprendre sans s’énerver.”
                        </p>
                    </div>
                    <div class="client-info">
                        <div class="client-avatar">A</div>
                        <div class="client-details">
                            <h4>Alex, 42 ans</h4>
                            <span>Paris, France</span>
                        </div>
                    </div>
                </div>

                <!-- Client 2 -->
                <div class="testimonial-card">
                    <div>
                        <div class="stars">
                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                        </div>
                        <p class="testimonial-quote">
                            “Je pensais que notre relation était foutue… mais ce guide m’a ouvert les yeux sur mes erreurs. En appliquant les conseils, j’ai réussi à recréer une vraie connexion. Franchement, ça fait la différence.”
                        </p>
                    </div>
                    <div class="client-info">
                        <div class="client-avatar" style="background:#0284c7;">K</div>
                        <div class="client-details">
                            <h4>Kevin, 32 ans</h4>
                            <span>Kinshasa, RDC</span>
                        </div>
                    </div>
                </div>

                <!-- Client 3 -->
                <div class="testimonial-card">
                    <div>
                        <div class="stars">
                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                        </div>
                        <p class="testimonial-quote">
                            “Je ne savais jamais quoi dire pendant les conflits, j’empirais souvent la situation. Les techniques m’ont vraiment aidé à garder mon calme et à gérer les discussions intelligemment. Ça a changé l’ambiance dans mon couple.”
                        </p>
                    </div>
                    <div class="client-info">
                        <div class="client-avatar" style="background:#10b981;">B</div>
                        <div class="client-details">
                            <h4>Bernard, 37 ans</h4>
                            <span>Bruxelles, Belgique</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Author Section -->
    <section class="author-section">
        <div class="container">
            <div class="author-grid-brand">
                <div class="author-brand-emblem">
                    <div class="author-monogram">DÉ</div>
                    <h3 style="font-size:1.3rem; color:#fff; font-family:'Outfit';">DORA ÉLYSIANE</h3>
                    <p style="font-size:0.85rem; color:#c084fc; margin-top:4px;">ACCOMPAGNEMENT & DÉVELOPPEMENT PERSONNEL</p>
                </div>

                <div>
                    <h2 class="section-title" style="text-align:left; margin-bottom:20px;">Qui est Dora Élysiane ?</h2>
                    <p style="font-size:1.1rem; color:#334155; margin-bottom:16px;">
                        Je m’appelle <strong>Dora Élysiane</strong>, et depuis plusieurs années j’aide des jeunes, des hommes et des femmes à reprendre confiance en eux, à mieux gérer leurs émotions et à transformer leur vie affective et personnelle.
                    </p>
                    <p style="font-size:1.05rem; color:#64748b; margin-bottom:16px;">
                        J’ai créé mes guides pour une raison simple : j’ai vu trop de personnes souffrir en silence, manquer d’outils, de repères et de conseils clairs pour avancer réellement.
                    </p>
                    <p style="font-size:1.05rem; color:#64748b; margin-bottom:24px;">
                        Mon objectif est toujours le même : donner des solutions simples, vraies et efficaces, que tu peux appliquer dès aujourd’hui.
                    </p>
                    
                    <div style="display:flex; gap:30px;">
                        <div>
                            <h3 style="color:var(--purple-primary); font-size:1.8rem;">+5 ANS</h3>
                            <p style="color:var(--text-muted); font-size:0.9rem;">D'Expérience</p>
                        </div>
                        <div>
                            <h3 style="color:var(--purple-primary); font-size:1.8rem;">+5 000</h3>
                            <p style="color:var(--text-muted); font-size:0.9rem;">Lecteurs Satisfaits</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Les questions qui me viennent d'habitude sont maintenant là.</h2>
                <p class="section-subtitle">Réponses aux questions les plus fréquentes :</p>
            </div>

            <div class="faq-accordion">
                <div class="faq-item">
                    <div class="faq-question">
                        <span>1. Ce guide peut-il vraiment aider à améliorer une relation ?</span>
                        <i class="fa-solid fa-chevron-down faq-icon"></i>
                    </div>
                    <div class="faq-answer">
                        Oui. Il propose des méthodes simples et concrètes pour mieux communiquer, éviter les conflits inutiles et rétablir une relation plus saine.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>2. Est-ce que ça fonctionne même si la relation est déjà tendue ?</span>
                        <i class="fa-solid fa-chevron-down faq-icon"></i>
                    </div>
                    <div class="faq-answer">
                        Oui. Les conseils sont pensés pour les situations réelles, même quand il y a déjà des tensions ou une distance installée.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>3. Est-ce que je dois tout changer dans mon comportement ?</span>
                        <i class="fa-solid fa-chevron-down faq-icon"></i>
                    </div>
                    <div class="faq-answer">
                        Non. Le guide t’aide à ajuster certaines réactions et à mieux comprendre les situations, sans changer qui tu es.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>4. Combien de temps avant de voir des résultats ?</span>
                        <i class="fa-solid fa-chevron-down faq-icon"></i>
                    </div>
                    <div class="faq-answer">
                        Tu peux remarquer des améliorations dès les premières discussions si tu appliques les méthodes. Les résultats dépendent de ta régularité.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer style="background:#09030e; color:#94a3b8; padding:50px 0; text-align:center; border-top:1px solid rgba(168,85,247,0.2);">
        <div class="container">
            <p style="margin-bottom:16px;">
                <a href="#" style="color:#cbd5e1; text-decoration:none; margin:0 10px;">Mentions légales</a> | 
                <a href="#" style="color:#cbd5e1; text-decoration:none; margin:0 10px;">Conditions Générales de Vente</a> | 
                <a href="#" style="color:#cbd5e1; text-decoration:none; margin:0 10px;">Politique de Confidentialité</a>
            </p>
            <p style="font-size:0.9rem;">Copyright © 2026 - Dora Élysiane - Tous droits réservés.</p>
        </div>
    </footer>

    <!-- Mobile Sticky CTA Bar -->
    <div class="mobile-sticky-bar">
        <a href="#commander" class="btn-eloquence" style="padding:12px 20px; font-size:1rem;">
            <span>OBTENIR MAINTENANT (9 900 FCFA)</span>
        </a>
    </div>

    <!-- JavaScript Interactions -->
    <script>
        // FAQ Accordion Toggle
        document.querySelectorAll('.faq-question').forEach(question => {{
            question.addEventListener('click', () => {{
                const faqItem = question.parentElement;
                faqItem.classList.toggle('active');
            }});
        }});

        // Countdown Timer Logic
        function startTimer(durationInSeconds, displayElements) {{
            let timer = durationInSeconds;
            setInterval(() => {{
                let hours = parseInt(timer / 3600, 10);
                let minutes = parseInt((timer % 3600) / 60, 10);
                let seconds = parseInt(timer % 60, 10);

                hours = hours < 10 ? '0' + hours : hours;
                minutes = minutes < 10 ? '0' + minutes : minutes;
                seconds = seconds < 10 ? '0' + seconds : seconds;

                displayElements.forEach(el => {{
                    if(el) el.textContent = hours + ':' + minutes + ':' + seconds;
                }});

                if (--timer < 0) {{
                    timer = durationInSeconds;
                }}
            }}, 1000);
        }}

        window.onload = function () {{
            const topTimer = document.getElementById('top-timer');
            startTimer(81918, [topTimer]);
        }};
    </script>
</body>
</html>
'''

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated clean landing page with strictly user info and purple theme successfully.')
