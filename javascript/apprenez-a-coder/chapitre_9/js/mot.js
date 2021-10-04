var tableauMots = [];

var mot = prompt("Entrez un mot");
var i = -1;


while (mot.toLowerCase() !== "stop") {
    i++;
    tableauMots.push(mot);
    mot = prompt("Entrez un nouveau mot");
};

if (mot.toLowerCase() === "stop") {
    tableauMots.push("stop");
};

console.log("stop ! voici la liste des mots que vous avez saisis :");
tableauMots.forEach(function (mot) {
                 console.log(mot);   
 });