// Liste des journaux
var journaux = ["http://lemonde.fr","http://lefigaro.fr","http://liberation.fr"];
var nomJournal=["Le monde","Le figaro","Liberation"]

var listeJournal = document.createElement("ul");
listeJournal.id="liste";
document.getElementById("contenu").appendChild(listeJournal);

lienJournal =[];
ajoutJournal = [];

function ajouterJournal (i) {
    ajoutJournal[i] = document.createElement("a");
    ajoutJournal[i].id = nomJournal[i];
    ajoutJournal[i].textContent = nomJournal[i];
    ajoutJournal[i].href = journaux[i];
}
ajouterJournal(0);
ajouterJournal(1);
ajouterJournal(2);
console.log (ajoutJournal);

function ajouterliste (i) {
    lienJournal[i] = document.createElement("li");
    lienJournal[i].id = nomJournal[i];
}

ajouterliste(0);
ajouterliste(1);
ajouterliste(2);

console.log(lienJournal);

for (i=0; i<journaux.length; i++) {
document.getElementById("liste").appendChild(lienJournal[i]);
document.getElementById(nomJournal[i]).appendChild(ajoutJournal[i]);
}

/*ajoutJournal = document.createElement("li");
ajoutJournal.id = "ajout";
lienJournal= document.createElement("a");
lienJournal.id = "lien";
lienJournal.href = "http://lemonde.fr" ;
lienJournal.textContent = "Le monde"; 
console.log(lienJournal);
console.log(ajoutJournal);
document.getElementById("contenu").appendChild(listeJournal);
document.getElementById("liste").appendChild(ajoutJournal);
document.getElementById("ajout").appendChild(lienJournal);
document.getElementById("liste").appendChild(ajoutJournal);
document.getElementById("contenu").appendChild(listeJournal);*/

