from htdp_pt_br.base import definir_estrutura

VAZIA = None
Lista = definir_estrutura("Lista", "primeiro, resto")
'''
ListaInteiros é um desses:
- Lista(Int, ListaInteiros) ou
- VAZIA
interp. uma lista vazia é representada por VAZIA (None), senão
é representada como uma estrutura do tipo Lista.
Exemplos:
'''
L_VAZIA = VAZIA
L_1 = Lista(1, VAZIA)
L_2 = Lista(5, L_1)
L_3 = Lista(7, L_2)

'''
#template
def fn_para_listainteiros(lista):
    if lista is vazia:
        ...
    else:
        ... lista.primeiro 
            fn_para_listainteiros(lista.resto)
'''



'''
dobra_todos: ListaInteiros -> ListaInteiros
'''
def dobra_todos(lista):
    if lista is VAZIA:
        return VAZIA
    else:
        return Lista(lista.primeiro*2,
                     dobra_todos(lista.resto))


'''
soma_todos: ListaInteiros -> Int
'''
def soma_todos(lista):
    if lista is VAZIA:
        return 0
    else:
        return lista.primeiro + soma_todos(lista.resto)


print(dobra_todos(L_3))
print(soma_todos(L_3))



'''
map: ListaInteiros -> Lista
'''
def map(funcao, lista):
    if lista is VAZIA:
        return VAZIA
    else:
        return Lista(funcao(lista.primeiro),
                     map(funcao, lista.resto))


import math
print(map(math.factorial, L_3))
import operator
print(map(lambda x: x*2, L_3))

'''
reduce: ListaInteiros -> Inteiro
'''
def reduce(funcao, lista, acc=0):
    if lista is VAZIA:
        return acc
    else:
        atual = funcao(acc, lista.primeiro)
        return reduce(funcao, lista.resto, atual)


print(reduce(operator.add, L_3))
print(reduce(operator.mul, L_3, acc=1))

##soma dos quadrados:
print(reduce(operator.add, map(lambda x: x**2, L_3)))