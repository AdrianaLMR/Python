# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro da tinta, pinta uma área de 2 metros^2

largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
areaParede = largura * altura
litrosTinta = areaParede / 2

print('Para pintar a parede é necessário de {} litros de tinta. '.format(litrosTinta))

largura = 2
altura = 2

area_parede = largura * altura
litros_tinta = area_parede / 2
print('Para pintar a parede é necessário de {} litros de tinta. '.format(litros_tinta))
