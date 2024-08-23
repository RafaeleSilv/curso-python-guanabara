# ler os catetos e descobrir o valor da hipotenusa
import math
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adj.: '))
hip = (co**2 + ca**2) ** (1/2)
print('o valor da hipotenusa é igual a: {:.2f}'.format(hip))