from random import *
from math import *
import unittest

class TestEntryUser :
    pass


class TestEntryComp : 
    def test_reponse_trouvee(self):
        pass

def liste_Chiffre():
    liste_1à100 = []
    for i in range(1,101):
        liste_1à100.append(i)
    return liste_1à100



def recherche_dichotomique_ordi(tab): # pour l'ordinateur 
    elemT = False
    debut = 0 # le chiffre 1
    fin = len(tab) # le chiffre 100
    while elemT != True and debut <= fin : 
        millieu = (debut+fin)//2 # le chiffre 50
        print('plus grand, plus petit que : ',millieu,'?')
        réponse = str(input(' : '))
        if  réponse == 'plus petit' : 
            fin = millieu
            print(fin)

        elif réponse == 'plus grand' :
            debut = millieu 
            print(debut)

        elif debut == fin : 
            print('trouvé le chiffre était : ',millieu)
            elemT = True

    return True

def chiffre_aléatoire(): # pour l'utilisateur 
    return randint(1,101)

print('chiffre aléatoire',chiffre_aléatoire())

def recherche_dichotomique_user(tab,element):
    debut = 0 
    fin = len(tab)-1 
    trouvé = False

    while trouvé != True and debut <= fin :
        










