import os


class DictionnaireOrdonnee:
    
    #on initialise le dictionnaire (prise en compte de la présence de plusieurs paramètres)
    def __init__(self, **parametres):
        self.dico = {} #le dictionnaire est vide par défaut
        if parametres.items():
            for cle,valeur in parametres.items():
                self.dico[cle]=valeur #on remplit le dictionnaire avec les données fournies
    
    #affichage du dictionnaire
    def __repr__(self):
        return "{}".format(self.dico)
    
    #affichage d'une valeur connaissant la clé
    def __getitem__(self,index):
        """Cette méthode spéciale est appelée quand on fait objet[index]. Elle redirige vers self.dictionnaire[index]"""
        return self.dico[index]
    
    #ajout d'un élément
    def __setitem__(self,index,valeur):
        """Cette méthode est appelée quand on écrit objet[index]=valeur. On redirige vers self._dictionnaire[index]=valeur"""
        self.dico[index]=valeur
    
    #supprimer un élément 
    def __delitem__(self,index):
        del self.dico[index]
    
    #on regarde si le dictionnaire contient l'élément fourni
    def __contains__(self,index): 
        return index in self.dico.keys()
    
    #on convertit le dictionnaire en liste de tuples
    def items(self):
        listeDico = [(i,j) for i,j in self.dico.items()]
        return listeDico
    
    #on crée une liste pour les clés
    def keys(self):
        listeCles =[i for i in self.dico.keys()]
        return listeCles
    
    #on crée une liste pour les valeurs
    def values(self): 
        listeValeurs = [i for i in self.dico.values()]
        return listeValeurs
    
    #on calcule la longueur du dictionnaire (le nombre d'éléments contenus dans le dictionnaire)
    def __len__(self):
        return len(self.dico)
    
    #on fusionne deux dictionnaires
    def __add__(self,dico_a_ajouter):
        
        if type(self) == type(dico_a_ajouter) :
            for i,j in dico_a_ajouter.items(): #on prend le deuxième dictionnaire
                if self.__contains__(i): #si un élément du deuxième dictionnaire est déjà dans le premier dictionnaire
                    self.__setitem__(i,self.__getitem__(i)+j) #on ajoute la deuxième valeur 
                else:
                    self.__setitem__(i,j) ##sinon on ajoute l'élément dans le dictionnaire
            self.__repr__()
        else :
            raise TypeError( \
                "Impossible de concaténer {0} et {1}".format( \
                type(self), type(dico_a_ajouter)))
    
    def sort(self):
        listeDicoTriee = sorted(self.items(), key=lambda fruit: fruit[0]) #on trie la liste de tuples
        #return listeDicoTriee
        DicoTriee = DictionnaireOrdonnee() #on crée un dictionnaire vide
        for fruit,nombre in listeDicoTriee:
            DicoTriee.dico[fruit]= nombre #on rentre les éléments de la liste un par un dans le nouveau dictionnaire
        self.dico = DicoTriee.dico #on écrase le contenu de l'ancien dictionnaire par le nouveau
        
    def reverse(self):
        listeDicoTriee = sorted(self.items(), key=lambda fruit: fruit[0],reverse = True) #on trie la liste de tuples
        #return listeDicoTriee
        DicoTriee = DictionnaireOrdonnee() #on crée un dictionnaire vide
        for fruit,nombre in listeDicoTriee:
            DicoTriee.dico[fruit]= nombre #on rentre les éléments de la liste un par un dans le nouveau dictionnaire
        self.dico = DicoTriee.dico #on écrase le contenu de l'ancien dictionnaire par le nouveau
    
    def __iter__(self):
        
        return IterateurDico(self.keys()) #on utilise l'itérateur
        
class IterateurDico :

    def __init__(self,liste): #initialisation de l'itérateur
        self.liste = liste #l'iterateur se base sur une liste
        self.position = -1
        
    def __next__(self):
        
        self.position += 1
        if self.position == len(self.liste): #si on atteint le dernier élément on arrête le parcours
            raise StopIteration
        else :
            return self.liste[self.position] #on parcourt la liste à chaque itération
        
os.system("pause")