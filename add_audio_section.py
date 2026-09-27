import re

script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for Audio Section
audio_css = """
        /* Audio Section & Player Widget Styling */
        .audio-grid {{
            display: grid;
            grid-template-columns: 1fr 440px;
            gap: 50px;
            align-items: center;
        }}

        .audio-features-list {{
            display: flex;
            flex-direction: column;
            gap: 18px;
        }}

        .audio-feature-item {{
            display: flex;
            align-items: flex-start;
            gap: 16px;
            background: rgba(37, 9, 56, 0.4);
            border: 1px solid rgba(192, 132, 252, 0.2);
            padding: 18px 20px;
            border-radius: 14px;
        }}

        .audio-feature-icon {{
            width: 44px;
            height: 44px;
            border-radius: 12px;
            background: linear-gradient(135deg, var(--purple-glow), var(--pink-accent));
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            flex-shrink: 0;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
        }}

        .audio-feature-item h4 {{
            color: #ffffff;
            font-size: 1.1rem;
            margin-bottom: 4px;
        }}

        .audio-feature-item p {{
            color: #cbd5e1;
            font-size: 0.95rem;
            margin: 0;
            line-height: 1.5;
        }}

        .audio-player-card {{
            background: linear-gradient(145deg, rgba(37, 9, 56, 0.95), rgba(13, 2, 20, 0.98));
            border: 2px solid rgba(192, 132, 252, 0.35);
            border-radius: 24px;
            padding: 30px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 35px rgba(124, 58, 237, 0.25);
            position: relative;
            text-align: center;
        }}

        .player-badge-top {{
            display: inline-block;
            background: rgba(236, 72, 153, 0.2);
            color: var(--pink-accent);
            border: 1px solid rgba(236, 72, 153, 0.4);
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 800;
            margin-bottom: 20px;
        }}

        .player-cover {{
            background: rgba(124, 58, 237, 0.15);
            border-radius: 16px;
            padding: 25px 20px;
            border: 1px solid rgba(192, 132, 252, 0.2);
            margin-bottom: 20px;
        }}

        .player-icon-glow {{
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7c3aed, #c084fc);
            color: #ffffff;
            font-size: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 15px;
            box-shadow: 0 0 25px rgba(192, 132, 252, 0.6);
        }}

        .player-cover h3 {{
            color: #ffffff;
            font-size: 1.4rem;
            margin-bottom: 4px;
        }}

        .player-cover p {{
            color: var(--pink-accent);
            font-size: 0.9rem;
            font-weight: 600;
            margin: 0;
        }}

        .audio-waveform {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            height: 35px;
            margin: 20px 0;
        }}

        .audio-waveform span {{
            width: 4px;
            background: linear-gradient(180deg, var(--pink-accent), var(--purple-glow));
            border-radius: 4px;
            animation: wavePulse 1.4s ease-in-out infinite alternate;
        }}

        .audio-waveform span:nth-child(2n) {{ animation-delay: 0.2s; }}
        .audio-waveform span:nth-child(3n) {{ animation-delay: 0.4s; }}
        .audio-waveform span:nth-child(4n) {{ animation-delay: 0.1s; }}

        @keyframes wavePulse {{
            0% {{ transform: scaleY(0.3); opacity: 0.4; }}
            100% {{ transform: scaleY(1); opacity: 1; }}
        }}

        .player-time {{
            display: flex;
            justify-content: space-between;
            color: #cbd5e1;
            font-size: 0.82rem;
            font-weight: 600;
            margin-bottom: 6px;
        }}

        .player-progress-bar {{
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
        }}

        .player-progress-fill {{
            width: 42%;
            height: 100%;
            background: linear-gradient(90deg, var(--purple-glow), var(--pink-accent));
            border-radius: 10px;
        }}

        .player-buttons {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }}

        .p-btn {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #ffffff;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s;
        }}

        .p-btn.play-main {{
            width: 55px;
            height: 55px;
            background: linear-gradient(135deg, var(--purple-glow), var(--pink-accent));
            font-size: 1.3rem;
            box-shadow: 0 0 20px rgba(124, 58, 237, 0.5);
        }}

        .player-footer-tag {{
            font-size: 0.85rem;
            color: #ffffff;
            font-weight: 700;
            background: rgba(124, 58, 237, 0.2);
            padding: 8px 12px;
            border-radius: 10px;
            border: 1px dashed rgba(192, 132, 252, 0.4);
        }}

        @media (max-width: 900px) {{
            .audio-grid {{
                grid-template-columns: 1fr;
                gap: 35px;
            }}
            .audio-player-card {{
                max-width: 450px;
                margin: 0 auto;
            }}
        }}
"""

