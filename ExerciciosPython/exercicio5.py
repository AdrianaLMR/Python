# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor.

numero = int(input('Digite um número: '))

sucessor = numero + 1
antecessor = numero - 1
penultimo = numero - 2

print('O sucessor de {} é: {}, o  antecesor é: {} e o penultimo é: {}'.format(numero, sucessor, antecessor, penultimo))
