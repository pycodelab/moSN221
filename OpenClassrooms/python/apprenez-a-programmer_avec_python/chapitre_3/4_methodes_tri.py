import os

"""Première approche du tri"""

prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]

prenoms.sort() #modifie la liste prenoms

"""Avec la fonction sorted"""

autrePrenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]

sorted(autrePrenoms) #retourne une nouvelle liste et ne modifie pas la liste de départ

sorted([1,8,-2,15,9]) 
#on veut trier des entiers
#retourne [-2, 1, 8, 9, 15] : tri croissant

sorted(["1","8","-2","15","9"])
#on veut trier des chaines de caractères
#retourne ["-2","1","15","8","9"] : tri alphabétique

#"sorted([1,"8","-2","15",9])"
#retourne une erreur car on veut trier des objets de type différents et Python ne sait pas quelle méthode choisir



"""Trier avec des clés précises"""
etudiants = [
    ("Clément",14,16),
    ("Charles",12,15),
    ("Oriane",14,18),
    ("Thomas",11,12),
    ("Damien",12,15),
]

sorted(etudiants)
#retourne la liste classée selon la première colonne
#charles,clément,damien,oriane, thomas

"pour changer selon une autre colonne, on utilise les fonctions lambda"

doubler = lambda x:x*2
doubler
doubler (8)

"Tri selon la deuxième colonne"
lambda colonnes: colonnes[2]
tri_colonne_2 = sorted(etudiants,key=lambda colonnes:colonnes[2])

print(tri_colonne_2)


"""Tirer une liste d'objets"""
class Etudiant:
    """Classe représentant un étudiant.
    On représente un étudiant par son prénom (attribut prenom), son âge (attribut âge) et sa note moyenne (attribut moyenne, entre 0 et 20)
    
    Paramètres du constructeur :
    prenom -- le prénom de l'étudiant
    age -- l'âge de l'étudiant
    moyenne -- la moyenne de l'étudiant """
    
    def __init__(self,prenom,age,moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne
        
    def __repr__(self):
        return "<Etudiant {} (âge = {}, moyenne = {})>".format(self.prenom, self.age,self.moyenne)
    
"on recrée la liste"
etudiants = [
    Etudiant("Clément",14,16),
    Etudiant("Charles",12,15),
    Etudiant("Oriane",14,18),
    Etudiant("Thomas",12,12),
    Etudiant("Damien",15,15)
]

"on pourrait utiliser la méthode __lt__ (lower than) pour comparer les différents éléments et faire le tri ou utiliser l'argument key"

listeTriee = sorted(etudiants, key=lambda etudiant: etudiant.moyenne)

print(listeTriee)


"""Trier dans l'ordre inverse"""
listeInversee = sorted(etudiants, key=lambda etudiant: etudiant.age, reverse=True)

print(listeInversee)


"""Utilisation du module operator"""
"Trier une liste de tuples"

etudiants = [   
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

"methode 1"
sorted(etudiants, key=lambda etudiant: etudiant[2])

"methode 2"
from operator import itemgetter
sorted(etudiants, key=itemgetter(2))

"Trier une liste d'objets"
etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]
from operator import attrgetter
sorted(etudiants, key=attrgetter("moyenne")) #le calcul se fait sur un attribut de l'objet, ici moyenne au lieu d'un tuple


"""Trier selon plusieurs critères"""
from operator import attrgetter
sorted(etudiants, key=attrgetter("age","moyenne"))

"""Chainage de tris"""

class LigneInventaire:
    
    """Classe représentant une ligne d'un inventaire de vente
    
    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit"""
    
    def __init__(self,produit,prix,quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite
    
    def __repr__(self):
        return "<Ligne d'inventaire {} ({}x{})>".format(self.produit,self.prix,self.quantite)

#Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge",1.2,19),
    LigneInventaire("orange",1.4,24),
    LigneInventaire("banane",0.9,21),
    LigneInventaire("poire",1.2,24),
]
    
"Trier par prix et par quantité"
from operator import attrgetter
inventaireTriee=sorted(inventaire,key=attrgetter("prix","quantite"))

print(inventaireTriee)

"trier selon deux critères"
Test1=sorted(inventaire,key=attrgetter("quantite"),reverse=True) 
test1 = sorted(Test1,key=attrgetter("prix"))
    

Test2 = sorted(inventaire,key=attrgetter("prix"))  
test2=sorted(inventaire,key=attrgetter("quantite"),reverse=True)    

"""Mais si vous voulez trier par prix croissant et par quantité décroissante ? C'est-à-dire qu'on veut trier par prix croissant, mais que si deux lignes d'inventaires ont le même prix, alors on trie dans l'ordre décroissant de quantité ?

Le plus simple ici est de faire deux tris en utilisant la propriété de stabilité. La subtilité, c'est que l'on va trier d'abord par notre second critère et ensuite par notre premier. Ici, nous allons donc trier d'abord par ordre décroissant de quantité, puis ensuite par ordre croissant de prix."""
os.system("pause")