# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual  foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import random

print('--' * 10)
print('Tente adivinhar um número entre 0 e 5: ')
print('--' * 10)

#Gerando número aleatório
num_alea = int(random.uniform(0, 5))

# pedi número pro usuário
numero = int(input('Qual número eu pensei? '))

# verificar número usuário == número(var)

if numero == num_alea:
    print('Você adivinhou!')
elif numero >= 6:
    print('Digite um valor entre 0 e 5')
else:
    print('Você não acertou!o número correto era: {}'.format(num_alea))

# Outra forma de resolução
from random import randint
from time import sleep

#Gerando número aleatório
computador = randint(0, 5)

print('-=-' * 10)
print('Adivinhe o número que eu pensei entre 0 e 5: ')
print('-=-' * 10)

# pedi número pro usuário
jogador = int(input('Digite o número: '))

#lib time/ método sleep
print('PROCESSANDO...')
sleep(3)

#Comparando os números
if jogador == computador:
    print('Você acertou!')
else:
    print('Você errou! o número correto era: {}'.format(computador))
