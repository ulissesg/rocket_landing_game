#!/usr/bin/env python
# -*- coding: utf-8 -*-

from personagens import *
from foguete import *

''' Jogo de pousar foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (1200, 700)
tela = criar_tela_base(LARGURA, ALTURA)

IMG_FUNDO = carregar_imagem("imagens/fundo.png")
IMG_FUNDO = definir_dimensoes(IMG_FUNDO, LARGURA, ALTURA)

FREQUENCIA= 30

X_BOOST= LARGURA // 2 * 1.5
Y_BOOST= 50
COR_BOOST= "red"
TAMANHO_BOOST = 30
PONTOS_BOOST= 10
FONTE_BOOST= "monospace"

METADE_L_FOGUETE = largura_imagem(IMG_FOGUETE) // 2
METADE_H_FOGUETE = altura_imagem(IMG_FOGUETE) // 2
METADE_L_PS = largura_imagem(IMG_AVIAO) // 2
METADE_H_PS = altura_imagem(IMG_AVIAO) // 2

LIMITE_CIMA_PLATAFORMA  = LIMITE_BAIXO - altura_imagem(IMG_PLATAFORMA)

TECLA_ENTER = pg.K_RETURN

'''==================='''
'''# Definições de dados: '''

Jogo = definir_estrutura("Jogo", "foguete, personagens, booster, game_over, win")
''' Jogo pode ser formado como: Jogo(Foguete, ListaPersonagem, Int, Boolean, Boolean)
interp. representa o jogo sendo ele conposto por um foguete, os personagens(obstaculos), um contador para o booster,
um game over, e um check se ganhou.
'''
#EXEMPLOS:
JOGO_INICIAL= Jogo(FOGUETE_INICIAL, L_PERSONAGEM_MEIO, 0, False, False)

JOGO_MEIO= Jogo(FOGUETE_MEIO, L_PERSONAGEM_INICIAL, 0, False, False)

JOGO_GAME_OVER = Jogo(FOGUETE_MEIO, L_PERSONAGEM_INICIAL, 30, True, True)

JOGO_GAME_OVER_2= Jogo(FOGUETE_INICIAL, L_PERSONAGEM_INICIAL, 40, True, True)



##TEMPLATE
'''
def fn_para_jogo(jogo):
    if jogo.game_over == False:
        ...jogo.foguete
           jogo.asteroide
           ...
    ...jogo.foguete
       jogo.asteroide
       ...
'''


'''===================='''
''' Funções: '''

'''
cria_jogo_inicial: -> Lista 
cria um novo jogo 
'''

def cria_jogo_inicial():

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

    L_PERSONAGEM_MEIO = criar_lista(
        PERSONAGEM_1, PERSONAGEM_2, PERSONAGEM_3, PERSONAGEM_4, PERSONAGEM_5, PERSONAGEM_6
    )

    return Jogo(JOGO_INICIAL.foguete, L_PERSONAGEM_MEIO, 0, False, False)

'''
colidem: Foguete, Personagem -> Boolean
se os personagens nao colidirem com o foguete retorna TRUE senao retorna FALSE
'''

def colidem(f, ps):
    cima_foguete = f.y - METADE_H_FOGUETE
    baixo_foguete = f.y + METADE_H_FOGUETE
    direita_foguete = f.x + METADE_L_FOGUETE
    esquerda_foguete = f.x - METADE_L_FOGUETE

    cima_ps = ps.y - METADE_H_PS
    baixo_ps = ps.y + METADE_H_PS
    direita_ps = ps.x + METADE_L_PS
    esquerda_ps = ps.x - METADE_L_PS

    if ps.tipo != 3:

        if f.y <= LIMITE_BAIXO:
            return direita_foguete >= esquerda_ps and \
                   esquerda_foguete <= direita_ps and \
                   baixo_foguete >= cima_ps and \
                   cima_foguete <= baixo_ps
        return True

    return False

'''
colide_algum_ps: Foguete, ListaPersonagem -> Boolean
interp. verifica se algum personagem da lista esta colidindo com o foguete
'''
def colide_algum_ps(f, personagens):
    return personagens.ormap(lambda ps: colidem(f, ps))

'''
check_win: Foguete, Personagem -> Boolean
interp. se ganhou retorna True, senao retorna False
'''
def check_win(f, ps):
    if ps.tipo == 3:
        cima_foguete = f.y - METADE_H_FOGUETE
        baixo_foguete = f.y + METADE_H_FOGUETE
        direita_foguete = f.x + METADE_L_FOGUETE
        esquerda_foguete = f.x - METADE_L_FOGUETE

        cima_ps = ps.y - METADE_H_PS // 4
        baixo_ps = ps.y + METADE_H_PS
        direita_ps = ps.x + METADE_L_PS
        esquerda_ps = ps.x - METADE_L_PS

        return direita_foguete >= esquerda_ps and \
               esquerda_foguete <= direita_ps and \
               baixo_foguete >= cima_ps and \
               cima_foguete <= baixo_ps
    return False

