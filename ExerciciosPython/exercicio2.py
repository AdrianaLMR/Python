print('Programa que lê o nome do usuário e mostre uma mensgem com o valor recebido')
name = input('Qual o seu nome?')

print('Seja bem vindo!', name)

print('Saída formatada, bloco substituído pela formatação ({}) ')
print('Seja bem vindo {}!'.format(name))

print('Script de input, que pede um valor ao usuário')
nome = input('Qual o eu nome?')
idade = input('Qual a sua idade?')
peso = input('Qual o seu peso?')
print(nome, idade, peso)

print('Script utilizando valor recebido e retornando uma mensagem')
dia = input('Qual o dia do seu nascimento')
mes = input('Qual o mes do seu nascimento')
ano = input('Qual o ano do seu nascimento')
print('Você', nome, 'nasceu no dia ', dia, '/', mes, '/', ano,)