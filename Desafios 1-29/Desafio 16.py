import math

#Desafio 16: Parte inteira de um número real

print('=-'*30)
print("Desafio 16: Parte inteira de um número real")
print('=-'*30)

entrada = input("Digite um número real: ")
numero = float(entrada)
def parte_inteira(numero):
    """
    Retorna a parte inteira de um número real.
    """
    return math.trunc(numero)  
def parte_decimal(numero):
    """
    Retorna a parte decimal de um número real.
    """
    return numero - math.floor(numero)

# Conta os dígitos após o ponto na entrada
if '.' in entrada:
    casas_decimais = len(entrada.split('.')[1])
else:
    casas_decimais = 0

print()
print(f"A parte inteira de {numero} é {parte_inteira(numero)} e a parte decimal é {parte_decimal(numero):.{casas_decimais}f}") 
print()
print('=-'*30)
print("Fim do desafio 16")
print('=-'*30)