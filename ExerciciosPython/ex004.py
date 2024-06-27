# Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre elas(metodos(is))

#!!! Espacos digitados no terminal alteram o resultado das questões exceto na pergunta de espacos

msg = input('Digite algo no seu teclado:')

print(msg)
print('Tipo primitivo do valor recebido pelo teclado: {}'.format(type(msg)))
print('O valor possui espaços? {}'.format(msg.isspace()))
print('O valor recebido é numérico? {}'.format(msg.isnumeric()))
print('O valor recebido é alfabético? {}'.format(msg.isalpha()))
print('O valor recebido é alfanumérico? {}'.format(msg.isalnum()))
print('O valor recebido está escrito em maiúsculo? {}'.format(msg.isupper()))
print('O valor recebido está escrito em minúsculo? {}'.format(msg.islower()))
print('O valor recebido é decimal? {}'.format(msg.isdecimal()))
print('O valor recebido são caracteres string ASCII? {}'.format(msg.isascii()))
print('O valor recebido é digito? {}'.format(msg.isdigit()))
print('Está capitalizada("Name")? {}'.format(msg.istitle()))


