from personagens import *

''' ================= '''
''' Main (Big Bang):'''


''' ListaPersonagem -> ListaPersonagem '''
''' inicie o mundo com L_PERSONAGEM_MEIO'''

def main(a):
    big_bang(a, tela=tela, frequencia= FREQUENCIA_PERSONAGENS,
             quando_tick=mover_personagens,
             desenhar=desenha_personagens,
             modo_debug= True
             )

main(L_PERSONAGEM_MEIO)