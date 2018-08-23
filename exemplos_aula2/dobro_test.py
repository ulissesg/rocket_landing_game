import unittest
from dobro import *

class Test(unittest.TestCase):

    def test_dobro(self):
        self.assertEqual(dobro(4), 8)
        self.assertEqual(dobro(-2), -4)
        self.assertEqual(dobro(0), 0)

    def test_raiz_quadrada(self):
        pass

    def test_numero_perfeito(self):
        pass


res = 50
print("hello " + str(res))

# unittest.main()  # não excluir (a menos que esteja rodando como unit test no PyCharm)
