# 32 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Ano bissextos são divisiveis por 4, exceto anos multiplos de 100 que não são multiplos de 400.

from datetime import date
ano = int(input('Qual ano quer analisar? Para o ano atual digite o número 0: '))

#Verifica o ano atual
if ano == 0:
    ano = date.today().year

# Verifica se o ano é bissexto/ Forma correta
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
