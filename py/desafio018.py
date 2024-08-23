# ler um ângulo e mostrar o valor de seno cosseno e tg desse ângulo obs; math.radians converte para graus
import math
a = float(input('digite o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('o ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e o tangente de {:.2f}' .format(a, s, c, tg))


