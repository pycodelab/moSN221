var nombre = prompt("Entrez votre moyenne");
var moyenne = Number(nombre);
if (moyenne>=10){
    if (moyenne<=12) {
        console.log("vous êtes reçu !!!")
    }
    else {
        console.log("vous êtes reçu avec mention !!!")
    }
}
else {
   console.log("vous êtes recalé")
}
