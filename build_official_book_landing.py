import os
import base64

output_dir = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing'
os.makedirs(output_dir, exist_ok=True)
html_file = os.path.join(output_dir, 'index.html')

book_img_path = r'C:\Users\HP TTS\.gemini\antigravity\brain\f7c99c96-882b-4d26-9e07-2efd257a1816\.user_uploaded\media__1789510600647.png'

with open(book_img_path, 'rb') as f:
    b64_book = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

def make_hero_bundle_svg(book_img):
    return f'''<div class="hero-bundle-container">
        <div class="glow-sphere"></div>
        <div class="bundle-flex-layout">
            <!-- Left Laptop -->
            <div class="laptop-mockup-wrapper left-lap">
                <div class="laptop-screen">
                    <div class="lap-header">SAUVER TON COUPLE</div>
                    <div class="lap-body">
                        <i class="fa-solid fa-book-open-reader" style="font-size:2.5rem; color:#d4af37; margin-bottom:10px;"></i>
                        <p style="color:#fff; font-weight:700; font-size:0.9rem;">ACCÈS NUMÉRIQUE SÉCURISÉ</p>
                        <p style="color:#f472b6; font-size:0.75rem;">9 Chapitres + 2 Bonus PDF</p>
                    </div>
                </div>
                <div class="laptop-base"></div>
            </div>

            <!-- Main Official 3D Book Cover Centerpiece -->
            <div class="official-book-centerpiece">
                <span class="center-badge">GUIDE OFFICIEL</span>
                <img src="{book_img}" alt="Sauver Ton Couple par Dora Élysiane" class="book-img-3d">
            </div>

            <!-- Right Laptop -->
            <div class="laptop-mockup-wrapper right-lap">
                <div class="laptop-screen">
                    <div class="lap-header" style="background:#d4af37; color:#000;">DORA ÉLYSIANE</div>
                    <div class="lap-body">
                        <i class="fa-solid fa-shield-heart" style="font-size:2.5rem; color:#f472b6; margin-bottom:10px;"></i>
                        <p style="color:#fff; font-weight:700; font-size:0.9rem;">HOMME MODERNE</p>
                        <p style="color:#d4af37; font-size:0.75rem;">Plan d'Action Complet</p>
                    </div>
                </div>
                <div class="laptop-base"></div>
            </div>
        </div>
    </div>'''

def make_module_mockup(book_img, num):
    return f'''<div class="module-mockup-circle-wrapper">
        <div class="module-circle-glow"></div>
        <div class="module-book-stack">
            <img src="{book_img}" alt="Chapitre {num}" class="module-book-img">
            <div class="module-mini-badge">CHAPITRE {num}</div>
        </div>
    </div>'''

