import React, { useState } from 'react';
import { SmsItem, Language, UI_TRANSLATIONS } from '../data/smsData';
import { Copy, Check, MessageCircleHeart, Volume2, VolumeX } from 'lucide-react';

interface SmsCardProps {
  sms: SmsItem;
  language: Language;
}

export const SmsCard: React.FC<SmsCardProps> = ({ sms, language }) => {
  const [copied, setCopied] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);

  const t = UI_TRANSLATIONS[language] || UI_TRANSLATIONS.fr;
  const smsText = sms.text[language] || sms.text.fr;

  const handleCopy = () => {
    // Strip surrounding quotes for easy pasting into messaging apps
    const cleanText = smsText.replace(/^["«\s]+|["»\s]+$/g, '');
    navigator.clipboard.writeText(cleanText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  const handlePlayAudio = () => {
    if (isPlaying) {
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      setIsPlaying(false);
      return;
    }

    if (!smsText) return;

    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(smsText);
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
    <div className="sms-card-container bg-gradient-to-br from-[#1f0611] via-[#2a0b1b] to-[#15030b] border border-pink-900/50 rounded-2xl p-6 sm:p-8 shadow-2xl relative overflow-hidden transition hover:border-pink-500/60">
      {/* Glow Effect */}
      <div className="absolute top-0 right-0 w-32 h-32 bg-pink-500/10 rounded-full blur-2xl pointer-events-none" />

      <div className="flex items-center justify-between gap-4 mb-4 pb-3 border-b border-pink-900/40">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-pink-500/20 border border-pink-500/40 flex items-center justify-center text-pink-300 font-serif font-extrabold text-lg shadow-inner">
            {sms.id}
          </div>
          <span className="text-xs sm:text-sm font-bold tracking-wider text-pink-300 uppercase">
            {t.smsLabel} #{sms.id}
          </span>
        </div>

        <MessageCircleHeart className="w-5 h-5 text-pink-400 opacity-80" />
      </div>

      {/* SMS Text Content with Lip-Sync Karaoke Highlight */}
      <div className={`my-4 p-5 rounded-xl text-base sm:text-lg font-serif leading-relaxed italic shadow-inner transition-all duration-300 ${
        isPlaying
          ? 'bg-gradient-to-r from-pink-950/90 via-purple-900/90 to-pink-950/90 text-amber-200 border-2 border-amber-400 ring-4 ring-amber-400/30 scale-[1.02] shadow-2xl'
          : 'bg-[#14020a]/80 border border-pink-950/60 text-pink-100'
      }`}>
        {smsText}
      </div>

      {/* Action Buttons: Audio Speech & Copy */}
      <div className="flex items-center justify-between pt-2 gap-3 flex-wrap">
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
              <span>Écouter le SMS</span>
            </>
          )}
        </button>

        <button
          onClick={handleCopy}
          className={`px-5 py-2 rounded-full font-semibold text-xs sm:text-sm transition flex items-center gap-2 shadow-lg cursor-pointer ${
            copied
              ? 'bg-emerald-600 text-white shadow-emerald-600/30'
              : 'bg-pink-600 hover:bg-pink-500 text-white shadow-pink-600/30 hover:scale-105'
          }`}
        >
          {copied ? (
            <>
              <Check className="w-4 h-4" />
              <span>{t.copiedBtn}</span>
            </>
          ) : (
            <>
              <Copy className="w-4 h-4" />
              <span>{t.copyBtn}</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
};
