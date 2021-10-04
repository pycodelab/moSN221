function perimetre(rayon) {
    resultat=2*Math.PI*rayon;
    return resultat;
}
function aire(rayon) {
    resultat=Math.PI*rayon**2;
    return resultat;
}

rayonUtilisateur=prompt("saisir une valeur en m");
console.log("le périmètre d'un cercle de rayon "+rayonUtilisateur+ " est "+ " " + perimetre(rayonUtilisateur)+"m");
console.log("l'aire d'un cercle de rayon "+rayonUtilisateur+ " est "+ " " + aire(rayonUtilisateur)+"m²");