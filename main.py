# projet de Ilian Touati 1ère année licence info 

from random import *
from math import *

def liste_Chiffre():
    liste_0à100 = []
    for i in range(1,101):
        liste_0à100.append(i)
    return liste_0à100

def millieu(debu,f1): 
    millieu = (debu+f1)//2
    return millieu 

    
def indication_user(): 
    saisi = input('mettez votre indication pour la machine +/-/= : ')
    return saisi

def ordi():
    jeu_ordi = True 
    debut = 0
    fin = longueur(liste_Chiffre())
    while jeu_ordi != False :
        #print('debut: ',debut)
        #print('fin',fin)
        mid = millieu(debut,fin)
        print('Ce chiffre ? : ',mid)
        indication = indication_user()
        
        if debut == fin :
            print('le chiffre auxquelles vous pensez est le : ',mid)
            jeu_ordi = False 
            break

        if indication == '+' :
            debut = mid+1
        elif indication == '-' : 
            fin = mid-1
        elif indication == '=' : 
            return "si t'es arrivé c que c'est bon"
        else :
            print('!!CARACTÈRE NON VALIDE!!')

    return "si t'es arrivé c que c'est bon"


def chiffre_aléatoire():  
    return randint(1,100)

def longueur(liste):
    return len(liste)

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
    while True:
        proposition_user = input('Veuillez entrer un chiffre : ')
        try:
            chiffre = int(proposition_user)
            return chiffre
        except ValueError:
            print("Entrée invalide. Veuillez entrer un chiffre entier.")

def redemande_user():
    re = int(input('votre chiffre invalide veuillez saisir un chiffre compris entre 1 et 100 : '))
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
    return 'valide'
             

def jeu_globale():
    jeu_actif = True

    while jeu_actif:
        print("Répondre par : Jouer/Machine")
        Init_game = input("Voulez-vous jouer ou faire jouer la machine ? ").strip().lower()

        if Init_game == "jouer":
            jeu_user()
        elif Init_game == "machine":
            print(ordi())
        else:
            print("Entrée invalide. Veuillez répondre par 'Jouer' ou 'Machine'.")
            continue

        while True:
            End_game = input("Voulez-vous rejouer ou faire jouer l'ordinateur ? oui/non : ").strip().lower()

            if End_game == "non":
                jeu_actif = False
                break
            elif End_game == "oui":
                break
            else:
                print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")

    print("Merci d'avoir joué au jeu !")
    return 'good'

        
 