# sorteando uma ordem na lista --> usando o shuffle do random
import random
a1 = input('1 aluno: ')
a2 = input('2 aluno: ')
a3 = input('3 aluno: ')
a4 = input('4 aluno: ')
lista = [a1, a2, a3, a4]
sorteio = random.shuffle(lista)
print('ordem da apresentação: {}'. format(lista))
