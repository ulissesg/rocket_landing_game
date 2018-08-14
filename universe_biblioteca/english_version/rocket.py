#!/usr/bin/env python
# -*- coding: utf-8 -*-


from universe import *

''' Programa do Foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(WIDTH, HEIGHT) = (400, 400)
screen = create_base_screen(WIDTH, HEIGHT)

L_FOGUETE = 60
A_FOGUETE = 100
IMG_FOGUETE = rectangle(60, 100, pg.color.Color("darkred"))
IMG_FOGUETE = rotate(IMG_FOGUETE, 45)
BOLA = circle(50, Color("yellow"))
IMG_FOGUETE = overlay(IMG_FOGUETE, BOLA)

# X = 200  #numero magico
X = WIDTH // 2


'''==================='''
'''# Definições de dados: '''

''' Foguete é Int[0,HEIGHT] 
interp. representa a posicao y do foguete em pixels
Exemplos:
'''
F_INICIAL = 0
F_MEIO = HEIGHT//2
F_FINAL = HEIGHT
'''Template:
def fn_para_foguete(y):
    if y > HEIGHT or y < 0:
        return "Foguete invalido"
    else:
        ... y
'''



'''===================='''
''' Funções: '''

'''
desce: Foguete -> Foguete
Faz o foguete descer 3 pixels no eixo y, se não estiver no chao
'''
def desce(y):
    if y > HEIGHT or y < 0:
        return "Foguete invalido"
    else:
        if y >= HEIGHT - 2:
            return HEIGHT
        else:
            return y + 3


'''
desenha: Foguete -> Imagem
Desenha foguete na screen
'''
def desenha(y):
    # pg.draw.circle(screen, (203,230,67), (X, y), 20)
    place_image(IMG_FOGUETE, screen, X, y - A_FOGUETE + 28)

''' ================= '''
''' Main (Big Bang):
'''

''' Foguete -> Foguete '''
''' inicie o mundo com main()'''
def main():
    big_bang(F_INICIAL, screen=screen,
             on_tick=desce, \
             to_draw=desenha,
             debug_mode=True)



main()
# place_image_sobre_e_mostrar(screen, IMG_FOGUETE, 50, 50)
# pg.draw.rect(screen, "Red", )
    
