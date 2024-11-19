import unittest
from testmain import recherche_dichotomique,liste_100,generation_aleatoire


class Testfonction(unittest.TestCase) :

    def test_liste_100(self):
        tab = liste_100()
        for i in range(1,101):
            self.assertEqual(tab[i], i)

    def test_generation_aleatoire(self):
        for i in range(100):
            v = generation_aleatoire()
            self.assertTrue(v >= 1)
            self.assertTrue(v <= 100)
    



if __name__ == '__main__':
    unittest.main()