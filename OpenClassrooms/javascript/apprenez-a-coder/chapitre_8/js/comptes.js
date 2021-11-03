var compte = {
    initCB : function (nom,solde) {
        this.nom = nom;
        this.solde = solde;
    
},
    debiter : function (montant) {
        this.solde = this.solde - montant;
        return this.solde;
    },
    crediter : function (montant) {
        this.solde = this.solde + montant
    },
    decrire : function () {
        var description = "Titulaire : " + this.nom + " , Solde : " + this.solde + " euros.";
        return description;
    },
};

var compteBancaire = Object.create(compte);
var compteEpargne = Object.create(compte);
compteEpargne.initCE = function (nom,solde,taux) {
    compteEpargne.initCB(nom,solde);
    compteEpargne.taux = taux;  
};
compteEpargne.ajouterInterets = function () {
    this.solde = (this.solde*this.taux)+this.solde;
};
var compte1 = Object.create(compteBancaire);
compte1.initCB("Alex",100);
var compte2 = Object.create(compteEpargne);
compte2.initCE("Marco", 50, 0.05);

console.log("Etat initial des comptes :");
console.log(compte1.decrire());
console.log(compte2.decrire());

var montant = Number(prompt("Entrez le montant à transférer entre les comptes en euros."));
compte1.debiter(montant);
compte2.crediter(montant);

compte2.ajouterInterets();

//Afficher le bilan des comptes
console.log("Voici l'état final des comptes");
console.log(compte1.decrire());
console.log(compte2.decrire());



