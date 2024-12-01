# projet de Ilian Touati 1ère année licence info 

from random import *
from math import *

def liste_Chiffre():
    liste_0à100 = []
    for i in range(1,101):
        liste_0à100.append(i)
    return liste_0à100

print('test----')
print('liste de chiffre de ses morts : ',liste_Chiffre())
la = len(liste_Chiffre())+1
print('la longueur de la liste +1 est : ',la)

def millieu(debu,f1): 
    millieu = (debu+f1)//2
    return millieu 

    
def indication_user(): 
    saisi = input('mettez votre indication pour la machine +/-/= : ')
    return saisi

def jeu_ordi(millieu,indication):
    jeu_ordi = True 
    while jeu_ordi != False :
        print('le millieu : ',millieu)
        
        if debut == fin or indication == '=':
            print('votre chiffre était le : ',millieu)
            jeu_ordi = False 
            break

        else : 
            if indication == '+' :
                debut = millieu
                
            if indication == '-' : 
                fin = millieu
    #print('fin : ',fin)
    #print('début : ',debut)


def chiffre_aléatoire():  
    return randint(1,100)

def longueur(liste):
    return len(liste)

print('la longueur de la liste',longueur(liste_Chiffre()))

def user(le_chiffre,saisie_user,liste): 
    trouvé = False
    while trouvé != True :
        #print(saisie_user)
        #print(liste[0])
        #print(long(liste)+1)
        if saisie_user >= liste[0] and saisie_user < longueur(liste)+1:
            if saisie_user == le_chiffre :
                trouvé = True 
            
            elif saisie_user > le_chiffre : 
                return ('-')
            
            elif saisie_user < le_chiffre: 
                return ('+')

        else :
            return('hors intervalle')
            
            
    return trouvé

def demande_chiffre_user():
    proposition_user = int(input(' : '))
    return proposition_user

def redemande_user():
    re = int(input('votre chiffre est hors intervalle veuillez saisir un chiffre compris entre 1 et 100 : '))
    return re

def jeu_user(): 
    jeu = True 
    x = chiffre_aléatoire()
    lancement = user(x,demande_chiffre_user(),liste_Chiffre()) 
    while jeu != False :
        print(lancement)  
        if lancement == 'hors intervalle':
            lancement = user(x,redemande_user(),liste_Chiffre())
    
        elif lancement == True : 
            jeu = False
        
        else : 
            lancement = user(x,demande_chiffre_user(),liste_Chiffre())
             

def jeu_globale():
    jeu_globale = True 

    while jeu_globale != False : 
        
        print("répondre par : Jouer/Machine")
        Init_game = input("voulez vous jouez ou faire jouer la machine ? ")
        
        if Init_game == 'Jouer' or Init_game == 'JOUER' or Init_game == 'jouer' :
            jeu_user()

        else :
            jeu_ordi(millieu(0,longueur(liste_Chiffre())),indication_user())

        End_game = input("voulez vous rejouez ou faire jouer l'ordinateur ? oui/non : ")  

        if End_game == 'non' or End_game == 'NON' or End_game == 'Non' : 
            jeu_globale = False 

    print("merci d'avoir jouer au jeu")   

print('fin des test----')

jeu_globale()
        
 