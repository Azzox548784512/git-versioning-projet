import unittest
from main import liste_Chiffre, millieu, chiffre_aléatoire, user,indication_user,demande_chiffre_user, jeu_ordi,jeu_user,jeu_globale

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
            x = user(60,60,liste_Chiffre())
            self.assertTrue(x==True)
        
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

class test_fonction_globale(unittest.TestCase):

    def test_fonction_jeu_ordi_auto(self):
        jeu_ordi()
        pass
    def test_fonction_user_auto(self):
        jeu_user()
        pass
    def test_fonction_globale(self):
        pass


if __name__ == '__main__':
    unittest.main()
