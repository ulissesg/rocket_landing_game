#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *
import random

''' Programa do personagens '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (1200, 700)
tela = criar_tela_base(LARGURA, ALTURA)

FREQUENCIA_PERSONAGENS = 30

 #AVIAO
IMG_AVIAO = carregar_imagem("imagens/aviao.png")
IMG_AVIAO = definir_dimensoes(IMG_AVIAO, 100, 70)
IMG_AVIAO_DIREITA = espelhar(IMG_AVIAO)
IMG_AVIAO_ESQUERDA = IMG_AVIAO

AVIAO = 2

LIMITE_AVIAO = ALTURA // 4 *3.2 - altura_imagem(IMG_AVIAO) // 2

DX_AVIAO = 5
DY_AVIAO = 0.7

#ASTEROIDE
IMG_ASTEROIDE = carregar_imagem("imagens/asteroide.png")
IMG_ASTEROIDE = definir_dimensoes(IMG_ASTEROIDE, 80, 80)

ASTEROIDE = 1

LIMITE_ASTEROIDE = ALTURA // 2.5 - altura_imagem(IMG_ASTEROIDE) // 2

DX_ASTEROIDE = 10
DY_ASTEROIDE = 0.5

#PLATAFORMA
IMG_PLATAFORMA = carregar_imagem("imagens/plataforma.png")
IMG_PLATAFORMA = definir_dimensoes(IMG_PLATAFORMA, 100,60)

PLATAFORMA  = 3

DX_PLATAFORMA = 0
DY_PLATAFORMA = 0


LIMITE_CIMA = altura_imagem(IMG_AVIAO) // 2 + 1
LIMITE_BAIXO = ALTURA - altura_imagem(IMG_PLATAFORMA) // 2 -1
LIMITE_DIREITA =LARGURA - largura_imagem(IMG_AVIAO) // 2 - 1
LIMITE_ESQUERDA =largura_imagem(IMG_AVIAO) // 2 + 1

LIMITE_SEGURANCA = 60

'''==================='''
'''# Definições de dados: '''

Personagem = definir_estrutura("Personagem", "x, y, dx, dy, tipo")
''' Personagem pode ser formado assim: Personagem(Int[LIMITE_ESQUERDA, LIMITE_DIREITA], Int[LIMITE_CIMA, LIMITE_BAIXO], Int, Int, Int)
interp. representa um personagem com as posicoes x, y e as velocidades dos mesmos dx, dy.
'''
#EXEMPLOS:
PS_INICIAL = Personagem(60, 60, 1, 1, AVIAO)
PS_MEIO = Personagem(300, 200, 1, 1, ASTEROIDE)
PS_FIM = Personagem(600, 400, 1, 1, PLATAFORMA)
PS_DIREITO = Personagem(600, 200, 1, 1, ASTEROIDE)
PS_ESQUERDO = Personagem(0, 200, 1, 1, AVIAO)

PERSONAGEM_1 = Personagem(500, 240, 15, 3, ASTEROIDE)
PERSONAGEM_2 = Personagem(230, 230, 10, 2, ASTEROIDE)
PERSONAGEM_3 = Personagem(600, 300, 5, 1, AVIAO)
PERSONAGEM_4 = Personagem(800, 350, 19, 3, AVIAO)
PERSONAGEM_5 = Personagem(600, LIMITE_BAIXO , DX_PLATAFORMA, DY_PLATAFORMA, PLATAFORMA)
PERSONAGEM_6 = Personagem(900, LIMITE_BAIXO , DX_PLATAFORMA, DY_PLATAFORMA, PLATAFORMA)


#TEMPLATE
'''
def fn_para_personagem(ps):
    if ps.x >= LIMITE_DIREITA or ps.x <= LIMITE_ESQUERDA:
        ps.x
        ps.y
        ps.dx
        ps.dy
        ps.tipo
        
    if ps.y >= LIMITE_CIMA or ps.y >= LIMITE_BAIXO:
        ps.x
        ps.y
        ps.dx
        ps.dy
        ps.tipo
    
    ps.x
        ps.y
        ps.dx
        ps.dy
        ps.tipo
'''

