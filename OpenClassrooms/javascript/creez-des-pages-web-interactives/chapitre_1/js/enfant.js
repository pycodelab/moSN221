/*
Exercice : afficher l'enfant d'un objet du DOM
*/

//  Affiche un enfant d'un objet du DOM
//  Le paramètre noeud est l'objet du DOM
//  Le paramètre indice est l'indice de l'enfant à afficher

function afficherEnfant(noeud,indice) {
    if (noeud.childNodes[0]) {
        if (indice < 0 || indice >= noeud.childNodes.length) {
        console.error("Indice incorrect");  
        }
        else {
            //(noeud.childNodes[indice].nodeType === document.ELEMENT_NODE) {
            console.log(noeud.childNodes[indice]);
        
        }
    }
    
    else {
        console.error("Le noeud ne possède pas d'enfants.");
        }    
    
}

afficherEnfant(document.body,1);
afficherEnfant(document.body,-1);
afficherEnfant(document.body,8);
afficherEnfant(document.body.childNodes[0],0);