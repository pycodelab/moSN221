#-*-coding:utf-8-*-
import os #on importe le module os

#Variables
mon_age = 21
print(mon_age)

mon_age = mon_age +2
print(mon_age)

mon_agex2 = mon_age * 2
print(mon_agex2)

#Type de donnees
mon_entier = 3
print(mon_entier)

mon_flottant = 3.152
print(mon_flottant)

ma_chaine_de_caracteres = "ceci est une chaîne de caractères"
ma_chaine_de_caracteres2 = 'ceci est une chaîne de caractères'
ma_chaine_de_caracteres3 = """ceci est une chaîne de caractères"""
ma_chaine_de_caracteres4 = 'J\'aime le Python !'
ma_chaine_de_caracteres5 = "\"Le seul individu formé, c'est celui qui a appris comment apprendre (...)\" (Karl Rogers, 1976)"

print(ma_chaine_de_caracteres)
print(ma_chaine_de_caracteres2)
print(ma_chaine_de_caracteres3)
print(ma_chaine_de_caracteres4)
print(ma_chaine_de_caracteres5)

ma_variable = 3
ma_variable = ma_variable + 1
ma_variable += 1

a = 5
b = 32
a,b = b,a #permutation

x = y = 3

#Fonctions

#fonction "type"
type(a) #renvoie <class 'int'>
type(3.4) # renvoie <class 'float'>
type("un essai") # renvoie <class 'str'>

#fonction "print"
print(a)
a = a + 3
b = b - 2
print("a =", a, "et b =", b) #renvoie a = 6 et b = 4


os.system("pause")