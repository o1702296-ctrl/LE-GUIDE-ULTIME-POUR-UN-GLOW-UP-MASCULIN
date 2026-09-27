script_path = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_eloquence_structured_violet_landing.py'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove "PDF"
content = content.replace('Guide Complet (9 Chapitres PDF)', 'Guide Complet (9 Chapitres)')
content = content.replace('Format numérique PDF téléchargeable', 'Format numérique téléchargeable')

# 2. Initial HTML display for countdown badge
content = content.replace('>00:14:59<', '>23:59:59<')

# 3. Update startTimer JS function & 24h duration initialization
old_timer_func = """        function startTimer(duration, display) {{
            let timer = duration, minutes, seconds;
            setInterval(function () {{
                minutes = parseInt(timer / 60, 10);
                seconds = parseInt(timer % 60, 10);

                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                display.textContent = "00:" + minutes + ":" + seconds;

                if (--timer < 0) {{
                    timer = duration;
                }}
            }}, 1000);
        }}"""

new_timer_func = """        function startTimer(duration, display) {{
            let timer = duration, hours, minutes, seconds;
            setInterval(function () {{
                hours = parseInt(timer / 3600, 10);
                minutes = parseInt((timer % 3600) / 60, 10);
                seconds = parseInt(timer % 60, 10);

                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                display.textContent = hours + ":" + minutes + ":" + seconds;

                if (--timer < 0) {{
                    timer = duration;
                }}
            }}, 1000);
        }}"""

content = content.replace(old_timer_func, new_timer_func)

# Update window.onload duration initialization
old_onload_timer = """            let fifteenMinutes = 60 * 14 + 59,
                display = document.querySelector('#countdown');
            startTimer(fifteenMinutes, display);"""

new_onload_timer = """            let twentyFourHours = 24 * 3600 - 1,
                display = document.querySelector('#countdown');
            startTimer(twentyFourHours, display);"""

content = content.replace(old_onload_timer, new_onload_timer)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated PDF removal and 24h timer in build script.")
