/* 
Activité : gestion des contacts
*/

// TODO : complétez le programme

// Objet Contact
var Contact = {
    init: function (prenom, nom) {
        this.nom = nom;
        this.prenom = prenom;
    }
};

var contacts = []; //tableau de contacts

// Fonction Ajout d'un contact
var ajoutContact = function (prenom, nom) {
    var contact = Object.create(Contact);
    contact.init(prenom, nom);
    contacts.push(contact);
};

// Fonction Affichage des options
var affOption = function () {
    console.log("1 : Lister les contacts");
    console.log("2 : Ajouter un contact");
    console.log("0 : Quitter");
    optionSaisi = prompt("Choisissez une option :");
    return optionSaisi;
};


// Fonction Affichage des contacts
var affContact = function () {
    console.log("Voici la liste de tous vos contacts :");
    contacts.forEach(function (contact) {
        console.log("Nom : " + contact.nom + ", prénom : " + contact.prenom);
    })
}

// Fonction Gestion des options
var gestOption = function (option) {
    switch (option) {
        case "1":
            affContact();
            console.log("\n");
            break;
        case "2":
            var nom = prompt("Nom du nouveau contact:");
            var prenom = prompt("Prénom du nouveau contact :");
            ajoutContact(prenom, nom);
            console.log("Le nouveau contact a été enregistré.");
            console.log("\n");
            break;
        default:
            console.log("Je n'ai pas compris.");
            console.log("\n");
            break;
    }
};

// Initialisation programme
var optionSaisi;
ajoutContact("Carole", "Lévisse");
ajoutContact("Mélodie", "Nelsonne");
console.log("Bienvenue dans le gestionnaire des contacts.");
optionSaisi = affOption();  // Affiche les options pour l'utilisateur et son choix

// Demande de l'option sélectionnée tant que l'utilisateur ne tape pas 0
while (optionSaisi !== "0") {
    gestOption(optionSaisi);
    optionSaisi = affOption();
};

// Fin du programme
console.log("\nAu revoir !");
