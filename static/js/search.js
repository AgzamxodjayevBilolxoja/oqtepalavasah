function search() {
    const query = document.getElementById("searchInput").value;

    if (!query) {
        return;
    }

    const currentUrl = new URL(window.location.href);

    if (currentUrl.searchParams.has("search")) {
        currentUrl.searchParams.set("search", query);
    } else {
        currentUrl.searchParams.append("search", query);
    }

    window.location.href = currentUrl.toString();
}

function search2() {
    const query = document.getElementById("searchbInput").value;

    if (!query) {
        return;
    }

    const currentUrl = new URL(window.location.href);

    if (currentUrl.searchParams.has("search_b")) {
        currentUrl.searchParams.set("search_b", query);
    } else {
        currentUrl.searchParams.append("search_b", query);
    }

    window.location.href = currentUrl.toString();
}
