var Chien = {
    // initialise le chien
    init: function (nom, race, taille) {
        this.nom = nom;
        this.race = race;
        this.taille = taille;
    },
    // renvoie l'aboiement du chien
    aboyer: function () {
        var aboiement = "Whoua ! Whoua!";
        if (this.taille < 25) {
            aboiement = "Kaii ! Kaii !";
        } else if (this.taille > 60) {
            aboiement = "Grr ! Grr !";
        }
        return aboiement;
    },
    decrire: function () {
    var description = this.nom + " est un " + this.race + " mesurant " + this.taille + "cm. Il aboie : " + this.aboyer();
    return description 
}
};

var chenil = [];
chien1 = Object.create(Chien);
chien1.init("Crockdur","mâtin de Naples",75);
chenil.push(chien1);
chien2 = Object.create(Chien);
chien2.init("Pupuce","bichon",22);
chenil.push(chien2);
chien3 = Object.create(Chien);
chien3.init("Médor","labrador",58);
chenil.push(chien3);

console.log("le chenil héberge " + chenil.length + " chiens.");
chenil.forEach(function (chien) {
    console.log(chien.decrire());
});
