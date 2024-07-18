# Algoritmo que leia o sálario de um funcinário e mostre seu novo sálario, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$ '))
percentualAumento = 15
aumento = (percentualAumento / 100) * salario

total = salario + aumento
print('O valor total do aumento foi de : {:.2f}, com 15% de aumento'.format(total))

# outra forma de resolução

sal = float(input('Digite o preço do produto: '))
tot = sal + (sal * 15 / 100)
print('O valor do sário com aumento é de: {:.2f}, com 15% de aumento'.format(tot))

