# 33 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Dgite o primeiro número: '))
n2 = int(input('Dgite o segundo número: '))
n3 = int(input('Dgite o terceiro número: '))

# verifica o menor número
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# verifica o maior número
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))

# Outra forma de resolução

number1 = int(input('Dgite o primeiro número: '))
number2 = int(input('Dgite o segundo número: '))
number3 = int(input('Dgite o terceiro número: '))
menor = number1
maior = number1

# verifica o menor número
if number2 < number1 and number2 < number3:
    menor = number2
if number3 < number1 and number3 < number2:
    menor = number3

# verifica o maior número
if number2 > number1 and number2 > number3:
    maior = number2
if number3 > number1 and number3 > number2:
    maior = number3

print('O número maior é {}'.format(maior))
print('O número menor é {}'.format(menor))
