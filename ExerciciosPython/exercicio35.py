#35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#EX: Os tamanhos da reta devem ser proporcionais para isso, pesquisar sobre o princípio do triângulo.
#Para formar um triângulo, a soma de cada dois lados deve ser sempre maior que a medida do terceiro lado. Ou seja,
# considerando três segmentos de reta (a), (b) e (c), para construir um triângulo, devemos ter: (b + c > a).
print('~' * 25)
print('Analisando o  triângulo')
print('~' * 25)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um  triângulo')
else:
    print('Os segmentos acima não podem formar um  triângulo')