'''
ListaPersonagem é um desses:
    - VAZIA
    - juntar(Personagem, ListaPersonagem)
'''
#Exemplos:
L_PERSONAGENS_1 = criar_lista(PS_INICIAL)
L_PERSONAGEM_INICIAL = criar_lista(
    Personagem(600, 80, -1, -1, AVIAO),
    Personagem(300, 200, 1, 1, PLATAFORMA),
    Personagem(300, 70, 1, 1, ASTEROIDE)
)
L_PERSONAGEM_MEIO = criar_lista(
    PERSONAGEM_1, PERSONAGEM_2, PERSONAGEM_3, PERSONAGEM_4, PERSONAGEM_5, PERSONAGEM_6
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
cria_lista_personagem: -> ListaPersonagem
cria uma lista de personagens aleatoriamente
'''

def cria_lista_personagem():
    PERSONAGEM_1 = Personagem(random.randrange(LIMITE_ESQUERDA + LIMITE_SEGURANCA, LIMITE_DIREITA - LIMITE_SEGURANCA),
                              random.randrange(LIMITE_ASTEROIDE - LIMITE_SEGURANCA, LIMITE_ASTEROIDE),
                              random.randrange(1,20), random.randrange(1, 4), ASTEROIDE)

    PERSONAGEM_2 = Personagem(random.randrange(LIMITE_ESQUERDA + LIMITE_SEGURANCA, LIMITE_DIREITA - LIMITE_SEGURANCA),
                              random.randrange(LIMITE_ASTEROIDE - LIMITE_SEGURANCA, LIMITE_ASTEROIDE),
                              random.randrange(1,20), random.randrange(1, 4), ASTEROIDE)

    PERSONAGEM_3 = Personagem(random.randrange(LIMITE_ESQUERDA + LIMITE_SEGURANCA, LIMITE_DIREITA - LIMITE_SEGURANCA),
                              random.randrange(LIMITE_ASTEROIDE, LIMITE_AVIAO),
                              random.randrange(1,20), random.randrange(1, 4), AVIAO)

    PERSONAGEM_4 = Personagem(random.randrange(LIMITE_ESQUERDA + LIMITE_SEGURANCA, LIMITE_DIREITA - LIMITE_SEGURANCA),
                              random.randrange(LIMITE_ASTEROIDE, LIMITE_AVIAO),
                              random.randrange(1,20), random.randrange(1, 4), AVIAO)

    PERSONAGEM_5 = Personagem(random.randrange(LIMITE_ESQUERDA, LIMITE_DIREITA), LIMITE_BAIXO , DX_PLATAFORMA, DY_PLATAFORMA, PLATAFORMA)

    PERSONAGEM_6 = Personagem(random.randrange(LIMITE_ESQUERDA, LIMITE_DIREITA), LIMITE_BAIXO , DX_PLATAFORMA, DY_PLATAFORMA, PLATAFORMA)

    L_PERSONAGEM = criar_lista(PERSONAGEM_1, PERSONAGEM_2, PERSONAGEM_3, PERSONAGEM_4, PERSONAGEM_5, PERSONAGEM_6)

    return L_PERSONAGEM

'''
mover_avioes: ListaPersonagem -> ListaPersonagem
Produz o próximo estado dos personagens
'''

def mover_personagens(personagens):
    return criar_lista([mover_personagem(ps) for ps in personagens ])


'''
muda_direcao_horizontal: Personagem-> Personagem
muda a direcao na horizontal do personagem
'''
def muda_direcao_horizontal(ps):
    return Personagem(ps.x - ps.dx, ps.y, -ps.dx, ps.dy, ps.tipo)

'''
muda_direcao_vertical: Personagem-> Personagem
muda a direcao na vertical do personagem
'''
def muda_direcao_vertical(ps):
    return Personagem(ps.x, ps.y - ps.dy, ps.dx, -ps.dy, ps.tipo)


'''
mover_aviao: Personagem -> Personagem
interp. produz o proximo estado de um personagem
'''

def mover_personagem(ps):

    if ps.tipo == ASTEROIDE or ps.tipo == AVIAO:

        if ps.x >= LIMITE_DIREITA or ps.x <= LIMITE_ESQUERDA:
            return muda_direcao_horizontal(ps)

        elif ps.tipo == ASTEROIDE:

            if ps.y >= LIMITE_ASTEROIDE or ps.y <= LIMITE_CIMA:
                return muda_direcao_vertical(ps)

        elif ps.tipo == AVIAO:

            if ps.y >= LIMITE_AVIAO or ps.y <= LIMITE_CIMA:
                return muda_direcao_vertical(ps)

    return Personagem(ps.x + ps.dx, ps.y + ps.dy, ps.dx, ps.dy, ps.tipo)

'''
desenha_personagem: Personagem -> Imagem
desenha um personagem na tela
'''
def desenha_personagem(ps):

    if ps.tipo == ASTEROIDE:
        colocar_imagem(IMG_ASTEROIDE, tela, ps.x, ps.y)

    elif ps.tipo == AVIAO and ps.x > 0:
        if ps.dx < 0:
            colocar_imagem(IMG_AVIAO_ESQUERDA, tela, ps.x, ps.y)

        if ps.dx > 0:
            colocar_imagem(IMG_AVIAO_DIREITA, tela, ps.x, ps.y)

    elif ps.tipo == PLATAFORMA:
        colocar_imagem(IMG_PLATAFORMA, tela, ps.x, ps.y)

'''
desenha_personagens: ListaPersonagem -> Imagem
Desenha os personagens na tela
'''
def desenha_personagens(ps):
    for perso in ps:
        desenha_personagem(perso)
