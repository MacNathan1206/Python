#Notas da escola
print('ooo'*10)
print('===== \033[3mNotas da escola\033[0m =====')
print('ooo'*10)
print()
#Ingressando as notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print()
#Caculando o destino do aluno
if media < 5.0:
    print(f'Você foi \033[1;31mReprovado\033[0m com uma média de {media:.1f}.')
elif 5.0 <= media < 7.0:
    print(f'Você está de \033[1;33mRecuperação\033[0m com uma média de {media:.1f}.')
else:
    print(f'Você foi \033[1;32mAprovado\033[0m com uma média de {media:.1f}.')
print()
print('===== \033[3mFim do desafio 40\033[0m =====')