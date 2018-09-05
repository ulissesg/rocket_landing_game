
'''
Foguete é um Int [0, ALTURA]

'''
from universe import *



ALTURA = 200
LARGURA = 800

IMG_FOGUETE = carregar_imagem("foguete.png")  ## NÃO É O FOGUETE, É A REPRESENTAÇÃO DO FOGUETE
IMG_FOGUETE = definir_dimensoes(IMG_FOGUETE, 50,70)

ALTURA_FOGUETE = altura_imagem(IMG_FOGUETE)

tela = criar_tela_base(LARGURA, ALTURA)


'''
desenha_foguete: Foguete -> Imagem
Desenha um foguete na tela.
CONVENÇÃO: A ABNT DA PROGRAMAÇÃO. OBJETIVO: PADRONIZAR TEXTO DO CODIGO
REFATORAÇÃO: FAZER MELHORIAS EM CODIGO QUE JÁ ESTÁ FUNCIONANDO
'''
def desenha_foguete(y):
    chao = ALTURA - ALTURA_FOGUETE // 4
    if y > chao:
        colocar_imagem(IMG_FOGUETE, tela, LARGURA // 2, chao)
    else:
        colocar_imagem(IMG_FOGUETE, tela, LARGURA // 2, y)


    # mostrar_tela()


#TESTES:


# desenha_foguete(ALTURA - ALTURA_FOGUETE//2)

animar(desenha_foguete, frequencia=100)





