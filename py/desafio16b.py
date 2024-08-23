# ler um número real e dar a parte inteira com biblioteca math
from math import trunc
n1 = float(input('digite um número: '))
n2  = trunc(n1)
print('a parte inteira é: {}'.format(n2))