import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for crisp flag images
flag_css = '''
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
'''
content = content.replace('    </style>', flag_css)

# 2. Update Toast HTML structure to include crisp flag img tag
new_toast_html = '''
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
'''

content = re.sub(r'<!-- LIVE SOCIAL PROOF SALES NOTIFICATION TOAST -->\s*<div id="social-proof-toast".*?</div>\s*</div>', new_toast_html, content, flags=re.DOTALL)

# 3. Update JavaScript array with country codes & flag URLs
new_js_array = '''
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
'''

content = re.sub(r'// Live International Social Proof Sales Notifications Engine.*?\s*function closeSocialProofToast', new_js_array + '\n\n        function closeSocialProofToast', content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added crisp country flag images next to all country names!")
