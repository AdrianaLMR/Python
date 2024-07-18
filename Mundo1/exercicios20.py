# 20 O mesmo professor do desafio anterior(19) quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno1 = str(input('digite o nome do primeiro aluno:'))
aluno2 = str(input('digite o nome do segundo aluno:'))
aluno3 = str(input('digite o nome do terceiro aluno:'))
aluno4 = str(input('digite o nome do quarto aluno:'))
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A ordem de apresentação dos trabalhos será:')
print('\n'.join(alunos))

from random import  shuffle
n1 = str(input('digite o nome do primeiro aluno:'))
n2 = str(input('digite o nome do segundo aluno:'))
n3 = str(input('digite o nome do terceiro aluno:'))
n4 = str(input('digite o nome do quarto aluno:'))
lista = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação é: ')
print(lista)
