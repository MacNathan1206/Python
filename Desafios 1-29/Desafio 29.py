#Desafio 29: Multa por excesso de velocidade
print('ooo'*20)
print('Desafio 29 - Multa por excesso de velocidade')
print('ooo'*20)
print()
# Velocidade atual do carro
velocidade = float(input('Digite a velocidade atual do carro (km/h): '))
print()
# Velocidade máxima permitida
max = 80.0
#Calculo da multa por excesso de velocidade
excesso = velocidade - max
multa = excesso * 7.0
if velocidade > max:
    print(f'Você ultrapassou o limite de velocidade de {max} km/h em {excesso:.2f} km/h. \n')  
    print(f'Você será multado por excesso de velocidade com uma multa de R$ {multa:.2f}')
else:
    print('Você está dentro do limite de velocidade 80.0 km/h. Dirija sempre com segurança!')
print()
print('ooo'*20)
print('Fim do Desafio 29')
print('ooo'*20)
