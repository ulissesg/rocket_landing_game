
from gato2 import  *

''' ================= '''
''' Main (Big Bang):
'''

''' Gato -> Gato '''
''' inicie o mundo com GATO_INICIAL '''
def main(inic):
    big_bang(inic, frequencia=FREQUENCIA,
             quando_tick=mover,  #Gato -> Gato  #LISTA DE DESEJOS
             desenhar=desenha,   #Gato -> Imagem
             quando_tecla=trata_tecla, #Gato, Tecla -> Gato
             parar_quando=final_da_tela,  #Gato -> Boolean
             modo_debug=True
    )


main(GATO_INICIAL)   #chamando o main com estado inicial  = 0