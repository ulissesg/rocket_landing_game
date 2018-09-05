import unittest
from gato2 import *

class Test(unittest.TestCase):

    def test_mover(self):
        self.assertEqual(mover(0), 3)
        self.assertEqual(mover(3), 6)
        self.assertEqual(mover(6), 9)


    def test_trata_tecla(self):
        #caso em que é espaço
        self.assertEqual(trata_tecla(GATO_MEIO, pg.K_SPACE),  GATO_INICIAL)
        #caso em que não é espaço
        self.assertEqual(trata_tecla(GATO_MEIO, pg.K_a), GATO_MEIO)

    def test_final_da_tela(self):

        #passou dos limites
        self.assertEqual(final_da_tela(LARGURA), True)
        self.assertEqual(final_da_tela(LARGURA+DX), True)
        #ta dentro
        self.assertEqual(final_da_tela(LARGURA-DX), False)