var films = ["Le loup de Wall Street", "Vice-Versa", "Babysitting"];
console.log(films.length); //Affiche 3

var tableauVide = []; //Création d'un tableau vide
console.log(tableauVide.length); // Affiche 0

console.log(films[0]);
console.log(films[1]);
console.log(films[2]);

//Parcourir un tableau
for (var i =0; i<films.length; i++) {
    console.log(films[i]);
}
 //Parcourir un tableau
films.forEach(function (film) {
    console.log(film);
});

//Ajouter un élément au tableau
films.push("Les Bronzés");
console.log(films[3]);

//Tableaux d'objets
var Film = {
    //Initialise le film
    init:function (titre,annee) {
        this.titre = titre;
        this.annee = annee;
    },
    // Renvoie la description du film
    decrire:function () {
        var description = this.titre + " (" + this.annee + ")";
        return description;
    }
};

var film1=Object.create(Film);
film1.init("Le loup de Wall Street",2013);

var film2=Object.create(Film);
film2.init("Vice-Versa",2015);

var film3=Object.create(Film);
film3.init("Babbysitting",2013);

var tableauFilms = [];
tableauFilms.push(film1);
tableauFilms.push(film2);
tableauFilms.push(film3);

tableauFilms.forEach(function (film) {
    console.log(film.decrire());
});
