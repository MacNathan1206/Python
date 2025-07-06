# Desafio 23: Digitos separados
print('--'*20)
print('Desafio 23 - Dígitos separados')
print('__'*20)
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro positivo entre 0 e 9999: "))
# Converte o número para uma string para facilitar a separação dos dígitos
numero_str = str(numero)
# Criar lista
unidade = numero_str[-1] if len(numero_str) > 0 else '0'
dezena = numero_str[-2] if len(numero_str) > 1 else '0'
centena = numero_str[-3] if len(numero_str) > 2 else '0'
milhar = numero_str[-4] if len(numero_str) > 3 else '0'
# Exibe os dígitos separados
print(f"Unidades: {unidade}")
print(f"Dezenas: {dezena}")
print(f"Centenas: {centena}")
print(f"Milhares: {milhar}")  
print('--'*20)
print('Fim do Desafio 23')
print('__'*20)