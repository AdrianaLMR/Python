# Estruturas condicionais são fundamentais em qualquer linguagem de programação, incluindo Python.
# Elas permitem que o programa tome decisões com base em determinadas condições. Em Python, as estruturas condicionais mais
# comuns são if, elif e else.

# O if é usado para executar um bloco de código verdadeiro.
# Exemplo:

nome = str(input('Digite seu nome'))
if nome == 'Adriana':
    print('Bem vindo, {}!'.format(nome))


#Estrutura elif
#A estrutura elif (abreviação de "else if") permite verificar múltiplas condições.
# Se a condição if for falsa, a condição elif é verificada.
x = 10
if x > 15:
    print("x é maior que 15")
elif x > 5:
    print("x é maior que 5, mas menor ou igual a 15")

#Estrutura else
# A estrutura else é usada para executar um bloco de código se todas as condições anteriores (if e elif) forem falsas.
z = 3
if z > 5:
    print("z é maior que 5")
elif z > 2:
    print("z é maior que 2, mas menor ou igual a 5")
else:
    print("z é menor ou igual a 2")

#Condições Aninhadas
# Pode aninhar estruturas condicionais dentro de outras para criar lógica mais complexa.

a = 10
b = 5
if a > 5:
    if b > 3:
        print("'A' é maior que 5 e 'B' é maior que 3")
    else:
        print("'A' é maior que 5 e 'B' é menor ou igual a 3")
else:
    print("'A' é menor ou igual a 5")

