import React from 'react';
import { Language, LANGUAGE_OPTIONS, UI_TRANSLATIONS, AUTHOR_NAME } from '../data/affirmationsData';
import { Globe, Sparkles, ScrollText, Layers, ChevronDown } from 'lucide-react';

interface HeaderProps {
  currentLang: Language;
  onLangChange: (lang: Language) => void;
  isContinuous: boolean;
  onToggleContinuous: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  currentLang,
  onLangChange,
  isContinuous,
  onToggleContinuous
}) => {
  const ui = UI_TRANSLATIONS[currentLang];
  const activeOpt = LANGUAGE_OPTIONS.find(l => l.code === currentLang) || LANGUAGE_OPTIONS[0];

  return (
    <header className="sticky top-0 z-50 bg-stone-900/90 backdrop-blur-md border-b border-rose-900/30 px-4 py-3 shadow-xl">
      <div className="max-w-4xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        {/* Title & Author */}
        <div className="flex items-center gap-3 text-center md:text-left">
          <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-rose-500 to-amber-400 p-0.5 shadow-lg shadow-rose-500/20 flex-shrink-0">
            <div className="w-full h-full bg-stone-950 rounded-full flex items-center justify-center">
              <Sparkles className="w-5 h-5 text-amber-300 animate-pulse" />
            </div>
          </div>
          <div>
            <div className="flex items-center gap-2 justify-center md:justify-start">
              <span className="text-xs font-semibold tracking-wider text-rose-400 uppercase bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40">
                {ui.title}
              </span>
              <span className="text-xs font-semibold text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-700/40">
                {ui.valueBadge}
              </span>
            </div>
            <h1 className="text-lg md:text-xl font-serif font-bold text-stone-100 tracking-wide mt-0.5">
              {ui.subtitle}
            </h1>
            <p className="text-xs text-rose-300/80 font-medium">
              {ui.authorBy}
            </p>
          </div>
        </div>

        {/* Controls: Navigation, Mode Switch & Language Selector */}
        <div className="flex items-center gap-2 flex-wrap justify-center">
          {/* Main eBook / Bonus Quick Nav */}
          <div className="relative group">
            <button className="flex items-center gap-1 px-3 py-1.5 text-xs font-semibold rounded-lg bg-rose-950/80 text-rose-200 border border-rose-800/60 hover:bg-rose-900 transition">
              <span>📖 Navigation</span>
              <ChevronDown className="w-3.5 h-3.5" />
            </button>
            <div className="absolute right-0 mt-2 w-52 bg-stone-900 border border-rose-800/60 rounded-xl shadow-2xl p-2 hidden group-hover:block z-50">
              <a href="../" className="flex items-center justify-between p-2 rounded-lg hover:bg-stone-800 text-xs font-semibold text-stone-200 transition">
                <span>📖 eBook Principal</span>
                <span>→</span>
              </a>
              <a href="../bonus1/" className="flex items-center justify-between p-2 rounded-lg hover:bg-stone-800 text-xs font-semibold text-pink-300 transition">
                <span>Bonus 1 : 10 SMS</span>
                <span>→</span>
              </a>
              <a href="../bonus2/" className="flex items-center justify-between p-2 rounded-lg hover:bg-stone-800 text-xs font-semibold text-amber-300 transition">
                <span>Bonus 2 : 5 Gestes</span>
                <span>→</span>
              </a>
              <a href="../bonus3/" className="flex items-center justify-between p-2 rounded-lg hover:bg-stone-800 text-xs font-semibold text-rose-400 bg-rose-950/50 transition">
                <span>Bonus 3 : 10 Affirmations</span>
                <span>✓</span>
              </a>
            </div>
          </div>

          {/* Toggle View Mode */}
          <button
            onClick={onToggleContinuous}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-lg bg-stone-800/80 text-stone-200 border border-stone-700 hover:border-rose-500/50 hover:bg-stone-800 transition"
            title="Basculer le mode de vue"
          >
            {isContinuous ? (
              <>
                <Layers className="w-3.5 h-3.5 text-rose-400" />
                <span>Mode Cartes</span>
              </>
            ) : (
              <>
                <ScrollText className="w-3.5 h-3.5 text-amber-400" />
                <span>Mode Défilement</span>
              </>
            )}
          </button>

          {/* Language Selector Dropdown */}
          <div className="relative group">
            <div className="flex items-center gap-1.5 px-3 py-1.5 bg-stone-800/80 rounded-lg border border-rose-900/40 text-stone-200 text-xs font-medium cursor-pointer hover:bg-stone-800 transition">
              <Globe className="w-3.5 h-3.5 text-rose-400" />
              <span className="font-bold text-amber-300">{activeOpt.prefix}</span>
              <span className="hidden sm:inline text-stone-300">({activeOpt.label})</span>
            </div>

            <select
              value={currentLang}
              onChange={(e) => onLangChange(e.target.value as Language)}
              className="absolute inset-0 opacity-0 cursor-pointer w-full h-full"
            >
              {LANGUAGE_OPTIONS.map((opt) => (
                <option key={opt.code} value={opt.code} className="bg-stone-900 text-stone-200">
                  {opt.prefix} - {opt.label}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>
    </header>
  );
};
