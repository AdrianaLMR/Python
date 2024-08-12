# 42 Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos lados diferentes

#Desafio 35 (#35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#EX: Os tamanhos da reta devem ser proporcionais para isso, pesquisar sobre o princípio do triângulo.
#Para formar um triângulo, a soma de cada dois lados deve ser sempre maior que a medida do terceiro lado. Ou seja,
# considerando três segmentos de reta (a), (b) e (c), para construir um triângulo, devemos ter: (b + c > a).


print('~' * 25)
print('Analisando o Triângulo')
print('~' * 25)

# Leitura dos segmentos de reta
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

# Verificação se podem formar um triângulo
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo.')
    # Verificação do tipo de triângulo
    if reta1 == reta2 == reta3:
        print('Triângulo Equilátero: todos os lados iguais.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Triângulo Isósceles: dois lados iguais.')
    else:
        print('Triângulo Escaleno: todos os lados diferentes.')
else:
    print('Os segmentos acima não podem formar um triângulo.')

#Exemplo aula
print('~' * 25)
print('Analisando o Triângulo')
print('~' * 25)

# Leitura dos segmentos de reta
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verificação se podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
    # Verificação do tipo de triângulo
    if r1 == r2 == r3:
        print('Triângulo Equilátero: todos os lados iguais.')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno: dois lados iguais.')
    else:
        print('Triângulo Isósceles:: todos os lados diferentes.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
