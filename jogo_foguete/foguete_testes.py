from foguete import *
import unittest

class Test(unittest.TestCase):

    def test_move_foguete(self):
        self.assertEqual(move_foguete(FOGUETE_INICIAL), Pc_simples(LIMITE_DIREITA//2, LIMITE_CIMA + DY, DX ,DY))
        self.assertEqual(move_foguete(FOGUETE_MEIO), Pc_simples(LIMITE_DIREITA//2, LIMITE_BAIXO//2 + DY, DX ,DY))
        self.assertEqual(move_foguete(FOGUETE_FINAL), FOGUETE_FINAL)


    def test_trata_tecla(self):
        self.assertEqual(trata_tecla(FOGUETE_INICIAL, TECLA_DIREITA), Pc_simples(LIMITE_DIREITA//2 + DDX, LIMITE_CIMA, DX ,DY))
        self.assertEqual(trata_tecla(FOGUETE_MEIO, TECLA_ESQUERDA), Pc_simples(LIMITE_DIREITA//2 - DDX, LIMITE_BAIXO//2, DX ,DY))

        # self.assertEquals(trata_tecla(Pc_simples(LIMITE_DIREITA//2, LIMITE_BAIXO, 2, 2), TECLA_CIMA),
        #                   Pc_simples(LIMITE_DIREITA//2, LIMITE_BAIXO, 2, 2))

        self.assertEquals(trata_tecla(Pc_simples(LIMITE_DIREITA, LIMITE_BAIXO//2, 2, 2), TECLA_DIREITA),
                          Pc_simples(LIMITE_DIREITA, LIMITE_BAIXO//2, 2, 2))

        self.assertEquals(trata_tecla(Pc_simples(LIMITE_ESQUERDA -10, LIMITE_BAIXO//2, 2, 2), TECLA_ESQUERDA),
                          Pc_simples(LIMITE_ESQUERDA -10, LIMITE_BAIXO//2, 2, 2))

        self.assertEquals(trata_tecla(Pc_simples(LIMITE_ESQUERDA, LIMITE_BAIXO, 2, 2), TECLA_CIMA),
                          Pc_simples(LIMITE_ESQUERDA, LIMITE_BAIXO, 2, 2))