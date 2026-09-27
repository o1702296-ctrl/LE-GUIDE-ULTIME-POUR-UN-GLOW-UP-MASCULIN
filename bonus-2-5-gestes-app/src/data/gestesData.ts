export type Language = 'fr' | 'en' | 'es' | 'de' | 'it' | 'pt' | 'nl' | 'ru' | 'tr' | 'ar';

export interface GesteItem {
  id: number;
  title: Record<Language, string>;
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
  authorBy: string;
  gesteLabel: string;
}> = {
  "fr": {
    "title": "Bonus 2 : Le guide express",
    "subtitle": "Les 5 gestes qui rendent une femme inoubliable",
    "valueBadge": "Valeur 19 €",
    "intro": "Apprends à captiver ton homme sans mots : ces gestes subtils mais puissants déclenchent instantanément l’attirance, le respect et l’envie chez lui. Ces gestes ne sont pas seulement physiques, ils traduisent ton assurance, ton mystère et ta féminité intérieure. Découvre-les et incarne-les au quotidien pour devenir une femme qui marque les esprits.",
    "authorBy": "Par Lina Rela",
    "gesteLabel": "Geste"
  },
  "en": {
    "title": "Bonus 2: The Express Guide",
    "subtitle": "The 5 gestures that make a woman unforgettable",
    "valueBadge": "Value €19",
    "intro": "Learn to captivate your man without words: these subtle yet powerful gestures instantly spark attraction, respect, and desire in him. These gestures express your confidence, mystery, and inner femininity.",
    "authorBy": "By Lina Rela",
    "gesteLabel": "Gesture"
  },
  "es": {
    "title": "Bonus 2: La Guía Exprés",
    "subtitle": "Los 5 gestos que hacen a una mujer inolvidable",
    "valueBadge": "Valor 19 €",
    "intro": "Aprende a cautivar a tu hombre sin palabras: estos gestos sutiles pero poderosos despiertan instantáneamente la atracción, el respeto y el deseo en él.",
    "authorBy": "Por Lina Rela",
    "gesteLabel": "Gesto"
  },
  "de": {
    "title": "Bonus 2: Der Express-Ratgeber",
    "subtitle": "Die 5 Gesten, die eine Frau unvergesslich machen",
    "valueBadge": "Wert 19 €",
    "intro": "Lerne, deinen Mann ohne Worte zu fesseln: Diese subtilen, aber kraftvollen Gesten lösen sofort Anziehung, Respekt und Verlangen aus.",
    "authorBy": "Von Lina Rela",
    "gesteLabel": "Geste"
  },
  "it": {
    "title": "Bonus 2: La Guida Express",
    "subtitle": "I 5 gesti che rendono una donna indimenticabile",
    "valueBadge": "Valore 19 €",
    "intro": "Impara a catturare il tuo uomo senza parole: questi gesti sottili ma potenti innescano all'istante l'attrazione, il rispetto e il desiderio.",
    "authorBy": "Di Lina Rela",
    "gesteLabel": "Gesto"
  },
  "pt": {
    "title": "Bónus 2: O Guia Expresso",
    "subtitle": "Os 5 gestos que tornam uma mulher inesquecível",
    "valueBadge": "Valor 19 €",
    "intro": "Aprenda a cativar o seu homem sem palavras: estes gestos subtis e poderosos despertam instantaneamente a atração, o respeito e o desejo.",
    "authorBy": "Por Lina Rela",
    "gesteLabel": "Gesto"
  },
  "nl": {
    "title": "Bonus 2: De Express Gids",
    "subtitle": "De 5 gebaren die een vrouw onvergetelijk maken",
    "valueBadge": "Waarde €19",
    "intro": "Leer je man zonder woorden te boeien: deze subtiele maar krachtige gebaren wekken meteen aantrekkingskracht en verlangen op.",
    "authorBy": "Door Lina Rela",
    "gesteLabel": "Gebaar"
  },
  "ru": {
    "title": "Бонус 2: Экспресс-руководство",
    "subtitle": "5 жестов, которые делают женщину незабываемой",
    "valueBadge": "Ценность 19 €",
    "intro": "Научитесь привлекать мужчину без слов: эти утонченные, но мощные жесты мгновенно вызывают влечение, уважение и желание.",
    "authorBy": "Лина Рела",
    "gesteLabel": "Жест"
  },
  "tr": {
    "title": "Bonus 2: Ekspres Rehber",
    "subtitle": "Bir kadını unutulmaz kılan 5 hareket",
    "valueBadge": "Değer 19 €",
    "intro": "Erkeğinizi kelimeler olmadan büyülemeyi öğrenin: Bu zarif ama etkili hareketler onda anında çekim, saygı ve arzu uyandırır.",
    "authorBy": "Lina Rela Tarafından",
    "gesteLabel": "Hareket"
  },
  "ar": {
    "title": "البونص ٢: الدليل السريع",
    "subtitle": "الحركات الخمس التي تجعل المرأة لا تُنسى",
    "valueBadge": "القيمة ١٩ يورو",
    "intro": "تعلمي كيف تسحرين الرجل دون كلمات: هذه الحركات البسيطة والقوية تثير الانجذاب والاحترام والشغف فوراً لديها.",
    "authorBy": "بقلم لينا ريلا",
    "gesteLabel": "الحركة"
  }
};

