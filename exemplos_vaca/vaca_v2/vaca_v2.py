#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Programa da vaquinha '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

LARGURA, ALTURA = 600, 400
tela = criar_tela_base(LARGURA, ALTURA) #descomente isso

Y = ALTURA // 2
IMG_VACA_INO = carregar_imagem("./vaca.png")
IMG_VACA_VORTANO = espelhar(IMG_VACA_INO, True, False)
IMG_CHURRASQUEIRO = carregar_imagem("./churrasqueiro.png", 100, 130)


FREQUENCIA = 60

TC_VIRAR = pg.K_SPACE

LIMITE_ESQUERDO = 0 + largura_imagem(IMG_VACA_INO) // 2
LIMITE_DIREITO = LARGURA - largura_imagem(IMG_VACA_INO) // 2
LIMITE_CIMA = 0 #altura_imagem(IMG_CHURRASQUEIRO) // 2
LIMITE_BAIXO = ALTURA
               #- altura_imagem(IMG_CHURRASQUEIRO) // 2



# API = Application Programming Interface


'''==================='''
'''# Definições de dados: '''


Vaca = definir_estrutura("Vaca", "x, dx")
''' Vaca pode ser formada da seguinte forma: Vaca(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[-LARGURA, +LARGURA])
interp. representa a posição da vaca no eixo x, e sua velocidade
e direção (dx)
'''
#EXEMPLOS:
VACA_INICIAL = Vaca(LIMITE_ESQUERDO, 3)
VACA_MEIO = Vaca(LARGURA//2, 3)
VACA_FIM = Vaca(LIMITE_DIREITO, 3)
VACA_FIM_VIRADA = Vaca(LIMITE_DIREITO, -3)
VACA_VORTANO_MEIO = Vaca(LARGURA//2, -3)
VACA_VORTANO_INICIO = Vaca(LIMITE_ESQUERDO, -3)

##TEMPLATE
'''
def fn_para_vaca(vaca):
    ... vaca.x
        vaca.dx
'''


Churrasqueiro = definir_estrutura("Churrasqueiro", "x, y, dy")
''' Churrasqueiro pode ser formado como: Churrasqueiro(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[LIMITE_CIMA, LIMITE_BAIXO], Int)
interp. representa a posição do churrasqueiro no eixo, x, y, e velocidade
e direção dy 
'''
#EXEMPLOS:
CHURRAS_INICIAL = Churrasqueiro(LARGURA//2, LIMITE_CIMA, 6)
CHURRAS_MEIO = Churrasqueiro(LARGURA//2, ALTURA//2, 6 )
CHURRAS_FIM = Churrasqueiro(LARGURA//2, LIMITE_BAIXO, 6)
CHURRAS_FIM_VIRADA = Churrasqueiro(LARGURA//2, LIMITE_BAIXO, -6)
CHURRAS_VORTANO_MEIO = Churrasqueiro(LARGURA//2, ALTURA//2, -6)

##TEMPLATE
'''
def fn_para_churras(churras):
    if churras.x < LIMITE_ESQUERDO or churras.x > LIMITE_DIREITO: #VALIDAÇÃO
        raise ValueError("ERRO: churrasqueiro invalido (x está fora dos limites)")
    #COLOCAR VALIDACAO ṔARA Y
    ... churras.x
        churras.y
        churras.dy
'''


Jogo = definir_estrutura("Jogo", "vaca, churras, game_over")
''' Jogo pode ser formado assim: Jogo(Vaca, Churrasqueiro, Boolean)
interp. representa o jogo todo com uma vaca e um churrasqueiro. O campo
game_over indica se o jogo está acabado ou não.
'''
#EXEMPLOS:
JOGO_INICIAL = Jogo(VACA_INICIAL, CHURRAS_INICIAL, False)  #CHAMANDO CONSTRUTOR
JOGO_MEIO = Jogo(Vaca(LARGURA//4, 3), Churrasqueiro(LARGURA//2, ALTURA//4, 6), False)
JOGO_COLIDINDO = Jogo(VACA_MEIO, CHURRAS_MEIO, False)
JOGO_GAME_OVER = Jogo(VACA_MEIO, CHURRAS_MEIO, True)

#TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.churras
        jogo.game_over
'''

'''===================='''
''' Funções: '''

'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo
'''
# !!! TODO
def mover_tudo(jogo):
    nova_vaca = mover_vaca(jogo.vaca)   ##funcao helper (auxiliar)
    novo_churras = mover_churras(jogo.churras)  ##funcao helper
    return Jogo(nova_vaca, novo_churras, False)


'''
mover_churras: Churrasqueiro -> Churrasqueiro
Move o churrasqueiro no eixo y
'''
# !!! TODO
def mover_churras(churras):
    posicao_y_futura = churras.y + churras.dy
    if posicao_y_futura > LIMITE_BAIXO \
            or posicao_y_futura < LIMITE_CIMA:
        return Churrasqueiro(churras.x, churras.y, -churras.dy)
    # else (senao)
    return Churrasqueiro(churras.x, posicao_y_futura , churras.dy)


'''
mover_vaca: Vaca -> Vaca
Produz a próxima vaca (move ela no eixo x)'''
def mover_vaca(vaca):
    posicao_x_futura = vaca.x + vaca.dx
    if posicao_x_futura > LIMITE_DIREITO \
            or posicao_x_futura < LIMITE_ESQUERDO:
        return Vaca(vaca.x, -vaca.dx)
    #else (senao)
    return Vaca(posicao_x_futura, vaca.dx)

'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na posicao x'''
def desenha_churras(churras):
    colocar_imagem(IMG_CHURRASQUEIRO, tela, churras.x, churras.y)


'''
desenha_jogo: Jogo -> Imagem
Desenha todos os elementos do jogo de acordo com o estado atual
'''
# !!! TODO
def desenha_jogo(jogo):
    desenha_vaca(jogo.vaca)
    desenha_churras(jogo.churras)

'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na posicao x'''
def desenha_vaca(vaca):
    if vaca.dx >= 0:
        colocar_imagem(IMG_VACA_INO, tela, vaca.x, Y)
    else:
        colocar_imagem(IMG_VACA_VORTANO, tela, vaca.x, Y)


'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Trata tecla para o jogo todo.
'''
# !!! TODO
def trata_tecla_jogo(jogo, tecla):
    return jogo


'''
trata_tecla: Vaca, Tecla -> Vaca  ##assinatura
Quando teclar "espaço" vira a vaca  '''
def trata_tecla_vaca(vaca, tecla):
    if tecla == TC_VIRAR:
        return Vaca(vaca.x, -vaca.dx)
    else:
        return vaca




