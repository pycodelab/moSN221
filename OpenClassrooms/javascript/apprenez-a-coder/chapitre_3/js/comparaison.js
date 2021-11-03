var valeur1 = prompt("Entrez un nombre");
var valeur2 = prompt("Entrez un nombre");
var nombre1=Number(valeur1);
var nombre2=Number(valeur2);
if (valeur1 !== valeur2) {
    if (valeur1>valeur2) {
       console.log(valeur1 + " est supérieur à " + valeur2)
   }
    else {
        console.log(valeur1 + " est inférieur à " + valeur2)
    }
}
else{
    console.log(valeur1 + " est égal à " + valeur2)
}
        
