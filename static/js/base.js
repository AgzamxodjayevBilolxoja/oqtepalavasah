let logout = document.getElementById("logout");
let logout_div = document.getElementById("logout-div");
let logout_no = document.getElementById("logout-no");

logout.addEventListener("click", function() {
    logout_div.classList.add("logout-div")
})

logout_no.addEventListener("click", function() {
    window.location.replace('http://127.0.0.1:8000/')
    // logout_div.classList.remove("logout-div")
})
