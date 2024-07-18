# 34 Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. para salários superiores
#R$1.250.00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250:
   novo_sal = salario + (salario * 15 / 100)
else:
    novo_sal = salario + (salario * 10 / 100)
print('Quem ganhava RS{:.2f} passa a receber agora {:.2f}'.format(salario, novo_sal))

