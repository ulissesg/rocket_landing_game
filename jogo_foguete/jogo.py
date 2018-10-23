#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
from asteroides import *
from aviao import *
from foguete import *
from plataforma import *

''' Jogo de pousar foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = criar_tela_base(LARGURA, ALTURA)

FREQUENCIA= 30

X_BOOST=500
Y_BOOST=50
COR_BOOST= "black"
TAMANHO_BOOST= 40
FONTE_BOOST= "monospace"

X_PLATAFORMA1=100
Y_PLATAFORMA1=500

X_PLATAFORMA2=300
Y_PLATAFORMA2=500


IMG_METEORO =
LARGURA_METEORO= largura_imagem(IMG_METEORO)
ALTURA_METEORO= altura_imagem(IMG_METEORO)

IMG_AVIAO=
LARGURA_AVIAO= largura_imagem(IMG_AVIAO)
ALTURA_AVIAO= altura_imagem(IMG_AVIAO)

IMG_PLATAFORMA=
LARGURA_PLATAFORMA= largura_imagem(IMG_PLATAFORMA)
ALTURA_PLATAFORMA= altura_imagem(IMG_PLATAFORMA)

'''==================='''
'''# Definições de dados: '''

Jogo = definir_estrutura("Jogo", "foguete, ast_1, ast_2, aviao_1, aviao_2, plat_1, plat_2, game_over")
''' Jogo pode ser formado como: Jogo(Foguete, Asteroide, Asteroide, Aviao, Aviao, Plataforma, PLataforma, Boolean)
interp. representa o jogo sendo ele conposto por um foguete, dois asteroides, dois avioes, duas plataformas, e um game over.
'''
#EXEMPLOS:
JOGO_INICIAL= Jogo(FOGUETE_INICIAL, ASTEROIDE_INICIAL, ASTEROIDE_INICIAL2, AVIAO_INICIAL, AVIAO_INICIAL2,
                   PLATAFORMA1, PLATAFORMA2, False);

JOGO_MEIO= Jogo(FOGUETE_MEIO, ASTEROIDE_MEIO, ASTEROIDE_MEIO, AVIAO_MEIO, AVIAO_MEIO,
                PLATAFORMA1, PLATAFORMA2, False);

JOGO_GAME_OVER= Jogo(FOGUETE_MEIO, ASTEROIDE_MEIO, ASTEROIDE_MEIO, AVIAO_MEIO, AVIAO_MEIO,
                PLATAFORMA1, PLATAFORMA2, True);


##TEMPLATE
'''
def fn_para_jogo(jogo):
    if jogo.game_over == False:
        ...jogo.foguete
           jogo.ast_1
           ...
    ...jogo.foguete
       jogo.ast_1
       ...
'''


'''===================='''
''' Funções: '''


'''
tock: EstadoMundo -> EstadoMundo
Produz o próximo ...
# !!! TODO
def tock(estado):
    pass
'''


'''
desenha: EstadoMundo -> Imagem
Desenha...
# !!! TODO
def desenha(estado):
    pass
'''


'''
trata_tecla: EstadoMundo, Tecla -> EstadoMundo
Quando teclar ... produz ... <apagar caso não precise usar>
# !!! TODO
Template:

def trata_tecla(estado, tecla):
    if tecla == pg.K_SPACE:
        ... estado
    else:
        ... estado
'''


'''
trata_mouse: EstadoMundo, Int, Int, EventoMouse -> EstadoMundo:
Quando fazer ... nas posições x y no mouse produz ...   <apagar caso não precise usar>
# !!! TODO
Template:

def trata_mouse(estado, x, y, ev):

    if ev == pg.MOUSEMOTION:
        ... estado
    else:
        ... estado

'''

''' ================= '''
''' Main (Big Bang):'''


''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com ...'''
def main(m):
    big_bang(m, tela=tela, frequencia=XX, \
             quando_tick=tock, \
             desenhar=desenha, \
             quando_tecla=..., \
             quando_mouse=..., \
             parar_quando=...)


