let products = document.getElementsByClassName("product");
let buttons = document.getElementsByClassName("btn_0001");

Array.from(buttons).forEach(button => {
    button.addEventListener("click", function() {
        Array.from(products).forEach(product => {
//            let div = document.createElement("div")
            document.getElementById("add_product").style.display = "flex"

//            product.classList.add("add_product")
        });
    });
});

document.getElementById("x").addEventListener("click", function() {
    document.getElementById("add_product").style.display = "none"
})