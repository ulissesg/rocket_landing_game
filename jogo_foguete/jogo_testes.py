from jogo import *
import unittest

class Test(unittest.TestCase):

    def test_cima_plataforma(self):
        self.assertEqual(cima_plataforma(Jogo(Foguete(LIMITE_BAIXO - ))),
                         criar_lista(Personagem(599, 79, -1, -1, AVIAO), Personagem(301, 201, 1, 1, PLATAFORMA),
                                     Personagem(301, 71, 1, 1, ASTEROIDE)))