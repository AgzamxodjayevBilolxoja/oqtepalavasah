function toggleHeart(button) {
    var productId = button.getAttribute("data-id");
    var csrfToken = document.querySelector('[name=csrf-token]').getAttribute('content');
    var img = button.querySelector('img');

    // AJAX so'rovini yuborish
    fetch(`/add-like/${productId}/`, {
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
            // Yurakcha holatini o'zgartirish
            if (data.new_status) {
                img.src = data.new_icon;
            } else {
                img.src = data.new_icon;
            }
        } else {
            alert('Xato yuz berdi');
        }
    })
    .catch(error => {
        console.error('Xato:', error);
        alert('Xato yuz berdi');
    });
}
