#Desafio 35: Retas para um triângulo
print('^^^'* 15)
print('Desafio 35: Retas para um triângulo')
print('^^^'* 15)
print()
#Entrada de dados
reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
#Calculo se forma um triângulo
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print()
    print('As retas formam um triângulo!')
else:
    print()
    print('As retas não formam um triângulo!')
#Resultado
print()
print('^^^'* 15)
print('Fim do desafio 35')
print('^^^'* 15)