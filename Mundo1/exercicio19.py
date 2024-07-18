# Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno1 = str(input('digite o nome do primeiro aluno:'))
aluno2 = str(input('digite o nome do segundo aluno:'))
aluno3 = str(input('digite o nome do terceiro aluno:'))
aluno4 = str(input('digite o nome do quarto aluno:'))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)

print('O aluno escolhido para apagar o quadro é: {}'.format(escolhido))

