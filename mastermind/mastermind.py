from random import randint

def genere_configuration(n_couleurs=6, p_positions=4) ->list:
    """
        Entrée : n_couleurs : int
                 p_positions : int
        Renvoie une liste de couleur généré alèatoirement de len p_positions
    """
    return [randint(0,n_couleurs) for i in range(p_positions)]

def genere_configurationRec(n_couleurs=6, p_positions=4) ->list:
    """
        Entrée : n_couleurs : int
                 p_positions : int
        Renvoie une liste de couleur généré alèatoirement de len p_positions
    """
    if p_positions == 1:
        return [randint(0, n_couleurs)]
    else:
        return [randint(0, n_couleurs)] + genere_configurationRec(n_couleurs, p_positions - 1)

def n_bien_places(configuration_1:list, configuration_2:list):
    """ Renvoie le nombre d'éléments bien placés entre config1 et config2, càd le nbre d'éléments qui sont les mêmes
    """
    assert len(configuration_1) == len(configuration_2)
    return [configuration_1[i] == configuration_2[i] for i in range(len(configuration_1))].count(True)


##TEST

tab1 = genere_configuration()
tab2 = genere_configurationRec()
print(tab1)
print(tab2)
print(n_bien_places(tab1, tab2))