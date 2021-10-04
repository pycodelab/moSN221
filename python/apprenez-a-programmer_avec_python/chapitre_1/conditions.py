#-*-coding:utf-8-*
import os #on importe le module os
annee=int(input("Saisissez une année : "))
if annee%4 != 0 :
    print("Cette année n'est pas bissextile")
else :
    if annee%100 == 0 :
        if annee%400 == 0 :
            print("Cette année est bissextile")
        else :
            print("Cette année n'est pas bissextile")
    else :
        print("Cette année est bissextile")

os.system("pause")