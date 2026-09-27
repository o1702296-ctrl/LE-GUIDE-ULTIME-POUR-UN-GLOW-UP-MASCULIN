# -*- coding: utf-8 -*-
import os

html_content = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Le Guide ULTIME Pour un Glow Up Masculin </title>
    <meta name="description" content="Découvrez le guide ultime pour augmenter votre attractivité physique immédiatement. ">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700;800;900&family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {
            /* SHADOW MONARCH PURPLE AURA PALETTE - INSPIRED BY PURPLE AURA CHARACTER */
            --bg-void: #030206;
            --bg-dark: #07050d;
            --bg-surface: #0e091a;
            --bg-card: rgba(14, 9, 26, 0.88);
            --bg-glass: rgba(18, 12, 34, 0.92);
            
            --border-glow: rgba(168, 85, 247, 0.45);
            --border-subtle: rgba(255, 255, 255, 0.12);
            --border-active: rgba(168, 85, 247, 0.85);
            
            --accent-purple: #a855f7;
            --accent-purple-bright: #c084fc;
            --accent-purple-glow: #e9d5ff;
            --accent-purple-deep: #7e22ce;
            --accent-gold: #f59e0b;
            
            --accent-crimson: #a855f7;
            --accent-crimson-bright: #c084fc;
            
            --text-main: #f8fafc;
            --text-muted: #cbd5e1;
            --text-dim: #94a3b8;
            
            --radius-sm: 8px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-full: 9999px;
            
            --shadow-dark: 0 25px 60px rgba(0, 0, 0, 0.98);
            --shadow-glow-purple: 0 0 35px rgba(168, 85, 247, 0.5);
            
            --font-main: 'Plus Jakarta Sans', sans-serif;
            --font-heading: 'Outfit', sans-serif;
            --font-luxury: 'Cinzel', serif;
            --transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
            font-family: var(--font-main);
            background-color: var(--bg-void);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
        }

        body {
            background-color: var(--bg-void);
            color: var(--text-main);
            position: relative;
        }

        /* Ambient Dark Glow Spheres */
        .ambient-glow {
            position: fixed;
            border-radius: 50%;
            filter: blur(140px);
            z-index: 0;
            pointer-events: none;
            opacity: 0.25;
        }
        .glow-1 {
            width: 550px;
            height: 550px;
            background: #7e22ce;
            top: -100px;
            left: -100px;
        }
        .glow-2 {
            width: 600px;
            height: 600px;
            background: #a855f7;
            bottom: 10%;
            right: -150px;
        }

        .container {
            max-width: 1180px;
            margin: 0 auto;
            padding: 0 24px;
            position: relative;
            z-index: 2;
        }

        /* Sticky Announcement Bar */
        .top-bar {
            background: linear-gradient(90deg, #030206 0%, #2a0845 50%, #030206 100%);
            border-bottom: 1px solid var(--accent-purple);
            box-shadow: 0 4px 25px rgba(168, 85, 247, 0.4);
            padding: 10px 16px;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            flex-wrap: wrap;
            font-size: 0.95rem;
            font-weight: 700;
        }
        .top-bar .urgency-text {
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 8px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        .top-bar .timer-box {
            background: rgba(168, 85, 247, 0.3);
            border: 1px solid var(--accent-purple);
            padding: 4px 16px;
            border-radius: var(--radius-full);
            color: #ffffff;
            font-family: monospace;
            font-size: 1.1rem;
            font-weight: 800;
            box-shadow: 0 0 15px rgba(168, 85, 247, 0.6);
        }

        /* CLEARLY VISIBLE BACKGROUND CHARACTER ARTWORK ON ALL SECTIONS */
        .section-padding {
            padding: 95px 0;
            position: relative;
            overflow: hidden;
            border-bottom: 1px solid var(--border-subtle);
        }

        .bg-section-blur {
            position: relative;
        }
        .bg-section-blur::before {
            content: '';
            position: absolute;
            inset: -10px;
            background-image: url('images/peaky_blinders_hero_man.png');
            background-size: cover;
            background-position: center top;
            background-repeat: no-repeat;
            filter: blur(1px) brightness(0.72) contrast(1.08);
            transform: scale(1.03);
            z-index: 0;
            pointer-events: none;
        }
        .bg-section-blur::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(3, 2, 6, 0.65) 0%, rgba(9, 6, 18, 0.55) 50%, rgba(3, 2, 6, 0.75) 100%);
            z-index: 1;
            pointer-events: none;
        }



        /* HERO SECTION */
        .hero-section {
            padding: 90px 0 110px;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .badge-flash {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(0, 0, 0, 0.7);
            border: 1px solid var(--border-glow);
            padding: 8px 18px;
            border-radius: var(--radius-full);
            color: #ffffff;
            font-size: 0.88rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 24px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.9);
            backdrop-filter: blur(10px);
        }

        .hero-title {
            font-family: var(--font-heading);
            font-size: 3rem;
            font-weight: 900;
            line-height: 1.15;
            color: #ffffff;
            margin-bottom: 20px;
            letter-spacing: -0.5px;
            text-shadow: 0 4px 25px rgba(0,0,0,0.98);
        }

        .hero-title .highlight-text {
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, var(--accent-crimson-bright) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-subtitle {
            font-size: 1.15rem;
            color: #f1f5f9;
            margin-bottom: 32px;
            line-height: 1.7;
            text-shadow: 0 2px 14px rgba(0,0,0,0.95);
        }
        .hero-subtitle strong {
            color: #ffffff;
        }

        /* 3D MAIN BOOK MOCKUP STYLING WITH SMOKE EMANATING DIRECTLY FROM BOOK */
        .mockup-wrapper {
            position: relative;
            perspective: 1200px;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            overflow: visible !important;
        }

        .book-container {
            width: 310px;
            height: 440px;
            position: relative;
            transform-style: preserve-3d;
            transform: rotateY(-22deg) rotateX(8deg);
            transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
            box-shadow: -25px 30px 60px rgba(0, 0, 0, 0.98), 0 0 35px rgba(225, 29, 72, 0.3);
            border-radius: 4px 12px 12px 4px;
            z-index: 5;
        }

        .book-container:hover {
            transform: rotateY(-10deg) rotateX(3deg) translateY(-10px);
            box-shadow: -30px 40px 70px rgba(0, 0, 0, 0.98), 0 0 50px rgba(225, 29, 72, 0.5);
        }

        .book-cover {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 4px 12px 12px 4px;
            overflow: hidden;
            background-image: url('images/glowup_suit_gold_tie_mockup.jpg');
            background-size: cover;
            background-position: center top;
            border: 1px solid rgba(255, 255, 255, 0.25);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 24px;
            z-index: 2;
        }

        .book-cover-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.1) 40%, rgba(0, 0, 0, 0.92) 100%);
            z-index: 1;
        }

        .book-content {
            position: relative;
            z-index: 2;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .book-author-tag {
            font-family: var(--font-luxury);
            font-size: 0.88rem;
            letter-spacing: 2px;
            color: var(--accent-gold);
            text-transform: uppercase;
            font-weight: 800;
            text-shadow: 0 2px 8px rgba(0,0,0,0.9);
        }

        .book-main-title {
            font-family: var(--font-heading);
            font-size: 1.7rem;
            font-weight: 900;
            line-height: 1.2;
            color: #ffffff;
            text-shadow: 0 4px 15px rgba(0,0,0,0.95);
            text-transform: uppercase;
        }
        .book-main-title span {
            color: var(--accent-crimson-bright);
            display: block;
        }

        .book-badge-tag {
            align-self: flex-start;
            background: linear-gradient(135deg, var(--accent-crimson) 0%, #9f1239 100%);
            color: #ffffff;
            padding: 6px 14px;
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            box-shadow: 0 4px 15px rgba(225, 29, 72, 0.6);
        }

        .book-spine {
            position: absolute;
            left: 0;
            top: 0;
            width: 34px;
            height: 100%;
            background: linear-gradient(90deg, #050508 0%, #181822 50%, #050508 100%);
            transform: rotateY(90deg) translateZ(0px);
            transform-origin: left;
            border-left: 1px solid rgba(255,255,255,0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-muted);
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 2px;
            writing-mode: vertical-rl;
            text-transform: uppercase;
        }

        .book-pages {
            position: absolute;
            right: 0;
            top: 4px;
            width: 30px;
            height: calc(100% - 8px);
            background: linear-gradient(90deg, #e2e8f0 0%, #cbd5e1 50%, #94a3b8 100%);
            transform: rotateY(90deg) translateZ(310px);
            transform-origin: right;
            border-radius: 0 4px 4px 0;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.3);
        }

        .book-shadow-pedestal {
            position: absolute;
            bottom: -35px;
            width: 320px;
            height: 35px;
            background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.9) 0%, rgba(225, 29, 72, 0.3) 40%, transparent 75%);
            filter: blur(10px);
            border-radius: 50%;
            transform: rotateX(80deg);
        }

        /* CTA BUTTONS */
        .btn-cta {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 18px 32px;
            background: linear-gradient(135deg, #a855f7 0%, #6b21a8 100%);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.35);
            border-radius: var(--radius-md);
            font-size: 1.2rem;
            font-weight: 800;
            text-decoration: none;
            cursor: pointer;
            transition: var(--transition);
            box-shadow: 0 10px 35px rgba(168, 85, 247, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.45);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }

        .btn-cta:hover {
            transform: translateY(-3px) scale(1.01);
            background: linear-gradient(135deg, #c084fc 0%, #7e22ce 100%);
            box-shadow: 0 15px 45px rgba(168, 85, 247, 0.75), inset 0 1px 0 rgba(255, 255, 255, 0.6);
            color: #ffffff;
        }

        .btn-subtext {
            font-size: 0.88rem;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.9);
            text-transform: none;
            margin-top: 4px;
        }

        .payment-callout-box {
            background: rgba(4, 4, 6, 0.92);
            border: 1px solid var(--border-glow);
            border-radius: var(--radius-md);
            padding: 28px;
            margin: 35px 0;
            text-align: center;
            box-shadow: var(--shadow-dark);
            backdrop-filter: blur(12px);
        }

        .payment-callout-box h3 {
            font-size: 1.15rem;
            color: var(--accent-gold);
            margin-bottom: 12px;
            font-family: var(--font-heading);
            font-weight: 800;
        }

        .payment-badges {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 14px;
        }

        .pay-badge {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-subtle);
            padding: 6px 14px;
            border-radius: var(--radius-sm);
            font-size: 0.82rem;
            color: var(--text-main);
            font-weight: 600;
        }

        .section-title-wrap {
            text-align: center;
            max-width: 780px;
            margin: 0 auto 50px;
        }

        .section-subtitle-tag {
            color: var(--text-muted);
            font-size: 0.9rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
            display: block;
        }

        .section-title {
            font-family: var(--font-heading);
            font-size: 2.3rem;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.25;
            text-shadow: 0 4px 20px rgba(0,0,0,0.95);
        }

        /* PAIN POINTS CARDS */
        .cards-grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }

        .card-dark {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 30px;
            transition: var(--transition);
            backdrop-filter: blur(12px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.8);
        }
        .card-dark:hover {
            border-color: var(--border-glow);
            transform: translateY(-5px);
            box-shadow: 0 20px 45px rgba(0,0,0,0.95), 0 0 25px rgba(225, 29, 72, 0.25);
        }

        .card-icon {
            width: 54px;
            height: 54px;
            border-radius: var(--radius-md);
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glow);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            font-size: 1.4rem;
            margin-bottom: 20px;
        }
        .card-icon.crimson {
            background: rgba(225, 29, 72, 0.15);
            border-color: var(--accent-crimson);
            color: var(--accent-crimson-bright);
        }

        .card-dark h4 {
            font-size: 1.2rem;
            color: #ffffff;
            margin-bottom: 12px;
            font-weight: 700;
        }
        .card-dark p {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .quote-box-dark {
            background: rgba(4, 4, 6, 0.94);
            border-left: 4px solid var(--accent-crimson);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            padding: 35px 40px;
            margin: 40px 0;
            backdrop-filter: blur(14px);
            box-shadow: var(--shadow-dark);
        }
        .quote-box-dark p {
            font-size: 1.25rem;
            color: #ffffff;
            font-weight: 600;
            line-height: 1.7;
            font-style: italic;
        }

        /* PROGRAM CHECKLIST */
        .program-box {
            background: rgba(4, 4, 6, 0.94);
            border: 1px solid var(--border-glow);
            border-radius: var(--radius-lg);
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: var(--shadow-dark);
            backdrop-filter: blur(12px);
        }

        .checklist-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 24px;
        }

        .check-item {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-subtle);
            padding: 16px 20px;
            border-radius: var(--radius-md);
        }
        .check-item i {
            color: var(--accent-crimson-bright);
            font-size: 1.2rem;
            margin-top: 2px;
        }
        .check-item span {
            color: var(--text-main);
            font-size: 1rem;
            font-weight: 600;
        }

        /* HIGH-END 3D BONUS DIGITAL PRODUCT MOCKUPS */
        .bonus-card-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            margin: 40px 0;
        }

        .bonus-card {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            overflow: visible !important;
            display: flex;
            flex-direction: column;
            transition: var(--transition);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(12px);
        }
        .bonus-card:hover {
            border-color: var(--accent-gold);
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.95), 0 0 30px rgba(245, 158, 11, 0.3);
        }

        .bonus-card-header {
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(225, 29, 72, 0.15) 100%);
            border-bottom: 1px solid var(--border-subtle);
            padding: 14px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .bonus-tag {
            color: var(--accent-gold);
            font-weight: 800;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .bonus-val {
            background: rgba(0,0,0,0.8);
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold);
            padding: 3px 12px;
            border-radius: var(--radius-full);
            font-size: 0.8rem;
            font-weight: 800;
        }

        /* 3D DIGITAL PRODUCT MOCKUP AREA FOR BONUSES WITH SMOKE EMANATING DIRECTLY OUT OF MOCKUPS */
        .bonus-mockup-stage {
            position: relative;
            perspective: 1000px;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px 20px 45px;
            background: radial-gradient(circle at center, rgba(20, 20, 30, 0.8) 0%, rgba(0, 0, 0, 0.95) 100%);
            border-bottom: 1px solid var(--border-subtle);
            min-height: 300px;
            overflow: visible !important;
        }

        /* 3D BOOK WITH EMBEDDED SMOKE EMITTER BUILT INSIDE THE BOOK ITSELF */
        .bonus-3d-book {
            width: 175px;
            height: 245px;
            position: relative;
            transform-style: preserve-3d;
            transform: rotateY(-18deg) rotateX(6deg);
            transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.5s ease;
            box-shadow: -20px 22px 40px rgba(0, 0, 0, 0.98), 0 0 25px rgba(225, 29, 72, 0.25);
            border-radius: 3px 8px 8px 3px;
            z-index: 5;
        }

        .bonus-card:hover .bonus-3d-book {
            transform: rotateY(-6deg) rotateX(2deg) translateY(-8px) scale(1.04);
            box-shadow: -22px 30px 50px rgba(0, 0, 0, 0.98), 0 0 40px rgba(225, 29, 72, 0.45);
        }

        /* SMOKE EMITTING DIRECTLY FROM INSIDE THE MOCKUP BOOK STRUCTURE */
        .mockup-direct-smoke {
            position: absolute;
            inset: -25px;
            pointer-events: none;
            z-index: 10;
            overflow: visible !important;
        }

        .smoke-cloud-inner {
            position: absolute;
            bottom: 10px;
            border-radius: 50%;
            background: radial-gradient(circle at center, rgba(18, 15, 28, 0.45) 0%, rgba(8, 6, 14, 0.25) 50%, rgba(225, 29, 72, 0.08) 75%, transparent 100%);
            filter: blur(18px);
            box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.4), 0 0 10px rgba(0, 0, 0, 0.3);
            animation: emergeDirectFromMockup 5.2s infinite ease-out;
            opacity: 0;
            pointer-events: none;
        }

        .smoke-cloud-inner.m1 { left: 10%; width: 110px; height: 110px; animation-delay: 0s; }
        .smoke-cloud-inner.m2 { left: 40%; width: 140px; height: 140px; animation-delay: 1.2s; animation-duration: 6s; }
        .smoke-cloud-inner.m3 { left: 65%; width: 100px; height: 100px; animation-delay: 2.4s; animation-duration: 4.8s; }
        .smoke-cloud-inner.m4 { left: 25%; width: 125px; height: 125px; animation-delay: 3.6s; animation-duration: 5.6s; }

        @keyframes emergeDirectFromMockup {
            0% {
                transform: translateY(15px) scale(0.4) rotate(0deg);
                opacity: 0;
            }
            30% {
                opacity: 0.42;
            }
            65% {
                transform: translateY(-80px) scale(1.6) rotate(60deg);
                opacity: 0.22;
            }
            100% {
                transform: translateY(-170px) scale(2.5) rotate(120deg);
                opacity: 0;
            }
        }

        .bonus-3d-cover {
            position: absolute;
            inset: 0;
            border-radius: 3px 8px 8px 3px;
            overflow: hidden;
            background-size: cover;
            background-position: center top;
            border: 1px solid rgba(255, 255, 255, 0.25);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 14px;
            z-index: 2;
        }

        .bonus-3d-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0, 0, 0, 0.45) 0%, rgba(0, 0, 0, 0.1) 40%, rgba(0, 0, 0, 0.92) 100%);
            z-index: 1;
        }

        .bonus-3d-content {
            position: relative;
            z-index: 2;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .bonus-3d-author {
            font-family: var(--font-luxury);
            font-size: 0.62rem;
            letter-spacing: 1.5px;
            color: var(--accent-gold);
            text-transform: uppercase;
            font-weight: 800;
            text-shadow: 0 2px 6px rgba(0,0,0,0.9);
        }

        .bonus-3d-title {
            font-family: var(--font-heading);
            font-size: 0.92rem;
            font-weight: 900;
            line-height: 1.15;
            color: #ffffff;
            text-shadow: 0 2px 10px rgba(0,0,0,0.95);
            text-transform: uppercase;
        }
        .bonus-3d-title span {
            color: var(--accent-crimson-bright);
            display: block;
        }

        .bonus-3d-badge {
            align-self: flex-start;
            background: linear-gradient(135deg, var(--accent-crimson) 0%, #9f1239 100%);
            color: #ffffff;
            padding: 3px 8px;
            border-radius: var(--radius-full);
            font-size: 0.58rem;
            font-weight: 800;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            box-shadow: 0 2px 8px rgba(225, 29, 72, 0.5);
        }

        .bonus-3d-spine {
            position: absolute;
            left: 0;
            top: 0;
            width: 20px;
            height: 100%;
            background: linear-gradient(90deg, #050508 0%, #181822 50%, #050508 100%);
            transform: rotateY(90deg) translateZ(0px);
            transform-origin: left;
            border-left: 1px solid rgba(255,255,255,0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-muted);
            font-size: 0.55rem;
            font-weight: 700;
            writing-mode: vertical-rl;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .bonus-3d-pages {
            position: absolute;
            right: 0;
            top: 3px;
            width: 18px;
            height: calc(100% - 6px);
            background: linear-gradient(90deg, #e2e8f0 0%, #cbd5e1 50%, #94a3b8 100%);
            transform: rotateY(90deg) translateZ(175px);
            transform-origin: right;
            border-radius: 0 3px 3px 0;
        }

        .bonus-3d-pedestal {
            position: absolute;
            bottom: 12px;
            width: 190px;
            height: 25px;
            background: radial-gradient(ellipse at center, rgba(0, 0, 0, 0.9) 0%, rgba(225, 29, 72, 0.3) 40%, transparent 75%);
            filter: blur(8px);
            border-radius: 50%;
            transform: rotateX(80deg);
        }

        .bonus-card-body {
            padding: 24px;
            flex-grow: 1;
            position: relative;
            z-index: 3;
            background: var(--bg-card);
        }
        .bonus-card-body h4 {
            font-size: 1.15rem;
            color: #ffffff;
            margin-bottom: 10px;
            font-weight: 700;
        }
        .bonus-card-body p {
            font-size: 0.92rem;
            color: var(--text-muted);
            line-height: 1.6;
        }

        /* PRICE STACK BOX */
        .price-stack-box {
            background: linear-gradient(180deg, #09090e 0%, #030305 100%);
            border: 2px solid var(--accent-crimson);
            border-radius: var(--radius-lg);
            padding: 45px;
            text-align: center;
            box-shadow: 0 0 60px rgba(0, 0, 0, 0.98), 0 0 30px rgba(225, 29, 72, 0.3);
            margin: 50px 0;
            position: relative;
            backdrop-filter: blur(14px);
        }

        .price-old {
            font-size: 1.4rem;
            color: var(--text-dim);
            text-decoration: line-through;
            margin-bottom: 8px;
            font-weight: 600;
        }
        .price-current {
            font-family: var(--font-heading);
            font-size: 3.5rem;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
            margin-bottom: 8px;
        }
        .price-current span {
            color: var(--accent-crimson-bright);
        }
        .price-sub {
            color: var(--text-muted);
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 24px;
        }

        /* GUARANTEE BADGE */
        .guarantee-box {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-glow);
            border-radius: var(--radius-md);
            padding: 28px;
            display: flex;
            align-items: center;
            gap: 24px;
            margin: 30px 0;
        }
        .guarantee-icon {
            font-size: 3rem;
            color: var(--accent-gold);
            flex-shrink: 0;
        }
        .guarantee-text h4 {
            color: #ffffff;
            font-size: 1.15rem;
            margin-bottom: 6px;
        }
        .guarantee-text p {
            color: var(--text-muted);
            font-size: 0.92rem;
        }

        /* FULL VISUAL TRANSFORMATIONS GRID */
        .transformations-full-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            max-width: 1180px;
            margin: 40px auto 0;
        }

        .transform-card-wrapper {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            overflow: hidden;
            backdrop-filter: blur(12px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.85);
            transition: var(--transition);
        }
        .transform-card-wrapper:hover {
            border-color: var(--border-glow);
            transform: translateY(-5px);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.98), 0 0 30px rgba(168, 85, 247, 0.35);
        }

        .transform-img-box {
            position: relative;
            overflow: hidden;
            background: #000;
        }
        .transform-img-box img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: contain;
            transition: var(--transition);
        }

        .transform-info-bar {
            padding: 16px 20px;
            background: rgba(14, 9, 26, 0.95);
            border-top: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
        }
        .transform-author-name {
            color: #ffffff;
            font-size: 1.05rem;
            font-weight: 800;
            display: flex;
            align-items: center;
        }
        .transform-author-location {
            color: var(--text-dim);
            font-size: 0.88rem;
            font-weight: 600;
            display: flex;
            align-items: center;
        }

        @media (max-width: 768px) {
            .transformations-full-grid {
                grid-template-columns: 1fr !important;
                gap: 24px !important;
            }
        }

        .stars {
            color: var(--accent-gold);
            font-size: 0.9rem;
            margin-bottom: 12px;
        }
        .testimonial-text {
            color: var(--text-main);
            font-size: 0.95rem;
            font-style: italic;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .testimonial-author {
            display: flex;
            align-items: center;
            gap: 12px;
            border-top: 1px solid var(--border-subtle);
            padding-top: 16px;
        }
        .avatar-circle {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: rgba(168, 85, 247, 0.2);
            border: 1px solid var(--accent-purple);
            color: #ffffff;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
        }
        .author-info h5 {
            color: #ffffff;
            font-size: 0.98rem;
            font-weight: 700;
        }
        .author-info span {
            color: var(--text-dim);
            font-size: 0.8rem;
        }

        /* FAQ ACCORDION */
        .faq-accordion {
            display: flex;
            flex-direction: column;
            gap: 16px;
            max-width: 840px;
            margin: 0 auto;
        }

        .faq-item {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            overflow: hidden;
            transition: var(--transition);
            backdrop-filter: blur(12px);
        }
        .faq-item.active {
            border-color: var(--border-glow);
        }

        .faq-question {
            padding: 20px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            font-size: 1.05rem;
            font-weight: 700;
            color: #ffffff;
            user-select: none;
        }
        .faq-question i {
            color: var(--text-muted);
            transition: transform 0.3s ease;
        }
        .faq-item.active .faq-question i {
            transform: rotate(180deg);
            color: var(--accent-crimson-bright);
        }

        .faq-answer {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s cubic-bezier(0, 1, 0, 1);
            padding: 0 24px;
            background: rgba(0, 0, 0, 0.4);
        }
        .faq-item.active .faq-answer {
            max-height: 300px;
            padding: 0 24px 20px 24px;
            transition: max-height 0.4s ease-in-out;
        }
        .faq-answer p {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.6;
        }

        /* AUTHOR BIO SECTION */
        .author-card {
            background: rgba(4, 4, 6, 0.94);
            border: 1px solid var(--border-glow);
            border-radius: var(--radius-lg);
            padding: 40px;
            display: grid;
            grid-template-columns: 290px 1fr;
            gap: 40px;
            align-items: center;
            box-shadow: var(--shadow-dark);
            backdrop-filter: blur(14px);
        }

        .author-img {
            width: 100%;
            height: 380px;
            object-fit: cover;
            object-position: center top;
            border-radius: var(--radius-md);
            border: 2px solid var(--border-glow);
            box-shadow: 0 15px 40px rgba(0,0,0,0.95), 0 0 25px rgba(225, 29, 72, 0.3);
        }

        .author-content h3 {
            font-family: var(--font-heading);
            font-size: 2rem;
            color: #ffffff;
            margin-bottom: 14px;
        }
        .author-content p {
            color: var(--text-muted);
            font-size: 1rem;
            line-height: 1.7;
            margin-bottom: 16px;
        }

        /* SPLIT GRID 2-COLUMN LAYOUTS FOR LAST 3 SECTIONS */
        .split-sec-grid {
            display: grid;
            grid-template-columns: 360px 1fr;
            gap: 40px;
            align-items: center;
        }
        .split-sec-grid.alt-reverse {
            grid-template-columns: 1fr 360px;
        }

        .split-img-card {
            width: 100%;
            height: 440px;
            border-radius: var(--radius-lg);
            overflow: hidden;
            border: 2px solid var(--border-glow);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.95), 0 0 35px rgba(168, 85, 247, 0.4);
            position: relative;
        }
        .split-img-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center top;
            transition: transform 0.5s ease;
        }
        .split-img-card:hover img {
            transform: scale(1.04);
        }
        .split-img-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, transparent 60%, rgba(3, 2, 6, 0.85) 100%);
        }

        /* FOOTER */
        .footer {
            background: #000000;
            border-top: 1px solid var(--border-subtle);
            padding: 40px 0;
            text-align: center;
            color: var(--text-dim);
            font-size: 0.88rem;
            position: relative;
            z-index: 2;
        }

        
        /* HIGH-PRECISION DESKTOP RESPONSIVE DESIGN SYSTEM WITH FULL-PAGE CONTINUOUS BACKGROUND */
        @media (min-width: 993px) {
            body {
                position: relative;
                background-color: var(--bg-void);
            }
            body::before {
                content: '';
                position: fixed;
                inset: 0;
                background-image: url('images/peaky_blinders_hero_man.png');
                background-size: cover;
                background-position: center 15%;
                background-repeat: no-repeat;
                filter: blur(1px) brightness(0.70) contrast(1.1);
                z-index: 0;
                pointer-events: none;
            }

            /* Remove per-section background breaks so body background covers ALL sections continuously */
            .bg-section-blur::before {
                display: none !important;
            }

            .bg-section-blur::after {
                background: linear-gradient(180deg, rgba(3, 2, 6, 0.72) 0%, rgba(7, 5, 13, 0.55) 50%, rgba(3, 2, 6, 0.80) 100%);
            }

            .container {
                max-width: 1160px;
                padding: 0 32px;
            }

            .container {
                max-width: 1160px;
                padding: 0 32px;
            }

            .section-padding {
                padding: 100px 0;
            }

            .section-title-wrap {
                max-width: 820px;
                margin-bottom: 55px;
            }

            .section-title {
                font-size: 2.5rem;
                line-height: 1.22;
            }

            /* Clean Background Layering on Desktop */
            .bg-section-blur::before {
                background-attachment: scroll;
                background-position: center top;
                background-size: cover;
                filter: blur(1px) brightness(0.65) contrast(1.08);
                transform: none;
            }
            .bg-section-blur::after {
                background: linear-gradient(180deg, rgba(3, 2, 6, 0.78) 0%, rgba(7, 5, 13, 0.60) 50%, rgba(3, 2, 6, 0.85) 100%);
            }

            /* Hero Section Desktop Alignment */
            .hero-section {
                padding: 100px 0 120px;
            }
            .hero-grid {
                grid-template-columns: 1.12fr 0.88fr;
                gap: 60px;
                align-items: center;
            }
            .hero-title {
                font-size: 3.2rem;
                line-height: 1.15;
                margin-bottom: 22px;
            }
            .hero-subtitle {
                font-size: 1.18rem;
                margin-bottom: 36px;
                line-height: 1.75;
            }
            .hero-content .btn-cta {
                max-width: 520px;
            }

            /* 3D Hero Book Mockup */
            .mockup-wrapper {
                padding: 10px 0;
            }
            .book-container {
                width: 320px;
                height: 455px;
            }

            /* Testimonials / Transformations Full Grid on Desktop */
            .transformations-full-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 28px;
                max-width: 1080px;
                margin: 45px auto 0;
                align-items: stretch;
            }
            .transform-card-wrapper {
                display: flex;
                flex-direction: column;
                height: 100%;
                border-radius: var(--radius-md);
                background: var(--bg-card);
                border: 1px solid var(--border-subtle);
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.88);
            }
            .transform-img-box {
                height: 440px;
                width: 100%;
                overflow: hidden;
                position: relative;
                background: #000;
            }
            .transform-img-box img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: top center;
            }
            .transform-info-bar {
                margin-top: auto;
                padding: 18px 22px;
                background: rgba(14, 9, 26, 0.96);
            }

            /* 3-Column Feature Cards Grid */
            .cards-grid-3 {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 28px;
                align-items: stretch;
            }
            .card-dark {
                display: flex;
                flex-direction: column;
                height: 100%;
                padding: 34px 28px;
            }

            /* 6 Modules & 3 Bonuses 3D Cards Grid */
            .bonus-card-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 28px;
                align-items: stretch;
            }
            .bonus-card {
                display: flex;
                flex-direction: column;
                height: 100%;
            }
            .bonus-mockup-stage {
                height: 290px;
                padding: 30px 15px;
            }
            .bonus-card-body {
                flex-grow: 1;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                padding: 26px 22px;
            }

            /* Price Stack Recap Box */
            .price-stack-box {
                max-width: 880px;
                margin: 60px auto;
                padding: 50px 45px;
                border-radius: 20px;
                box-shadow: 0 0 70px rgba(0, 0, 0, 0.98), 0 0 40px rgba(168, 85, 247, 0.35);
            }
            .price-current {
                font-size: 3.6rem !important;
            }

            /* Quote Box */
            .quote-box-dark {
                max-width: 960px;
                margin: 45px auto;
                padding: 40px 48px;
            }

            /* FAQ Accordion */
            .faq-accordion {
                max-width: 860px;
                margin: 0 auto;
            }

            /* Author Bio & Final CTA */
            .sec-author .container {
                max-width: 880px;
            }
            .sec-footer .container {
                max-width: 840px;
            }
        }

        /* HIGH-PRECISION MOBILE RESPONSIVE DESIGN SYSTEM */
        @media (max-width: 992px) {
            .container { padding: 0 16px; }
            .section-padding { padding: 65px 0; }
            .section-title { font-size: 1.85rem; line-height: 1.3; }
            .section-title-wrap { margin-bottom: 35px; }
            .section-subtitle-tag { font-size: 0.8rem; letter-spacing: 1.5px; }

            /* Mobile Background Image Framing & Alignment */
            .bg-section-blur::before {
                background-size: cover;
                background-position: center 15%;
                filter: blur(1.5px) brightness(0.68) contrast(1.05);
                transform: scale(1.02);
            }
            .sec-hero::before { background-position: center 10%; }
            .sec-pain::before { background-position: center top; }
            .sec-transform::before { background-position: center top; }
            .sec-program::before { background-position: center 15%; }
            .sec-testimonials::before { background-position: center 10%; }
            .sec-faq::before { background-image: url('images/peaky_last_sec1_blue_suit.png'); background-position: center 15%; }
            .sec-author::before { background-image: url('images/peaky_last_sec2_foggy_standing.png'); background-position: center 10%; }
            .sec-footer::before { background-image: url('images/peaky_last_sec3_glasses_profile.png'); background-position: center 15%; }

            /* Hero Section Responsive */
            .hero-section { padding: 45px 0 65px; }
            .hero-grid { grid-template-columns: 1fr; gap: 35px; text-align: center; }
            .badge-flash { font-size: 0.78rem; padding: 6px 14px; margin: 0 auto 18px; }
            .hero-title { font-size: 2.1rem; line-height: 1.25; }
            .hero-subtitle { font-size: 1.02rem; margin-bottom: 24px; }
            .payment-badges { justify-content: center !important; }

            /* Hero 3D Book Mockup Responsive */
            .mockup-wrapper { padding: 10px 0; }
            .book-container { width: 250px; height: 355px; margin: 0 auto; transform: rotateY(-10deg) rotateX(4deg); }
            .book-cover { padding: 18px; }
            .book-main-title { font-size: 1.35rem; }
            .book-author-tag { font-size: 0.78rem; }
            .book-spine { width: 26px; font-size: 0.65rem; }
            .book-pages { transform: rotateY(90deg) translateZ(250px); width: 24px; }
            .book-shadow-pedestal { width: 250px; bottom: -30px; }

            /* Grid Layouts Responsive */
            .cards-grid-3 { grid-template-columns: 1fr; gap: 20px; }
            .bonus-card-grid { grid-template-columns: 1fr !important; gap: 28px !important; }
            .testimonial-grid { grid-template-columns: 1fr; gap: 20px; }

            /* 3D Module & Bonus Mockup Stages */
            .bonus-card { margin: 0 auto; width: 100%; max-width: 440px; }
            .bonus-mockup-stage { min-height: 250px; padding: 30px 15px 35px; }
            .bonus-3d-book { width: 155px; height: 218px; transform: rotateY(-8deg) rotateX(3deg); }
            .bonus-3d-pages { transform: rotateY(90deg) translateZ(155px); }
            .bonus-3d-pedestal { width: 160px; }

            /* Price Stack / Recap Box Responsive */
            .price-stack-box { padding: 28px 18px !important; margin: 35px auto !important; border-radius: var(--radius-md) !important; }
            .price-current { font-size: 2.6rem !important; }
            
            /* Author Bio Card Responsive */
            .author-card { grid-template-columns: 1fr; text-align: center; padding: 28px 20px; gap: 25px; }
            .author-img { width: 220px; height: 280px; margin: 0 auto; }
            .author-content h3 { font-size: 1.6rem; }

            .quote-box-dark { padding: 25px 20px; margin: 30px 0; }
            .quote-box-dark p { font-size: 1.08rem; line-height: 1.6; }
        }

        @media (max-width: 576px) {
            .container { padding: 0 14px; }
            .top-bar { padding: 8px 8px; font-size: 0.78rem; gap: 6px; }
            .top-bar .timer-box { font-size: 0.9rem; padding: 2px 8px; }

            /* Smartphone Background Framing */
            .bg-section-blur::before {
                background-position: center 8%;
                filter: blur(1px) brightness(0.72) contrast(1.06);
            }
            .sec-hero::before { background-position: center 5%; }
            .sec-program::before { background-position: center 8%; }

            .hero-title { font-size: 1.75rem; }
            .hero-subtitle { font-size: 0.95rem; }
            .btn-cta { padding: 15px 18px; font-size: 1rem; }
            .btn-subtext { font-size: 0.78rem; }

            .book-container { width: 220px; height: 315px; }
            .book-main-title { font-size: 1.15rem; }
            .book-cover { padding: 14px; }
            .book-pages { transform: rotateY(90deg) translateZ(220px); }
            .book-shadow-pedestal { width: 220px; }

            .price-current { font-size: 2.1rem !important; }
            .guarantee-box { flex-direction: column; text-align: center; gap: 14px; padding: 18px 14px; }
            .guarantee-text { text-align: center !important; }
            .guarantee-icon { font-size: 2.4rem; }

            .pay-badge { font-size: 0.75rem; padding: 5px 9px; }
            .payment-badges { gap: 6px; }

            .card-dark { padding: 20px 16px; }
            .card-dark h4 { font-size: 1.1rem; }
            .card-dark p { font-size: 0.9rem; }
            
            .testimonial-card { padding: 20px 16px; }
            .testimonial-text { font-size: 0.9rem; }
            
            .faq-question { padding: 16px 16px; font-size: 0.92rem; }
            .faq-answer { padding: 0 16px; }
            .faq-item.active .faq-answer { padding: 0 16px 16px 16px; }
            .faq-answer p { font-size: 0.88rem; }

            .payment-callout-box { padding: 20px 14px; margin: 25px 0; }
            .payment-callout-box h3 { font-size: 1.02rem; }
            .payment-callout-box p { font-size: 0.92rem !important; }
        }

        
        
        /* LIVE SOCIAL PROOF NOTIFICATION TOAST (PURPLE INITIAL BADGE) */
        .social-proof-toast {
            position: fixed;
            bottom: 24px;
            left: 24px;
            z-index: 9999;
            background: rgba(14, 9, 26, 0.96);
            border: 1px solid var(--accent-purple);
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.9), 0 0 25px rgba(168, 85, 247, 0.45);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            max-width: 410px;
            backdrop-filter: blur(16px);
            transform: translateY(100px);
            opacity: 0;
            visibility: hidden;
            transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.5s ease, visibility 0.5s ease;
        }

        .social-proof-toast.active {
            transform: translateY(0);
            opacity: 1;
            visibility: visible;
        }

        .toast-content {
            display: flex;
            align-items: center;
            gap: 14px;
            position: relative;
        }

        /* Glowing Purple Initials Avatar Badge matching user screenshot */
        .toast-avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7e22ce 0%, #a855f7 100%);
            border: 2px solid #c084fc;
            box-shadow: 0 0 18px rgba(168, 85, 247, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
            font-weight: 900;
            color: #ffffff;
            font-family: var(--font-heading);
            letter-spacing: 0.5px;
            flex-shrink: 0;
            user-select: none;
        }

        .toast-text {
            flex-grow: 1;
            line-height: 1.35;
        }

        .toast-buyer {
            color: #ffffff;
            font-size: 0.9rem;
            margin: 0;
        }

        .toast-buyer strong {
            color: var(--accent-purple-glow);
            font-weight: 800;
        }

        .toast-loc {
            color: var(--text-dim);
            font-weight: 600;
            font-size: 0.82rem;
            margin-left: 4px;
        }

        .toast-product {
            color: var(--accent-gold);
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin: 3px 0 2px;
        }

        .toast-time {
            color: var(--text-dim);
            font-size: 0.72rem;
            display: block;
        }

        .toast-close {
            background: none;
            border: none;
            color: var(--text-dim);
            font-size: 1.2rem;
            cursor: pointer;
            padding: 0 4px;
            line-height: 1;
            transition: color 0.2s ease;
            position: absolute;
            top: -6px;
            right: -6px;
        }
        .toast-close:hover {
            color: #ffffff;
        }

        @media (max-width: 576px) {
            .social-proof-toast {
                left: 12px;
                right: 12px;
                bottom: 16px;
                max-width: none;
            }
        }

        
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

        .toast-flag-img {
            width: 20px;
            height: 14px;
            object-fit: cover;
            border-radius: 2px;
            vertical-align: middle;
            margin-left: 5px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.6);
            display: inline-block;
        }
    </style>





