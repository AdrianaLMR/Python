# #44 Elabore um programa que calcule o valor a ser pago por um produto, considerando
# # o seu preço normal e condição de pagamento:
# # - A vista dinheiro/cheque: 10% de desconto
# # - A vista cartão: 5% de desconto
# # - Em até 2x no cartão: Preço normal
# # - Em até 3x ou mais no cartão: 20% juros
#
# # Leitura do preço do produto
# valor = float(input('Digite o preço do produto: R$ '))
#
# # Definindo os descontos e juros como valores calculados
# desconto_din_che = valor * 0.10  # 10% de desconto para dinheiro/cheque
# desconto_cartao = valor * 0.05   # 5% de desconto para cartão
# juros_cartao = valor * 0.20      # 20% de juros para parcelamento em 3x ou mais
#
# # Exibindo as opções de pagamento
# print('Condições de pagamento:')
# print('[1] À vista dinheiro/cheque: 10% de desconto')
# print('[2] À vista cartão: 5% de desconto')
# print('[3] Em até 2x no cartão: Preço normal')
# print('[4] Em 3x ou mais no cartão: 20% de juros')
#
# # Leitura da opção de pagamento escolhida
# opcao = int(input('Escolha a condição de pagamento: '))
#
# # Inicialização da variável total com o valor original
# total = valor
#
# # Aplicação dos descontos ou juros conforme a opção escolhida
# if opcao == 1:
#     total -= desconto_din_che #-= é uma forma abreviada de escrever x = x - y.
# elif opcao == 2:
#     total -= desconto_cartao
# elif opcao == 3:
#     parcelas = 2
#     valor_parcela = total / parcelas
#     print('O produto será parcelado em {}x de R$ {:.2f} sem juros.'.format(parcelas, valor_parcela))
# elif opcao == 4:
#     total += juros_cartao
#     parcelas = int(input('Quantas parcelas? '))
#     valor_parcela = total / parcelas
#     print('O produto será parcelado em {}x de R$ {:.2f} com juros.'.format(parcelas, valor_parcela))
# else:
#     print('Opção inválida de pagamento. Considerando preço normal.')
#
# # Exibindo o valor total a ser pago
# print('O valor total a ser pago é: R$ {:.2f}'.format(total))

#EXEMPLO AULA

print('{: ^40}'.format(' LOJAS DRIKA '))
preco = float(input("Preço das compras: "))
print(''' Formas de pagamento:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')

option = int(input('Qual a opção? '))
if option == 1:
    total = preco - (preco * 10 / 100)
elif option == 2:
    total = preco - (preco * 5 / 100)
elif option == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif option == 4:
    total = preco + (preco * 20 / 100)
    tot_parc = int(input('Quantas parcelas'))
    parcela = total / tot_parc
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(tot_parc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))

