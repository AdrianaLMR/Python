# Solicita ao usuário que digite sua idade
idade = int(input('Digite sua idade: '))

# Verifica se a idade é maior ou igual a 18 anos
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

# Verificando a média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
print('Sua média é igual a: {:.2f} e '.format(media))
if media >= 6:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')

# Forma simplificada de verificar a média
print('Parabéns!' if media >= 6 else 'Estude mais!')

