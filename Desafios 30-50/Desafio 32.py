#Desafio 32: Ano bissexto 

print('¡!¡!'* 15)
print('Desafio 32: Ano bissexto')
print('¡!¡!'* 15)

ano = int(input('Digite o ano que você deseja saber se é bissexto: \n'))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'\033[34mO ano {ano} é bissexto.\33[m')
else:
    print(f'\033[31mO ano {ano} não é bissexto.\033[m')

print('¡!¡!'* 15)
print('Fim do desafio 32')
print('¡!¡!'* 15)

