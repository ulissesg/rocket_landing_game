from vaca_v1 import *

''' ================= '''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com VACA_INICIAL '''
def main(inic):
    big_bang(inic,   # Vaca
             tela=tela, frequencia=FREQUENCIA,
             quando_tick=mover_vaca,  # Vaca -> Vaca
             desenhar=desenha_vaca,   # Vaca -> Imagem
             quando_tecla=trata_tecla, # Vaca Tecla -> Vaca
             modo_debug=True,
             cor_fundo=Cor("lightgreen")
             )

main(VACA_INICIAL)