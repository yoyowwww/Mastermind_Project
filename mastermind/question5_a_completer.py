### Module importée
from random import randint
import copy # question 3

### Fonctions

## Question 1 :
# version itérative :
def genere_configuration(n_couleurs =6, p_positions =4):
    """
    Entrées : entier
    Sortie : liste d'entier
    Renvoie une configuration aléatoire générée uniformément sur l'ensemble de
    toutes les configurations possibles
    >>> genere_configuration()
    >>> [1,3,6,2]
    """
    ListFinale = []
    for i in range(p_positions):
        ListFinale.append(randint(1, n_couleurs))
    return ListFinale

#version récursive :
def genere_configuraton_rec(n_couleurs = 6, p_positions = 4):
    """
    Entrées : entier
    Sortie : liste d'entier
    Renvoie une configuration aléatoire générée uniformément sur l'ensemble de
    toutes les configurations possibles
    >>> genere_configuration()
    >>> [1,3,6,2]
    """
    if p_positions == 0:
        return []
    else:
        return [randint(1, n_couleurs)] + genere_configuraton_rec(n_couleurs, p_positions - 1)
    
## Question 2 :
def n_bien_places(configuration1,configuration2):
    """ 
    Entrées :listes (configurations)
    Sortie:entier
    Calcule le nombre de couleurs communes aux deux configurations et en même
    position
    >>> n_bien_places([1,2,3,4],[1,2,3,4])
    4
    >>> n_bien_places([1,2,3,4],[1,3,2,4])
    2
    >>> n_bien_places([1,2,3,4],[4,3,2,1])
    0
    """
    assert len(configuration1) == len(configuration2), 'Les 2 listes doivent être de la même taille'
    count = 0
    for i in range(len(configuration1)):
        if configuration1[i] == configuration2[i]:
            count += 1
    return count
## Question 3 :

def n_pions_communs(configuration1 ,configuration2):
    """ 
    Entrées 2 listes (configurations 1 & 2)
    Sortie : entier
    Calcule le nombre de couleurs communes aux deux configurations incluant les
    répétitions
    >>> n_pions_communs([4,2,5,6],[6,5,2,4])
    4
    >>> n_pions_communs([4,2,5,6],[1,1,4,5])
    2
    >>> n_pions_communs([4,2,5,6],[1,1,1,1])
    0
    """
    assert len(configuration1) == len(configuration2), 'Les 2 listes doivent être de la même taille'
    count = 0
    for i in range(len(configuration1)):
        if configuration1[i] in configuration2:
            count += 1
    return count


## Question 4 :
def n_noirs_blancs(configuration1,configuration2):
    """ 
    Entrées 2 listes (configurations 1 & 2)
    Sortie : tuple (nombre de fiche noire, nombre de fiche blanche)
    Calcule le nombre de pions bien placés et bonnes couleurs (fiche noire) et
    nombre de bonne couleur mais mal positionné (fiche blanche)
    >>> n_noirs_blancs([4,2,5,6],[4,5,2,4])
    (1, 2)
    """
    noir = n_bien_places(configuration1, configuration2)
    blanc = n_pions_communs(configuration1, configuration2)
    return (noir, blanc - noir)

## Question 5 :
def joueur_devine(n_couleurs = 6, p_positions = 4,n_essais = 10):
    """ 
    Entrées :
        * n_couleurs : int
        * p_positions : int
        * n_essais : int
    Sortie : None
    Fait intéragir l'utilisdateur pour le faire jouer.
    """
    configuration_cachee = genere_configuration(n_couleurs, p_positions)
    print("Taille de la configuration cachée : ",p_positions)
    i = n_essais #nombre d'essais déjà réalisés
    trouve = False # variable booléenne qui indique si la configuration a été trouvée

    while (not(trouve) and i > 0) :
        i = i - 1
        m = input("Essai (entree des chiffres séparés par un espace) "+ str(i) + " : ")
        # conversion de la configuration entrée par le joueur dans le bon type
        configuration_proposee = [int(elt) for elt in m.split(" ")]
        # tester la reponse
        reponse = n_noirs_blancs(configuration_cachee, configuration_proposee)
        print("  ",reponse)
        trouve = configuration_cachee == configuration_proposee # renvoie vraie quand la réponse est trouvée

    if trouve:
        print("Bravo vous avez trouvé en " + str(i) + " essais")
    else :
        print ("Perdu vous avez épuisé vos " + str(i) + " tentatives , bonne réponse = " + str(configuration_cachee) )

## PARTIE B
#  Question 2
def enumerer_configs(n_couleurs = 6, p_positions = 4):
    """
    Entées : 
        * n_couleurs : int
        * p_positions : int
    Sortie ; List
    renvoie une liste de toutes les combianisons possibles avec les n_couleurs et p_positions
    """
    if(p_positions == 0):
        return [[]]
    else:
        listFinale = []
        for elt in enumerer_configs(n_couleurs, p_positions - 1):
            for i in range(1, n_couleurs + 1):
                listFinale.append(elt + [i])
        return listFinale
    
#  Question 3
def reduction_configs_possibles(configs_possibles, tentative, n_bien_places, n_mal_places):
    """
    Entrées : 
        * configs_possibles : list
        * tentative : list
        * n_bien_places : int
        * n_mal_places : int
    Sortie ; list
    Renvoie le nombre de configurations candidates au prochain tour
    """
    listFinale = []
    for elt in configs_possibles:
        if n_noirs_blancs(elt, tentative) == (n_bien_places, n_mal_places):
            listFinale.append(elt)
    return listFinale


        
### Programme principal :
#joueur_devine()
print(genere_configuration())
