from jogo import *
import unittest

class Test(unittest.TestCase):

    def test_colidem(self):
        self.assertEqual(colidem(Personagem(200, 400, 0, 0, 4), Personagem(210, 410, 0, 0, 1)), True)
        self.assertEqual(colidem(Personagem(200, 400, 0, 0, 4), Personagem(210, 410, 0, 0, 3)), False)
        self.assertEqual(colidem(Personagem(200, LIMITE_BAIXO, 0, 0, 4), Personagem(210, LIMITE_BAIXO, 0, 0, 1)), True)

    def test_colide_algum_ps(self):
        self.assertEqual(colide_algum_ps(Personagem(310, 80, 0, 0, 4), L_PERSONAGEM_INICIAL), True)
        self.assertEqual(colide_algum_ps(Personagem(310, 200, 0, 0, 4), L_PERSONAGEM_INICIAL), False)

    def test_check_win(self):
        self.assertEqual(check_win(Personagem(200, 400, 0, 0, 4), Personagem(210, 410, 0, 0, 1)), False)
        self.assertEqual(check_win(Personagem(200, 400, 0, 0, 4), Personagem(210, 410, 0, 0, 3)), True)

    def test_ganhou(self):
        self.assertEqual(ganhou(Personagem(310, 200, 0, 0, 4), L_PERSONAGEM_INICIAL), True)
        self.assertEqual(ganhou(Personagem(310, 80, 0, 0, 4), L_PERSONAGEM_INICIAL), False)

    def test_mover_jogo(self):
        self.assertEqual(mover_jogo(Jogo(FOGUETE_INICIAL, L_PERSONAGEM_INICIAL, False, True)),
                         Jogo(FOGUETE_INICIAL, L_PERSONAGEM_INICIAL, False, True))

        self.assertEqual(mover_jogo(Jogo(FOGUETE_INICIAL, L_PERSONAGEM_INICIAL, True, False)),
                         Jogo(FOGUETE_INICIAL, L_PERSONAGEM_INICIAL, True, False))

        self.assertEqual(mover_jogo(Jogo(Personagem(310, 80, 0, 0, 4), L_PERSONAGEM_INICIAL, False, False)),
                         Jogo(move_foguete(Personagem(310, 80, 0, 0, 4)), mover_personagens(L_PERSONAGEM_INICIAL), True, False))

        self.assertEqual(mover_jogo(Jogo(Personagem(310, 200, 0, 0, 4), L_PERSONAGEM_INICIAL, False, False)),
                         Jogo(move_foguete(Personagem(310, 200, 0, 0, 4)), mover_personagens(L_PERSONAGEM_INICIAL), False, True))

        self.assertEqual(mover_jogo(Jogo(Personagem(100, LIMITE_CIMA, 0, 0, 4), L_PERSONAGEM_INICIAL, False, False)),
                         Jogo(move_foguete(Personagem(100, LIMITE_CIMA, 0, 0, 4)),
                              mover_personagens(L_PERSONAGEM_INICIAL), False, False))

    # def test_trata_tecla_jogo(self):
    #     self.assertEqual(trata_tecla_jogo(JOGO_MEIO, pg.K_RETURN), cria_jogo_inicial())
    #     self.assertEqual(trata_tecla_jogo(JOGO_MEIO, TECLA_DIREITA), Jogo(trata_tecla(JOGO_MEIO.foguete, TECLA_DIREITA),
    #                                                                       JOGO_MEIO.personagens, JOGO_MEIO.game_over, JOGO_MEIO.win))

    #  teste cria novo jogo