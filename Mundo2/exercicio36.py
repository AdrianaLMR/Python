# 36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador  e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
# empréstimo será negado.

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos_pagamento = float(input('Digite quantos anos pretende pagar o valor da casa: '))

#Calcula o valor da prestaçaõ mensal
meses_pagamento = anos_pagamento * 12 #converte anos em meses
prestacao = salario / 30 #divide o valor da casa pelo número de meses de pagamento.

# Verificase a prestaçaõ mensal é maior que 30% do salário
limite = salario * 0.3

print('\nAnalisando o empréstimo...')
if prestacao <= limite:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
