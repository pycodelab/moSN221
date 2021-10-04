//ecrire la fonction compterElements

function compterElements(selecteur) {
    
    return document.querySelectorAll(selecteur).length;
    
}

console.log(compterElements("p"));
//console.log(document.querySelectorAll(".adjectif").length);
console.log(compterElements(".adjectif"));
console.log(compterElements("p .adjectif"));
console.log(compterElements("p > .adjectif"));