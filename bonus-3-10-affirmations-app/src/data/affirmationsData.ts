export type Language = 'fr' | 'en' | 'es' | 'de' | 'it' | 'pt' | 'nl' | 'ru' | 'tr' | 'ar';

export interface AffirmationItem {
  id: number;
  text: Record<Language, string>;
}

export const AUTHOR_NAME = "Lina Rela";

export interface LangOption {
  code: Language;
  prefix: string;
  label: string;
  shortCode: string;
  isRtl?: boolean;
}

export const LANGUAGE_OPTIONS: LangOption[] = [
  { code: 'fr', prefix: 'FR', label: 'Français', shortCode: 'FR' },
  { code: 'en', prefix: 'GB', label: 'English', shortCode: 'EN' },
  { code: 'es', prefix: 'ES', label: 'Español', shortCode: 'ES' },
  { code: 'de', prefix: 'DE', label: 'Deutsch', shortCode: 'DE' },
  { code: 'it', prefix: 'IT', label: 'Italiano', shortCode: 'IT' },
  { code: 'pt', prefix: 'PT', label: 'Português', shortCode: 'PT' },
  { code: 'nl', prefix: 'NL', label: 'Nederlands', shortCode: 'NL' },
  { code: 'ru', prefix: 'RU', label: 'Русский', shortCode: 'RU' },
  { code: 'tr', prefix: 'TR', label: 'Türkçe', shortCode: 'TR' },
  { code: 'ar', prefix: 'SA', label: 'العربية', shortCode: 'AR', isRtl: true }
];

