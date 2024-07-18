# 30 Crie um programa que leia um número inteiro e mostre na tela se ele é par ou inpar.
# O resto de números pares são 0 e o de impar são 1.

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Par')
else:
    print('Inpar')

# Outra forma de resolução
number = int(input('Digite um número: '))
result = number % 2

if number == 0:
    print('O número {} é Par'.format(number))
else:
    print('O número {} é Inpar'.format(number))
