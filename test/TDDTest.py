import unittest
from testmain import entree_ind, ordinateur,liste_100,generation_aleatoire


class Testfonction(unittest.TestCase) :

    def test_liste_100(self):
        tab = liste_100()
        tab_test= list(range(1,101))
        for i in range(0,100):
            print(i)
            self.assertEqual(tab[i], tab_test[i])

    def test_generation_aleatoire(self):
        for i in range(100):
            v = generation_aleatoire()
            self.assertTrue(v >= 1)
            self.assertTrue(v <= 100)

    def test_trouvé(self):
        pass

class test_entree_user_ordi(unittest.TestCase) : 
    
    def test_ind_user(self):
        x = entree_ind()
        self.assertTrue()




if __name__ == '__main__':
    unittest.main()