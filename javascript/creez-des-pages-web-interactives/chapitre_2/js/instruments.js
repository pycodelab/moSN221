function infosLiens () {
    var nbreLien = 0;
    if (document.querySelectorAll("a")) {
        for (i=0; i<document.querySelectorAll("a").length;i++) {
            if (document.querySelectorAll("a")[i].hasAttribute("href")) {
                nbreLien++;
            }
        }
        var premierLien = document.querySelector("a").href;
        var dernierLien= document.querySelectorAll("a")[nbreLien-1].href ;
    }
    else {
        console.log("Pas de liens dans cette page !")
    }
    
    console.log(nbreLien);
    console.log(premierLien);
    console.log(dernierLien);
}

infosLiens();


function possede (attributID,contenuClass) {
    if (document.getElementById(attributID)) {
    console.log((document.getElementById(attributID).classList.contains(contenuClass)));
    }
    else {
        console.log("Aucun élément ne possède l'attribut "+attributID);
    }
}

possede("saxophone","bois");
possede("saxophone","cuivre");
possede("trompette","cuivre");
possede("contrebasse","cordes");