export const UI_TRANSLATIONS: Record<Language, {
  title: string;
  subtitle: string;
  valueBadge: string;
  intro: string;
  repeatBtn: string;
  copyBtn: string;
  copiedBtn: string;
  authorBy: string;
  affLabel: string;
}> = {
  "fr": {
    "title": "Bonus 3 : 10 Affirmations puissantes",
    "subtitle": "Confiance & Aura Féminine",
    "valueBadge": "Valeur 37 €",
    "intro": "Un rituel quotidien pour renforcer ta confiance, ton énergie et ton aura féminine afin que tu rayonnes naturellement sans avoir besoin d’en faire trop. Lis ces affirmations chaque matin, avec intention et bienveillance. Respire profondément et ressens chaque mot comme une vérité déjà présente en toi.",
    "repeatBtn": "Répéter l'affirmation",
    "copyBtn": "Copier l'affirmation",
    "copiedBtn": "Copié !",
    "authorBy": "Par Lina Rela",
    "affLabel": "Affirmation"
  },
  "en": {
    "title": "Bonus 3: 10 Powerful Affirmations",
    "subtitle": "Confidence & Feminine Aura",
    "valueBadge": "Value €37",
    "intro": "A daily ritual to strengthen your confidence, energy, and feminine aura so that you radiate naturally. Read these affirmations each morning with intention and kindness. Take a deep breath and feel each word as a truth within you.",
    "repeatBtn": "Repeat Affirmation",
    "copyBtn": "Copy Affirmation",
    "copiedBtn": "Copied!",
    "authorBy": "By Lina Rela",
    "affLabel": "Affirmation"
  },
  "es": {
    "title": "Bonus 3: 10 Afirmaciones Poderosas",
    "subtitle": "Confianza y Aura Femenina",
    "valueBadge": "Valor 37 €",
    "intro": "Un ritual diario para fortalecer tu confianza, tu energía y tu aura femenina para que brilles naturalmente. Lee estas afirmaciones cada mañana con intención y amor.",
    "repeatBtn": "Repetir afirmación",
    "copyBtn": "Copiar afirmación",
    "copiedBtn": "¡Copiado!",
    "authorBy": "Por Lina Rela",
    "affLabel": "Afirmación"
  },
  "de": {
    "title": "Bonus 3: 10 Kraftvolle Affirmationen",
    "subtitle": "Selbstbewusstsein & Weibliche Ausstrahlung",
    "valueBadge": "Wert 37 €",
    "intro": "Ein tägliches Ritual, um dein Selbstvertrauen und deine weibliche Aura zu stärken, sodass du ganz natürlich strahlst. Lies diese Affirmationen jeden Morgen voller Intention.",
    "repeatBtn": "Wiederholen",
    "copyBtn": "Kopieren",
    "copiedBtn": "Kopiert!",
    "authorBy": "Von Lina Rela",
    "affLabel": "Affirmation"
  },
  "it": {
    "title": "Bonus 3: 10 Affermazioni Potenti",
    "subtitle": "Fiducia e Aura Femminile",
    "valueBadge": "Valore 37 €",
    "intro": "Un rituale quotidiano per rafforzare la tua fiducia, la tua energia e la tua aura femminile per risplendere naturalmente.",
    "repeatBtn": "Ripeti affermazione",
    "copyBtn": "Copia affermazione",
    "copiedBtn": "Copiato!",
    "authorBy": "Di Lina Rela",
    "affLabel": "Affermazione"
  },
  "pt": {
    "title": "Bónus 3: 10 Afirmações Poderosas",
    "subtitle": "Confiança e Aura Feminina",
    "valueBadge": "Valor 37 €",
    "intro": "Um ritual diário para fortalecer a sua confiança, energia e aura feminina para irradiar naturalmente. Leia estas afirmações todas as manhãs com intenção.",
    "repeatBtn": "Repetir afirmação",
    "copyBtn": "Copiar afirmação",
    "copiedBtn": "Copiado!",
    "authorBy": "Por Lina Rela",
    "affLabel": "Afirmação"
  },
  "nl": {
    "title": "Bonus 3: 10 Krachtige Affirmaties",
    "subtitle": "Zelfvertrouwen & Vrouwelijke Aura",
    "valueBadge": "Waarde €37",
    "intro": "Een dagelijks ritueel om je zelfvertrouwen en vrouwelijke uitstraling te versterken zodat je natuurlijk straalt.",
    "repeatBtn": "Herhaal affirmatie",
    "copyBtn": "Kopieer affirmatie",
    "copiedBtn": "Gekopieerd!",
    "authorBy": "Door Lina Rela",
    "affLabel": "Affirmatie"
  },
  "ru": {
    "title": "Бонус 3: 10 Мощных Аффирмаций",
    "subtitle": "Уверенность и Женская Аура",
    "valueBadge": "Ценность 37 €",
    "intro": "Ежедневный ритуал для укрепления уверенности и женской ауры, чтобы излучать свет совершенно естественно. Читайте эти аффирмации каждое утро.",
    "repeatBtn": "Повторить аффирмацию",
    "copyBtn": "Копировать",
    "copiedBtn": "Скопировано!",
    "authorBy": "Лина Рела",
    "affLabel": "Аффирмация"
  },
  "tr": {
    "title": "Bonus 3: 10 Güçlü Olumlama",
    "subtitle": "Özgüven & Dişil Işıltı",
    "valueBadge": "Değer 37 €",
    "intro": "Özgüveninizi ve dişil enerjinizi güçlendirerek doğal bir şekilde ışıldamanızı sağlayacak günlük bir ritüel. Bu olumlamaları her sabah niyetle okuyun.",
    "repeatBtn": "Olumlamayı Tekrarla",
    "copyBtn": "Kopyala",
    "copiedBtn": "Kopyalandı!",
    "authorBy": "Lina Rela Tarafından",
    "affLabel": "Olumlama"
  },
  "ar": {
    "title": "البونص ٣: ١٠ توكيدات قوية للثقة الأنثوية",
    "subtitle": "الثقة والهالة الأنثوية",
    "valueBadge": "القيمة ٣٧ يورو",
    "intro": "طقس يومي لتعزيز ثقتكِ بنفسكِ وطاقتكِ وهالتكِ الأنثوية لِتشرقي بطبيعتكِ دون تكلّف. اقرئي هذه التوكيدات كل صباح بنية وصفاء نية.",
    "repeatBtn": "تكرار التوكيد",
    "copyBtn": "نسخ التوكيد",
    "copiedBtn": "تم النسخ!",
    "authorBy": "بقلم لينا ريلا",
    "affLabel": "توكيد"
  }
};

