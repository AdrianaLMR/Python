print('Tipos primitivos')

number = input('Digite um valor')
print(type(number))

value = int(input('Digite um valor'))
print(type(value))

value1 = int(input('Digite um valor:'))
value2 = int(input('Digite outro valor:'))
calculo = value1 - value2
print('O resultado do calculo é: {}'.format(calculo))

#print('A subtração entre ', value1, 'e', value2, 'é igual a: ', calculo) - Formato antigo do python
print('A subtração entre {} e {} é igual a: {}'.format(value1, value2, calculo))


