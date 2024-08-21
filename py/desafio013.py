# ler o salário de um funcionário e mostre seu novo salário com 15% de aumento

s1 = float(input('digite o atual salário: '))
a = (s1*15)/100
s2 = s1 + a

print('Parabéns! você recebeu um aumento. A partir do mês que vem, seu salário será: R${}'.format(s2))