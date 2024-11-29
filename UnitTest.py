import unittest
from main import liste_Chiffre, millieu, chiffre_aléatoire, user,indication_user,demande_chiffre_user

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

class test_fonction_ordi(unittest.TestCase):

        def test_fonction_millieu(self):
            self.assertTrue(millieu(0,100) == 50)
            

class test_entree_user_userGame(unittest.TestCase):
        def test_saisie_victorieuse(self):
            y = chiffre_aléatoire()
            x = demande_chiffre_user()
            self.assertTrue(x==y)
        
        def test_saisie_chiffre_supérieur(self):
            x = user(60,70,liste_Chiffre())
            self.assertTrue(x=='-')
        
        def test_saisie_chiffre_inférieur(self):
            x = user(60,30,liste_Chiffre())
            self.assertTrue(x=='+')
        
        def test_saisie_superieur_intervalle(self):
             x = user(60,150,liste_Chiffre())
             self.assertTrue(x=='hors intervalle')
        
        def test_saisie_inferieur_intervalle(self):
             x = user(60,-1,liste_Chiffre())
             self.assertTrue(x=='hors intervalle')






if __name__ == '__main__':
    unittest.main()
