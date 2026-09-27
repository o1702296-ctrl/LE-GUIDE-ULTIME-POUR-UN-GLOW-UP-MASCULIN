import os
import base64

output_dir = r'C:\Users\HP TTS\.gemini\antigravity\scratch\sauver-ton-couple-landing'
os.makedirs(output_dir, exist_ok=True)
html_file = os.path.join(output_dir, 'index.html')

book_img_path = r'C:\Users\HP TTS\.gemini\antigravity\brain\f7c99c96-882b-4d26-9e07-2efd257a1816\.user_uploaded\media__1789510600647.png'

with open(book_img_path, 'rb') as f:
    b64_book = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Helper to build exact 7-box 3D cascade + dual laptop V-stage matching Éloquence 2.0 image with official book cover on centerpiece box
def create_grand_eloquence_bundle_html(book_img):
    return f'''
    <div class="grand-bundle-stage">
        <!-- Central Violet Glow Halo -->
        <div class="grand-halo-circle"></div>

        <!-- 7-Box Cascade Stack behind laptops -->
        <div class="grand-box-cascade">
            <!-- Box 1: Module 1 (Far Left Front) -->
            <div class="elo-box box-pos-1">
                <div class="elo-box-top"></div>
                <div class="elo-box-spine"><span>SAUVER TON COUPLE — MODULE 1</span></div>
                <div class="elo-box-front">
                    <div class="elo-top-dark">
                        <h4>SAUVER TON COUPLE</h4>
                        <p>PSYCHOLOGIE FÉMININE</p>
                    </div>
                    <div class="elo-mid-light">
                        <div class="elo-circle-icon"><i class="fa-solid fa-heart-crack"></i></div>
                    </div>
                    <div class="elo-pill-footer">Module 1 : Causes des Tensions</div>
                </div>
            </div>

            <!-- Box 2: Module 2 (Mid Left) -->
            <div class="elo-box box-pos-2">
                <div class="elo-box-top"></div>
                <div class="elo-box-spine"><span>SAUVER TON COUPLE — MODULE 2</span></div>
                <div class="elo-box-front">
                    <div class="elo-top-dark">
                        <h4>SAUVER TON COUPLE</h4>
                        <p>COMMUNICATION SAINE</p>
                    </div>
                    <div class="elo-mid-light">
                        <div class="elo-circle-icon"><i class="fa-solid fa-comments"></i></div>
                    </div>
                    <div class="elo-pill-footer">Module 2 : Dialogue Sans Dispute</div>
                </div>
            </div>

            <!-- Box 3: Module 3 (Back Left) -->
            <div class="elo-box box-pos-3">
                <div class="elo-box-top"></div>
                <div class="elo-box-spine"><span>SAUVER TON COUPLE — MODULE 3</span></div>
                <div class="elo-box-front">
                    <div class="elo-top-dark">
                        <h4>SAUVER TON COUPLE</h4>
                        <p>POSTURE DU LEADER</p>
                    </div>
                    <div class="elo-mid-light">
                        <div class="elo-circle-icon"><i class="fa-solid fa-user-tie"></i></div>
                    </div>
                    <div class="elo-pill-footer">Module 3 : Dignité & Respect</div>
                </div>
            </div>

            <!-- Box 4: Centerpiece Main Box featuring Official Book Cover artwork -->
            <div class="elo-box box-pos-center">
                <div class="elo-box-top"></div>
                <div class="elo-box-spine"><span>PACK INTÉGRAL — SAUVER TON COUPLE</span></div>
                <div class="elo-box-front official-cover-front">
                    <img src="{book_img}" alt="Livre Officiel Sauver Ton Couple" class="box-official-cover-img">
                </div>
            </div>

            <!-- Box 5: Bonus 1 (Back Right) -->
            <div class="elo-box box-pos-5">
                <div class="elo-box-top"></div>
                <div class="elo-box-spine"><span>SAUVER TON COUPLE — BONUS #1</span></div>
                <div class="elo-box-front">
                    <div class="elo-top-dark">
                        <h4>SAUVER TON COUPLE</h4>
                        <p>GUIDE D'URGENCE</p>
                    </div>
                    <div class="elo-mid-light">
                        <div class="elo-seal-badge">BONUS</div>
                        <div class="elo-circle-icon"><i class="fa-solid fa-shield-halved"></i></div>
                    </div>
                    <div class="elo-pill-footer">Bonus #1 : Plan Anti-Dispute</div>
                </div>
            </div>

            <!-- Box 6: Bonus 2 (Mid Right) -->
            <div class="elo-box box-pos-6">
                <div class="elo-box-top"></div>
                <div class="elo-box-spine"><span>SAUVER TON COUPLE — BONUS #2</span></div>
                <div class="elo-box-front">
                    <div class="elo-top-dark">
                        <h4>SAUVER TON COUPLE</h4>
                        <p>FEUILLE DE ROUTE</p>
                    </div>
                    <div class="elo-mid-light">
                        <div class="elo-seal-badge">BONUS</div>
                        <div class="elo-circle-icon"><i class="fa-solid fa-calendar-check"></i></div>
                    </div>
                    <div class="elo-pill-footer">Bonus #2 : Plan 30 Jours</div>
                </div>
            </div>

            <!-- Box 7: Guarantee Box (Far Right Front) -->
            <div class="elo-box box-pos-7">
                <div class="elo-box-top"></div>
                <div class="elo-box-spine"><span>GARANTIE 30 JOURS</span></div>
                <div class="elo-box-front">
                    <div class="elo-top-dark">
                        <h4>SAUVER TON COUPLE</h4>
                        <p>SATISFAIT OU REMBOURSÉ</p>
                    </div>
                    <div class="elo-mid-light">
                        <div class="elo-guarantee-round-seal">
                            <span>100%</span>
                            <strong>GARANTI</strong>
                        </div>
                    </div>
                    <div class="elo-pill-footer">Garantie 30 Jours</div>
                </div>
            </div>
        </div>

        <!-- Foreground Dual Laptops in V-Angle displaying digital book content -->
        <div class="grand-laptops-v-stage">
            <!-- Left Laptop -->
            <div class="grand-lap lap-left">
                <div class="lap-bezel">
                    <div class="lap-screen">
                        <div class="lap-screen-title">SAUVER TON COUPLE</div>
                        <div class="lap-screen-sub">DORA ÉLYSIANE</div>
                        <img src="{book_img}" alt="Aperçu du livre" class="laptop-book-preview-img">
                        <div class="lap-screen-tag">GUIDE NUMÉRIQUE PDF</div>
                    </div>
                </div>
                <div class="lap-keyboard">
                    <div class="lap-notch"></div>
                </div>
            </div>

            <!-- Right Laptop -->
            <div class="grand-lap lap-right">
                <div class="lap-bezel">
                    <div class="lap-screen">
                        <div class="lap-screen-title">SAUVER TON COUPLE</div>
                        <div class="lap-screen-sub">PLAN D'ACTION 30 J</div>
                        <img src="{book_img}" alt="Aperçu du livre" class="laptop-book-preview-img">
                        <div class="lap-screen-tag">EXERCICES PRATIQUES</div>
                    </div>
                </div>
                <div class="lap-keyboard">
                    <div class="lap-notch"></div>
                </div>
            </div>
        </div>
    </div>
    '''

