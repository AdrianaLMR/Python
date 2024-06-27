# Algoritmo que leia o sálario de um funcinário e mostre seu novo sálario, com 15% de aumento.

salario = float(input('Digite o preço do produto: '))
percentualAumento = 15
aumento = (percentualAumento / 100) * salario

total = salario + aumento
print('O valor total do aumento foi de : {}, com 15% de aumento'.format(total))
