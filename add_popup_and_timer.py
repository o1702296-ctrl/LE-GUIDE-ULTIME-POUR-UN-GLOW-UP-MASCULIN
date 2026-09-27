import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update initial timer text in top bar from 14:59 to 23:59:59
content = content.replace('<div class="timer-box" id="timer">14:59</div>', '<div class="timer-box" id="timer">23:59:59</div>')

# 2. Add CSS for Social Proof Toast Popup before </style>
toast_css = '''
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
            max-width: 380px;
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
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: rgba(168, 85, 247, 0.2);
            border: 1px solid var(--accent-purple-bright);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            color: var(--accent-purple-bright);
            flex-shrink: 0;
        }

        .toast-text {
            flex-grow: 1;
            line-height: 1.35;
        }

        .toast-buyer {
            color: #ffffff;
            font-size: 0.88rem;
            margin: 0;
        }

        .toast-buyer strong {
            color: var(--accent-purple-glow);
            font-weight: 800;
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
content = content.replace('    </style>', toast_css)

# 3. Add Toast HTML element before </body>
toast_html = '''
    <!-- LIVE SOCIAL PROOF SALES NOTIFICATION TOAST -->
    <div id="social-proof-toast" class="social-proof-toast">
        <div class="toast-content">
            <button class="toast-close" onclick="closeSocialProofToast()">&times;</button>
            <div class="toast-avatar">
                <i class="fa-solid fa-fire" style="color: var(--accent-purple-bright);"></i>
            </div>
            <div class="toast-text">
                <p class="toast-buyer"><strong id="toast-name">Lucas (Lyon)</strong> vient de rejoindre</p>
                <p class="toast-product">LE GUIDE ULTIME POUR UN GLOW UP MASCULIN</p>
                <span class="toast-time" id="toast-time">Il y a 3 min • Achat vérifié</span>
            </div>
        </div>
    </div>
'''

# Replace old interactive scripts block with persistent 24h timer & toast popup JS
new_scripts = '''
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

        // Live Social Proof Sales Notification Popup Engine
        const salesNotifications = [
            { name: "Lucas (Lyon, France)", time: "Il y a 2 minutes" },
            { name: "Maxime (Paris, France)", time: "Il y a 4 minutes" },
            { name: "Théo (Abidjan, Côte d'Ivoire)", time: "Il y a 7 minutes" },
            { name: "Alexandre (Dakar, Sénégal)", time: "Il y a 1 minute" },
            { name: "Kevin (Bordeaux, France)", time: "Il y a 5 minutes" },
            { name: "Dylan (Douala, Cameroun)", time: "Il y a 3 minutes" },
            { name: "Rayan (Bruxelles, Belgique)", time: "Il y a 9 minutes" },
            { name: "Antoine (Lomé, Togo)", time: "Il y a 6 minutes" },
            { name: "Julien (Marseille, France)", time: "Il y a 2 minutes" },
            { name: "Cédric (Yaoundé, Cameroun)", time: "Il y a 8 minutes" },
            { name: "Mohamed (Casablanca, Maroc)", time: "Il y a 4 minutes" }
        ];

        let currentNotificationIndex = 0;

        function showSocialProofNotification() {
            const toast = document.querySelector('#social-proof-toast');
            const nameEl = document.querySelector('#toast-name');
            const timeEl = document.querySelector('#toast-time');
            if (!toast || !nameEl || !timeEl) return;

            const notif = salesNotifications[currentNotificationIndex];
            nameEl.textContent = notif.name;
            timeEl.textContent = notif.time + ' • Achat vérifié';

            toast.classList.add('active');

            setTimeout(() => {
                toast.classList.remove('active');
                currentNotificationIndex = (currentNotificationIndex + 1) % salesNotifications.length;

                const nextDelay = Math.floor(Math.random() * 5000) + 7000;
                setTimeout(showSocialProofNotification, nextDelay);
            }, 5000);
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
'''

script_pattern = r'<!-- INTERACTIVE SCRIPTS -->\s*<script>.*?</script>'
content = re.sub(script_pattern, toast_html + new_scripts, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Popup and 24h persistent timer added successfully!")
