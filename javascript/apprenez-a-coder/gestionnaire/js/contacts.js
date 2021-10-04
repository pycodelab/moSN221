/* 
Activité : gestion des contacts
*/

// TODO : complétez le programme
console.log("Bienvenue dans votre gestionnaire de contacts");

// Definition d'un objet pour l'affichage du menu
var menu = {
    initMenu : function (numero,intitule) {
        this.numero = numero;
        this.intitule = intitule;
    },
    decrireMenu : function () {
        console.log(this.numero + " : " + this.intitule);
    },
};

// Definition d'un objet pour gérer les détails du contact
var contact = {
    nouveauContact : function (prenom,nom) {
        this.prenom = prenom;
        this.nom = nom;
    },
    decrireContact : function () {
        var description = "prenom : " + this.prenom + " / nom : " + this.nom;
        return description
    },
};

// Description et affichage du menu
option1 = Object.create(menu);
option1.initMenu(1,"Liste des contacts");
option2 = Object.create(menu);
option2.initMenu(2,"Ajouter un nouveau contact");
option3 = Object.create(menu);
option3.initMenu(0, "Quitter");

var Menu = [];
Menu.push(option1);
Menu.push(option2);
Menu.push(option3);

Menu.forEach(function (choix) {
    choix.decrireMenu();
});

//Les premiers contacts
var contact1 = Object.create(contact);
var contact2 = Object.create(contact);
var contact3 = Object.create(contact);
contact1.nouveauContact("Didier","Drogba");
contact2.nouveauContact("Frank","Lampard");
contact3.nouveauContact("John","Terry");

var Contacts =[];
Contacts.push(contact1);
Contacts.push(contact2);
Contacts.push(contact3);

//Boucles 
var choixUtilisateur = Number(prompt("Choisissez une option"));

while (choixUtilisateur !==0) {
    if (choixUtilisateur === 1) {
        console.log("Voici la liste des contacts");
        Contacts.forEach(function (contact) {
            console.log(contact.decrireContact());
        });//Affichage de la liste de contacts
        console.log(" "); // Saut de ligne
        Menu.forEach(function (choix) {
        choix.decrireMenu();
        }); // Affichage du menu
        choixUtilisateur = Number(prompt("Choisissez une option"));
         }
    
    else if (choixUtilisateur ===2) {
        console.log("Ajout d'un nouveau contact");
        var newContact = Object.create(contact);
        nouveauPrenom = prompt("Entrez le prenom du nouveau contact");
        nouveauNom = prompt("Entrez le nom du nouveau contact");
        newContact.nouveauContact(nouveauPrenom,nouveauNom);//Création du nouveau contact
        Contacts.push(newContact);//Ajout d'un nouveau contact dans le tableau
        console.log("Un nouveau contact a été ajouté !")
        console.log(" "); // Saut de ligne
        Menu.forEach(function (choix) {
        choix.decrireMenu();//Affichage du menu
        }); // Affichage du menu
        choixUtilisateur = Number(prompt("Choisissez une option"));
    }
};

// Quitter le gestionnaire
if (choixUtilisateur === 0) {
    console.log("Vous quittez le gestionnaire de contacts. A bientôt")
};

