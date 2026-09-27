
        function setTranslateCookie(langCode) {
            var domain = window.location.hostname;
            var cookieVal = "/fr/" + langCode;
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            document.cookie = "googtrans=" + cookieVal + "; path=/;";
            if (domain && domain !== 'localhost' && domain !== '127.0.0.1') {
                document.cookie = "googtrans=" + cookieVal + "; path=/; domain=" + domain + ";";
                document.cookie = "googtrans=" + cookieVal + "; path=/; domain=." + domain + ";";
            }
        }

        function resetToFrenchDefault() {
            var domain = window.location.hostname;
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=" + domain + ";";
            document.cookie = "googtrans=/fr/fr; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            localStorage.removeItem('selected_landing_lang');
        }

        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'fr',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
                autoDisplay: false
            }, 'google_translate_element');
        }

        function changePageLanguage(langCode) {
            if (!langCode || langCode === 'fr') {
                resetToFrenchDefault();
                location.reload();
                return;
            }
            localStorage.setItem('selected_landing_lang', langCode);
            setTranslateCookie(langCode);
            var googleSelect = document.querySelector('.goog-te-combo');
            if (googleSelect) {
                googleSelect.value = langCode;
                googleSelect.dispatchEvent(new Event('change'));
            }
            var selectElem = document.getElementById('custom-language-select');
            if (selectElem) {
                selectElem.value = langCode;
            }
            setTimeout(function() {
                location.reload();
            }, 150);
        }

        function syncLanguageDropdownUI() {
            var savedLang = localStorage.getItem('selected_landing_lang');
            var match = document.cookie.match(/(?:^|;\s*)googtrans=([^;]*)/);
            var activeLang = savedLang || 'fr';
            if (match && match[1]) {
                var parts = match[1].split('/');
                if (parts.length >= 3 && parts[2]) {
                    activeLang = parts[2];
                }
            }
            var selectElem = document.getElementById('custom-language-select');
            if (selectElem && activeLang) {
                selectElem.value = activeLang;
            }
        }

        
        function updateRTLState() {
            var savedLang = localStorage.getItem('selected_landing_lang');
            var match = document.cookie.match(/(?:^|;\s*)googtrans=([^;]*)/);
            var activeLang = savedLang || 'fr';
            if (match && match[1]) {
                var parts = match[1].split('/');
                if (parts.length >= 3 && parts[2]) {
                    activeLang = parts[2];
                }
            }
            if (activeLang === 'ar') {
                document.documentElement.setAttribute('dir', 'rtl');
            } else {
                document.documentElement.setAttribute('dir', 'ltr');
            }
        }

        document.addEventListener('DOMContentLoaded', updateRTLState);
        window.addEventListener('load', updateRTLState);

        document.addEventListener('DOMContentLoaded', syncLanguageDropdownUI);
    