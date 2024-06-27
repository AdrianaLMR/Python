# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

#1 metro = 100 centímetros
# 1 metro = 1000 milímetros
# 1 metro ≈ 3,28084 pés
# 1 metro ≈ 1,09361 jardas

metros = float(input('Digite um valor: '))

centimetros = metros * 100
milimetros = metros * 1000
pes = metros * 3.28084
jardas = metros * 1.09361

print('O valor em centímetros é: {:.2f} cm'.format(centimetros))
print('O valor em milímetros é: {:.2f} mm'.format(milimetros))
print('O valor em pés é: {:.5f} ft'.format(pes))
print('O valor em jardas é: {:.5f} yd'.format(jardas))


