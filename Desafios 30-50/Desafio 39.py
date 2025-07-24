#Alistamento militar
from datetime import date
print()
print('===== \033[3mAlistamento militar\033[0m =====')
print()
data = int(input('Digite o ano de nascimento: '))
print()
ano_atual = date.today().year
idade = ano_atual - data
if idade < 18:
    print(f'Você ainda não tem idade para se alistar, faltam {18 - idade} anos.')
elif idade == 18:
    print('Você deve se alistar este ano!')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.\n')
    ano_alistamento = data + 18
    print(f'Seu alistamento foi em {ano_alistamento}.')
print()
print('===== \033[3mFim do desafio 39\033[0m =====')
print()
