document.getElementById('region').addEventListener('click', function () {
    let regions = document.getElementById('regions')
    if (regions.style.display === "none") {
        regions.style.display = "flex"
    } else {
        regions.style.display = "none"
    }
})

function RegionUrl(region) {
    let url = window.location.href;

    if (url.includes('region=')) {
        url = url.replace(/(region=)[^\&]+/, `$1${region}`);
    } else {
        const separator = url.includes('?') ? '&' : '?';
        url += `${separator}region=${region}`;
    }

    window.location.href = url;
}