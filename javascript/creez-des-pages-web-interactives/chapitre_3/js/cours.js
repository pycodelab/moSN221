// Modification du contenu HTML de la liste : ajout d'un langage
document.getElementById("langages").innerHTML += '<li id="c">C</li>';

//Supression du contenu HTML de la liste
//document.getElementById("langages").innerHTML = "";

//Modification du contenu textuel du premier titre
document.querySelector("h1").textContent += " de programmation";

//Définition de l'attribut "id" du premier titre
document.querySelector("h1").setAttribute("id","titre");
document.querySelector("h1").id = "titre";

var titreElt = document.querySelector("h1"); //Accès au premier titre h1
titreElt.classList.remove("debut"); //Suprression de la classe "debut"
titreElt.classList.add("titre"); //Ajout de la classe"titre"
console.log(titreElt);

var pythonElt = document.createElement("li");//Création d'un élément li
pythonElt.id = "python"; //Définition de son identifiant
pythonElt.textContent = "Python"; //Définition de son contenu textuel
document.getElementById("langages").appendChild(pythonElt); //Insertion d'un nouvel élément

//Variante = ajouter un noeud de type texte au nouvel élément
var rubyElt = document.createElement("li"); // Création d'un élément li
rubyElt.id = "ruby"; //Définition de son identifiant
rubyElt.appendChild(document.createTextNode("Ruby")); //Définition de son contenu textuel
document.getElementById("langages").appendChild(rubyElt); //Insertion du nouvel Element

//Ajout d'un noeud avant un autre noeud
var perlElt = document.createElement("li");
perlElt.id = "perl";
perlElt.textContent="Perl";
//Ajout du nouvel élément avant l'identifiant identifié par php
document.getElementById("langages").insertBefore(perlElt,document.getElementById("php"));

//Choix de la position exacte avec (beforebegin, afterbegin, beforeend, afterend) en utilisant insertadjacentHTML (position, contenu HTML à ajouter)
//Ajout d'un élément au tout début de la liste
document.getElementById("langages").insertAdjacentHTML("afterbegin", '<li id="javascript">Javascript</li>');

var bashElt = document.createElement("li");
bashElt.id = "bash";
bashElt.textContent = "Bash";
//Remplacement de l'élément identifié par "perl" par le nouveau élément
document.getElementById("langages").replaceChild(bashElt,document.getElementById("perl"));
//Suppression de l'élément identifié par "bash"
document.getElementById("langages").removeChild(document.getElementById("bash"));

//Ajout d'un paragraphe
var newParagraph = document.createElement("p");
newParagraph.id = "paragraph";
newParagraph.appendChild(document.createTextNode("En voici une "));
var lien = document.createElement("a");
lien.id = "lien";
lien.href = "https://fr.wikipedia.org/wiki/Liste_de_langages_de_programmation";
lien.textContent = "liste";
newParagraph.appendChild(lien);
newParagraph.appendChild(document.createTextNode(" complète."));
document.getElementById("contenu").appendChild(newParagraph);
