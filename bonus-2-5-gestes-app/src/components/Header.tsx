import React, { useState, useRef, useEffect } from 'react';
import { Language, LANGUAGE_OPTIONS, UI_TRANSLATIONS } from '../data/gestesData';
import { Globe, ChevronDown, Sparkles } from 'lucide-react';

interface HeaderProps {
  currentLanguage: Language;
  onLanguageChange: (lang: Language) => void;
}

export const Header: React.FC<HeaderProps> = ({
  currentLanguage,
  onLanguageChange
}) => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const t = UI_TRANSLATIONS[currentLanguage] || UI_TRANSLATIONS.fr;
  const currentLangObj = LANGUAGE_OPTIONS.find((l) => l.code === currentLanguage) || LANGUAGE_OPTIONS[0];

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setIsDropdownOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  return (
    <header className="sticky top-0 z-50 bg-[#1e0712]/95 backdrop-blur-md border-b border-pink-900/40 text-white px-4 py-3 flex flex-wrap items-center justify-between gap-3 shadow-2xl">
      {/* Brand & Title */}
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-pink-500 to-purple-600 flex items-center justify-center font-bold text-white shadow-md shadow-pink-500/30 border border-white/20 shrink-0">
          LR
        </div>
        <div>
          <h1 className="font-serif-title text-base sm:text-lg font-bold tracking-tight text-white leading-tight flex items-center gap-2">
            <span>{t.title}</span>
            <span className="text-xs px-2 py-0.5 rounded-full bg-pink-500/20 text-pink-300 border border-pink-500/40 font-semibold hidden sm:inline-flex items-center gap-1">
              <Sparkles className="w-3 h-3 text-pink-400" />
              {t.valueBadge}
            </span>
          </h1>
          <p className="text-xs text-pink-300 font-medium">{t.authorBy} — {t.subtitle}</p>
        </div>
      </div>

      {/* Language Selector Dropdown */}
      <div className="relative" ref={dropdownRef}>
        <button
          onClick={() => setIsDropdownOpen(!isDropdownOpen)}
          className="flex items-center gap-2.5 bg-[#2b0816] hover:bg-[#3d0b20] text-white px-4 py-2 rounded-full border border-pink-500/50 shadow-md transition font-semibold text-xs sm:text-sm tracking-wide cursor-pointer"
        >
          <Globe className="w-4 h-4 text-pink-400 shrink-0" />
          <span className="font-bold tracking-wider">
            {currentLangObj.prefix} {currentLangObj.label} ({currentLangObj.shortCode})
          </span>
          <ChevronDown className={`w-4 h-4 text-pink-300 transition-transform duration-200 ${isDropdownOpen ? 'rotate-180' : ''}`} />
        </button>

        {isDropdownOpen && (
          <div className="absolute right-0 mt-2 w-60 bg-[#1f0611] border-2 border-pink-500/60 rounded-2xl shadow-2xl overflow-hidden z-50 py-1 text-white font-sans">
            {LANGUAGE_OPTIONS.map((lang) => {
              const isSelected = lang.code === currentLanguage;
              return (
                <button
                  key={lang.code}
                  onClick={() => {
                    onLanguageChange(lang.code);
                    setIsDropdownOpen(false);
                  }}
                  className={`w-full text-left px-4 py-2.5 text-sm font-bold flex items-center gap-2 transition cursor-pointer ${
                    isSelected
                      ? 'bg-zinc-600/70 text-white font-extrabold'
                      : 'hover:bg-pink-900/40 text-zinc-200 hover:text-white'
                  }`}
                >
                  <span className="text-pink-400 font-extrabold text-xs tracking-widest">{lang.prefix}</span>
                  <span>{lang.label} ({lang.shortCode})</span>
                </button>
              );
            })}
          </div>
        )}
      </div>
    </header>
  );
};
