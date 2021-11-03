document.querySelector("button").addEventListener("click", function (e) {
    nouveauDessert = prompt("Entrer le nom d'un dessert");
    ajoutDessert = document.createElement("li");
    ajoutDessert.id = nouveauDessert;
    ajoutDessert.textContent = nouveauDessert;
    ajoutDessert.addEventListener ("click",function (e) {
        newDessert = prompt("Modifier le dessert :", e.target.textContent);
        e.target.textContent = newDessert;
    })
    
    document.getElementById("desserts").appendChild(ajoutDessert);
})
