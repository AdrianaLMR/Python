# 31 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
#R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
#Metros para quilômetros:

# km = metros ÷ 1000 km = metros ÷ 1000 conversao para km
distancia = float(input('Digite a distância da viagem em Km: '))

# Verifica se a distância é menor ou igual a 200 km
if distancia <= 200:
    valor_passagem = distancia * 0.50
# Verifica se a distância é maior que 200 km
else:
    valor_passagem = distancia * 0.45
print('O valor da passagem será de R${:.2f}'.format(valor_passagem))


#Outra forma de resolução
dist = float(input('Digite a distância da viagem em Km: '))
valor_pass = dist * 0.50 if dist <= 200 else dist * 0.45
print('O valor da passagem será de R${:.2f}'.format(valor_pass))
