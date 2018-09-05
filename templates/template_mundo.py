#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Meu programa mundo  (torne isto mais específico) '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

#(LARGURA, ALTURA) = (600, 400)
#tela = criar_tela_base(LARGURA, ALTURA) #descomente isso

##Criar/carregar imagens:
#IMG_GATO = carregar_imagem('cat1.png')

'''==================='''
'''# Definições de dados: '''

''' EstadoMundo é ... (dê um nome melhor para EstadoMundo) '''



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
    if ev == pg.MOUSEBUTTONDOWN:
        ... estado
    elif ev == pg.MOUSEBUTTONUP:
        ... estado
    elif ev == pg.MOUSEMOTION:
        ... estado
    else:
        ... estado

'''

''' ================= '''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com ... 
def main(inic):
    big_bang(inic, tela=tela, frequencia=XX, \
             quando_tick=tock, \
             desenhar=desenha, \
             quando_tecla=..., \
             quando_mouse=..., \
             parar_quando=...)           
             

'''