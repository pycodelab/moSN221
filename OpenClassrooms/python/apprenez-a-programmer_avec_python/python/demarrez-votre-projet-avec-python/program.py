#-*- coding: utf8 -*-

import json
import random

def read_values_from_json(file,key): #Renvoie une liste à partir d'un fichier json
    values = []#Create an empty list
    with open(file) as f : #open a json file with myobjects
        data = json.load(f) #Charge le fichier json et le transforme en objet Python
        for entry in data : #load all the data contained in this file
            values.append(entry[key])#add each item in my list
    return values #return my completed list

      
#Enlève les espaces en début et en fin de chaine pour chaque élément d'une liste
def clean_strings(sentences):
    cleaned = []
    for sentence in sentences:
        clean_sentence = sentence.strip()#enlève les espaces en début et fin de chaine
        cleaned.append(clean_sentence)#ajoute la nvlle phrase dans la liste
    return cleaned


def get_random_item_in(my_list): #Renvoie une valeur au hasard dans la liste
    rand_numb = random.randint(0,len(my_list)-1)#renvoie un nombre entier au hasard compris entre 0 et le nombre d'éléments de la liste
    item = my_list[rand_numb]#get a quote from a list
    return item

def random_value(file,key): #return a random value from list
    all_values = read_values_from_json(file,key)#phrases dans une liste
    clean_values = clean_strings(all_values)#nettoie toutes les phrases de la liste
    return get_random_item_in(clean_values)#renvoie une phrase au hasard de la liste


###############################################
#################QUOTES########################
###############################################

def random_quote():
    return random_value("quotes.json","quote")
    
###############################################
#################CHARACTERS########################
###############################################

def random_character():
    return random_value("characters.json","character")
    

###############################################
#################AFFICHAGE########################
###############################################

def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character,rand_quote))
    


    
def main_loop():
    while True:
        print_random_sentence()
        message = ("Voulez-vous voir une autre citation ? Pour sortir du programme, tapez [B].")
        choice = input(message).upper()
        if choice == 'B':
            break
            #This will stop the loop
    
if __name__ =="__main__": #Pour pouvoir exécuter le module tout seul
    main_loop()