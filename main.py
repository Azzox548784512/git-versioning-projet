# projet de Ilian Touati 1ère année licence info 

from random import *
from math import *
#from main import UnitTest

# ---------------------------------------------------THE FUNCTIONS---------------------------------------------------------------


# Fonction utilisé pour l'ordinateur quand il joue / fait joué

def liste_Chiffre():
    liste_0à100 = []
    for i in range(1,101):
        liste_0à100.append(i)
    return liste_0à100


def millieu(debu,f1): # fonction qui permet de tester le millieu de l'ordinateur, quand on veut lui faire trouver le chiffre auxquel on pense 
    millieu = (debu+f1)//2
    return millieu 

    
def indication_user(): # fonction permettant à l'utilisateur de dire si le chiffre que l'ordinateur doit trouver est inf/sup/égale
    saisi = input('mettez votre indication pour la machine +/-/= : ')
    return saisi


# Fonction utilisé pour l'utilisateur

def chiffre_aléatoire():  
    return randint(1,100)

def user(le_chiffre,saisie_user,liste): 
    trouvé = False
    while trouvé != True :
        if saisie_user > liste[0] and saisie_user < liste[len(liste)+1]:
            if saisie_user == le_chiffre :
                trouvé = True 
            
            elif saisie_user > le_chiffre : 
                return ('-')
            
            elif saisie_user < le_chiffre: 
                return ('+')

        else : 
            return ('hors intervalle')
            
    return True
    
    
# ----------------------------------------------------THE GAME ----------------------------------------------------------------


# le jeu :
jeu_globale = True 
# Partie 1 tu doit trouver le chiffre générer par la machine 

while jeu_globale != False : 
    
    print("répondre par : Jouer/Machine")
    Init_game = input("voulez vous jouez ou faire jouer la machine ? ")

    if Init_game == 'Jouer' or Init_game == 'JOUER' or Init_game == 'jouer' :
        proposition_user = int(input(' : '))
        x = chiffre_aléatoire()
        print(x)
        while user(x,proposition_user,liste_Chiffre()) != True : 
            proposition_user = int(input(' : ')) # on demande un chiffre à l'utilisateur 
            lancement = user(x,proposition_user,liste_Chiffre()) # on fait trouner la fonction jusqu'a ce que la fonction retourne True 
            print(lancement) # montre ce que la fonction retourne 


# Partie 2 la machine doit trouver le chiffre auxquel tu pense
    
    else :
        # Variable utilisées
        jeu_ordi = True
        debut = 0
        fin = len(liste_Chiffre()) 

        # jeu par la machine
        while jeu_ordi != False :
            x = millieu(debut,fin) 
            print('le millieu : ',x)
            y = indication_user()

            if debut == fin or y == '=':
                print('votre chiffre était le : ',x)
                jeu_ordi = False 
                break

            else : 
                if y == '+' :
                    debut = x
                
                if y == '-' : 
                    fin = x

            #print('fin : ',fin)
            #print('début : ',debut)
                     
    # condition de fin de boucle While du jeu globale 

    End_game = input("voulez vous rejouez ou faire jouer l'ordinateur ? oui/non : ")  

    if End_game == 'non' or End_game == 'NON' or End_game == 'Non' : 
        jeu_globale = False 

print("merci d'avoir jouer au jeu")   



        
 