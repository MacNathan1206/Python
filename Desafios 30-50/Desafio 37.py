#Converãao de sistema de numeração
print('...'*20)
print('Desafio 37 - Conversão de sistema de numeração')
print('...'*20)
#Ingresar o número a ser convertido
numero = int(input('Informe um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[1] Converter para binário')
print('[2] Converter para octal')
print('[3] Converter para hexadecimal')
opcao = int(input('Sua opção: '))
# Realizar a conversão com base na opção escolhida
if opcao == 1:
    print(f'O número {numero} em binário é: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} em octal é: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} em hexadecimal é: {hex(numero)[2:].upper()}')
else:
    print('Opção inválida! Por favor, escolha uma opção válida.')
print()
print('...'*20)
print('Fim do Desafio 37')
print('...'*20)