# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print('A média do aluno é igual a: {:.2f}'.format(media))

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

mediaFinal = (n1 + n2) / 2
print('A média do aluno é igual a: {:.1f}'.format(mediaFinal)) #Arendonda a media dependendo do valor resultante

