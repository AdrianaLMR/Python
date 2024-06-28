# Operadores Aritméticos
# Todos os operadores pecisam de operandos(int, var), os operdores são binários(precisa de dois operandos)
# utiliza-se  dois operdores == para saber o resultado pois um  = é considerado para a atribuição
#Adição(+), subtração(-), multiplicação(*), divião(/)
#Potenciação(**), diivisão inteira(//), resto da divisão(módulo(%))

numeroP = int(input('Digite o primeiro número: '))
numeroS = int(input('Digite o segundo número: '))
a = numeroP + numeroS
b = numeroP - numeroS
c = numeroP * numeroS
d = numeroP / numeroS
e = numeroP ** numeroS  #(Função interna - > pow(5, 2), perde a ordem de resolução)
f = numeroP // numeroS
g = numeroP % numeroS
print('A soma é {}, a subtração é {} o produto é {} e a divisão é {:.3f} '.format(a, b, c, d), end='') #Evita a quebra de linha end= ''
print('A potência {}, divisão inteira é {} e o \n resto é {}'.format(e, f, g)) #Quebra a linha \n

#Ordem de procedência(resolução)

# 1 -> ()
# 2 -> **
# 3 -> *, /, %, //
# 4 -> +, - (binários)

#Quando usar var
#Quando usamos var é porque precisaos dessa variavel posteriormente, caso contrario faça como o código abaixo:
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma vale {}'.format(n1 + n2))

#Ao utilizar string com operadores o valor da string é repetido pelo valor operado/ não são operadores Aritméticos

print('oi' * 2)
print('oi ' + 'mundo')

nome = input('Qual o seu nome?')
print('Seja bem vindo {}!'.format(nome))
print('Seja bem vindo {:10}!'.format(nome)) #adiciona o espaco
print('Seja bem vindo {:<20}!'.format(nome)) #alina a esquerda
print('Seja bem vindo {:>30}!'.format(nome)) #alinha a direita
print('Seja bem vindo {:^10}!'.format(nome)) #centraliza
print('Seja bem vindo {:^10}!'.format(nome))  # Centraliza e preenche com o caracter padrão (espaço)