#Desafio 33: Número maior e menor
print('¡!'* 15)
print('Desafio 33: Número maior e menor')
print('¡!'* 15)
print()
#Entrada de dados
uno = float(input('Digite um número: '))
dois = float(input('Digite outro número: '))
tres = float(input('Digite mais um número: '))
#Calculo numero maior
if uno > dois and uno > tres:
    maior = uno
elif dois > uno and dois > tres:
    maior = dois
else:
    maior = tres
#Calculo numero menor
if uno < dois and uno < tres:
    menor = uno
elif dois < uno and dois < tres:
    menor = dois
else:
    menor = tres
#Resultado
print()
print(f'O maior número é {maior} \n')
print(f'O menor número é {menor} \n')

print('¡!'* 15)
print('Fim do desafio 33')
print('¡!'* 15)


