#Desafio 38: Comparação de números
print('--'*15)
print('Desafio 38 - Comparação de dois números inteiros')
print('--'*15)
#Ingresar dois números inteiros
num1 = int(input('Informe o um número inteiro: '))
num2 = int(input('Informe outro número inteiro: '))
# Comparar os números e exibir o resultado
if num1 > num2:
    print(f'O número 1 {num1} é maior que o número 2 {num2}.')
elif num1 < num2:
    print(f'O número 1 {num1} é menor que o número 2 {num2}.')
else:
    print(f'Os números são iguais: {num1} = {num2}.')
print()
print('--'*15)
print('Fim do Desafio 38')
print('--'*15)
