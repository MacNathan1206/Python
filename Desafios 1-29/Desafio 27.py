# Desafio 27: Primeiro e último nome
print('*+*'*20)
print('Desafio 27 - Primeiro e último nome')
print('+*+'*20)
print()
# Solicita o nome completo ao usuário
nome = input("Digite seu nome completo: ").strip()
# Divide o nome completo em partes
partes = nome.split()
# Verifica se o nome tem pelo menos duas partes
if len(partes) < 2:
    print("Por favor, digite pelo menos um nome e um sobrenome.")
else:
    primeiro_nome = partes[0] # Obtém o primeiro e o último nome
    ultimo_nome = partes[-1]
# Exibe os resultados
    print(f"Seu primeiro nome é: {primeiro_nome}")
    print(f"Seu último nome é: {ultimo_nome}")
print()
print(f'Se primeiro nome é: {partes[0]}')
print(f'Seu último nome é: {partes[-1]}')
print('¨¨'*20)
print('Fim do Desafio 27')
print('¨¨'*20)
