
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
        
        if debut+1 == fin :
            print('le chiffre auxquelles vous pensez est le : ',mid)
            jeu_ordi = False 
            break

        if indication == '+' :
            debut = mid+1
        elif indication == '-' : 
            fin = mid-1
        elif indication == '=' : 
            return mid
        else :
            print('!!CARACTÈRE NON VALIDE!!')
    return mid

def liste_Chiffre():
    liste_0à100 = []
    for i in range(1,101):
        liste_0à100.append(i)
    return liste_0à100

def longueur(liste):
    return len(liste)


def millieu(debu,f1): 
    millieu = (debu+f1)//2
    return millieu#,debu,f1

    
def indication_user(): 
    saisi = input('mettez votre indication pour la machine +/-/= : ')
    return saisi


print(ordi())