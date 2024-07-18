# ANSI  (American National Standards Institute)

# O padrão ANSI é um conjunto de especificações que define uma maneira de exibir texto colorido e formatado em terminais
# de texto. Essas especificações são amplamente utilizadas em terminais de sistemas operacionais baseados em Unix, como
# Linux e macOS, além de alguns terminais do Windows.
#
# Sequências de Escape ANSI

# As sequências de escape ANSI são cadeias de caracteres que controlam a formatação do texto, como cor, estilo e posição
# do cursor. Essas sequências começam com o caractere de escape \033 seguido de um ou mais códigos que definem o estilo
# desejado. "\033[style; color_text; back m"
#  Normalmente, em Python, as variáveis em maiúsculas são usadas para constantes. No entanto, no contexto de sequências
# de escape ANSI, é comum usar letras maiúsculas para facilitar a leitura e diferenciar os códigos de controle
# do texto principal.

# Código de style(melhor compatibilidade com o terminal)
# 0 = sem estilo, none
# 1 = bold, negrito
# 4 = unerline, sublinhar
# 7 = negative, inverte as configurações(fundo vira letra e virse e versa)

# Código de text(melhor compatibilidade com o terminal), para adicionar mais precisa de lib externa
# 30 = Branco
# 31 = Vermelho
# 32 = Verde
# 33 = amarelo
# 34 = Azul
# 35 = Magenta
# 36 = Cíano
# 37 = Cinza

# Código de Background(melhor compatibilidade com o terminal), para adicionar mais precisa de lib externa
# 40 = Branco
# 41 = Vermelho
# 42 = Verde
# 43 = amarelo
# 44 = Azul
# 45 = Magenta
# 46 = Cíano
# 47 = Cinza

# Definindo cores em sequência de escape ANSI(Cores comuns)
print('<-------Definindo cores em sequência de escape ANSI------->')
# Códigos de cor
PRETO = "\033[30m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"
RESET = "\033[0m"  # Reseta a formatação

# Usando cores no texto
print("{}Este texto é vermelho{}".format(VERMELHO, RESET))
print("{}Este texto é verde{}".format(VERDE, RESET))
print("{}Este texto é azul{}".format(AZUL, RESET))

# Estilo de texto, como negrito, sublinhado e piscar
print('<-------Estilo texto------->')
# Códigos de estilo
NEGRITO = "\033[1m"
SUBLINHADO = "\033[4m"
PISCAR = "\033[5m"
RESET2 = "\033[0m"

# Usando estilos no texto
print("{}Este texto está em negrito{}".format(NEGRITO, RESET2))
print("{}Este texto está sublinhado{}".format(SUBLINHADO, RESET2))
print("{}Este texto está piscando{}".format(PISCAR, RESET2))

#Cores de fundo
print('<-------Cores de fundo------->')
# Códigos de cor de fundo
FUNDO_PRETO = "\033[40m"
FUNDO_VERMELHO = "\033[41m"
FUNDO_VERDE = "\033[42m"
FUNDO_AMARELO = "\033[43m"
FUNDO_AZUL = "\033[44m"
FUNDO_MAGENTA = "\033[45m"
FUNDO_CIANO = "\033[46m"
FUNDO_BRANCO = "\033[47m"
RESET3 = "\033[0m"

# Usando cores de fundo
print("{}{}Texto com fundo verde e texto preto{}".format(FUNDO_VERDE, PRETO, RESET3))
print("{}{}Texto com fundo azul e texto branco{}".format(FUNDO_AZUL, BRANCO, RESET3))

# Exemplo completo
print('<-------Exemplo completo------->')
# Definindo cores e estilos
COR_VERMELHO = "\033[31m"
COR_VERDE = "\033[32m"
COR_AZUL = "\033[34m"
ESTILO_NEGRITO = "\033[1m"
ESTILO_UBLINHADO = "\033[4m"
RESET4 = "\033[0m"

# Usando cores e estilos no texto
print("{}Texto vermelho{}".format(COR_VERMELHO, RESET4))
print("{}Texto verde{}".format(COR_VERDE, RESET4))
print("{}{}Texto azul e negrito{}".format(COR_AZUL, ESTILO_NEGRITO, RESET4))
print("{}Texto sublinhado{}".format(ESTILO_UBLINHADO, RESET4))

# Considerações
# --> Nem todos os terminais suportam todas as sequências de escape ANSI.

# --> Alguns terminais podem precisar de configurações adicionais para suportar cores e estilos.

# --> Em alguns ambientes (como scripts executados em segundo plano), as sequências de escape podem
# não funcionar corretamente.

# --> As sequências de escape ANSI são uma maneira poderosa e flexível de adicionar formatação ao texto no terminal,
# tornando a saída mais legível e visualmente atraente.
