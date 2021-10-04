motDePasse1 = document.getElementById("mdp1").value;
motDePasse2 = document.getElementById("mdp2").value;

document.querySelector("form").addEventListener("submit", function (e) {
    motDePasse1 = document.getElementById("mdp1").value;
    motDePasse2 = document.getElementById("mdp2").value;
    regexMotDePasse = /.+[0-9]/;
    if ((motDePasse1.length >=6) && (motDePasse1==motDePasse2) && (regexMotDePasse.test(motDePasse1))) {
        
        document.getElementById("infoMdp").textContent = "Mot de passe valide";
    }
    else if (motDePasse1.length<=6) {
        document.getElementById("infoMdp").textContent = "Erreur : la longueur minimale du mot de passe est de 6 caractères";
    }
    else if (!regexMotDePasse.test(motDePasse1)) {
            document.getElementById("infoMdp").textContent = "Le mot de passe est trop faible"; 
    }
    else if (!(motDePasse1==motDePasse2)) {
        document.getElementById("infoMdp").textContent = "Les deux mots de passe sont différents";
    }
    e.preventDefault(); // Annulation de l'envoi des données
});