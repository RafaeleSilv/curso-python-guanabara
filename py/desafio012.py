# ler um preço e mostrar um novo preço com 5% de desconto

p1 = float(input('digite o preço atual do produto: '))
d = (p1 * 5)/100
p2 = p1 - d
print('o produto com o desconto está por R${}'.format(p2))