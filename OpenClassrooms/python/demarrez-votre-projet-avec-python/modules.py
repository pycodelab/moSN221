from turtle import * #TUrtle est une librairie de dessin graphique
import random
#forward(100)
color('red','yellow')
begin_fill()
while True :
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

def get_random_item(my_list): #Renvoie une citation au hasard dans la liste
    rand_numb = random.radint(0,len(my_list)-1)
    item = my_list[rand_numb]#get a quote from a list
    return item