</head>
<body>

    <!-- Ambient Glow background -->
    <div class="ambient-glow glow-1"></div>
    <div class="ambient-glow glow-2"></div>

    <!-- Sticky Urgency Header -->
    <div class="top-bar">
        <div class="urgency-text">
            <i class="fa-solid fa-fire text-pink"></i>
            <span>LA PROMO EXPIRE DANS :</span>
        </div>
        <div class="timer-box" id="timer">23:59:59</div>
        <div class="urgency-text" style="font-size:0.85rem; opacity: 0.95;">
            (OFFRE FLASH -50% : LIMITÉE AUX 50 PREMIÈRES PERSONNES)
        </div>
        
                <!-- Multi-Language Selector Widget with HD Country Flags -->
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
        </div>
    </div>

    <!-- HERO SECTION WITH BLURRED DARK ARTWORK BACKGROUND -->
    <header class="section-padding hero-section bg-section-blur sec-hero">
        <div class="container">
            <div class="hero-grid">
                <!-- Left Column Text Content -->
                <div class="hero-content">
                    <div class="badge-flash">
                        <i class="fa-solid fa-star"></i> ÉDITION PREMIUM — OFFRE LIMITÉE
                    </div>
                    <h1 class="hero-title">
                        Je t’aide à <span class="highlight-text">augmenter ton attractivité</span> physique immédiatement.
                    </h1>
                    <p class="hero-subtitle">
                        Même si tu penses ne pas être “beau de base”, <strong>sans salle de sport, sans produits coûteux, et sans faux discours.</strong>
                    </p>

                    <a href="https://syalpfmx.mychariow.shop/prd_9gal1zvj/checkout" class="btn-cta">
                        <span>DEVENIR PLUS ATTIRANT DÈS MAINTENANT <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></span>
                    </a>


                </div>

                <!-- Right Column 3D Book Mockup with Smoke Emanating Directly out of Mockup -->
                <div class="mockup-wrapper">
                    <div class="book-container">
                        <!-- Direct Smoke Emitter inside the Mockup -->
                        <div class="mockup-direct-smoke">
                            <div class="smoke-cloud-inner m1"></div>
                            <div class="smoke-cloud-inner m2"></div>
                            <div class="smoke-cloud-inner m3"></div>
                            <div class="smoke-cloud-inner m4"></div>
                        </div>

                        <div class="book-spine">Glow Up Masculin</div>
                        <div class="book-cover">
                            <div class="book-cover-overlay"></div>
                            <div class="book-content">
                                <div class="book-author-tag">ÉDITION PREMIUM</div>
                                <div class="book-main-title">
                                    LE GUIDE ULTIME
                                    <span>POUR UN GLOW UP MASCULIN</span>
                                </div>
                                <div class="book-badge-tag">ÉDITION PREMIUM</div>
                            </div>
                        </div>
                        <div class="book-pages"></div>
                    </div>
                    <div class="book-shadow-pedestal"></div>
                </div>
            </div>
        </div>
    </header>

    <!-- TESTIMONIALS & VISUAL TRANSFORMATIONS SECTION (TOP PROOF BELOW HERO) -->
    <section class="section-padding bg-section-blur sec-testimonials">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-subtitle-tag">Transformations Réelles</span>
                <h2 class="section-title">Avant / Après : Les résultats spectaculaires après 30 jours</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 10px;">Découvre la métamorphose de ceux qui ont appliqué les 18 leviers d'attractivité du guide.</p>
            </div>

            <div class="transformations-full-grid">
                <!-- Full Visual Transformation #1 -->
                <div class="transform-card-wrapper">
                    <div class="transform-img-box">
                        <img src="images/testimonial_before_after_1.jpg" alt="Transformation Glow Up Avant / Après — Lucas (Lyon, France)">
                    </div>
                    <div class="transform-info-bar">
                        <div class="transform-author-name"><i class="fa-solid fa-circle-check" style="color: var(--accent-purple-bright); margin-right: 6px;"></i> Lucas, 19 ans</div>
                        <div class="transform-author-location"><i class="fa-solid fa-location-dot" style="margin-right: 4px;"></i> Lyon, France</div>
                    </div>
                </div>

                <!-- Full Visual Transformation #2 -->
                <div class="transform-card-wrapper">
                    <div class="transform-img-box">
                        <img src="images/testimonial_before_after_2.png" alt="Transformation Glow Up Avant / Après — Maxime (Paris, France)">
                    </div>
                    <div class="transform-info-bar">
                        <div class="transform-author-name"><i class="fa-solid fa-circle-check" style="color: var(--accent-purple-bright); margin-right: 6px;"></i> Maxime, 21 ans</div>
                        <div class="transform-author-location"><i class="fa-solid fa-location-dot" style="margin-right: 4px;"></i> Paris, France</div>
                    </div>
                </div>

                <!-- Full Visual Transformation #3 -->
                <div class="transform-card-wrapper">
                    <div class="transform-img-box">
                        <img src="images/testimonial_before_after_3.png" alt="Transformation Glow Up Avant / Après — Théo (Abidjan, Côte d'Ivoire)">
                    </div>
                    <div class="transform-info-bar">
                        <div class="transform-author-name"><i class="fa-solid fa-circle-check" style="color: var(--accent-purple-bright); margin-right: 6px;"></i> Théo, 26 ans</div>
                        <div class="transform-author-location"><i class="fa-solid fa-location-dot" style="margin-right: 4px;"></i> Abidjan, Côte d'Ivoire</div>
                    </div>
                </div>
            </div>

            <!-- CTA Button after top transformations -->
            <div style="text-align: center; margin-top: 35px;">
                <a href="https://syalpfmx.mychariow.shop/prd_9gal1zvj/checkout" class="btn-cta" style="display: inline-flex; width: auto; padding: 16px 36px;">
                    <span>OBTENIR MON GLOW UP MASCULIN <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></span>
                </a>
            </div>
        </div>
    </section>

    <!-- PAIN POINTS & REALITY SECTION WITH BLURRED DARK BACKGROUND -->
    <section class="section-padding bg-section-blur sec-pain">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-subtitle-tag">La Réalité Sans Filtre</span>
                <h2 class="section-title">Tu as l’impression que les autres ont “quelque chose en plus” que toi ?</h2>
            </div>

            <div class="cards-grid-3">
                <div class="card-dark">
                    <div class="card-icon crimson"><i class="fa-solid fa-eye-slash"></i></div>
                    <h4>Sentiment d'invisibilité</h4>
                    <p>Tu te regardes dans le miroir et tu te dis que tu pourrais être plus attirant et plus sûr de toi... mais tu ne sais pas par quoi commencer sans tomber dans des clichés ou des dépenses absurdes.</p>
                </div>

                <div class="card-dark">
                    <div class="card-icon"><i class="fa-solid fa-gem"></i></div>
                    <h4>La Beauté N'est Pas Un Don</h4>
                    <p>La vérité, c’est que la beauté masculine n’est pas réservée à une élite génétique. C’est un ensemble de leviers précis que très peu de gens connaissent et appliquent correctement.</p>
                </div>

                <div class="card-dark">
                    <div class="card-icon crimson"><i class="fa-solid fa-bullseye"></i></div>
                    <h4>Des Résultats Sans Chirurgie</h4>
                    <p>Ce guide a été conçu pour te donner les clés réelles d'une transformation d'image rapide, sans passer par la chirurgie, sans produits ruineux et sans faux discours.</p>
                </div>
            </div>


        </div>
    </section>

    <!-- TRANSFORMATION SECTION WITH BLURRED DARK RED AURA BACKGROUND -->
    <section class="section-padding bg-section-blur sec-transform">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-subtitle-tag">Prends Le Contrôle</span>
                <h2 class="section-title">Rends-toi compte de ce qui va changer...</h2>
            </div>

            <div class="quote-box-dark">
                <p>
                    “Pendant longtemps, tu te regardais sans vraiment t’aimer, avec ce doute constant qui te faisait te sentir inférieur ou invisible. Mais en appliquant ces leviers jour après jour, tu vas reprendre le contrôle de ton image, te sentir plus à l’aise dans ton corps, et imposer naturellement ta présence sans jamais avoir à forcer.”
                </p>
            </div>

            <div class="cards-grid-3">
                <div class="card-dark">
                    <div class="card-icon"><i class="fa-solid fa-1"></i></div>
                    <h4>1️⃣ Pourquoi tu en es là</h4>
                    <p>Tu n'es pas "moche". Tu n'as juste jamais appris à mettre ton potentiel en valeur. Personne ne t'a enseigné comment optimiser intelligemment tes traits et ta prestance.</p>
                </div>

                <div class="card-dark">
                    <div class="card-icon crimson"><i class="fa-solid fa-2"></i></div>
                    <h4>2️⃣ Ce que ta vie peut devenir</h4>
                    <p>Imagine-toi dans 30 jours : tu te regardes dans le miroir avec fierté, tu sors avec assurance, et le regard des autres change naturellement sans que tu n'aies rien à demander.</p>
                </div>

                <div class="card-dark">
                    <div class="card-icon"><i class="fa-solid fa-3"></i></div>
                    <h4>3️⃣ Pour qui est ce guide ?</h4>
                    <p>Pour l'homme qui veut des résultats concrets, plus de charisme et une présence affirmée. ❌ Pas fait pour ceux qui attendent une magie sans appliquer de conseils.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- PROGRAM CONTENT & BONUSES WITH BLURRED DARK BACKGROUND -->
    <section class="section-padding bg-section-blur sec-program">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-subtitle-tag">Contenu Du Guide</span>
                <h2 class="section-title">Voici exactement ce qui te rendra plus attirant</h2>
            </div>

            <!-- 6 MODULES 3D MOCKUP GRID WITH DIRECT MOCKUP SMOKE AND CUSTOM IMAGES -->
            <div class="bonus-card-grid" style="grid-template-columns: repeat(3, 1fr); gap: 28px; margin-bottom: 60px;">
                
                <!-- MODULE 1 3D MOCKUP -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag" style="color: var(--accent-crimson-bright);"><i class="fa-solid fa-fire"></i> 01</span>
                        <span class="bonus-val" style="border-color: var(--accent-crimson); color: #ffffff;">INCLUS</span>
                    </div>
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>
                            <div class="bonus-3d-spine">01</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/point1_blue_eyes_shirt.png');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">LA COMPÉTENCE<span>DU BEAU</span></div>
                                    <div class="bonus-3d-badge">01</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>
                    <div class="bonus-card-body">
                        <h4>Pourquoi paraître plus beau est une compétence, pas de la génétique</h4>
                        <p>Découvre les leviers psychologiques et visuels que 99% des hommes ignorent pour décupler ton esthétique naturelle.</p>
                    </div>
                </div>

                <!-- MODULE 2 3D MOCKUP -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag" style="color: var(--accent-crimson-bright);"><i class="fa-solid fa-bolt"></i> 02</span>
                        <span class="bonus-val" style="border-color: var(--accent-crimson); color: #ffffff;">INCLUS</span>
                    </div>
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>
                            <div class="bonus-3d-spine">02</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/point2_black_curly_hair.png');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">LES 18 LEVIERS<span>INVISIBLES</span></div>
                                    <div class="bonus-3d-badge">02</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>
                    <div class="bonus-card-body">
                        <h4>Les 18 leviers invisibles de l’attractivité masculine ultra-efficaces</h4>
                        <p>Le guide stratégique complet dévoilant les 18 secrets subtils qui déclenchent une attraction spontanée.</p>
                    </div>
                </div>

                <!-- MODULE 3 3D MOCKUP -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag" style="color: var(--accent-crimson-bright);"><i class="fa-solid fa-triangle-exclamation"></i> 03</span>
                        <span class="bonus-val" style="border-color: var(--accent-crimson); color: #ffffff;">INCLUS</span>
                    </div>
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>
                            <div class="bonus-3d-spine">03</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/point3_suit_sofa.png');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">PIÈGES & ERREURS<span>À ÉVITER</span></div>
                                    <div class="bonus-3d-badge">03</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>
                    <div class="bonus-card-body">
                        <h4>Les erreurs courantes qui ruinent ton image sans que tu le saches</h4>
                        <p>Identifie et éradique instantanément les faux pas de style et de posture qui détruisent ton charisme au quotidien.</p>
                    </div>
                </div>

                <!-- MODULE 4 3D MOCKUP -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag" style="color: var(--accent-crimson-bright);"><i class="fa-solid fa-eye"></i> 04</span>
                        <span class="bonus-val" style="border-color: var(--accent-crimson); color: #ffffff;">INCLUS</span>
                    </div>
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>
                            <div class="bonus-3d-spine">04</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/point4_glasses_suit.png');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">POSTURE & REGARD<span>CAPTIVANT</span></div>
                                    <div class="bonus-3d-badge">04</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>
                    <div class="bonus-card-body">
                        <h4>Posture, regard, style et détails visuels qui captivent l'attention</h4>
                        <p>Maîtrise le langage corporel alpha, la communication non-verbale et la puissance d'un regard hypnotique.</p>
                    </div>
                </div>

                <!-- MODULE 5 3D MOCKUP -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag" style="color: var(--accent-crimson-bright);"><i class="fa-solid fa-stopwatch"></i> 05</span>
                        <span class="bonus-val" style="border-color: var(--accent-crimson); color: #ffffff;">INCLUS</span>
                    </div>
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>
                            <div class="bonus-3d-spine">05</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/point5_denim_jacket_bag.png');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">L'IMPRESSION EN<span>3 SECONDES</span></div>
                                    <div class="bonus-3d-badge">05</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>
                    <div class="bonus-card-body">
                        <h4>Comment créer une première impression marquante en seulement 3 secondes</h4>
                        <p>Captive immédiatement le regard de tes interlocuteurs dès l'instant où tu entres dans n'importe quelle pièce.</p>
                    </div>
                </div>

                <!-- MODULE 6 3D MOCKUP -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag" style="color: var(--accent-crimson-bright);"><i class="fa-solid fa-calendar-check"></i> 06</span>
                        <span class="bonus-val" style="border-color: var(--accent-crimson); color: #ffffff;">INCLUS</span>
                    </div>
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>
                            <div class="bonus-3d-spine">06</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/point6_sunglasses_white_shirt.png');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">PLAN D'ACTION<span>30 JOURS</span></div>
                                    <div class="bonus-3d-badge">06</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>
                    <div class="bonus-card-body">
                        <h4>Un plan d’action pas à pas sur 30 jours pour métamorphoser ton style</h4>
                        <p>La feuille de route quotidienne étape par étape pour ancrer définitivement ta transformation d'image.</p>
                    </div>
                </div>
            </div>

            <!-- CTA Button after 6 Modules -->
            <div style="text-align: center; margin: 35px 0 50px;">
                <a href="https://syalpfmx.mychariow.shop/prd_9gal1zvj/checkout" class="btn-cta" style="display: inline-flex; width: auto; padding: 16px 36px;">
                    <span>ACCÉDER AUX 6 MODULES DU GUIDE <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></span>
                </a>
            </div>

            <!-- BONUSES GRID WITH SMOKE EMANATING DIRECTLY FROM EACH MOCKUP BOOK -->
            <div class="section-title-wrap" style="margin-top: 60px; margin-bottom: 30px;">
                <span class="section-subtitle-tag">Cadeaux Exclusifs</span>
                <h2 class="section-title">3 Bonus Offerts Pour Une Transformation Complète</h2>
            </div>

            <div class="bonus-card-grid">
                <!-- Bonus 1 3D MOCKUP WITH DIRECT MOCKUP SMOKE -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag">🎁 BONUS 1</span>
                        <span class="bonus-val">Valeur 19 €</span>
                    </div>
                    
                    <!-- 3D Mockup Area -->
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <!-- Direct Smoke Emitter inside Mockup -->
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>

                            <div class="bonus-3d-spine">Bonus 1</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/glowup_messy_hair_chain.jpg');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">
                                        CHECK-LIST
                                        <span>APPARENCE MAÎTRISÉE</span>
                                    </div>
                                    <div class="bonus-3d-badge">GUIDE EXCLUSIF</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>

                    <div class="bonus-card-body">
                        <h4>Check-list “Apparence Maîtrisée”</h4>
                        <p>Une check-list rapide à utiliser avant chaque sortie pour t'assurer d'une tenue, d'une posture et d'une attitude irréprochables sans douter.</p>
                    </div>
                </div>

                <!-- Bonus 2 3D MOCKUP WITH DIRECT MOCKUP SMOKE -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag">🎁 BONUS 2</span>
                        <span class="bonus-val">Valeur 27 €</span>
                    </div>

                    <!-- 3D Mockup Area -->
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <!-- Direct Smoke Emitter inside Mockup -->
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>

                            <div class="bonus-3d-spine">Bonus 2</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/glowup_bonus2_manhwa.jpg');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">
                                        LES ERREURS
                                        <span>INVISIBLES</span>
                                    </div>
                                    <div class="bonus-3d-badge">DOSSIER SECRET</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>

                    <div class="bonus-card-body">
                        <h4>Les Erreurs Invisibles</h4>
                        <p>Révèle les pièges subtils faits par 90% des hommes qui gâchent leur charisme : attitudes, détails vestimentaires et langage corporel à corriger.</p>
                    </div>
                </div>

                <!-- Bonus 3 3D MOCKUP WITH DIRECT MOCKUP SMOKE -->
                <div class="bonus-card">
                    <div class="bonus-card-header">
                        <span class="bonus-tag">🎁 BONUS 3</span>
                        <span class="bonus-val">Valeur 17 €</span>
                    </div>

                    <!-- 3D Mockup Area -->
                    <div class="bonus-mockup-stage">
                        <div class="bonus-3d-book">
                            <!-- Direct Smoke Emitter inside Mockup -->
                            <div class="mockup-direct-smoke">
                                <div class="smoke-cloud-inner m1"></div>
                                <div class="smoke-cloud-inner m2"></div>
                                <div class="smoke-cloud-inner m3"></div>
                                <div class="smoke-cloud-inner m4"></div>
                            </div>

                            <div class="bonus-3d-spine">Bonus 3</div>
                            <div class="bonus-3d-cover" style="background-image: url('images/glowup_bonus3_suit.jpg');">
                                <div class="bonus-3d-overlay"></div>
                                <div class="bonus-3d-content">
                                    <div class="bonus-3d-title">
                                        ROUTINE
                                        <span>ASSURANCE VISUELLE</span>
                                    </div>
                                    <div class="bonus-3d-badge">PROGRAMME 30J</div>
                                </div>
                            </div>
                            <div class="bonus-3d-pages"></div>
                        </div>
                        <div class="bonus-3d-pedestal"></div>
                    </div>

                    <div class="bonus-card-body">
                        <h4>Routine d'Assurance Visuelle</h4>
                        <p>Une routine quotidienne de quelques minutes pour ancrer automatiquement un regard confiant, une posture droite et une présence naturelle.</p>
                    </div>
                </div>
            </div>

            <!-- PRICE & STACK RECAP BOX FOLLOWING EXACT REQUESTED STRUCTURE -->
            <div class="price-stack-box" style="text-align: left; max-width: 900px; margin: 50px auto;">
                <!-- Alert Header Badge -->
                <div style="background: rgba(225, 29, 72, 0.25); border: 1px solid var(--accent-crimson); color: #ffffff; padding: 12px 20px; border-radius: var(--radius-md); font-size: 1rem; font-weight: 800; text-transform: uppercase; text-align: center; margin-bottom: 25px; box-shadow: 0 0 20px rgba(225, 29, 72, 0.4);">
                    ⚠️ ATTENTION : OFFRE SPÉCIALE D'ACCÈS IMMÉDIAT !
                </div>

                <!-- Main Box Title -->
                <h3 style="font-family: var(--font-heading); font-size: 1.6rem; font-weight: 900; color: #ffffff; text-align: center; margin-bottom: 25px; text-transform: uppercase;">
                    VOICI LE RÉCAPITULATIF DE TOUT CE QUE VOUS ALLEZ RECEVOIR
                </h3>

                <!-- Stack Items List -->
                <div style="background: rgba(0, 0, 0, 0.6); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 25px; margin-bottom: 30px;">
                    <div style="font-size: 1.15rem; font-weight: 800; color: #ffffff; margin-bottom: 8px; display: flex; align-items: center; gap: 10px;">
                        <i class="fa-solid fa-circle-check" style="color: var(--accent-crimson-bright);"></i>
                        <span>ACCÈS IMMÉDIAT AU PROGRAMME "LE GUIDE ULTIME POUR UN GLOW UP MASCULIN"</span>
                    </div>
                    <div style="color: var(--text-dim); font-size: 0.9rem; margin-left: 30px; margin-bottom: 18px;">
                        Format numérique téléchargeable sécurisé
                    </div>

                    <ul style="list-style: none; padding-left: 0; display: flex; flex-direction: column; gap: 12px;">
                        <li style="color: var(--text-main); font-size: 1rem; font-weight: 600; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed rgba(255,255,255,0.1); padding-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                            <span style="display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-check" style="color: var(--accent-purple-bright);"></i> Les 18 Leviers Complets du Guide</span>
                            <span style="color: var(--text-muted); font-size: 0.92rem; white-space: nowrap;">Valeur : 19 800 FCFA / 30 €</span>
                        </li>
                        <li style="color: var(--text-main); font-size: 1rem; font-weight: 600; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed rgba(255,255,255,0.1); padding-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                            <span style="display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-gift" style="color: var(--accent-gold);"></i> BONUS #1 : Check-list “Apparence Maîtrisée”</span>
                            <span style="color: var(--accent-gold); font-size: 0.92rem; white-space: nowrap;">Valeur : 12 500 FCFA / 19 € (GRATUIT)</span>
                        </li>
                        <li style="color: var(--text-main); font-size: 1rem; font-weight: 600; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed rgba(255,255,255,0.1); padding-bottom: 10px; flex-wrap: wrap; gap: 8px;">
                            <span style="display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-gift" style="color: var(--accent-gold);"></i> BONUS #2 : Les 10 Erreurs Invisibles à éviter</span>
                            <span style="color: var(--accent-gold); font-size: 0.92rem; white-space: nowrap;">Valeur : 17 500 FCFA / 27 € (GRATUIT)</span>
                        </li>
                        <li style="color: var(--text-main); font-size: 1rem; font-weight: 600; display: flex; justify-content: space-between; align-items: center; padding-bottom: 4px; flex-wrap: wrap; gap: 8px;">
                            <span style="display: flex; align-items: center; gap: 8px;"><i class="fa-solid fa-gift" style="color: var(--accent-gold);"></i> BONUS #3 : Routine d'Assurance Visuelle (30 Jours)</span>
                            <span style="color: var(--accent-gold); font-size: 0.92rem; white-space: nowrap;">Valeur : 11 000 FCFA / 17 € (GRATUIT)</span>
                        </li>
                    </ul>
                </div>

                <!-- Pricing Values Breakdown -->
                <div style="text-align: center; margin-bottom: 30px;">
                    <div style="font-size: 1.1rem; color: var(--text-muted); font-weight: 700; margin-bottom: 6px;">
                        VALEUR TOTALE DU PROGRAMME : <span style="text-decoration: line-through; color: var(--text-dim);">60 800 FCFA / 93 €</span>
                    </div>
                    <div style="font-size: 1.2rem; color: var(--text-main); font-weight: 800; margin-bottom: 18px;">
                        PRIX HABITUEL : <span style="text-decoration: line-through; color: var(--text-dim);">19 800 FCFA / 30 €</span>
                    </div>

                    <div style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 12px; flex-wrap: wrap;">
                        <span style="font-size: 1.8rem; text-decoration: line-through; color: var(--text-dim); font-weight: 700;">19 800 FCFA</span>
                        <span style="font-size: 3.2rem; font-weight: 900; color: #ffffff; font-family: var(--font-heading);">9 900 FCFA</span>
                        <span style="background: var(--accent-crimson); color: #ffffff; padding: 6px 14px; border-radius: var(--radius-full); font-weight: 800; font-size: 1rem;">-50% AUJOURD'HUI</span>
                    </div>

                    <div style="font-size: 1.15rem; color: var(--accent-gold); font-weight: 800;">
                        Soit seulement 15 € <span style="font-size: 0.95rem; color: var(--text-muted); font-weight: 600;">(Offre valable jusqu'à ce soir 23h59)</span>
                    </div>
                </div>

                <!-- Main CTA Button with Link -->
                <a href="https://syalpfmx.mychariow.shop/prd_9gal1zvj/checkout" class="btn-cta" style="margin-bottom: 20px;">
                    <span>JE REJOINS LE PROGRAMME MAINTENANT <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></span>
                </a>

                <!-- Mobile Money & Payment Method Badges Grid -->
                <div class="payment-badges" style="justify-content: center; gap: 8px; margin-bottom: 25px;">
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Wave</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> MTN Mobile Money</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Moov Money</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Orange Money</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Airtel Money</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Free Sénégal</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Celtis Cash</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Coris Money</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Tmoney</span>
                    <span class="pay-badge"><i class="fa-solid fa-credit-card"></i> Carte Bancaire (VISA/Mastercard)</span>
                </div>

                <!-- Guarantee -->
                <div class="guarantee-box" style="margin-top: 20px;">
                    <i class="fa-solid fa-shield-halved guarantee-icon"></i>
                    <div class="guarantee-text" style="text-align: left;">
                        <h4>Garantie 100% "Satisfait ou Remboursé" pendant 15 jours</h4>
                        <p>Si après 15 jours d'application des conseils du guide tu n'observes aucun changement positif sur ton attractivité, envoie un simple message et tu seras intégralement remboursé.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- TESTIMONIALS & VISUAL TRANSFORMATIONS SECTION -->
    <section class="section-padding bg-section-blur sec-testimonials">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-subtitle-tag">Transformations Réelles</span>
                <h2 class="section-title">Avant / Après : Les résultats spectaculaires après 30 jours</h2>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-top: 10px;">Découvre la métamorphose de ceux qui ont appliqué les 18 leviers d'attractivité du guide.</p>
            </div>

            <div class="transformations-full-grid">
                <!-- Full Visual Transformation #1 -->
                <div class="transform-card-wrapper">
                    <div class="transform-img-box">
                        <img src="images/testimonial_before_after_1.jpg" alt="Transformation Glow Up Avant / Après — Lucas (Lyon, France)">
                    </div>
                    <div class="transform-info-bar">
                        <div class="transform-author-name"><i class="fa-solid fa-circle-check" style="color: var(--accent-purple-bright); margin-right: 6px;"></i> Lucas, 19 ans</div>
                        <div class="transform-author-location"><i class="fa-solid fa-location-dot" style="margin-right: 4px;"></i> Lyon, France</div>
                    </div>
                </div>

                <!-- Full Visual Transformation #2 -->
                <div class="transform-card-wrapper">
                    <div class="transform-img-box">
                        <img src="images/testimonial_before_after_2.png" alt="Transformation Glow Up Avant / Après — Maxime (Paris, France)">
                    </div>
                    <div class="transform-info-bar">
                        <div class="transform-author-name"><i class="fa-solid fa-circle-check" style="color: var(--accent-purple-bright); margin-right: 6px;"></i> Maxime, 21 ans</div>
                        <div class="transform-author-location"><i class="fa-solid fa-location-dot" style="margin-right: 4px;"></i> Paris, France</div>
                    </div>
                </div>

                <!-- Full Visual Transformation #3 -->
                <div class="transform-card-wrapper">
                    <div class="transform-img-box">
                        <img src="images/testimonial_before_after_3.png" alt="Transformation Glow Up Avant / Après — Théo (Abidjan, Côte d'Ivoire)">
                    </div>
                    <div class="transform-info-bar">
                        <div class="transform-author-name"><i class="fa-solid fa-circle-check" style="color: var(--accent-purple-bright); margin-right: 6px;"></i> Théo, 26 ans</div>
                        <div class="transform-author-location"><i class="fa-solid fa-location-dot" style="margin-right: 4px;"></i> Abidjan, Côte d'Ivoire</div>
                    </div>
                </div>
            </div>

            <!-- CTA Button after second transformations section -->
            <div style="text-align: center; margin-top: 35px;">
                <a href="https://syalpfmx.mychariow.shop/prd_9gal1zvj/checkout" class="btn-cta" style="display: inline-flex; width: auto; padding: 16px 36px;">
                    <span>REJOINDRE CEUX QUI ONT TRANSFORMÉ LEUR IMAGE <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></span>
                </a>
            </div>
        </div>
    </section>

    <!-- 1. FAQ SECTION -->
    <section class="section-padding bg-section-blur sec-faq">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-subtitle-tag">Foire Aux Questions</span>
                <h2 class="section-title">Les questions fréquemment posées</h2>
            </div>

            <div class="faq-accordion" style="max-width: 820px; margin: 0 auto;">
                <div class="faq-item active">
                    <div class="faq-question">
                        <span>1. Est-ce que ce guide fonctionne vraiment ?</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </div>
                    <div class="faq-answer">
                        <p>Oui. Les 18 leviers sont simples, concrets et basés sur la psychologie de l'attraction et de l'image. Beaucoup d'hommes ont déjà transformé leur présence en 30 jours.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>2. Ai-je besoin de changer complètement mon apparence ?</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </div>
                    <div class="faq-answer">
                        <p>Non. Ce guide t’apprend à optimiser ce que tu as déjà et à corriger les erreurs invisibles qui sabotent ton image au quotidien sans te dénaturer.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>3. Combien de temps faut-il pour voir des résultats ?</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </div>
                    <div class="faq-answer">
                        <p>Certains ajustements (posture, regard, premières impressions) donnent des résultats immédiats. La transformation complète s'ancrera en 30 jours d'application.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>4. Ce guide convient-il à tous les âges ?</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </div>
                    <div class="faq-answer">
                        <p>Oui, il est pensé pour les jeunes adultes et hommes de tous âges. Les principes d'attractivité masculine sont universels.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    

    <!-- 3. FINAL CONVERSION SECTION -->
    <section class="section-padding bg-section-blur sec-footer">
        <div class="container" style="max-width: 800px;">
            <div class="payment-callout-box" style="margin: 0; text-align: center; padding: 40px;">
                <div style="color: var(--accent-gold); font-size: 0.9rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px;">
                    ⚡ ULTIME CHANCE POUR PROFITER DE L'OFFRE
                </div>
                <h3 style="font-family: var(--font-heading); font-size: 2.1rem; font-weight: 900; color: #ffffff; margin-bottom: 14px; line-height: 1.25;">
                    Passe à l'action et métamorphose ton image dès aujourd'hui
                </h3>
                <p style="color: var(--text-muted); font-size: 1.05rem; margin-bottom: 24px; line-height: 1.6;">
                    Accède immédiatement au programme complet avec les 18 leviers d'attractivité et les 3 cadeaux bonus exclusifs.
                </p>

                <a href="https://syalpfmx.mychariow.shop/prd_9gal1zvj/checkout" class="btn-cta" style="margin-bottom: 20px;">
                    <span>JE REJOINS LE PROGRAMME MAINTENANT <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></span>
                </a>

                <div class="payment-badges" style="justify-content: center; gap: 8px;">
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Wave</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> MTN</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Moov</span>
                    <span class="pay-badge"><i class="fa-solid fa-mobile-button"></i> Orange</span>
                    <span class="pay-badge"><i class="fa-solid fa-credit-card"></i> Carte Bancaire</span>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER CREDITS BAR -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2026 . Tous droits réservés. — Le Guide ULTIME Pour un Glow Up Masculin.</p>
            <p style="margin-top: 8px; font-size: 0.8rem;">Paiements sécurisés via Mobile Money & Cartes bancaires.</p>
        </div>
    </footer>

    
    
    
    
    <!-- LIVE SOCIAL PROOF SALES NOTIFICATION TOAST -->
    <div id="social-proof-toast" class="social-proof-toast">
        <div class="toast-content">
            <button class="toast-close" onclick="closeSocialProofToast()">&times;</button>
            <div class="toast-avatar" id="toast-initials">
                LU
            </div>
            <div class="toast-text">
                <p class="toast-buyer"><strong id="toast-name">Lucas</strong> <span id="toast-location" class="toast-loc">Lyon, France <img id="toast-flag" src="https://flagcdn.com/w40/fr.png" alt="Drapeau" class="toast-flag-img"></span></p>
                <p class="toast-product">vient de rejoindre LE GUIDE ULTIME</p>
                <span class="toast-time" id="toast-time">Il y a 3 min • Achat vérifié 🟢</span>
            </div>
        </div>
    </div>

    </div>

    </div>

    </div>

    <!-- INTERACTIVE SCRIPTS -->
    <script>
        // Persistent 24-Hour Countdown Timer (Saved in localStorage)
        function start24hTimer() {
            const display = document.querySelector('#timer');
            if (!display) return;

            const TIMER_KEY = 'glowup_24h_timer_endtime';
            const DURATION = 24 * 60 * 60 * 1000; // 24 Hours in ms

            let endTime = localStorage.getItem(TIMER_KEY);
            const now = Date.now();

            if (!endTime || isNaN(endTime) || now >= parseInt(endTime, 10)) {
                endTime = now + DURATION;
                localStorage.setItem(TIMER_KEY, endTime);
            } else {
                endTime = parseInt(endTime, 10);
            }

            function updateDisplay() {
                const currentTime = Date.now();
                let diff = Math.max(0, Math.floor((endTime - currentTime) / 1000));

                if (diff <= 0) {
                    endTime = Date.now() + DURATION;
                    localStorage.setItem(TIMER_KEY, endTime);
                    diff = Math.floor(DURATION / 1000);
                }

                const hours = Math.floor(diff / 3600);
                const minutes = Math.floor((diff % 3600) / 60);
                const seconds = diff % 60;

                const hStr = hours < 10 ? "0" + hours : hours;
                const mStr = minutes < 10 ? "0" + minutes : minutes;
                const sStr = seconds < 10 ? "0" + seconds : seconds;

                display.textContent = hStr + ":" + mStr + ":" + sStr;
            }

            updateDisplay();
            setInterval(updateDisplay, 1000);
        }

        
        
        
        // Live International Social Proof Sales Notifications Engine (Crisp Flag CDN Images)
        const salesNotifications = [
            // EUROPE
            { initials: "LU", name: "Lucas", city: "Lyon", country: "France", flag: "https://flagcdn.com/w40/fr.png", time: "Il y a 3 minutes" },
            { initials: "MA", name: "Maxime", city: "Paris", country: "France", flag: "https://flagcdn.com/w40/fr.png", time: "Il y a 45 minutes" },
            { initials: "RA", name: "Rayan", city: "Bruxelles", country: "Belgique", flag: "https://flagcdn.com/w40/be.png", time: "Il y a 2 heures" },
            { initials: "JU", name: "Julien", city: "Genève", country: "Suisse", flag: "https://flagcdn.com/w40/ch.png", time: "Il y a 5 heures" },
            { initials: "LI", name: "Liam", city: "Londres", country: "Royaume-Uni", flag: "https://flagcdn.com/w40/gb.png", time: "Il y a 1 jour" },

            // AFRIQUE
            { initials: "TH", name: "Théo", city: "Abidjan", country: "Côte d'Ivoire", flag: "https://flagcdn.com/w40/ci.png", time: "Il y a 12 minutes" },
            { initials: "AL", name: "Alexandre", city: "Dakar", country: "Sénégal", flag: "https://flagcdn.com/w40/sn.png", time: "Il y a 4 heures" },
            { initials: "DY", name: "Dylan", city: "Douala", country: "Cameroun", flag: "https://flagcdn.com/w40/cm.png", time: "Il y a 2 jours" },
            { initials: "MO", name: "Mohamed", city: "Casablanca", country: "Maroc", flag: "https://flagcdn.com/w40/ma.png", time: "Il y a 1 semaine" },
            { initials: "AN", name: "Antoine", city: "Lomé", country: "Togo", flag: "https://flagcdn.com/w40/tg.png", time: "Il y a 8 heures" },
            { initials: "CE", name: "Cédric", city: "Kinshasa", country: "RDC", flag: "https://flagcdn.com/w40/cd.png", time: "Il y a 3 jours" },

            // AMÉRIQUE & CARAÏBES
            { initials: "SA", name: "Samuel", city: "Montréal", country: "Canada", flag: "https://flagcdn.com/w40/ca.png", time: "Il y a 25 minutes" },
            { initials: "JO", name: "Jordan", city: "Miami", country: "États-Unis", flag: "https://flagcdn.com/w40/us.png", time: "Il y a 6 heures" },
            { initials: "EN", name: "Enzo", city: "Fort-de-France", country: "Martinique", flag: "https://flagcdn.com/w40/mq.png", time: "Il y a 1 jour" },
            { initials: "GA", name: "Gabriel", city: "São Paulo", country: "Brésil", flag: "https://flagcdn.com/w40/br.png", time: "Il y a 4 jours" },

            // AUTRES CONTINENTS & DOM-TOM
            { initials: "KA", name: "Karim", city: "Dubaï", country: "Émirats Arabes", flag: "https://flagcdn.com/w40/ae.png", time: "Il y a 2 semaines" },
            { initials: "MT", name: "Mathieu", city: "Saint-Denis", country: "La Réunion", flag: "https://flagcdn.com/w40/re.png", time: "Il y a 14 minutes" },
            { initials: "KE", name: "Kevin", city: "Bordeaux", country: "France", flag: "https://flagcdn.com/w40/fr.png", time: "Il y a 3 heures" },
            { initials: "YO", name: "Youssef", city: "Tunis", country: "Tunisie", flag: "https://flagcdn.com/w40/tn.png", time: "Il y a 2 jours" },
            { initials: "IS", name: "Ismaël", city: "Bamako", country: "Mali", flag: "https://flagcdn.com/w40/ml.png", time: "Il y a 10 heures" },
            { initials: "DA", name: "David", city: "Pointe-à-Pitre", country: "Guadeloupe", flag: "https://flagcdn.com/w40/gp.png", time: "Il y a 1 semaine" },
            { initials: "KO", name: "Kofi", city: "Accra", country: "Ghana", flag: "https://flagcdn.com/w40/gh.png", time: "Il y a 5 jours" },
            { initials: "KJ", name: "Kenji", city: "Tokyo", country: "Japon", flag: "https://flagcdn.com/w40/jp.png", time: "Il y a 18 heures" },
            { initials: "RO", name: "Romain", city: "Luxembourg", country: "Luxembourg", flag: "https://flagcdn.com/w40/lu.png", time: "Il y a 35 minutes" },
            { initials: "BR", name: "Brice", city: "Cotonou", country: "Bénin", flag: "https://flagcdn.com/w40/bj.png", time: "Il y a 2 heures" }
        ];

        let currentNotificationIndex = 0;

        function showSocialProofNotification() {
            const toast = document.querySelector('#social-proof-toast');
            const nameEl = document.querySelector('#toast-name');
            const locEl = document.querySelector('#toast-location');
            const timeEl = document.querySelector('#toast-time');
            const initialsEl = document.querySelector('#toast-initials');
            if (!toast || !nameEl || !timeEl || !initialsEl) return;

            const notif = salesNotifications[currentNotificationIndex];
            nameEl.textContent = notif.name;
            if (locEl) {
                locEl.innerHTML = notif.city + ', ' + notif.country + ' <img src="' + notif.flag + '" alt="Drapeau ' + notif.country + '" class="toast-flag-img">';
            }
            timeEl.textContent = notif.time + ' • Achat vérifié 🟢';
            initialsEl.textContent = notif.initials;

            toast.classList.add('active');

            setTimeout(() => {
                toast.classList.remove('active');
                currentNotificationIndex = (currentNotificationIndex + 1) % salesNotifications.length;

                const nextDelay = Math.floor(Math.random() * 2500) + 3500;
                setTimeout(showSocialProofNotification, nextDelay);
            }, 4000);
        }


        function closeSocialProofToast() {
            const toast = document.querySelector('#social-proof-toast');
            if (toast) {
                toast.classList.remove('active');
            }
        }

        // Accordion Interactivity
        document.querySelectorAll('.faq-question').forEach(q => {
            q.addEventListener('click', () => {
                const item = q.parentElement;
                const isActive = item.classList.contains('active');
                
                document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
                
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        });

        // Initialize on load
        window.addEventListener('load', () => {
            start24hTimer();
            setTimeout(showSocialProofNotification, 2500);
        });
    </script>


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
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</body>

</html>
'''

with open(r'C:\Users\HP TTS\.gemini\antigravity\scratch\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'C:\Users\HP TTS\.gemini\antigravity\scratch\landing_page.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully updated landing page with dark blurred background images on EVERY section and pitch black theme!")
