### Module importée
import copy

## Fonctions :


def enumerer_configs(n_couleurs=6, p_positions=4):
    """
    Entrées : 
        * n_couleurs : int
        * p_positions : int
    Sortie ; List
    renvoie une liste de toutes les combinaisons possibles avec les n_couleurs et p_positions
    """
    if (p_positions == 0):
        return [[]]
    else:
        listFinale = []
        for elt in enumerer_configs(n_couleurs, p_positions - 1):
            for i in range(1, n_couleurs + 1):
                listFinale.append(elt + [i])
        return listFinale


def n_bien_places(configuration1,configuration2):
    """
    Entrées : listes (configurations)
    Sortie:entier
    Calcule le nombre de couleurs communes aux deux configurations et en même
    position

    ------

    >>> n_bien_places([1,2,3,4],[1,2,3,4])
    4
    >>> n_bien_places([1,2,3,4],[1,3,2,4])
    2
    >>> n_bien_places([1,2,3,4],[4,3,2,1])
    0
    """
    good = 0 # initialisation de la variable qui compte les bonnes positions et bonnes couleurs
    p_positions =(len(configuration1))
    for i in range (p_positions):
        if configuration1[i] == configuration2[i] :
            good = good + 1
    return good

def n_pions_communs(configuration_1 ,configuration_2):
    """
    Entrées 2 listes (configurations 1 & 2)
    Sortie : entier
    Calcule le nombre de couleurs communes aux deux configurations incluant les
    répétitions

    ------

    >>> n_pions_communs([4,2,5,6],[6,5,2,4])
    4
    >>> n_pions_communs([4,2,5,6],[1,1,4,5])
    2
    >>> n_pions_communs([4,2,5,6],[1,1,1,1])
    0
    """
    configuration_2_copy = copy.deepcopy(configuration_2)
    n_communs = 0
    for c in configuration_1 :
        if c in configuration_2_copy :
            n_communs = n_communs +1
            configuration_2_copy.remove(c)
    return n_communs

def n_noirs_blancs(configuration_1,configuration_2):
    """ 
    Entrées 2 listes (configurations 1 & 2)
    Sortie : tuple (nombre de fiche noire, nombre de fiche blanche)
    Calcule le nombre de pions bien placés et bonnes couleurs (fiche noire) et
    le nombre de bonne couleur mais mal positionné (fiche blanche)
    
    ------

    >>> n_noirs_blancs([4,2,5,6],[4,5,2,4])
    (1, 2)
    """
    a = n_bien_places(configuration_1,configuration_2)
    b = n_pions_communs(configuration_1,configuration_2)
    return(a,b-a)

def reduction_configurations_possibles(configs_possibles, tentative, n_bien_places,n_mal_places):
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

def machine_devine(n_couleurs=6, p_positions=4, n_essais=10):
    # génére toutes les configurations possibles :
    configurations_possibles = enumerer_configs(n_couleurs ,p_positions)

    # interface utilisateur :
    print("Couleurs de 1 à ",n_couleurs)
    print("Taille de la configuration cachée : ",p_positions)

    # initialisation
    i = 0 # nombre d ’essai
    trouve = False

    while (not(trouve) and (i < n_essais)) :
        i = i + 1
        tentative = configurations_possibles[0]
        configurations_possibles.remove(tentative)

        reponse = input("Essai "+ str(i)+ " "+ str(tentative)+" : " )
        reponse_joueur = [int(c) for c in reponse.split()]

        trouve = (reponse_joueur[0] == p_positions)

        if not(trouve) :
            n_bien_places = reponse_joueur[0]
            n_mal_places = reponse_joueur[1]
            configurations_possibles = reduction_configurations_possibles(configurations_possibles,tentative,n_bien_places,n_mal_places)


    if trouve :
        print("Bravo la machine a trouvé en " + str(i)+ " essais " + str(tentative))
    else :
        print ("Perdu la machine a épuisé ses " + str(i) + " tentatives")

### programme principal pour tester fonctions
machine_devine()

