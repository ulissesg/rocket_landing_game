from htdp_pt_br.universe import *
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Programa do personagem '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

#(LARGURA, ALTURA) = (600, 400)
#tela = criar_tela_base(LARGURA, ALTURA) #descomente isso


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
def fn_para_ps(ps):
    ... ps.x
        ps.y
        ps.dx
        ps.dy
       
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




