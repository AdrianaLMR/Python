#37 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão: 1 = binário, 2 = octal, 3 = hexadecimal

#Para tirar o prefixos usar --> ([2:])
numero = int(input('Digite um número:  '))

#Conversões
binario = bin(numero)[2:]
hexadecimal = hex(numero)[2:]
octal = oct(numero)[2:]

print('--' * 10)
conversao = int(input('Escolha uma das bases paraa conversão do número: [1] binário, [2] octal, [3] hexadecimal \n Digite a bse de conversão escolhida: '))
print('--' * 10)
if conversao == 1:
    print("O número {} convertido em binário é {}".format(numero, binario))
elif conversao == 2:
    print("O número {} convertido em octal é {}".format(numero, octal))
elif conversao == 3:
    print("O número {} convertido em hexadecimal é {}".format(numero, hexadecimal))
else:
    print('Digite uma opção válida')


#Exemplo aula
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases paraa conversão do número: [1] binário, [2] octal, [3] hexadecimal ')

opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print("O número {} convertido em binário é {}".format(num, bin(num)))
elif opcao == 2:
    print("O número {} convertido em octal é {}".format(num, oct(num)))
elif opcao == 3:
    print("O número {} convertido em hexadecimal é {}".format(num, hex(num)))
else:
    print('Digite uma opção válida')
