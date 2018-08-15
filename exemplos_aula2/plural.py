#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


''' PROBLEMA: Fazer uma função que recebe uma palavra e pluraliza
a palavra. Ex: 'carro' -> 'carros'
'''

'''
plural: String -> String
Colocar a palavra no plural
'''
def plural(p):
    return p + "s"


'''Para cada nova funcao criada, voce deve criar uma funcao
dentro da classe Test para testá-la, conforme o template
'''
class Test(unittest.TestCase):

    def test_plural(self):
        self.assertEqual(   plural("mesa"), "mesas"   )
        self.assertEqual(   plural("cadeira"), "cadeiras"   )


# unittest.main()  #não excluir (a menos que esteja rodando como unit test no PyCharm)