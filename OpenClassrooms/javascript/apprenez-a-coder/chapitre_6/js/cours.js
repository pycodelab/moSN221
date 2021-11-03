//Longueur d'une chaîne de caractères
console.log("ABC".length);
console.log("Je suis une chaîne".length);
var mot="kangourou";
var longueurMot=mot.length;
console.log(longueurMot);

//Passage en majuscules ou minuscules
var motInitial="bonjour";
var motEnMinuscules=motInitial.toLowerCase();
var motEnMajuscules=motInitial.toUpperCase();
console.log(motEnMajuscules+" "+motEnMinuscules);
console.log("bonjour".toLowerCase()+" "+"bonjour".toUpperCase());

//comparer deux chaînes
var chaine="azerty";
console.log(chaine==="azerty");//affiche true
console.log(chaine==="qwerty");//affiche false

//comparer une chaine saisie par l'utilisateur
var valeurSaisie = "Quitter";
console.log(valeurSaisie==="quitter"); //affiche false
console.log(valeurSaisie.toLowerCase()==="quitter");//affiche true

//Accéder à une caractère d'une chaîne
//Attention, l'indice du premier caractère est 0 et non 1
//donc l'indice du dernier caractère = longueur de la chaine -1
var sport="Tennis-ballon";
console.log(sport.charAt(0));//affiche T
console.log(sport[0]);//Affiche T

//Parcourir une chaine de caractères
var nom="Mohamed";
for (i=0; i<nom.length; i++) {
    console.log(nom[i]);
}