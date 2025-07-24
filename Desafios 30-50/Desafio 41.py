#Confederação de natação
from datetime import date
print('ooo'*10)
print('===== \033[3mConfederação de natação\033[0m')
print('ooo'*10)
print()
#Cálculo da idade do atleta
ano_atleta = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano_atleta
print(f'O atleta tem {idade} anos.')
print()
#Definindo a categoria do atleta
if idade <= 9:
    categoria = 'Mirim'
elif 10 <= idade <= 14:
    categoria = 'Infantil'
elif 15 <= idade <= 19:
    categoria = 'Junior'
elif 20 <= idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print(f'Segundo a idade do atleta, ele está na categoria \033[1;36m{categoria}\033[0m.')
print()
print('===== \033[3mFim do desafio 41\033[0m =====')
