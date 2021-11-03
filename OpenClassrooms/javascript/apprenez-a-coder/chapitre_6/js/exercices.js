//Information sur le mot
var mot=prompt("entrez un mot");
nbCaracteres = mot.length;
motEnMajuscules=mot.toUpperCase();//Ecriture en majuscules
motEnMinuscules=mot.toLowerCase();//Ecriture en minuscules
console.log("Le mot "+ mot+ " contient "+ nbCaracteres+ " caractére(s).");
console.log("Il s'écrit en minuscules : "+motEnMinuscules);
console.log("Il s'écrit en majuscules : "+motEnMajuscules);

//Comptage du nombre de voyelles
function compterNbVoyelles (motUtilisateur) {
    var nbVoyelles=0;
    for (i=0;i<motUtilisateur.length;i++) {
        switch (motUtilisateur[i].toLowerCase()){
            case "a":
            nbVoyelles++
            break;
            case "o":
            nbVoyelles++
            break;
            case "u":
            nbVoyelles++
            break;
            case "i":
            nbVoyelles++
            break;
            case "e":
            nbVoyelles++
            break;
            case "é":
            nbVoyelles++
            break;
            case "è":
            nbVoyelles++
            break;
            case "ê":
            nbVoyelles++
            break;
            default:
            nbVoyelles=nbVoyelles
        }    
    }
return nbVoyelles;           
}

function inverser(motUtilisateur) {
    var i=0;
    var motInverse=" ";
    var caractereSuivant;
    var numeroCaractere;
    while (i<motUtilisateur.length) {
        numeroCaractere=motUtilisateur.length - i-1;//indice du caractère depuis la fin
        caractereSuivant=motUtilisateur[numeroCaractere];//lettre correspondant à cet indice
        motInverse=motInverse+caractereSuivant;//Ecriture du mot inversé
        i++;
    }
    return motInverse;
}

function palindrome(motUtilisateur) {
   var inverse=inverser(motUtilisateur);
    if (inverse===motUtilisateur) {
     var  message = console.log(motUtilisateur+ " est un palindrome")
    }
    else {
     var message = console.log(motUtilisateur+ " n'est pas un palindrome")
    }
   return message; 
}

function trouverLettreLeek(lettre){
    var leet;
       switch (lettre.toLowerCase()) {
           case "a" :
           leet=String(4)
           break;
           case "b" :
           leet=String(8)
           break;
           case "e" :
           leet=String(3)
           break;
           case "l" :
           leet=String(1)
           break;
           case "o" :
           leet=String(0)
           break;
           case "s" :
           leet=String(5)
           break;
           default:
            leet=lettre   
       }
    return leet;
    } 

function convertirLeek(motUtilisateur){
    var motConverti="";
    for (i=0; i<motUtilisateur.length;i++) {
        motConverti=motConverti+trouverLettreLeek(motUtilisateur[i]);
    }
    return console.log(motUtilisateur+ " en langage leet donne "+motConverti);
}

console.log("Il contient "+ compterNbVoyelles(mot) + " voyelle(s).");
console.log("Il s'écrit à l'envers :"+inverser(mot));
palindrome(mot);
convertirLeek(mot);



