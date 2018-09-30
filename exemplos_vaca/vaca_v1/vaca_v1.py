#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Programa da vaquinha '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

LARGURA, ALTURA = 600, 400
tela = criar_tela_base(LARGURA, ALTURA) #descomente isso

Y = ALTURA // 2
IMG_VACA_INO = carregar_imagem("../figuras/vaca.png")  #caminho relativo
# caminho absoluto?  "c:/user/dkdk/"  "/home/fulano/..."
IMG_VACA_VORTANO = espelhar(IMG_VACA_INO, True, False)
FREQUENCIA = 60

TC_VIRAR = pg.K_SPACE

LIMITE_ESQUERDO = 0 + largura_imagem(IMG_VACA_INO) // 2
LIMITE_DIREITO = LARGURA - largura_imagem(IMG_VACA_INO) // 2

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



'''===================='''
''' Funções: '''

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
def desenha_vaca(vaca):
    # colocar_imagem(FUNDO, tela, )
    if vaca.dx >= 0:
        colocar_imagem(IMG_VACA_INO, tela, vaca.x, Y)
    else:
        colocar_imagem(IMG_VACA_VORTANO, tela, vaca.x, Y)


'''
trata_tecla: Vaca, Tecla -> Vaca  ##assinatura
Quando teclar "espaço" vira a vaca  '''
# !!! TODO
def trata_tecla(vaca, tecla):
    if tecla == TC_VIRAR:
        return Vaca(vaca.x, -vaca.dx)
    else:
        return vaca




