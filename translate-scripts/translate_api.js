const translate = async (text) => {
    const sourceLang = 'en';
    const targetLang = 'hi';
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${sourceLang}&tl=${targetLang}&dt=t&q=${encodeURI(text)}`;

    const response = await fetch(url);
    const data = await response.json();

    if (data[0][0][0]) {
        return data[0][0][0];
    } else {
        return text;
    }
};


let elements = document.querySelectorAll('body strong, h1, a:not(a.hover-no-underline), body span:not(span.icon-medium), body h2, body h3, body button,p, footer a, a.link-gray-underline a.site-header__navigation-action, a.site-header__navigation-submenu-action');
for (let element of elements) {
    if (element.innerText) {
        const originalText = element.innerText
        translate(originalText.toString())
            .then((translatedText) => {
                element.innerText = translatedText;
            })
            .catch((error) => {
                console.error(error);
                element.innerText = originalText;
            });
    }
}
