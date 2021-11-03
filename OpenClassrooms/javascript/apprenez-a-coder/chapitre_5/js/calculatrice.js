function calculer(x1,p,x2) {
    switch (p) {
        case "+" :
            resultat=x1+x2
            break;
        case "-" :
            resultat=x1-x2
            break;
        case "*" :
            resultat=x1*x2
            break;
        case "/":
            resultat=x1/x2
            break;
        default :
            resultat="inconnu"        
        
    }
    return resultat;
}

console.log(calculer(4,"+",6));
console.log(calculer(4,"-",6));
console.log(calculer(2,"*",0));
console.log(calculer(12,"/",0));
console.log(calculer(2,"rien",2));