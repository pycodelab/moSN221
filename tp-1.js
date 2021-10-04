nombre = parseInt(prompt("saisir un nombre"));
 function saisie () {
        if (nombre && nombre>0 && nombre <=999) {
            console.log ("saisie correcte");
        }
        
     
     
     else {
            console.log("saisie incorrecte");
        }
     return nombre;
        }

var centaine, dizaine, unites;
var lettreCentaine, lettreDizaine, lettreUnites


function decomposition () {
    if (saisie correcte)
    centaine = parseInt(nombre/100);
    dizaine = parseInt((nombre%100)/10);
    unites = parseInt((nombre%100)%10);
    console.log(centaine);
    console.log(dizaine);
    console.log(unites);
}



saisie();
decomposition();