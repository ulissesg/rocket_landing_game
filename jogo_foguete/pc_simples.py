from htdp_pt_br.universe import *

Pc_simples = definir_estrutura("Pc_simples", "x, y, dx, dy")
''' Foguete pode ser formado assim: Foguete(int[LIMITE_ESQUERDA, LIMITE_DIREITA], int[LIMITE_CIMA, LIMITE_BAIXO], int, int)
interp. representa um plano cartesiano com as posicoes x, y e as velocidades dos mesmos dx, dy.
'''
#EXEMPLOS:
PC_INICIAL = Pc_simples(0, 0, 1, 1)
PC_MEIO = Pc_simples(300, 200, 1, 1)
PC_FIM = Pc_simples(600, 400, 1, 1)
PC_DIREITO = Pc_simples(600, 200, 1, 1)
PC_ESQUERDO = Pc_simples(0, 200, 1, 1)

#TEMPLATE
'''
def fn_para_pc(f):
    ... pc.x
        pc.y
        pc.dx
        pc.dy
       
'''
