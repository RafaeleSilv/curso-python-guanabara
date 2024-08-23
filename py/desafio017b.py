# usando módulo hypot para descobrir a hipotenusa
import math
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adj.: '))
hip = math.hypot(co, ca)
print('o valor da hipotenusa é: {:.2f}'.format(hip))