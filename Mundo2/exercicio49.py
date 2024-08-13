#49 Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço for.
numero = int(input('Digite um número para ver sua tabuada: '))

print('Tabuada de {}:'.format(numero))
for i in range(1, 11):
    print('{} x {:2} x {}'.format(numero, i, numero * i))

