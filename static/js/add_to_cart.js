function toggleCart(button, lang) {
    // Buttonning data-id atributidan p.id ni olish
    var productId = button.getAttribute("data-id");

    // CSRF tokenni meta tegidan olish
    var csrfToken = document.querySelector('[name=csrf-token]').getAttribute('content');

    // Turli tillar uchun button matnlarini sozlash
    var addToCartText, removeFromCartText;

    if (lang === "ru") {
        addToCartText = "Добавить в корзину";
        removeFromCartText = "Убрать из корзины";
    } else if (lang === "en") {
        addToCartText = "Add to Cart";
        removeFromCartText = "Remove from Cart";
    } else {
        addToCartText = "Savatga qo'shish";
        removeFromCartText = "Savatdan olib tashlash";
    }

    // AJAX so'rovini yuborish
    fetch(`/add-to-cart/${productId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({})
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                // Button matnini o'zgartirish
                if (button.textContent.trim() === addToCartText) {
                    button.textContent = removeFromCartText;
                } else {
                    button.textContent = addToCartText;
                }
            } else {
            }
        })
}