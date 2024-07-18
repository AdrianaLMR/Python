n = float(input('Digite um valor:'))
print(type(n), n)

print('Somando dois valores recebidos com tipo primitivo bool(True/ False')
p = bool(input('Digite um valor: '))
print(type(p), p)

# Verificando se um valor é numérico

valor = input('Digite algo:')
print(valor.isnumeric())

#Valores alfabeticos e alphanumericos
alpha = input('Digite algo: ')
print(alpha.isalpha())

alphaNumerico = input('Digite algo: ')
print(alphaNumerico.isalnum())

#verifica se está com letras maiúsculas
texto = input('escreva algo: ')
print(texto.isupper())
