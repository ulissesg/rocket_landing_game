#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Programa do personagens '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = criar_tela_base(LARGURA, ALTURA)

FREQUENCIA_PERSONAGENS = 30

 # IMAGEM AVIAO
IMG_AVIAO = carregar_imagem("imagens/aviao.png")
IMG_AVIAO = definir_dimensoes(IMG_AVIAO, 100, 100)
IMG_AVIAO_DIREITA = espelhar(IMG_AVIAO)
IMG_AVIAO_ESQUERDA = IMG_AVIAO

#IMAGEM ASTEROIDE
IMG_ASTEROIDE = carregar_imagem("imagens/asteroide.png")
IMG_ASTEROIDE = definir_dimensoes(IMG_ASTEROIDE, 100, 100)

#IMAGEM PLATAFORMA
IMG_PLATAFORMA = carregar_imagem("imagens/plataforma.png")
IMG_PLATAFORMA = definir_dimensoes(IMG_PLATAFORMA, 100,30)

LIMITE_CIMA = altura_imagem(IMG_AVIAO) // 2  #rever
LIMITE_BAIXO = ALTURA - altura_imagem(IMG_AVIAO) // 2
LIMITE_DIREITA =LARGURA - largura_imagem(IMG_AVIAO) // 2
LIMITE_ESQUERDA =largura_imagem(IMG_AVIAO) // 2


'''==================='''
'''# Definições de dados: '''

Personagem = definir_estrutura("Personagem", "x, y, dx, dy")
''' Personagem pode ser formado assim: Personagem(int[LIMITE_ESQUERDA, LIMITE_DIREITA], int[LIMITE_CIMA, LIMITE_BAIXO], int, int)
interp. representa um personagem com as posicoes x, y e as velocidades dos mesmos dx, dy.
'''
#EXEMPLOS:
PS_INICIAL = Personagem(0, 0, 1, 1)
PS_MEIO = Personagem(300, 200, 1, 1)
PS_FIM = Personagem(600, 400, 1, 1)
PS_DIREITO = Personagem(600, 200, 1, 1)
PS_ESQUERDO = Personagem(0, 200, 1, 1)

#TEMPLATE
'''
def fn_para_aviao(av):
    ... av.x
        av.y
        av.dx
        av.dy
'''

'''
ListaPersonagem é um desses:
    - VAZIA
    - juntar(Personagem, ListaPersonagem)
'''
#Exemplos:
L_AVIAO_1 = criar_lista(PS_INICIAL)
L_AVIAO_INICIAL = criar_lista(
    Personagem(600, 50, -1, -1),
    Personagem(300, 200, 1, 1),
    Personagem(300, 400, 1, 1)
)

'''
#template
def fn_para_lista(lista):
    if lista.vazia:
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''

'''===================='''
''' Funções: '''


'''
mover_avioes: ListaPersonagem -> ListaPersonagem
Produz o próximo estado dos personagens
'''

def mover_personagens(ps):
    pass


'''
mover_aviao: Personagem -> Personagem
interp. produz o proximo estado de um personagem
'''

def mover_personagem(ps):
    pass

'''
desenha: ListaPersonagem -> Imagem
Desenha os personagens na tela
'''
def desenha(ps):
    pass
