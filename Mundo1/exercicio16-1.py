# 16 crie um programa que leia o número Real qualquer pelo teclado e mostre na tela sua porção inteira.
#EXemplo: num = 6.127 / O num tem a parte inteira 6.

#Outra forma de resolução do desafio

num = float(input('Digite um valor: '))
print('O valor digitado é {} e sua porção inteira é {}'.format(num, int(num)))
