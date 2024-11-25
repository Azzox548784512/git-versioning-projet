
import random 



'''
def recherche_dichotomique(tableau, valeur):
    gauche = 0
    droite = len(tableau) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2

        if tableau[milieu] == valeur:
            return milieu
        elif tableau[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return -1  # La valeur n'est pas dans le tableau
'''

def generation_aleatoire():
    x = random.randint(1,101)

    return x 

def liste_100(): # la liste des 100 chiffre compris entre 1 et 100 
    liste = []
    for i in range(1,101):
        liste.append(i)
    
    return liste

for i in range(1000) : 
    x = generation_aleatoire()
    if x == 101 :
        pass
        #print(x)
    


'''
trouvé = False 
while trouvé != True :
    saisie = input('vazy : ')
    x = ordinateur(liste_100(),saisie)
    print(x)
'''



