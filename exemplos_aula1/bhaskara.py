#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

''' PROBLEMA:
ax**2 + bx + c = 0, x???

Exemplos:
a = 1, b = 12, c = -13   =>   x1 = 1, x2 = -13
a = 1, b = -2, c = 16    =>   False

'''

''' Float Float Float -> (Float, Float) ou Float ou False'''
def bhaskara(a,b,c):   #definicao da funcao
    delta = b**2 - 4*a*c
    if delta < 0:
        return False
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        return (x1, x2)
    
   

#chamando:
    
print("Tamo ai")

resultado1 = bhaskara(1,-2,16)
print(resultado1)

resultado2 = bhaskara(1,12,-13)  #chamando
print(resultado2)


'''
QUeremos calcular isto
x**2 + 2x + 3 = 0
2x**2 + 2x +3 = 0
3x**2 + 2x +3 = 0
4x**2 + 2x +3 = 0
5x**2 + 2x +3 = 0
...

'''

for cont in range(1,1001):
    res = bhaskara(2, cont, 3)
    print(res)



'''
Bhaskara de exemplos aleatorios com parametros de 0 a 100
'''
import random
for cont in range(1000):
    a = random.randrange(1,101)
    b = random.randrange(1,101)
    c = random.randrange(1,101)
    res = bhaskara(a,b,c)
    print("Resultado para a =",a,"b =",b,"c =",c,"é",res)