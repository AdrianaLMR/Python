# 25 Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Digite seu nome completo: ')).lower().split()
print('O nome tem Silva: {}'.format('silva' in nome))
