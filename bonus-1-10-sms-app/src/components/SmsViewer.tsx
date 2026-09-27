import React, { useState } from 'react';
import { SMS_DATA, Language, LANGUAGE_OPTIONS, UI_TRANSLATIONS } from '../data/smsData';
import { Header } from './Header';
import { SmsCard } from './SmsCard';
import { Sparkles, Heart, Lightbulb, ArrowUp } from 'lucide-react';

export const SmsViewer: React.FC = () => {
  const [currentLanguage, setCurrentLanguage] = useState<Language>('fr');
  const [showScrollTop, setShowScrollTop] = useState(false);

  const t = UI_TRANSLATIONS[currentLanguage] || UI_TRANSLATIONS.fr;
  const currentLangObj = LANGUAGE_OPTIONS.find((l) => l.code === currentLanguage);
  const isRtl = Boolean(currentLangObj?.isRtl);

  React.useEffect(() => {
    const handleScroll = () => {
      setShowScrollTop(window.scrollY > 300);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div dir={isRtl ? 'rtl' : 'ltr'} className="min-h-screen bg-zinc-950 text-zinc-100 flex flex-col font-body selection:bg-pink-500 selection:text-white">
      {/* Top Header */}
      <Header
        currentLanguage={currentLanguage}
        onLanguageChange={setCurrentLanguage}
      />

      {/* Main Container */}
      <main className="flex-1 py-8 px-4 max-w-4xl mx-auto w-full flex flex-col items-center">
        {/* Hero Header Card */}
        <div className="w-full bg-gradient-to-br from-purple-900/40 via-pink-900/40 to-purple-950/60 border-2 border-pink-500/40 rounded-3xl p-6 sm:p-10 mb-8 text-center relative overflow-hidden shadow-2xl">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-pink-500/20 text-pink-300 border border-pink-500/40 font-bold text-xs sm:text-sm tracking-wider uppercase mb-4">
            <Sparkles className="w-4 h-4 text-pink-400" />
            {t.valueBadge}
          </div>

          <h1 className="font-serif-title text-3xl sm:text-5xl font-extrabold text-white leading-tight mb-4 tracking-tight drop-shadow-md">
            {t.title}
          </h1>

          <p className="font-serif text-lg sm:text-xl text-pink-200 font-medium mb-6">
            {t.subtitle}
          </p>

          <div className="w-24 h-1 bg-gradient-to-r from-transparent via-pink-500 to-transparent mx-auto mb-6" />

          <p className="text-sm sm:text-base text-zinc-300 max-w-2xl mx-auto leading-relaxed font-normal">
            {t.intro}
          </p>

          <div className="mt-6 inline-flex items-center gap-2 text-xs font-semibold text-pink-400">
            <Heart className="w-4 h-4 fill-pink-500 text-pink-500" />
            <span>{t.authorBy}</span>
          </div>
        </div>

        {/* 10 SMS Cards Stack (Continuous Scroll) */}
        <div className="w-full flex flex-col gap-6">
          {SMS_DATA.map((sms) => (
            <SmsCard key={sms.id} sms={sms} language={currentLanguage} />
          ))}
        </div>

        {/* Pro Tip Section */}
        <div className="mt-10 w-full bg-gradient-to-r from-amber-950/40 via-pink-950/50 to-purple-950/40 border border-amber-500/40 rounded-2xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
          <div className="flex items-start gap-4">
            <div className="p-3 rounded-2xl bg-amber-500/20 border border-amber-500/40 text-amber-300 shrink-0">
              <Lightbulb className="w-6 h-6 text-amber-400" />
            </div>
            <div>
              <h3 className="font-serif-title text-xl font-bold text-amber-200 mb-2 flex items-center gap-2">
                {t.tipTitle}
              </h3>
              <p className="text-sm sm:text-base text-zinc-200 leading-relaxed font-normal">
                {t.tipText}
              </p>
            </div>
          </div>
        </div>
      </main>

      {/* Floating Scroll to Top */}
      {showScrollTop && (
        <button
          onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
          className="fixed bottom-6 right-6 z-50 p-3 rounded-full bg-pink-600 hover:bg-pink-500 text-white shadow-2xl transition-all duration-300 transform hover:scale-110 border border-pink-400/40 cursor-pointer"
          title="Retour en haut"
        >
          <ArrowUp className="w-6 h-6" />
        </button>
      )}

      {/* Footer */}
      <footer className="py-6 border-t border-zinc-900 text-center text-xs text-zinc-500 mt-12">
        <p>{t.title} — {t.subtitle} © {new Date().getFullYear()} Lina Rela</p>
      </footer>
    </div>
  );
};
