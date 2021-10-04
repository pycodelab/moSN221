paragraphe = document.querySelectorAll("div");
console.log(paragraphe);
couleurTexte = prompt("Entrez une couleur de texte");
couleurFond = prompt("Entrez une couleur de fond");
for (i in paragraphe) {
paragraphe[i].style.backgroundColor = couleurFond;
paragraphe[i].style.color = couleurTexte;
}