import math

num = int(input('Digite um número: '))

# Calcula a raiz quadrada do número
raiz = math.sqrt(num)

# Arredonda a raiz para cima e mostra o resultado
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

# Mostra a raiz com duas casas decimais
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Outra maneira é importar uma função da lib específica

from  math import floor

# Usando a função floor(x): Arredonda x para baixo para o inteiro mais próximo.

valor = 4.7
total = floor(valor)
print(total)  # 4

from  math import pi, floor

# Usando a função floor(x): Arredonda x para baixo para o inteiro mais próximo.

numero = int(input('Digite um número: '))
calculo = pi * numero
print('O resultado do calculo é {}'.format(floor(calculo)))
