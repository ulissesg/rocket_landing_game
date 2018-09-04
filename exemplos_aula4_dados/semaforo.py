#!/usr/bin/env python
# -*- coding: utf-8 -*-


MSG_ERRO_INVALIDO = "Erro: dado invalido"

'''DEFINIÇÕES DE DADOS'''


'''
CorSemaforo é uma dessas:
    - "verde"
    - "amarelo"
    - "vermelho"
interp. a cor do semaforo
Exemplos: dispensa
'''

'''
#template
def fn_para_cor_semaforo(cs):
    if cs == "verde":
        ... cs
    elif cs == "amarelo":
        ... cs
    elif cs == "vermelho":
        ... cs
    else:
        return MSG_ERRO_INVALIDO
'''

'''
CorSemaforo -> CorSemaforo
'''

def proxima_cor(cs):
    if cs == "verde":
        return "amarelo"
    elif cs == "amarelo":
        return "vermelho"
    elif cs == "vermelho":
        return "verde"
    else:
        return MSG_ERRO_INVALIDO
