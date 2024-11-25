liste = list(range(1, 101))

def millieu(debu,f1):
    millieu = (debu+f1)//2
    return millieu 

    
def indication_user():
    saisi = input('mettez votre indication pour la machine +/-/= : ')
    return saisi


jeu = True
debut = 0
fin = len(liste) 
while jeu != False :
    x = millieu(debut,fin) 
    print('le millieu : ',x)
    y = indication_user()

    if debut == fin or y == '=':
        print('votre chiffre était le : ',x)
        jeu = False 
        break

    else : 
        if y == '+' :
            debut = x
        
        if y == '-' : 
            fin = x

    

    print('fin : ',fin)
    print('début : ',debut)
    
print("merci d'avoir joué au jeu ! ")

    