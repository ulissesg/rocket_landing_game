from foguete import *

''' ================= '''
''' Main (Big Bang):'''


''' Foguete -> Foguete '''
''' inicie o mundo com ...'''
def main(f):
    big_bang(f, tela=tela, frequencia=FREQUENCIA_FOGUETE,
             quando_tick=move_foguete,
             desenhar=desenha,
             quando_tecla=trata_tecla,
             modo_debug= True
             )

main(FOGUETE_INICIAL)

