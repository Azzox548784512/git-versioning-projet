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



def recherche_dichotomique(tab): # pour l'ordinateur 
    elemT = False
    debut = 0 # le chiffre 1
    fin = len(tab) # le chiffre 100
    while elemT != True : 
        réponse = str(input('plus grand, plus petit ?'))
        millieu = len(tab)//2 # le chiffre 50
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
recherche_dichotomique(liste_Chiffre()) 








