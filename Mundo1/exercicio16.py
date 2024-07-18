# 16 crie um programa que leia o número Real qualquer pelo teclado e mostre na tela sua porção inteira.
#EXemplo: num = 6.127 / O num tem a parte inteira 6.

import math
numero = float(input('Digite um número:'))
print('O número é: {}'.format(numero))

num = float(input('Digite um número:'))
print(math.trunc(num))

number = float(input('Digite um número:'))
print('A porção inteira de {} é {}'.format(number, math.trunc (number)))


from math import trunc
n = float(input('Digite um número:'))
print('A porção inteiro de {} é {}'.format(n, trunc(n)))
