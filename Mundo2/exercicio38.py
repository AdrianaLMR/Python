# 38 escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - 0 primeiro valor é maior
# - 0 segundo valor é maior
# - Não existe valor maior, os dois são iguais

num_um = float(input('Digite o primeiro número: '))
num_dois = float(input('Digite o segundo número: '))

# Comparação dos números
if num_um > num_dois:
    print('O primeiro valor ({:.2f}) é maior'.format(num_um))
elif num_dois > num_um:
    print('O segundo valor ({:.1f}) é maior'.format(num_dois))
else:
    print('Não existe valor maior, os dois são iguais')
