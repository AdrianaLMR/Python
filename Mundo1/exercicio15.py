# escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a
# quantidade de dias que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM

km = float(input('Digite quantos KM percorreu com o carro alugado: KM '))
dias = float(input('Digite quantos dias você alugou o carro: '))
preco = (dias * 60) + (0.15 * km)
print('O total a pagar pelo carro alugado é: R${:.2f}'.format(preco))
