# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro da tinta, pinta uma área de 2 metros^2

larg = float(input('Insira a largura da parede: '))
alt = float(input('Insira a altura da parede: '))
area = larg * alt
litros = area / 2

print('Para pintar a parede de {:.2f}m² ({}x{}) é necessário {:.2f} litros de tinta'.format(larg * alt, larg, alt, litros))

# Com var
largura = 2
altura = 2

area_parede = largura * altura
litros_tinta = area_parede / 2
print('Para pintar a parede de {:.2f}m² ({}x{}) é necessário {} litros de tinta. '.format(area_parede, largura, altura,litros_tinta))
