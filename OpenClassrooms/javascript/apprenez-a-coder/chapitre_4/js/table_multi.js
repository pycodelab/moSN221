var nombre=Number(prompt("entrez un nombre entre 2 et 9"))
if (nombre>=2 && nombre<=9) {
for (i=1;i<=10;i++) {
    var produit=nombre*i;
    console.log( nombre+ " x "+i+ " = "+ produit)
}
}
else {
    console.log("erreur de saisie")
}