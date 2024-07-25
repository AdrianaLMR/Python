# 48 Crie um programa que calcule a soma entre todos os números impares que são multiplos de três
# e que se encontram no intervalo de 1 até 500.

# Inicializa a soma
soma = 0

# Loop para percorrer todos os números de 1 a 500
for numero in range(1, 501):
    # Verifica se o número é ímpar e múltiplo de 3
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

# Exibe o resultado
print('A soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500 é: {}'.format(soma))

