import re

path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_dark_glowup_landing.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the salesNotifications JS array with varied time units (minutes, hours, days, weeks)
new_js_array = '''
        // Live International Social Proof Sales Notifications Engine (Varied Time Units: min, h, jours, semaines)
        const salesNotifications = [
            // EUROPE
            { initials: "LU", name: "Lucas", location: "Lyon, France 🇫🇷", time: "Il y a 3 minutes" },
            { initials: "MA", name: "Maxime", location: "Paris, France 🇫🇷", time: "Il y a 45 minutes" },
            { initials: "RA", name: "Rayan", location: "Bruxelles, Belgique 🇧🇪", time: "Il y a 2 heures" },
            { initials: "JU", name: "Julien", location: "Genève, Suisse 🇨🇭", time: "Il y a 5 heures" },
            { initials: "LI", name: "Liam", location: "Londres, Royaume-Uni 🇬🇧", time: "Il y a 1 jour" },

            // AFRIQUE
            { initials: "TH", name: "Théo", location: "Abidjan, Côte d'Ivoire 🇨🇮", time: "Il y a 12 minutes" },
            { initials: "AL", name: "Alexandre", location: "Dakar, Sénégal 🇸🇳", time: "Il y a 4 heures" },
            { initials: "DY", name: "Dylan", location: "Douala, Cameroun 🇨🇲", time: "Il y a 2 jours" },
            { initials: "MO", name: "Mohamed", location: "Casablanca, Maroc 🇲🇦", time: "Il y a 1 semaine" },
            { initials: "AN", name: "Antoine", location: "Lomé, Togo 🇹🇬", time: "Il y a 8 heures" },
            { initials: "CE", name: "Cédric", location: "Kinshasa, RDC 🇨🇩", time: "Il y a 3 jours" },

            // AMÉRIQUE & CARAÏBES
            { initials: "SA", name: "Samuel", location: "Montréal, Canada 🇨🇦", time: "Il y a 25 minutes" },
            { initials: "JO", name: "Jordan", location: "Miami, États-Unis 🇺🇸", time: "Il y a 6 heures" },
            { initials: "EN", name: "Enzo", location: "Fort-de-France, Martinique 🇲🇶", time: "Il y a 1 jour" },
            { initials: "GA", name: "Gabriel", location: "São Paulo, Brésil 🇧🇷", time: "Il y a 4 jours" },

            // AUTRES CONTINENTS & DOM-TOM
            { initials: "KA", name: "Karim", location: "Dubaï, Émirats Arabes 🇦🇪", time: "Il y a 2 semaines" },
            { initials: "MT", name: "Mathieu", location: "Saint-Denis, La Réunion 🇷🇪", time: "Il y a 14 minutes" },
            { initials: "KE", name: "Kevin", location: "Bordeaux, France 🇫🇷", time: "Il y a 3 heures" },
            { initials: "YO", name: "Youssef", location: "Tunis, Tunisie 🇹🇳", time: "Il y a 2 jours" },
            { initials: "IS", name: "Ismaël", location: "Bamako, Mali 🇲🇱", time: "Il y a 10 heures" },
            { initials: "DA", name: "David", location: "Pointe-à-Pitre, Guadeloupe 🇬🇵", time: "Il y a 1 semaine" },
            { initials: "KO", name: "Kofi", location: "Accra, Ghana 🇬🇭", time: "Il y a 5 jours" },
            { initials: "KJ", name: "Kenji", location: "Tokyo, Japon 🇯🇵", time: "Il y a 18 heures" },
            { initials: "RO", name: "Romain", location: "Luxembourg 🇱🇺", time: "Il y a 35 minutes" },
            { initials: "BR", name: "Brice", location: "Cotonou, Bénin 🇧🇯", time: "Il y a 2 heures" }
        ];
'''

content = re.sub(r'// Live International Social Proof Sales Notifications Engine.*?\];', new_js_array.strip(), content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated popups to vary across minutes, hours, days, and weeks!")
