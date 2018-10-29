from pc_simples import *

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Programda do foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

#(LARGURA, ALTURA) = (600, 400)
#tela = criar_tela_base(LARGURA, ALTURA) #descomente isso


'''==================='''
'''# Definições de dados: '''


''' Foguete eh um Pc_simples
interp. representa um foguete com suas posicoes e velocidades.
'''
#EXEMPLOS:
FOGUETE_INICIAL = Pc_simples(300, 0, 0, 2)
FOGUETE_MEIO = Pc_simples(300, 200, 0, 2)
FOGUETE_FINAL = Pc_simples(300, 400, 0, 2)

#TEMPLATE
'''
def fn_para_foguete(f):
    ... f.x
        f.y
        f.dx
        f.dy
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
# def main(m):
#     big_bang(m, tela=tela, frequencia=XX, \
#              quando_tick=tock, \
#              desenhar=desenha, \
#              quando_tecla=..., \
#              quando_mouse=..., \
#              parar_quando=...)




