# Desafio 17 Hipotenusa

print('-==-'*20)
print('Desafio 17 - Hipotenusa')
print('-==-'*20)

import math

print ('Digite o comprimento do cateto 1: ')
cateto1 = float(input())
print ('Digite o comprimento do cateto 2: ')
cateto2 = float(input())
hipotenusa = math.hypot(cateto1, cateto2)
print()
print('A hipotenusa do triangulo reto com catetos de comprimento {:.2f} e {:.2f} é {:.2f}'.format(cateto1, cateto2, hipotenusa))
print()
print('-==-'*20)
print('Fim do Desafio 17 - Hipotenusa')
print('-==-'*20)    
