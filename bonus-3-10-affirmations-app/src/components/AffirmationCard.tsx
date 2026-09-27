import React, { useState } from 'react';
import { AffirmationItem, Language, UI_TRANSLATIONS } from '../data/affirmationsData';
import { Copy, Check, Volume2, RotateCcw, Heart, Sparkles } from 'lucide-react';

interface AffirmationCardProps {
  item: AffirmationItem;
  currentLang: Language;
  index: number;
}

export const AffirmationCard: React.FC<AffirmationCardProps> = ({
  item,
  currentLang,
  index
}) => {
  const [copied, setCopied] = useState(false);
  const [repeatCount, setRepeatCount] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);

  const ui = UI_TRANSLATIONS[currentLang];
  const text = item.text[currentLang];
  const isRtl = currentLang === 'ar';

  const handleCopy = () => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleRepeat = () => {
    setRepeatCount(prev => prev + 1);

    // Use Web Speech API if available
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      const langCodes: Record<Language, string> = {
        fr: 'fr-FR', en: 'en-US', es: 'es-ES', de: 'de-DE',
        it: 'it-IT', pt: 'pt-PT', nl: 'nl-NL', ru: 'ru-RU',
        tr: 'tr-TR', ar: 'ar-SA'
      };
      utterance.lang = langCodes[currentLang] || 'fr-FR';
      utterance.rate = 0.9;
      utterance.onstart = () => setIsPlaying(true);
      utterance.onend = () => setIsPlaying(false);
      utterance.onerror = () => setIsPlaying(false);
      window.speechSynthesis.speak(utterance);
    }
  };

  return (
    <div 
      className="group relative bg-gradient-to-b from-stone-900 via-stone-900/95 to-stone-950 rounded-2xl border border-rose-900/40 p-6 md:p-8 shadow-xl hover:shadow-rose-950/30 hover:border-rose-700/60 transition-all duration-300 flex flex-col justify-between"
      dir={isRtl ? 'rtl' : 'ltr'}
    >
      {/* Top Badge & Number */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-2">
          <span className="w-8 h-8 rounded-full bg-rose-950/80 border border-rose-800/50 text-rose-300 font-serif text-sm font-bold flex items-center justify-center shadow-inner">
            {index + 1}
          </span>
          <span className="text-xs font-semibold tracking-wider text-amber-400/90 uppercase">
            {ui.affLabel} {index + 1}
          </span>
        </div>

        {repeatCount > 0 && (
          <div className="flex items-center gap-1 text-xs text-rose-300 bg-rose-950/60 px-2.5 py-1 rounded-full border border-rose-800/40">
            <Heart className="w-3 h-3 text-rose-500 fill-rose-500 animate-pulse" />
            <span>Répété {repeatCount}x</span>
          </div>
        )}
      </div>

      {/* Main Quote Content */}
      <div className="my-4 relative">
        <div className="text-rose-500/10 text-6xl font-serif absolute -top-8 -left-2 select-none">
          “
        </div>
        <p className={`font-serif text-lg md:text-xl leading-relaxed font-medium relative z-10 p-4 rounded-xl transition-all duration-300 ${
          isPlaying
            ? 'bg-gradient-to-r from-rose-950/90 via-amber-950/90 to-rose-950/90 text-amber-200 border-2 border-amber-400 ring-4 ring-amber-400/30 scale-[1.02] shadow-2xl font-bold'
            : 'text-stone-100'
        }`}>
          {text}
        </p>
        <div className="text-rose-500/10 text-6xl font-serif absolute -bottom-10 right-0 select-none">
          ”
        </div>
      </div>

      {/* Action Buttons */}
      <div className="mt-8 pt-4 border-t border-stone-800/80 flex items-center justify-between gap-3 flex-wrap">
        <button
          onClick={handleRepeat}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold transition shadow-md ${
            isPlaying
              ? 'bg-rose-600 text-white animate-pulse'
              : 'bg-stone-800 hover:bg-rose-950 text-rose-200 border border-rose-900/50 hover:border-rose-600'
          }`}
        >
          <Volume2 className={`w-4 h-4 ${isPlaying ? 'animate-bounce' : 'text-rose-400'}`} />
          <span>{ui.repeatBtn}</span>
        </button>

        <button
          onClick={handleCopy}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold transition shadow-md ${
            copied
              ? 'bg-emerald-900/80 text-emerald-200 border border-emerald-600'
              : 'bg-stone-800 hover:bg-stone-700 text-stone-200 border border-stone-700 hover:border-stone-500'
          }`}
        >
          {copied ? (
            <>
              <Check className="w-4 h-4 text-emerald-400" />
              <span>{ui.copiedBtn}</span>
            </>
          ) : (
            <>
              <Copy className="w-4 h-4 text-stone-400" />
              <span>{ui.copyBtn}</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
};
