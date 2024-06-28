# A biblioteca math em Python fornece funções matemáticas definidas pelo padrão C.
# Ela inclui operações matemáticas básicas e funções avançadas para cálculos matemáticos.

# Importar a lib Math

import math

# --------------------Funções Básicas -------------------

# 1 - Arredondamento e Valores Absolutos

# math.ceil(x): Arredonda x para cima para o inteiro mais próximo.
print(math.ceil(4.3))   # 5

# math.floor(x): Arredonda x para baixo para o inteiro mais próximo.
print(math.floor(4.7))  # 4

# math.trunc(x): Trunca x, removendo a parte decimal.
print(math.trunc(4.7))  # 4

# math.fabs(x): Retorna o valor absoluto de x
print(math.fabs(-4.7))  # 4.7

# 2 - Potências e Logaritmos

# math.pow(x, y): Retorna x elevado à potência y.
print(math.pow(2, 3))    # 8.0

# math.sqrt(x): Retorna a raiz quadrada de x.
print(math.sqrt(16))     # 4.0

# math.log(x, base): Retorna o logaritmo de x na base especificada (base 10 por padrão).
print(math.log(100, 10)) # 2.0

# 3 - Constantes

# math.pi: O valor de pi (π).
print(math.pi)  # 3.141592653589793

# math.e: A base dos logaritmos naturais (e).
print(math.e)   # 2.718281828459045

# --------------------Funções Trigonométricas -------------------

#  1- Seno, Cosseno e Tangente

# math.sin(x): Retorna o seno de x (em radianos).
print(math.sin(math.pi/2))  # 1.0

# math.cos(x): Retorna o cosseno de x (em radianos).
print(math.cos(math.pi))    # -1.0

# math.tan(x): Retorna a tangente de x (em radianos).
print(math.tan(math.pi/4))  # 1.0

# 2 -Funções Inversas

# math.asin(x): Retorna o arco seno de x, em radianos.
print(math.asin(1))  # 1.5707963267948966 (π/2)

# math.acos(x): Retorna o arco cosseno de x, em radianos.
print(math.acos(1))  # 0.0

# math.atan(x): Retorna o arco tangente de x, em radianos.
print(math.atan(1))  # 0.7853981633974483 (π/4)

# 3 - Conversão entre Graus e Radianos

# math.degrees(x): Converte x de radianos para graus.
print(math.degrees(math.pi))  # 180.0

# math.radians(x): Converte x de graus para radianos.
print(math.radians(180))      # 3.141592653589793

# --------------------Funções Estatísticas -------------------

# 1 - Máximo e Mínimo

# math.fmax(x, y): Retorna o maior valor entre x e y.
print(max(2, 3))  # 3

# math.fmin(x, y): Retorna o menor valor entre x e y.
print(min(2, 3))  # 2

# 2 - Funções de Soma e Produto

# math.fsum(iterable): Retorna a soma de uma lista de números com precisão flutuante.
print(math.fsum([0.1, 0.1, 0.1]))  # 0.30000000000000004

# math.prod(iterable): Retorna o produto de uma lista de números.
print(math.prod([2, 3, 4]))        # 24

# ------------------------Outras Funções Úteis-----------------

# math.factorial(x): Retorna o fatorial de x.
print(math.factorial(5))   # 120

# math.isfinite(x): Retorna True se x é finito.
print(math.isfinite(4.5))  # True

# math.isinf(x): Retorna True se x é infinito.
print(math.isinf(math.inf))  # True

# math.isnan(x): Retorna True se x não é um número (NaN).
print(math.isnan(math.nan))  # True
