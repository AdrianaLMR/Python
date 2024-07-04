# 26 Faça um programa que leia uma frase pelo teclado e mostre:
frase = (input('Digite uma frase: ')).upper().strip()

# a) Quantas veze a letra "A"
letra = frase.count('A')
print('A letra A aparece {} vezes na frase: {}'.format(letra, frase))

# b) Em que posição ela aparece a primeira vez
posicao = frase.find('A') + 1
print('A primeira vez que a letra A apreceu foi no ídice: {}'.format(posicao))

#c) Em que posição ela aparece a última vez
ultima_posicao = frase.rfind('A') + 1
print('A última vez que a letra "A" apareceu na frase foi na posição: {}'.format(ultima_posicao, frase))

