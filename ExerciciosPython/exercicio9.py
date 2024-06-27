# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

numero = int(input('Digite um número'))

# Exibição da tabuada do número
print('Tabuada de {}:'.format(numero))
for i in range(1, 11):
    print('{} x {} = {}'.format(numero, i, numero * i))
