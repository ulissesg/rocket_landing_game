
from htdp_pt_br.base import *

ListaString = definir_estrutura("ListaString", "primeiro, resto")
ListaInt = definir_estrutura("ListaInt", "primeiro, resto")
'''
ListaString pode ser um desses:
    - VAZIA
    - ListaString(String, ListaString)
interp. lista de strings
'''
#Exemplos:

VAZIA = None
L_1 = ListaString("feijao", VAZIA)
L_2 = ListaString("bolacha", L_1)
L_3 = ListaString("macarrão", L_2)
L_4 = ListaString("arroz", L_3)
L_5 = ListaString("refri", L_4)

'''
#templates
def fn_para_lista(lista):
    if lista is VAZIA:
        return ...
    else:
        ... lista.primeiro
            fn_para_lista(lista.resto)
'''


print(L_5)


'''
check_todas: ListaString -> ListaString
Coloca 'COMPRADO' na frente dos itens 
'''
def check_todas(lista):
    if lista is VAZIA:
        return lista   ##CASO BASE (CONDIÇÃO DE PARADA)
    else:
        return ListaString(lista.primeiro + " COMPRADO",
                           check_todas(lista.resto))  ##PASSO RECURSIVO


resultado = check_todas(VAZIA)
print(resultado)
resultado = check_todas(L_5)
print(resultado)


LL_1 = ListaInt(5, VAZIA)
LL_2 = ListaInt(10, LL_1)
LL_3 = ListaInt(15, LL_2)

'''
dobra_tudo: ListaInt -> ListaInt
'''
def dobra_tudo(lista):
    if lista is VAZIA:
        return lista
    else:
        return ListaInt( lista.primeiro*2,
                         dobra_tudo(lista.resto))

'''
somatoria: ListaInt -> Int
'''
def somatoria(lista):
    if lista is VAZIA:
        return 0
    else:
        return lista.primeiro + somatoria(lista.resto)


print(dobra_tudo(LL_3))

print(somatoria(LL_3))