export const AFFIRMATIONS_DATA: AffirmationItem[] = [
  {
    id: 1,
    text: {
      "fr": "Je suis une femme forte, belle et confiante.",
      "en": "I am a strong, beautiful, and confident woman.",
      "es": "Soy una mujer fuerte, hermosa y segura.",
      "de": "Ich bin eine starke, wunderschöne und selbstbewusste Frau.",
      "it": "Sono una donna forte, bella e sicura di me.",
      "pt": "Sou uma mulher forte, bonita e confiante.",
      "nl": "Ik ben een sterke, schone en zelfverzekerde vrouw.",
      "ru": "Я сильная, красивая и уверенная в себе женщина.",
      "tr": "Ben güçlü, güzel ve özgüvenli bir kadınım.",
      "ar": "أنا امرأة قوية، جميلة، وواثقة من نفسي.",
    }
  },
  {
    id: 2,
    text: {
      "fr": "Je mérite tout l’amour, le succès et le bonheur que la vie m’offre.",
      "en": "I deserve all the love, success, and happiness life offers me.",
      "es": "Merezco todo el amor, el éxito y la felicidad que la vida me ofrece.",
      "de": "Ich verdiene alle Liebe, den Erfolg und das Glück, das das Leben mir schenkt.",
      "it": "Merito tutto l'amore, il successo e la felicità che la vita mi offre.",
      "pt": "Mereco todo o amor, sucesso e felicidade que a vida me oferece.",
      "nl": "Ik verdien alle liefde, succes en geluk die het leven mij biedt.",
      "ru": "Я заслуживаю всей любви, успеха и счастья, которые мне дарит жизнь.",
      "tr": "Hayatın bana sunduğu tüm sevgiyi, başarıyı ve mutluluğu hak ediyorum.",
      "ar": "أنا أستحق كل الحب والنجاح والسعادة التي تقدمها لي الحياة.",
    }
  },
  {
    id: 3,
    text: {
      "fr": "Mon énergie féminine est puissante et magnétique.",
      "en": "My feminine energy is powerful and magnetic.",
      "es": "Mi energía femenina es poderosa y magnética.",
      "de": "Meine weibliche Energie ist kraftvoll und magnetisch.",
      "it": "La mia energia femminile è potente e magnetica.",
      "pt": "A minha energia feminina é poderosa e magnética.",
      "nl": "Mijn vrouwelijke energie is krachtig en magnetisch.",
      "ru": "Моя женская энергия сильна и магнетична.",
      "tr": "Dişil enerjim güçlü ve büyüleyicidir.",
      "ar": "طاقتي الأنثوية قوية ومغناطيسية تجذب الخیر.",
    }
  },
  {
    id: 4,
    text: {
      "fr": "Je choisis chaque jour de briller sans crainte ni comparaison.",
      "en": "I choose each day to shine without fear or comparison.",
      "es": "Elijo cada día brillar sin miedo ni comparación.",
      "de": "Ich entscheide mich jeden Tag zu strahlen, ohne Furcht oder Vergleich.",
      "it": "Scegli di risplendere ogni giorno senza paura né confronti.",
      "pt": "Escolho todos os dias brilhar sem medo nem comparações.",
      "nl": "Ik kies er elke dag voor om te stralen zonder angst of vergelijking.",
      "ru": "Я каждый день выбираю сиять без страха и сравнений.",
      "tr": "Her день korkmadan ve kıyaslamadan parlamayı seçiyorum.",
      "ar": "أنا أختار كل يوم أن أشرق دون خوف أو مقارنة مع أحد.",
    }
  },
  {
    id: 5,
    text: {
      "fr": "Je suis en paix avec mon corps, mon cœur et mon esprit.",
      "en": "I am at peace with my body, my heart, and my mind.",
      "es": "Estoy en paz con mi cuerpo, mi corazón y mi mente.",
      "de": "Ich bin im Frieden mit meinem Körper, meinem Herzen und meinem Geist.",
      "it": "Sono in pace con il mio corpo, il mio cuore e la mia mente.",
      "pt": "Estou em paz com o meu corpo, o meu coração e a minha mente.",
      "nl": "Ik ben in vrede met mijn lichaam, mijn hart en mijn geest.",
      "ru": "Я в мире со своим телом, сердцем и разумом.",
      "tr": "Bedenimle, kalbimle ve zihnimle barış içindeyim.",
      "ar": "أنا في سلام تام مع جسدي، وقلبي، وعقلي.",
    }
  },
  {
    id: 6,
    text: {
      "fr": "Ma confiance inspire le respect et l’admiration autour de moi.",
      "en": "My confidence inspires respect and admiration around me.",
      "es": "Mi confianza inspira respeto y admiración a mi alrededor.",
      "de": "Mein Selbstvertrauen inspiriert Respekt und Bewunderung um mich herum.",
      "it": "La mia fiducia ispira rispetto e ammirazione intorno a me.",
      "pt": "A minha confiança inspira respeito e admiração ao meu redor.",
      "nl": "Mijn zelfvertrouwen inspireert respect en bewondering om mij heen.",
      "ru": "Моя уверенность внушает уважение и восхищение окружающим.",
      "tr": "Özgüvenim çevremde saygı ve hayranlık uyandırır.",
      "ar": "ثقتي بنفسي تلهم الاحترام والإعجاب من حولي.",
    }
  },
  {
    id: 7,
    text: {
      "fr": "Je suis capable d’accomplir tout ce que je désire.",
      "en": "I am capable of achieving everything I desire.",
      "es": "Soy capaz de lograr todo lo que deseo.",
      "de": "Ich bin fähig, alles zu erreichen, was ich mir wünsche.",
      "it": "Sono capace di realizzare tutto ciò che desidero.",
      "pt": "Sou capaz de alcançar tudo o que desejo.",
      "nl": "Ik ben in staat om alles te bereiken wat ik verlang.",
      "ru": "Я способна достичь всего, чего пожелаю.",
      "tr": "Arzuladığım her şeyi başarma gücüne sahibim.",
      "ar": "أنا قادرة على تحقيق كل ما أتطلع إليه برغبة واقتدار.",
    }
  },
  {
    id: 8,
    text: {
      "fr": "Je rayonne de douceur, de force et de sérénité.",
      "en": "I radiate softness, strength, and serenity.",
      "es": "Irradio dulzura, fuerza y serenidad.",
      "de": "Ich strahle Sanftheit, Stärke und Gelassenheit aus.",
      "it": "Rad io dolcezza, forza e serenità.",
      "pt": "Irradio doçura, força e serenidade.",
      "nl": "Ik straal zachtheid, kracht en kalmte uit.",
      "ru": "Я излучаю нежность, силу и умиротворение.",
      "tr": "Zarafet, güç ve huzur saçıyorum.",
      "ar": "أنا أفيض رقة، وقوة، وسكينة.",
    }
  },
  {
    id: 9,
    text: {
      "fr": "Chaque jour, je m’élève davantage dans ma puissance féminine.",
      "en": "Every day, I rise higher into my feminine power.",
      "es": "Cada día, me elevo más en mi poder femenino.",
      "de": "Jeden Tag wachse ich weiter in meine weibliche Kraft hinein.",
      "it": "Ogni giorno mi elevo sempre più nella mia potenza femminile.",
      "pt": "Todos os dias, me elevo mais no meu poder feminino.",
      "nl": "Elke dag stijg ik verder in mijn vrouwelijke kracht.",
      "ru": "Каждый день я поднимаюсь всё выше в своей женской силе.",
      "tr": "Her gün dişil gücümde daha da yükseliyorum.",
      "ar": "كل يوم يرتقي وعيي وتزداد قوتي الأنثوية نضجاً.",
    }
  },
  {
    id: 10,
    text: {
      "fr": "Je suis déjà celle que je rêve de devenir.",
      "en": "I am already the woman I dream of becoming.",
      "es": "Ya soy la persona que sueño con llegar a ser.",
      "de": "Ich bin bereits die Frau, die ich zu werden träume.",
      "it": "Sono già la donna che sogno di diventare.",
      "pt": "Já sou a mulher que sonho tornar-me.",
      "nl": "Ik ben al de vrouw die ik droom te worden.",
      "ru": "Я уже та женщина, которой мечтаю стать.",
      "tr": "Zaten olmak istediğim o kadınım.",
      "ar": "أنا بالفعل المرأة التي أحلم بأن أكونها.",
    }
  },
];

export const AFFIRMATIONS = AFFIRMATIONS_DATA;