export const GESTES_DATA: GesteItem[] = [
  {
    id: 1,
    title: {
      "fr": "1. Le regard soutenu et doux",
      "en": "1. The Soft, Sustained Gaze",
      "es": "1. La mirada sostenida y suave",
      "de": "1. Der lange, sanfte Blick",
      "it": "1. Lo sguardo sostenuto e dolce",
      "pt": "1. O olhar sustentado e suave",
      "nl": "1. De zachte, langdurige blik",
      "ru": "1. Пристальный и мягкий взгляд",
      "tr": "1. Yumuşak ve derin bakış",
      "ar": "١. النظرة الهادئة والعميقة",
    },
    text: {
      "fr": "Regarde-le avec calme et intensité. Un regard sincère, légèrement appuyé, crée une connexion émotionnelle profonde.",
      "en": "Look at him with calm and intensity. A sincere, slightly lingered gaze creates a deep emotional connection.",
      "es": "Míralo con calma e intensidad. Una mirada sincera y ligeramente sostenida crea una conexión emocional profunda.",
      "de": "Schau ihn mit Ruhe und Intensität an. Ein aufrichtiger, leicht verweilender Blick schafft eine tiefe emotionale Verbindung.",
      "it": "Guardalo con calma e intensità. Uno sguardo sincero, leggermente prolungato, crea una profonda connessione emotiva.",
      "pt": "Olhe para ele com calma e intensidade. Um olhar sincero e ligeiramente prolongado cria uma conexão emocional profunda.",
      "nl": "Kijk hem rustig en intens aan. Een oprechte blik schept een diepe emotionele band.",
      "ru": "Посмотрите на него с спокойствием и интенсивностью. Искренний взгляд создает глубокую эмоциональную связь.",
      "tr": "Ona sakince ve etkileyici bir şekilde bakın. Samimi bir bakış derin bir duygusal bağ oluşturur.",
      "ar": "انظري إليه بهدوء وتركيز. النظرة الصادقة والعميقة تخلق توازناً وعاطفة عميقة.",
    }
  },
  {
    id: 2,
    title: {
      "fr": "2. Le sourire en coin",
      "en": "2. The Subtle Half-Smile",
      "es": "2. La sonrisa de reojo",
      "de": "2. Das feine Lächeln",
      "it": "2. Il sorriso accennato",
      "pt": "2. O sorriso discreto",
      "nl": "2. De subtiele glimlach",
      "ru": "2. Едва заметная улыбка",
      "tr": "2. Hafif tebessüm",
      "ar": "٢. الابتسامة الخفيفة والمغرية",
    },
    text: {
      "fr": "Un léger sourire, sans tout dévoiler, intrigue et charme. Il laisse place à l’imagination et attise le désir.",
      "en": "A slight smile, without revealing everything, intrigues and charms. It leaves room for imagination and sparks desire.",
      "es": "Una ligera sonrisa, sin revelarlo todo, intriga y encanta. Deja espacio a la imaginación y aviva el deseo.",
      "de": "Ein leichtes Lächeln fasziniert und charmiert. Es lässt Raum für Phantasie und weckt das Begehren.",
      "it": "Un leggero sorriso, senza svelare tutto, intriga e affascina. Lascia spazio all'immaginazione e stuzzica il desiderio.",
      "pt": "Um ligeiro sorriso, sem revelar tudo, intriga e encanta. Dá asas à imaginação e desperta o desejo.",
      "nl": "Een lichte glimlach zonder alles te onthullen intrigeert en charmeert. Het geeft ruimte aan de verbeelding.",
      "ru": "Легкая улыбка интригует и очаровывает. Она оставляет место воображению и разжигает желание.",
      "tr": "Hafif bir tebessüm merak uyandırır ve büyüler. Hayal gücüne yer bırakır ve arzuyu tetikler.",
      "ar": "ابتسامة خفيفة تدعو إلى الفضول والسحر وتفتح المجال للخيال والاشتياق.",
    }
  },
  {
    id: 3,
    title: {
      "fr": "3. Le toucher délicat",
      "en": "3. The Delicate Touch",
      "es": "3. El toque delicado",
      "de": "3. Die zarte Berührung",
      "it": "3. Il tocco delicato",
      "pt": "3. O toque delicado",
      "nl": "3. De zachte aanraking",
      "ru": "3. Деликатное прикосновение",
      "tr": "3. Zarif dokunuş",
      "ar": "٣. اللمسة الرقيقة",
    },
    text: {
      "fr": "Un effleurement subtil sur le bras ou l’épaule déclenche une sensation immédiate de proximité et d’intimité.",
      "en": "A subtle touch on the arm or shoulder triggers an immediate feeling of closeness and intimacy.",
      "es": "Un roce sutil en el brazo o el hombro desencadena una sensación inmediata de cercanía e intimidad.",
      "de": "Eine subtile Berührung am Arm oder an der Schulter löst ein sofortiges Gefühl von Nähe aus.",
      "it": "Un tocco leggero sul braccio o sulla spalla innesca una sensazione immediata di vicinanza e intimità.",
      "pt": "Um toque subtil no braço ou no ombro desperta uma sensação imediata de proximidade e intimidade.",
      "nl": "Een subtiele aanraking van de arm of schouder wekt meteen een gevoel van nabijheid op.",
      "ru": "Легкое прикосновение к руке или плечу вызовет мгновенное ощущение близости.",
      "tr": "Kola veya omuza yapılan küçük bir dokunuş anında bir yakınlık hissi uyandırır.",
      "ar": "لمسة خفيفة على الذراع أو الكتف تثير شعوراً فورياً بالقرابة والألفة.",
    }
  },
  {
    id: 4,
    title: {
      "fr": "4. La posture ouverte et assurée",
      "en": "4. An Open, Confident Posture",
      "es": "4. La postura abierta y segura",
      "de": "4. Eine offene, selbstbewusste Haltung",
      "it": "4. La postura aperta e sicura",
      "pt": "4. A postura aberta e confiante",
      "nl": "4. Een open, zelfverzekerde houding",
      "ru": "4. Открытая и уверенная осанка",
      "tr": "4. Açık ve özgüvenli duruş",
      "ar": "٤. الهيئة الواثقة والمنفتحة",
    },
    text: {
      "fr": "Tiens-toi droite, détendue, avec une présence ancrée. Ta posture parle avant même que tu n’ouvres la bouche.",
      "en": "Stand tall, relaxed, with a grounded presence. Your posture speaks even before you open your mouth.",
      "es": "Mantente erguida, relajada, con una presencia firme. Tu postura habla antes de que abras la boca.",
      "de": "Stehe aufrecht, entspannt und präsent. Deine Haltung spricht, noch bevor du den Mund öffnest.",
      "it": "Tieniti dritta, rilassata, con una presenza salda. La tua postura parla prima ancora che tu apra bocca.",
      "pt": "Mantenha-se ereta, relaxada, com uma presença firme. A sua postura fala antes de abrir a boca.",
      "nl": "Sta recht en ontspannen met een krachtige uitstraling. Je houding spreekt al voordat je wat zegt.",
      "ru": "Держитесь прямо и расслабленно. Ваша осанка говорит сама за себя еще до того, как вы заговорите.",
      "tr": "Dik ve rahat durun. Duruşunuz siz daha konuşmadan önce konuşur.",
      "ar": "قفي بثقة واسترخاء وشموخ. هيئتك تعبر عنكِ قبل أن تنطقي بكلمة واحدة.",
    }
  },
  {
    id: 5,
    title: {
      "fr": "5. Le silence confiant",
      "en": "5. Confident Silence",
      "es": "5. El silencio confiado",
      "de": "5. Das selbstbewusste Schweigen",
      "it": "5. Il silenzio sicuro",
      "pt": "5. O silêncio confiante",
      "nl": "5. De zelfverzekerde stilte",
      "ru": "5. Уверенное молчание",
      "tr": "5. Özgüvenli sessizlik",
      "ar": "٥. الصمت الواثق",
    },
    text: {
      "fr": "Ne cherche pas à combler chaque silence. Un silence assumé montre ton assurance et ton pouvoir intérieur.",
      "en": "Don't try to fill every silence. An owned silence shows your poise and inner strength.",
      "es": "No intentes llenar cada silencio. Un silencio asumido demuestra tu seguridad y poder interior.",
      "de": "Versuche nicht, jede Stille zu füllen. Ein bewusstes Schweigen zeigt deine Stärke.",
      "it": "Non cercare di riempire ogni silenzio. Un silenzio vissuto con naturalezza mostra la tua sicurezza.",
      "pt": "Não tente preencher todos os silêncios. Um silêncio assumido mostra a sua confiança.",
      "nl": "Probeer niet elke stilte op te vullen. Een rustige stilte toont je innerlijke kracht.",
      "ru": "Не пытайтесь заполнить каждую паузу. Уверенное молчание показывает вашу внутреннюю силу.",
      "tr": "Her sessizliği doldurmaya çalışmayın. Kendinden emin bir sessizlik gücünüzü gösterir.",
      "ar": "لا تحاولي ملء كل لحظة صمت. الصمت الهادئ يظهر ثقتكِ وقوتكِ الداخلية.",
    }
  },
];
