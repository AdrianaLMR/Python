# LEMBRAR DE VERIFICAR O ESTILO CONFIGURAÇÃO PADRÃO ESCOLHIDA DO PAYCHARM OU EDITOR DE TEXTO
print('-' * 40)
print('Exercícios')
print('-' * 40)

RESET = "\033[0;0;0m"

# Teste 1: Back = vermelho e text = white
test1 = "\033[0;0;41m" #Exemplo de visualização da formatação completa(style,text,back)
print("{}Este é TESTE 1{}".format(test1, RESET))

# Teste 2: Style = sublinhado e text = amarelo e Back = ciano
test2 = "\33[4;33;44m"
print("{}Este é TESTE 2{}".format(test2, RESET))

# Teste 3: Back = amarelo e text = magenta
test3 = "\33[0;35;43m"
print("{}Este é TESTE 3{}".format(test3, RESET))

# Teste 4: Back = verde e text = white
test4 = "\33[42m"
print("{}Este é TESTE 4{}".format(test4, RESET))

# Teste 5: Back = preto e text = cinza
test5 = "\33[37;40m"
print("{}Este é TESTE 5{}".format(test5, RESET))

# Teste 6: Back = cinza e text = preto
test6 = "\33[30;47m"
print("{}Este é TESTE 6{}".format(test6, RESET))

print('\033[1;31;43m Olá mundo!\033[m')
print('\033[4;0;45m Olá mundo!\033[m')
print('\033[7;30;45m Olá mundo!\033[m') #Invertendo a cor de fundo com a cor do texto

print('-' * 40)
print('Exercícios: Colorindo var específicas')
print('-' * 40)

a = 3
b = 5
# Maneira de colorir apenas o valores específicos de um texto(Delimitar onde inícia e termina)
print('Oa valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
# Exemplo que mostra sem a delimitação(O 'e' fica colorido e afeta o próxima cor )
## print('Oa valores são \033[32m{} e \033[31m{}'.format(a, b)) #exclua o comentário para testar

nome = 'Fulano'
print('Olá! É um prazer te conhecer, {}{}{} !!'.format("\033[4;34m",  nome, "\033[m"))

# Criando cores no sistema(Dicionário)
print('-' * 40)
print('Criando cores no sistema')
print('-' * 40)
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'magenta': '\033[4;35m'
}
usuario = 'Siclano'
print('Olá! É um prazer te conhecer, {}{}{} !!'.format(cores['amarelo'], usuario, cores['limpa']))
print('Olá! É um prazer te conhecer, {}{}{} !!'.format(cores['azul'], usuario, cores['limpa']))
print('Olá! É um prazer te conhecer, {}{}{} !!'.format(cores['magenta'], usuario, cores['limpa']))
