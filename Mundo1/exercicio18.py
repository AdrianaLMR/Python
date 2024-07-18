# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um ângulo: '))
print(angulo)
ang_rad = math.radians(angulo)
print(ang_rad)
seno = math.sin(ang_rad)
print('O seno do ângulo {} é igual a: {:.2f}'.format(angulo, seno))
cosseno = math.cos(ang_rad)
print('O cosseno do ângulo {} é igual a: {:.2f}'.format(angulo, cosseno))
tangente = math.tan(ang_rad)
print('O tangente do ângulo {} é igual a: {:.2f}'.format(angulo, tangente))

# Outra forma de resolução
from math import sin, cos, tan, radians

ang = float(input('Digite o vlor do ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O valor do seno é {:.2f} \n O valor do Cosseno é {:.2f} \n o valor da tangente é {:.2f}'.format(sen, cos, tan))
