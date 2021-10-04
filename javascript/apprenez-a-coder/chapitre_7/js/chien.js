var chien = {
    nom : "Crockdur",
    race : "mâtin de Naples",
    taille : 75,
    aboyer: function () {
        var cri = "Grr ! Grr !";
        return cri;  
    }   
}
console.log(chien.nom + " est un " + chien.race + " mesurant " + chien.taille + " cm");
console.log("Tiens, un chat ! "+ chien.nom+ " aboie : " + chien.aboyer());