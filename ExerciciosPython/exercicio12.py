# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
percentualDesconto = 5
desconto = (percentualDesconto / 100) * preco

total = preco - desconto
print('O valor total foi de: {} com 5% de desconto.'.format(total))

