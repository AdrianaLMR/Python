# # Laços de repetição são usados em programação para executar um bloco de código várias vezes.
# # Em Python, os dois principais laços de repetição são for e while.
#
# # 1. Laço for
# # O laço for é usado para iterar sobre uma sequência (como uma lista, tupla, string ou intervalo).
# # Aqui estão alguns exemplos de como usar o laço for:
#
# # Exemplo com range
# for i in range(5):  # Vai de 0 a 4
#     print(i)
#
# # Exemplo com lista
# frutas = ['maçã', 'banana', 'cereja']
# for fruta in frutas:
#     print(fruta)
#
# # Exemplo com string
# for letra in 'Python':
#     print(letra)
#
# # 2. Laço while
# # O laço while executa um bloco de código enquanto uma condição for verdadeira.
# # Aqui está um exemplo de como usar o laço while:
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#
# # Laços aninhados
# # Você pode aninhar laços dentro de outros laços para criar estruturas mais complexas. Aqui estão alguns exemplos de laços aninhados:
#
# # for dentro de for
# for i in range(3):
#     for j in range(2):
#         print(f'i = {i}, j = {j}')
#
# # while dentro de while
# i = 0
# while i < 3:
#     j = 0
#     while j < 2:
#         print(f'i = {i}, j = {j}')
#         j += 1
#     i += 1
#
# # for dentro de while
# i = 0
# while i < 3:
#     for j in range(2):
#         print(f'i = {i}, j = {j}')
#     i += 1
#
# # while dentro de for
# for i in range(3):
#     j = 0
#     while j < 2:
#         print(f'i = {i}, j = {j}')
#         j += 1
#
# # Uso de break e continue
# # Você pode usar break para sair de um laço e continue para pular para a próxima iteração.
#
# # Exemplo com break
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
#
# # Exemplo com continue
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
#
# # Exemplo aula, Lembre que o ùltimo ele ignora
# for c in range(0, 6):
#     print('OI')
# print('FIM')
#
# # Exemplo aula
#
# # (Estrutura de repetição com var de controlhe)
# #Contando para trás
#
# for d in range(6, 0, -1):
#     print(d)
# print('FIM!')
#
# #Pulando dois números
# for m in range(0, 8, 2):
#     print(m)
# print("Fim!")
#
# #Exeplo com input: Ex 1
# number = int(input('Digite um número: '))
# for numeros in range(0, number+1):
#     print(numeros)
# print('Fim')
#
# #Ex 2
# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for acao in range(i, f+1, p):
#     print(acao)
# print('Fim')
#
# #Exemplo com var dentro do blocoÇ Ex 1
# for valor in range(0, 3):
#     n = int(input('Digite um valor: '))
# print('Fim')
#
# #Ex 2
# s = 0
# for num in range(0, 4):
#     n = int(input('Digite um valor: '))
#     s += n
# print('O somatória de todos os valores foi {}'.format(s))

# Estrutura de repetição de teste lógico
#Ex 1
a = 1
while a < 10:
    print(a)
    a = a + 1 #a += 1
print('Fim')

#Ex 2
value = 1
while value != 0:
    value = int(input('Digite um valor: '))
print("Fim")

#Ex 3
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')

#Ex 4
k = 1
par = impar = 0
while k != 0:
    k = int(input('Digite um valor:'))
    if k != 0:
        if k % 2 == 0:
            par += 1
        else:
            impar += 1
print('Vocë digitou {} números pares e {} números impares!'.format(par, impar))


# Diferença entre Laços de repetição e condições aninhadas:

# Laços de repetição e condições aninhadas são dois conceitos diferentes na programação.

# Laços de repetição, como for e while, são usados para executar um bloco de código várias vezes.
# Por exemplo, o laço for é útil para iterar sobre uma sequência, como uma lista ou intervalo de números,
# enquanto o laço while continua a execução enquanto uma condição for verdadeira. A principal característica
# dos laços de repetição é a repetição de ações até que uma condição específica seja satisfeita, facilitando
# a execução repetitiva de tarefas.

# Condições aninhadas, por outro lado, referem-se ao uso de estruturas condicionais if, elif e else dentro
# de outras estruturas condicionais. Isso permite a verificação de múltiplas condições de forma hierárquica
# e a execução de diferentes blocos de código com base nos resultados dessas condições. A principal
# característica das condições aninhadas é a tomada de decisões baseadas em múltiplas verificações,
# permitindo um controle mais granular do fluxo do programa.

# Em resumo, laços de repetição são usados para repetir ações várias vezes, enquanto condições aninhadas são
# usadas para tomar decisões complexas com base em múltiplas condições. Ambos são essenciais para criar
# programas eficientes e funcionais, mas servem a propósitos distintos dentro do fluxo de controle da
# programação.
