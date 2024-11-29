# projet de Ilian Touati 1ère année licence info 

from random import *
from math import *
#from main import UnitTest

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
    while jeu_ordi != False :
            x = millieu(debut,fin) 
            print('le millieu : ',x)
            y = indication

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


def chiffre_aléatoire():  
    return randint(1,100)

def long(liste):
    return len(liste)

print('la longueur de la liste',long(liste_Chiffre()))

def user(le_chiffre,saisie_user,liste): 
    trouvé = False
    while trouvé != True :
        if saisie_user > liste[0] and saisie_user < long(liste)+1:
            if saisie_user == le_chiffre :
                trouvé = True 
            
            elif saisie_user > le_chiffre : 
                return ('-')
            
            elif saisie_user < le_chiffre: 
                return ('+')

        else : 
            return ('hors intervalle')
            
    return True

def demande_chiffre_user():
    proposition_user = int(input(' : ')) 
    return proposition_user

def jeu_user(): 
    jeu = True 
    x = chiffre_aléatoire() 
    while jeu != False : 
        lancement = user(x,demande_chiffre_user(),liste_Chiffre()) 
        print(lancement)
        if lancement == True : 
            jeu = True 

def jeu_globale():
    # le jeu :
    jeu_globale = True 
    # Partie 1 tu doit trouver le chiffre générer par la machine 

    while jeu_globale != False : 
        
        print("répondre par : Jouer/Machine")
        Init_game = input("voulez vous jouez ou faire jouer la machine ? ")
        
        if Init_game == 'Jouer' or Init_game == 'JOUER' or Init_game == 'jouer' :
            jeu_user()

        else :
            jeu_ordi()

        End_game = input("voulez vous rejouez ou faire jouer l'ordinateur ? oui/non : ")  

        if End_game == 'non' or End_game == 'NON' or End_game == 'Non' : 
            jeu_globale = False 

    print("merci d'avoir jouer au jeu")   

print('fin des test----')
jeu_globale()
        
 