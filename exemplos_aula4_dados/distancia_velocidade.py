#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

''' PROBLEMA: quero calcular a distancia percorrida
 por um carro dada a velocidade e o tempo'''

''' CONSTANTES '''
MSG_ERRO_INVALIDO = "Erro: dado invalido"



'''DEFINIÇÕES DE DADOS'''
'''
Velocidade é um Float
interp. descreve a velocidade de um objeto em m/s
'''
#EXEMPLOS:
V_LENTO = 2
V_RAPIDA = 15
V_PARADO = 0
V_MARCHA_RE_LENTO = -2
V_MARCHA_RE_RAPIDO = -15

'''
#template
def fn_para_velocidade(v):
    ... v
'''

'''
Distancia é um Float
interp. descreve a distancia do ponto origem, m
'''
#EXEMPLOS:
D_FRENTE = 50
D_ORIGEM = 0
D_TRAS = -50

'''
#template
    def fn_para_distancia(d):
    ... d
'''


'''
Tempo é um Float (>=0) ou [0, +inf.]
interp. descreve o tempo em segundos (s)
'''
#EXEMPLOS
T_0 = 0
T_FINAL = 60
T_MEIO = T_FINAL // 2

'''
#template
def fn_para_tempo(t):
    if t < 0:
        return MSG_ERRO_INVALIDO
    ... t

'''

''' FIM DEFINIÇÕES DE DADOS'''


''' INICIO FUNÇÕES'''

'''
Tempo, Velocidade -> Distancia
Calcula a distancia dada a velocidade e tempo.
'''
def calcula_distancia(t, v):
    if t < 0:                    
        return MSG_ERRO_INVALIDO
    return t * v


class Test(unittest.TestCase):

    def test_calcula_distancia(self):
        self.assertEqual(calcula_distancia(15, 10), 150)
        self.assertEqual(calcula_distancia(0, 10), 0)
        self.assertEqual(calcula_distancia(10, 0), 0)
        self.assertEqual(calcula_distancia(15, -10), -150)
        self.assertEqual(calcula_distancia(-10, 10), MSG_ERRO_INVALIDO)


unittest.main() 
