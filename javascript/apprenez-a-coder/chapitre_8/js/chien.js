var Chien = {
    init : function (nom,race,taille) {
        this.nom = nom;
        this.race = race;
        this.taille = taille;   
    },
    aboyer : function () {
        var cri;
        switch (this.race ) {
            case "mâtin de Naples" :
            cri = "Grr ! Grr !"
            break;
            case "bichon" :
            cri = "Kai ! Kai !"
            break; 
    } return cri;  
},
    }

var crockdur = Object.create(Chien);
crockdur.init("Crockdur","mâtin de Naples",75);
console.log(crockdur.nom + " est un " + crockdur.race + " mesurant " + crockdur.taille + " cm");
console.log("Tiens, un chat ! " + crockdur.nom + " aboie : " + crockdur.aboyer());

var pupuce = Object.create(Chien);
pupuce.init("Pupuce","bichon",22);
console.log(pupuce.nom + " est un " + pupuce.race + " mesurant " + pupuce.taille + " cm");
console.log("Tiens, un chat ! " + pupuce.nom + " aboie : " + pupuce.aboyer());