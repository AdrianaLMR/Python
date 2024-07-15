# LEMBRAR DE VERIFICAR O ESTILO CONFIGURAÇÃO PADRÃO ESCOLHIDA DO PAYCHARM OU EDITOR DE TEXTO

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

