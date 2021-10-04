import random
import pickle
"""Ce fichier décrit la liste des fonctions nécessaires au fonctionnement du jeu"""

def aDeviner(listeMots):
    """Fonction pour générer un mot au hasard"""
    return random.choice(listeMots) #Génération d'un mot au hasard à partir d'une liste


def motMasque(mot):
    """Fonction permettant de créerun mot masqué (en étoile) de la même taille que le mot à deviner"""
    tableauMasque = [] #liste des lettres qui composeront le résultat
    i = 0
    while i<len(mot) :
        #print(motADeviner[i])
        tableauMasque.append("*") #création d'un tableau de même longueur que celui du mot à deviner
        i += 1

    motMasque = "".join(tableauMasque) #Création du mot masqué
    return motMasque

def motEnTableau(mot):
    """Fonction qui transforme un mot en une liste de caractères"""

    tableau = [] #liste des lettres qui composent le mot
    i = 0
    while i<len(mot) :
        #print(motADeviner[i])
        tableau.append(mot[i]) #construction de la liste des lettres qui composent le mot
        i += 1
    return tableau
                    
def jeuUtilisateur (nbre,mot1,mot2):
    """Fonction qui reproduit le jeu du pendule : Elle prend en paramètre un nbre représentant le nombre d'essais, le mot à deviner et un mot masqué (ne comportant que des * et de la même taille que le mot à deviner). A chaque tour de boucle (si l'utiisateur choisi une lettre), on compare le mot à deviner et le mot démasqué. On récupère le nbre de tentatives (<= au nbre d'essais autorisé) et le mot démasqué final obtenu"""
    score = 0 #initialisation du score
    nbreLettresTrouvees = 0 #initialisation du nbre de lettres trouvées
    nbEssai = 0 #initialisation du nbre d'essais
    tableauADeviner = motEnTableau(mot1)
    tableauDevine = motEnTableau(mot2)
    while ((nbEssai <= nbre) and (mot1 != mot2)) :
        try :
            choixJoueur=str(input("Choix de lettre : ")) #choix du joueur
            assert choixJoueur != " "
        except AssertionError :
            print("erreur de saisie")
        else :
            nbEssai += 1
            for indice, elt in enumerate(tableauADeviner) : #création d'un tuple indice, lettre 
                if choixJoueur == elt : #le joueur a trouvé une lettre
                                        
                    if tableauDevine[indice] == elt :
                        print("lettre déjà trouvée !")
                    else :
                        tableauDevine[indice] = elt #Modification du mot en remplacant l'étoile correspondante par la lettre
                        print("Vous avez trouvé une lettre ! ")
                        mot2 = "".join(tableauDevine) 
    return mot2, nbEssai

def calculScore(mot1, mot2, nbre1, nbre2):
    """Cette fontion calcule le score obtenu par le joueur : si le mot démasqué et le mot à deviner sont différents, le score est de 0, sinon le score correspond au nbre de tentatives restant quand le joueur découvre le mot"""
    if mot1 != mot2 :
        score = 0
        print("Perdu ! Vous êtes pendu") #Si le joueur ne trouve pas le mot complètement
    else :
        score = nbre2 - nbre1 #Le score correpond à nbre de tentatives autorisé - nbre d'essai utilisé par le joueur
    return score
        

def enregistrementScoreJoueur (nomJoueur,score, dicoJoueurs) :
    """Cette fonction permet d'enregistrer le score du joueur dans un dictionnaire sous la forme nomJoueur => score s'il s'agit d'un nouveau joueur ou réactualise le score du joueur s'il est déjà inscrit"""
    if dicoJoueurs == {} : #Si le dico est vide, le joueur y est inscrit directement avec son score
        dicoJoueurs[nomJoueur] = score
        print("Vous venez d'être inscrit à la liste de joueurs")
    else : #sinon on regarde si le joueur est déjà dans le dico ou nom
        try : #on tente de réactualiser le score du joueur dans le dico
            dicoJoueurs[nomJoueur] = dicoJoueurs[nomJoueur] + score
        except KeyError : #levée d'un keyError si le joueur n'existe pas dans le dico
            dicoJoueurs[nomJoueur] = score
            print("Vous venez d'être inscrit à la liste de joueurs")
        else :
            print("Vous etiez déjà inscrit, votre score a été mis à jour.")
                    
            
def affichageBilanScore (dicoJoueurs):
    """Cette fonction affiche un bilan des scores de tous les joueurs. Il permet de réactualiser le score d'un joueur s'il est déjà inscrit """

    for pseudo, total in dicoJoueurs.items() :
        print("{} : {} points".format(pseudo, total)) #Affichage de la liste des scores pour chaque joueur
    
        
def enregistrementScoreFichier (dico):
    """Cette fonction permet d'enregistrer le score dans un fichier"""
    with open("scores.txt","wb") as fichier : #ouverture du fichier (ou création s'il n'existe pas)
        mon_pickler = pickle.Pickler(fichier)
        
        for nomJoueur, score in dico.items():
            aEnregistrer = nomJoueur+" : "+str(score)+" points"
            mon_pickler.dump(aEnregistrer) # enregistrement du fichier
    print("Les scores sont enregistrés dans le fichier \'scores.txt\'")