# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print('A média do aluno é igual a: {}'.format(media))
