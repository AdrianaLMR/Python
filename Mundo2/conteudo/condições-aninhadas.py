# Em Python, estruturas de repetição com condições alinhadas são usadas para executar um bloco de código várias
# vezes enquanto uma condição for verdadeira. Aqui estão alguns exemplos de como você pode usar essas estruturas:

# 1. while com condições alinhadas
# A estrutura while continua a executar um bloco de código enquanto uma condição for verdadeira. Você pode aninhar condições dentro desse bloco usando if, elif e else.

x = 0
while x < 10:
    if x % 2 == 0:
        print(f"{x} é par")
    else:
        print(f"{x} é ímpar")
    x += 1

# 2. for com condições alinhadas
# A estrutura for é usada para iterar sobre uma sequência (como uma lista, tupla ou string). Dentro do bloco for, você pode usar if, elif e else para criar condições alinhadas.

for z in range(10):
    if z % 2 == 0:
        print(f"{z} é par")
    else:
        print(f"{z} é ímpar")

# 3. while aninhado
# Você pode aninhar um while dentro de outro while para criar condições mais complexas.

a = 0
while a < 5:
    b = 0
    while b < 3:
        print(f"a = {a}, b = {b}")
        b += 1
    a += 1

# 4. for aninhado
# Da mesma forma, você pode aninhar um for dentro de outro for.

for c in range(5):
    for d in range(3):
        print(f"c = {c}, d = {d}")

# 5. for com while aninhado
# Você também pode combinar for e while dentro de uma estrutura de repetição.

for e in range(5):
    f = 0
    while f < 3:
        print(f"e = {e}, f = {f}")
        f += 1

# 6. while com for aninhado
# E o contrário também é válido.

g = 0
while g < 5:
    for h in range(3):
        print(f"g = {g}, h = {h}")
    g += 1

nome = str(input('Digite seu nome: '))
if nome == 'Adriana':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Maria' or nome == 'Manuela':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem comum no Brasil')
print('tenha um bom dia, {}'.format(nome))
