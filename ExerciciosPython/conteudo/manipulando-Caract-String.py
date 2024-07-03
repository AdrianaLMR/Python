# Uma cadeia de caracteres,conhecida como string, é uma sequência de caracteres delimitada por aspas simples (')
# ou duplas ("). Strings são utilizadas para representar texto em um programa.

# Criação de strings com aspas simples ou duplas
string1 = 'Olá, mundo!'
string2 = "Olá, mundo!"

# String multilinha estendem por várias linhas, pode-se usar aspas triplas
string_multilinha = """ Está é uma string que ocupa várias linhas"""

# Acessando Caracteres através da  posição (índice), começando do zero.
string = 'Python'
print(string[0])
print(string[1])

# Fatiamento de strings. Pode-se obter uma subsequência de caracteres (substring) usando a notação de fatiamento.
text = 'Frase'
print(string[1:4])

# Imutabilidade/ Strings em Python são imutáveis, o que significa que uma vez criada, seus caracteres não podem ser alterados diretamente.
strings = 'Palavras'
print(string.strip())
print(string.upper())
print(string.lower())

# Concatenação de strings. Pode-se inserir valores em strings utilizando a formatação com format() ou f-strings.
nome = 'Maria'
idade = 25
print('Nome: {}, Idade: {}'.format(nome, idade))
print(f'Nome: {nome}, Idade{idade}')
