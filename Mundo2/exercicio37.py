#37 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão: 1 = binário, 2 = octal, 3 = hexadecimal

#Para tirar o prefixos usar --> ([2:])
numero = int(input('Digite um número:  '))

#Conversões
binario = bin(numero)[2:]
hexadecimal = hex(numero)[2:]
octal = oct(numero)[2:]

print('--' * 10)
conversao = int(input('Escolha uma das bases paraa conversão do número:  1 = binário, 2 = octal, 3 = hexadecimal '))
print('--' * 10)
if conversao == 1:
    print("O número {} convertido em binário é {}".format(numero, binario))
elif conversao == 2:
    print("O número {} convertido em octal é {}".format(numero, octal))
elif conversao == 3:
    print("O número {} convertido em hexadecimal é {}".format(numero, hexadecimal))
else:
    print('Digite um número válido')
