from os import *

ma_liste = list() #on crée une liste vide
ma_liste = [] #on crée une liste vide
print(type(ma_liste))
print(ma_liste)

ma_liste = [1,2,3,4,5] #Une liste avec cinq objets
print(ma_liste)

ma_liste = [1,3.5,"une chaine", []]
print(ma_liste)

ma_liste = ['c','f','m']
print(ma_liste)
print(ma_liste[0]) #On accède au premier de la liste
print(ma_liste[2]) #3e élément
ma_liste[1] = 'Z' #On remplace 'f' par 'Z'

print(ma_liste)

ma_liste = [1,2,3]
ma_liste.append(29)
print(ma_liste)

#Pour les chaines de caractères
chaine1 = "une petite phrase"
chaine2 = chaine1.upper() #On met en majuscules chaine1
print(chaine1)            #On affiche la chaine d'origine, elle n'a pas été modifiée par la méthode upper

print(chaine2) #On affiche chaine2, c'est une chaine2 qui contient la chaine en majuscules

#Pour les listes à présent
liste1 = [1,5.5,18]
liste2 = liste1.append(-15) #on ajoute -15 à liste1
print(liste1) #Cette fois, l'appel de la méthode a été modifié l'objet d'origine (liste1)

print(liste2) #On obtient rien : None

ma_liste = ['a', 'b', 'd', 'e']
ma_liste.insert(2,'c') #On insère 'c' à l'indice 2
print(ma_liste)

ma_liste1 = [3,4,5]
ma_liste2 = [8,9,10]
ma_liste1.extend(ma_liste2) #On insère ma_liste2 à la fin de ma_liste1
print(ma_liste1)
ma_liste1 = [3,4,5]
print(ma_liste1 + ma_liste2)
print(ma_liste1)
#print(ma_liste1 += ma_liste2) #Identique à extend
#print(ma_liste1)

#del
variable = 34
del variable
#print(variable) #variable not defined

ma_liste = [-5,-2,1,4,7,10]
del ma_liste[0] #On supprime le premier élément de la liste
print(ma_liste)
del ma_liste[2] #On supprime le troisième élément de la liste
print(ma_liste)

#remove
ma_liste = [31,32,33,34,35]
ma_liste.remove(32)
print(ma_liste)

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h']
i = 0 #Notre indice pour la boucle while
while i<len(ma_liste):
    print(ma_liste[i])
    i+=1 #On incrémente i, ne pas oublier !

#Cette méthode est cependant préférable
for elt in ma_liste : #elt va prendre les valeurs successives des éléments de ma_liste
    print(elt)

#Enumerate
for i, elt in enumerate(ma_liste):
    print("A l'indice {} se trouve {}.".format(i,elt))

for elt in enumerate(ma_liste):
    print(elt)

autre_liste = [(1,'a'),(4,'d'),(7,'g'),(26,'z'),]

for nb, lettre in autre_liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre,nb))

#Tuples
tuple_vide = ()
tuple_non_vide = (1,) #est équivalent à ci-dessous
tuple_non_vide = 1,
tubple_avec_plusieurs_valeurs = (1,2,5)

#exple tuple : une fonction renvoyant plusieurs valeurs
def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière et le reste de entier/ divise_par"""
    p_e=entier// divise_par #partie entière de entier/divise_par
    reste = entier%divise_par #reste de entier/divise_par
    return p_e, reste

partie_entiere, reste = decomposer(20,3)

print(partie_entiere)
print(reste)

retour = decomposer (16,6)
print(retour)

system("pause")