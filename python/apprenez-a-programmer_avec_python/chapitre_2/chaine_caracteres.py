from os import *

chaine = "NE CRIE PAS SI FORT !"
print(chaine.lower()) #Mettre la chaine en minuscule

chaine = str() #crée une chaine vide

while chaine.lower() != "q" :
    print ("Tapez 'Q' pour quitter...")
    chaine = input()
print("Merci")

minuscules = "une chaine en minuscules"
print(minuscules.upper()) #Mettre en majuscule
print(minuscules.capitalize()) #Première lettre en majuscule
espaces=" une chaine avec des espaces "
print(espaces.strip()) #Retire les espaces au début et à la fin
titre = "introduction"
print(titre.upper().center(20)) #Centrer dans un espace de 20 caractères

chaine = "Bonjour tout le monde !"
print(chaine)

prenom = "Mohamed"
nom = "Diaw"
age = 29
print("Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age))


print(
	"Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} ans.".format(prenom,nom,age,nom.upper()))

date = "Mercredi 23 juillet 2020"
heure = "17:00"
print("Cela s'est produit le {}, à {}.".format(date,heure))

adresse = """{no_rue}, {nom_rue} 
    {code_postal} {nom_ville} ({pays})""".format(no_rue=34, nom_rue="rue du champ des oiseaux", code_postal=76000, nom_ville="Rouen", pays="France")
print(adresse)

message = "Bonjour"
chaine_complete = message + " " + prenom
print(chaine_complete)

msg = "J'ai " + str(age) + " ans."
print(msg)

chaine = "Salut les ZER0S !"
chaine[0]
chaine[2]
chaine[-1]

chaine = "Salut"
print(len(chaine))
i = 0
while i<len(chaine) :
    print(chaine[i]) # On affiche le caractère à chaque tour de boucle
    i+=1

presentation = "salut"
print(presentation[0:2]) #On sélectionne les deux premières lettres
print(presentation[:2]) # du début jusuq'à la 3e lettre non comprise
print(presentation[2:len(presentation)]) #On sélectionne la chaîne sauf les 2 premières lettres
print(presentation[2:]) #de la troisième lettre jusqu'à la fin

mot="lac"
print(mot)
mot ="b" + mot[1:]
print(mot)

system("pause")