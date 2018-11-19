from personagens import *
import unittest

class Test(unittest.TestCase):

    def test_mover_avioes(self):
        self.assertEqual(mover_personagens(L_PERSONAGEM_INICIAL),
                         criar_lista(Personagem(599, 49, -1, -1), Personagem(301, 201, 1, 1), Personagem(301, 401, 1, 1)))

    def test_mover_aviao(self): # fazer mais testes
        self.assertEqual(mover_personagem(PS_INICIAL),
                         Personagem(PS_INICIAL.x + PS_INICIAL.dx, PS_INICIAL.y + PS_INICIAL.dy,
                                    PS_INICIAL.dx, PS_INICIAL.dy))

        self.assertEqual(mover_personagem(PS_MEIO),
                         Personagem(PS_MEIO.x + PS_MEIO.dx, PS_MEIO.y + PS_MEIO.dy,
                                    PS_MEIO.dx, PS_MEIO.dy))