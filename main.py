# projet de Ilian Touati 1ère année licence info 

from random import *
from math import *
#from main import UnitTest

# Fonction utilisé pour l'ordinateur 
def liste_Chiffre():
    liste_0à100 = []
    for i in range(1,101):
        liste_0à100.append(i)
    return liste_0à100



def recherche_dichotomique_ordi(tab): 
    elemT = False
    debut = 0 # le chiffre 1
    fin = len(tab) # le chiffre 100

    while elemT != True : 
        millieu = (debut+fin)//2 # le chiffre 50
        print(":" ,millieu,"?")
        #print('fin : ',fin)
        #print('début : ',debut)
        réponse = str(input("? +/-/trouver" ' : '))
    
        if debut==fin or réponse == "trouver":
            print("j'ai trouvé votre chiffre ! ")
            elemT = True
        
        if  réponse == "-" : 
            fin = millieu

        elif réponse == "+" :
            debut = millieu 
            

    return "trouvé"


# Fonction utilisé pour l'utilisateur

def chiffre_aléatoire():  
    return randint(0,100)

def recherche_dichotomique_user(le_chiffre): 
    trouvé = False
    while trouvé != True :
        nombre = int(input('ton chiffre : '))
        if nombre == le_chiffre :
            print('gagné')
            break 
        
        elif nombre > le_chiffre : 
            print('moins')
        
        else : 
            print('plus')
            
    return trouvé 
    
    
# le jeu :
jeu = True 
# Partie 1 la machine doit trouver le chiffre auxquel tu pense 
'''
while jeu != False : 
    print("répondre par : Jouer/Machine")
    Init_game = input("voulez vous jouez ou faire jouer la machine ? ")
    if Init_game == 'Jouer' or Init_game == 'JOUER' or Init_game == 'jouer' :
        recherche_dichotomique_user(chiffre_aléatoire())
    
    else : 
        recherche_dichotomique_ordi(liste_Chiffre())
        
    # condition de fin de boucle While 

    End_game = input("voulez vous rejouez ou faire jouer l'ordinateur ? oui/non : ")  

    if End_game == 'non' or End_game == 'NON' or End_game == 'Non' : 
        jeu = False 

print("merci d'avoir jouer au jeu")   

'''



