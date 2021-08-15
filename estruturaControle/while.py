from random import randint

num_inf = -1
num_aleatorio = randint(0,9)

while num_inf != num_aleatorio:
    num_inf = int(input('informe o valor: '))

print('Numero secreto {} foi encontrado !' .format(num_aleatorio))    