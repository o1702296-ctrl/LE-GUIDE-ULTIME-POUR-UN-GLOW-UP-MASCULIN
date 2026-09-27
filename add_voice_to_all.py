# -*- coding: utf-8 -*-
import os
import re

voice_css_js_markup = r"""
    <!-- Voice Reader & Lip-Sync Styles -->
    <style>
        .btn-voice-toggle {
            background: linear-gradient(135deg, #7e22ce, #a855f7);
            color: #ffffff;
            border: 1px solid #c084fc;
            padding: 7px 16px;
            border-radius: 20px;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.88rem;
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
        }
        .btn-voice-toggle:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(168, 85, 247, 0.6);
            background: linear-gradient(135deg, #9333ea, #c084fc);
        }

        .voice-player-floating {
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 3000;
            background: rgba(26, 6, 54, 0.95);
            backdrop-filter: blur(12px);
            border: 1.5px solid #a855f7;
            border-radius: 16px;
            padding: 14px 20px;
            box-shadow: 0 10px 35px rgba(0,0,0,0.6);
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 16px;
            max-width: 440px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            transform: translateY(150%);
            opacity: 0;
            pointer-events: none;
        }

        .voice-player-floating.active {
            transform: translateY(0);
            opacity: 1;
            pointer-events: auto;
        }

        .avatar-lipsync-container {
            position: relative;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7e22ce, #a855f7);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 4px 15px rgba(168, 85, 247, 0.5);
        }

        .avatar-lipsync-container i {
            font-size: 1.3rem;
            color: #ffffff;
        }

        .soundwave-bars {
            display: flex;
            align-items: flex-end;
            gap: 3px;
            height: 18px;
            position: absolute;
            bottom: -4px;
        }

        .soundwave-bar {
            width: 3px;
            background: #c084fc;
            border-radius: 2px;
            height: 6px;
            transition: height 0.2s ease;
        }

        .voice-player-floating.speaking .soundwave-bar:nth-child(1) { animation: waveAnim 0.6s infinite alternate ease-in-out; }
        .voice-player-floating.speaking .soundwave-bar:nth-child(2) { animation: waveAnim 0.6s 0.2s infinite alternate ease-in-out; }
        .voice-player-floating.speaking .soundwave-bar:nth-child(3) { animation: waveAnim 0.6s 0.4s infinite alternate ease-in-out; }

        @keyframes waveAnim {
            0% { height: 4px; }
            100% { height: 18px; }
        }

        .voice-info-group {
            display: flex;
            flex-direction: column;
            gap: 2px;
            flex: 1;
            overflow: hidden;
        }

        .voice-title {
            font-family: var(--font-heading);
            font-weight: 800;
            font-size: 0.92rem;
            color: #ffffff;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .voice-status {
            font-size: 0.78rem;
            color: #e9d5ff;
            font-style: italic;
        }

        .voice-controls-btns {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .btn-voice-ctrl {
            background: rgba(168, 85, 247, 0.2);
            border: 1px solid rgba(168, 85, 247, 0.4);
            color: #ffffff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .btn-voice-ctrl:hover {
            background: #a855f7;
            transform: scale(1.08);
        }

        .voice-speed-select {
            background: #2e1065;
            border: 1px solid #a855f7;
            color: #ffffff;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            outline: none;
        }

        .voice-active-highlight {
            outline: 3px solid #a855f7 !important;
            outline-offset: 4px;
            border-radius: 8px;
            background-color: rgba(192, 132, 252, 0.15) !important;
            transition: all 0.3s ease;
            box-shadow: 0 0 25px rgba(168, 85, 247, 0.4) !important;
        }
    </style>

    <!-- Floating Lip-Sync Audio Player Widget -->
    <div id="voice-player-floating" class="voice-player-floating">
        <div class="avatar-lipsync-container">
            <i class="fa-solid fa-headset"></i>
            <div class="soundwave-bars">
                <div class="soundwave-bar"></div>
                <div class="soundwave-bar"></div>
                <div class="soundwave-bar"></div>
            </div>
        </div>

        <div class="voice-info-group">
            <div class="voice-title">Lina Rela — Synchro Vocale</div>
            <div class="voice-status" id="voice-status-text">Initialisation...</div>
        </div>

        <div class="voice-controls-btns">
            <select class="voice-speed-select" onchange="VoiceReader.setSpeed(this.value)">
                <option value="1.0">1.0x</option>
                <option value="1.25">1.25x</option>
                <option value="1.5">1.5x</option>
            </select>
            <button class="btn-voice-ctrl" onclick="VoiceReader.toggle()" title="Play / Pause">
                <i id="voice-play-icon" class="fa-solid fa-play"></i>
            </button>
            <button class="btn-voice-ctrl" onclick="VoiceReader.stop()" title="Arrêter">
                <i class="fa-solid fa-stop"></i>
            </button>
        </div>
    </div>

    <!-- Voice Reader Script Engine -->
    <script type="text/javascript">
        var VoiceReader = {
            elements: [],
            currentIndex: 0,
            isPlaying: false,
            isPaused: false,
            playbackRate: 1.0,
            utterance: null,

            LANG_MAP: {
                'fr': 'fr-FR',
                'en': 'en-US',
                'es': 'es-ES',
                'de': 'de-DE',
                'it': 'it-IT',
                'pt': 'pt-PT',
                'nl': 'nl-NL',
                'ar': 'ar-SA',
                'ru': 'ru-RU',
                'zh-CN': 'zh-CN',
                'ja': 'ja-JP'
            },

            getActiveLanguage: function() {
                var savedLang = localStorage.getItem('selected_landing_lang') || 'fr';
                return this.LANG_MAP[savedLang] || 'fr-FR';
            },

            collectReadableElements: function() {
                var container = document.querySelector('.pdf-document-container');
                if (!container) return [];
                var candidates = container.querySelectorAll('h1, h2, h3, p.para, .pdf-quote-text, .pdf-sister-box p, .pdf-metaphor-body, .cover-tagline, .phrase-text, .error-title, .error-row span:not(.badge-err):not(.badge-sol)');
                var items = [];
                candidates.forEach(function(el) {
                    var text = el.innerText.trim();
                    if (text && text.length > 1) {
                        items.push({ element: el, text: text });
                    }
                });
                return items;
            },

            toggle: function() {
                if (this.isPlaying) {
                    if (this.isPaused) {
                        this.resume();
                    } else {
                        this.pause();
                    }
                } else {
                    this.start();
                }
            },

            start: function() {
                if (!('speechSynthesis' in window)) {
                    alert('La synthèse vocale n\'est pas supportée sur ce navigateur.');
                    return;
                }
                window.speechSynthesis.cancel();
                this.elements = this.collectReadableElements();
                if (this.elements.length === 0) return;

                this.currentIndex = 0;
                this.isPlaying = true;
                this.isPaused = false;

                this.updateUI(true);
                this.readCurrent();
            },

            readCurrent: function() {
                if (!this.isPlaying || this.currentIndex >= this.elements.length) {
                    this.stop();
                    return;
                }

                this.clearHighlights();

                var item = this.elements[this.currentIndex];
                item.element.classList.add('voice-active-highlight');
                item.element.scrollIntoView({ behavior: 'smooth', block: 'center' });

                var self = this;
                this.utterance = new SpeechSynthesisUtterance(item.text);
                this.utterance.lang = this.getActiveLanguage();
                this.utterance.rate = this.playbackRate;

                this.utterance.onend = function() {
                    if (self.isPlaying && !self.isPaused) {
                        self.currentIndex++;
                        setTimeout(function() {
                            self.readCurrent();
                        }, 180);
                    }
                };

                this.utterance.onerror = function(e) {
                    console.error('Speech error:', e);
                    if (self.isPlaying) {
                        self.currentIndex++;
                        self.readCurrent();
                    }
                };

                var playerWidget = document.getElementById('voice-player-floating');
                if (playerWidget) playerWidget.classList.add('speaking');

                this.updateStatusText();
                window.speechSynthesis.speak(this.utterance);
            },

            pause: function() {
                if (window.speechSynthesis.speaking) {
                    window.speechSynthesis.pause();
                    this.isPaused = true;
                    this.updateUIState();
                }
            },

            resume: function() {
                if (window.speechSynthesis.paused) {
                    window.speechSynthesis.resume();
                    this.isPaused = false;
                    this.updateUIState();
                } else {
                    this.readCurrent();
                }
            },

            stop: function() {
                window.speechSynthesis.cancel();
                this.isPlaying = false;
                this.isPaused = false;
                this.clearHighlights();
                this.updateUI(false);
            },

            setSpeed: function(rate) {
                this.playbackRate = parseFloat(rate);
                if (this.isPlaying) {
                    window.speechSynthesis.cancel();
                    this.readCurrent();
                }
            },

            clearHighlights: function() {
                document.querySelectorAll('.voice-active-highlight').forEach(function(el) {
                    el.classList.remove('voice-active-highlight');
                });
            },

            updateStatusText: function() {
                var statusElem = document.getElementById('voice-status-text');
                if (statusElem && this.elements.length > 0) {
                    var pct = Math.round(((this.currentIndex + 1) / this.elements.length) * 100);
                    statusElem.innerText = 'Élément ' + (this.currentIndex + 1) + ' / ' + this.elements.length + ' (' + pct + '%)';
                }
            },

            updateUI: function(active) {
                var widget = document.getElementById('voice-player-floating');
                if (widget) {
                    if (active) widget.classList.add('active');
                    else widget.classList.remove('active', 'speaking');
                }
                this.updateUIState();
            },

            updateUIState: function() {
                var playBtnIcon = document.getElementById('voice-play-icon');
                var topBtnText = document.getElementById('top-voice-btn-text');
                var widget = document.getElementById('voice-player-floating');

                if (this.isPlaying && !this.isPaused) {
                    if (playBtnIcon) playBtnIcon.className = 'fa-solid fa-pause';
                    if (topBtnText) topBtnText.innerText = 'Pause Vocale';
                    if (widget) widget.classList.add('speaking');
                } else if (this.isPaused) {
                    if (playBtnIcon) playBtnIcon.className = 'fa-solid fa-play';
                    if (topBtnText) topBtnText.innerText = 'Reprendre Vocale';
                    if (widget) widget.classList.remove('speaking');
                } else {
                    if (playBtnIcon) playBtnIcon.className = 'fa-solid fa-play';
                    if (topBtnText) topBtnText.innerText = 'Écouter';
                    if (widget) widget.classList.remove('speaking');
                }
            }
        };

        window.addEventListener('beforeunload', function() {
            VoiceReader.stop();
        });
    </script>
"""

