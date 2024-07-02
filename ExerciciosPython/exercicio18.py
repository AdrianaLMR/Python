# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um ângulo: '))
print(angulo)

ang_rad = math.radians(angulo)
print(ang_rad)

seno = math.sin(ang_rad)
print('O seno do ângulo {} é igual a: {}'.format(angulo, seno))

cosseno = math.cos(ang_rad)
print('O cosseno do ângulo {} é igual a: {}'.format(angulo, cosseno))

tangente = math.tan(ang_rad)
print('O tangente do ângulo {} é igual a: {}'.format(angulo, tangente))

