document.getElementById('lang').addEventListener("click", function () {
    let langs = document.getElementById('langs')
    if (langs.style.display === "none") {
        langs.style.display = "flex"
    } else {
        langs.style.display = "none"
    }
})

function addParamToUrl(lang) {
    let url = window.location.href;

    if (url.includes('lang=')) {
        url = url.replace(/(lang=)[^\&]+/, `$1${lang}`);
    } else {
        const separator = url.includes('?') ? '&' : '?';
        url += `${separator}lang=${lang}`;
    }

    window.location.href = url;
}