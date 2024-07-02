import emoji

#Exemplos documentação
# Usa o alias :thumbsup: para representar o emoji 👍. O parâmetro language='alias' define o uso de aliases em inglês.
print(emoji.emojize('Python is :thumbsup:', language='alias'))

# Similar ao anterior, mas sem especificar o idioma dos aliases, assume o padrão (inglês)
print(emoji.emojize('Python is :thumbsup:'))

# Converte o emoji 👍 de volta para o texto :thumbsup:
print(emoji.demojize('Python is 👍'))

# Converte :red_heart: para o emoji ❤️
print(emoji.emojize("Python is fun :red_heart:"))

# Usa o alias em português :polegar_para_cima: para representar o emoji 👍.
print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))

# Converte :red_heart: para o emoji ❤️ usando a variante emoji_type.
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))

# Converte o emoji 👍 para o texto :polegar_para_cima: em português
print(emoji.demojize("Python é 👍", language='pt'))

#Exemplos aula

# versão antiga, não utilizada atualmente
# print(emoji.emojize("olá mundo :earth_americas: !", use_aliases=True))

#Versãoatualizada do exemplo acima
print(emoji.emojize("olá mundo :earth_americas:!", language='alias'))

#19 Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# 20 O mesmo professor do desafio anterior(19) quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que elia o nome dos quatro alunos e mostre a ordem sorteada.

# 21 Faça um programa em python que abre e reproduza áudio de um arquivo MP3.