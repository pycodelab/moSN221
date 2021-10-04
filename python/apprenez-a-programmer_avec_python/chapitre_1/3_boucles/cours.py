#-*-coding:utf-8-*
import os #on importe le module os
print(" 1 * 7 =", 1*7)
print(" 2 * 7 =", 2*7)
print(" 3 * 7 =", 3*7)
print(" 4 * 7 =", 4*7)
print(" 5 * 7 =", 5*7)
print(" 6 * 7 =", 6*7)
print(" 7 * 7 =", 7*7)
print(" 8 * 7 =", 8*7)
print(" 9 * 7 =", 9*7)
print(" 10 * 7 =", 10*7, "\n")

nb=24
print("1 *",nb,"=", 1*nb)
print("2 *",nb,"=", 2*nb)
print("3 *",nb,"=", 3*nb)
print("4 *",nb,"=", 4*nb)
print("5 *",nb,"=", 5*nb)
print("6 *",nb,"=", 6*nb)
print("7 *",nb,"=", 7*nb)
print("8 *",nb,"=", 8*nb)
print("9 *",nb,"=", 9*nb)
print("10 *",nb,"=", 10*nb, "\n")

nb=7 #on garde la variable contenant le nombre dont on veut la table de multiplication
i=0 #C'est notre variable compteur que nous allons incrémenter

while i<10: #Tant que i est strictement inférieure à 10
    print(i+1,"*",nb,"=",(i+1)*nb)
    i+=1 #On incrémente i de 1 à chaque tour de boucle

print("\n");

chaine="Bonjour les ZEROS"
for lettre in chaine:
    print(lettre)

print("\n");

for lettre in chaine:
    if lettre in "AEIOUYaeiouy": #lettre est une voyelle
        print(lettre)
    else : #lettre est une consonne...ou plus exactement n'est pas une voyelle
        print("*")

print("\n")

while 1: #1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter :")
    if lettre =="Q":
        print("Fin de la boucle")
        break

i=1
while i<20: #Tant que i est inférieure à 20
    if i%3 ==0:
        i += 4 #On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à",i)
        continue #On retourne au while (ou au for) sans exécuter les autres lignes
    print("La variable i =",i)
    i+=1 #Dans le cas classique on ajoute juste 1 à i
    
os.system("pause")