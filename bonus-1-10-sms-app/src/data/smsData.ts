export type Language = 'fr' | 'en' | 'es' | 'de' | 'it' | 'pt' | 'nl' | 'ru' | 'tr' | 'ar';

export interface SmsItem {
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
  tipTitle: string;
  tipText: string;
  copyBtn: string;
  copiedBtn: string;
  authorBy: string;
  smsLabel: string;
}> = {
  "fr": {
    "title": "Bonus 1 : 10 SMS irrésistibles",
    "subtitle": "Pour raviver le désir dans ton couple",
    "valueBadge": "Valeur 39 €",
    "intro": "Des messages simples et puissants à lui envoyer pour rallumer la flamme, créer du manque et faire renaître le jeu de séduction, même après plusieurs années de relation.",
    "tipTitle": "Astuce & Conseil Pro",
    "tipText": "Envoie ces messages avec confiance, au bon moment, et surtout sans attente. Le secret, c’est de susciter l’émotion, pas de chercher la validation. Laisse la magie opérer naturellement…",
    "copyBtn": "Copier le SMS",
    "copiedBtn": "SMS Copié !",
    "authorBy": "Par Lina Rela",
    "smsLabel": "SMS"
  },
  "en": {
    "title": "Bonus 1: 10 Irresistible Texts",
    "subtitle": "To reignite desire in your relationship",
    "valueBadge": "Value €39",
    "intro": "Simple and powerful messages to send him to reignite the flame, create longing, and revive the game of seduction, even after years together.",
    "tipTitle": "Pro Tip & Advice",
    "tipText": "Send these messages with confidence, at the right moment, and without expectations. The secret is to spark emotion, not seek validation. Let the magic happen naturally...",
    "copyBtn": "Copy Text",
    "copiedBtn": "Copied!",
    "authorBy": "By Lina Rela",
    "smsLabel": "Text"
  },
  "es": {
    "title": "Bonus 1: 10 SMS Irresistibles",
    "subtitle": "Para reavivar el deseo en tu pareja",
    "valueBadge": "Valor 39 €",
    "intro": "Mensajes simples y poderosos para enviarle, reavivar la llama, crear añoranza y renacer el juego de la seducción.",
    "tipTitle": "Consejo Profesional",
    "tipText": "Envía estos mensajes con confianza, en el momento adecuado y sin expectativas. El secreto es despertar emoción, no buscar validación.",
    "copyBtn": "Copiar SMS",
    "copiedBtn": "¡SMS Copiado!",
    "authorBy": "Por Lina Rela",
    "smsLabel": "SMS"
  },
  "de": {
    "title": "Bonus 1: 10 Unwiderstehliche SMS",
    "subtitle": "Um das Begehren in Deiner Beziehung neu zu entfachen",
    "valueBadge": "Wert 39 €",
    "intro": "Einfache und kraftvolle Nachrichten, um das Feuer neu zu entfachen, Sehnsucht zu wecken und das Spiel der Verführung neu zu beleben.",
    "tipTitle": "Pro-Tipp & Ratschlag",
    "tipText": "Sende diese Nachrichten mit Selbstvertrauen, im richtigen Moment und ohne Erwartungen. Das Geheimnis liegt darin, Emotionen zu wecken.",
    "copyBtn": "SMS Kopieren",
    "copiedBtn": "Kopiert!",
    "authorBy": "Von Lina Rela",
    "smsLabel": "SMS"
  },
  "it": {
    "title": "Bonus 1: 10 SMS Irresistibili",
    "subtitle": "Per riaccendere il desiderio nella tua coppia",
    "valueBadge": "Valore 39 €",
    "intro": "Messaggi semplici e potenti da inviargli per riaccendere la fiamma, creare mancanza e far rinascere il gioco della seduzione.",
    "tipTitle": "Consiglio Pro",
    "tipText": "Invia questi messaggi con fiducia, al momento giusto e senza aspettative. Il segreto è suscitare emozione.",
    "copyBtn": "Copia SMS",
    "copiedBtn": "Copiato!",
    "authorBy": "Di Lina Rela",
    "smsLabel": "SMS"
  },
  "pt": {
    "title": "Bónus 1: 10 SMS Irresistíveis",
    "subtitle": "Para reavivar o desejo na sua relação",
    "valueBadge": "Valor 39 €",
    "intro": "Mensagens simples e poderosas para lhe enviar, acender a chama e fazer renascer o jogo da sedução.",
    "tipTitle": "Dica Profissional",
    "tipText": "Envie estas mensagens com confiança, no momento certo e sem expectativas. O segredo é despertar emoção.",
    "copyBtn": "Copiar SMS",
    "copiedBtn": "Copiado!",
    "authorBy": "Por Lina Rela",
    "smsLabel": "SMS"
  },
  "nl": {
    "title": "Bonus 1: 10 Onweerstaanbare SMS'jes",
    "subtitle": "Om het verlangen in je relatie te heroveren",
    "valueBadge": "Waarde €39",
    "intro": "Eenvoudige en krachtige berichten om het vuur weer aan te wakkeren en de verleiding te laten herleven.",
    "tipTitle": "Pro Tip",
    "tipText": "Stuur deze berichten met zelfvertrouwen op het juiste moment. Het geheim is emotie opwekken.",
    "copyBtn": "SMS Kopiëren",
    "copiedBtn": "Gekopieerd!",
    "authorBy": "Door Lina Rela",
    "smsLabel": "SMS"
  },
  "ru": {
    "title": "Бонус 1: 10 Неотразимых СМС",
    "subtitle": "Чтобы разжечь страсть в ваших отношениях",
    "valueBadge": "Ценность 39 €",
    "intro": "Простые и мощные сообщения, чтобы зажечь пламя, вызвать тоску и возродить игру соблазнения.",
    "tipTitle": "Совет Профессионала",
    "tipText": "Отправляйте эти сообщения с уверенностью, в нужный момент и без ожиданий. Секрет в эмоциях.",
    "copyBtn": "Копировать СМС",
    "copiedBtn": "Скопировано!",
    "authorBy": "Лина Рела",
    "smsLabel": "СМС"
  },
  "tr": {
    "title": "Bonus 1: 10 Etkileyici SMS",
    "subtitle": "İlişkinizde tutkuyu yeniden alevlendirmek için",
    "valueBadge": "Değer 39 €",
    "intro": "Ateşi yeniden yakmak, özlem yaratmak ve baştan çıkarma oyununu canlandırmak için ona gönderebileceğiniz güçlü mesajlar.",
    "tipTitle": "İpucu & Tavsiye",
    "tipText": "Bu mesajları özgüvenle, doğru zamanda ve beklentisizce gönderin. Sır duygu uyandırmaktır.",
    "copyBtn": "SMS'i Kopyala",
    "copiedBtn": "Kopyalandı!",
    "authorBy": "Lina Rela Tarafından",
    "smsLabel": "SMS"
  },
  "ar": {
    "title": "البونص ١: ١٠ رسائل نصية لا تُقاوم",
    "subtitle": "لإعادة إشعال الشغف في علاقتكِ الزوجية",
    "valueBadge": "القيمة ٣٩ يورو",
    "intro": "رسائل بسيطة وقوية لإرسالها له لإعادة إشعال الشعلة وتأجيج الشوق وإحياء لعبة الإغراء.",
    "tipTitle": "نصيحة الذهبية",
    "tipText": "أرسلي هذه الرسائل بثقة في الوقت المناسب ودون انتظار مقابل. السر هو إثارة المشاعر برقي...",
    "copyBtn": "نسخ الرسالة",
    "copiedBtn": "تم النسخ!",
    "authorBy": "بقلم لينا ريلا",
    "smsLabel": "رسالة"
  }
};

