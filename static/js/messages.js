document.addEventListener("DOMContentLoaded", function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach((message) => {
        setTimeout(() => {
            message.style.display = 'none';
        }, 5000);
    });
});
