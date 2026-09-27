import React, { useState } from 'react';
import { Language } from './data/affirmationsData';
import { Header } from './components/Header';
import { AffirmationViewer } from './components/AffirmationViewer';
import { Sparkles, Heart } from 'lucide-react';

export const App: React.FC = () => {
  const [currentLang, setCurrentLang] = useState<Language>('fr');
  const [isContinuous, setIsContinuous] = useState<boolean>(true); // Default to scroll mode as requested

  return (
    <div className="min-h-screen bg-stone-950 text-stone-100 flex flex-col font-sans selection:bg-rose-900 selection:text-rose-100">
      <Header
        currentLang={currentLang}
        onLangChange={setCurrentLang}
        isContinuous={isContinuous}
        onToggleContinuous={() => setIsContinuous(!isContinuous)}
      />

      <main className="flex-1">
        <AffirmationViewer
          currentLang={currentLang}
          isContinuous={isContinuous}
        />
      </main>

      <footer className="border-t border-rose-950/60 bg-stone-900/60 py-6 px-4 text-center text-xs text-stone-400">
        <div className="max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
          <p className="flex items-center gap-1">
            <span>Bonus 3 : 10 Affirmations puissantes de confiance féminine</span>
            <Sparkles className="w-3.5 h-3.5 text-amber-400 inline" />
          </p>
          <p className="flex items-center gap-1 text-stone-300 font-serif">
            <span>Auteur :</span>
            <strong className="text-amber-300">Lina Rela</strong>
          </p>
        </div>
      </footer>
    </div>
  );
};

export default App;
