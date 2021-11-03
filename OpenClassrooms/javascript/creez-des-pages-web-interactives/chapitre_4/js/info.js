
infoElt = getComputedStyle(document.getElementById("contenu"));
console.log(infoElt.height);
console.log(infoElt.width);

titreInfo = document.createElement("p");
titreInfo.id = "titre";
titreInfo.textContent = "Informations sur l'élément";
document.querySelector("body").appendChild(titreInfo);

liste = document.createElement("ul");
liste.id = "liste";
document.getElementById("titre").appendChild(liste);

infolongueur = document.createElement("li");
infolongueur.id = "longueur";
infolongueur.textContent = "Longueur: "+infoElt.height;
document.getElementById("liste").appendChild(infolongueur);

infolargeur = document.createElement("li");
infolargeur.id = "largeur";
infolargeur.textContent = "Largeur: "+infoElt.width;
document.getElementById("liste").appendChild(infolargeur);

