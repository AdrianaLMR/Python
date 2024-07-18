# 24 Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

#Considerando qualquer string com o significado santo e em qualquer posicao

cid = str(input('Digite o nome de uma cidade: ')).lower().split()
print('Tem santo no nome da cidade: {}'.format('santo' in cid))

