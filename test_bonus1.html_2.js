
        var VoiceReader = {
            queue: [],
            currentIndex: 0,
            isPlaying: false,
            isPaused: false,
            playbackRate: 1.0,
            utterance: null,
            keepAliveInterval: null,

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

            splitTextIntoSentences: function(text) {
                if (!text) return [];
                var parts = text.split(/(?<=[.!?؟،])\s+/);
                var chunks = [];
                parts.forEach(function(p) {
                    var trimmed = p.trim();
                    if (trimmed.length > 0) {
                        if (trimmed.length > 200) {
                            var clauses = trimmed.split(/(?<=[,;:])\s+/);
                            clauses.forEach(function(c) {
                                var sub = c.trim();
                                if (sub.length > 0) chunks.push(sub);
                            });
                        } else {
                            chunks.push(trimmed);
                        }
                    }
                });
                return chunks.length > 0 ? chunks : [text];
            },

            collectReadableElements: function() {
                var container = document.querySelector('.pdf-document-container');
                if (!container) return [];

                var selectors = [
                    '.cover-top-header', '.cover-main-title', '.cover-subtitle', '.cover-tagline', '.cover-author-name', '.cover-bottom-bar',
                    'h1', 'h2', 'h3', 'p',
                    '.pdf-quote-text', '.pdf-sister-header',
                    '.pdf-metaphor-header', '.pdf-metaphor-body',
                    '.toc-chapter-title', '.toc-chapter-sub',
                    '.phrase-text', '.error-title', '.error-row span'
                ].join(', ');

                var candidates = container.querySelectorAll(selectors);
                var queueItems = [];
                var self = this;

                candidates.forEach(function(el) {
                    if (el.offsetWidth === 0 && el.offsetHeight === 0) return;
                    
                    var text = el.innerText ? el.innerText.trim() : '';
                    if (text.length > 1) {
                        var sentences = self.splitTextIntoSentences(text);
                        sentences.forEach(function(sentence) {
                            queueItems.push({
                                element: el,
                                text: sentence
                            });
                        });
                    }
                });

                return queueItems;
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
                this.queue = this.collectReadableElements();
                if (this.queue.length === 0) {
                    alert('Aucun texte à lire trouvé.');
                    return;
                }

                this.currentIndex = 0;
                this.isPlaying = true;
                this.isPaused = false;

                this.startKeepAlive();
                this.updateUI(true);
                this.readCurrent();
            },

            readCurrent: function() {
                if (!this.isPlaying || this.currentIndex >= this.queue.length) {
                    this.stop();
                    return;
                }

                this.clearHighlights();

                var item = this.queue[this.currentIndex];
                if (item.element) {
                    item.element.classList.add('voice-active-highlight');
                    item.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }

                var self = this;
                this.utterance = new SpeechSynthesisUtterance(item.text);
                this.utterance.lang = this.getActiveLanguage();
                this.utterance.rate = this.playbackRate;

                this.utterance.onend = function() {
                    if (self.isPlaying && !self.isPaused) {
                        self.currentIndex++;
                        setTimeout(function() {
                            self.readCurrent();
                        }, 150);
                    }
                };

                this.utterance.onerror = function(e) {
                    console.warn('Speech error, advancing to next sentence:', e);
                    if (self.isPlaying) {
                        self.currentIndex++;
                        setTimeout(function() {
                            self.readCurrent();
                        }, 150);
                    }
                };

                var playerWidget = document.getElementById('voice-player-floating');
                if (playerWidget) playerWidget.classList.add('speaking');

                this.updateStatusText();
                window.speechSynthesis.speak(this.utterance);
            },

            startKeepAlive: function() {
                this.stopKeepAlive();
                this.keepAliveInterval = setInterval(function() {
                    if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {
                        window.speechSynthesis.pause();
                        window.speechSynthesis.resume();
                    }
                }, 8000);
            },

            stopKeepAlive: function() {
                if (this.keepAliveInterval) {
                    clearInterval(this.keepAliveInterval);
                    this.keepAliveInterval = null;
                }
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
                this.stopKeepAlive();
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
                if (statusElem && this.queue.length > 0) {
                    var pct = Math.round(((this.currentIndex + 1) / this.queue.length) * 100);
                    statusElem.innerText = 'Lecture : ' + (this.currentIndex + 1) + ' / ' + this.queue.length + ' (' + pct + '%)';
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
    