# 39 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -se ele ainda vai se alistar ao serviço militar.
# -se é a hora de se alistar.
# -se já pasou do tempo do alistamento.
#O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
# Ano atual
ano_atual = date.today().year

# Leitura do ano de nascimento
ano_nascimento = int(input('Digite o ano de nascimento: '))

# Cálculo da idade
idade = ano_atual - ano_nascimento

# Verificação da situação do alistamento
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar.')
    print('Faltam {} anos para o alistamento.'.format(18 - idade))
elif idade == 18:
    print('É a hora de se alistar ao serviço militar.')
else:
    print('Já passou do tempo de alistamento.')
    print('Você deveria ter se alistado há {} anos.'.format(idade - 18))

#Exemplo aula
from datetime import date
# Ano atual
atual = date.today().year

# Leitura do ano de nascimento
nasc = int(input('Digite o ano de nascimento: '))

# Cálculo da idade
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

# Verificação da situação do alistamento
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

