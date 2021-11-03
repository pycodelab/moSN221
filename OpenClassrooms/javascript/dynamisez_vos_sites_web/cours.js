/*var age = parseInt(prompt("veuillez entrer votre age"));
if (age) {
    if (age > 1 && age <=17) {
        alert("Vous n'etes pas encore majeur");
    }
    else if (age > 17 && age <=49) {
        alert("Vous etes pas majeur mais pas encore senior");
    }
    else if (age > 49 && age <=59) {
        alert("Vous etes senior mais pas encore retraité");
    }
    else if (age > 59 && age <=120) {
        alert("Vous êtes retraité, profitez de vore temps libre !");
    }
    else if (age <= 0) {
        alert("Vous n'êtes pas encore né");
    }
    
    else if (age>120) {
        alert("Yalla nga goude fane ak wer");
    }
    }
else {
    alert("Vous n'avez pas saisi de nombre");
}*/

/*var message = prompt("entrez votre texte") 
while (!message) {
    message = prompt("réessayer");
}

alert (message);*/

function asknumber(){
var nombre = parseInt(prompt("entrez un nombre"));
while (isNaN(nombre)) {
    nombre = parseInt(prompt("réessayez"));
}
    return nombre;
}
alert ("Le nombre est : "+asknumber());