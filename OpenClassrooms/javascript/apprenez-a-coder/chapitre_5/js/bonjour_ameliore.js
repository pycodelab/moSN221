function direBonjour(prenom,nom) {
    var message = "Bonjour, " + prenom + " " + nom + " !";
    return message
}
nomUtilisateur=prompt("entrez votre nom");
prenomUtilisateur=prompt("entrez votre prenom");
console.log(direBonjour(prenomUtilisateur,nomUtilisateur));