# Update generate_full_guide_html.py
py1 = r'C:\Users\HP TTS\.gemini\antigravity\scratch\generate_full_guide_html.py'
with open(py1, 'r', encoding='utf-8') as f:
    c1 = f.read()

btn_guide = """            <button id="btn-global-voice-start" class="btn-voice-toggle" onclick="VoiceReader.toggle()">
                <i class="fa-solid fa-volume-high"></i> <span id="top-voice-btn-text">Écouter</span>
            </button>
            <div class="pdf-lang-dropdown">"""

c1 = c1.replace('<div class="pdf-lang-dropdown">', btn_guide)
c1 = c1.replace('</body>', voice_css_js_markup + '\n</body>')

with open(py1, 'w', encoding='utf-8') as f:
    f.write(c1)

# Update build_bonus1_html.py
py2 = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_bonus1_html.py'
with open(py2, 'r', encoding='utf-8') as f:
    c2 = f.read()

c2 = c2.replace('<div class="pdf-lang-dropdown">', btn_guide)
c2 = c2.replace('</body>', voice_css_js_markup + '\n</body>')

with open(py2, 'w', encoding='utf-8') as f:
    f.write(c2)

# Update build_bonus2_html.py
py3 = r'C:\Users\HP TTS\.gemini\antigravity\scratch\build_bonus2_html.py'
with open(py3, 'r', encoding='utf-8') as f:
    c3 = f.read()

c3 = c3.replace('<div class="pdf-lang-dropdown">', btn_guide)
c3 = c3.replace('</body>', voice_css_js_markup + '\n</body>')

with open(py3, 'w', encoding='utf-8') as f:
    f.write(c3)

print("Voice engine integrated into all 3 generator scripts!")
