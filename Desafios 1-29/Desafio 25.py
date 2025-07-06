#Desafio 25: Tem Silva no seu nome?
print('--'*20)
print('Desafio 25 - Tem Silva no seu nome?')
print('__'*20)
# Solicita o nome completo de uma pessoa ao usuário
nome = input("Digite o seu nome completo: ")
# Verifica se o nome contém "Silva"
if 'silva' in nome.lower():
    print("O nome contém 'Silva'.")
else:
    print("O nome não contém 'Silva'.")
print()
print('O nome digitado tem Silva? {}'.format('silva' in nome.lower()))
print()

print('--'*20)
print('Fim do Desafio 25')
print('__'*20)
