#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PROBLEMA: Desenhar um tabuleiro de xadrez
'''

from universe import *

tela = criar_tela_base(400,400)

# QUADRADO = quadrado(100, Cor("red"))
# CIRCULO = circulo(30, Cor("green"))
# FRAME = folha_transparente(400, 400)
# FRAME = colocar_imagem(QUADRADO, FRAME, 50, 50)
# FRAME = colocar_imagem(CIRCULO, FRAME, 350, 350)
#
# OS_DOIS = encima(QUADRADO, CIRCULO)
# FRAME = colocar_imagem(OS_DOIS, FRAME, 150, 300)
#
#
# colocar_imagem_sobre_tela_e_mostrar(FRAME, 200, 200)

'''
quatro: Imagem -> Imagem     #assinatura
'''
def quatro(imagem):
    linha_de_cima = lado(imagem, imagem)
    linha_de_baixo = lado(imagem, imagem)
    img_final = encima(linha_de_cima, linha_de_baixo)
    return img_final

QUATRO_BOLAS = quatro(    circulo(50,Cor("blue"))     )

# colocar_imagem_sobre_tela_e_mostrar(QUATRO_BOLAS , 200, 200)
'''
dezesseis: Imagem -> Imagem     #assinatura
'''
def dezesseis(imagem):
    # quatro(quatro(imagem))
    quatro_imagens = quatro(imagem)
    return quatro(quatro_imagens)

DEZESSEIS_BOLAS = dezesseis(  circulo(20,Cor("green"))     )
# colocar_imagem_sobre_tela_e_mostrar(DEZESSEIS_BOLAS , 200, 200)

'''
padrao_xadrez: Int, Cor, Cor -> Imagem     #assinatura
'''
def padrao_xadrez(tamanho, cor1, cor2):
    quadrado_cor1 = quadrado(tamanho // 2, cor1)
    quadrado_cor2 = quadrado(tamanho // 2, cor2)
    dupla1 = lado(quadrado_cor1, quadrado_cor2)
    dupla2 = lado(quadrado_cor2, quadrado_cor1)
    img_final = encima(dupla1, dupla2)
    return img_final


import random
PADRAO_TESTE = padrao_xadrez(100, (random.randrange(0,256),
                                   random.randrange(0, 256),
                                   random.randrange(0,256)),
                                  (random.randrange(0,256),
                                   random.randrange(0,256),
                                   random.randrange(0, 256), ))   #EXEMPLO
# print(PADRAO_TESTE)
# colocar_imagem_sobre_tela_e_mostrar(PADRAO_TESTE, 200, 200)

'''
tabuleiro: Int, Cor, Cor -> Imagem     #assinatura
'''
def tabuleiro(tamanho, cor1, cor2):
    return dezesseis(padrao_xadrez(tamanho // 4, cor1, cor2))



TABULEIRO = tabuleiro(400, Cor("black"), Cor("gray"))  #exemplo
colocar_imagem_sobre_tela_e_mostrar(TABULEIRO, 200, 200)


#MAIN (PROGRAMA PRINCIPAL)

tamanho = int(input("Escreva o tamanho"))
cor1 = input()


