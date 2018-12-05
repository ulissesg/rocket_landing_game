from jogo import *

''' Main (Big Bang):'''


''' Jogo -> Jogo '''
''' inicie o mundo com cria_novo_jogo'''
def main(j):
    big_bang(j, tela=tela, frequencia= FREQUENCIA,
             quando_tick=mover_jogo,
             desenhar=desenha,
             quando_tecla=trata_tecla_jogo,
             quando_solta_tecla=trata_solta_tecla_jogo,
             )


main(cria_novo_jogo())