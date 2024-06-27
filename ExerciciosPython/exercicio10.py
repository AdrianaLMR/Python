#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# (U$$1.00 = R$3,27)
cambio = 3.27
carteira = float(input('Digite a quantia de dinheiro na sua carteira: '))

dolares = carteira / cambio

print('Você pode comprar U$${:.2f} '.format(dolares))
