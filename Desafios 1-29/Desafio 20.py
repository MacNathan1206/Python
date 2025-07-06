#Apresentação de trabalhos 
print('^^^'*20)
print('Desafio 20 - Apresentação de trabalhos')
print('^^^'*20)
print()
import random
# Solicita todos os nomes em uma linha só
entrada = input("Digite o nome dos alunos separados por vírgula: ")
alunos = [nome.strip() for nome in entrada.split(',') if nome.strip()]
print()  # Linha em branco para melhor formatação
random.shuffle(alunos)  # Embaralha a lista de alunos
print('A ordem de apresentação dos trabalhos será:')
print()
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}º - {aluno}")    
print()
print('^^^'*20)
print('Fim do desafio 20')
print('^^^'*20)
