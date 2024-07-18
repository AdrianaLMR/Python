# Uma tupla em Python é uma estrutura de dados que pode conter múltiplos itens, como uma lista, mas com a diferença
# de que as tuplas são imutáveis. Isso significa que, uma vez criada, uma tupla não pode ser alterada
# (não é possível adicionar, remover ou modificar.
# Isso as torna úteis para armazenar dados que não devem ser modificados.os itens)

# Tuplas são definidas usando parênteses () e os itens são separados por vírgulas
minha_tupla = (1, 2, 3)
print(minha_tupla)

# Os itens de uma tupla podem ser acessados por meio de índices, começando do zero.
acesso_tupla = (1, 2, 3)
print(acesso_tupla[0])  # Saída: 1

# Tuplas podem conter outras tuplas como itens, permitindo estruturas aninhadas.
tupla_aninhada = (1, (2, 3), (4, 5))

# Pode-se realizar operações como concatenação e repetição usando operadores + e *.
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Saída: (1, 2, 3, 4)

tupla_repetida = tupla1 * 3
print(tupla_repetida)  # Saída: (1, 2, 1, 2, 1, 2)

# Pode-se desempacotar os itens de uma tupla em variáveis individuais.
tupla = (1, 2, 3)
a, b, c = tupla
print(a)  # Saída: 1
print(b)  # Saída: 2
print(c)  # Saída: 3




