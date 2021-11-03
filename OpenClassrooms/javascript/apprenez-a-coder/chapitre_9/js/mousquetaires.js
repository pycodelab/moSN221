var mousquetaire = ["Athos","Porthos","Aramis"];//Création du tableau
for (var i =0;i<mousquetaire.length;i++) {
    console.log(mousquetaire[i]);
};
mousquetaire.push ("d'Artagnan");

console.log("A présent ils sont quatre mousquetaires :")
mousquetaire.forEach(function (film) {
    console.log(film);
});