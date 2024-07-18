# Uma cadeia de caracteres,conhecida como string, é uma sequência de caracteres delimitada por aspas simples (')
# ou duplas ("). Strings são utilizadas para representar texto em um programa.

# Criação de strings com aspas simples ou duplas
string1 = 'Olá, mundo!'
print(string1)
string2 = "Hello, world!"
print(string2)

# String multilinha estendem por várias linhas, pode-se usar aspas triplas
string_multilinha = """Está é uma string que ocupa várias linhas"""
print(string_multilinha)

# Acessando Caracteres através da  posição (índice), começando do zero.
print('acessando caracter pelo indice')
string = 'indice '
print(string[2])
print(string[1])

# Fatiamento de strings. Pode-se obter uma subsequência de caracteres (substring) usando a notação de fatiamento.
print('Fatiamento')
text = 'Paralelepípedo'
print(text[3])
print(text[1:4])
print(text[:5])
print(text[7:])
print(text[0::3])
print(text[0:13:2])


# Imutabilidade/ Strings em Python são imutáveis, o que significa que uma vez criada, seus caracteres não podem ser alterados diretamente.
print('Imutabilidade')
strings = 'Palavras'
print(strings.strip())
print(strings.upper())
print(strings.lower())

# Concatenação de strings. Pode-se inserir valores em strings utilizando a formatação com format() ou f-strings.
print('Concatenação')
nome = 'Maria'
idade = 25
print('Nome: {}, Idade: {}'.format(nome, idade))
print(f'Nome: {nome}, Idade{idade}')

# Análisar

#A função len() em Python, quando aplicada a uma cadeia de caracteres (string), retorna o número de caracteres presentes
# na string. Isso inclui letras, números, espaços, sinais de pontuação e quaisquer outros caracteres.
texto = "Olá, mundo!"
comprimento_texto = len(texto)
print('Comprimento do texto: {}'.format(comprimento_texto))

# Função count método utilizado para contar o número de ocorrências de um valor específico em uma sequência, como uma string,
# lista ou tupla.
frase = 'Estou aprendendo python'
contador = frase.count('o')
print('Existe {} letras "O" na frase {}'.format(contador, frase))

carta = "Olá, mundo! Olá, universo!"
contagem = texto.count("Olá", 0, 12)
print('Número de vezes que "Olá" aparece nos primeiros 12 caracteres: {}'.format(contagem))

# A função find é um método usado para localizar a primeira ocorrência de uma substring dentro de uma string.
# Ela retorna o índice da primeira posição onde a substring é encontrada. Se a substring não for encontrada, o método
# retorna -1.

paragrafo = "Eu amo gatos"
indice = paragrafo.find("gat")
print('Índice da primeira ocorrência de "gat": {}'.format(indice))

# Operador "IN" é usado para verificar se um valor está presente em uma sequência, como uma string, lista, tupla,
# conjunto ou dicionário. Ele retorna um valor booleano True se o valor estiver presente e False caso contrário.
# A forma inversa, o operador not in, verifica se o valor não está presente na sequência.

comida = "Gosto de bolo de chocolate"
resultado = "quente" in comida
print(resultado)

bebida = "Gosto de coca-cola"
resposta = "Suco" in bebida
print(resposta)

# Transformação , geralmente se referem a operações que modificam a forma ou o conteúdo da string original.

# Python é usado para substituir todas as ocorrências de uma substring por outra dentro de uma string.
# Ele retorna uma nova string onde todas as ocorrências da substring especificada são substituídas pela nova substring
# fornecida como argumento.

frases = "Chocolate quente"
frases = frases.replace("Chocolate", "Cachorro")

#Concatenação
text1 = "Bom"
text2 = "Dia"
result = text1 + " " + text2
print(result)

#Substituição
text3 = "Boa, Noite!"
novo_texto = text3.replace("Noite", "Tarde")
print(novo_texto)

# Separação e Junção: Divide uma string em substrings com base em um separador e junta substrings em uma única string.
text5 = "Olá mundo Python"
palavras1 = text5.split()
print(palavras1)

palavras_juntas = "-".join(palavras1)
print(palavras_juntas)

#Formatação: Formata uma string com valores inseridos em posições específicas.
name = "Maria"
peso = 30.50
mensagem = "Olá, meu nome é {} e peso {:.1f} Kilos.".format(name, peso)
print(mensagem)

