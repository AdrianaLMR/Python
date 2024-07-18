# 27 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza primeiro = Ana último = Souza

nome_completo = str(input('Digite seu nome completo: ')).strip().split()
print(nome_completo)
primeiro_nome = nome_completo[0]
segundo_nome = nome_completo[-1]
print('Primeiro nome: {}'.format(primeiro_nome))
print('Último nome: {}'.format(segundo_nome))

#outra forma de resolução
nome = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome) - 1]))
