var titresElts = document.getElementsByTagName("h2"); //Tous les titres h2
console.log(titresElts[0]); //Affiche le premier titre h2
console.log(titresElts.length); //Affiche 3

//Tous les élements ayant la classe "merveilles"
var merveillesElts = document.getElementsByClassName("merveilles");
for (var i=0;i<merveillesElts.length;i++) {
    console.log(merveillesElts[i]);
}

//Elément portant l'identifiant "nouvelles"
console.log(document.getElementById("nouvelles"));

//Tous les paragraphes
console.log(document.querySelectorAll("p").length);

//Tous les paragraphes à l'intérieur de l'élément identifié par "contenu"
console.log(document.querySelectorAll("#contenu p").length);

//Tous les éléments ayant la classe "existe"
console.log(document.querySelectorAll(".existe").length);

//Tous les éléments fils de l'élément identifié par "antiques" ayant la classe "existe"
console.log(document.querySelectorAll("#antiques > .existe").length);

//le premier paragraphe
console.log(document.querySelector("p"));

//Le contenu HTML de l'élément identifié par "contenu"
console.log(document.getElementById("contenu").innerHTML);

//Le contenu textuel de l'élément identifié par "contenu"
console.log(document.getElementById("contenu").textContent);

//L'attribut href du premier lien
console.log(document.querySelector("a").getAttribute("href"));

//L'identifiant de la première liste
console.log(document.querySelector("ul").id);

//L'attribut href du premier lien
console.log(document.querySelector("a").href);

if (document.querySelector("a").hasAttribute("target")) {
    console.log("Le premier lien possède l'attribut target");
} else {
    console.log("Le premier lien ne possède pas l'attribut target")
}

//Liste des classes de l'élément identifié par "antiques"
var classes = document.getElementById("antiques").classList;
console.log(classes.length);// affiche 1 : l'élément possède une seule classe
console.log(classes[0]); 

if(document.getElementById("antiques").classList.contains("merveilles")) {
    console.log("L'élément identifié par antiques possède la classe merveilles");
}
else {
    console.log("L'élément identifié par antiques ne possède pas la classe merveilles");
}
