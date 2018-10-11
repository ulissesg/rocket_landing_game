#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Programa da vaquinha '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

LARGURA, ALTURA = 600, 400
tela = criar_tela_base(LARGURA, ALTURA) #descomente isso

Y_VACA = ALTURA // 2
IMG_VACA_INO = carregar_imagem("./vaca.png")
IMG_VACA_VORTANO = espelhar(IMG_VACA_INO, True, False)
IMG_CHURRASQUEIRO = carregar_imagem("./churrasqueiro.png", 100, 130)

METADE_L_VACA = largura_imagem(IMG_VACA_INO) // 2
METADE_H_VACA = altura_imagem(IMG_VACA_INO) // 2
METADE_L_CHURRAS = largura_imagem(IMG_CHURRASQUEIRO) // 2
METADE_H_CHURRAS = altura_imagem(IMG_CHURRASQUEIRO) // 2

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
CHURRAS_INICIAL = Churrasqueiro(LARGURA//2, LIMITE_CIMA, 3)
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

'''
ListaChurras é um desses:
    - VAZIA
    - juntar(Churrasqueiro, ListaChurras)
'''
#Exemplos:
L_CHURRAS_1 = criar_lista(CHURRAS_INICIAL)
L_CHURRAS_INICIAL = criar_lista(
    Churrasqueiro(LARGURA//4, LIMITE_CIMA, 3),
    Churrasqueiro(LARGURA//2, ALTURA//2, 3),
    Churrasqueiro(LARGURA//2 + LARGURA//4, LIMITE_BAIXO, 3)
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


Jogo = definir_estrutura("Jogo", "vaca, churrasqueiros, game_over")
''' Jogo pode ser formado assim: Jogo(Vaca, ListaChurras, Boolean)
interp. representa o jogo todo com uma vaca e zero ou mais churrasqueiros. O campo
game_over indica se o jogo está acabado ou não.
'''
#EXEMPLOS:
JOGO_INICIAL_ANTIGO = Jogo(VACA_INICIAL, criar_lista(CHURRAS_INICIAL), False)  #CHAMANDO CONSTRUTOR
JOGO_MEIO = Jogo(Vaca(LARGURA//4, 3), criar_lista(Churrasqueiro(LARGURA//2, ALTURA//4, 6)), False)
JOGO_COLIDINDO = Jogo(VACA_MEIO, criar_lista(CHURRAS_MEIO), False)
JOGO_GAME_OVER = Jogo(VACA_MEIO, criar_lista(CHURRAS_MEIO), True)

JOGO_INICIAL = Jogo(VACA_INICIAL, L_CHURRAS_INICIAL, False)

#TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.churrasqueiros
        jogo.game_over
'''

'''===================='''
''' Funções: '''

'''
colidirem: Vaca, Churrasqueiro -> Boolean
Verifica se a vaca e o churrasqueiro colidiram
'''
def colidirem(vaca, churras):
    esquerda_vaca = vaca.x - METADE_L_VACA
    direita_vaca = vaca.x + METADE_L_VACA
    cima_vaca = Y_VACA - METADE_H_VACA
    baixo_vaca = Y_VACA + METADE_H_VACA

    esquerda_churras = churras.x - METADE_L_CHURRAS
    direita_churras = churras.x + METADE_L_CHURRAS
    cima_churras = churras.y - METADE_H_CHURRAS
    baixo_churras = churras.y + METADE_H_CHURRAS

    if direita_vaca >= esquerda_churras and \
        esquerda_vaca <= direita_churras and \
        baixo_vaca >= cima_churras and \
        cima_vaca <= baixo_churras:
        return True
    #else
    return False


'''
colidir_algum_churras: Vaca, ListaChurras -> Boolean
!!! TODO
'''
def colide_algum_churras(vaca, churrasqueiros):
    if churrasqueiros.vazia:
        return False
    else:
        return colidirem(vaca, churrasqueiros.primeiro) \
               or colide_algum_churras(vaca, churrasqueiros.resto)


'''
mover_churrasqueiros: ListaChurras -> ListaChurras
!!! TODO
'''
def mover_churrasqueiros(churrasqueiros):
    if churrasqueiros.vazia:
        return churrasqueiros
    else:
        return juntar(mover_churras(churrasqueiros.primeiro),
                      mover_churrasqueiros(churrasqueiros.resto))


'''
mover_tudo: Jogo -> Jogo
Produz o próximo estado do jogo
'''
def mover_tudo(jogo):
    if (not colide_algum_churras(jogo.vaca, jogo.churrasqueiros)):
        nova_vaca = mover_vaca(jogo.vaca)   ##funcao helper (auxiliar)
        novos_churras = mover_churrasqueiros(jogo.churrasqueiros)  ##funcao helper
        return Jogo(nova_vaca, novos_churras, False)
    else:
        return Jogo(jogo.vaca, jogo.churras, True)


'''
mover_churras: Churrasqueiro -> Churrasqueiro
Move o churrasqueiro no eixo y
'''
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
desenha_game_over: -> Imagem
Desenha a tela do game over
'''
def desenha_game_over():
    texto_game_over = texto("GAME OVER", Fonte("comicsans", 50), Cor("red"))
    colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//2)


'''
desenha_jogo: Jogo -> Imagem
Desenha todos os elementos do jogo de acordo com o estado atual
'''
def desenha_jogo(jogo):
    if (not jogo.game_over):
        desenha_vaca(jogo.vaca)
        desenha_churras(jogo.churras)
    else:
        desenha_game_over()

'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na posicao x'''
def desenha_vaca(vaca):
    if vaca.dx >= 0:
        colocar_imagem(IMG_VACA_INO, tela, vaca.x, Y_VACA)
    else:
        colocar_imagem(IMG_VACA_VORTANO, tela, vaca.x, Y_VACA)


'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Trata tecla para o jogo todo.
'''
# !!! TODO
def trata_tecla_jogo(jogo, tecla):
    if (not jogo.game_over):
        nova_vaca = trata_tecla_vaca(jogo.vaca, tecla)
        return Jogo(nova_vaca, jogo.churras, jogo.game_over)
    elif tecla == pg.K_RETURN:
        return JOGO_INICIAL
    else:
        return jogo




'''
trata_tecla: Vaca, Tecla -> Vaca  ##assinatura
Quando teclar "espaço" vira a vaca  '''
def trata_tecla_vaca(vaca, tecla):
    if tecla == TC_VIRAR:
        return Vaca(vaca.x, -vaca.dx)
    else:
        return vaca




