from personagem import *

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Programada do foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (1200, 800)
tela = criar_tela_base(LARGURA, ALTURA)


FREQUENCIA_FOGUETE = 30
IMG_FOGUETE = carregar_imagem("foguete.png")
IMG_FOGUETE = definir_dimensoes(IMG_FOGUETE, 100, 80)

LIMITE_BAIXO = ALTURA - altura_imagem(IMG_FOGUETE) * 1.25
LIMITE_DIREITA = LARGURA - largura_imagem(IMG_FOGUETE) // 4
LIMITE_ESQUERDA = 0 + largura_imagem(IMG_FOGUETE) // 4
LIMITE_CIMA = 0 + altura_imagem(IMG_FOGUETE)

DX = 0
DY = 1
DDX = 5
DDY = 2
ACELERACAO_FOGUETE = 0.5
ACELERACAO_FOGUETE_CIMA = 0.1


TECLA_DIREITA = pg.K_RIGHT
TECLA_ESQUERDA = pg.K_LEFT
TECLA_CIMA = pg.K_UP

'''==================='''
'''# Definições de dados: '''


''' Foguete eh um personagem
interp. representa um foguete com suas posicoes e velocidades.
'''
#EXEMPLOS:
FOGUETE_INICIAL = Personagem(LIMITE_DIREITA//2, LIMITE_CIMA, DX, DY)
FOGUETE_MEIO = Personagem(LIMITE_DIREITA //2 , LIMITE_BAIXO //2, 2, -5)
FOGUETE_FINAL = Personagem(LIMITE_DIREITA//2, LIMITE_BAIXO, 3, -4)

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
    if f.y < LIMITE_BAIXO:

        if f.x <= LIMITE_ESQUERDA:

            if f.dy < 0:
                return Personagem(f.x + 1, f.y + f.dy, f.dx, f.dy - ACELERACAO_FOGUETE)
            return Personagem(f.x + 1, f.y + f.dy, f.dx, f.dy + ACELERACAO_FOGUETE_CIMA)

        if f.x >= LIMITE_DIREITA:
            if f.dy < 0:
                return Personagem(f.x - 1, f.y + f.dy, f.dx, f.dy - ACELERACAO_FOGUETE)
            return Personagem(f.x - 1, f.y + f.dy, f.dx, f.dy + ACELERACAO_FOGUETE_CIMA)

        if f.dy < 0:
            return Personagem(f.x + f.dx, f.y + f.dy, f.dx, f.dy - ACELERACAO_FOGUETE)
        return Personagem(f.x + f.dx, f.y + f.dy, f.dx, f.dy + ACELERACAO_FOGUETE_CIMA)

    return f


'''
desenha: Foguete -> Imagem
Desenha o foguete na tela
'''
def desenha_foguete(f):
    colocar_imagem(IMG_FOGUETE,tela, f.x, f.y)


'''
trata_tecla: Foguete, Tecla -> Foguete
Quando teclar pra cima o foguete sobe, pra direita move o foguete para a direita e para a esquerda move o foguete para esquerda.
'''

def trata_tecla(f, tecla):
    if f.y < LIMITE_BAIXO:

        if tecla == TECLA_CIMA:
            return Personagem(f.x, f.y, f.dx, -DDY)

        elif tecla == TECLA_DIREITA:
                return Personagem(f.x , f.y, DDX, f.dy)

        elif tecla == TECLA_ESQUERDA:
                return Personagem(f.x , f.y, -DDX, f.dy)

        return f

    return f

'''
trata_solta_tecla: Foguete, Tecla -> Foguete
interp. quando soltar a tecla devolve o novo estado do Foguete
'''

def trata_solta_tecla(f, t):
    if t == TECLA_CIMA:
        return Personagem(f.x, f.y, f.dx, DY)

    if t == TECLA_ESQUERDA or t == TECLA_DIREITA:
        return Personagem(f.x , f.y, 0, f.dy)

    return f
