var mois = Number(prompt("saisir un numéro de mois"));
if (mois>12 || mois<1){
    console.log("erreur de saisie")
}
else{
   switch (mois) {
       case 1:
       case 3:
       case 5:
       case 7:
       case 8:
       case 10:
       case 12:
           console.log("ce mois compte 31 jours")
           break;
       case 4:
       case 6:
       case 9:
       case 11:
           console.log("ce mois compte 30 jours")
           break;
       default:
           console.log("février compte 28 jours")
   }
}