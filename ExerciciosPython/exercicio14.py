# escreva um programa que converta uma temperatura digitada em Celcius para Fahrenheit
# 1 C = 33.8 F ((1 °C × 9/5) + 32 = 33,8 °F)

c = float(input('Digite a temperatura em Celsius: '))
f = (9/5) * c + 32
print('A temperatura em Celcius {} convertida em Fahrenheit é {}:'.format(c, f))

# Outra forma de resolução

celcius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = ((9 * celcius) / 5) + 32
print('A temperatura em Celcius {} convertida em Fahrenheit é {}:'.format(celcius, fahrenheit))
