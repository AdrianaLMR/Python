# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

#1 metro = 100 centímetros
# 1 metro = 1000 milímetros
# 1 metro = 3,28084 pés
# 1 metro = 1,09361 jardas

metros = float(input('Digite um valor: '))

centimetros = metros * 100
milimetros = metros * 1000
pes = metros * 3.28084
jardas = metros * 1.09361

print('O valor em centímetros é: {:.2f} cm'.format(centimetros))
print('O valor em milímetros é: {:.2f} mm'.format(milimetros))
print('O valor em pés é: {:.5f} ft'.format(pes))
print('O valor em jardas é: {:.5f} yd'.format(jardas))

# desafio extra
quilometros = metros / 1000
hectometros = metros / 100
decametros = metros / 10
decimetros = metros * 10

print('O valor de quilômetros em metros é : {}'.format(quilometros))
print('O valor de hectômetros em metros é : {} '.format(hectometros))
print('O valor de decâmetros em metros é : {}'.format(decametros))
print('O valor de decímetros em metros é : {}'.format(decimetros))
