#import du module os

import os
from math import *
from random import *

print ("BIENVENUE DANS ZCASINO")
gain = 0
numeroGagnant = 0
autorisationMise = False 
autorisationRoulette = False
autorisationPortefeuille = False

#Saisie portefeuille du joueur
while autorisationPortefeuille==False :
    try :
        portefeuille = int(input("Votre portefeuille de jeu ? "))
        assert portefeuille>0
    except ValueError :
        print("Vous n'avez pas saisi un nombre")
    except AssertionError :
        print("Le nombre saisi est négatif")
    else :
        autorisationPortefeuille=True

print("Vous entrez avec ",portefeuille, "$.")


while autorisationMise == False : #autorisation de miser si le numéro choisi est entre 0 et 49
    try :
        numeroMise = int(input("Misez sur un numéro entre 0 et 49 : "))
        assert numeroMise>0 and numeroMise<50
    except ValueError :
        print("Vous n'avez pas saisi un nombre")
    except AssertionError :
        print("Le nombre saisi n'est pas entre 0 et 49")
    else :
        autorisationMise = True
        autorisationRoulette = False
        #Autorisation de tourner la roulette si la mise saisie est bonne
        while autorisationRoulette == False :
            try :
                sommeMise = int(input("Entrez le montant de votre mise : "))
                assert sommeMise>0 and sommeMise<=portefeuille
            except ValueError :
                print("Vous n'avez pas saisi un nombre")
            except AssertionError :
                print("La somme saisie est incorrecte.")
            else :
                autorisationRoulette = True
                numeroGagnant = randrange(49)
                #Calcul des gains
                if numeroGagnant == numeroMise :
                    gain = 3*sommeMise
                elif (numeroGagnant != numeroMise):
            
                    if (numeroGagnant%2 == 0 and numeroMise%2 == 0) or (numeroGagnant%2 !=0 and numeroMise%2 !=0) :
                        gain = ceil(0.5*sommeMise)
                    else:
                
                        gain = -sommeMise
                #Situation portefeuille
                portefeuille = portefeuille + gain
                print("Le numero gagnant était : ",numeroGagnant)
                
                #Etat de la partie : banqueroute ou pas ? est-ce que le joueur revient ou pas ?
                if portefeuille <=0 :
                    print("Vous avez écoulé votre portefeuille.")
                    print("Merci d'avoir joué au Zcasino, revenez avec de l'argent.")
                else :
                    print("Gain obtenu pendant ce tour :",gain,"$")    
                    print("Vous avez dans votre portefeuille :",portefeuille,"$") 
                    volonteJoueur = input("Voulez-vous continuer la partie ? (y/n)")
                    if volonteJoueur == "n" :
                        print("Merci d'avoir joué. Vous repartez avec ",portefeuille, "$.")
                        autorisationMise = True
                        autorisationRoulette = True
                    else :
                        print("C'est reparti pour un autre tour !")
                        autorisationMise=False
    
    
os.system("pause")
 
            
        
            
                

