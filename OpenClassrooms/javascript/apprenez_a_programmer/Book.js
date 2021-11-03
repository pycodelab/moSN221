//création de la class Book
class Book {
    constructor(titre,author,description,pages,currentPage) {
        this.titre = titre;
        this.author = author;
        this.description = description;
        this.pages = pages;
        this.currentPage = currentPage;
        this.read = false; 
    }

//pour savoir si le livre est lu ou pas et gestion d'erreur
  readBook () { 
    if (this.currentPage < 1 || this.currentPage > this.pages) {
          return 0;
        
      }
    if (this.currentPage >= 1 && this.currentPage < this.pages) {
        return 1;
        }
    if (this.pages == this.currentPage) {
        this.read = true;
        return 1;
    }
  }  
    
// affichage des messages
    affichage () {
        this.readBook();
        if (this.read==true) {
            console.log("Vous avez déjà lu "+this.titre);
        }
        if (this.read == false) {
            if (this.readBook()== 1) {
            console.log("vous n'avez pas encore fini de lire "+this.titre);
            }
        
            else /*if (this.readBook()==0)*/ {
            console.log("erreur : vous avez lu plus de pages que le nombre de pages du livre");
        }
        
        }
            
        }
}


// Création de 3 livres
let MadalKhabiru = new Book("Madalkhabiru","CheikhoulKhadim","khassaides",12,5);
let TaawuduSighar = new Book("TazzawuduSighar","Khadimassoul","XamXam",280,280);
let Tere = new Book("tourouTerebi","kikobind","gestu",170,200);

// Insertion des livres dans un tableau

const books = [];

books.push = MadalKhabiru;
books.push = TaawuduSighar;
books.push= Tere;


// Affichages et tests
TaawuduSighar.affichage();
//console.log(MadalKhabiru.readBook());
//console.log(MadalKhabiru.read);
MadalKhabiru.affichage();
//console.log(Tere.readBook());
//console.log(Tere.read);
Tere.affichage();
