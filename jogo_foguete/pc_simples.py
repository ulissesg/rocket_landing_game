from htdp_pt_br.universe import *
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Programa do plano cartesiano '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

#(LARGURA, ALTURA) = (600, 400)
#tela = criar_tela_base(LARGURA, ALTURA) #descomente isso


'''==================='''
'''# Definições de dados: '''

Pc_simples = definir_estrutura("Pc_simples", "x, y, dx, dy")
''' Foguete pode ser formado assim: Foguete(int[LIMITE_ESQUERDA, LIMITE_DIREITA], int[LIMITE_CIMA, LIMITE_BAIXO], int, int)
interp. representa um plano cartesiano com as posicoes x, y e as velocidades dos mesmos dx, dy.
'''
#EXEMPLOS:
PC_INICIAL = Pc_simples(0, 0, 1, 1)
PC_MEIO = Pc_simples(300, 200, 1, 1)
PC_FIM = Pc_simples(600, 400, 1, 1)
PC_DIREITO = Pc_simples(600, 200, 1, 1)
PC_ESQUERDO = Pc_simples(0, 200, 1, 1)

#TEMPLATE
'''
def fn_para_pc(pc):
    ... pc.x
        pc.y
        pc.dx
        pc.dy
       
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




