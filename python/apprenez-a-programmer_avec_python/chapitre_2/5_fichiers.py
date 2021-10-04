import os
import pickle

#Lire le fichier
#os.chdir("C:/apprenez-a-coder_avec_python/chapitre_2")
mon_fichier = open("fichier.txt","r")
print(mon_fichier)
print(type(mon_fichier))
#mon_fichier.close()

#Lecture du fichier
contenu=mon_fichier.read()
print(contenu)

mon_fichier.close()

#Ecriture dans un fichier
mon_fichier = open("fichier.txt","w") #w écrase tout et a ajoute ce qu'on écrit à la fin
#Les 2 méthodes créent le fichier s'il n'existe pas
mon_fichier.write("Premier test d'écriture dans un fichier via Python")#write ne prend que des chaines de caractères

mon_fichier.close()

#Ecrire d'autres types de données
#convertir en chaine de caractères avant d'écrire puis en nombre après avoir lu

with open("fichier.txt","r") as mon_fichier :
    texte = mon_fichier.read()

print(mon_fichier.closed)

#Enregistrer des données
score = {
    "joueur 1":5,
    "joueur 2":35,
    "joueur 3":20,
    "joueur 4":2
}

#Utilisation du module pickle qui contient deux classes Pickler et Unpickler

with open("donnees.txt","wb") as fichier :
    mon_pickler= pickle.Pickler(fichier) #Crée un obtjet de classe Pickler pour le fichier
    # enregistrement
    mon_pickler.dump(score)

#Récupérer des données enregistrés
with open("donnees.txt","rb") as fichier :
    mon_depickler = pickle.Unpickler(fichier)
    #Lecture des objets contenus dans le fichier
    score_recupere = mon_depickler.load()

print(score_recupere)
os.system("pause")

