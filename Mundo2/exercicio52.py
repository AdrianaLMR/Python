# 52 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Lê um número inteiro do usuário

#Números Não Primos
# --> Números Compostos: São números que têm mais de dois divisores. Por exemplo, o número 6 é divisível
# por 1, 2, 3 e 6, portanto, não é primo.
# --> Números Menores que 2: O número 1 e todos os números menores que 1 não são considerados primos.

# Números Primos
# --> Definição: Um número é considerado primo se ele tem exatamente dois divisores positivos: 1 e ele mesmo.
# --> Exemplo: O número 7 é divisível apenas por 1 e 7. Portanto, 7 é um número primo.

numero = int(input("Digite um número inteiro: "))

# Verifica se o número é primo
if numero <= 1:
    print(f"O número {numero} não é primo.")
else:
    # Inicializa uma flag para verificar se o número é primo
    eh_primo = True

    # Verifica divisores até a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
