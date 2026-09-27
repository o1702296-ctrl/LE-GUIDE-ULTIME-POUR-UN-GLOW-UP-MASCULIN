import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update toast avatar CSS in build script
new_toast_css = '''
        /* LIVE SOCIAL PROOF NOTIFICATION TOAST */
        .social-proof-toast {
            position: fixed;
            bottom: 24px;
            left: 24px;
            z-index: 9999;
            background: rgba(14, 9, 26, 0.96);
            border: 1px solid var(--accent-purple);
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.9), 0 0 25px rgba(168, 85, 247, 0.4);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            max-width: 400px;
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

        .toast-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: 2px solid var(--accent-purple-bright);
            overflow: hidden;
            flex-shrink: 0;
            box-shadow: 0 0 15px rgba(168, 85, 247, 0.5);
            background: #000;
        }

        .toast-profile-pic {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top center;
            display: block;
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

# Replace toast CSS
content = re.sub(r'/\* LIVE SOCIAL PROOF NOTIFICATION TOAST \*/.*?</style>', new_toast_css, content, flags=re.DOTALL)

# 2. Update Toast HTML structure
new_toast_html = '''
    <!-- LIVE SOCIAL PROOF SALES NOTIFICATION TOAST -->
    <div id="social-proof-toast" class="social-proof-toast">
        <div class="toast-content">
            <button class="toast-close" onclick="closeSocialProofToast()">&times;</button>
            <div class="toast-avatar">
                <img id="toast-avatar-img" src="images/testimonial_before_after_1.jpg" alt="Avatar acheteur" class="toast-profile-pic">
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

# 3. Update JavaScript Sales Notifications Array & Display Logic
new_js_array = '''
        // Live International Social Proof Sales Notifications Engine (Europe, Afrique, Amérique, etc.)
        const salesNotifications = [
            // EUROPE
            { name: "Lucas", location: "Lyon, France 🇫🇷", time: "Il y a 2 minutes", avatar: "images/testimonial_before_after_1.jpg" },
            { name: "Maxime", location: "Paris, France 🇫🇷", time: "Il y a 4 minutes", avatar: "images/testimonial_before_after_2.png" },
            { name: "Rayan", location: "Bruxelles, Belgique 🇧🇪", time: "Il y a 6 minutes", avatar: "images/point1_blue_eyes_shirt.png" },
            { name: "Julien", location: "Genève, Suisse 🇨🇭", time: "Il y a 3 minutes", avatar: "images/point4_glasses_suit.png" },
            { name: "Liam", location: "Londres, Royaume-Uni 🇬🇧", time: "Il y a 8 minutes", avatar: "images/point3_suit_sofa.png" },

            // AFRIQUE
            { name: "Théo", location: "Abidjan, Côte d'Ivoire 🇨🇮", time: "Il y a 1 minute", avatar: "images/testimonial_before_after_3.png" },
            { name: "Alexandre", location: "Dakar, Sénégal 🇸🇳", time: "Il y a 5 minutes", avatar: "images/point2_black_curly_hair.png" },
            { name: "Dylan", location: "Douala, Cameroun 🇨🇲", time: "Il y a 3 minutes", avatar: "images/point6_sunglasses_white_shirt.png" },
            { name: "Mohamed", location: "Casablanca, Maroc 🇲🇦", time: "Il y a 9 minutes", avatar: "images/point5_denim_jacket_bag.png" },
            { name: "Antoine", location: "Lomé, Togo 🇹🇬", time: "Il y a 4 minutes", avatar: "images/glowup_profile_red_eyes.jpg" },
            { name: "Cédric", location: "Kinshasa, RDC 🇨🇩", time: "Il y a 7 minutes", avatar: "images/glowup_messy_hair_chain.jpg" },

            // AMÉRIQUE
            { name: "Samuel", location: "Montréal, Canada 🇨🇦", time: "Il y a 2 minutes", avatar: "images/point4_glasses_suit.png" },
            { name: "Jordan", location: "Miami, États-Unis 🇺🇸", time: "Il y a 5 minutes", avatar: "images/point6_sunglasses_white_shirt.png" },
            { name: "Enzo", location: "Fort-de-France, Martinique 🇲🇶", time: "Il y a 4 minutes", avatar: "images/point2_black_curly_hair.png" },

            // AUTRES CONTINENTS / DOM-TOM
            { name: "Karim", location: "Dubaï, Émirats Arabes 🇦🇪", time: "Il y a 8 minutes", avatar: "images/glowup_suit_gold_tie_mockup.jpg" },
            { name: "Mathieu", location: "Saint-Denis, La Réunion 🇷🇪", time: "Il y a 6 minutes", avatar: "images/point1_blue_eyes_shirt.png" }
        ];

        let currentNotificationIndex = 0;

        function showSocialProofNotification() {
            const toast = document.querySelector('#social-proof-toast');
            const nameEl = document.querySelector('#toast-name');
            const locEl = document.querySelector('#toast-location');
            const timeEl = document.querySelector('#toast-time');
            const avatarImg = document.querySelector('#toast-avatar-img');
            if (!toast || !nameEl || !timeEl || !avatarImg) return;

            const notif = salesNotifications[currentNotificationIndex];
            nameEl.textContent = notif.name;
            if (locEl) locEl.textContent = notif.location;
            timeEl.textContent = notif.time + ' • Achat vérifié 🟢';
            avatarImg.src = notif.avatar;

            toast.classList.add('active');

            setTimeout(() => {
                toast.classList.remove('active');
                currentNotificationIndex = (currentNotificationIndex + 1) % salesNotifications.length;

                const nextDelay = Math.floor(Math.random() * 5000) + 7000;
                setTimeout(showSocialProofNotification, nextDelay);
            }, 5000);
        }
'''

content = re.sub(r'// Live Social Proof Sales Notification Popup Engine.*?\s*function closeSocialProofToast', new_js_array + '\n\n        function closeSocialProofToast', content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated popups with international buyers and matching profile photos!")
