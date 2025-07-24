# Emprestimo para comprar casa

print('...'*20)
print('Desafio 36 - Emprestimo para comprar casa')
print('...'*20)

#Ingresar os dados necessários para análise do emprestimo
salario = float(input('Informe o seu salário: R$ '))
casa = float(input('Informe o valor da casa que deseja comprar: R$ '))
parcelas = int(input('Informe em quantos anos deseja pagar: '))

# Calcular o valor da parcela mensal
valor_parcela = casa / (parcelas * 12)

# Viabilidade do emprestimo

if valor_parcela <= salario * 0.3:
    print(f'Empréstimo aprovado! O valor da parcela mensal será de R$ {valor_parcela:.2f}.')
else:
    print(f'Empréstimo negado! O valor da parcela mensal de R$ {valor_parcela:.2f} excede 30% do seu salário de R$ {salario:.2f}.\n')
print('...'*20)
print('Fim do Desafio 36')
print('...'*20)
