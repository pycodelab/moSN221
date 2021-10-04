var ajout = {
  // initialise les attributs du liste
    init: function (nom, prenom) {
        this.nom = nom;
        this.prenom = prenom;
    },
    decrire: function () {
        return "nom : " + this.nom + ", prenom : " + this.prenom;
    }
};

var nom1 = Object.create(ajout);
nom1.init("Carole", "Lévisse");

var nom2 = Object.create(ajout);
nom2.init("Mélodie", "Nelsonne");

var contact = [];
contact.push(nom1);
contact.push(nom2);

var liste;

while(liste!=="0")
    {
    console.log("1 : lister les contacts");
    console.log("2 : Ajouter un contact");
    console.log("0 : Quitter");
    var liste = prompt("choisissez une obtion")

    if (liste==1)
    {
        console.log("");
        console.log("Voici la liste de tous vos contact :");
        contact.forEach(function (contacts) {
        console.log(contacts.decrire());
        });
    }

        else if(liste==2)
        {
            var nom = prompt("nom :");
            var prenom = prompt("prenom :");
            var contacts = Object.create(ajout);
            contacts.init(nom, prenom);
            contact.push(contacts);
            console.log("Le nouveau contact a été ajouté");
        }
  console.log();
}

console.log("Au revoir !");
