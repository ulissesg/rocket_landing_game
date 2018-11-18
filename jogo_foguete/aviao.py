#!/usr/bin/env python
# -*- coding: utf-8 -*-

from personagem import *

''' Programa do aviao '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = criar_tela_base(LARGURA, ALTURA)

FREQUENCIA_AVIAO = 30

IMG_AVIAO = carregar_imagem("aviao.png")
IMG_AVIAO = definir_dimensoes(IMG_AVIAO, 100, 80)
IMG_AVIAO_DIREITA = espelhar(IMG_AVIAO)
IMG_AVIAO_ESQUERDA = IMG_AVIAO

LIMITE_CIMA = altura_imagem(IMG_AVIAO) // 2
LIMITE_BAIXO = ALTURA - altura_imagem(IMG_AVIAO) // 2
LIMITE_DIREITA =LARGURA - largura_imagem(IMG_AVIAO) // 2
LIMITE_ESQUERDA =largura_imagem(IMG_AVIAO) // 2


'''==================='''
'''# Definições de dados: '''


''' Aviao eh um Personagem
interp. representa um aviao com suas posicoes e velocidades.
'''
#EXEMPLOS:
AVIAO_INICIAL = Personagem(0, 200, 1, -1)
AVIAO_INICIAL2 = Personagem(600, 50, -1, -1)
AVIAO_MEIO = Personagem(300, 200, 1, 1)
AVIAO_FINAL = Personagem(300, 400, 1, 1)

#TEMPLATE
'''
def fn_para_aviao(av):
    ... av.x
        av.y
        av.dx
        av.dy
'''

'''
ListaAviao é um desses:
    - VAZIA
    - juntar(Aviao, ListaAviao)
'''
#Exemplos:
L_AVIAO_1 = criar_lista(AVIAO_INICIAL)
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
mover_avioes: ListaAviao -> ListaAviao
Produz o próximo estado dos avioes
'''

def mover_avioes(avioes):
    pass


'''
mover_aviao: Aviao -> Aviao
interp. produz o proximo estado de um aviao
'''

def mover_aviao(a):
    pass

'''
desenha: EstadoMundo -> Imagem
Desenha...
# !!! TODO
def desenha(estado):
    pass
'''

