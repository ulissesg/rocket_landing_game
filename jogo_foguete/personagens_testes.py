from personagens import *
import unittest

class Test(unittest.TestCase):

    # def test_mover_avioes(self):
    #     self.assertEqual(mover_avioes(AVIAO_INICIAL),
    #                      Personagem(AVIAO_INICIAL.x + AVIAO_INICIAL.dx, AVIAO_INICIAL.y + AVIAO_INICIAL.dy,
    #                                 AVIAO_INICIAL.dx, AVIAO_INICIAL.dy + ACELERACAO_FOGUETE_CIMA))

    def test_mover_aviao(self):
        self.assertEqual(mover_aviao(AVIAO_INICIAL),
                         Personagem(AVIAO_INICIAL.x + AVIAO_INICIAL.dx, AVIAO_INICIAL.y + AVIAO_INICIAL.dy,
                                    AVIAO_INICIAL.dx, AVIAO_INICIAL.dy))