import React, { useState } from 'react';
import { GesteItem, Language, UI_TRANSLATIONS } from '../data/gestesData';
import { Eye, Smile, Hand, ShieldCheck, Volume2, VolumeX, Sparkles } from 'lucide-react';

interface GesteCardProps {
  geste: GesteItem;
  language: Language;
}

const GESTE_ICONS = [
  Eye,          // 1. Regard
  Smile,        // 2. Sourire
  Hand,         // 3. Toucher
  ShieldCheck,  // 4. Posture
  Volume2       // 5. Silence
];

export const GesteCard: React.FC<GesteCardProps> = ({ geste, language }) => {
  const [isPlaying, setIsPlaying] = useState(false);

  const t = UI_TRANSLATIONS[language] || UI_TRANSLATIONS.fr;
  const gesteTitle = geste.title[language] || geste.title.fr;
  const gesteText = geste.text[language] || geste.text.fr;
  const IconComponent = GESTE_ICONS[(geste.id - 1) % GESTE_ICONS.length];

  const handlePlayAudio = () => {
    if (isPlaying) {
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      setIsPlaying(false);
      return;
    }

    const textToRead = `${gesteTitle}. ${gesteText}`;

    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(textToRead);
      const langCodes: Record<Language, string> = {
        fr: 'fr-FR', en: 'en-US', es: 'es-ES', de: 'de-DE',
        it: 'it-IT', pt: 'pt-PT', nl: 'nl-NL', ru: 'ru-RU',
        tr: 'tr-TR', ar: 'ar-SA'
      };
      utterance.lang = langCodes[language] || 'fr-FR';
      utterance.rate = 0.9;
      utterance.onstart = () => setIsPlaying(true);
      utterance.onend = () => setIsPlaying(false);
      utterance.onerror = () => setIsPlaying(false);
      window.speechSynthesis.speak(utterance);
    }
  };

  return (
    <div className="geste-card-container bg-gradient-to-br from-[#1f0611] via-[#2a0b1b] to-[#15030b] border border-pink-900/50 rounded-2xl p-6 sm:p-8 shadow-2xl relative overflow-hidden transition hover:border-pink-500/60">
      {/* Background Ambient Glow */}
      <div className="absolute top-0 right-0 w-36 h-36 bg-pink-500/10 rounded-full blur-2xl pointer-events-none" />

      <div className="flex items-center justify-between gap-4 mb-4 pb-3 border-b border-pink-900/40">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-pink-500/20 border border-pink-500/40 flex items-center justify-center text-pink-300 font-serif font-extrabold text-lg shadow-inner">
            {geste.id}
          </div>
          <span className="text-xs sm:text-sm font-bold tracking-wider text-pink-300 uppercase">
            {t.gesteLabel} #{geste.id}
          </span>
        </div>

        <div className="p-2.5 rounded-xl bg-purple-900/30 border border-purple-500/30 text-pink-300">
          <IconComponent className="w-5 h-5 text-pink-400" />
        </div>
      </div>

      {/* Geste Title */}
      <h3 className="font-serif-title text-xl sm:text-2xl font-bold text-white mb-3 tracking-tight flex items-center justify-between gap-2">
        <span>{gesteTitle}</span>
      </h3>

      {/* Geste Description Paragraph with Lip-Sync Karaoke Highlight */}
      <div className={`p-5 rounded-xl text-base sm:text-lg font-sans leading-relaxed shadow-inner mb-4 transition-all duration-300 ${
        isPlaying
          ? 'bg-gradient-to-r from-pink-950/90 via-purple-900/90 to-pink-950/90 text-amber-200 border-2 border-amber-400 ring-4 ring-amber-400/30 scale-[1.02] shadow-2xl font-semibold'
          : 'bg-[#14020a]/80 border border-pink-950/60 text-pink-100'
      }`}>
        {gesteText}
      </div>

      {/* Audio Button */}
      <div className="flex justify-end">
        <button
          onClick={handlePlayAudio}
          className={`px-4 py-2 rounded-full font-semibold text-xs sm:text-sm transition flex items-center gap-2 shadow-lg cursor-pointer ${
            isPlaying
              ? 'bg-rose-600 text-white animate-pulse'
              : 'bg-stone-800 hover:bg-pink-950 text-pink-200 border border-pink-900/50 hover:border-pink-600'
          }`}
        >
          {isPlaying ? (
            <>
              <VolumeX className="w-4 h-4 text-white animate-bounce" />
              <span>Stop</span>
            </>
          ) : (
            <>
              <Volume2 className="w-4 h-4 text-pink-400" />
              <span>Écouter le geste</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
};
