# 50 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
# pares. Se o valor digitação for impar, desconsidere-o

# Inicializa a soma dos números pares
soma_pares = 0

# Loop para ler seis números inteiros
for i in range(6):
    # Lê um número inteiro
    numero = int(input("Digite um número inteiro: "))

    # Verifica se o número é par
    if numero % 2 == 0:
        # Adiciona o número à soma dos pares
        soma_pares += numero

# Exibe a soma dos números pares
print("A soma dos números pares é:", soma_pares)
