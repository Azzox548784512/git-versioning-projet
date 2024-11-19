
import random 


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

def generation_aleatoire():
    x = random.randint(1,100)

    return x 

def liste_100(liste=[]):
    for i in range(1,101):
        liste.append(i)
    
    return liste

x = liste_100

print(liste_100())

a = list(range(1,101))
print(a)