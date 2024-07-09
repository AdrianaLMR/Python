# 29 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limite

velocidade = float(input('Digite a velocidade do carro: '))
print('velocidade do carro: {} Km/h'.format(velocidade))

excesso_velocidade = velocidade - 80

# verifica velocidade == 80
if excesso_velocidade > 0:
    multa = excesso_velocidade * 7
    print('você recebeu uma multa de R${}'.format(multa))
print('tenha uma bom dia! Dirija com segurança.')

# Outra forma de resolução
velocid = float(input('Digite a velocidade do carro: '))
print('velocidade do carro: {} Km/h'.format(velocid))

# verifica velocidade == 80
if velocid > 80:
    multa = (velocid - 80) * 7
    print('você recebeu uma multa de R${:.2f}'.format(multa))
print('tenha uma bom dia! Dirija com segurança.')
