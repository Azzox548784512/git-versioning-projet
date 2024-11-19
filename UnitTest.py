import unittest
from main import liste_Chiffre, recherche_dichotomique_ordi, chiffre_aléatoire, recherche_dichotomique_user

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

class test_ordi(unittest.TestCase):

    def test_fonction_ordi(self):
        x = recherche_dichotomique_ordi(liste_Chiffre())
        self.assertEqual(x,"trouvé")

class test_entree_user(unittest.TestCase):
    def Vérification_saisie_user(self):
        x = recherche_dichotomique_user(chiffre_aléatoire())
        self.assertTrue()


if __name__ == '__main__':
    unittest.main()
