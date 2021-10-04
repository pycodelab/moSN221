"""module multipi contenant la fonction table"""

import os

def table(nb,max):
    """Fonction affichnt la table de multiplication par nb de 1*nb jusqu'à max*nb"""
    i=0 # Notre compteur 
    while i<max : #Tant que i est strictement inférieur à 10
        print(i+1,"*",nb,"=",(i+1)*nb)
        i+=1 #On incrémente i de 1 à chaque tour de boucle

#test de la fonction table
if __name__=="__main__" :
    table(4,10)
    os.system("pause")