#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import *

tela = criar_tela_base( 500,500)
ALTURA_ESTRELA = 50
LARGURA_ESTRELA = 60
IMG_ESTRELA = carregar_imagem('Preto_e_branco_com_estrela_ao_meio.png', LARGURA_ESTRELA, ALTURA_ESTRELA)

quadrado_transparente = retangulo(LARGURA_ESTRELA, ALTURA_ESTRELA, pg.SRCALPHA)

FRAME_ESTRELAS = folha_transparente(retangulo_azul.get_width(), retangulo_azul.get_height())

estrelas = lado(quadrado_transparente, IMG_ESTRELA)

linha_seis = colocar_imagem (FRAME_ESTRELAS, estrelas, 100,100)

estrelas(500,500)

def estrelas (largura, altura ):
    quadrado_transparente = retangulo(largura, altura, pg.SRCALPHA)

