# um pograma que lê a altura e a largura de uma parade em m, calcule a área e a quantidade de tinta necessária para pintá-la

h = float(input('digite a altura da parede em m*2: '))
l = float(input('digite a largura em m*2: '))
a = h * l
lt = a / 2

print('a sua parede percisa de {}l de tinta para pintá-la'.format(lt))
