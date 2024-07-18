# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# Calcular a Porcentagem de um Valor:
# Para encontrar a porcentagem de um valor em relação a outro, você utiliza a fórmula:
# Porcentagem = (Parte / Total) × 100%
# Por exemplo, se você quer calcular 20% de 150:
# Porcentagem = (20 / 100) × 150 = 0.20 × 150 = 30


preco = float(input('Digite o preço do produto: '))
percentualDesconto = 5
desconto = (percentualDesconto / 100) * preco

total = preco - desconto
print('O valor total foi de: {:.2f} com 5% de desconto.'.format(total))

# Outra forma de resolução

preço = float(input('Digite o preço do produto: '))
novo = preço - (preço * 5 / 100)
print('o produto que custava {:.2f}, na promoção vai custar {:.2f}'.format(preço, novo))
