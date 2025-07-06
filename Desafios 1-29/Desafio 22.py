# Desafio 22: Nome completo

print('_-_-'*20)
print('Desafio 22 - Nome completo')
print('_-_-'*20)
print()
# Solicita o nome completo do usuário
nome = input("Digite seu nome completo: ")
#Letras maiúsculas
nome_maiusculo = nome.upper()
#Letras minúsculas
nome_minusculo = nome.lower()
#Quantidade de letras sem espaços
quantidade_letras = len(nome.replace(" ", ""))
#Quantidade de letras do primeiro nome
primeiro_nome = len(nome.split()[0])
# Exibe os resultados
print()
print(f"Nome em maiúsculas: {nome_maiusculo}")
print()
print(f"Nome em minúsculas: {nome_minusculo}")
print()
print(f"Quantidade de letras (sem espaços): {quantidade_letras}")
print()
print(f"Quantidade de letras do primeiro nome: {primeiro_nome}")
print()
print('_-_-'*20)
print('Fim do desafio 22')
print('_-_-'*20)
