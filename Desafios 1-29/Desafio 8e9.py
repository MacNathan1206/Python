
# Desafio 8

print()
print('=' * 50)
print('Desafio 8 : Conversor a centimetros e milimetros')
print('=' * 50)
print()

# Entrada de dados
while True:
    try:
        medida = float(input("Digite uma distância em metros: "))
        break  # Sai do loop se for um número válido
    except ValueError:
        print("Valor inválido! Por favor, digite um número.")

# Calculo de conversao
centimetros = medida * 100
milimetros = medida * 1000

# Saída de dados
print()
print(f'A medida de {medida} metros corresponde a {centimetros:.0f} centimetros e {milimetros:.0f} milimetros.')
print()
print('Fim do desafio 8!')
print()

# Desafio 9

print('=' * 50)
print('Desafio 9: Tabuada')
print('=' * 50)

# Entrada de dados

numero = int(input('Digite um número para ver sua tabuada: '))

# Saída de dados
print()
print(f'Tabuada do {numero}:')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i:2} = {resultado:2}')
print()