# 43 desenvolva uma lógica que leia o peso e altura de um apessoa, calcule seu IMC e mostre seu status, de acordo
# com a tabela abaixo:
# - Abaixo  de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até  30 : Sobrepeso
# - 30 até  40: Obesidade
# - Acima de 40: Obesidade mórbita

# Leitura do peso e altura
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibindo o IMC
print('Seu IMC é: {:.1f}'.format(imc))

# Determinação do status de acordo com o IMC
if imc < 18.5:
    print('Status: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Status: Peso ideal')
elif 25 <= imc < 30:
    print('Status: Sobrepeso')
elif 30 <= imc < 40:
    print('Status: Obesidade')
else:
    print('Status: Obesidade mórbida')


