#Desafio 34: Aumento de salário
print('^^^'* 15)
print('Desafio 34: Aumento de salário')
print('^^^'* 15)
print()
#Entrada de dados
salario = float(input('Digite seu salário: R$ \n'))
#Calculo aumento de salário
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
#Calculo novo salário
novo = salario + aumento
#Resultado
print()
print(f'O aumento do seu salário é de R$ {aumento:.2f} \n')
print(f'Seu novo salário é de R$ {novo:.2f} \n')

print('^^^'* 15)
print('Fim do desafio 34')
print('^^^'* 15)