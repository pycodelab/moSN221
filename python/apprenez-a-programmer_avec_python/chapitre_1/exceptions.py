import os

annee = input()
try: #On essaye deconvertir l'année en entier
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")

try:
    resultat = numerateur/denominateur
except:
    print("Une erreur est survenue...laquelle?")

try:
    resultat = numerateur/denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)

try:
    #bloc de test
except type_de_l_exception as exception_retournee:
    print("Voici l'erreur:", exception_retournee)

try:
    #Test d'instruction(s)
except type_de_l_exception:
    #Traitement en casd'erreur
finally:
    #Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non

try:
    #Test d'instruction(s)
except type_de_l_exception : #Rien ne doit se passer en cas d'erreur
    pass

annee = input("Saisissez une année supérieure à 0:")
try:
    annee = int(annee) #Conversion de l'année
    assert annee > 0 #Renvoie True si le test est vraie sinon exception AssertionError
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
    
os.system("pause")