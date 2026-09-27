import os

output_dir = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing'
os.makedirs(output_dir, exist_ok=True)
html_file = os.path.join(output_dir, 'index.html')

html_content = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAUVER SON COUPLE 2.0 | Le Programme Utile pour l'Homme Moderne</title>
    <meta name="description" content="Le programme complet et structuré de résolution des crises de couple. Maîtrisez la communication, apaiser les tensions et rétablissez l'intimité en moins de 30 jours.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {
            --primary: #852310;
            --primary-hover: #691a0b;
            --primary-light: #a32d16;
            --secondary: #d4af37;
            --secondary-light: #f3e5ab;
            --dark-bg: #0b0f19;
            --dark-surface: #151c2e;
            --dark-card: #1e293b;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --text-light: #f8fafc;
            --accent-green: #10b981;
            --accent-red: #ef4444;
            --border-radius: 16px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --shadow-sm: 0 4px 6px -1px rgba(0,0,0,0.05);
            --shadow-md: 0 10px 25px -5px rgba(0,0,0,0.1);
            --shadow-lg: 0 20px 40px -15px rgba(133, 35, 16, 0.2);
            --shadow-glow: 0 0 35px rgba(212, 175, 55, 0.35);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
            font-family: 'Inter', sans-serif;
            color: var(--text-dark);
            background-color: #f8fafc;
            line-height: 1.6;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            line-height: 1.2;
        }

        /* Utility Classes */
        .container {
            max-width: 1160px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .text-center { text-align: center; }
        .text-primary { color: var(--primary); }
        .text-gold { color: var(--secondary); }
        .bg-dark { background-color: var(--dark-bg); color: var(--text-light); }
        .bg-surface { background-color: var(--dark-surface); color: var(--text-light); }
        .bg-light { background-color: #ffffff; }

        /* Top Bar Urgency */
        .announcement-bar {
            background: linear-gradient(90deg, #73140c 0%, #a32d16 50%, #73140c 100%);
            color: #ffffff;
            text-align: center;
            padding: 12px 15px;
            font-size: 0.95rem;
            font-weight: 600;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .announcement-bar .timer-badge {
            background: rgba(0,0,0,0.4);
            padding: 4px 14px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.25);
            font-family: monospace;
            font-size: 1.05rem;
            color: #fde047;
            font-weight: 700;
        }

        /* Buttons */
        .btn {
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 18px 38px;
            border-radius: 50px;
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 800;
            text-decoration: none;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            width: 100%;
            max-width: 580px;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary) 0%, #b83218 100%);
            color: #ffffff;
            border: 1px solid rgba(255,255,255,0.2);
        }

        .btn-primary:hover {
            transform: translateY(-3px) scale(1.02);
            background: linear-gradient(135deg, #691a0b 0%, var(--primary) 100%);
            box-shadow: 0 18px 40px rgba(133, 35, 16, 0.45);
        }

        .btn-gold {
            background: linear-gradient(135deg, #d4af37 0%, #f5d061 100%);
            color: #0f172a;
        }

        .btn-gold:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 18px 40px rgba(212, 175, 55, 0.45);
        }

        .btn-subtext {
            font-size: 0.85rem;
            font-weight: 400;
            opacity: 0.9;
            margin-top: 3px;
        }

        /* Hero Section */
        .hero {
            padding: 60px 0 90px;
            background: radial-gradient(circle at 50% 20%, #1a233a 0%, #0b0f19 100%);
            color: #ffffff;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: -100px;
            right: -100px;
            width: 450px;
            height: 450px;
            background: rgba(133, 35, 16, 0.18);
            filter: blur(120px);
            border-radius: 50%;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(212, 175, 55, 0.15);
            border: 1px solid rgba(212, 175, 55, 0.4);
            color: var(--secondary-light);
            padding: 8px 22px;
            border-radius: 30px;
            font-size: 0.9rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 24px;
        }

        .hero-title {
            font-size: 3.2rem;
            line-height: 1.15;
            margin-bottom: 24px;
            color: #ffffff;
        }

        .hero-title span {
            background: linear-gradient(135deg, #f87171 0%, #ef4444 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-subtitle {
            font-size: 1.25rem;
            color: #94a3b8;
            max-width: 840px;
            margin: 0 auto 36px;
        }

        .hero-target-box {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 20px 30px;
            max-width: 860px;
            margin: 0 auto 40px;
            font-size: 1.05rem;
            color: #cbd5e1;
        }

        .hero-target-box strong {
            color: #ffffff;
        }

        /* Giant Hero Bundle Mockup Showcase */
        .hero-bundle-showcase {
            position: relative;
            max-width: 1000px;
            margin: 50px auto 60px;
            padding: 40px 20px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(212, 175, 55, 0.25);
            border-radius: 24px;
            backdrop-filter: blur(15px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.6);
        }

        .hero-bundle-badge {
            position: absolute;
            top: -16px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, #d4af37, #f5d061);
            color: #000000;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 0.85rem;
            padding: 6px 24px;
            border-radius: 30px;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: var(--shadow-glow);
        }

        .bundle-grid-display {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        /* 3D Mockup E-Book Card Component */
        .mockup-book {
            width: 160px;
            height: 220px;
            border-radius: 12px;
            padding: 16px 12px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            box-shadow: 0 15px 30px rgba(0,0,0,0.5), inset 3px 0 6px rgba(255,255,255,0.2);
            transition: var(--transition);
            border: 1px solid rgba(255,255,255,0.15);
            overflow: hidden;
            text-align: center;
            user-select: none;
        }

        .mockup-book::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 8px;
            height: 100%;
            background: rgba(0,0,0,0.3);
            border-right: 1px solid rgba(255,255,255,0.1);
        }

        .mockup-book:hover {
            transform: translateY(-8px) scale(1.06);
            box-shadow: 0 22px 45px rgba(0,0,0,0.7);
        }

        .mockup-book.main-pack {
            width: 220px;
            height: 290px;
            border: 2px solid var(--secondary);
            box-shadow: 0 25px 55px rgba(133, 35, 16, 0.6), 0 0 25px rgba(212, 175, 55, 0.3);
            z-index: 5;
        }

        .mockup-book-badge {
            font-size: 0.65rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 10px;
            text-transform: uppercase;
            align-self: center;
            letter-spacing: 0.5px;
        }

        .mockup-book-icon {
            font-size: 2.2rem;
            margin: 10px 0;
        }

        .mockup-book-title {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.88rem;
            line-height: 1.25;
            color: #ffffff;
        }

        .mockup-book-sub {
            font-size: 0.7rem;
            opacity: 0.85;
            margin-top: 4px;
        }

        /* Specific Color Themes for Mockups */
        .m-theme-main { background: linear-gradient(145deg, #a32d16 0%, #4a0d05 100%); color: #fff; }
        .m-theme-ch1 { background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%); color: #f87171; }
        .m-theme-ch2 { background: linear-gradient(145deg, #1e3a8a 0%, #0f172a 100%); color: #60a5fa; }
        .m-theme-ch3 { background: linear-gradient(145deg, #581c87 0%, #2e1065 100%); color: #c084fc; }
        .m-theme-ch4 { background: linear-gradient(145deg, #9f1239 0%, #4c0519 100%); color: #fda4af; }
        .m-theme-ch5 { background: linear-gradient(145deg, #78350f 0%, #451a03 100%); color: #fcd34d; }
        .m-theme-ch6 { background: linear-gradient(145deg, #064e3b 0%, #022c22 100%); color: #6ee7b7; }
        .m-theme-ch7 { background: linear-gradient(145deg, #172554 0%, #090d16 100%); color: #93c5fd; }
        .m-theme-ch8 { background: linear-gradient(145deg, #155e75 0%, #083344 100%); color: #67e8f9; }
        .m-theme-ch9 { background: linear-gradient(145deg, #334155 0%, #0f172a 100%); color: #cbd5e1; }
        .m-theme-b1  { background: linear-gradient(145deg, #854d0e 0%, #422006 100%); color: #fef08a; border: 1px solid #d4af37; }
        .m-theme-b2  { background: linear-gradient(145deg, #881337 0%, #4c0519 100%); color: #fecdd3; border: 1px solid #ef4444; }

        /* Social Proof Bar */
        .proof-bar {
            background: #ffffff;
            padding: 30px 0;
            border-bottom: 1px solid #e2e8f0;
            box-shadow: var(--shadow-sm);
        }

        .proof-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
            text-align: center;
        }

        .proof-item h3 {
            font-size: 2.2rem;
            color: var(--primary);
            margin-bottom: 4px;
        }

        .proof-item p {
            color: var(--text-muted);
            font-size: 0.95rem;
            font-weight: 500;
        }

        /* Problem & Transformation Section */
        .transformation-section {
            padding: 90px 0;
            background: #ffffff;
        }

        .section-header {
            text-align: center;
            max-width: 820px;
            margin: 0 auto 60px;
        }

        .section-title {
            font-size: 2.4rem;
            color: var(--text-dark);
            margin-bottom: 16px;
        }

        .section-subtitle {
            font-size: 1.15rem;
            color: var(--text-muted);
        }

        .compare-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-top: 40px;
        }

        .compare-card {
            border-radius: var(--border-radius);
            padding: 40px;
            box-shadow: var(--shadow-md);
        }

        .compare-card.problem {
            background: #fff5f5;
            border-left: 6px solid var(--accent-red);
        }

        .compare-card.solution {
            background: #f0fdf4;
            border-left: 6px solid var(--accent-green);
        }

        .compare-card h3 {
            font-size: 1.6rem;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .compare-list {
            list-style: none;
        }

        .compare-list li {
            padding: 12px 0;
            border-bottom: 1px dashed rgba(0,0,0,0.08);
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 1.05rem;
        }

        .compare-list li:last-child {
            border-bottom: none;
        }

        .compare-list i {
            margin-top: 4px;
            font-size: 1.2rem;
        }

        /* Curriculum Chapters with Mockups */
        .curriculum-section {
            padding: 90px 0;
            background: #f8fafc;
        }

        .chapters-grid-mockups {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }

        .chapter-card-mockup {
            background: #ffffff;
            border-radius: 20px;
            padding: 30px;
            border: 1px solid #e2e8f0;
            box-shadow: var(--shadow-sm);
            transition: var(--transition);
            display: flex;
            gap: 20px;
            align-items: center;
        }

        .chapter-card-mockup:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
            border-color: var(--primary-light);
        }

        .chapter-content-side {
            flex: 1;
        }

        .chapter-num-badge {
            display: inline-block;
            background: var(--primary);
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 0.75rem;
            padding: 3px 12px;
            border-radius: 20px;
            margin-bottom: 10px;
        }

        .chapter-title-side {
            font-size: 1.2rem;
            color: var(--text-dark);
            margin-bottom: 8px;
        }

        .chapter-desc-side {
            color: var(--text-muted);
            font-size: 0.92rem;
            line-height: 1.5;
        }

        /* Bonus Section with Dedicated Mockups */
        .bonus-section {
            padding: 90px 0;
            background: linear-gradient(180deg, #0b0f19 0%, #151c2e 100%);
            color: #ffffff;
        }

        .bonus-grid-mockups {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 35px;
            margin-top: 50px;
        }

        .bonus-card-mockup {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(212, 175, 55, 0.35);
            border-radius: 24px;
            padding: 36px;
            display: flex;
            gap: 24px;
            align-items: center;
            backdrop-filter: blur(10px);
            position: relative;
        }

        .bonus-badge-tag {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(212, 175, 55, 0.2);
            color: var(--secondary-light);
            border: 1px solid var(--secondary);
            font-weight: 800;
            font-size: 0.8rem;
            padding: 4px 14px;
            border-radius: 20px;
        }

        .bonus-info-side {
            flex: 1;
        }

        .bonus-title-side {
            font-size: 1.35rem;
            color: #ffffff;
            margin-bottom: 12px;
            padding-right: 70px;
        }

        .bonus-desc-side {
            color: #cbd5e1;
            font-size: 1rem;
            line-height: 1.6;
        }

        /* Pricing & Value Stack */
        .pricing-section {
            padding: 100px 0;
            background: #ffffff;
        }

        .pricing-box {
            max-width: 820px;
            margin: 0 auto;
            background: #ffffff;
            border: 2px solid var(--primary);
            border-radius: 24px;
            box-shadow: 0 25px 60px rgba(133, 35, 16, 0.15);
            overflow: hidden;
            position: relative;
        }

        .pricing-header {
            background: linear-gradient(135deg, var(--primary) 0%, #691a0b 100%);
            color: #ffffff;
            padding: 30px;
            text-align: center;
        }

        .pricing-header h3 {
            font-size: 1.8rem;
            margin-bottom: 8px;
        }

        .pricing-body {
            padding: 40px;
        }

        .stack-list {
            list-style: none;
            margin-bottom: 30px;
        }

        .stack-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 0;
            border-bottom: 1px solid #f1f5f9;
            font-size: 1.05rem;
        }

        .stack-item span.item-val {
            font-weight: 700;
            color: var(--primary);
        }

        .price-total-box {
            background: #fff9f8;
            border-radius: 16px;
            padding: 24px;
            text-align: center;
            margin-bottom: 30px;
            border: 1px dashed var(--primary-light);
        }

        .old-price {
            font-size: 1.3rem;
            color: #94a3b8;
            text-decoration: line-through;
            margin-bottom: 4px;
        }

        .new-price {
            font-size: 3.2rem;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            color: var(--primary);
            line-height: 1;
            margin-bottom: 8px;
        }

        .new-price small {
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text-dark);
        }

        .payment-methods {
            display: flex;
            flex-direction: column;
            gap: 16px;
            align-items: center;
            margin-top: 30px;
        }

        /* Guarantee Box */
        .guarantee-box {
            background: #fffdf5;
            border: 2px solid var(--secondary);
            border-radius: 20px;
            padding: 40px;
            max-width: 860px;
            margin: 60px auto 0;
            display: flex;
            gap: 30px;
            align-items: center;
        }

        .guarantee-badge {
            width: 120px;
            height: 120px;
            flex-shrink: 0;
            background: linear-gradient(135deg, #d4af37, #f5d061);
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #000;
            text-align: center;
            box-shadow: var(--shadow-glow);
        }

        .guarantee-badge i {
            font-size: 2.2rem;
            margin-bottom: 4px;
        }

        .guarantee-badge span {
            font-size: 0.7rem;
            font-weight: 800;
            text-transform: uppercase;
        }

        /* Testimonials */
        .testimonials-section {
            padding: 90px 0;
            background: #f8fafc;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }

        .testimonial-card {
            background: #ffffff;
            border-radius: 16px;
            padding: 30px;
            box-shadow: var(--shadow-sm);
            border: 1px solid #e2e8f0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .stars {
            color: #f59e0b;
            margin-bottom: 14px;
            font-size: 1.1rem;
        }

        .testimonial-quote {
            font-style: italic;
            color: #334155;
            font-size: 1.02rem;
            margin-bottom: 20px;
        }

        .client-info {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .client-avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: var(--primary);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.1rem;
        }

        .client-details h4 {
            font-size: 1.05rem;
            color: var(--text-dark);
        }

        .client-details span {
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        /* Author Section without Photos (Vector Monogram Branding) */
        .author-section {
            padding: 100px 0;
            background: #ffffff;
        }

        .author-grid-brand {
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 50px;
            align-items: center;
        }

        .author-brand-emblem {
            width: 100%;
            height: 320px;
            background: linear-gradient(145deg, #0b0f19 0%, #1a233a 100%);
            border: 2px solid var(--secondary);
            border-radius: 24px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            box-shadow: var(--shadow-lg);
            text-align: center;
            padding: 30px;
        }

        .author-monogram {
            font-family: 'Outfit', sans-serif;
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(135deg, #d4af37 0%, #f5d061 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1;
            margin-bottom: 10px;
        }

        /* FAQ Accordion */
        .faq-section {
            padding: 90px 0;
            background: #f8fafc;
        }

        .faq-accordion {
            max-width: 800px;
            margin: 50px auto 0;
        }

        .faq-item {
            background: #ffffff;
            border-radius: 12px;
            margin-bottom: 16px;
            border: 1px solid #e2e8f0;
            overflow: hidden;
        }

        .faq-question {
            padding: 22px 28px;
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--text-dark);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: var(--transition);
        }

        .faq-question:hover {
            background: #f8fafc;
            color: var(--primary);
        }

        .faq-answer {
            padding: 0 28px 22px;
            color: var(--text-muted);
            font-size: 1.02rem;
            display: none;
            line-height: 1.6;
        }

        .faq-item.active .faq-answer {
            display: block;
        }

        .faq-item.active .faq-icon {
            transform: rotate(180deg);
            color: var(--primary);
        }

        /* Mobile Sticky CTA */
        .mobile-sticky-bar {
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
        }

        /* Responsive Breakpoints */
        @media (max-width: 992px) {
            .hero-title { font-size: 2.3rem; }
            .compare-grid { grid-template-columns: 1fr; }
            .bonus-grid-mockups { grid-template-columns: 1fr; }
            .author-grid-brand { grid-template-columns: 1fr; text-align: center; }
            .author-brand-emblem { max-width: 320px; margin: 0 auto; height: 260px; }
            .guarantee-box { flex-direction: column; text-align: center; }
        }

        @media (max-width: 768px) {
            .announcement-bar { font-size: 0.85rem; padding: 10px; }
            .hero { padding: 40px 0 60px; }
            .hero-title { font-size: 1.9rem; }
            .hero-subtitle { font-size: 1.05rem; }
            .btn { font-size: 1.1rem; padding: 16px 24px; }
            .mobile-sticky-bar { display: flex; align-items: center; justify-content: space-between; }
            .mobile-sticky-bar .btn { font-size: 1rem; padding: 12px 20px; width: 100%; }
            .chapter-card-mockup { flex-direction: column; text-align: center; }
            .bonus-card-mockup { flex-direction: column; text-align: center; }
            .bonus-title-side { padding-right: 0; }
            .bonus-badge-tag { position: relative; top: 0; right: 0; display: inline-block; margin-bottom: 12px; }
        }
    </style>
</head>
<body>

    <!-- Top Urgency Bar -->
    <div class="announcement-bar">
        <span><i class="fa-solid fa-fire text-gold"></i> OFFRE SPÉCIALE ÉCONOMIE (-50%) — DISPONIBLE SEULEMENT AUJOURD'HUI</span>
        <div class="timer-badge" id="top-timer">22:45:18</div>
    </div>

    <!-- Hero Section -->
    <section class="hero text-center">
        <div class="container">
            <div class="hero-badge">
                <i class="fa-solid fa-shield-halved"></i> Le Programme Ultimatum pour l'Homme Moderne
            </div>
            
            <h1 class="hero-title">
                Ne Laisse Plus Les Tensions Et Les Disputes <span>Détruire Ton Couple</span>.
            </h1>
            
            <p class="hero-subtitle">
                Le programme complet et structuré en 9 chapitres immersifs pour maîtriser la communication relationnelle, apaiser les conflits et rétablir l'intimité en moins de 30 jours.
            </p>

            <div class="hero-target-box">
                <i class="fa-solid fa-circle-check text-gold"></i> <strong>Conçu pour les hommes, maris et fiancés :</strong> Qui veulent mettre fin aux silences lourds, se faire respecter avec calme et devenir l'orateur apaisé de leur foyer.
            </div>

            <!-- GIANT HERO BUNDLE SHOWCASE (ALL 9 MODULES + 2 BONUSES + MAIN PACK) -->
            <div class="hero-bundle-showcase">
                <div class="hero-bundle-badge">
                    <i class="fa-solid fa-box-open"></i> PACK COMPLET 9 MODULES + 2 BONUS INCLUS
                </div>

                <div class="bundle-grid-display">
                    <!-- Main Book Pack -->
                    <div class="mockup-book mockup-book main-pack m-theme-main">
                        <span class="mockup-book-badge" style="background:var(--secondary); color:#000;">GUIDE ULTIME</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-heart-circle-bolt" style="color:#f5d061;"></i></div>
                        <div>
                            <div class="mockup-book-title" style="font-size:1.1rem;">SAUVER SON COUPLE 2.0</div>
                            <div class="mockup-book-sub">Méthode complète sur 30 Jours</div>
                        </div>
                        <div style="font-size:0.65rem; color:var(--secondary-light); font-weight:700;">DORA ÉLYSIANE</div>
                    </div>

                    <!-- Chapter 1 Mockup Mini -->
                    <div class="mockup-book m-theme-ch1">
                        <span class="mockup-book-badge" style="background:#ef4444; color:#fff;">MODULE 1</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-eye"></i></div>
                        <div class="mockup-book-title">Diagnostic Ombre</div>
                    </div>

                    <!-- Chapter 2 Mockup Mini -->
                    <div class="mockup-book m-theme-ch2">
                        <span class="mockup-book-badge" style="background:#3b82f6; color:#fff;">MODULE 2</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-user-tie"></i></div>
                        <div class="mockup-book-title">Miroir de l'Homme</div>
                    </div>

                    <!-- Chapter 3 Mockup Mini -->
                    <div class="mockup-book m-theme-ch3">
                        <span class="mockup-book-badge" style="background:#a855f7; color:#fff;">MODULE 3</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-crown"></i></div>
                        <div class="mockup-book-title">Se Faire Respecter</div>
                    </div>

                    <!-- Chapter 4 Mockup Mini -->
                    <div class="mockup-book m-theme-ch4">
                        <span class="mockup-book-badge" style="background:#f43f5e; color:#fff;">MODULE 4</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-fire-flame-curved"></i></div>
                        <div class="mockup-book-title">Le Lit Froid</div>
                    </div>

                    <!-- Chapter 5 Mockup Mini -->
                    <div class="mockup-book m-theme-ch5">
                        <span class="mockup-book-badge" style="background:#f59e0b; color:#fff;">MODULE 5</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-bolt"></i></div>
                        <div class="mockup-book-title">Haute Tension</div>
                    </div>

                    <!-- Chapter 6 Mockup Mini -->
                    <div class="mockup-book m-theme-ch6">
                        <span class="mockup-book-badge" style="background:#10b981; color:#fff;">MODULE 6</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-people-roof"></i></div>
                        <div class="mockup-book-title">Belle-Famille</div>
                    </div>

                    <!-- Bonus 1 Mockup Mini -->
                    <div class="mockup-book m-theme-b1">
                        <span class="mockup-book-badge" style="background:#d4af37; color:#000;">BONUS #1</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
                        <div class="mockup-book-title">10 Phrases Magiques</div>
                    </div>

                    <!-- Bonus 2 Mockup Mini -->
                    <div class="mockup-book m-theme-b2">
                        <span class="mockup-book-badge" style="background:#ef4444; color:#fff;">BONUS #2</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
                        <div class="mockup-book-title">12 Erreurs Fatales</div>
                    </div>
                </div>
            </div>

            <!-- CTA Hero -->
            <a href="#commander" class="btn btn-primary">
                <span><i class="fa-solid fa-download"></i> J'ACCÈDE À ÉLOQUENCE & SAUVER SON COUPLE 2.0</span>
                <span class="btn-subtext">Accès immédiat aux 9 Modules + 2 Bonus • 9 900 FCFA (~15 €)</span>
            </a>
            <p style="font-size: 0.9rem; color: #94a3b8; margin-top: 14px;">
                <i class="fa-solid fa-lock text-gold"></i> Paiement 100% Sécurisé (Wave, Orange, MTN, Moov, Carte)
            </p>
        </div>
    </section>

    <!-- Social Proof Bar -->
    <section class="proof-bar">
        <div class="container">
            <div class="proof-grid">
                <div class="proof-item">
                    <h3>+5 000</h3>
                    <p>Hommes Formés</p>
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
                    <h3>9 Modules</h3>
                    <p>Programme Complet</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Problem & Transformation Section -->
    <section class="transformation-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Imagine Si Demain, Chaque Dispute Devenait Une Occasion De Renforcer Votre Complicité...</h2>
                <p class="section-subtitle">
                    Tu n'as plus à subir la distance émotionnelle, les reproches incessants ou le silence pesant à la maison.
                </p>
            </div>

            <div class="compare-grid">
                <!-- Problem Card -->
                <div class="compare-card problem">
                    <h3><i class="fa-solid fa-circle-xmark text-primary"></i> 📌 La Situation Actuelle</h3>
                    <ul class="compare-list">
                        <li>
                            <i class="fa-solid fa-xmark text-primary"></i>
                            <span>Des discussions simples qui tournent rapidement au drame et aux insatisfactions.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-primary"></i>
                            <span>L'impression de n'être perçu que comme un "portefeuille" sans reconnaissance.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-primary"></i>
                            <span>Des jours entiers de silence pesant et d'évitement à la maison.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-primary"></i>
                            <span>La peur permanente de dire le mauvais mot et d'empirer la situation.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark text-primary"></i>
                            <span>Le lit froid et la perte d'intimité physique et affective.</span>
                        </li>
                    </ul>
                </div>

                <!-- Solution Card -->
                <div class="compare-card solution">
                    <h3><i class="fa-solid fa-circle-check text-gold"></i> ✅ Après Avoir Suivi Le Programme</h3>
                    <ul class="compare-list">
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Tu gardes ton calme et sais exactement quelles phrases prononcer pour apaiser la tension.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Tu te fais respecter naturellement sans crier ni utiliser la violence.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Les échanges deviennent fluides, clairs, chaleureux et constructifs.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Tu comprends ce que ta partenaire ressent réellement sous sa colère.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check text-gold"></i>
                            <span>Tu rétablis la complicité et ravives le désir au sein de ton foyer.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- CURRICULUM CHAPTERS WITH DEDICATED MOCKUP COVERS -->
    <section class="curriculum-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">VOICI TOUT CE QUE VOUS ALLEZ APPRENDRE AVEC SAUVER SON COUPLE 2.0</h2>
                <p class="section-subtitle">Un programme structuré en 9 modules immersifs avec leur support dédié :</p>
            </div>

            <div class="chapters-grid-mockups">
                
                <!-- Chapitre 1 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch1" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#ef4444; color:#fff;">MODULE 1</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-eye"></i></div>
                        <div class="mockup-book-title">Diagnostic Ombre</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 1</span>
                        <h3 class="chapter-title-side">Le Diagnostic de l'Ombre</h3>
                        <p class="chapter-desc-side">Pourquoi tu as l'impression de n'être qu'un portefeuille ? Analyser la perte de connexion émotionnelle et identifier les blocages réels.</p>
                    </div>
                </div>

                <!-- Chapitre 2 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch2" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#3b82f6; color:#fff;">MODULE 2</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-user-tie"></i></div>
                        <div class="mockup-book-title">Miroir de l'Homme</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 2</span>
                        <h3 class="chapter-title-side">Le Miroir de l'Homme</h3>
                        <p class="chapter-desc-side">Avant de la changer elle, regarde-toi. Retrouver sa confiance en soi, sa clarté mentale et son leadership personnel.</p>
                    </div>
                </div>

                <!-- Chapitre 3 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch3" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#a855f7; color:#fff;">MODULE 3</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-crown"></i></div>
                        <div class="mockup-book-title">Se Faire Respecter</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 3</span>
                        <h3 class="chapter-title-side">L'Art de Se Faire Respecter (Sans Crier)</h3>
                        <p class="chapter-desc-side">Comment réagir face au mépris ou à la comparaison sans entrer dans la colère ni dans le silence boudeur.</p>
                    </div>
                </div>

                <!-- Chapitre 4 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch4" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#f43f5e; color:#fff;">MODULE 4</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-fire-flame-curved"></i></div>
                        <div class="mockup-book-title">Le Lit Froid</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 4</span>
                        <h3 class="chapter-title-side">Le Lit Froid – Briser la Grève de l'Intimité</h3>
                        <p class="chapter-desc-side">Comprendre le désir féminin et reconnecter physiquement avec ta partenaire sans mendier ni forcer.</p>
                    </div>
                </div>

                <!-- Chapitre 5 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch5" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#f59e0b; color:#fff;">MODULE 5</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-bolt"></i></div>
                        <div class="mockup-book-title">Haute Tension</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 5</span>
                        <h3 class="chapter-title-side">La Communication "Haute Tension"</h3>
                        <p class="chapter-desc-side">Comment parler de tes besoins sans que ça finisse en dispute. Apprendre l'écoute active et l'affirmation de soi.</p>
                    </div>
                </div>

                <!-- Chapitre 6 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch6" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#10b981; color:#fff;">MODULE 6</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-people-roof"></i></div>
                        <div class="mockup-book-title">La Belle-Famille</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 6</span>
                        <h3 class="chapter-title-side">Gérer la "Tribu" (Famille & Belle-Famille)</h3>
                        <p class="chapter-desc-side">Mettre des frontières saines et imperméables entre ton foyer et les influences extérieures perturbatrices.</p>
                    </div>
                </div>

                <!-- Chapitre 7 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch7" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#3b82f6; color:#fff;">MODULE 7</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-fist-raised"></i></div>
                        <div class="mockup-book-title">Frustration en Force</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 7</span>
                        <h3 class="chapter-title-side">Transformer la Frustration en Force</h3>
                        <p class="chapter-desc-side">Gérer sa propre colère et sa solitude émotionnelle. Trouver ses propres piliers de stabilité masculine.</p>
                    </div>
                </div>

                <!-- Chapitre 8 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch8" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#06b6d4; color:#fff;">MODULE 8</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-calendar-check"></i></div>
                        <div class="mockup-book-title">Plan 30 Jours</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 8</span>
                        <h3 class="chapter-title-side">Le Plan d'Action sur 30 Jours</h3>
                        <p class="chapter-desc-side">Des exercices concrets et quotidiens pour métamorphoser radicalement l'atmosphère de la maison.</p>
                    </div>
                </div>

                <!-- Chapitre 9 -->
                <div class="chapter-card-mockup">
                    <div class="mockup-book m-theme-ch9" style="flex-shrink:0;">
                        <span class="mockup-book-badge" style="background:#64748b; color:#fff;">MODULE 9</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-scale-balanced"></i></div>
                        <div class="mockup-book-title">Sagesse de Décision</div>
                    </div>
                    <div class="chapter-content-side">
                        <span class="chapter-num-badge">MODULE 9</span>
                        <h3 class="chapter-title-side">Quand est-il Temps de Partir ?</h3>
                        <p class="chapter-desc-side">La sagesse de savoir avec lucidité si le combat en vaut encore la peine et comment prendre les bonnes décisions.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- BONUS SECTION WITH DEDICATED MOCKUP COVERS -->
    <section class="bonus-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title" style="color:#fff;">MAIS CE N'EST PAS TOUT !</h2>
                <p class="section-subtitle" style="color:#cbd5e1;">VOICI LES BONUS EXCLUSIFS INCLUS DANS VOTRE PROGRAMME</p>
            </div>

            <div class="bonus-grid-mockups">
                <!-- Bonus 1 Card with Mockup -->
                <div class="bonus-card-mockup">
                    <span class="bonus-badge-tag">OFFERT (Valeur 8 000 FCFA)</span>
                    <div class="mockup-book m-theme-b1" style="flex-shrink:0; width:150px; height:210px;">
                        <span class="mockup-book-badge" style="background:#d4af37; color:#000;">BONUS #1</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
                        <div class="mockup-book-title">10 Phrases Magiques</div>
                    </div>
                    <div class="bonus-info-side">
                        <h3 class="bonus-title-side">🎁 BONUS #1 : 10 Phrases pour Désamorcer un Conflit Immédiatement</h3>
                        <p class="bonus-desc-side">
                            Un ensemble de phrases simples, prêtes à utiliser dans les moments tendus pour calmer une discussion, éviter l’escalade et reprendre le contrôle émotionnel. Tu sauras quoi dire au bon moment.
                        </p>
                    </div>
                </div>

                <!-- Bonus 2 Card with Mockup -->
                <div class="bonus-card-mockup">
                    <span class="bonus-badge-tag">OFFERT (Valeur 10 000 FCFA)</span>
                    <div class="mockup-book m-theme-b2" style="flex-shrink:0; width:150px; height:210px;">
                        <span class="mockup-book-badge" style="background:#ef4444; color:#fff;">BONUS #2</span>
                        <div class="mockup-book-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
                        <div class="mockup-book-title">12 Erreurs Fatales</div>
                    </div>
                    <div class="bonus-info-side">
                        <h3 class="bonus-title-side">🎁 BONUS #2 : Les 12 Erreurs qui Détruisent un Couple sans s’en rendre compte</h3>
                        <p class="bonus-desc-side">
                            Tu vas découvrir les comportements les plus courants qui fragilisent une relation : mauvaises réactions en dispute, manque d’écoute, attitudes distancantes… Chaque erreur a sa solution claire.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Pricing Section -->
    <section class="pricing-section" id="commander">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">VALEUR TOTALE ET OFFRE SPÉCIALE</h2>
                <p class="section-subtitle">Investissez aujourd'hui dans l'harmonie et la tranquillité de votre foyer.</p>
            </div>

            <div class="pricing-box">
                <div class="pricing-header">
                    <h3>RÉCAPITULATIF DE TOUT CE QUE VOUS RECEVEZ</h3>
                    <p>Accès numérique complet et instantané</p>
                </div>

                <div class="pricing-body">
                    <ul class="stack-list">
                        <li class="stack-item">
                            <span>📘 Programme Sauver Son Couple 2.0 (9 Modules Complet)</span>
                            <span class="item-val">15 500 FCFA</span>
                        </li>
                        <li class="stack-item">
                            <span>🎁 Bonus #1 : 10 Phrases pour Désamorcer un Conflit</span>
                            <span class="item-val">8 000 FCFA</span>
                        </li>
                        <li class="stack-item">
                            <span>🎁 Bonus #2 : Les 12 Erreurs Fatales à éviter</span>
                            <span class="item-val">10 000 FCFA</span>
                        </li>
                        <li class="stack-item" style="font-weight: 700; background: #f8fafc; padding: 14px;">
                            <span>💎 VALEUR TOTALE :</span>
                            <span style="text-decoration: line-through; color: #64748b;">33 500 FCFA</span>
                        </li>
                    </ul>

                    <div class="price-total-box">
                        <div class="old-price">PRIX NORMAL : 19 900 FCFA</div>
                        <div class="new-price">9 900 <small>FCFA</small></div>
                        <p style="color: var(--primary); font-weight: 800; font-size: 1rem;">
                            🔥 OFFRE EXCLUSIVE AUJOURD'HUI (~15 €)
                        </p>
                    </div>

                    <div class="payment-methods">
                        <!-- Mobile Money CTA -->
                        <a href="https://doraelysiane.com/prd_eqioqv/checkout" class="btn btn-primary">
                            <span><i class="fa-solid fa-mobile-screen-button"></i> PAYER PAR WAVE, ORANGE, MTN, MOOV</span>
                            <span class="btn-subtext">(Mobile Money - Accès Instantané)</span>
                        </a>

                        <!-- Card CTA -->
                        <a href="https://doraelysiane.com/prd_eqioqv/checkout" class="btn btn-gold" style="margin-top: 10px;">
                            <span><i class="fa-solid fa-credit-card"></i> PAYER PAR CARTE BANCAIRE (VISA / MASTERCARD)</span>
                            <span class="btn-subtext">(Paiement 100% Sécurisé)</span>
                        </a>
                    </div>

                    <div style="text-align: center; margin-top: 24px; color: var(--text-muted); font-size: 0.88rem; display:flex; justify-content:center; gap:20px;">
                        <span><i class="fa-solid fa-lock text-gold"></i> Cryptage SSL 256-bit</span>
                        <span><i class="fa-solid fa-bolt text-gold"></i> Téléchargement Direct</span>
                    </div>
                </div>
            </div>

            <!-- Guarantee Box -->
            <div class="guarantee-box">
                <div class="guarantee-badge">
                    <i class="fa-solid fa-award"></i>
                    <span>GARANTIE 30 JOURS</span>
                </div>
                <div>
                    <h3 style="font-size: 1.4rem; color: var(--text-dark); margin-bottom: 8px;">Garantie Satisfait ou Remboursé de 30 jours</h3>
                    <p style="color: var(--text-muted); font-size: 1rem;">
                        Je suis tellement convaincue de la valeur de cette méthode que je prends 100% du risque sur mes épaules. Si dans les 30 jours suivant votre inscription, vous n'êtes pas entièrement satisfait des résultats obtenus dans vos échanges de couple, envoie un email pour être remboursé intégralement.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">ILS ONT SUIVI MES FORMATIONS ET ACCOMPAGNEMENTS</h2>
                <p class="section-subtitle">Découvrez ce que disent les hommes qui ont appliqué ces méthodes.</p>
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
                            “Je ne savais jamais quoi dire pendant les conflits, j’empirais souvent la situation. Les techniques m’ont vraiment aidé à garder mon calme et à gérer les discussions intelligemment. Ça a changé l’ambiance chez nous.”
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

    <!-- Author Section (Vector Monogram Branding without photos) -->
    <section class="author-section">
        <div class="container">
            <div class="author-grid-brand">
                <div class="author-brand-emblem">
                    <div class="author-monogram">DÉ</div>
                    <h3 style="font-size:1.3rem; color:#fff; font-family:'Outfit';">DORA ÉLYSIANE</h3>
                    <p style="font-size:0.85rem; color:var(--secondary-light); margin-top:4px;">CABINET CONSEIL & ÉLÉGANCE RELATIONNELLE</p>
                </div>

                <div>
                    <h2 class="section-title" style="text-align:left; margin-bottom:20px;">QUI EST DORA ÉLYSIANE ?</h2>
                    <p style="font-size:1.1rem; color:#334155; margin-bottom:16px;">
                        Je m’appelle <strong>Dora Élysiane</strong>, et depuis plusieurs années j’aide des jeunes, des hommes et des femmes à reprendre confiance en eux, à mieux gérer leurs émotions et à transformer leur vie affective.
                    </p>
                    <p style="font-size:1.05rem; color:#64748b; margin-bottom:16px;">
                        J’ai créé mes guides pour une raison simple : j’ai vu trop de personnes souffrir en silence, manquer d’outils, de repères et de conseils clairs pour avancer réellement.
                    </p>
                    <p style="font-size:1.05rem; color:#64748b; margin-bottom:24px;">
                        Mon objectif est toujours le même : donner des solutions simples, vraies et efficaces, que tu peux appliquer dès aujourd’hui.
                    </p>
                    
                    <div style="display:flex; gap:30px;">
                        <div>
                            <h3 style="color:var(--primary); font-size:1.8rem;">+5 ANS</h3>
                            <p style="color:var(--text-muted); font-size:0.9rem;">D'Expertise Terrain</p>
                        </div>
                        <div>
                            <h3 style="color:var(--primary); font-size:1.8rem;">+5 000</h3>
                            <p style="color:var(--text-muted); font-size:0.9rem;">Élèves & Lecteurs</p>
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
                <h2 class="section-title">FOIRE AUX QUESTIONS</h2>
                <p class="section-subtitle">Tout ce que vous devez savoir avant de rejoindre le programme.</p>
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

                <div class="faq-item">
                    <div class="faq-question">
                        <span>5. Quels moyens de paiement sont acceptés ?</span>
                        <i class="fa-solid fa-chevron-down faq-icon"></i>
                    </div>
                    <div class="faq-answer">
                        Vous pouvez payer par carte bancaire (Visa, Mastercard) ou par Mobile Money (Wave, Orange Money, MTN, Moov, Airtel, Free Sénégal). Tous les paiements sont 100% sécurisés avec accès instantané.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer style="background:#0b0f19; color:#94a3b8; padding:50px 0; text-align:center; border-top:1px solid rgba(255,255,255,0.1);">
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
        <a href="#commander" class="btn btn-primary" style="padding:12px 20px; font-size:1rem;">
            <span>REJOINDRrecipe E LE PROGRAMME (9 900 FCFA)</span>
        </a>
    </div>

    <!-- JavaScript Interactions -->
    <script>
        // FAQ Accordion Toggle
        document.querySelectorAll('.faq-question').forEach(question => {
            question.addEventListener('click', () => {
                const faqItem = question.parentElement;
                faqItem.classList.toggle('active');
            });
        });

        // Countdown Timer Logic
        function startTimer(durationInSeconds, displayElements) {
            let timer = durationInSeconds;
            setInterval(() => {
                let hours = parseInt(timer / 3600, 10);
                let minutes = parseInt((timer % 3600) / 60, 10);
                let seconds = parseInt(timer % 60, 10);

                hours = hours < 10 ? '0' + hours : hours;
                minutes = minutes < 10 ? '0' + minutes : minutes;
                seconds = seconds < 10 ? '0' + seconds : seconds;

                displayElements.forEach(el => {
                    if(el) el.textContent = hours + ':' + minutes + ':' + seconds;
                });

                if (--timer < 0) {
                    timer = durationInSeconds;
                }
            }, 1000);
        }

        window.onload = function () {
            const topTimer = document.getElementById('top-timer');
            startTimer(81918, [topTimer]);
        };
    </script>
</body>
</html>
'''

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated index.html successfully with mockups and without photos.')
