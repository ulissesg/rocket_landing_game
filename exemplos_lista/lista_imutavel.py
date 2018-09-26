
from htdp_pt_br.list import *

'''
Lista<Int> é um desses:
- conj(Int, Lista<Int>)
- VAZIA
Lista de inteiros
Exemplos:
'''
L_VAZIA = VAZIA
L_1 = conj(2, VAZIA)
L_2 = conj(5, L_1)
L_3 = conj(7, L_2)
L_10 = criar_lista(4,7,8,2,4,9,6,3,5,3)


'''
#template
def fn_para_lista<int>(lista):
    if lista.vazia:
        ...
    else:
        ... lista.primeiro 
            fn_para_lista<int>(lista.resto)
'''

'''
dobra_todos: ListaInteiros -> ListaInteiros
'''
def dobra_todos(lista):
    if lista.vazia:
        return lista
    else:
        return conj(lista.primeiro*2,
                     dobra_todos(lista.resto))
                           

print(dobra_todos(L_3))
print(dobra_todos(L_10))

import operator
print(criar_lista(tuple(map(lambda x: x*2, L_3))))