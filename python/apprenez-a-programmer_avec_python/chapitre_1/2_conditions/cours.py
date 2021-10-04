#-*-coding:utf-8-*
import os #on importe le module os

#Premier exemple de condition
a = 5
if a > 0: #Si a est supérieur à 0
    print("a est supérieur 0.")

a=5
b=8
if a>0:
    #on incrémente la valeur de b
    b +=1
    #on affiche les valeurs des variables
    print("a=",a," et b =",b)

a=5
if a>0:
    print("a est positif.")
if a<0:
    print("a est négatif.")
    
age = 21
if age>= 18:
    print ("Vous êtes majeur.")
else :
    print("Vous êtes mineur.")

a=5
if a >0:
    print("a est supérieur à 0.")
else:
    print("a est inférieur ou égal à 0.")
    
if a>0:
    print("a est positif.")
elif a<0:
    print("a est négatif.")
else:
    print("a est nul.")
    
age=21
majeur = False
if age >=18 :
    majeur = True

#On fait un test pour savoir si a est comprise dans l'intervalle allant de 2 à 8 inclus
a=5
if a>=2:
    if a<=8:
        print("a est dans l'intervalle.")
    else:
        print("a n'est pas dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")
    
if a>=2 and a<=8:
    print("a est dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle")
    
if a<2 or a>8:
    print("a n'est pas dans l'intervalle.")
else:
    print("a est dans l'intervalle.")
    
majeur=False
if majeur != True:
    print("Vous n'êtes pas encore majeur.")

os.system("pause")