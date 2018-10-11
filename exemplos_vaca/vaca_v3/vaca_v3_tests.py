import unittest
from vaca_v3 import *


class Test(unittest.TestCase):


    def test_mover_vaca(self):
        ## CASOS NORMAIS (ANDANDO PARA FRENTE)
        self.assertEqual(mover_vaca(Vaca(LIMITE_ESQUERDO, 3)), Vaca(LIMITE_ESQUERDO + 3, 3))
        self.assertEqual(mover_vaca(Vaca(LIMITE_ESQUERDO + 3, 3)), Vaca(LIMITE_ESQUERDO + 6, 3))

        ## CASO EM QUE TOCA NO LIMITE DIREITO
        self.assertEqual(mover_vaca(Vaca(LIMITE_DIREITO, 3)), Vaca(LIMITE_DIREITO, -3))
        self.assertEqual(mover_vaca(Vaca(LIMITE_DIREITO - 2, 3)), Vaca(LIMITE_DIREITO - 2, -3))
        self.assertEqual(mover_vaca(Vaca(LIMITE_DIREITO - 1, 3)), Vaca(LIMITE_DIREITO - 1, -3))

        ## CASO ANDANDO PARA TRÁS
        self.assertEqual(mover_vaca(Vaca(LIMITE_DIREITO, -3)), Vaca(LIMITE_DIREITO - 3, -3))
        self.assertEqual(mover_vaca(Vaca(LARGURA//2, -3)), Vaca(LARGURA//2 - 3, -3))

        ## CASO EM QUE TOCA NO LIMITE ESQUERDO
        self.assertEqual(mover_vaca(Vaca(LIMITE_ESQUERDO, -3)), Vaca(LIMITE_ESQUERDO, 3))
        self.assertEqual(mover_vaca(Vaca(LIMITE_ESQUERDO + 1, -3)), Vaca(LIMITE_ESQUERDO + 1, 3))
        self.assertEqual(mover_vaca(Vaca(LIMITE_ESQUERDO + 2, -3)), Vaca(LIMITE_ESQUERDO + 2, 3))

    def test_trata_tecla_vaca(self):
        self.assertEqual(trata_tecla_vaca(Vaca(LARGURA//2, 3), TC_VIRAR), Vaca(LARGURA//2, -3))
        self.assertEqual(trata_tecla_vaca(Vaca(LARGURA // 2, -3), TC_VIRAR), Vaca(LARGURA // 2, 3))
        self.assertEqual(trata_tecla_vaca(Vaca(LARGURA // 2, 3), pg.K_0), Vaca(LARGURA // 2, 3))

    def test_trata_tecla_jogo(self):
        self.assertEqual( trata_tecla_jogo(JOGO_GAME_OVER, pg.K_RETURN),
                          JOGO_INICIAL )
        self.assertEqual(trata_tecla_jogo(JOGO_GAME_OVER, pg.K_SPACE),
                         JOGO_GAME_OVER)

    def test_mover_tudo(self):

        ## CASO NORMAL
        self.assertEqual(mover_tudo(Jogo(Vaca(LIMITE_ESQUERDO, 3), Churrasqueiro(LARGURA//2, LIMITE_CIMA, 6), False)),
                         Jogo(Vaca(LIMITE_ESQUERDO + 3, 3), Churrasqueiro(LARGURA // 2, LIMITE_CIMA + 6, 6), False))

        ## CASO COLISAO

        self.assertEqual(mover_tudo(
                            Jogo(
                                Vaca(LARGURA//2, -3),
                                Churrasqueiro(LARGURA//2, ALTURA // 2, -3),
                                False)  ),
                            Jogo(
                                Vaca(LARGURA // 2, -3),
                                Churrasqueiro(LARGURA // 2, ALTURA // 2, -3),
                                True) )

        self.assertEqual(mover_tudo(
            Jogo(
                Vaca(LARGURA // 2 - largura_imagem(IMG_VACA_INO) // 2
                                  - largura_imagem(IMG_CHURRASQUEIRO) // 2 + 2,
                     -3),
                Churrasqueiro(
                    LARGURA // 2,
                    ALTURA // 2,
                    -3),
                False)),
            Jogo(
                Vaca(LARGURA // 2 - largura_imagem(IMG_VACA_INO) // 2
                     - largura_imagem(IMG_CHURRASQUEIRO) // 2 + 2,
                     -3),
                Churrasqueiro(
                    LARGURA // 2,
                    ALTURA // 2,
                    -3),
                True))

    def test_colidirem(self):

        self.assertEqual( colidirem( Vaca(LIMITE_ESQUERDO, 3),
                                     Churrasqueiro(LARGURA//2, LIMITE_CIMA, 6)),
                          False)
        self.assertEqual( colidirem( Vaca(LARGURA // 2 - largura_imagem(IMG_VACA_INO) // 2
                                                       - largura_imagem(IMG_CHURRASQUEIRO) // 2 + 2,
                                         -3),
                                     Churrasqueiro(
                                         LARGURA // 2,
                                         ALTURA // 2,
                                         -3)),
                         True)

    def test_mover_churras(self):
        ## CASOS NORMAIS (ANDANDO)
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_CIMA, 3)), Churrasqueiro(LARGURA//2, LIMITE_CIMA + 3, 3))
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_CIMA + 3, 3)), Churrasqueiro(LARGURA//2, LIMITE_CIMA + 6, 3))

        ## CASO EM QUE TOCA NO LIMITE BAIXO
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_BAIXO, 3)), Churrasqueiro(LARGURA//2, LIMITE_BAIXO, -3))
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_BAIXO - 2, 3)), Churrasqueiro(LARGURA//2, LIMITE_BAIXO - 2, -3))
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_BAIXO - 1, 3)), Churrasqueiro(LARGURA//2, LIMITE_BAIXO - 1, -3))

        ## CASO ANDANDO PARA TRÁS
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_BAIXO, -3)), Churrasqueiro(LARGURA//2, LIMITE_BAIXO - 3, -3))
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, ALTURA // 2, -3)), Churrasqueiro(LARGURA//2, ALTURA // 2 - 3, -3))

        ## CASO EM QUE TOCA NO LIMITE CIMA
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_CIMA, -3)), Churrasqueiro(LARGURA//2, LIMITE_CIMA, 3))
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_CIMA + 1, -3)), Churrasqueiro(LARGURA//2, LIMITE_CIMA + 1, 3))
        self.assertEqual(mover_churras(Churrasqueiro(LARGURA//2, LIMITE_CIMA + 2, -3)), Churrasqueiro(LARGURA//2, LIMITE_CIMA + 2, 3))




# unittest.main()  #não excluir (a menos que esteja rodando como unit test no PyCharm)
