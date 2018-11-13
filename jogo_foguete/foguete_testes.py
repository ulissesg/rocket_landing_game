from foguete import *
import unittest

class Test(unittest.TestCase):

    def test_move_foguete(self):
        self.assertEqual(move_foguete(FOGUETE_INICIAL),
                         Pc_simples(FOGUETE_INICIAL.x + FOGUETE_INICIAL.dx, FOGUETE_INICIAL.y + FOGUETE_INICIAL.dy,
                                    FOGUETE_INICIAL.dx, FOGUETE_INICIAL.dy + ACELERACAO_FOGUETE_CIMA))

        self.assertEqual(move_foguete(FOGUETE_MEIO),
                         Pc_simples(FOGUETE_MEIO.x + FOGUETE_MEIO.dx, FOGUETE_MEIO.y + FOGUETE_MEIO.dy,
                                    FOGUETE_MEIO.dx, FOGUETE_MEIO.dy - ACELERACAO_FOGUETE))

        self.assertEqual(move_foguete(FOGUETE_FINAL), FOGUETE_FINAL)

        # Teste no limite direito
        self.assertEqual(move_foguete(Pc_simples(LIMITE_DIREITA , LIMITE_BAIXO //2, 2, -5)),
                         Pc_simples(LIMITE_DIREITA - 1, LIMITE_BAIXO //2 + (-5), 2, -5 - ACELERACAO_FOGUETE))

        self.assertEqual(move_foguete(Pc_simples(LIMITE_DIREITA , LIMITE_BAIXO //2, 2, 5)),
                         Pc_simples(LIMITE_DIREITA - 1, LIMITE_BAIXO //2 + 5, 2, 5 + ACELERACAO_FOGUETE_CIMA))

        # Teste no limite esquerdo
        self.assertEqual(move_foguete(Pc_simples(LIMITE_ESQUERDA , LIMITE_BAIXO //2, 2, -5)),
                         Pc_simples(LIMITE_ESQUERDA + 1, LIMITE_BAIXO //2 + (-5), 2, -5 - ACELERACAO_FOGUETE))

        self.assertEqual(move_foguete(Pc_simples(LIMITE_ESQUERDA , LIMITE_BAIXO //2, 2, 5)),
                         Pc_simples(LIMITE_ESQUERDA + 1, LIMITE_BAIXO //2 + 5, 2, 5 + ACELERACAO_FOGUETE_CIMA))



    def test_trata_tecla(self):
        # tecla cima
        self.assertEqual(trata_tecla(FOGUETE_INICIAL, TECLA_CIMA),
                         Pc_simples(FOGUETE_INICIAL.x, FOGUETE_INICIAL.y, FOGUETE_INICIAL.dx, -DDY))
        # tecla direita
        self.assertEqual(trata_tecla(FOGUETE_INICIAL, TECLA_DIREITA),
                         Pc_simples(FOGUETE_INICIAL.x, FOGUETE_INICIAL.y, DDX, FOGUETE_INICIAL.dy))

        # tecla esquerda
        self.assertEqual(trata_tecla(FOGUETE_INICIAL, TECLA_ESQUERDA),
                         Pc_simples(FOGUETE_INICIAL.x, FOGUETE_INICIAL.y, -DDX, FOGUETE_INICIAL.dy))

        self.assertEqual(trata_tecla(FOGUETE_INICIAL, pg.K_BACKSPACE), FOGUETE_INICIAL)

    def test_trata_solta_tecla(self):

        self.assertEquals(trata_solta_tecla(FOGUETE_MEIO, TECLA_CIMA),
                          Pc_simples(FOGUETE_MEIO.x, FOGUETE_MEIO.y, FOGUETE_MEIO.dx, DY))

        self.assertEquals(trata_solta_tecla(FOGUETE_MEIO, TECLA_ESQUERDA),
                          Pc_simples(FOGUETE_MEIO.x, FOGUETE_MEIO.y, 0, FOGUETE_MEIO.dy))

        self.assertEquals(trata_solta_tecla(FOGUETE_MEIO, TECLA_DIREITA),
                          Pc_simples(FOGUETE_MEIO.x, FOGUETE_MEIO.y, 0, FOGUETE_MEIO.dy))

        self.assertEquals(trata_solta_tecla(FOGUETE_MEIO, pg.K_BACKSPACE), FOGUETE_MEIO)