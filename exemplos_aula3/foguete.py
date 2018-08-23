
'''
Foguete é um Int [0, ALTURA]

'''
from universe import *



ALTURA = 400
LARGURA = 800

IMG_FOGUETE = carregar_imagem("foguete.png")  ## NÃO É O FOGUETE, É A REPRESENTAÇÃO DO FOGUETE
IMG_FOGUETE = definir_dimensoes(IMG_FOGUETE, 50,70)

ALTURA_FOGUETE = altura_imagem(IMG_FOGUETE)

tela = criar_tela_base(LARGURA, ALTURA)



'''
desenha_foguete: Foguete -> Imagem
Desenha um foguete na tela.
'''
def desenha_foguete(y):
    colocar_imagem(IMG_FOGUETE, tela, LARGURA // 2, y + ALTURA//2)
    # mostrar_tela()


#TESTES:


desenha_foguete(ALTURA - ALTURA_FOGUETE//2)

animar(desenha_foguete)





