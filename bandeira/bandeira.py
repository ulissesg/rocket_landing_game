#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PROBLEMA: Desenhar a bandeira dos EUA
'''

from universe import *

ALTURA = 390
LARGURA = 700



#tela base
tela = criar_tela_base(LARGURA, ALTURA)

#declaracao das faixas
faixa_vermelha = retangulo(LARGURA , 30,Cor(200,0,0))
faixa_branca= retangulo(LARGURA, 30, Cor("white"))

#conjunto de faixas
dupla_faixa= encima(faixa_vermelha, faixa_branca)

quatro_faixas = encima(dupla_faixa, dupla_faixa)

oito_faixas = encima(quatro_faixas, quatro_faixas)

dezesseis_faixas = encima(oito_faixas, oito_faixas)

#retangulo azul
retangulo_azul = retangulo(LARGURA // 2.3, ALTURA //1.779 , Cor(0,0,180))

#imagem das estrelas

IMG_ESTRELA = carregar_imagem('Estrelas.png', 280 , 200 )

img_retangulo = sobrepor(IMG_ESTRELA, retangulo_azul)

#montagem da bandeira
bandeira = colocar_imagem(img_retangulo, dezesseis_faixas, LARGURA // 4.666666667,ALTURA // 3.9)


#MOSTRAR
colocar_imagem_sobre_tela_e_mostrar(bandeira, LARGURA //2 , ALTURA // 1.625)