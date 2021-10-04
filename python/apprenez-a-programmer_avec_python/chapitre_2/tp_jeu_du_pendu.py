import os
from fonctions import *
from donnees_jeu_pendu import *

"""Code du jeu à partir des fonctions définies dans le module fonctions"""

#nbre d'essais autorisés par défaut
nbEssais=10

#Création du dico
dicoJoueurs = {}

#Si l'utilisateur veut jouer au pendu
while str(input("Voulez-vous jouer au pendu (y/n) ? ")) == "y" :
    #Le joueur doit saisir son nom
    nomJoueur=str(input("Votre nom ? "))
    #nbEssais = int(input("En combien d'essais pensez-vous trouver le mot ?"))
    while nomJoueur !="" : 
        
        try :
            assert nomJoueur != " "
        except AssertionError :
            print("erreur de saisie")
        else : 
           
            #Choix aléatoire du mot à deviner
            motADeviner = aDeviner(listeMots)
            
            #Affichage du mot à deviner
            print(motADeviner)
            
            #Création du mot masqué contenant des étoiles et autant de caractères que le mot à deviner
            motEnEtoile = motMasque(motADeviner)
            
            
            #La fonction simule le jeu et retourne le nbre d'essai et le mot démasqué
            motDevine,nbEssai = jeuUtilisateur (nbEssais,motADeviner,motEnEtoile)
            
            #Calcul du score du joueur
            scoreJoueur = calculScore(motADeviner, motDevine, nbEssai, nbEssais)
                
                            

            
        print(motDevine) #Affichage du mot démasqué
        print(scoreJoueur) #Affichage du score du joueur
            
        #Enregistrement du score du joueur dans le dictionnaire   
        enregistrementScoreJoueur (nomJoueur,scoreJoueur, dicoJoueurs)
                    
            
        print("Merci d'avoir joué au Pendu")
        #Réinitialisation du nom du joueur
        nomJoueur=""
        
        #Affichage du bilan des scores
        affichageBilanScore(dicoJoueurs)
        
        #Enregistrement du score dans un fichier
        enregistrementScoreFichier(dicoJoueurs)

#Si l'utilisateur choisi "n"
print("Merci ! Au revoir")

os.system("pause")