#-*-coding:utf-8-*
import os #on importe le module os

def table_par_7():
    nb=7
    i=0 #Notre compteur ! L'auriez-vous oublié ?
    while i<10: #Tant que i  est strictement inférieur à 10,
        print(i+1,"*",nb,"=",(i+1)*nb)
        i += 1 #On incrémente i de 1 à chaque tour de boucle
    print("\n")

table_par_7()

      
def table(nb):
    i=0
    while i<10: #Tant que i est strictement inférieure à 10,
        print(i +1,"*", nb,"=",(i+1)*nb)
        i += 1 #On incrémente i de 1 à chaque tour de boucle
    print("\n")     

table(5)

def table_max(nb, max):
    i=0
    while i<max: #Tant que i est strictement inférieure à la variable max
        print(i+1,"*",nb,"=",(i+1)*nb)
        i+=1
    print("\n")

table_max(11,20)


def table_max_10(nb, max=10):
    """Fonction affichant la table de multiplication par nb de 1*nb à max*nb. max(>=0)"""
    i=0
    while i<max:
        print(i+1,"*",nb,"=",(i+1)*nb)
        i+=1
    print("\n")

table_max_10(2)
table_max_10(5,15)
help(table_max_10)

def carre(valeur):
    return valeur*valeur

variable=carre(5)
print(variable)

f = lambda x : x * x
print(f(5))
print(f(-18))

g = lambda x,y: x+y


os.system("pause")