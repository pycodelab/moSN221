// Liste de quelques maisons de Game of Thrones. Chaque maison a un code et un nom
var maisons = [
    {
        code: "ST",
        nom: "Stark"
    },
    {
        code: "LA",
        nom : "Lannister"
    },
    {
        code: "BA",
        nom: "Baratheon"
    },
    {
        code: "TA",
        nom: "Targaryen"
    }
];

// Renvoie un tableau contenant quelques personnages d'une maison
function getPersonnages(codeMaison) {
switch (codeMaison) {
        case "ST" :
            return ["Eddard", "Catelyn", "Robb", "Sansa", "Arya", "Jon Snow"];
        case "LA":
            return ["Tywin", "Cersei", "Jaime", "Tyrion"];
        case "BA":
            return ["Robert","Stannis","Renly"];
        case "TA":
            return ["Aerys", "Daenerys", "Viserys"];
        default:
            return [];       
    }
}

option = [];
for (i=0; i<maisons.length; i++) {
    option[i] = document.createElement("option");
    option[i].value = maisons[i].code;
    option[i].textContent = maisons[i].nom;
    document.getElementById("maison").appendChild(option[i]);
}


document.getElementById("maison").addEventListener("change", function (e) {
    document.getElementById("persos").textContent="";
    tableauPersonnage = getPersonnages(e.target.value);
    for (i=0; i<tableauPersonnage.length; i++) {
        personnage = document.createElement("li")
        personnage.id = tableauPersonnage[i];
        personnage.textContent = tableauPersonnage[i];
        document.getElementById("persos").appendChild(personnage);
    } 
}); 