export const SMS_DATA: SmsItem[] = [
  {
    id: 1,
    text: {
      "fr": "« J’ai repensé à notre première nuit ensemble… tu te rappelles ce moment où tout a basculé ? »",
      "en": "“I was thinking back to our first night together... do you remember the moment everything shifted?”",
      "es": "«Estaba recordando nuestra primera noche juntos… ¿recuerdas el momento en que todo cambió?»",
      "de": "„Ich habe an unsere erste gemeinsame Nacht gedacht… erinnerst du dich an den Moment, als sich alles veränderte?“",
      "it": "«Ho ripensato alla nostra prima notte insieme… ti ricordi il momento in cui tutto è cambiato?»",
      "pt": "«Estava a recordar a nossa primeira noite juntos… lembras-te do momento em que tudo mudou?»",
      "nl": "“Ik dacht terug aan onze eerste nacht samen... herinner je je het moment dat alles veranderde?”",
      "ru": "«Я вспомнила нашу первую ночь вместе… помнишь тот момент, когда всё изменилось?»",
      "tr": "“Birlikte ilk gecemizi düşünüyordum… her şeyin değiştiği o anı hatırlıyor musun?”",
      "ar": "«كنت أفكر في أول ليلة قضيناها معاً... هل تتذكر اللحظة التي تغير فيها كل شيء؟»",
    }
  },
  {
    id: 2,
    text: {
      "fr": "« Je ne sais pas si c’est ton parfum ou ton regard qui me rend folle aujourd’hui. »",
      "en": "“I don't know if it's your perfume or your gaze that's driving me crazy today.”",
      "es": "«No sé si es tu perfume o tu mirada lo que me tiene loca hoy.»",
      "de": "„Ich weiß nicht, ob es dein Parfum oder dein Blick ist, der mich heute wahnsinnig macht.“",
      "it": "«Non so se sia il tuo profumo o il tuo sguardo a rendermi pazza oggi.»",
      "pt": "«Não sei se é o teu perfume ou o teu olhar que me está a enlouquecer hoje.»",
      "nl": "“Ik weet niet of het je parfum is of je blik, maar je maakt me gek vandaag.”",
      "ru": "«Не знаю, твой ли это парфюм или твой взгляд, но ты сводишь меня с ума сегодня.»",
      "tr": "“Bugün beni deli eden parfümün mü yoksa bakışların mı bilmiyorum.”",
      "ar": "«لا أعلم إن كان عطرك أم نظراتك هي التي تجعلني أذوب شغفاً اليوم.»",
    }
  },
  {
    id: 3,
    text: {
      "fr": "« Tu ne réalises pas à quel point tu peux encore me troubler sans rien faire. »",
      "en": "“You don't realize how much you can still captivate me without doing a thing.”",
      "es": "«No te das cuenta de lo mucho que me sigues cautivando sin hacer nada.»",
      "de": "„Du ahnst nicht, wie sehr du mich immer noch verwirren kannst, ohne irgendwas zu tun.“",
      "it": "«Non ti rendi conto di quanto tu riesca ancora a turbarmi senza fare nulla.»",
      "pt": "«Não percebes o quanto ainda me podes perturbar sem fazer nada.»",
      "nl": "“Je hebt geen idee hoe erg je me nog steeds kunt stimuleren zonder iets te doen.”",
      "ru": "«Ты даже не представляешь, как всё ещё можешь волнуешь меня, ничего не делая.»",
      "tr": "“Hiçbir şey yapmadan bile beni hâlâ ne kadar etkileyebildiğinin farkında değilsin.”",
      "ar": "«أنت لا تدرك مدى قدرتك على إرباكي وجذبي دون أن تفعل شيئاً.»",
    }
  },
  {
    id: 4,
    text: {
      "fr": "« Si tu savais ce que j’ai envie de te dire… mais je préfère te le murmurer ce soir. »",
      "en": "“If you only knew what I want to tell you... but I prefer to whisper it to you tonight.”",
      "es": "«Si supieras lo que tengo ganas de decirte… pero prefiero susurrártelo esta noche.»",
      "de": "„Wenn du wüsstest, was ich dir sagen möchte… aber ich flüstere es dir lieber heute Abend.“",
      "it": "«Se sapessi cosa ho voglia di dirti… ma preferisco sussurrartelo stasera.»",
      "pt": "«Se soubesses o que te quero dizer… mas prefiro sussurrar-te logo à noite.»",
      "nl": "“Als je eens wist wat ik je wil zeggen... maar ik fluister het je vanavond liever in.”",
      "ru": "«Если бы ты знал, что я хочу тебе сказать… но я предпочту шепнуть тебе это сегодня вечером.»",
      "tr": "“Sana ne söylemek istediğimi bir bilsen… ama bu gece kulağına fısıldamayı tercih ederim.”",
      "ar": "«لو تعلم ما أود أن أقوله لك... لكني أُفضل أن أهمس به في أذنك الليلة.»",
    }
  },
  {
    id: 5,
    text: {
      "fr": "« C’est fou comme tu peux encore me faire sourire juste en pensant à toi. »",
      "en": "“It's crazy how you can still make me smile just by thinking of you.”",
      "es": "«Es increíble cómo me sigues haciendo sonreír solo con pensar en ti.»",
      "de": "„Es ist verrückt, wie du mich immer noch zum Lächeln bringst, nur indem ich an dich denke.“",
      "it": "«È incredibile come tu riesca ancora a farmi sorridere solo pensando a te.»",
      "pt": "«É incrível como ainda me fazes sorrir só de pensar em ti.»",
      "nl": "“Het is bizar hoe je me nog steeds kunt laten glimlachen door alleen aan je te denken.”",
      "ru": "«Удивительно, как ты всё ещё заставляешь меня улыбаться, просто думая о тебе.»",
      "tr": "“Sadece seni düşünerek bile beni hâlâ gülümsetebilmen çok çılgınca.”",
      "ar": "«من المدهش كيف يمكنك تقليب مبتسمتي وتفائلي بمجرد التفكير فيك.»",
    }
  },
  {
    id: 6,
    text: {
      "fr": "« Tu me manques… mais pas de la façon dont tu crois. »",
      "en": "“I miss you... but not in the way you think.”",
      "es": "«Te echo de menos… pero no de la forma que crees.»",
      "de": "„Du fehlst mir… aber nicht auf die Art, wie du denkst.“",
      "it": "«Mi manchi… ma non nel modo in cui pensi.»",
      "pt": "«Tenho saudades tuas… mas não da forma como pensas.»",
      "nl": "“Ik mis je... maar niet op de manier die je denkt.”",
      "ru": "«Я скучаю по тебе… но не так, как ты думаешь.»",
      "tr": "“Seni özlüyorum… ama düşündüğün şekilde değil.”",
      "ar": "«أنا أشتاق إليك... ولكن ليس بالطريقة التي تعتقدها.»",
    }
  },
  {
    id: 7,
    text: {
      "fr": "« J’ai eu une idée un peu folle pour nous deux. Tu veux que je t’en parle ou tu préfères la découvrir ? »",
      "en": "“I had a slightly crazy idea for the two of us. Do you want me to tell you, or prefer to find out?”",
      "es": "«Tuve una idea un poco loca para los dos. ¿Quieres que te la cuente o prefieres descubrirla?»",
      "de": "„Ich hatte eine verrückte Idee für uns zwei. Soll ich sie dir erzählen oder willst du sie entdecken?“",
      "it": "«Ho avuto un'idea un po' folle per noi due. Vuoi che te ne parli o preferisci scoprirla?»",
      "pt": "«Tive uma ideia um pouco louca para nós dois. Queres que te conte ou preferes descobrir?»",
      "nl": "“Ik had een gek idee voor ons tweeën. Wil je dat ik het vertel of ontdek je het liever?”",
      "ru": "«У меня появилась безумная идея для нас двоих. Хочешь расскажу или предпочтешь узнать потом?»",
      "tr": "“İkimiz için biraz çılgınca bir fikrim var. Anlatayım mı yoksa keşfetmeyi mi tercih edersin?”",
      "ar": "«خطرت لي فكرة مجنونة بعض الشيء لنا نحن الاثنين. هل تريد أن أخبرك أم تفضل اكتشافها بنفسك؟»",
    }
  },
  {
    id: 8,
    text: {
      "fr": "« Si tu savais ce que ton dernier message m’a fait… »",
      "en": "“If you only knew what your last message did to me...”",
      "es": "«Si supieras lo que me hizo tu último mensaje…»",
      "de": "„Wenn du wüsstest, was deine letzte Nachricht mit mir gemacht hat…“",
      "it": "«Se sapessi cosa mi ha fatto il tuo ultimo messaggio…»",
      "pt": "«Se soubesses o que a tua última mensagem me fez…»",
      "nl": "“Als je wist wat je laatste berichtje met me deed...”",
      "ru": "«Если бы ты знал, что твое последнее сообщение сделало со мной…»",
      "tr": "“Son mesajının bana ne yaptığını bir bilsen…”",
      "ar": "«لو تعلم ماذا فعلت بي رسالتك الأخيرة...»",
    }
  },
  {
    id: 9,
    text: {
      "fr": "« Ce soir, je veux juste être celle qui te fait oublier le reste du monde. »",
      "en": "“Tonight, I just want to be the one who makes you forget the rest of the world.”",
      "es": "«Esta noche, solo quiero ser la persona que te haga olvidar el resto del mundo.»",
      "de": "„Heute Abend möchte ich einfach die sein, die dich den Rest der Welt vergessen lässt.“",
      "it": "«Stasera voglio solo essere colei che ti fa dimenticare il resto del mondo.»",
      "pt": "«Esta noite, só quero ser aquela que te faz esquecer o resto do mundo.»",
      "nl": "“Vanavond wil ik gewoon degene zijn die je de rest van de wereld doet vergeten.”",
      "ru": "«Сегодня вечером я просто хочу быть той, кто заставит тебя забыть обо всем мире.»",
      "tr": "“Bu gece sadece sana tüm dünyayı unutturan kişi olmak istiyorum.”",
      "ar": "«الليلة، أريد فقط أن أكون تلك التي تجعلك تنسى العالم بأكمله.»",
    }
  },
  {
    id: 10,
    text: {
      "fr": "« Tu veux savoir à quoi je pense en ce moment ? Indice : c’est toi, mais version sans filtre. »",
      "en": "“Wanna know what I'm thinking about right now? Hint: it's you, but unfiltered.”",
      "es": "«¿Quieres saber en qué estoy pensando ahora? Pista: eres tú, pero sin filtro.»",
      "de": "„Willst du wissen, woran ich gerade denke? Hinweis: an dich, aber unzensiert.“",
      "it": "«Vuoi sapere a cosa sto pensando in questo momento? Indizio: sei tu, versione senza filtri.»",
      "pt": "«Queres saber no que estou a pensar agora? Pista: és tu, mas versão sem filtro.»",
      "nl": "“Wil je weten waar ik nu aan denk? Hint: aan jou, maar dan ongefilterd.”",
      "ru": "«Хочешь знать, о чем я сейчас думаю? Подсказка: о тебе, но без фильтров.»",
      "tr": "“Şu an ne düşündüğümü bilmek ister misin? İpucu: sensin, ama filtresiz versiyonun.”",
      "ar": "«هل تريد أن تعرف بمَ أفكر في هذه اللحظة؟ تلميح: أفكر فيك، ولكن دون أي قيود.»",
    }
  },
];
