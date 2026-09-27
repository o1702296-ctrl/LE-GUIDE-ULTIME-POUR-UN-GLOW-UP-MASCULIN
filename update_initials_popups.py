import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Toast Avatar CSS to match the purple initial circle from user screenshot
new_toast_css = '''
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
    </style>
'''

content = re.sub(r'/\* LIVE SOCIAL PROOF NOTIFICATION TOAST \*/.*?</style>', new_toast_css, content, flags=re.DOTALL)

# 2. Update Toast HTML element with initial text container
new_toast_html = '''
    <!-- LIVE SOCIAL PROOF SALES NOTIFICATION TOAST -->
    <div id="social-proof-toast" class="social-proof-toast">
        <div class="toast-content">
            <button class="toast-close" onclick="closeSocialProofToast()">&times;</button>
            <div class="toast-avatar" id="toast-initials">
                LU
            </div>
            <div class="toast-text">
                <p class="toast-buyer"><strong id="toast-name">Lucas</strong> <span id="toast-location" class="toast-loc">Lyon, France 🇫🇷</span></p>
                <p class="toast-product">vient de rejoindre LE GUIDE ULTIME</p>
                <span class="toast-time" id="toast-time">Il y a 2 min • Achat vérifié 🟢</span>
            </div>
        </div>
    </div>
'''

content = re.sub(r'<!-- LIVE SOCIAL PROOF SALES NOTIFICATION TOAST -->\s*<div id="social-proof-toast".*?</div>\s*</div>', new_toast_html, content, flags=re.DOTALL)

# 3. Update JavaScript array with 25 diverse international buyer profiles and fast country rotation
new_js_array = '''
        // Live International Social Proof Sales Notifications Engine (25+ Countries across Europe, Africa, America, Asia)
        const salesNotifications = [
            // EUROPE
            { initials: "LU", name: "Lucas", location: "Lyon, France 🇫🇷", time: "Il y a 2 minutes" },
            { initials: "MA", name: "Maxime", location: "Paris, France 🇫🇷", time: "Il y a 4 minutes" },
            { initials: "RA", name: "Rayan", location: "Bruxelles, Belgique 🇧🇪", time: "Il y a 1 minute" },
            { initials: "JU", name: "Julien", location: "Genève, Suisse 🇨🇭", time: "Il y a 3 minutes" },
            { initials: "LI", name: "Liam", location: "Londres, Royaume-Uni 🇬🇧", time: "Il y a 5 minutes" },

            // AFRIQUE
            { initials: "TH", name: "Théo", location: "Abidjan, Côte d'Ivoire 🇨🇮", time: "Il y a 1 minute" },
            { initials: "AL", name: "Alexandre", location: "Dakar, Sénégal 🇸🇳", time: "Il y a 3 minutes" },
            { initials: "DY", name: "Dylan", location: "Douala, Cameroun 🇨🇲", time: "Il y a 2 minutes" },
            { initials: "MO", name: "Mohamed", location: "Casablanca, Maroc 🇲🇦", time: "Il y a 6 minutes" },
            { initials: "AN", name: "Antoine", location: "Lomé, Togo 🇹🇬", time: "Il y a 4 minutes" },
            { initials: "CE", name: "Cédric", location: "Kinshasa, RDC 🇨🇩", time: "Il y a 5 minutes" },

            // AMÉRIQUE & CARAÏBES
            { initials: "SA", name: "Samuel", location: "Montréal, Canada 🇨🇦", time: "Il y a 2 minutes" },
            { initials: "JO", name: "Jordan", location: "Miami, États-Unis 🇺🇸", time: "Il y a 4 minutes" },
            { initials: "EN", name: "Enzo", location: "Fort-de-France, Martinique 🇲🇶", time: "Il y a 3 minutes" },
            { initials: "GA", name: "Gabriel", location: "São Paulo, Brésil 🇧🇷", time: "Il y a 7 minutes" },

            // AUTRES CONTINENTS & DOM-TOM
            { initials: "KA", name: "Karim", location: "Dubaï, Émirats Arabes 🇦🇪", time: "Il y a 8 minutes" },
            { initials: "MT", name: "Mathieu", location: "Saint-Denis, La Réunion 🇷🇪", time: "Il y a 1 minute" },
            { initials: "KE", name: "Kevin", location: "Bordeaux, France 🇫🇷", time: "Il y a 3 minutes" },
            { initials: "YO", name: "Youssef", location: "Tunis, Tunisie 🇹🇳", time: "Il y a 5 minutes" },
            { initials: "IS", name: "Ismaël", location: "Bamako, Mali 🇲🇱", time: "Il y a 4 minutes" },
            { initials: "DA", name: "David", location: "Pointe-à-Pitre, Guadeloupe 🇬🇵", time: "Il y a 2 minutes" },
            { initials: "KO", name: "Kofi", location: "Accra, Ghana 🇬🇭", time: "Il y a 6 minutes" },
            { initials: "KJ", name: "Kenji", location: "Tokyo, Japon 🇯🇵", time: "Il y a 9 minutes" },
            { initials: "RO", name: "Romain", location: "Luxembourg 🇱🇺", time: "Il y a 3 minutes" },
            { initials: "BR", name: "Brice", location: "Cotonou, Bénin 🇧🇯", time: "Il y a 2 minutes" }
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
            if (locEl) locEl.textContent = notif.location;
            timeEl.textContent = notif.time + ' • Achat vérifié 🟢';
            initialsEl.textContent = notif.initials;

            toast.classList.add('active');

            setTimeout(() => {
                toast.classList.remove('active');
                currentNotificationIndex = (currentNotificationIndex + 1) % salesNotifications.length;

                // Frequent rapid rotation between 3.5 to 6 seconds
                const nextDelay = Math.floor(Math.random() * 2500) + 3500;
                setTimeout(showSocialProofNotification, nextDelay);
            }, 4000);
        }
'''

content = re.sub(r'// Live International Social Proof Sales Notifications Engine.*?\s*function closeSocialProofToast', new_js_array + '\n\n        function closeSocialProofToast', content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated popups to purple initial badges with 25 fast-rotating international countries!")
