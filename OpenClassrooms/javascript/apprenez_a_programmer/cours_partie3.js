
let i=0;
let resultat =0;

const moyenne = (note) => {
    if (note.length ==0) {
        return 0;
    }
 while (i<note.length) {
  resultat=resultat+note[i];
        i++;
    }
    return resultat/note.length;
}

/*let notes = [5,6,8,7,14,9,17,35];
let noteVide = [];
const taMoyenne = moyenne(notes);
console.log(taMoyenne);
console.log(moyenne(noteVide));*/

class Show {
    constructor() {
    this.ratings =[];
    this.averageRatings = 0;
    }
    addRating (notation) {
        if (notation <=5 && notation >= 0) {
            this.ratings.push (notation);
            this.averageRatings = moyenne(this.ratings);
            }
        else {
            console.log("Erreur de saisie")
        }
    }

}

let SaaNexx = new Show();
SaaNexx.addRating(-3);
SaaNexx.addRating(5);
SaaNexx.addRating(2);
SaaNexx.addRating(1.5);
SaaNexx.addRating(3.7);
console.log ("Les notes obtenues par ce film sont : ")
for (i=0; i<SaaNexx.ratings.length; i++) {
    console.log(SaaNexx.ratings[i]);
}
console.log("La note moyenne obtenue par ce film est "+SaaNexx.averageRatings+" .");


    
