
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for dado in dados.splitlines():
   # print(*dado.split(','))
    print('Nome:{}, Idade: {}'.format(*dado.split(',')))

