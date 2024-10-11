from random import *
from math import *
import unittest

class TestEntryUser :
    pass


class TestEntryComp : 
    def test_reponse_trouvee(self):
        pass

# Fonction utilisé pour l'ordinateur 
def liste_Chiffre():
    liste_1à100 = []
    for i in range(1,101):
        liste_1à100.append(i)
    return liste_1à100

def recherche_dichotomique_ordi(tab): 
    elemT = False
    debut = 0 # le chiffre 1
    fin = len(tab) # le chiffre 100
    print("votre réponse doit contenir uniquement + ou - ")
    while elemT != True and debut <= fin : 
        millieu = (debut+fin)//2 # le chiffre 50
        print(millieu,'?')
        réponse = str(input(' : '))
        if  réponse == "-" : 
            fin = millieu
            print(fin)

        elif réponse == "+" :
            debut = millieu 
            print(debut)

        else : 
            print('trouvé le chiffre était : ',millieu)
            elemT = True

    return True


# Fonction utilisé pour l'utilisateur

def chiffre_aléatoire():  
    return randint(1,101)

def recherche_dichotomique_user(tab,element):
    debut = 0 
    fin = len(tab)-1 
    trouvé = False
    mil = (debut+fin)//2
    while trouvé != True and debut <= fin :
        if tab[mil] == element :
            trouvé = True
        else :
            if element > tab[mil] : 
                debut = mil+1
            else :
                fin = mil-1
    if trouvé == True : 
        print("la valeur",element,"est au rang",mil)
    else : 
        print("la valeur",element,"n'est pas dans le tableau")




# le jeu :
jeu = True 
# Partie 1 la machine doit trouver le chiffre auxquel tu pense 
while jeu != False : 
    print("répondre par : Jouer/Machine")
    Init_game = input("voulez vous jouez ou faire jouer la machine ? ")
    if Init_game == 'Jouer' or Init_game == 'JOUER' or Init_game == 'jouer' :
        print("Random Number",chiffre_aléatoire())
        recherche_dichotomique_user(liste_Chiffre(),chiffre_aléatoire())
    
    else : 
        recherche_dichotomique_ordi(liste_Chiffre())   


    # condition de fin de boucle While 

    End_game = input("voulez vous rejouez ou faire jouer l'ordinateur ? oui/non : ")  

    if End_game == 'non' or End_game == 'NON' or End_game == 'Non' : 
        jeu = False 

print("merci d'avoir jouer au jeu")   










