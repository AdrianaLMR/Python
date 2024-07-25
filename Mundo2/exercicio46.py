# 46 Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 sgundos entre elas

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print('O estouro dos fogos artifício começou!!')
