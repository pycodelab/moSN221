var compteBancaire = {
    titulaire : "Mohamed",
    solde : 0,
    //pour créditer le compte
    crediter : function (depot) {
        this.solde = this.solde + depot;
        return this.solde;
    },
    //pour débiter le compte
    debiter : function (debit) {
        this.solde = this.solde - debit;
        return this.solde;
    },
    //description du compte
    decrire : function () {
        var description = "Le titulaire de ce compte est " + this.titulaire + ". Le solde du compte est : "+ this.solde + " euros.";
        return description;
    }
}

//solde de départ
console.log(compteBancaire.decrire());

//depot de 5O euros
compteBancaire.crediter(50);
console.log(compteBancaire.decrire());

//retrait de 20 euros
compteBancaire.debiter(20);
console.log(compteBancaire.decrire());