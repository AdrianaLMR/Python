# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# (U$$1.00 = R$3,27)

real = float(input('Digite a quantia de dinheiro na sua carteira: R$ '))

dolares = real / 3.27

print('Você pode comprar U$${:.2f} com R${:.2f}'.format(dolares, real))


# Com variavel
dinheiro = float(input('Digite a quantia de dinheiro na sua carteira: R$ '))
cambio = 3.27
dolar = dinheiro / cambio

print('Você pode comprar U$${:.2f} com R${:.2f}'.format(dolar, dinheiro))

# Valor dolar atualizado 2024

# Para o dolar
r = float(input('Digite a quantia de dinheiro na sua carteira: R$ '))
d = 5.57

conversao = r / d
print('Você pode comprar U$${:.2f} com R${:.2f}'.format(d, r))

# Para o Euro
r = float(input('Digite a quantia de dinheiro na sua carteira em R$: '))
euro_rate = 6.50

conversao_euro = r / euro_rate
print('Você pode comprar {:.2f} Euros com R${:.2f}'.format(conversao_euro, r))

# Para o Bitcoin
bitcoin_rate = 300000

conversao_bitcoin = r / bitcoin_rate
print('Você pode comprar {:.8f} Bitcoins com R${:.2f}'.format(conversao_bitcoin, r))