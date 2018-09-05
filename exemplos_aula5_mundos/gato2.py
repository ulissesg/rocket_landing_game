#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *


''' Meu programa do gatinho '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

LARGURA, ALTURA = 600, 400
tela = criar_tela_base(LARGURA, ALTURA) #descomente isso

Y = ALTURA // 2

##Criar/carregar imagens:
IMG_GATO = carregar_imagem('cat1.png')

FREQUENCIA = 60

DX = 3


'''==================='''
'''# Definições de dados: '''

''' Gato é um Int (>0)
interp. a posição x do gato na tela
'''
#exemplos
GATO_INICIAL = 0
GATO_MEIO = LARGURA // 2
GATO_FINAL = LARGURA

'''
#template
def fn_para_gato(x):
    ... x
'''



'''===================='''
''' Funções: '''

'''
mover: Gato -> Gato
Faz o gato se mover para direita'''
def mover(x):
     return x + DX


'''
desenha: Gato -> Imagem
Desenha o gato na tela'''
def desenha(x):
    colocar_imagem(IMG_GATO, tela, x, Y)
    return tela


'''
trata_tecla: Gato, Tecla -> Gato
Quando teclar espaço produz o gato inicial
# !!! TODO'''

def trata_tecla(x, tecla):
    if tecla == pg.K_SPACE:
        return GATO_INICIAL
    else:
        return x




'''
final-da_tela: Gato -> Boolean
Para a animação se chegar no final da tela
'''
def final_da_tela(x):
    # if x >= LARGURA:
    #     return True
    # return False
    return x >= LARGURA