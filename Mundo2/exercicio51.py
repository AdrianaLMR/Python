# 51 Desenvolva um programa que leia o primeiro termo e a razão de um Progressão Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

# Lê o primeiro termo e a razão da Progressão Aritmética
primeiro_termo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))

# Calcula e exibe os 10 primeiros termos da PA
print("Os 10 primeiros termos da Progressão Aritmética são:")
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    print(termo_atual)
