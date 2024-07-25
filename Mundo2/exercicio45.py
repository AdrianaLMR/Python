# 45 crie um programa que faça o computador jogar Jokempô com você

import random

# Opções disponíveis para o jogo
opcoes = ['pedra', 'papel', 'tesoura']

# Exibe opções para o jogador
print('Escolha uma opção:')
print('1. Pedra')
print('2. Papel')
print('3. Tesoura')

# Leitura da escolha do jogador
escolha_jogador = int(input('Digite o número da sua escolha: '))

# Mapeia a escolha do jogador para texto
if escolha_jogador == 1:
    escolha_jogador = 'pedra'
elif escolha_jogador == 2:
    escolha_jogador = 'papel'
elif escolha_jogador == 3:
    escolha_jogador = 'tesoura'
else:
    print('Escolha inválida. Tente novamente.')
    exit()  # Sai do programa se a escolha for inválida

# Escolha aleatória do computador
escolha_computador = random.choice(opcoes)

# Exibição das escolhas
print('Você escolheu: {}'.format(escolha_jogador))
print('O computador escolheu: {}'.format(escolha_computador))

# Determinação do vencedor
if escolha_jogador == escolha_computador:
    resultado = 'Empate!'
elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
     (escolha_jogador == 'tesoura' and escolha_computador == 'papel') or \
     (escolha_jogador == 'papel' and escolha_computador == 'pedra'):
    resultado = 'Você ganhou!'
else:
    resultado = 'Você perdeu!'

# Exibição do resultado
print(resultado)
