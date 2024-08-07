#40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre de 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_um = float(input('Digite a primeira nota'))
nota_dois = float(input('Digite a segunda nota'))

media = (nota_um + nota_dois) / 2

if media < 5:
    print('Você foi REPROVADO!')
elif 5.0 <= media <= 6.9:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')


