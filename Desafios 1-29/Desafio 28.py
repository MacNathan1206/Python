#Desafio 28: O computador que escolhe
import random   
print('*+*'*20)
print('Desafio 28 - O computador que escolhe')
print('+*+'*20)
print()

# Escolha de um número aleatório entre 0 e 5 pelo computador
numero = random.randint(0, 5)

# Usuário digita um número válido
while True:
    usuario = int(input("Digite um número inteiro entre 0 e 5: "))
    if 0 <= usuario <= 5:
        break
    print("Número inválido! Por favor, escolha um número entre 0 e 5.")

# Comparação entre o número do computador e o número do usuário
print()
if usuario == numero:
    print(f"Parabéns! Você acertou o número {numero}.")
else:
    print(f"Você errou! O número era {numero}.")
print()
print('¨¨'*20)
print('Fim do Desafio 28')
print('¨¨'*20)
