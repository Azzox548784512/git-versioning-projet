import unittest
from unittest.mock import patch
from main import liste_Chiffre, recherche_dichotomique_ordi, chiffre_aléatoire, recherche_dichotomique_user

class TestFonctionsOrdi(unittest.TestCase):
    def test_liste_Chiffre(self):
        # Test que la liste contient bien les chiffres de 0 à 99
        self.assertEqual(liste_Chiffre(), list(range(100)))

    @patch('builtins.input', side_effect=['-', '+', '-', 'trouver'])
    def test_recherche_dichotomique_ordi(self, mock_input):
        # Test de la recherche dichotomique de l'ordinateur
        self.assertTrue(recherche_dichotomique_ordi(liste_Chiffre()))


class TestFonctionsUtilisateur(unittest.TestCase):
    def test_chiffre_aléatoire(self):
        # Test que le nombre généré est bien entre 0 et 100
        nombre = chiffre_aléatoire()
        self.assertTrue(0 <= nombre <= 100)

    @patch('builtins.input', side_effect=['50', '75', '25', 'gagné'])
    def test_recherche_dichotomique_user(self, mock_input):
        # Test de la recherche dichotomique pour l'utilisateur
        with patch('main.chiffre_aléatoire', return_value=50):
            recherche_dichotomique_user(50)  # Ici 50 est l'entrée simulée par mock_input


if __name__ == '__main__':
    unittest.main()
