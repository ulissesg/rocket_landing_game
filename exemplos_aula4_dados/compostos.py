#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *


# Como seria com classes:
# class Aluno:
#     def __init__(self, nome, cpf, grr, idade):
#         self.nome = nome
#         self.cpf = cpf
#         self.grr = grr
#         self.idade = idade



Aluno = definir_estrutura("Aluno", "nome, cpf, grr, idade")

aluno1 = Aluno("Gabriel", 123450, 2018363, 18)
aluno2 = Aluno("Ulisses", 54321, 201892, 18)

print(aluno1.nome)
print(aluno2.nome)
print(aluno2.grr)

print(aluno1)

aluno3 = aluno1

# aluno3.nome = "Gabriel Angelo"  #só funciona se mutavel=True na definição de Aluno

print(aluno3.nome)
print(aluno1.nome)

Ponto = definir_estrutura("Ponto", "x, y")

posicao1 = Ponto(50,50)

print(posicao1)




Musica = definir_estrutura("Musica", "titulo, artista, duracao, album, genero")
'''
Musica é formada assim: Musica(String, String, Int, String, String)
interp. representa uma musica com os campo titulo, artista, duracao, album, genero,
a duração é em segundos.
'''
#exemplos
MUSICA1 = Musica("Na Sola da Bota", "Rio Negro e Solimões",
                 3*60+50, "Sertanejo do Buteco", "Sertanejo")
MUSICA2 = Musica("Arco iris feliz", "Patati Patatá", 20*60,
                 "Palhacinho Camarada", "Infantil")
'''
#template
def fn_para_musica(m):
    ... m.titulo
        m.artista
        m.duracao
        m.album
        m.genero
'''



'''
duracao_maior: Musica Musica -> Musica
Encontra a musica com a maior duração.
'''
def duracao_maior(m1, m2):
    if (m1.duracao > m2.duracao):
        return m1
    #else
    return m2


import unittest
class Test(unittest.TestCase):

    def test_duracao_maior(self):
        self.assertEqual(duracao_maior(MUSICA1, MUSICA2),  MUSICA2)
        self.assertEqual(duracao_maior(MUSICA2, MUSICA1),  MUSICA2)


unittest.main()


