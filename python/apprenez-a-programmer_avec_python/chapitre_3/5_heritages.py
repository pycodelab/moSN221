import os

"""HERITAGE SIMPLE"""
class A:
    """Classe A, pour illustrer notre exemple d'héritage"""
    pass #On laisse la définition vide, cen'est qu'un exemple

class B(A):
    """Classe B, qui hérite de A.
    Elle reprend les mêmes méthodes et attributs (dans cet exemple, la classe A ne possède de toute façon ni méthode ni attribut)"""
    pass

class Personne:
    """Classe représentant une personne"""
    def __init__(self,nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaine"""
        return "{0} {1}".format(self.prenom,self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial. Elle hérite de la classe Personne"""
    
    def __init__(self,nom,matricule):
        """Un agent se définit par son nom et son matricule"""
        Personne.__init__(self,nom) #Pour accéder à la méthode __init__ de la classe mère, on appelle explicitement le constructeur de Personne
        self.matricule = matricule
    
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaine"""
        return "Agent {0}, matricule {1}".format(self.nom,self.matricule)





issubclass(AgentSpecial,Personne)#Renvoie True si Agent Special hérite de Personne ==> True
issubclass(AgentSpecial, object)#True Agent Special hérite de la classe Object
issubclass(Personne,object)
issubclass(Personne,AgentSpecial) #False

"""isinstance permet de savoir si un objet est issu d'une classe ou de ses classes filles
    isinstance(objet,classe)"""

"""HERITAGE MULTIPLE"""
"""Au lieu d'hériter d'une seule classe, on peut hériter de plusieurs"""
"""class MaClasseHeritee(MaClasseMere1,MaClasseMere2)"""

"""EXCEPTIONS"""

"""object==>BaseException==>Exception==>XxxError (les exceptions erreur)"""
class MonException(Exception):
    """Exception levée dans un certain contexte... qui reste à définir"""
    def __init__(self,message):
        """On se contente de stocker le message d'erreur"""
        self.message = message
    def __str__(self):
        """On renvoie le message"""
        return self.message
    
class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration) n'a pas pu être analysé.
    
    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""
    
    def __init__(self,fichier,ligne,message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    
    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]:{}".format(self.fichier,self.ligne, self.message)
    
    

















os.system("pause")