html_content = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sauver Ton Couple | Guide de résolution des crises pour l'homme moderne - Dora Élysiane</title>
    <meta name="description" content="Le guide honnête que tu aurais voulu avoir avant la première dispute. Par Dora Élysiane.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {{
            --burgundy-primary: #5c1d30;
            --burgundy-dark: #360e1a;
            --burgundy-light: #7a223c;
            --gold-accent: #d4af37;
            --gold-light: #f5e08c;
            --pink-accent: #f472b6;
            --burgundy-gradient: linear-gradient(135deg, #7a223c 0%, #5c1d30 50%, #360e1a 100%);
            --burgundy-hover: linear-gradient(135deg, #421121 0%, #280812 100%);
            --dark-bg: #14050a;
            --dark-surface: #1f0810;
            --dark-card: #2b0c16;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --border-radius: 16px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --shadow-sm: 0 4px 6px -1px rgba(0,0,0,0.05);
            --shadow-md: 0 10px 30px -5px rgba(92, 29, 48, 0.15);
            --shadow-lg: 0 20px 40px -15px rgba(92, 29, 48, 0.35);
            --gold-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
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
        .text-gold {{ color: var(--gold-accent); }}
        .text-pink {{ color: var(--pink-accent); }}

        /* Top Bar Urgency */
        .announcement-bar {{
            background: var(--burgundy-gradient);
            border-bottom: 2px solid var(--gold-accent);
            color: #ffffff;
            text-align: center;
            padding: 12px 15px;
            font-size: 0.95rem;
            font-weight: 700;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 12px rgba(92, 29, 48, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .announcement-bar .timer-badge {{
            background: rgba(0,0,0,0.4);
            padding: 4px 14px;
            border-radius: 20px;
            border: 1px solid var(--gold-accent);
            font-family: monospace;
            font-size: 1.05rem;
            color: #fde047;
            font-weight: 800;
        }}

        /* Buttons matching Luxury Burgundy Gold */
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
            border: 2px solid var(--gold-accent);
            width: 100%;
            max-width: 680px;
            text-align: center;
            background: var(--burgundy-gradient);
            color: #ffffff;
            box-shadow: 0 15px 35px rgba(92, 29, 48, 0.5);
        }}

        .btn-eloquence:hover {{
            transform: translateY(-3px) scale(1.02);
            background: var(--burgundy-hover);
            box-shadow: 0 20px 45px rgba(212, 175, 55, 0.4);
        }}

        .btn-subtext {{
            font-size: 0.85rem;
            font-weight: 500;
            color: var(--gold-light);
            margin-top: 4px;
        }}

        /* Hero Section */
        .hero {{
            padding: 70px 0 90px;
            background: linear-gradient(180deg, #1f0810 0%, #0d0206 100%);
            color: #ffffff;
            position: relative;
            overflow: hidden;
        }}

        .hero-badge {{
            display: inline-block;
            background: rgba(212, 175, 55, 0.15);
            border: 1px solid var(--gold-accent);
            color: var(--gold-light);
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
            color: var(--pink-accent);
        }}

        .hero-subtitle {{
            font-size: 1.2rem;
            color: #cbd5e1;
            max-width: 860px;
            margin: 0 auto 36px;
            line-height: 1.6;
        }}

        /* 3D Hero Bundle Showcase Components */
        .hero-bundle-container {{
            position: relative;
            max-width: 950px;
            margin: 40px auto;
            padding: 40px 20px;
        }}

        .glow-sphere {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 360px;
            height: 360px;
            background: radial-gradient(circle, rgba(212, 175, 55, 0.8) 0%, rgba(92, 29, 48, 0.6) 60%, transparent 100%);
            border-radius: 50%;
            filter: blur(40px);
            z-index: 1;
        }}

        .bundle-flex-layout {{
            position: relative;
            z-index: 2;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
        }}

        .official-book-centerpiece {{
            position: relative;
            width: 260px;
            transition: var(--transition);
        }}

        .official-book-centerpiece:hover {{
            transform: translateY(-10px) scale(1.04);
        }}

        .book-img-3d {{
            width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.8), 0 0 30px rgba(212, 175, 55, 0.3);
        }}

        .center-badge {{
            position: absolute;
            top: -14px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--gold-accent);
            color: #000;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 0.75rem;
            padding: 4px 16px;
            border-radius: 20px;
            text-transform: uppercase;
            white-space: nowrap;
            box-shadow: var(--shadow-sm);
        }}

        /* 3D Laptop Component */
        .laptop-mockup-wrapper {{
            width: 240px;
            background: #1e293b;
            border-radius: 12px;
            padding: 10px;
            border: 2px solid #64748b;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            transform: perspective(600px) rotateY(15deg);
        }}

        .laptop-mockup-wrapper.right-lap {{
            transform: perspective(600px) rotateY(-15deg);
        }}

        .laptop-screen {{
            background: #0f172a;
            border-radius: 6px;
            overflow: hidden;
            height: 150px;
            display: flex;
            flex-direction: column;
        }}

        .lap-header {{
            background: var(--burgundy-primary);
            color: #ffffff;
            font-size: 0.75rem;
            font-weight: 800;
            padding: 6px;
            text-align: center;
        }}

        .lap-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 10px;
            text-align: center;
        }}

        .laptop-base {{
            height: 10px;
            background: #cbd5e1;
            border-radius: 0 0 8px 8px;
            margin-top: 6px;
        }}

        .hero-target-box {{
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(212, 175, 55, 0.3);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 22px 30px;
            max-width: 880px;
            margin: 0 auto 40px;
            font-size: 1.05rem;
            color: #e2e8f0;
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
            color: var(--burgundy-primary);
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
            background: #fffdfa;
            border-left: 6px solid var(--gold-accent);
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

        /* MODULE CARDS MATCHING SCREENSHOT 1 STRICTLY */
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
            border: 2px solid var(--burgundy-primary);
            border-top: 4px solid var(--gold-accent);
            border-radius: 16px;
            padding: 35px;
            box-shadow: 0 10px 30px rgba(92, 29, 48, 0.08);
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 40px;
            align-items: center;
        }}

        .module-mockup-circle-wrapper {{
            position: relative;
            width: 100%;
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .module-circle-glow {{
            position: absolute;
            width: 180px;
            height: 180px;
            background: radial-gradient(circle, var(--gold-accent) 0%, rgba(92, 29, 48, 0.5) 70%, transparent 100%);
            border-radius: 50%;
            filter: blur(15px);
        }}

        .module-book-stack {{
            position: relative;
            z-index: 2;
            width: 170px;
            text-align: center;
        }}

        .module-book-img {{
            width: 100%;
            border-radius: 6px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.5);
        }}

        .module-mini-badge {{
            background: var(--burgundy-primary);
            color: #fff;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 10px;
            display: inline-block;
            margin-top: 8px;
            border: 1px solid var(--gold-accent);
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

        .gold-arrow-icon {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 24px;
            height: 24px;
            background: var(--gold-accent);
            color: #000000;
            border-radius: 50%;
            font-size: 0.8rem;
            font-weight: 900;
            flex-shrink: 0;
            margin-top: 2px;
        }}

        /* BONUS CARDS MATCHING SCREENSHOT 4 STRICTLY */
        .bonus-section {{
            padding: 90px 0;
            background: var(--dark-bg);
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
            background: var(--dark-surface);
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid var(--gold-accent);
            box-shadow: 0 20px 40px rgba(0,0,0,0.8);
        }}

        .bonus-header-banner {{
            background: var(--burgundy-gradient);
            border-bottom: 2px solid var(--gold-accent);
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
            color: var(--gold-light);
        }}

        .bonus-body-content {{
            padding: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }}

        .bonus-mockup-center {{
            max-width: 320px;
            width: 100%;
            margin-bottom: 24px;
        }}

        .bonus-text-desc {{
            font-size: 1.15rem;
            color: #e2e8f0;
            line-height: 1.7;
            max-width: 800px;
        }}

        /* GUARANTEE SECTION MATCHING SCREENSHOT 2 STRICTLY */
        .guarantee-section-eloquence {{
            padding: 90px 0;
            background: linear-gradient(180deg, #1f0810 0%, #0a0205 100%);
            color: #ffffff;
        }}

        .guarantee-grid-layout {{
            display: grid;
            grid-template-columns: 360px 1fr;
            gap: 50px;
            align-items: center;
            max-width: 1000px;
            margin: 0 auto;
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
            color: var(--gold-light);
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
            border: 3px solid var(--burgundy-primary);
            border-radius: 24px;
            box-shadow: 0 25px 60px rgba(92, 29, 48, 0.2);
            overflow: hidden;
        }}

        .pricing-header {{
            background: var(--burgundy-gradient);
            border-bottom: 2px solid var(--gold-accent);
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
            color: var(--burgundy-primary);
        }}

        .price-total-box {{
            background: #fff8f0;
            border-radius: 16px;
            padding: 26px;
            text-align: center;
            margin-bottom: 30px;
            border: 2px dashed var(--gold-accent);
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
            color: var(--burgundy-primary);
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
            background: var(--burgundy-primary);
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
            background: linear-gradient(145deg, #1f0810 0%, #0d0206 100%);
            border: 2px solid var(--gold-accent);
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
            color: var(--gold-accent);
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
            background: #fff8f0;
            color: var(--burgundy-primary);
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
            color: var(--burgundy-primary);
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
            .laptop-mockup-wrapper {{ display: none; }}
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

            <!-- GIANT HERO BUNDLE SHOWCASE WITH OFFICIAL 3D BOOK COVER -->
            {make_hero_bundle_svg(b64_book)}

            <!-- CTA Button -->
            <a href="#commander" class="btn-eloquence">
                <span>Obtenir maintenant</span>
                <span class="btn-subtext">Accès Immédiat au Guide + 2 Bonus • Seulement 9 900 FCFA (~15,5 €)</span>
            </a>
            
            <p style="font-size: 0.92rem; color: #cbd5e1; margin-top: 16px;">
                <i class="fa-solid fa-lock text-gold"></i> Paiement 100% Sécurisé (Wave, Orange Money, MTN, Moov, Carte)
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
                    <h3><i class="fa-solid fa-circle-xmark text-pink"></i> 📌 Le problème</h3>
                    <ul class="compare-list">
                        <li>
                            <i class="fa-solid fa-xmark text-pink"></i>
                            <span>Au début, tout allait bien. Puis les tensions ont commencé à apparaître.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-pink"></i>
                            <span>Discussions qui tournent mal, silences lourds, distance émotionnelle.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-pink"></i>
                            <span>Tu ne sais pas quoi dire au bon moment quand la tension monte.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-pink"></i>
                            <span>Tu as peur d’aggraver la situation et tu te retrouves souvent incompris.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-pink"></i>
                            <span>Résultat : la connexion s’affaiblit, et la relation devient de plus en plus fragile.</span>
                        </li>
                    </ul>
                </div>

                <!-- Solution Card -->
                <div class="compare-card solution">
                    <h3><i class="fa-solid fa-circle-check text-gold"></i> ✅ La solution : un guide clair et structuré</h3>
                    <ul class="compare-list">
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Gérer les conflits avec plus de calme et de contrôle.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Communiquer de manière plus claire et efficace sans tension.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Comprendre ce qui se joue réellement dans une dispute.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Réparer la connexion après une tension et réinstaurer le respect.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Tu ne réagis plus au hasard : tu comprends et tu maîtrises.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- MODULES / CHAPTERS SECTION WITH OFFICIAL 3D BOOK MOCKUP -->
    <section class="curriculum-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">📘 Ce que contient le guide</h2>
                <p class="section-subtitle">Découvre les 9 chapitres conçus pour l'homme moderne :</p>
            </div>

            <div class="modules-list">
                
                <!-- CHAPITRE 1 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 1)}
                    <div class="module-info-side">
                        <h3>Chapitre 1 : Le Diagnostic de l'Ombre</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Pourquoi tu as l'impression de n'être qu'un portefeuille ?</li>
                            <li><span class="gold-arrow-icon">➔</span> Analyser la perte de connexion émotionnelle dans le couple</li>
                            <li><span class="gold-arrow-icon">➔</span> Comprendre les causes profondes des tensions accumulées</li>
                            <li><span class="gold-arrow-icon">➔</span> Identifier les signaux d'alerte avant qu'il ne soit trop tard</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 2 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 2)}
                    <div class="module-info-side">
                        <h3>Chapitre 2 : Le Miroir de l'Homme</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Avant de la changer elle, regarde-toi</li>
                            <li><span class="gold-arrow-icon">➔</span> Retrouver sa confiance en soi et son leadership personnel</li>
                            <li><span class="gold-arrow-icon">➔</span> Ajuster certaines réactions sans changer qui tu es</li>
                            <li><span class="gold-arrow-icon">➔</span> Agir avec plus de calme, de maîtrise et de maturité émotionnelle</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 3 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 3)}
                    <div class="module-info-side">
                        <h3>Chapitre 3 : L'Art de se faire respecter (Sans crier)</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Comment réagir face au mépris ou à la comparaison</li>
                            <li><span class="gold-arrow-icon">➔</span> Réagir sans entrer dans la violence ou le silence boudeur</li>
                            <li><span class="gold-arrow-icon">➔</span> Fixer des limites claires et poser le respect naturellement</li>
                            <li><span class="gold-arrow-icon">➔</span> Garder son sang-froid dans les moments les plus tendus</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 4 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 4)}
                    <div class="module-info-side">
                        <h3>Chapitre 4 : Le Lit Froid – Briser la Grève de l'Intimité</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Comprendre le désir féminin et ses mécanismes</li>
                            <li><span class="gold-arrow-icon">➔</span> Reconnecter physiquement sans mendier l'attention</li>
                            <li><span class="gold-arrow-icon">➔</span> Retrouver une complicité chaleureuse et naturelle</li>
                            <li><span class="gold-arrow-icon">➔</span> Rétablir la passion et le rapprochement corporel</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 5 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 5)}
                    <div class="module-info-side">
                        <h3>Chapitre 5 : La Communication "Haute Tension"</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Comment parler de tes besoins sans que ça finisse en dispute</li>
                            <li><span class="gold-arrow-icon">➔</span> Apprendre l'écoute active et l'affirmation de soi</li>
                            <li><span class="gold-arrow-icon">➔</span> Désamorcer une discussion explosive avant l'escalade</li>
                            <li><span class="gold-arrow-icon">➔</span> Rendre les échanges plus clairs et efficaces</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 6 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 6)}
                    <div class="module-info-side">
                        <h3>Chapitre 6 : Gérer la "Tribu" (Famille et Belle-famille)</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Mettre des frontières saines entre ton foyer et les influences extérieures</li>
                            <li><span class="gold-arrow-icon">➔</span> Gérer les pressions de la belle-famille sans créer de rancœur</li>
                            <li><span class="gold-arrow-icon">➔</span> Protéger l'intimité et les décisions du couple</li>
                            <li><span class="gold-arrow-icon">➔</span> Maintenir l'unité et la solidarité dans le foyer</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 7 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 7)}
                    <div class="module-info-side">
                        <h3>Chapitre 7 : Transformer la frustration en force</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Gérer sa propre colère et sa solitude émotionnelle</li>
                            <li><span class="gold-arrow-icon">➔</span> Trouver ses propres soutiens et piliers d'équilibre</li>
                            <li><span class="gold-arrow-icon">➔</span> Transformer les moments difficiles en moteur d'évolution</li>
                            <li><span class="gold-arrow-icon">➔</span> Conserver sa sérénité en toutes circonstances</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 8 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 8)}
                    <div class="module-info-side">
                        <h3>Chapitre 8 : Le Plan d'Action sur 30 jours</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> Des exercices concrets et quotidiens</li>
                            <li><span class="gold-arrow-icon">➔</span> Changer progressivement l'atmosphère de la maison</li>
                            <li><span class="gold-arrow-icon">➔</span> Mettre en pratique les conseils jour après jour</li>
                            <li><span class="gold-arrow-icon">➔</span> Obtenir des améliorations durables et perceptibles</li>
                        </ul>
                    </div>
                </div>

                <!-- CHAPITRE 9 -->
                <div class="module-card-eloquence">
                    {make_module_mockup(b64_book, 9)}
                    <div class="module-info-side">
                        <h3>Chapitre 9 : Quand est-il temps de partir ?</h3>
                        <ul class="module-bullets">
                            <li><span class="gold-arrow-icon">➔</span> La sagesse de savoir si le combat en vaut encore la peine</li>
                            <li><span class="gold-arrow-icon">➔</span> Évaluer la situation avec lucidité et sérénité</li>
                            <li><span class="gold-arrow-icon">➔</span> Prendre les bonnes décisions pour son avenir</li>
                            <li><span class="gold-arrow-icon">➔</span> Préserver son respect et sa dignité</li>
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
                            <img src="{b64_book}" alt="Bonus 1" style="max-width:200px; border-radius:8px; box-shadow:0 15px 30px rgba(0,0,0,0.6);">
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
                            <img src="{b64_book}" alt="Bonus 2" style="max-width:200px; border-radius:8px; box-shadow:0 15px 30px rgba(0,0,0,0.6);">
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
                <div class="guarantee-mockup-side text-center">
                    <img src="{b64_book}" alt="Garantie Sauver ton couple" style="max-width:220px; border-radius:8px; box-shadow:0 20px 40px rgba(0,0,0,0.7);">
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
                        <li class="stack-item" style="font-weight: 800; background: #fff8f0; padding: 14px;">
                            <span>💎 Valeur totale :</span>
                            <span style="text-decoration: line-through; color: #64748b;">52 € / 34 320 FCFA</span>
                        </li>
                    </ul>

                    <div class="price-total-box">
                        <div class="old-price">Valeur normale : 19 900 FCFA</div>
                        <div class="new-price">9 900 <small>FCFA</small></div>
                        <p style="color: var(--burgundy-primary); font-weight: 900; font-size: 1.05rem;">
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
                        <a href="https://doraelysiane.com/prd_eqioqv/checkout" class="btn-eloquence" style="background: linear-gradient(135deg, #1f0810, #0d0206); margin-top: 10px;">
                            <span>Payer par Carte Bancaire</span>
                            <span class="btn-subtext">Paiement 100% Sécurisé (9 900 FCFA)</span>
                        </a>
                    </div>

                    <div style="text-align: center; margin-top: 24px; color: var(--text-muted); font-size: 0.9rem; display:flex; justify-content:center; gap:20px;">
                        <span><i class="fa-solid fa-lock text-gold"></i> Cryptage SSL 256-bit</span>
                        <span><i class="fa-solid fa-bolt text-gold"></i> Téléchargement Direct</span>
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
                    <p style="font-size:0.85rem; color:var(--gold-accent); margin-top:4px;">ACCOMPAGNEMENT & DÉVELOPPEMENT PERSONAL</p>
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
                            <h3 style="color:var(--burgundy-primary); font-size:1.8rem;">+5 ANS</h3>
                            <p style="color:var(--text-muted); font-size:0.9rem;">D'Expérience</p>
                        </div>
                        <div>
                            <h3 style="color:var(--burgundy-primary); font-size:1.8rem;">+5 000</h3>
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
    <footer style="background:#14050a; color:#94a3b8; padding:50px 0; text-align:center; border-top:1px solid rgba(212,175,55,0.3);">
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

print('Generated landing page with official 3D book cover successfully.')
