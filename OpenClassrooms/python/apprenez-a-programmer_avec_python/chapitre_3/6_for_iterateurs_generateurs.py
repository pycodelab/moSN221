import os

"""ITERATEURS"""

ma_liste = [1,2,3]
for element in ma_liste:
    print(element)

"""fonctions spéciales __iter__, __next__ // fonctions iter() et next() puis levée de l'exception StopIteration si le parcours touche à sa fin"""

ma_chaine = "test"
"""iterateur_de_ma_chaine = iter(ma_chaine)#création de l'itérateur
iterateur_de_ma_chaine
next(iterateur_de_ma_chaine) #parcours de la liste ==> t
next(iterateur_de_ma_chaine) #parcours de la liste ==> e
next(iterateur_de_ma_chaine) #parcours de la liste ==> s
next(iterateur_de_ma_chaine) #parcours de la liste ==> t
next(iterateur_de_ma_chaine) #Fin de la liste ==> StopIteration"""

"""On peut créer nos itérateurs"""
class RevStr(str):
    """Classe reprenant les méthodes et attributs des chaînes construites depuis str. On se contente de définir une méthode de parcours différente : au lieu de parcourir la chaîne de la première à la dernière lettre, on la parcourt de la dernière à la première
    
    Les autres méthodes, y compris le constructeur, n'ont pas besoin d'être redéfinies"""
    
    def __iter__(self):
        """Cette méthode renvoie un itérateur parcourant la chaine dans le sens inverse de celui de str"""
        return ItRevStr(self) #On renvoie l'iterateur créé pour l'occasion
    
class ItRevStr:
    """Un iterateur permettant de parcourir une chaine de la dernière lettre à la première. On stocke dans des attributs la position courante et la chaine à parcourir"""
    
    def __init__(self,chaine_a_parcourir):
        """On se positionne à la fin de la chaine"""
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)
        
    def __next__(self):
        """Cette méthode doit renvoyer l'élément suivant dans le parcours, ou lever l'exception 'Stopiteration' si le parcours est fini"""
        
        if self.position == 0: #Fin du parcours
            raise StopIteration
        self.position -= 1 #On décrémente la position
        return self.chaine_a_parcourir[self.position]

"""ma_chaine = RevStr("Bonjour")
    ma chaine
    for lettre in ma_chaine:
            print(lettre)"""

"""GENERATEURS"""

def mon_generateur(): #permet d'obtenir un générateur
    """Notre premier générateur. Il va simplement renvoyer 1,2 et 3"""
    yield 1
    yield 2
    yield 3

"""mon_generateur
    ==> <function mon_generateur at xxx>
    mon_generateur()
    ==> <generator object mon_generateur at xxx>
    
    quand on fait mon_iterateur = iter(mon_generateur()) ==> création de l'itérateur
                    next(mon_iterateur) ==> 1 puis 2 puis 3, ...
                    
    ou bien
    for nombre in mon_generateur():
        print(nombre)"""

def intervalle(inf,sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup
    Note:borne_inf doit être inférieure à borne_sup"""
    inf +=1
    while inf<sup:
        yield inf
        inf += 1
    
def revIntervalle (inf,sup):
    if inf<sup:
        inf+=1
        while inf<sup:
            yield inf
            inf+=1
    else :
        sup+=1
        while inf>sup:
            yield sup
            sup +=1
            
            
"""CO-ROUTINES"""
"""Ce sont des méthodes de yield"""
generateur = intervalle(5,20)
for nombre in generateur: #pour appeler une méthode du générateur on doit le stocker dans une variable
    if nombre>17:
        generateur.close() #Interruption de la boucle

def intervalle_bis(borne_inf,borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    Notre générateur doit pouvoir 'sauter' une certaine plage de nombres en fonction d'une valeur qu'on lui donne pendant le parcours. La valeur qu'on lui passe est la nouvelle valeur de borne_inf"""
    """Note: borne_inf doit être inférieure à borne_sup"""
    
    borne_inf +=1
    while borne_inf < borne_sup :
        valeur_recue = (yield borne_inf) #on passe une valeur à notre générateur
        if valeur_recue is not None: #Notre générateur a reçue quelque chose
            borne_inf = valeur_recue #il affiche la valeur qu'on lui a passée
        else :
            borne_inf+=1
    
    """On interagit avec notre générateur avec la méthode send"""
    
generateur = intervalle_bis(10,25)
for nombre in generateur:
    if nombre == 16: #On saute à 20
        nombre = generateur.send(20)
    print(nombre,end=" ")




















os.system("pause")