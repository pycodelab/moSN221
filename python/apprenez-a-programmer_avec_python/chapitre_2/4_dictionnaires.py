from os import *

mon_dictionnaire = dict()
print(type(mon_dictionnaire))

print(mon_dictionnaire)

#2e methode de définition
deuxieme_dictionnaire = {}
print(deuxieme_dictionnaire)


mon_dictionnaire = {}
mon_dictionnaire["pseudo"]="Prolixe"
mon_dictionnaire["mot de passe"]= "*"
print(mon_dictionnaire)

mon_dictionnaire["pseudo"] = "6pril"
print(mon_dictionnaire)

print(mon_dictionnaire["mot de passe"])
#Si la clé n'existe pas dans le dictionnaire, une exception de type KeyError sera levée

mon_dictionnaire={}
mon_dictionnaire[0]="a"
mon_dictionnaire[1]="e"
mon_dictionnaire[2]="i"
mon_dictionnaire[3]="o"
mon_dictionnaire[4]="u"
mon_dictionnaire[5]="y"

print(mon_dictionnaire)


#Codage echiquier
echiquier = {}
echiquier['a',1]="tour blanche" #En bas à gauche de l'échiquier
echiquier['b',1]="cavalier blanc" #A droite de la tour
echiquier['c',1]="fou blanc" #A droite du cavalier
echiquier['d',1]="reine blanche" #A droite du fou
#...Première ligne des blancs
echiquier['a',2]="pion blanc" #Devant la tour
echiquier['b',2]="pion blanc" #Devant le cavalier, à droite du pion
#...Seconde ligne des blancs

print(echiquier)

placard={"chemise":3,"pantalon":6,"tee-shirt":7}
print(placard)

mon_dictionnaire={'pseudo','mot de passe'} #Cela définit un set
#Un set est très semblable à une liste, Sauf qu'il ne peut contenir deux objets identiques
print(mon_dictionnaire)

del placard["chemise"]
print(placard)

print(placard.pop("pantalon"))

print(placard)

#Fonctions dans des dictionnaires
def fete():
    print("C'est la fête.")

def oiseau():
    print("Fais comme l'oiseau")

fonctions = {}
fonctions["fete"]=fete #on ne met pas les parenthèses
fonctions["oiseau"]=oiseau
print(fonctions["oiseau"])
fonctions["oiseau"]() #on essaie de l'appeler

#Methodes de parcours
#Parcours des clés
fruits = {"pommes":21,"melons":3,"poires":31}
for cle in fruits:
    print(cle)

for cle in fruits.keys():
    print(cle)

#Parcours des valeurs
for valeur in fruits.values():
    print(valeur)

if 21 in fruits.values():
    print("Un des fruits se trouve dans la quantité 21.")

#Parcours des clés et valeurs simultanément
#items renvoie une liste contenant les couples clé:valeur, sous la forme d'un tuple
for cle,valeur in fruits.items():
    print("La clé {} contient la valeur {}.".format(cle,valeur))

#Récupérer les paramètres nommés dans un dictionnaire
def fonction_inconnue(**parametres_nommes):
    #Fonction permettant de voir comment récupérer les paramètres nommés dans un dictionnaire
    print("J'ai reçu en paramètres nommés:{}.".format(parametres_nommes))

fonction_inconnue() #Aucun paramètre
fonction_inconnue(p=4,j=8)

#def fonction_inconnue(*en_liste,**en_dictionnaire)
#Fonction qui accepte n'importe quel type de parametres, nommés ou non, dans n'importe quel ordre, dans n'importe quelle quantité -- Les paramètres non nommés (*) se retrouveront dans la variable (en_liste) et les paramètres nommés dans la variable (en_dictionnaire)

#Transformer un dictionnaire en parametres nommés d'une fonction
parametres={"sep":" >> ","end":" -\n"}
print("Voici","un","exemple","d'appel",**parametres)

system("pause")