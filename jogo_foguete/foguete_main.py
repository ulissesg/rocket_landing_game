from foguete import *

''' ================= '''
''' Main (Big Bang):'''


''' Foguete -> Foguete '''
''' inicie o mundo com FOGUETE_INCIAL'''

def main(f):
    big_bang(f, tela=tela, frequencia=FREQUENCIA_FOGUETE,
             quando_tick=move_foguete,
             desenhar=desenha_foguete,
             quando_tecla=trata_tecla,
             quando_solta_tecla= trata_solta_tecla,
             modo_debug= True
             )

main(FOGUETE_INICIAL)