if '/* Audio Section & Player Widget Styling */' not in content:
    content = content.replace('/* Author Section */', audio_css + '\n        /* Author Section */')

# 2. Add Audio Section HTML Block
audio_html_block = """
    <!-- NOUVELLE SECTION DÉDIÉE : L'AUDIO COMPLET DU GUIDE -->
    <section class="audio-section" style="background: linear-gradient(180deg, #13031f 0%, #1a0528 50%, #0d0214 100%); padding: 80px 0; border-top: 1px solid rgba(192, 132, 252, 0.2); border-bottom: 1px solid rgba(192, 132, 252, 0.2);">
        <div class="container">
            <div class="audio-grid">
                <!-- Texte & Avantages -->
                <div class="audio-text-content">
                    <span class="section-tag" style="background: rgba(124, 58, 237, 0.25); color: var(--pink-accent); border: 1px solid var(--purple-glow);">
                        <i class="fa-solid fa-headphones"></i> INCLUS DANS VOTRE ACCÈS
                    </span>
                    <h2 class="section-title" style="text-align: left; margin: 15px 0 20px;">
                        EN PLUS DU GUIDE ÉCRIT : L'AUDIO COMPLET DU PROGRAMME
                    </h2>
                    <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.7; margin-bottom: 25px;">
                        Vous n'avez pas toujours le temps de vous asseoir pour lire ? Écoutez l'intégralité du guide où que vous soyez. Transformez vos trajets en voiture, vos séances de sport ou vos moments de calme en opportunités de métamorphose pour votre couple.
                    </p>

                    <div class="audio-features-list">
                        <div class="audio-feature-item">
                            <div class="audio-feature-icon"><i class="fa-solid fa-car"></i></div>
                            <div>
                                <h4>Écoute en déplacement</h4>
                                <p>Dans la voiture, les transports, au sport ou en marchant – intégrez les clés du programme sans bloquer de temps de lecture.</p>
                            </div>
                        </div>
                        <div class="audio-feature-item">
                            <div class="audio-feature-icon"><i class="fa-solid fa-circle-play"></i></div>
                            <div>
                                <h4>Format MP3 HD Téléchargeable</h4>
                                <p>Écoutable immédiatement sur votre smartphone, iPhone, Android, tablette ou ordinateur, même sans connexion internet.</p>
                            </div>
                        </div>
                        <div class="audio-feature-item">
                            <div class="audio-feature-icon"><i class="fa-solid fa-bolt"></i></div>
                            <div>
                                <h4>Intégration émotionnelle rapide</h4>
                                <p>Une voix claire, posée et captivante pour imprégner votre esprit des bonnes attitudes et des phrases clés de désamorçage.</p>
                            </div>
                        </div>
                    </div>

                    <div style="margin-top: 30px;">
                        <a href="https://syalpfmx.mychariow.shop/prd_9n9ofrxp/checkout" class="btn-eloquence">
                            <span>JE VEUX LE GUIDE ÉCRIT + LA VERSION AUDIO <span class="btn-price-tag">—&nbsp;9&nbsp;900&nbsp;FCFA</span></span>
                        </a>
                    </div>
                </div>

                <!-- Widget Lecteur Audio 3D/Glassmorphism -->
                <div class="audio-player-card">
                    <div class="player-badge-top"><i class="fa-solid fa-compact-disc fa-spin"></i> VERSION AUDIO MP3 HD</div>
                    <div class="player-cover">
                        <div class="player-icon-glow"><i class="fa-solid fa-headphones"></i></div>
                        <h3>SAUVER TON COUPLE</h3>
                        <p>L'Audiobook Complet (Intégralité du Guide)</p>
                    </div>

                    <div class="audio-waveform">
                        <span style="height: 45%;"></span>
                        <span style="height: 75%;"></span>
                        <span style="height: 100%;"></span>
                        <span style="height: 60%;"></span>
                        <span style="height: 35%;"></span>
                        <span style="height: 85%;"></span>
                        <span style="height: 95%;"></span>
                        <span style="height: 50%;"></span>
                        <span style="height: 70%;"></span>
                        <span style="height: 100%;"></span>
                        <span style="height: 80%;"></span>
                        <span style="height: 40%;"></span>
                        <span style="height: 65%;"></span>
                    </div>

                    <div class="player-controls">
                        <div class="player-time"><span>04:12</span> <span>3h 45min</span></div>
                        <div class="player-progress-bar">
                            <div class="player-progress-fill"></div>
                        </div>
                        <div class="player-buttons">
                            <button class="p-btn"><i class="fa-solid fa-backward-step"></i></button>
                            <button class="p-btn play-main"><i class="fa-solid fa-play"></i></button>
                            <button class="p-btn"><i class="fa-solid fa-forward-step"></i></button>
                        </div>
                    </div>
                    <div class="player-footer-tag">
                        <i class="fa-solid fa-circle-check text-pink"></i> INCLUS GRATUITEMENT DANS VOTRE COMMANDE
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

if '<!-- NOUVELLE SECTION DÉDIÉE : L\'AUDIO COMPLET DU GUIDE -->' not in content:
    content = content.replace('<!-- SECTION 4 :', audio_html_block + '\n    <!-- SECTION 4 :')

# 3. Add Audio translation keys to i18nMap
i18n_audio_keys = """            "INCLUS DANS VOTRE ACCÈS": "INCLUDED IN YOUR ACCESS",
            "EN PLUS DU GUIDE ÉCRIT : L'AUDIO COMPLET DU PROGRAMME": "IN ADDITION TO THE WRITTEN GUIDE: THE COMPLETE AUDIO PROGRAM",
            "Vous n'avez pas toujours le temps de vous asseoir pour lire ? Écoutez l'intégralité du guide où que vous soyez. Transformez vos trajets en voiture, vos séances de sport ou vos moments de calme en opportunités de métamorphose pour votre couple.": "Don't always have time to sit down and read? Listen to the entire guide wherever you are. Turn your car rides, workouts, or quiet moments into transformational opportunities for your relationship.",
            "Écoute en déplacement": "Listen on the Go",
            "Dans la voiture, les transports, au sport ou en marchant – intégrez les clés du programme sans bloquer de temps de lecture.": "In the car, on public transit, at the gym, or walking – absorb the program's keys without blocking out reading time.",
            "Format MP3 HD Téléchargeable": "Downloadable HD MP3 Format",
            "Écoutable immédiatement sur votre smartphone, iPhone, Android, tablette ou ordinateur, même sans connexion internet.": "Listen immediately on your smartphone, iPhone, Android, tablet, or computer, even offline.",
            "Intégration émotionnelle rapide": "Fast Emotional Absorption",
            "Une voix claire, posée et captivante pour imprégner votre esprit des bonnes attitudes et des phrases clés de désamorçage.": "A clear, calm, and engaging voice to naturally condition your mind with key defusing phrases and right attitudes.",
            "VERSION AUDIO MP3 HD": "HD MP3 AUDIO VERSION",
            "L'Audiobook Complet (Intégralité du Guide)": "The Complete Audiobook (Full Guide)",
            "INCLUS GRATUITEMENT DANS VOTRE COMMANDE": "INCLUDED FREE WITH YOUR ORDER",
            "JE VEUX LE GUIDE ÉCRIT + LA VERSION AUDIO": "I WANT THE WRITTEN GUIDE + THE AUDIO VERSION","""

if '"INCLUS DANS VOTRE ACCÈS"' not in content:
    content = content.replace('"OFFRE SPÉCIALE D\'ACCÈS IMMÉDIAT', i18n_audio_keys + '\n            "OFFRE SPÉCIALE D\'ACCÈS IMMÉDIAT')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Audio Section successfully added to build script!")
