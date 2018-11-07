from pc_simples import *

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Programda do foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (1200, 800)
tela = criar_tela_base(LARGURA, ALTURA)


FREQUENCIA_FOGUETE = 30
IMG_FOGUETE = carregar_imagem("foguete.png")
IMG_FOGUETE = definir_dimensoes(IMG_FOGUETE, 100, 80)

LIMITE_BAIXO = ALTURA - altura_imagem(IMG_FOGUETE) * 1.25
LIMITE_DIREITA = LARGURA - largura_imagem(IMG_FOGUETE) // 2
LIMITE_ESQUERDA = 0 + largura_imagem(IMG_FOGUETE) // 2
LIMITE_CIMA = 0 + altura_imagem(IMG_FOGUETE)

DX = 1
DY = 1
DDX = 50
DDY = 50

TECLA_DIREITA = pg.K_RIGHT
TECLA_ESQUERDA = pg.K_LEFT
TECLA_CIMA = pg.K_UP

'''==================='''
'''# Definições de dados: '''


''' Foguete eh um Pc_simples
interp. representa um foguete com suas posicoes e velocidades.
'''
#EXEMPLOS:
FOGUETE_INICIAL = Pc_simples(LIMITE_DIREITA//2, LIMITE_CIMA, DX, DY)
FOGUETE_MEIO = Pc_simples(LIMITE_DIREITA //2 , LIMITE_BAIXO //2, DX, DY)
FOGUETE_FINAL = Pc_simples(LIMITE_DIREITA//2, LIMITE_BAIXO, DX, DY)

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
move_foguete: Foguete -> Foguete
Produz o próximo estado do foguete
'''
def move_foguete(f):
    if f.y < LIMITE_BAIXO: # fazer variavel
        return Pc_simples(f.x, f.y + f.dy, f.dx, f.dy)
    return f


'''
desenha: Foguete -> Imagem
Desenha o foguete na tela
'''
def desenha(f):
    colocar_imagem(IMG_FOGUETE,tela, f.x, f.y)


'''
trata_tecla: Foguete, Tecla -> Foguete
Quando teclar pra cima o foguete sobe, pra direita move o foguete para a direita e para a esquerda move o foguete para esquerda.
'''

def trata_tecla(f, tecla):
    if f.y < LIMITE_BAIXO:

        if tecla == TECLA_CIMA:
                return Pc_simples(f.x, f.y - DDY, f.dx, f.dy)

        elif tecla == TECLA_DIREITA:
            if f.x <= LIMITE_DIREITA:
                return Pc_simples(f.x + DDX, f.y, f.dx, f.dy)
            return f

        elif tecla == TECLA_ESQUERDA:
            if f.x >= LIMITE_ESQUERDA:
                return Pc_simples(f.x - DDX, f.y, f.dx, f.dy)
            return f

        return f

    return f



