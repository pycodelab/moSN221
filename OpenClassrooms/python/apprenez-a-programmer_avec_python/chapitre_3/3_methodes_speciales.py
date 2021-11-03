import os
"""EDITION DE L'OBJET ET ACCES AUX ATTRIBUTS"""

class Personne:
    """Un petit exemple de classe"""
    def __init__(self,nom,prenom,age):
        """Exemple de constructeur (pour créer un objet)"""
        self.nom  = nom
        self.prenom = prenom
        self.age = age
        
    
    
    def __repr__(self):
        """Méthode appelée quand on veut afficher l'objet ie que l'on fait (print(mon_objet) ou mon_objet)"""
        return "Personne: nom({}), prénom({}), âge({})".format(self.nom,self.prenom,self.age)
    
        """On peut également faire repr(objet), ceci fait la même chose que la méthode __repr__"""
        
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet avec print()"""
        return "{ {},{},âgé de {} ans".format(self.prenom,self.nom,self.age)
    


class DeuxiemePersonne:
    """Un petit exemple de classe"""
    def __init__(self,nom,prenom,age):
        """Exemple de constructeur (pour créer un objet)"""
        self.nom  = nom
        self.prenom = prenom
        self.age = age

    
    def __del__(self): #On empêche la suppression de l'objet en soulevant une erreur
        """Méthode appelée quand l'objet est supprimé ie (del mon_objet)"""
        #raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")
        print("C'est la fin ! On me supprime")
        
