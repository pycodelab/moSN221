var nombre_manege = Number(prompt("combien de tours souhaitez-vous faire ?"));
if (nombre_manege<0) {
    console.log("erreur de saisie")
}
if (nombre_manege===0) {
    console.log("vous ne souhaitez pas faire de tours")
}
else {
    var i =1;
  while (i<=nombre_manege) {
    console.log("c'est le tour numéro " +i)
    i++;  
}  
}

