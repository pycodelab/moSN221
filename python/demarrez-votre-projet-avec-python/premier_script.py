import os

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]

# Show random quote
# If user_answer is 'B':
#   - leave the program

# Else :
#   - show anoter quote
user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme")

def get_random_quote(my_list):
    #Get a random number
    item = my_list[0]#get a quote from an array
    print(item) #show the quote in the interpreter
    return "program is over" #returned value
    
user_answer = "A"

while user_answer != "B" :
    
    get_random_quote(quotes)
    user_answer="B"

"""if user_answer == "B":
    pass #leave the program (Python ne fait rien et sort de la boucle)
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d'humour, je C...")
else :"""

"""Methodes chaines de caractères"""
print("{character} a dit : {quote}".format(character="Babar", quote="Tout n'est pas cirrhose dans la vie, comme dit l'alcoolique."))

print("{} a dit : {}".format("Babar", "Tout n'est pas cirrhose dans la vie, comme dit l'alcoolique."))

"""Methodes Listes"""
print(quotes[1])
characters.index("Babar") #Renvoie l'index de cette valeur
characters.append("Mowgli") #Ajout en fin de liste
characters.insert(4,"Balou") #Ajout d'un élément à un certain index
characters[1] = "La Fée Clochette"
characters.pop() #Supprime le dernier élément et renvoie sa valeur
characters.pop(4) #Supprime l'élément d'index 4 et renvoie sa valeur
characters.remove("Kirikou") #Supprime l'élément sans renvoyer de valeur
len(characters) #donne le nbre d'éléments dans une liste
characters[-1] #Accède au dernier élément d'une liste
print(characters)

program ={"quotes" : quotes,"characters" : characters}

print(program["quotes"][1])
program["characters"] = "Un nouveau nom" #Ajoute ou remplace une valeur
print(program["characters"])
program.update({"characters" : ["Alvin","Père Noël"], "quotes":["une citation unique"]}) #MàJ ou ajout de plusieurs valeurs
print(program)
program.pop("quotes") #Supprime une clé
print(program)

os.system("pause")