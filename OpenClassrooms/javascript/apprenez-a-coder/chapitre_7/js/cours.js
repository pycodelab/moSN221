///Introduire une variable objet
var stylo = {
    type: "bille",
    couleur: "bleu",
    marque: "Bic",
};

//Constructeur MonObjet
/*function MonObjet() {
    //Initialisation de l'objet
    // ...
}

// Instanciation d'un objet à partir d'un constructeur
var monObj = new MonObjet();*/

console.log(stylo.type);
console.log(stylo.couleur);
console.log(stylo.marque);
console.log("Mon stylo à " + stylo.type+ " "+stylo.marque+ " écrit en "+stylo.couleur);

stylo.couleur="rouge"
console.log("Mon stylo à " + stylo.type+ " "+stylo.marque+ " écrit en "+stylo.couleur);

stylo.prix=2.5;
console.log("Mon stylo à " + stylo.type+ " "+stylo.marque+ " écrit en "+stylo.couleur+" et coûte "+stylo.prix);