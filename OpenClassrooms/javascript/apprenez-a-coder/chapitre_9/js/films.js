var Film = {
    init:function (titre,annee,realisateur) {
        this.titre = titre;
        this.annee = annee;
        this.realisateur = realisateur;
    },
    decrire: function () {
        var description = this.titre + " (" + this.annee + ", "+ this.realisateur + ")";
        return description;
    }
};

var films = [];
var film1 = Object.create(Film);
film1.init("Le loup de Wall Street", 2013, "Martin Scorsese");
var film2 = Object.create(Film);
film2.init("Vice-versa", 2015, "Pete Docter");
var film3 = Object.create(Film);
film3.init("Baby-sitting", 2013, "Phillipe Lacheau et Nicolas Benamou");
films.push(film1);
films.push(film2);
films.push(film3);

films.forEach(function (film) {
    console.log(film.decrire());
});