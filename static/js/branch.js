function BranchButton(element) {
    let firstButton = document.getElementById('show-branches');
    let secondButton = document.getElementById('show-map');

    if (element === firstButton) {
        firstButton.classList.add('active_btn');
        secondButton.classList.remove('active_btn');
    } else if (element === secondButton) {
        secondButton.classList.add('active_btn');
        firstButton.classList.remove('active_btn');
    }
}


document.getElementById("show-branches").addEventListener("click", function() {
    document.getElementById("branches-list").style.display = "block";
    document.getElementById("map").style.display = "none";
});

document.getElementById("show-map").addEventListener("click", function() {
    document.getElementById("map").style.display = "block";
    document.getElementById("branches-list").style.display = "none";
});