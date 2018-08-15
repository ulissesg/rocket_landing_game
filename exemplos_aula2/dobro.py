#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

''' PROBLEMA: faça uma função que, dado um numero,
retorne o dobro do numero '''


'''
dobro: Float -> Float
Calcula dobro do numero.
'''
def dobro(n):
    return n*2

# #exemplos:
# x = dobro(4)   #deve dar 8
# print(x)


'''
Para cada nova funcao criada, voce deve criar uma funcao
dentro da classe Test para testá-la, conforme o template
'''
class Test(unittest.TestCase):

    def test_dobro(self):
        self.assertEqual(  dobro(4) ,  8  )
        self.assertEqual(  dobro(-2), -4  )
        self.assertEqual(  dobro(0),   0  )


    def test_raiz_quadrada(self):
        pass

unittest.main()  #não excluir (a menos que esteja rodando como unit test no PyCharm)