# Helper to build exact Éloquence 2.0 style 3-piece mockup for modules/bonuses with official book integration
def create_eloquence_style_mockup_html(module_num, title, subtitle, icon_class="fa-shield-heart", is_bonus=False, book_img=""):
    tag_label = f"BONUS #{module_num}" if is_bonus else f"Module {module_num}"
    box_header_sub = "GUIDE D'URGENCE" if is_bonus else "COMMENT PARLER À SA FEMME"
    
    return f'''
    <div class="eloquence-mockup-stage">
        <!-- Glowing Violet Circle Background -->
        <div class="eloquence-circle-bg"></div>

        <!-- Back Center Large 3D Box with Official Cover Artwork -->
        <div class="eloquence-box-back">
            <div class="box3d-top-lid"></div>
            <div class="box3d-spine-left"><span>SAUVER TON COUPLE — {tag_label}</span></div>
            <div class="box3d-front-panel official-cover-front">
                <img src="{book_img}" alt="Livre Officiel" class="box-official-cover-img">
            </div>
        </div>

        <!-- Front Right Medium 3D Box -->
        <div class="eloquence-box-front">
            <div class="box3d-top-lid"></div>
            <div class="box3d-spine-left"><span>SAUVER TON COUPLE — DORA ÉLYSIANE</span></div>
            <div class="box3d-front-panel">
                <div class="box-top-dark">
                    <h4>SAUVER TON COUPLE</h4>
                    <p>DORA ÉLYSIANE</p>
                </div>
                <div class="box-mid-light">
                    <div class="box-circle-emblem">
                        <i class="fa-solid {icon_class}"></i>
                    </div>
                </div>
                <div class="box-bottom-pill">
                    <span>{tag_label}</span>
                </div>
            </div>
        </div>

        <!-- Front Left Angled 3D Laptop -->
        <div class="eloquence-laptop-front">
            <div class="laptop-screen-bezel">
                <div class="laptop-display-content">
                    <div class="lap-title">SAUVER TON COUPLE</div>
                    <div class="lap-sub">Dora Élysiane</div>
                    <div class="lap-icon">
                        <i class="fa-solid {icon_class}"></i>
                    </div>
                    <div class="lap-module-tag">{tag_label}</div>
                    <div class="lap-detail">{subtitle}</div>
                </div>
            </div>
            <div class="laptop-keyboard-deck">
                <div class="laptop-notch"></div>
            </div>
        </div>
    </div>
    '''

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
            --purple-primary: #6b21a8;
            --purple-dark: #3b0764;
            --purple-light: #9333ea;
            --purple-deep: #1e0236;
            --purple-glow: #c084fc;
            --lavender-light: #f3e8ff;
            --pink-accent: #e879f9;
            --purple-gradient: linear-gradient(135deg, #9333ea 0%, #6b21a8 50%, #3b0764 100%);
            --purple-hover: linear-gradient(135deg, #581c87 0%, #2e1065 100%);
            --dark-bg: #0f0318;
            --dark-surface: #1a0528;
            --dark-card: #26083b;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --border-radius: 16px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --shadow-sm: 0 4px 6px -1px rgba(0,0,0,0.05);
            --shadow-md: 0 10px 30px -5px rgba(107, 33, 168, 0.25);
            --shadow-lg: 0 20px 40px -15px rgba(107, 33, 168, 0.45);
            --purple-shadow: 0 0 35px rgba(147, 51, 234, 0.4);
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
        .text-pink {{ color: var(--pink-accent); }}
        .text-purple {{ color: var(--purple-light); }}
        .text-lavender {{ color: var(--lavender-light); }}

        /* Top Bar Urgency (Pure Violet) */
        .announcement-bar {{
            background: var(--purple-gradient);
            border-bottom: 2px solid var(--purple-glow);
            color: #ffffff;
            text-align: center;
            padding: 12px 15px;
            font-size: 0.95rem;
            font-weight: 700;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 12px rgba(59, 7, 100, 0.5);
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
            border: 1px solid var(--purple-glow);
            font-family: monospace;
            font-size: 1.05rem;
            color: #ffffff;
            font-weight: 800;
        }}

        /* Buttons matching Luxury Violet */
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
            border: 2px solid var(--purple-glow);
            width: 100%;
            max-width: 680px;
            text-align: center;
            background: var(--purple-gradient);
            color: #ffffff;
            box-shadow: 0 15px 35px rgba(107, 33, 168, 0.55);
        }}

        .btn-eloquence:hover {{
            transform: translateY(-3px) scale(1.02);
            background: var(--purple-hover);
            box-shadow: 0 20px 45px rgba(232, 121, 249, 0.4);
        }}

        .btn-subtext {{
            font-size: 0.85rem;
            font-weight: 500;
            color: var(--lavender-light);
            margin-top: 4px;
        }}

        /* Hero Section */
        .hero {{
            padding: 70px 0 90px;
            background: linear-gradient(180deg, #1a0528 0%, #0a0112 100%);
            color: #ffffff;
            position: relative;
            overflow: hidden;
        }}

        .hero-badge {{
            display: inline-block;
            background: rgba(147, 51, 234, 0.2);
            border: 1px solid var(--purple-glow);
            color: var(--lavender-light);
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

        /* PIXEL-PERFECT GRAND ÉLOQUENCE 2.0 BUNDLE STAGE (7 BOXES + DUAL V-LAPTOPS WITH INTEGRATED OFFICIAL BOOK COVER) */
        .grand-bundle-stage {{
            position: relative;
            max-width: 1180px;
            margin: 40px auto 20px;
            padding: 60px 10px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            perspective: 1200px;
        }}

        .grand-halo-circle {{
            position: absolute;
            top: 35%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 520px;
            height: 380px;
            background: radial-gradient(ellipse at center, rgba(147, 51, 234, 0.8) 0%, rgba(107, 33, 168, 0.45) 60%, transparent 85%);
            border-radius: 50%;
            filter: blur(40px);
            z-index: 1;
        }}

        .grand-box-cascade {{
            position: relative;
            z-index: 2;
            width: 100%;
            height: 280px;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin-bottom: -110px;
        }}

        .elo-box {{
            position: absolute;
            bottom: 0;
            transform-style: preserve-3d;
            transition: var(--transition);
        }}

        .elo-box:hover {{
            transform: translateY(-8px) scale(1.03);
            z-index: 15 !important;
        }}

        .box-pos-1 {{ left: 2%; width: 125px; height: 170px; z-index: 6; transform: perspective(800px) rotateY(-18deg) rotateX(4deg); }}
        .box-pos-2 {{ left: 14%; width: 135px; height: 185px; z-index: 5; transform: perspective(800px) rotateY(-18deg) rotateX(4deg); }}
        .box-pos-3 {{ left: 26%; width: 145px; height: 200px; z-index: 4; transform: perspective(800px) rotateY(-18deg) rotateX(4deg); }}
        .box-pos-center {{ left: 50%; transform: translateX(-50%) perspective(800px) rotateY(0deg) rotateX(4deg); width: 170px; height: 235px; z-index: 3; }}
        .box-pos-5 {{ right: 26%; width: 145px; height: 200px; z-index: 4; transform: perspective(800px) rotateY(18deg) rotateX(4deg); }}
        .box-pos-6 {{ right: 14%; width: 135px; height: 185px; z-index: 5; transform: perspective(800px) rotateY(18deg) rotateX(4deg); }}
        .box-pos-7 {{ right: 2%; width: 125px; height: 170px; z-index: 6; transform: perspective(800px) rotateY(18deg) rotateX(4deg); }}

        .elo-box-top {{
            position: absolute;
            top: -20px;
            left: 0;
            width: 100%;
            height: 20px;
            background: #6b21a8;
            border: 1px solid var(--purple-glow);
            transform-origin: bottom center;
            transform: rotateX(90deg);
        }}

        .elo-box-spine {{
            position: absolute;
            top: 0;
            left: -20px;
            width: 20px;
            height: 100%;
            background: linear-gradient(180deg, #3b0764 0%, #1a032e 100%);
            border: 1px solid var(--purple-glow);
            border-right: none;
            transform-origin: right center;
            transform: rotateY(-90deg);
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .elo-box-spine span {{
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            color: var(--pink-accent);
            font-size: 0.6rem;
            font-weight: 800;
            letter-spacing: 1px;
            font-family: 'Outfit', sans-serif;
            white-space: nowrap;
        }}

        .elo-box-front {{
            width: 100%;
            height: 100%;
            border: 2px solid var(--purple-glow);
            border-radius: 4px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            background: #ffffff;
            box-shadow: 0 10px 25px rgba(0,0,0,0.85);
            position: relative;
        }}

        .official-cover-front {{
            background: #1a032e !important;
            padding: 0 !important;
        }}

        .box-official-cover-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .laptop-book-preview-img {{
            width: 65px;
            height: 85px;
            object-fit: cover;
            border-radius: 4px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.6);
            margin: 6px 0;
        }}

        .elo-top-dark {{
            background: linear-gradient(135deg, #3b0764 0%, #1a032e 100%);
            padding: 8px 4px;
            text-align: center;
            color: #ffffff;
            border-bottom: 2px solid var(--purple-glow);
        }}

        .elo-top-dark h4 {{
            font-size: 0.72rem;
            font-weight: 900;
            letter-spacing: 0.5px;
            line-height: 1.1;
            color: #ffffff;
        }}

        .elo-top-dark h3 {{
            font-size: 0.85rem;
            font-weight: 900;
            letter-spacing: 0.5px;
            line-height: 1.1;
            color: #ffffff;
        }}

        .elo-top-dark p {{
            font-size: 0.55rem;
            color: var(--pink-accent);
            font-weight: 700;
            margin-top: 2px;
            text-transform: uppercase;
        }}

        .elo-mid-light {{
            flex: 1;
            background: linear-gradient(180deg, #fcf9ff 0%, #f3e8ff 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8px;
            position: relative;
        }}

        .elo-circle-icon {{
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: #1a032e;
            border: 2px solid var(--purple-glow);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--pink-accent);
            font-size: 1.2rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }}

        .elo-circle-icon.large-icon {{
            width: 60px;
            height: 60px;
            font-size: 1.6rem;
        }}

        .elo-seal-badge {{
            position: absolute;
            top: 6px;
            right: 6px;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: var(--purple-gradient);
            border: 1px solid var(--purple-glow);
            color: #ffffff;
            font-size: 0.45rem;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 6px rgba(0,0,0,0.4);
        }}

        .elo-guarantee-round-seal {{
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: radial-gradient(circle, #e879f9 0%, #9333ea 60%, #3b0764 100%);
            border: 2px dashed #ffffff;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 0.5rem;
            line-height: 1;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        }}

        .elo-guarantee-round-seal strong {{
            font-size: 0.6rem;
            margin-top: 1px;
        }}

        .elo-pill-footer {{
            background: linear-gradient(135deg, #6b21a8 0%, #3b0764 100%);
            color: #ffffff;
            padding: 5px 6px;
            margin: 5px;
            border-radius: 20px;
            text-align: center;
            font-size: 0.6rem;
            font-weight: 800;
            font-family: 'Outfit', sans-serif;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            border: 1px solid var(--purple-glow);
        }}

        /* Dual Laptops in V-Angle Foreground Stage */
        .grand-laptops-v-stage {{
            position: relative;
            z-index: 10;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            width: 100%;
        }}

        .grand-lap {{
            position: relative;
            transform-style: preserve-3d;
            transition: var(--transition);
        }}

        .lap-left {{
            width: 480px;
            margin-right: -40px;
            transform: perspective(1000px) rotateY(32deg) rotateX(4deg);
            filter: drop-shadow(-15px 25px 35px rgba(0,0,0,0.95));
        }}

        .lap-left:hover {{
            transform: perspective(1000px) rotateY(18deg) scale(1.03);
            z-index: 20;
        }}

        .lap-right {{
            width: 480px;
            margin-left: -40px;
            transform: perspective(1000px) rotateY(-32deg) rotateX(4deg);
            filter: drop-shadow(15px 25px 35px rgba(0,0,0,0.95));
        }}

        .lap-right:hover {{
            transform: perspective(1000px) rotateY(-18deg) scale(1.03);
            z-index: 20;
        }}

        .lap-bezel {{
            background: #0f172a;
            border-radius: 12px 12px 0 0;
            padding: 10px;
            border: 3px solid #64748b;
            border-bottom: none;
        }}

        .lap-screen {{
            background: linear-gradient(180deg, #1a0528 0%, #0d0214 100%);
            border-radius: 6px;
            height: 250px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 15px;
            text-align: center;
            border: 2px solid var(--purple-primary);
            position: relative;
            overflow: hidden;
        }}

        .lap-screen-title {{
            font-size: 1.4rem;
            font-weight: 900;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            letter-spacing: 1px;
            margin-bottom: 2px;
        }}

        .lap-screen-sub {{
            font-size: 0.88rem;
            color: var(--pink-accent);
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 4px;
        }}

        .lap-screen-tag {{
            background: var(--purple-gradient);
            color: #ffffff;
            border: 1px solid var(--purple-glow);
            font-size: 0.8rem;
            font-weight: 800;
            padding: 4px 16px;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            margin-top: 4px;
        }}

        .lap-keyboard {{
            height: 16px;
            background: linear-gradient(180deg, #cbd5e1 0%, #64748b 100%);
            border-radius: 0 0 16px 16px;
            position: relative;
            box-shadow: 0 10px 20px rgba(0,0,0,0.8);
        }}

        .lap-notch {{
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 4px;
            background: #334155;
            border-radius: 0 0 4px 4px;
        }}

        /* EXACT ÉLOQUENCE 2.0 STYLE MOCKUP STAGE CSS COMPONENT FOR CHAPTERS/BONUSES */
        .eloquence-mockup-stage {{
            position: relative;
            width: 320px;
            height: 270px;
            margin: 0 auto;
            perspective: 1000px;
        }}

        .eloquence-circle-bg {{
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 230px;
            height: 230px;
            background: radial-gradient(circle, #9333ea 0%, #6b21a8 60%, transparent 100%);
            border-radius: 50%;
            filter: blur(8px);
            z-index: 1;
            opacity: 0.85;
        }}

        .eloquence-box-back {{
            position: absolute;
            top: 15px;
            right: 40px;
            width: 150px;
            height: 200px;
            z-index: 2;
            transform-style: preserve-3d;
            transform: rotateY(-18deg) rotateX(4deg);
            box-shadow: -12px 18px 30px rgba(0,0,0,0.8);
            transition: var(--transition);
        }}

        .eloquence-box-back:hover {{
            transform: rotateY(-10deg) translateY(-5px);
        }}

        .eloquence-box-front {{
            position: absolute;
            bottom: 20px;
            right: 15px;
            width: 135px;
            height: 175px;
            z-index: 4;
            transform-style: preserve-3d;
            transform: rotateY(-18deg) rotateX(4deg);
            box-shadow: -10px 15px 25px rgba(0,0,0,0.85);
            transition: var(--transition);
        }}

        .eloquence-box-front:hover {{
            transform: rotateY(-8deg) translateY(-6px);
        }}

        .box3d-top-lid {{
            position: absolute;
            top: -24px;
            left: 0;
            width: 100%;
            height: 24px;
            background: #6b21a8;
            border: 1px solid var(--purple-glow);
            transform-origin: bottom center;
            transform: rotateX(90deg);
        }}

        .box3d-spine-left {{
            position: absolute;
            top: 0;
            left: -24px;
            width: 24px;
            height: 100%;
            background: linear-gradient(180deg, #3b0764 0%, #1a032e 100%);
            border: 1px solid var(--purple-glow);
            border-right: none;
            transform-origin: right center;
            transform: rotateY(-90deg);
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .box3d-spine-left span {{
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            color: var(--pink-accent);
            font-size: 0.62rem;
            font-weight: 800;
            letter-spacing: 1px;
            font-family: 'Outfit', sans-serif;
            white-space: nowrap;
        }}

        .box3d-front-panel {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 2px solid var(--purple-glow);
            border-radius: 4px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            background: #ffffff;
        }}

        .box-top-dark {{
            background: linear-gradient(135deg, #3b0764 0%, #1a032e 100%);
            padding: 8px;
            text-align: center;
            color: #ffffff;
            border-bottom: 2px solid var(--purple-glow);
        }}

        .box-top-dark h4 {{
            font-size: 0.78rem;
            font-weight: 900;
            letter-spacing: 0.5px;
            line-height: 1.1;
            color: #ffffff;
        }}

        .box-top-dark p {{
            font-size: 0.6rem;
            color: var(--pink-accent);
            font-weight: 700;
            margin-top: 2px;
            text-transform: uppercase;
        }}

        .box-mid-light {{
            flex: 1;
            background: linear-gradient(180deg, #fcf9ff 0%, #f3e8ff 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
        }}

        .box-circle-emblem {{
            width: 55px;
            height: 55px;
            border-radius: 50%;
            background: #1a032e;
            border: 2px solid var(--purple-glow);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--pink-accent);
            font-size: 1.4rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }}

        .box-bottom-pill {{
            background: linear-gradient(135deg, #6b21a8 0%, #3b0764 100%);
            color: #ffffff;
            padding: 6px 8px;
            margin: 6px;
            border-radius: 20px;
            text-align: center;
            font-size: 0.65rem;
            font-weight: 800;
            font-family: 'Outfit', sans-serif;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            border: 1px solid var(--purple-glow);
        }}

        .eloquence-laptop-front {{
            position: absolute;
            bottom: 15px;
            left: 5px;
            width: 190px;
            z-index: 5;
            transform-style: preserve-3d;
            transform: rotateY(22deg) rotateX(4deg);
            filter: drop-shadow(-10px 12px 20px rgba(0,0,0,0.85));
            transition: var(--transition);
        }}

        .eloquence-laptop-front:hover {{
            transform: rotateY(12deg) translateY(-5px) scale(1.03);
        }}

        .laptop-screen-bezel {{
            background: #0f172a;
            border-radius: 8px 8px 0 0;
            padding: 6px;
            border: 2px solid #64748b;
            border-bottom: none;
        }}

        .laptop-display-content {{
            background: linear-gradient(180deg, #1a0528 0%, #0d0214 100%);
            border-radius: 4px;
            height: 110px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 8px;
            text-align: center;
            border: 1px solid var(--purple-primary);
        }}

        .lap-title {{
            font-size: 0.72rem;
            font-weight: 900;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            line-height: 1.1;
        }}

        .lap-sub {{
            font-size: 0.58rem;
            color: var(--pink-accent);
            font-weight: 700;
        }}

        .lap-icon {{
            font-size: 1.3rem;
            color: var(--purple-glow);
            margin: 4px 0;
        }}

        .lap-module-tag {{
            background: var(--purple-primary);
            color: #ffffff;
            font-size: 0.58rem;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 10px;
            margin-top: 2px;
        }}

        .lap-detail {{
            font-size: 0.55rem;
            color: #cbd5e1;
            margin-top: 2px;
        }}

        .laptop-keyboard-deck {{
            height: 10px;
            background: linear-gradient(180deg, #cbd5e1 0%, #94a3b8 100%);
            border-radius: 0 0 10px 10px;
            position: relative;
        }}

        .hero-target-box {{
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(192, 132, 252, 0.4);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 22px 30px;
            max-width: 880px;
            margin: 20px auto 40px;
            font-size: 1.05rem;
            color: #e2e8f0;
        }}

        /* Guarantee Badge 3D Violet */
        .guarantee-seal-3d {{
            width: 100px;
            height: 100px;
            background: radial-gradient(circle, #e879f9 0%, #9333ea 60%, #3b0764 100%);
            border-radius: 50%;
            border: 3px dashed #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.6), 0 0 25px rgba(147, 51, 234, 0.6);
            transform: rotate(-10deg);
        }}

        .guarantee-seal-3d span {{
            font-size: 0.65rem;
            line-height: 1.1;
            color: #ffffff;
        }}

        .guarantee-seal-3d strong {{
            font-size: 1.1rem;
            display: block;
            color: #ffffff;
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
            margin: 0 auto 55px;
        }}

        .section-tag {{
            color: var(--purple-primary);
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-size: 0.88rem;
            margin-bottom: 12px;
            display: block;
        }}

        .section-title {{
            font-size: 2.4rem;
            color: #0f172a;
            margin-bottom: 18px;
        }}

        .section-subtitle {{
            font-size: 1.1rem;
            color: var(--text-muted);
        }}

        .cards-grid-2 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 30px;
        }}

        .card-problem {{
            background: #faf5ff;
            border-top: 4px solid #c084fc;
            border-radius: var(--border-radius);
            padding: 35px;
            box-shadow: var(--shadow-md);
        }}

        .card-solution {{
            background: #f3e8ff;
            border-top: 4px solid var(--purple-primary);
            border-radius: var(--border-radius);
            padding: 35px;
            box-shadow: var(--shadow-md);
        }}

        .card-title {{
            font-size: 1.4rem;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .card-list {{
            list-style: none;
        }}

        .card-list li {{
            margin-bottom: 14px;
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 1rem;
            color: #334155;
        }}

        /* Chapters / Program Section */
        .program-section {{
            padding: 90px 0;
            background: #fcf9ff;
        }}

        .chapter-card {{
            background: #ffffff;
            border: 2px solid var(--purple-glow);
            border-radius: var(--border-radius);
            padding: 35px;
            margin-bottom: 40px;
            box-shadow: var(--shadow-md);
            display: grid;
            grid-template-columns: 340px 1fr;
            gap: 35px;
            align-items: center;
            transition: var(--transition);
        }}

        @media(max-width: 900px) {{
            .chapter-card {{
                grid-template-columns: 1fr;
                text-align: center;
            }}
        }}

        .chapter-card:hover {{
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
            border-color: var(--purple-primary);
        }}

        .chapter-mockup-wrapper {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #1a0528 0%, #0a0112 100%);
            padding: 20px 10px;
            border-radius: 16px;
            border: 1px solid var(--purple-glow);
            position: relative;
        }}

        .chapter-content h3 {{
            font-size: 1.5rem;
            color: var(--purple-primary);
            margin-bottom: 12px;
        }}

        .chapter-content p {{
            color: var(--text-muted);
            margin-bottom: 20px;
            font-size: 1.02rem;
        }}

        .bullet-list {{
            list-style: none;
        }}

        .bullet-list li {{
            margin-bottom: 10px;
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 0.98rem;
            color: #1e293b;
        }}

        .puce-arrow {{
            width: 24px;
            height: 24px;
            background: var(--purple-primary);
            color: #ffffff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: 900;
            flex-shrink: 0;
            margin-top: 2px;
            box-shadow: 0 2px 6px rgba(107, 33, 168, 0.4);
        }}

        /* Bonus Cards Section */
        .bonuses-section {{
            padding: 90px 0;
            background: #ffffff;
        }}

        .bonus-card {{
            background: #ffffff;
            border: 2px solid var(--purple-glow);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow-md);
            margin-bottom: 40px;
            transition: var(--transition);
        }}

        .bonus-card:hover {{
            transform: translateY(-5px);
            box-shadow: var(--shadow-lg);
        }}

        .bonus-header-banner {{
            background: var(--purple-gradient);
            border-bottom: 2px solid var(--purple-glow);
            color: #ffffff;
            padding: 16px 25px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .bonus-header-banner h4 {{
            font-size: 1.3rem;
            color: var(--lavender-light);
        }}

        .bonus-value-tag {{
            background: rgba(232, 121, 249, 0.2);
            border: 1px solid var(--purple-glow);
            color: var(--lavender-light);
            padding: 4px 14px;
            border-radius: 20px;
            font-weight: 800;
            font-size: 0.85rem;
        }}

        .bonus-body-grid {{
            padding: 35px;
            display: grid;
            grid-template-columns: 340px 1fr;
            gap: 35px;
            align-items: center;
        }}

        @media(max-width: 900px) {{
            .bonus-body-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        .bonus-mockup-display {{
            background: linear-gradient(180deg, #1a0528 0%, #0a0112 100%);
            border-radius: 16px;
            padding: 20px 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border: 1px solid var(--purple-glow);
        }}

        .bonus-title {{
            font-size: 1.5rem;
            color: var(--purple-primary);
            margin-bottom: 14px;
        }}

        /* Author Section */
        .author-section {{
            padding: 90px 0;
            background: linear-gradient(180deg, #1a0528 0%, #0a0112 100%);
            color: #ffffff;
        }}

        .author-grid {{
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 40px;
            align-items: center;
        }}

        @media(max-width: 768px) {{
            .author-grid {{
                grid-template-columns: 1fr;
                text-align: center;
            }}
        }}

        .author-emblem-container {{
            display: flex;
            justify-content: center;
        }}

        .author-monogram-circle {{
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: var(--purple-gradient);
            border: 4px solid var(--purple-glow);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: var(--purple-shadow);
        }}

        .author-monogram-circle h2 {{
            font-size: 4rem;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            letter-spacing: 2px;
            line-height: 1;
        }}

        .author-monogram-circle p {{
            font-size: 0.8rem;
            color: var(--pink-accent);
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-top: 6px;
        }}

        .author-bio h3 {{
            font-size: 2.2rem;
            color: #ffffff;
            margin-bottom: 8px;
        }}

        .author-bio .role-title {{
            color: var(--purple-glow);
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 20px;
        }}

        .author-bio p {{
            color: #cbd5e1;
            margin-bottom: 16px;
            font-size: 1.05rem;
            line-height: 1.7;
        }}

        /* Price Stack / Pricing Section */
        .pricing-section {{
            padding: 90px 0;
            background: #fcf9ff;
        }}

        .pricing-card {{
            background: #ffffff;
            border: 3px solid var(--purple-glow);
            border-radius: 20px;
            max-width: 780px;
            margin: 0 auto;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
        }}

        .pricing-header {{
            background: var(--purple-gradient);
            color: #ffffff;
            padding: 30px;
            text-align: center;
        }}

        .pricing-header h3 {{
            font-size: 2rem;
            color: #ffffff;
            margin-bottom: 8px;
        }}

        .pricing-body {{
            padding: 40px 30px;
        }}

        .price-display-box {{
            text-align: center;
            margin-bottom: 30px;
            background: #faf5ff;
            padding: 25px;
            border-radius: 12px;
            border: 1px dashed var(--purple-primary);
        }}

        .price-old {{
            font-size: 1.3rem;
            color: #94a3b8;
            text-decoration: line-through;
            margin-bottom: 6px;
        }}

        .price-current {{
            font-size: 3.2rem;
            color: var(--purple-primary);
            font-weight: 900;
            font-family: 'Outfit', sans-serif;
            line-height: 1;
        }}

        .price-badge {{
            display: inline-block;
            background: linear-gradient(135deg, #9333ea 0%, #6b21a8 100%);
            color: #ffffff;
            font-size: 0.85rem;
            font-weight: 800;
            padding: 4px 14px;
            border-radius: 20px;
            margin-top: 10px;
            text-transform: uppercase;
            border: 1px solid var(--purple-glow);
        }}

        /* Guarantee Section */
        .guarantee-section {{
            padding: 90px 0;
            background: linear-gradient(180deg, #1a0528 0%, #0a0112 100%);
            color: #ffffff;
            text-align: center;
        }}

        .guarantee-box {{
            max-width: 880px;
            margin: 0 auto;
            border: 2px solid var(--purple-glow);
            border-radius: var(--border-radius);
            padding: 50px 30px;
            background: rgba(255,255,255,0.02);
            backdrop-filter: blur(10px);
        }}

        .guarantee-box h3 {{
            font-size: 2.2rem;
            color: var(--lavender-light);
            margin-bottom: 16px;
        }}

        .guarantee-box p {{
            font-size: 1.08rem;
            color: #cbd5e1;
            line-height: 1.7;
            margin-bottom: 30px;
        }}

        /* FAQ Accordion */
        .faq-section {{
            padding: 90px 0;
            background: #ffffff;
        }}

        .faq-item {{
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            margin-bottom: 16px;
            overflow: hidden;
        }}

        .faq-question {{
            padding: 20px 25px;
            background: #fcf9ff;
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--purple-primary);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .faq-answer {{
            padding: 20px 25px;
            background: #ffffff;
            color: var(--text-muted);
            font-size: 1rem;
            line-height: 1.6;
            border-top: 1px solid #e2e8f0;
        }}

        /* Footer */
        footer {{
            background: #0a0112;
            color: #94a3b8;
            padding: 40px 0;
            text-align: center;
            font-size: 0.9rem;
            border-top: 1px solid rgba(192, 132, 252, 0.2);
        }}
    </style>
</head>
<body>

    <!-- Urgency Top Bar -->
    <div class="announcement-bar">
        <span>⚡ OFFRE SPÉCIALE D'ACCÈS IMMÉDIAT — EXPIRATION DE LA RÉDUCTION :</span>
        <div class="timer-badge" id="countdown">00:14:59</div>
    </div>

    <!-- HERO SECTION -->
    <section class="hero text-center">
        <div class="container">
            <span class="hero-badge"> GUIDE EXCLUSIF POUR L'HOMME MODERNE</span>
            <h1 class="hero-title">
                Comment Résoudre les Crises de Ton Couple <br>
                <span>Sans Perdre Ta Dignité ni Ton Respect</span>
            </h1>
            <p class="hero-subtitle">
                Le guide honnête, direct et sans filtre que tu aurais voulu avoir avant la première dispute.
                Une approche étape par étape créée pour l'homme qui veut restaurer la paix et l'attraction.
            </p>

            <!-- PIXEL-PERFECT GRAND ÉLOQUENCE BUNDLE SHOWCASE WITH OFFICIAL BOOK ARTWORK -->
            {create_grand_eloquence_bundle_html(b64_book)}

            <div class="hero-target-box">
                <i class="fa-solid fa-circle-check text-pink" style="margin-right:8px;"></i>
                <strong>Inclus dans le pack :</strong> Le Livre Principal (15 Chapitres, 50 Pages) + Les Exercices Pratiques + Le Plan 30 Jours + Les Bonus Exclusifs.
            </div>

            <a href="#commander" class="btn-eloquence">
                <span>OBTENIR LE GUIDE MAINTENANT (9 900 FCFA)</span>
                <span class="btn-subtext">🔒 Accès instantané en téléchargement sécurisé après paiement</span>
            </a>
        </div>
    </section>

    <!-- PROOF BAR -->
    <section class="proof-bar">
        <div class="container">
            <div class="proof-grid">
                <div class="proof-item">
                    <h3>15</h3>
                    <p>Chapitres Stratégiques</p>
                </div>
                <div class="proof-item">
                    <h3>50</h3>
                    <p>Pages d'Action Pure</p>
                </div>
                <div class="proof-item">
                    <h3>30 Jours</h3>
                    <p>Plan de Redressement</p>
                </div>
                <div class="proof-item">
                    <h3>100%</h3>
                    <p>Discrétion & Accès Immédiat</p>
                </div>
            </div>
        </div>
    </section>

    <!-- PROBLEM VS SOLUTION SECTION -->
    <section class="transformation-section">
        <div class="container">
            <div class="section-header">
                <span class="section-tag">COMPRENDRE LA SITUATION</span>
                <h2 class="section-title">Pourquoi Tes Méthodes Actuelles Ne Marchent Pas</h2>
                <p class="section-subtitle">
                    Quand les disputes s'accumulent, la plupart des hommes commettent deux erreurs fatalement opposées : soit ils s'écrasent pour éviter le conflit, soit ils s'énervent et détruisent le respect.
                </p>
            </div>

            <div class="cards-grid-2">
                <!-- Bad Approach -->
                <div class="card-problem">
                    <h3 class="card-title text-pink">
                        <i class="fa-solid fa-circle-xmark" style="color:var(--purple-glow);"></i>
                        Ce qui détruit ton couple
                    </h3>
                    <ul class="card-list">
                        <li>
                            <i class="fa-solid fa-xmark" style="color:var(--purple-glow); margin-top:4px;"></i>
                            <span>Supporter le silence et la froideur sans savoir comment réagir dignement.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark" style="color:var(--purple-glow); margin-top:4px;"></i>
                            <span>S'excuser excessivement pour des choses dont tu n'es pas responsable.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark" style="color:var(--purple-glow); margin-top:4px;"></i>
                            <span>Tenter d'argumenter pendant des heures avec une logique froide quand l'émotion explose.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-xmark" style="color:var(--purple-glow); margin-top:4px;"></i>
                            <span>Laisser la rancœur et l'éloignement s'installer jour après jour.</span>
                        </li>
                    </ul>
                </div>

                <!-- Good Approach -->
                <div class="card-solution">
                    <h3 class="card-title" style="color:var(--purple-primary);">
                        <i class="fa-solid fa-circle-check" style="color:var(--purple-primary);"></i>
                        La Méthode Dora Élysiane
                    </h3>
                    <ul class="card-list">
                        <li>
                            <i class="fa-solid fa-check" style="color:var(--purple-primary); margin-top:4px;"></i>
                            <span>Comprendre ce qu'elle ressent réellement derrière ses reproches ou son silence.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check" style="color:var(--purple-primary); margin-top:4px;"></i>
                            <span>Poser des limites claires avec un calme absolu et une fermeté respectueuse.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check" style="color:var(--purple-primary); margin-top:4px;"></i>
                            <span>Désamorcer les tensions instantanément sans donner l'impression de céder.</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-check" style="color:var(--purple-primary); margin-top:4px;"></i>
                            <span>Créer un climat de confiance où la passion et l'attraction naturelle reviennent.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- CHAPTERS & PROGRAMME -->
    <section class="program-section">
        <div class="container">
            <div class="section-header">
                <span class="section-tag">LE PROGRAMME DÉTAILLÉ</span>
                <h2 class="section-title">Ce Que Tu Vas Découvrir Dans Le Guide</h2>
                <p class="section-subtitle">Chaque chapitre apporte une solution concrète et immédiatement applicable à tes échanges quotidiens.</p>
            </div>

            <!-- Chapter 1 Card -->
            <div class="chapter-card">
                <div class="chapter-mockup-wrapper">
                    {create_eloquence_style_mockup_html(1, "Les Causes des Tensions", "Psychologie Féminine", icon_class="fa-heart-crack", is_bonus=False, book_img=b64_book)}
                </div>
                <div class="chapter-content">
                    <h3>Chapitre 1 : Les Vraies Causes du Désamour & des Tensions</h3>
                    <p>Pourquoi la plupart des disputes ne concernent jamais le sujet dont vous discutez en surface.</p>
                    <ul class="bullet-list">
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Comment décoder le langage émotionnel féminin et déceler les besoins non exprimés.</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Les 3 pièges inconscients dans lesquels tombent 90% des hommes en période de crise.</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Comment stopper net l'accumulation de ressentiment avant qu'il ne soit trop tard.</span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Chapter 2 Card -->
            <div class="chapter-card">
                <div class="chapter-mockup-wrapper">
                    {create_eloquence_style_mockup_html(2, "Communication Saine", "Maîtrise & Dialogue", icon_class="fa-comments", is_bonus=False, book_img=b64_book)}
                </div>
                <div class="chapter-content">
                    <h3>Chapitre 2 : Communiquer Sans Crier ni T'écraser</h3>
                    <p>La formule exacte pour faire entendre ton point de vue tout en restant un roc de sérénité.</p>
                    <ul class="bullet-list">
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>La technique de désamorçage verbal lors d'un conflit explosif.</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Comment maintenir le respect mutuel même dans les moments d'extrême tension.</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Les mots exacts à utiliser quand elle se ferme complètement au dialogue.</span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Chapter 3 Card -->
            <div class="chapter-card">
                <div class="chapter-mockup-wrapper">
                    {create_eloquence_style_mockup_html(3, "Dignité & Respect", "Posture du Leader", icon_class="fa-user-tie", is_bonus=False, book_img=b64_book)}
                </div>
                <div class="chapter-content">
                    <h3>Chapitre 3 : Préserver ta Dignité & Ton Rôle de Leader</h3>
                    <p>Restaurer ton autorité naturelle et ton charisme sans agressivité ni domination toxique.</p>
                    <ul class="bullet-list">
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Comment définir tes limites personnelles de manière claire, calme et inébranlable.</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Pourquoi le respect est la condition sine qua non de la passion et de l'amour durable.</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span>Le plan de 30 jours pour transformer le climat de ton foyer.</span>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="text-center" style="margin-top: 40px;">
                <a href="#commander" class="btn-eloquence">
                    <span>C'EST EXACTEMENT CE DONT J'AI BESOIN</span>
                    <span class="btn-subtext">Obtiens l'accès complet pour 9 900 FCFA</span>
                </a>
            </div>
        </div>
    </section>

    <!-- BONUSES SECTION -->
    <section class="bonuses-section">
        <div class="container">
            <div class="section-header">
                <span class="section-tag">CADEAUX EXCLUSIFS</span>
                <h2 class="section-title">Tes 2 Bonus Inclus Gratuitement</h2>
                <p class="section-subtitle">Offerts uniquement si tu commandes durant cette session d'accès promotionnel.</p>
            </div>

            <!-- Bonus 1 -->
            <div class="bonus-card">
                <div class="bonus-header-banner">
                    <h4>BONUS #1 : Le Guide Anti-Dispute d'Urgence</h4>
                    <span class="bonus-value-tag">VALEUR : 15 000 FCFA (OFFERT)</span>
                </div>
                <div class="bonus-body-grid">
                    <div class="bonus-mockup-display">
                        {create_eloquence_style_mockup_html(1, "Guide Anti-Dispute", "Intervention Rapide", icon_class="fa-shield-halved", is_bonus=True, book_img=b64_book)}
                    </div>
                    <div>
                        <h3 class="bonus-title">Le Protocole d'Urgence en 5 Étapes Quand une Dispute Éclate</h3>
                        <p style="color:var(--text-muted); margin-bottom:16px;">
                            Un mini-guide pratique à garder sur ton téléphone pour savoir exactement quoi dire et quoi faire dans la minute où la tension monte.
                        </p>
                        <ul class="bullet-list">
                            <li>
                                <div class="puce-arrow">➔</div>
                                <span>Les 3 phrases magiques pour désamorcer la colère instantanément.</span>
                            </li>
                            <li>
                                <div class="puce-arrow">➔</div>
                                <span>Comment garder ton sang-froid absolu quelle que soit la provocation.</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Bonus 2 -->
            <div class="bonus-card">
                <div class="bonus-header-banner">
                    <h4>BONUS #2 : Le Plan d'Action 30 Jours</h4>
                    <span class="bonus-value-tag">VALEUR : 20 000 FCFA (OFFERT)</span>
                </div>
                <div class="bonus-body-grid">
                    <div class="bonus-mockup-display">
                        {create_eloquence_style_mockup_html(2, "Plan 30 Jours", "Feuille de Route", icon_class="fa-calendar-check", is_bonus=True, book_img=b64_book)}
                    </div>
                    <div>
                        <h3 class="bonus-title">La Feuille de Route Quotidienne Pour Transformer Ton Foyer</h3>
                        <p style="color:var(--text-muted); margin-bottom:16px;">
                            Une checklist étape par étape jour par jour pour appliquer la méthode sans te poser de questions et observer des résultats dès la première semaine.
                        </p>
                        <ul class="bullet-list">
                            <li>
                                <div class="puce-arrow">➔</div>
                                <span>Des exercices simples de 5 minutes par jour pour reprogrammer tes réactions.</span>
                            </li>
                            <li>
                                <div class="puce-arrow">➔</div>
                                <span>Un suivi clair pour mesurer la réconciliation au quotidien.</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- AUTHOR SECTION -->
    <section class="author-section">
        <div class="container">
            <div class="author-grid">
                <div class="author-emblem-container">
                    <div class="author-monogram-circle">
                        <h2>DÉ</h2>
                        <p>Dora Élysiane</p>
                    </div>
                </div>
                <div class="author-bio">
                    <h3>Une voix de femme, pour l'homme qui lutte</h3>
                    <p class="role-title">Auteure & Coach en Relations de Couple</p>
                    <p>
                        "De la souffrance silencieuse à un foyer apaisé. J'ai écrit ce guide parce que je vois trop d'hommes de valeur souffrir en silence, perdre leur dignité ou abandonner leur foyer faute d'avoir les bonnes clés de compréhension."
                    </p>
                    <p>
                        Mon objectif à travers <strong>Sauver Ton Couple</strong> est de te donner le regard féminin authentique et les outils pratiques pour restaurer l'harmonie, l'attraction et le respect mutuel dans ton couple, sans jamais te renier.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- PRICING SECTION -->
    <section class="pricing-section" id="commander">
        <div class="container">
            <div class="pricing-card">
                <div class="pricing-header">
                    <h3>ACCÈS IMMÉDIAT AU PACK COMPLET</h3>
                    <p style="color:var(--lavender-light);">Téléchargement Numérique Instantané & Confidentiel</p>
                </div>
                <div class="pricing-body">
                    <div class="price-display-box">
                        <div class="price-old">Valeur Totale : 45 000 FCFA</div>
                        <div class="price-current">9 900 FCFA</div>
                        <span class="price-badge">RÉDUCTION SPÉCIALE -78%</span>
                    </div>

                    <ul class="bullet-list" style="margin-bottom: 30px;">
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span><strong>Le Guide Officiel Sauver Ton Couple</strong> (15 Chapitres, 50 Pages PDF)</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span><strong>Bonus #1 :</strong> Le Guide Anti-Dispute d'Urgence (Valeur 15 000 FCFA)</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span><strong>Bonus #2 :</strong> Le Plan d'Action 30 Jours (Valeur 20 000 FCFA)</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span><strong>Accès Immédiat 24h/7j</strong> sur Smartphone, Tablette & Ordinateur</span>
                        </li>
                        <li>
                            <div class="puce-arrow">➔</div>
                            <span><strong>Garantie Satisfait ou Remboursé 30 Jours</strong></span>
                        </li>
                    </ul>

                    <div class="text-center">
                        <a href="https://elysianedora.systeme.io/hommemoderne-cd57f727" class="btn-eloquence">
                            <span>VALIDER MA COMMANDE POUR 9 900 FCFA</span>
                            <span class="btn-subtext">Paiement 100% Sécurisé (Mobile Money, Carte Bancaire)</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- GUARANTEE SECTION -->
    <section class="guarantee-section">
        <div class="container">
            <div class="guarantee-box">
                <div style="display:flex; justify-content:center; margin-bottom:20px;">
                    <div class="guarantee-seal-3d">
                        <span>GARANTIE</span>
                        <strong>100%</strong>
                        <span>30 JOURS</span>
                    </div>
                </div>
                <h3>Garantie Satisfait ou Remboursé de 30 Jours</h3>
                <p>
                    Teste le guide et applique les conseils pendant 30 jours complets. Si tu ne constates pas un changement significatif dans tes échanges et une diminution nette des tensions dans ton couple, envoie simplement un email et tu seras remboursé intégralement, sans poser de questions.
                </p>
                <a href="#commander" class="btn-eloquence">
                    <span>JE PRENDS MON ACCÈS SANS RISQUE</span>
                    <span class="btn-subtext">Seulement 9 900 FCFA — Garantie Intégrale 30 Jours</span>
                </a>
            </div>
        </div>
    </section>

    <!-- FAQ SECTION -->
    <section class="faq-section">
        <div class="container">
            <div class="section-header">
                <span class="section-tag">FOIRE AUX QUESTIONS</span>
                <h2 class="section-title">Questions Fréquentes</h2>
            </div>

            <div style="max-width:850px; margin:0 auto;">
                <div class="faq-item">
                    <div class="faq-question">
                        <span>Comment vais-je recevoir le guide après avoir payé ?</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </div>
                    <div class="faq-answer">
                        Dès la confirmation de ton paiement de 9 900 FCFA, tu recevras immédiatement un lien direct pour télécharger le guide et tes bonus au format PDF. Tu pourras les lire sur ton téléphone, ta tablette ou ton ordinateur.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>Ma compagne saura-t-elle que j'ai acheté ce guide ?</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </div>
                    <div class="faq-answer">
                        Non, l'achat est 100% discret. L'intitulé de transaction est neutre et tu télécharges le fichier directement sur ton appareil personnel.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question">
                        <span>Est-ce utile si nous sommes déjà au bord de la rupture ?</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </div>
                    <div class="faq-answer">
                        Oui, absolument. Le guide contient justamente une partie dédiée à la gestion des crises aiguës et aux réactions d'urgence pour arrêter l'hémorragie et restaurer le respect.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <p style="margin-bottom:10px;">&copy; 2026 Dora Élysiane - Sauver Ton Couple. Tous droits réservés.</p>
            <p style="font-size:0.8rem; color:#64748b;">Ce site ne fait pas partie du site web Facebook ou de Facebook Inc. De plus, ce site n'est PAS approuvé par Facebook de quelque manière que ce soit.</p>
        </div>
    </footer>

    <!-- Countdown Timer Script -->
    <script>
        function startTimer(duration, display) {{
            let timer = duration, minutes, seconds;
            setInterval(function () {{
                minutes = parseInt(timer / 60, 10);
                seconds = parseInt(timer % 60, 10);

                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                display.textContent = minutes + ":" + seconds;

                if (--timer < 0) {{
                    timer = duration;
                }}
            }}, 1000);
        }}

        window.onload = function () {{
            const fifteenMinutes = 60 * 15;
            const display = document.querySelector('#countdown');
            if (display) {{
                startTimer(fifteenMinutes, display);
            }}
        }};
    </script>
</body>
</html>
'''

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully integrated official book cover artwork into 3D boxes at {html_file}")
