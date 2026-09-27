import React, { useState } from 'react';
import { AFFIRMATIONS, Language, UI_TRANSLATIONS } from '../data/affirmationsData';
import { AffirmationCard } from './AffirmationCard';
import { ChevronLeft, ChevronRight, Sparkles, BookOpen, Quote } from 'lucide-react';

interface AffirmationViewerProps {
  currentLang: Language;
  isContinuous: boolean;
}

export const AffirmationViewer: React.FC<AffirmationViewerProps> = ({
  currentLang,
  isContinuous
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const ui = UI_TRANSLATIONS[currentLang];
  const isRtl = currentLang === 'ar';

  const handleNext = () => {
    setCurrentIndex((prev) => (prev + 1) % AFFIRMATIONS.length);
  };

  const handlePrev = () => {
    setCurrentIndex((prev) => (prev - 1 + AFFIRMATIONS.length) % AFFIRMATIONS.length);
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8" dir={isRtl ? 'rtl' : 'ltr'}>
      {/* Intro Box */}
      <div className="mb-10 bg-gradient-to-r from-rose-950/40 via-stone-900 to-amber-950/40 border border-rose-900/40 rounded-2xl p-6 md:p-8 shadow-2xl relative overflow-hidden">
        <div className="absolute top-0 right-0 p-8 opacity-5">
          <Quote className="w-32 h-32 text-amber-200" />
        </div>
        
        <div className="relative z-10 flex flex-col md:flex-row items-center gap-6">
          <div className="w-16 h-16 rounded-full bg-gradient-to-tr from-rose-500 to-amber-400 p-0.5 shadow-lg flex-shrink-0 flex items-center justify-center">
            <div className="w-full h-full bg-stone-950 rounded-full flex items-center justify-center">
              <Sparkles className="w-8 h-8 text-amber-300" />
            </div>
          </div>

          <div className="text-stone-200 text-sm md:text-base leading-relaxed space-y-2">
            <p className="font-serif italic text-stone-200 text-base md:text-lg">
              "{ui.intro}"
            </p>
          </div>
        </div>
      </div>

      {/* Main Content Area */}
      {isContinuous ? (
        /* Continuous Vertical Scroll Mode */
        <div className="space-y-6">
          <div className="flex items-center justify-between border-b border-rose-900/30 pb-3 mb-6">
            <h2 className="text-sm font-semibold tracking-wider text-rose-400 uppercase flex items-center gap-2">
              <BookOpen className="w-4 h-4 text-amber-400" />
              <span>Toutes les 10 Affirmations</span>
            </h2>
            <span className="text-xs text-stone-400">10 sur 10</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {AFFIRMATIONS.map((item, idx) => (
              <AffirmationCard
                key={item.id}
                item={item}
                currentLang={currentLang}
                index={idx}
              />
            ))}
          </div>
        </div>
      ) : (
        /* Single Card Carousel / Paginated Mode */
        <div className="space-y-6">
          {/* Card Component */}
          <div className="transition-all duration-300 transform">
            <AffirmationCard
              item={AFFIRMATIONS[currentIndex]}
              currentLang={currentLang}
              index={currentIndex}
            />
          </div>

          {/* Navigation Controls */}
          <div className="flex items-center justify-between pt-4">
            <button
              onClick={handlePrev}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-stone-800 hover:bg-stone-700 text-stone-200 border border-stone-700 hover:border-rose-500/50 transition font-medium text-xs md:text-sm shadow-md"
            >
              <ChevronLeft className="w-4 h-4 text-rose-400" />
              <span>Précédent</span>
            </button>

            {/* Dots */}
            <div className="flex items-center gap-1.5 overflow-x-auto max-w-[200px] sm:max-w-none px-2 py-1">
              {AFFIRMATIONS.map((_, idx) => (
                <button
                  key={idx}
                  onClick={() => setCurrentIndex(idx)}
                  className={`w-2.5 h-2.5 rounded-full transition-all ${
                    idx === currentIndex
                      ? 'w-7 bg-amber-400 shadow-md shadow-amber-400/30'
                      : 'bg-stone-700 hover:bg-stone-500'
                  }`}
                  aria-label={`Aller à l'affirmation ${idx + 1}`}
                />
              ))}
            </div>

            <button
              onClick={handleNext}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-stone-800 hover:bg-stone-700 text-stone-200 border border-stone-700 hover:border-rose-500/50 transition font-medium text-xs md:text-sm shadow-md"
            >
              <span>Suivant</span>
              <ChevronRight className="w-4 h-4 text-rose-400" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
