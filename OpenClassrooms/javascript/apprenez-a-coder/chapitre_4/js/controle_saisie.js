var nombre=Number(prompt("entrez un nombre"))
while (nombre>=100 || nombre<=50) {
    console.log("corrigez votre saisie")
    nombre = Number(prompt("entrez un nombre"))
}
if (nombre<100 && nombre>50){
    console.log("bingo !");
}