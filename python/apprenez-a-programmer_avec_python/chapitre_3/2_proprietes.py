import os

"""Une propriété se crée dans le corps de la classe. Il s'agit même d'une classe, son nom est property. Elle attend 4 paramètres, tous optionnels : méthode donnant accès à l'attribut, méthode modifiant l'attribut, méthode appelée quand on souhaite supprimer l'attribut (del objet.attribut), méthode appelée quand on demande de l'aide sur l'attribut"""

class Personne:
    """Classe définissant une personne caractérisée par son nom, son prénom, son age, son lieu de résidence"""
    
    def __init__(self, nom, prenom): #l'attribut lieu_residence ne fait ps partie des paramètres du constructeur
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Rouen" #Notez le souligné devant le nom
    
    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut'lieu_residence'"""
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence
    
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format(self.prenom,nouvelle_residence))
        self._lieu_residence = nouvelle_residence
        
    #On va dire à Pthon que notre attribut lieu_residence (et non _lieu_residence) pointe vers une propriété
    lieu_residence = property(_get_lieu_residence,_set_lieu_residence)
    
    """nom_propriete = property(methode_accesseur,methode_mutateur,methode_suppression,methode_aide)"""
    
os.system("pause")