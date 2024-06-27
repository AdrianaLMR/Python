# Crie um algoritmo que leia um número e mostre o seu dobro, tiplo e rais quadrada.

numero = int(input('digite um número: '))

dobro = numero * 2
tiplo = numero * 3
raiz = numero ** (1/2)

print('O dobro de {} é igual a: {}, O tiplo é: {} e \n A raiz quadrada de {} é: {:.2f}. '.format(numero, dobro, tiplo,numero, raiz))

#sem var
n = int(input('digite um número: '))

print('O dobro de {} é igual a: {}, O tiplo é: {}. '.format(n, (n * 2), (n * 3)))
print('A raiz de {} é igual a: {:.2f}'.format(n, (n ** (1/2))))
print('A raiz de {} é igual a: {:.3f}'.format(n, pow(n, (1/2))))
