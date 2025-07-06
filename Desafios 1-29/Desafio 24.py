#Desafio 24: Cidade com Santo
print('--'*20)
print('Desafio 24 - Cidade com Santo')
print('__'*20)
# Solicita o nome de uma cidade ao usuário
cidade = input("Digite o nome de uma cidade brasileira: ")
# Verifica se a cidade começa com "Santo"
lista = cidade.split()
# Verifica se a primeira palavra da cidade é "Santo" (considerando letras mai
if lista[0].lower() == 'santo':
    print("A cidade começa com 'Santo'.")
else:
    print("A cidade não começa com 'Santo'.")
print()
print('--'*20)
print('Fim do Desafio 24')
print('__'*20)
