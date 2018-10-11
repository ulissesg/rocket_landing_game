
from htdp_pt_br.list import *



'''
ListaInt é um desses:
    - VAZIA
    - juntar(Int, ListaInt)
'''
L_1 = juntar(5, VAZIA)
L_2 = juntar(10, L_1)
L_3 = juntar(15, L_2)

L_10 = criar_lista(56, 7, 8, 2, 4, 9, 39, 19)
print(L_3)
print(L_10)
print(L_10.primeiro)
print(L_10.resto)
# print(L_10.segundo)


'''
#template
def fn_para_lista(lista):
    if lista.vazia():
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''


'''
somatoria: ListaInt -> Int
'''
def somatoria(lista):
    if lista.vazia:
        return 0
    else:
        return lista.primeiro + somatoria(lista.resto)


print(somatoria(L_10))


def dobro(n):  #todas as função são de alta ordem
    return n*2


resultado = L_10.map(dobro)  ##iteração interna
print(resultado)

import math
print(L_10.map(math.sqrt))

import operator


print(L_10.reduce(operator.mul, 1))
# operator.