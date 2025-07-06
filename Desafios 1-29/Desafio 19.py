#Desafio 19 - Limpeza do quadro
import random

print('xxx'*20)
print('Desafio 19 - Limpeza do quadro')
print('xxx'*20)
print() 
#Solicita o nome dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
#Escolha do aluno que irá limpar o quadro
alunos = [aluno1, aluno2, aluno3, aluno4] #Lista de alunos
escolhido = random.choice(alunos) #Escolhe um aluno aleatoriamente  
print()
#Exibe o nome do aluno escolhido
print(f"O aluno escolhido para limpar o quadro foi: {escolhido}")
print()
print('xxx'*20)
print('Fim do desafio 19')
print('xxx'*20)