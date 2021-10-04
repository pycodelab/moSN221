from os import *

#convertir une chaine en liste
ma_chaine = "Bonjour à tous"
print(ma_chaine.split(" "))

#convertir une liste en chaine
ma_liste = ['Bonjour','à','tous']
print("".join(ma_liste))

def afficher_flottant (flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaine de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.
    De plus, on va remplacer le point décimal par la virgule."""
    
    if type(flottant) is not float :
        print("erreur : le nombre saisi n'est pas un décimal")
    else :
        chaine_flottant = str(flottant)
        partie_entiere, partie_decimale = chaine_flottant.split(".")
        partie_arrondie = partie_decimale[0:3]
        #print(partie_entiere)
        #print(partie_arrondie)
        print(",".join([partie_entiere,partie_arrondie]))


afficher_flottant(5)
afficher_flottant(3.999998)
afficher_flottant(1.5)

#Les fonctions dont on ne connait pas le nombre de paramètres
def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
    
    print("J'ai reçu :{}.".format(parametres))

fonction_inconnue()
fonction_inconnue(33)
fonction_inconnue('a','e','f')
var = 3.5
fonction_inconnue(var,[4], "...")

#def fonction_inconnue(nom,prenom,*commentaires):
#def print(*values,sep=' ',end='\n',file=sys.stdout):

def afficher(*parametres,sep=' ',fin='\n'):
    #convertir les tuples en listes
    parametres = list(parametres)
    #convertir les parametres en chaines de caractères
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    #construction de la solution sous forme de liste
    parametres_sep=sep.join(parametres)
    print(parametres_sep+fin)

afficher(125,78,'tabaski',85,sep=' ',fin='\n')

#Transformer une liste en paramètre de fonction
liste_des_parametres = [1,4,9,16,25,36]
print(*liste_des_parametres)

#Les comprehensions de liste
liste_origine = [0,1,2,3,4,5]
liste_carree=[nb*nb for nb in liste_origine]
print(liste_carree)

#filtrage
liste_origine=[1,2,3,4,5,6,7,8,9,10]
liste_paire = [nb for nb in liste_origine if nb%2 ==0]
print(liste_paire)

qtt_a_retirer = 7 #on retire chaque semaine 7 fruits de chaque sorte
fruits_stockes=[15,3,18,21] #Par exemple 15 pommes, 3 melons, ...
fruits_restants=[nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits>qtt_a_retirer]

print(fruits_restants)

#Nouvelle application concrète
inventaire = [
    ("pommes",22),
    ("melons",4),
    ("poires",18),
    ("fraises",76),
    ("prunes",51),
]

print(inventaire)
#Objectif : trier la liste en fonction de la quantité de fruit
#On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt,nom_fruit) for nom_fruit,qtt in inventaire]
print(inventaire_inverse)
#On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé
#On reconstitue l'inventaire trié
inventaire = [(nom_fruit,qtt) for qtt,nom_fruit in sorted(inventaire_inverse,reverse=True)]

#2e méthode
inventaire_inverse = [(qtt,nom_fruit) for nom_fruit,qtt in inventaire]

inventaire_inverse.sort(reverse=True)
print(inventaire_inverse)

inventaire = [(nom_fruit,qtt) for qtt,nom_fruit in inventaire_inverse]

print(inventaire)

system("pause")