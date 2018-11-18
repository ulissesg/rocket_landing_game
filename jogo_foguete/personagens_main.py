from personagens import *

''' ================= '''
''' Main (Big Bang):'''


''' Aviao -> Aviao '''
''' inicie o mundo com AVIAO_INICIAL'''

def main(a):
    big_bang(a, tela=tela, frequencia= FREQUENCIA_AVIAO,
             quando_tick=mover_avioes,
             desenhar=...,
             modo_debug= True
             )

main(AVIAO_INICIAL)