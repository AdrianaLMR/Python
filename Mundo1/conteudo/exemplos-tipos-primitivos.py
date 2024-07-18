print('Tipos primitivos')

print('Exemplo de concatenação: os valores numéricos são tratados como texto e unidos, não somados:')
a = input('Digite o primeiro valor:')
b = input('Digite o segundo valor:')

resultado = a + b
print(resultado)

print('Somando dois valores recebidos com tipo primitivo int')
n1 = int(input('Digite o valor de n1:'))
n2 = int(input('Digite o valor de n2:'))
soma = n1 + n2
print('a soma de n1 e n2 é: {}'.format(soma))

print('Somando dois números entre si')
x = 10
z = 20
print(x + z)

print('Somando uma var com um número')
r = 10
print(r + 10)

print('Somando dois valores recebidos com tipo primitivo float')
pi = float(input('qual o valor de pi?'))
print(pi)

n = float(input('Digite um valor:'))
print(n)

print('Somando dois valores recebidos com tipo primitivo bool(True se houver valor/ False se não  houver valor')
p = bool(input('Digite um valor: '))
print(type(p), p)

print('Somando dois valores recebidos com tipo primitivo string')
text = 'Texto'
textNumber = '2.0'
textVazio = ''
print('Valores de string {}', text, textNumber, textVazio)
palavra = str(input('Digite uma palavra: '))
print(type(palavra), palavra)


