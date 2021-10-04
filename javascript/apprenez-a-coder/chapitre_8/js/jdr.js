var Personnage = {
    //Initialise le personnage
    initPerso: function (nom, sante, force, piece, cle) {
        this.nom = nom;
        this.sante = sante;
        this.force = force;    
    },
    inventairePerso : function (piece, cle) {
        this.piece = piece;
        this.cle = cle;
    },
    //Attaque d'un personnage cible
    attaquer: function (cible) {
        var degats = this.force
        if (this.sante>0) {
            console.log(this.nom + " attaque " + cible.nom + " et lui fait " + degats + " points de degats");
            cible.sante = cible.sante - degats;
            if (cible.sante>0) {
                console.log(cible.nom + " a encore " + cible.sante + " points de vie");
            }
            else {
                cible.sante =0;
                console.log(cible.nom + " est mort.")
            }
        }
        else {
                console.log (this.nom + " est déjà mort, il ne peut pas attaquer " + cible.nom)
            }
        }
    };

var Joueur = Object.create(Personnage);
//Initialise le joueur
Joueur.initJoueur = function(nom,sante,force) {
    this.initPerso(nom,sante,force);
    this.xp = 0; //L'expérience du joueur est toujours initialisée à 0
    this.inventairePerso (10,1);
};

Joueur.decrire = function () {
    var description = this.nom + " a " + this.sante + " points de vie, " + this.force + " en force, " + this.xp + " points d'expérience, " + this.piece + " pièces et " + this.cle + " clé(s).";
    return description;
};
//joueur combat un adversaire
Joueur.combattre = function(adversaire) {
    this.attaquer(adversaire);
    if (adversaire.sante ===0) {
        console.log(this.nom + " a tué " + adversaire.nom + " gagne " + adversaire.valeur + " points d'expérience, " + adversaire.piece + " pièces d'or et " + adversaire.cle + " clé(s).");
        this.xp = this.xp + adversaire.valeur;
        this.cle = this.cle + adversaire.cle;
        this.piece = this.piece + adversaire.piece;
    }
};

var Adversaire = Object.create(Personnage);
//Initalise l'adversaire
Adversaire.initAdversaire = function (nom, sante, force, race, valeur) {
    this.initPerso(nom, sante, force);
    this.race = race;
    this.valeur = valeur;
    this.inventairePerso (10,1);
};

var joueur1 = Object.create(Joueur);
joueur1.initJoueur("Aurora",150,25);

var joueur2 = Object.create(Joueur);
joueur2.initJoueur("Glacius",130,30);

console.log("Bienvenue dans ce jeu d'aventure ! Voici nos courageux héros");
console.log(joueur1.decrire());
console.log(joueur2.decrire());

var monstre = Object.create(Adversaire);
monstre.initAdversaire("ZogZog",40,20,"orc",10);

console.log("Un affreux monstre arrive : c'est un " + monstre.race + " nommé " + monstre.nom);

monstre.attaquer(joueur1);
monstre.attaquer(joueur2);

joueur1.combattre(monstre);
joueur2.combattre(monstre);

console.log(joueur1.decrire());
console.log(joueur2.decrire());
