// Liste des mots du dictionnaire
var mots = [
    {
        terme : "Procrastination",
        definition : "Tendance pathologique à remettre systématiquement au lendemain"
    },
    {
        terme : "Tautologie",
        definition : "Phrase dont la formulation ne peut qu'être vraie"
    },
    {
        terme : "Oxymore",
        definition : "Figure de style qui réunit dans un même syntaxe deux termes sémantiquement opposés"
    }
];

dico = document.createElement("dl");
dico.id = "dico";
document.getElementById("contenu").appendChild(dico);
mot = [];
description = [];
function creerMot (i) {
    mot[i] = document.createElement("dt");
    mot[i].id = mots[i].terme;
    mot[i].innerHTML ='<strong>'+ mots[i].terme+'</strong>';
    description[i] = document.createElement("dd");
    description[i].id = "description de "+ mots[i].terme;
    description[i].textContent = mots[i].definition;
}

function insertion (i) {
    document.getElementById("dico").appendChild(mot[i]);
    document.getElementById("dico").appendChild(description[i]);
}

creerMot(0);
creerMot(1);
creerMot(2);
console.log(mot);
console.log(description);

insertion (0);
insertion (1);
insertion (2);


    