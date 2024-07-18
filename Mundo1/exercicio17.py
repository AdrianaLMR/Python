# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa.

from math import hypot
catO = float(input('Digite o comprimento do cateto oposto: '))
catA = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(catA, catO)
print('o valor da hipotenusa é: {:.2f}'.format(hip))


import math
catetoO = float(input('Digite o comprimento do cateto oposto: '))
catetoA = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt((catetoA ** 2) + (catetoO ** 2))
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

# Forma tradicional
co = float(input('Digite o valor do cateto Oposto: '))
ca = float(input('Digite o valor de cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
