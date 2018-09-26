'''Templates'''

'''
Template para dados atômicos (Int, String, Float)
#exemplo:

Gato é Int
...
#template:

def fn_para_gato(g):
    ... g
'''


'''
Template para intervalos
#exemplo:

Foguete é Int[0, ALTURA]
...

#template:

def fn_para_foguete(f):
    if f < 0 or f > ALTURA:
        raise ValueError("ERRO: semaforo invalido")
    ... f
'''

'''
Template para dados enumerados
#exemplo:

def fn_para_semaforo(s):
    if s == "red":
        ... s
    elif s == "green":
        ... s
    elif s == "blue":
        ... s
    else:
        raise ValueError("ERRO: semaforo invalido")

'''

'''
Template para listas

#exemplo:

Lista<String> é um desses:
    - VAZIA
    - junta(

'''