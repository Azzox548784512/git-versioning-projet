import unittest
from main import liste_Chiffre, millieu, chiffre_aléatoire, user,indication_user,redemande_user,demande_chiffre_user, ordi,jeu_user,jeu_globale


class test_génération(unittest.TestCase):

    def test_liste_100(self):
        tab = liste_Chiffre()
        tab_test= list(range(1,101))
        for i in range(0,100):
            self.assertEqual(tab[i], tab_test[i])

    def test_generation_aleatoire(self):
        for i in range(100):
            v = chiffre_aléatoire()
            self.assertTrue(v >= 1)
            self.assertTrue(v <= 100)
            
    def test_fonction_millieu(self):
        self.assertTrue(millieu(0,100) == 50)

class test_entree_user_OrdiGame(unittest.TestCase):
    pass
            
class test_entree_user_userGame(unittest.TestCase):
        def test_saisie_victorieuse(self):
            self.assertTrue(user(60,60,liste_Chiffre())==True)
        
        def test_saisie_chiffre_supérieur(self):
            self.assertTrue(user(60,70,liste_Chiffre())=='-')
        
        def test_saisie_chiffre_inférieur(self):
            self.assertTrue(user(60,30,liste_Chiffre())=='+')
        
        def test_saisie_superieur_intervalle(self):
            self.assertTrue(user(60,150,liste_Chiffre())=='hors intervalle')
        
        def test_saisie_inferieur_intervalle(self):
            self.assertTrue(user(60,-1,liste_Chiffre())=='hors intervalle')
           
        

class test_fonction_globale(unittest.TestCase):

    def test_fonction_jeu_ordi_auto(self):
        self.assertTrue(ordi()=="si t'es arrivé c que c'est bon")

    
    def test_fonction_user_auto_valide(self):
        var = jeu_user()
        self.assertTrue(var=='valide')
    
        
    def test_fonction_globale(self):
        pass

if __name__ == '__main__':
    unittest.main()
