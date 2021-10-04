import os
import time

"""Le décorateur s'execute au moment de la définition et non lors de l'appel. Il prend en paramètre une fonction (celle qu'il modifie) et renvoie une fonction (qui peut être la même)"""

def mon_decorateur(fonction):
    """Premier exemple de décorateur"""
    print("Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
    return fonction #ici on renvoit la même fonction """salut() retourne 'salut'"""

"""On pourrait faire aussi fonction = decorateur(fonction)"""

@mon_decorateur #on fait savoir à Python que le décorateur est utilisé sur la fonction salut()
def salut():
    """Fonction modifiée par notre décorateur"""
    print("salut !")


def deuxieme_decorateur(fonction):
    """Notre décorateur: il va afficher un message avant l'appel de la fonction définie"""
    def fonction_modifiee():
        """Fonction que l'on va renvoyer. Il s'agit en fait d'une version un peu modifiée de notre fonction originellement définie. On se contente d'afficher un avertissement avant d'exécuter notre fonction originellement définie"""
        
        print("Attention ! On appelle {0}".format(fonction))
        return fonction()
    return fonction_modifiee

@deuxieme_decorateur
def bonjour():
    print("bonjour !")

bonjour()

def obsolete(fonction_origine):
    """Décorateur levant une exception pour noter que la fonction_origine est obsolète"""
    def fonction_modifiee():
        raise RuntimeError("la fonction {0} est obsolète !".format(fonction_origine))
    return fonction_modifiee

@obsolete
def bonsoir():
    print("bonsoir")


"""Un décorateur avec des paramètres"""
"""Pour gérer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre de secondes écoulées depuis le 1er janvier 1970 (habituellement). On va s'en servir pour calculer le temps mis par notre fonction pour s'éxecuter"""

def controler_temps(nb_secs):
    """Contrôle le temps mis par une fonction pour s'exécuter
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""
    
    def decorateur(fonction_a_executer):
        """Notre decorateur. C'est lui qui est appelé directement LORS DE LA DEFINITION de notre fonction (fonction_a_executer)"""
        
        def fonction_modifiee():
            """Fonction renvoyée par notre décorateur. Elle se charge de calculer le temps mis par la fonction à s'exécuter"""
            tps_avant = time.time() #Avant d'exécuter la fonction
            valeur_renvoyee = fonction_a_executer() #On execute la fonction #On execute la fonction
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format(fonction_a_executer,tps_execution))
            return valeur_renvoyee
        
        return fonction_modifiee
    
    return decorateur

@controler_temps(4)
def attendre():
    input("Appuyez sur Entrée ...")


"""Si l'on veut que fonction_modifiee prenne des parametres et que le decorateur continue à jouer son rôle ie que le decorateur s'execute pour n'importe quelle fonction, on met des parametres nommees et non nommees en paramètres de la fonction à executer et de la fonction modifiée"""


"""Décorateurs qui s'appliquent aux définitions de classe"""

def decorateur_classe(classe):
    print("Definition de la classe {0}".format(classe))
    return classe

@decorateur_classe
class Test :
    pass

"""Exple : les classes singleton sont des classes qui ne peuvent être instanciees qu'une seule fois
Autrement dit, on ne peut créer qu'un seul objet de cette classe"""
def singleton(classe_definie):
    instances = {} #Dictionnaires de nos instances singletons
    def get_instance():
        if classe_definie not in instances.keys() :
            #On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance

@singleton
class Test :
    pass

"""2e exple : vérification des types envoyés à une fonction"""
def controler_types(*a_args,**a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte une liste de paramètres indeterminés, étant donné que notre fonction pourra être appelée avec un nombre variable de paramètres et que chacun doit être contrôlé / les paramètres nommés sont un dico et les paramètres non nommés une liste"""
    
    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer fonction_modifiée"""
        def fonction_modifiee(*args,**kwargs):
            """Notre fonction modifiée. Elle se charge de contrôler les types qu'on lui passe en paramètres"""
            
            #La liste des paramètres attendus(a_args) doit être de même longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal au nbre reçu")
            #On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type {1}".format(i,a_args[i]))
            #On parcourt à présent la liste des paramètres reçu et nommés
            for cle in kwargs:
                    if cle not in a_kwargs:
                        raise TypeError("l'argument {0} n'a aucun type précisé".format(repr(cle)))
                    if a_kwargs[cle] is not type(kwargs[cle]):
                        raise TypeError("l'argument {0} n'est pas de type {1}".format(repr(cle),a_kwargs[cle]))
            return fonction_a_executer(*args,**kwargs)
        return fonction_modifiee
    return decorateur

@controler_types(int,int)
def intervalle(inf,sup):
    print("Intervalle de {0} à {1}".format(inf,sup))
    

os.system("pause")