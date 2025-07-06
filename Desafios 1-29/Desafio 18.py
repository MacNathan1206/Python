# Funções trigonométricas
import math
print('-==-'*20)
print('Desafio 18 - Funções Trigonométricas')
print('-==-'*20)
print()
# Solicita o ângulo em graus e converte para radianos
angulo = math.radians(float(input("Digite o ângulo em graus: ")))
#Calculos
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
# Exibe os resultados
print()
print(f'Seno de {angulo}: {sen:.3f}')
print(f'Cosseno {angulo}: {cos:.3f}')
print(f'Tangente {angulo}: {tan:.3f}')
print()
print('-==-'*20)
print('Fim do Desafio 18 - Funções Trigonométricas')
print('-==-'*20)