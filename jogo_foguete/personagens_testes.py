from personagens import *
import unittest

# FUNCAO PARA TESTAR A FUNCAO cria_lista_perosnagem

nova_lista = cria_lista_personagem()

def testa_jogo_inicial(nova_lista):
    if nova_lista[0].x >= LIMITE_ESQUERDA + LIMITE_SEGURANCA and \
            nova_lista[0].x < LIMITE_DIREITA - LIMITE_SEGURANCA and \
            nova_lista[0].y >= LIMITE_ASTEROIDE - LIMITE_SEGURANCA and \
            nova_lista[0].y < LIMITE_ASTEROIDE and nova_lista[0].dx >= 1 and \
            nova_lista[0].dx < 20 and nova_lista[0].dy >= 1 and nova_lista[0].dy < 20 and \
            nova_lista[4].x >= LIMITE_ESQUERDA and nova_lista[4].x < LIMITE_DIREITA:
        return True

    return False

#  TESTES DAS FUNCOES
class Test(unittest.TestCase):

    def test_mover_personagens(self):
        self.assertEqual(mover_personagens(L_PERSONAGEM_INICIAL),
                         criar_lista(Personagem(599, 79, -1, -1, AVIAO), Personagem(301, 201, 1, 1, PLATAFORMA),
                                     Personagem(301, 71, 1, 1, ASTEROIDE)))

        self.assertEqual(mover_personagens(L_PERSONAGEM_MEIO),
                         criar_lista(mover_personagem(L_PERSONAGEM_MEIO[0]), mover_personagem(L_PERSONAGEM_MEIO[1]),
                                     mover_personagem(L_PERSONAGEM_MEIO[2]), mover_personagem(L_PERSONAGEM_MEIO[3]),
                                     mover_personagem(L_PERSONAGEM_MEIO[4]), mover_personagem(L_PERSONAGEM_MEIO[5])))

    def test_mover_personagem(self):

        #TESTES PADRAO
        self.assertEqual(mover_personagem(PS_INICIAL),
                         Personagem(PS_INICIAL.x + PS_INICIAL.dx, PS_INICIAL.y + PS_INICIAL.dy,
                                    PS_INICIAL.dx, PS_INICIAL.dy, AVIAO))

        self.assertEqual(mover_personagem(PS_MEIO),
                         Personagem(PS_MEIO.x + PS_MEIO.dx, PS_MEIO.y + PS_MEIO.dy,
                                    PS_MEIO.dx, PS_MEIO.dy, ASTEROIDE))

        #TESTES PARA ASTEROIDE
        self.assertEqual(mover_personagem(Personagem(LIMITE_DIREITA , LIMITE_CIMA + 50, 2, 2, ASTEROIDE)),
                         Personagem(LIMITE_DIREITA - 2, LIMITE_CIMA + 50, -2, 2, ASTEROIDE))

        self.assertEqual(mover_personagem(Personagem(LIMITE_ESQUERDA , LIMITE_CIMA + 50, 2, 2, ASTEROIDE)),
                         Personagem(LIMITE_ESQUERDA - 2, LIMITE_CIMA + 50, -2, 2, ASTEROIDE))

        self.assertEqual(mover_personagem(Personagem(LIMITE_DIREITA - 50 , LIMITE_CIMA, 2, 2, ASTEROIDE)),
                         Personagem(LIMITE_DIREITA - 50, LIMITE_CIMA - 2, 2, -2, ASTEROIDE))

        self.assertEqual(mover_personagem(Personagem(LIMITE_DIREITA - 50 , LIMITE_ASTEROIDE, 2, 2, ASTEROIDE)),
                         Personagem(LIMITE_DIREITA - 50, LIMITE_ASTEROIDE - 2, 2, -2, ASTEROIDE))

        #TESTES PARA AVIAO

        self.assertEqual(mover_personagem(Personagem(LIMITE_DIREITA , LIMITE_CIMA + 50, 2, 2, AVIAO)),
                         Personagem(LIMITE_DIREITA - 2, LIMITE_CIMA + 50, -2, 2, AVIAO))

        self.assertEqual(mover_personagem(Personagem(LIMITE_ESQUERDA , LIMITE_CIMA + 50, 2, 2, AVIAO)),
                         Personagem(LIMITE_ESQUERDA - 2, LIMITE_CIMA + 50, -2, 2, AVIAO))

        self.assertEqual(mover_personagem(Personagem(LIMITE_DIREITA - 50 , LIMITE_CIMA, 2, 2, AVIAO)),
                         Personagem(LIMITE_DIREITA - 50, LIMITE_CIMA - 2, 2, -2, AVIAO))

        self.assertEqual(mover_personagem(Personagem(LIMITE_DIREITA - 50 , LIMITE_AVIAO, 2, 2, AVIAO)),
                         Personagem(LIMITE_DIREITA - 50, LIMITE_AVIAO - 2, 2, -2, AVIAO))


    def test_testa_jogo_inicial(self):

        self.assertEqual(testa_jogo_inicial(nova_lista), True)

