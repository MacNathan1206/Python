#Desafio 26: Letra A na frase
print('--'*20)
print('Desafio 26 - Letra A na frase')
print('__'*20)
print()
# Solicita uma frase ao usuário
frase = input("Digite uma frase: ").strip()
# Lista de variações da letra 'a'
variacoes_a = ['a', 'á', 'à', 'â', 'ã']
frase_lower = frase.lower()
quantidade = sum(frase_lower.count(letra) for letra in variacoes_a)
# Encontrar a posição da primeira e última ocorrência de qualquer variação de 'a'
primeira_vez = -1
ultima_vez = -1
for i, caractere in enumerate(frase_lower):
    if caractere in variacoes_a:
        if primeira_vez == -1:
            primeira_vez = i + 1  # +1 para posição humana
        ultima_vez = i + 1       # +1 para posição humana

# Exibe os resultados
print(f"A letra 'A' aparece {quantidade} vezes na frase.")
if primeira_vez != -1:
    print(f"A primeira letra 'A' aparece na posição {primeira_vez}.")
    print(f"A última letra 'A' aparece na posição {ultima_vez}.")
else:
    print("A letra 'A' não aparece na frase.")
print()
print('--'*20)
print('Fim do Desafio 26')
print('__'*20)

