console.log("Bienvenue dans ce jeu de devinette !");

// Cette ligne génère aléatoirement un nombre entre 1 et 100
//var solution = Math.floor(Math.random() * 100) + 1;
//var solution = 91;
var solution = Math.floor(Math.random() * 100) + 1;

// Décommentez temporairement cette ligne pour mieux vérifier le programme
//console.log("(La solution est " + solution + ")");

var proposition = Number(prompt("Entrez votre proposition"));
var i=1;
while ((solution!==proposition)&&i<=5) {
        while ((solution>proposition) && (i<=5)) {
            console.log(proposition + " est trop petit");
            proposition = Number(prompt("Entrez votre proposition"));
            i++;
        }
        while ((solution<proposition) && (i<=5)){
            console.log(proposition + " est trop grand");
            proposition = Number(prompt("Entrez votre proposition"));
            i++; 
        }
}
if ((solution===proposition) && i<=6) {
        console.log("Bravo la réponse était " + proposition);
        console.log("vous avez trouvé après " + i+ " essai(s)");
}
if ((solution!==proposition) && i===6) {
    console.log("perdu ! La solution était " + solution);
}
        

            