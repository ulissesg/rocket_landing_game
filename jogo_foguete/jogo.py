#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
from asteroides import *
from personagens import *
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


IMG_METEORO = ...#ainda nao definido
LARGURA_METEORO= largura_imagem(IMG_METEORO)
ALTURA_METEORO= altura_imagem(IMG_METEORO)

IMG_AVIAO= ...#ainda nao definido
LARGURA_AVIAO= largura_imagem(IMG_AVIAO)
ALTURA_AVIAO= altura_imagem(IMG_AVIAO)

IMG_PLATAFORMA= ...#ainda nao definido
LARGURA_PLATAFORMA= largura_imagem(IMG_PLATAFORMA)
ALTURA_PLATAFORMA= altura_imagem(IMG_PLATAFORMA)

'''==================='''
'''# Definições de dados: '''

Jogo = definir_estrutura("Jogo", "foguete, asteroide, aviao, plataforma, game_over")
''' Jogo pode ser formado como: Jogo(Foguete, ListaAsteroide, ListaAviao, ListaPlataforma, Boolean)
interp. representa o jogo sendo ele conposto por um foguete, dois asteroides, dois avioes, duas plataformas, e um game over.
'''
#EXEMPLOS:
JOGO_INICIAL= Jogo(FOGUETE_INICIAL, criar_lista(ASTEROIDE_INICIAL), criar_lista(AVIAO_INICIAL), criar_lista(PLATAFORMA1), False);

JOGO_MEIO= Jogo(FOGUETE_INICIAL, criar_lista(ASTEROIDE_MEIO), criar_lista(AVIAO_MEIO), criar_lista(PLATAFORMA2), False);

JOGO_GAME_OVER = Jogo(FOGUETE_INICIAL, criar_lista(ASTEROIDE_FINAL), criar_lista(AVIAO_FINAL), criar_lista(PLATAFORMA2), True);


##TEMPLATE
'''
def fn_para_jogo(jogo):
    if jogo.game_over == False:
        ...jogo.foguete
           jogo.asteroide
           ...
    ...jogo.foguete
       jogo.asteroide
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
    big_bang(m, tela=tela, frequencia= FREQUENCIA,
             # quando_tick=tock,
             # desenhar=desenha,
             quando_tecla=...,
             quando_solta_tecla=...
             )


