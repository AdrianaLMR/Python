# 41 A confederação Nacional de natação preciosa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria de acordo com a idade:
# - Até 9 anos : MIRIM
# - Até 14 anos : INFANTIL
# - Até 19 anos : JUNIOR
# - Até 25 anos : SÊNIOR
# - Acima: MASTER

from datetime import date

# Leitura do ano de nascimento
ano_nascimento = int(input('Digite o ano de nascimento: '))

# Ano atual
ano_atual = date.today().year

# Cálculo da idade
idade = ano_atual - ano_nascimento

# Verificação de categoria
if idade <= 9:
    print('Você está na categoia MIRIM')
elif idade <= 14:
    print('Você está na categoia INFANTIL')
elif idade <= 19:
    print('Você está na categoia JUNIOR')
elif idade <= 25:
    print('Você está na categoia SÊNIOR')
else:
    print('Você está na categoia MASTER')
