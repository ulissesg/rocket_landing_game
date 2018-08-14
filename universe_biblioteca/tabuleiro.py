#!/usr/bin/env python
# -*- coding: utf-8 -*-


from universe import *


(LARGURA, ALTURA) = (400, 400)
tela = criar_tela_base(LARGURA, ALTURA)

quadrado_branco = retangulo(100,100,Cor("gray"))
quadrado_preto = retangulo(100,100,Cor("black"))



duplo_quadrado = lado(quadrado_preto, quadrado_branco)
duplo_quadrado2 = lado(quadrado_branco, quadrado_preto)
minixadrez = encima(duplo_quadrado, duplo_quadrado2)

xadrez = encima(lado(minixadrez, minixadrez), lado(minixadrez, minixadrez))

# colocar_imagem_sobre_tela_e_mostrar(minixadrez, minixadrez.get_width()//2 , minixadrez.get_height()//2)
colocar_imagem_sobre_tela_e_mostrar(xadrez, xadrez.get_width()//2 , xadrez.get_height()//2)


def xadrez(tamanho, cor1, cor2):
    dezesseis(padrao_xadrez(tamanho//4, cor1, cor2 ))

