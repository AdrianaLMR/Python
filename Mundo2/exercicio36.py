# 36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador  e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
# empréstimo será negado.

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite quantos anos pretende pagar o valor da casa: '))

#Calcula o valor da prestaçaõ mensal
meses_pagamento = anos * 12 #converte anos em meses
prestacao = salario / 30 #divide o valor da casa pelo número de meses de pagamento.

# Verificase a prestação mensal é maior que 30% do salário
limite = salario * 0.3

print('\n Analisando o empréstimo...')
if prestacao <= limite:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')

print('Para Pagar uma casa de R${:.2f} em {} anso'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
# exemplo aula
cas = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
ano = int(input('Digite quantos anos pretende pagar o valor da casa: '))

prest = casa / (ano * 12)
minimo = sal * 30 / 100
if prest <= minimo:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo Negado!')
print('Para Pagar uma casa de R${:.2f} em {} anos'.format(cas, ano), end='')
print(' a prestação será de R${:.2f}'.format(prest))
