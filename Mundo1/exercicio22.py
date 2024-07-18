# Crie um programa que leia o nome completo de uma pessoa e mostre:
nome_completo = str(input('Digite seu nome completo: ')).strip()

# a) o nome com todas as letras maiúsculas
maiusculo = nome_completo.upper()
print('Nome completo em minúsculo: {}'.format(maiusculo))
print('Nome completo em minúsculo: {}'.format(maiusculo.upper()))

# b) O nome com todas minúsculas
minusculo = nome_completo.lower()
print('Nome completo em minúsculo: {}'.format(minusculo))
print('Nome completo em minúsculo: {}'.format(minusculo.lower()))

# c) quantas letras ao todo(sem considerar espaços)
nome_sem_espacos = nome_completo.replace(" ", "")
comprimento = len(nome_sem_espacos)
print('Comprimento do nome: {}'.format(comprimento))

# Outra forma d eresolução
print('Comprimento do nome: {}'.format(len(nome_completo) - nome_completo.count(' ')))

# d) Quantas letras tem o primeiro nome
primeiro_nome = nome_completo.split()[0]
quant_let_prim_nome = len(primeiro_nome)
print("Quantidade de letras do primeiro nome: {}".format(quant_let_prim_nome))

# Outra forma de eresolução
print("Quantidade de letras do primeiro nome: {}".format(nome_completo.find(' ')))
separa = nome_completo.split()
print("Quantidade de letras do primeiro nome: {}".format(len(separa[0])))