class Protege:
    """Classe possédant une méthode particulière d'accès à ses attributs : Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None """
    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.c = 3
        
    def __getattr__(self,nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle cette méthode : on affiche une alerte"""
        print("Alerte ! Il n'y a pas d'attribut {} ici mais 3 attributs: a = {}, b = {}, c = {}".format(nom, self.a,self.b,self.c))
        
    def __setattr__(self,nom_attr,val_attr):
        """Méthode appeléequand on fait objet.nom_attr=val_attr. On se charge d'enregistrer l'objet"""
        object.__setattr__(self,nom_attr,val_attr) #plutôt que self.nom_attr = val_attr, cela crée une boucle infinie
        
    def __delattr__(self,nom_attr):
        """On ne peut supprimer d'attribut, on lève l'exception AttributeError"""
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")
        #object.__delattr__(self,nom_attr)
        #print("L'attribut {} est supprimé.".format(nom_attr)) #Quand on refait objet.nom_attr, __getattr__ donne une boucle infinie car set.nom_attr n'existe plus
        
        """Si dans cette méthode on souhaite supprimer l'attribut il faut faire object.__delattr__(self,nom_attr) et non del self.nom_attr : sinon on crée une boucle infinie"""

""" Utilisation de chaine de caractères comme nom d'attribut et non objet.attribut
    objet.nom est semblable à getattr(objet,"nom")
    objet.nom = val ou objet.__set__attr__("nom",val) est semblable à setattr(objet,"nom",val)
    del objet.nom ou objet.__delattr__("nom") est semblable à delattr(objet,"nom")
    Renvoie True si l'attribut existe et False sinon ==> hasattr(objet,"nom")"""

"""METHODES DE CONTENEUR"""
class Zdict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
    
    def __getitem__(self,index):
        """Cette méthode spéciale est appelée quand on fait objet[index]. Elle redirige vers self.dictionnaire[index]"""
        return self._dictionnaire[index]
    
    def __setitem__(self,index,valeur):
        """Cette méthode est appelée quand on écrit objet[index]=valeur. On redirige vers self._dictionnaire[index]=valeur"""
        self._dictionnaire[index]=valeur
        
    def __delitem__(self,index):
        del self._dictionnaire[index]
    
    def __repr__(self):
        return "Voici la représentation {}.".format(self._dictionnaire)
        
    def __str__(self):
        return "Voici la chaine de caractères {}".format(self._dictionnaire)
    
    def __del__(self):
        print("Je supprime {}.".format(self._dictionnaire)) #Il supprime quand même le dictionnaire 
        
    def __contains__(self,index): 
        return index in self._dictionnaire.keys()

    def __len__(self):
        return len(self._dictionnaire)


    
#ma_liste = [1,2,3,4]
#8 in ma liste revient au même que ma_liste.__contains__(8)

#len(objet) équivaut à objet._len()_


"""METHODES MATHEMATIQUES"""
class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes et de secondes"""
    def __init__(self,min=0,sec=0):
        """Constructeur de la classe"""
        self.min = min #Nombre de minutes
        self.sec = sec #Nombre de secondes
        
    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min,self.sec)
    
    def __add__(self,objet_a_ajouter): #pour faire par exple à d1 + 4 (rajouter 4s à d1)
        """L'objet à ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        #On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        #On ajoute la durée
        nouvelle_duree.sec += objet_a_ajouter
        #Si le nbre de secondes >= 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        #On renvoie la nouvelle durée
        return nouvelle_duree

    """Sur le même modèle on a aussi 
    __sub__ ==> soustraction
    __mul__ ==> multiplication
    __truediv__ ==> / ie division flottante 
    __floordiv__ ==> // ie division entière
    __mod__ ==> % ie modulo
    __pow__ ==> ** ie puissance"""
    
    def __radd__(self,objet_a_ajouter): #pour faire par exple 4 + d1 et obtenir le même résultat que d1 + 4
        """Cette méthode est appelée si on écrit 4 + objet et que le premier objet (4 dans cet exemple) ne sait pas comment ajouter le second. On se contente de rediriger sur __add__ puisque, ici, cela revient au même : l'opération doit avoir le même résultat, posée dans un sens ou dans l'autre"""
        
        return self + objet_a_ajouter


    """Opérateurs +=, -=, ... ==> on préfixe les noms de méthode par i"""

    def __iadd__(self,objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        #On travaille directement sur self cette fois
        #on ajoute la durée
        self.sec += objet_a_ajouter
        #Si le nombre de secondes >= 60
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        #on renvoie self (type durée où l'on a déjà rajouter "objet_a_rajouter")
        return self

    """METHODES DE COMPARAISON"""

    """ == ==> def __eq__(self,objet_a_comparer):
    != ==> def __ne__(self,objet_a_comparer):
    >  ==> def __gt__(self,objet_a_comparer):
    >= ==> def __ge__(self,objet_a_comparer):
    <  ==> def __lt__(self,objet_a_comparer):
    <= ==> def __le__(self,objet_a_comparer):"""
    
    def __eq__(self,autre_duree):
        """Test si self et autre_duree sont égales"""
        return self.sec == autre_duree.sec and self.min == autre_duree.min
    
    def __gt__(self,autre_duree):
        """Test si self > autre_duree"""
        #On calcule le nombre de secondes de self et autre_duree
        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = autre_duree.sec + autre_duree.min*60
        return nb_sec1 > nb_sec2

"""METHODES SPECIALES UTILES A PICKLE"""
"""Quand on veut enregistrer l'objet à l'aide du module pickle, __getstate__ va être appelée juste avant l'enregistrement
Si aucune méthode __getstate__ n'est définie, pickle enregistre le dictionnaire des attributs de l'objet à enregistrer, il est contenu dans objet.__dict__. Sinon pickle enregistre dans le fichier la valeur renvoyée par __getstate__ (généralement un dictionnaire d'attributs modifié)"""

class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""
    
    def __init__(self):
        """Constructeur de notre objet"""
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une_autre_valeur"
        self.attribut_temporaire = 5
    
    def __getstate__(self):
        """renvoie le dictionnaire d'attributs à sérialiser"""
        dict_attr = dict(self.__dict__)
        dict_attr["attribut_temporaire"] = 0
        return dict_attr #pickle enregistre dict_attr au lieu de self.__dict__

    """La méthode __setstate__ est appelée au moment de désérialiser l'objet. Concrètement, si on récupère un objet à partir d'un fichier sérialisé, __setstate__ sera appelée après la récupération du dictionnaire des attributs si la méthode __setstate__ est définie"""

    def __setstate__(self,dict_attr):
        """Méthode appelée lors de la désérialisation de l'objet"""
        dict_attr["attribut_temporaire"]=0
        self.__dict__ = dict_attr #Dict_attr est récupéré, modifié puis est placé dans l'objet 

os.system("pause")