'''
ganhou: Foguete, ListaPersonagem -> Boolean
interp. verifica se o foguete chegou em alguma plataforma da lista
'''
def ganhou(f, personagens):
    return personagens.ormap(lambda ps: check_win(f, ps))

'''
mover_jogo: Jogo -> Jogo
Produz o próximo estado do jogo
'''
def mover_jogo(j):

    if not j.win:

        if not j.game_over:

            if not colide_algum_ps(j.foguete, j.personagens):

                if not ganhou(j.foguete, j.personagens):

                    return Jogo(move_foguete(j.foguete), mover_personagens(j.personagens), j.booster, j.game_over, j.win)

                return Jogo(move_foguete(j.foguete), mover_personagens(j.personagens), j.booster, j.game_over, True)

            return Jogo(move_foguete(j.foguete), mover_personagens(j.personagens), j.booster, True, j.win)

        return j

    return j



'''
desenha: Jogo -> Imagem
Desenha o estado atual do jogo
'''

def desenha(j):
    colocar_imagem(IMG_FUNDO, tela, LARGURA // 2, ALTURA // 2)

    desenha_personagens(j.personagens)
    desenha_foguete(j.foguete)
    desenha_boost(j.booster)

    if j.game_over:
        desenha_game_over()
    elif j.win:
        desenha_won()


'''
desenha_game_over: -> Imagem
desenha game over na tela
'''

def desenha_game_over():
    texto_game_over = texto("GAME OVER", Fonte("comicsans", 50), Cor("red"))
    colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//2)
    texto_continuar = texto("Tecle enter para jogar novamente", Fonte("comicsans", 30), Cor("red"))
    colocar_imagem(texto_continuar, tela, LARGURA//2, ALTURA//1.8)

'''
desenha_win: -> Imagem
desenha you win na tela 
'''
def desenha_won():
    texto_won = texto("YOU WON", Fonte("comicsans", 50), Cor("red"))
    colocar_imagem(texto_won, tela, LARGURA//2, ALTURA//2)
    texto_continuar = texto("Tecle enter para jogar novamente", Fonte("comicsans", 30), Cor("red"))
    colocar_imagem(texto_continuar, tela, LARGURA//2, ALTURA//1.8)


'''
desenha_boost: Int -> Imagem
'''
def desenha_boost(b):
    if b > 30:
        texto_booster_maximo = texto("Boost: 30", Fonte(FONTE_BOOST, TAMANHO_BOOST), Cor(COR_BOOST))
        colocar_imagem(texto_booster_maximo, tela, X_BOOST, Y_BOOST)

    elif b <= 30:
        texto_booster = texto("Boost: " + str(b), Fonte(FONTE_BOOST, TAMANHO_BOOST), Cor(COR_BOOST))
        colocar_imagem(texto_booster, tela, X_BOOST, Y_BOOST)


'''
trata_tecla_jogo: Jogo, Tecla -> Jogo
Quando teclar pra cima o foguete sobe, pra direita move o foguete para a direita e para a esquerda move o foguete para esquerda
se teclar enter reinicia o jogo.
'''

def trata_tecla_jogo(j, tecla):
    if tecla == TECLA_CIMA and j.booster >= PONTOS_BOOST * 3:
        return Jogo(j.foguete, j.personagens, j.booster + PONTOS_BOOST, j.game_over, j.win)

    elif tecla == TECLA_CIMA:
        return Jogo(trata_tecla(j.foguete, tecla), j.personagens, j.booster + PONTOS_BOOST, j.game_over, j.win)

    elif tecla == TECLA_ENTER:
        return cria_jogo_inicial()

    return Jogo(trata_tecla(j.foguete, tecla), j.personagens, j.booster, j.game_over, j.win)




'''
trata_solta_tecla: Jogo, Tecla -> Jogo
interp. quando soltar a tecla devolve o novo estado do Foguete
'''

def trata_solta_tecla_jogo(j, tecla):

    if tecla == TECLA_CIMA and j.booster > PONTOS_BOOST * 3:
        return j

    if tecla == TECLA_CIMA and j.booster == PONTOS_BOOST * 3:
        return Jogo(Personagem(j.foguete.x, j.foguete.y, j.foguete.dx, DY, j.foguete.tipo),
                    j.personagens, j.booster, j.game_over, j.win)

    return Jogo(trata_solta_tecla(j.foguete, tecla), j.personagens, j.booster, j.game_over, j.win)

