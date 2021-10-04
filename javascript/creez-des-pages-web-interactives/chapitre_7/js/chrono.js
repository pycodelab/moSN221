function incrementation () {
    nbreSecondes = Number(document.querySelector("span").textContent);
    document.querySelector("span").textContent = nbreSecondes+1;
}


document.getElementById("bouton").addEventListener("click", function(e){
    e.target.textContent = "Arrêter";
    setInterval(incrementation(),1000);
})