#Desafio 12
print()
print('=' * 50)
print('Desafio 12 - Calculadora de Desconto')
print('=' * 50)
print()

# Entrada de dados
while True:
    try:
        preco = float(input('Digite o preço do produto: R$ '))
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        break  # Sai do loop se for um número válido
    except ValueError as e:
        print(f"Valor inválido! {e}. Por favor, verifique o preço e digite novamente")

# Cálculo do desconto
desconto = preco * 0.05  # 5% de desconto
preco_final = preco - desconto  # Preço final após desconto     

# Resultado
print()
print(f'O preço do produto com 5% de desconto é R$ {preco_final:.2f}, e você economiza R$ {desconto:.2f}.')
print()
print('Fim do desafio 12!')

# Desafio 13
print('=' * 50)
print('Desafio 13 - Calculadora do aumento de salario')
print('=' * 50)
print()

# Entrada de dados
while True:
    try:
        salario = float(input('Digite o salário do funcionário: R$ '))
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        break  # Sai do loop se for um número válido
    except ValueError as e:
        print(f"Valor inválido! {e}. Por favor, verifique o salário e digite novamente")

# Cálculo do aumento
aumento = salario * 0.15  # 15% de aumento
salario_final = salario + aumento  # Salário final após aumento     

# Resultado
print()
print(f'O salário do funcionário com 15% de aumento é R$ {salario_final:.2f}, e o aumento foi de R$ {aumento:.2f}.')
print()
print('Fim do desafio 13!')
print()
# Fim do desafio 13!