import os

class Personne : #Définition de notre classe personne
    """Classe définissant une personne caractérisée par
    - son nom
    - son prénom
    - son age
    - son lieu de résidence"""
    
    def __init__(self):#méthode constructeur
        """ constructeur de notre classe"""
        self.nom = "Dupont"
        self.prenom = "Jean"
        self.age = 33
        self.lieu_residence = "Paris"
    

"""ATTRIBUTS DE CLASSE"""
class Compteur:
    """Cette classe possède un attribut de classe qui s'incrèmente à chaque fois que l'on crée un objet de ce type"""
    
    objets_crees = 0 #Le compteur vaut 0 au départ
    
    def __init__(self):
        """A chaque fois que l'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees +=1
        
"""METHODES D'INSTANCE'"""
class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire, lire et effacer, par jeu de méthodes. L'attribut modifié est 'surface'"""
    
    #Les attributs de l'objet sont propres à l'objet créé : Les attributs sont contenus dans l'objet
    #Les méthodes sont propres à la classe : Les méthodes sont contenues dans la classe tab.ecrire = TableauNoir.ecrire(tab,...)
    def __init__(self): 
        """Par défaut, notre surface est vide"""
        self.surface = ""
    
    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter le message à écrire"""
        
        if self.surface != "":
            self.surface += "\n"
            self.surface += message_a_ecrire

    def lire(self):
        """Méthode permettant de lire le tableau"""
        print(self.surface)
    
    def effacer(self) :
        "Methode permettant d'effacer le tableau"
        self.surface = ""
        
"""METHODES DE CLASSE"""      
class Compteur_bis:
    """Cette classe possède un attribut de classe et une méthode de classe"""
    
    objets_crees = 0 #attribut de classe
    def __init__(self):
        """A chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur_bis.objets_crees += 1
    
    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(cls.objets_crees))
    
    combien = classmethod(combien) #pour que Python convertisse la methode en methode de classe

"""METHODES STATIQUES"""
class Test:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose")
        print("peu importe les données de l'objet ou de la classe")
    
    afficher = staticmethod(afficher)

    
"""INTROSPECTION DIR et DICT"""
class Testbis:
    """Une classe de test tout simplement"""
    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"
        
    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))
        
    """Pour afficher ce qu'il y a dans la classe : dir(un objet de la classe) ou bien 
    objet_de_la_classe .__dict__[nom_attribut] = valeur de l'attribut. __dict__renvoie un dico avec comme clés le nom des attributs et comme valeur leurs valeurs"""
os.system("pause")