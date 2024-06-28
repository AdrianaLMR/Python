# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

numero = int(input('Digite um número para ver sua tabuada: '))

print('{} x {:2} x {}'.format(numero, 1, numero * 1))
print('{} x {:2} x {}'.format(numero, 2, numero * 2))
print('{} x {:2} x {}'.format(numero, 3, numero * 3))
print('{} x {:2} x {}'.format(numero, 4, numero * 4))
print('{} x {:2} x {}'.format(numero, 5, numero * 5))
print('{} x {:2} x {}'.format(numero, 6, numero * 6))
print('{} x {:2} x {}'.format(numero, 7, numero * 7))
print('{} x {:2} x {}'.format(numero, 8, numero * 8))
print('{} x {:2} x {}'.format(numero, 9, numero * 9))
print('{} x {:2} x {}'.format(numero, 10, numero * 10))

# Exibição da tabuada do número de outra forma
print('Tabuada de {}:'.format(numero))
for i in range(1, 11):
    print('{} x {:2} x {}'.format(numero, i, numero * i))
