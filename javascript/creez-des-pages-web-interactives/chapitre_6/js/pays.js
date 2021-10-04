// Liste des pays
var listePays = [
    "Afghanistan",
    "Afrique du Sud",
    "Albanie",
    "Algérie",
    "Allemagne",
    "Andorre",
    "Angola",
    "Anguilla",
    "Antarctique",
    "Antigua-et-Barbuda",
    "Antilles néerlandaises",
    "Arabie saoudite",
    "Argentine",
    "Arménie",
    "Aruba",
    "Australie",
    "Autriche",
    "Azerbaïdjan"
];

var paysElt = document.getElementById("pays");
var suggestionsElt = document.getElementById("suggestions");

//Changement de la valeur saisie
paysElt.addEventListener("input", function (e) {
    suggestionsElt.innerHTML="";
    
    listePays.forEach(function (pays) {
        //Si valeur en cours de saisie correspond au début du pays
        if (pays.indexOf(paysElt.value)===0) {
            var suggestionElt = document.createElement("div");
            suggestionElt.classList.add("suggestion");
            suggestionElt.textContent = pays;
        // Gère le clic sur une suggestion
            suggestionElt.addEventListener("click",function (e) {
                //Remplacement de la valeur saisie par la suggestion
                paysElt.value = e.target.textContent;
                //Vidage de la liste des suggestions
                suggestionsElt.innerHTML="";
            });
            suggestionsElt.appendChild(suggestionElt);
        }
    });
    
});
    
   