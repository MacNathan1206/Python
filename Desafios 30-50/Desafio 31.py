#Desafio 31 : Preço de passagens
print('lll'*20)
print('Desafio 31 - Preço de passagens')
print('lll'*20)
#Pedir o dado da distância
distancia = float(input('Qual a distância, em kilometros, da sua viagem? \n'))
#Calcular o preço da passagem
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
#Mostrar o preço da passagem
print()
print(f'O preço da sua passagem é de R$ {preco:.2f} \n')
print('Obrigado por viajar conosco!')

