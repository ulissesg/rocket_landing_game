#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *


'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = criar_tela_base(LARGURA, ALTURA)


IMG_GATO = carregar_imagem('cat1.png')
Y = ALTURA//2


''' ##### Inicio das definições de dados ##### '''

'''
Gato é um Int positivo (>=0)
interp. coordenada x do gato na tela
Exemplos:
'''
GATO_INICIAL = 0
GATO_MEIO= LARGURA//2
GATO_FIM = LARGURA
'''Template para funcoes que recebem Gato:
def fn_para_gato(g):
    ... g    #faz algo com o g
'''

''' ##### Fim das definições de dados ##### '''


'''#### Inicio das funçeõs: #####'''

'''mover: Gato -> Gato'''
def mover(gato):
    return gato + 3


'''desenha: Gato -> Imagem'''
def desenha(gato):
    colocar_imagem(IMG_GATO, tela, gato, Y)


'''trata-tecla: Gato EventoTecla -> Gato'''
def trata_tecla(gato, tecla):
    if tecla == pg.K_SPACE:
        return 0
    else:
        return gato


def trata_mouse(gato, x, y, ev):
    if ev == pg.MOUSEBUTTONDOWN:
        return x
    else:
        return gato

'''parar: Gato -> Boolean'''
def parar(gato):
    if gato >= LARGURA//2:
        return True
    else:
        return False



def main(gato):
    big_bang(0, \
             tela=tela, \
             a_cada_tick=mover, \
             desenhar=desenha, \
             quando_tecla=trata_tecla, \
             quando_mouse=trata_mouse
             # parar_quando=parar
             )


main(0)  #deixar comentado. excluir só quando chamar

