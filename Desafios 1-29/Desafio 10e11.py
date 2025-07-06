 #Desafio 10
print()
print('='*50)
print('Desafio 10 - Conversor de Reais para Dólares')
print('='*50)
print()

#Entrada de dados
reais = float(input('Digite a quantidade de reais que você possui: R$ \n'))

#Calculo da conversão
dolar = reais / 5.25

#Resultado
print(f'Com R$ {reais:.2f} você pode comprar US$ {dolar:.2f} dólares.')
print()
print('Fim do desafio 10!')
print()

# Desafio 11
print('='*50)
print('Desafio 11 - Calculadora de Área de Pintura')
print('='*50)
print()
print('<<<Para digitar números com decimais, use o ponto (.) como separador.', end='>>>\n')

# Entrada de dados
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

# Cálculo da área e tinta necessária
area = largura * altura 
tinta = area / 2    # 1 litro de tinta cobre 2 m²

# Resultado
print()
print(f'A área da parede é de {area:.2f} m² e você precisará de {tinta:.2f} litros de tinta para pintá-la.', end='\n')
print()
print('Fim do desafio 11! \n')
print()