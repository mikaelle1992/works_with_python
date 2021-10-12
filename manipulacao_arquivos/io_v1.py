
arquivo = open('postos.json')
dados = arquivo.read()
arquivo.close()

for dado in dados.splitlines():
   # print(*dado.split(','))
    print(format(*dado.split(',')))

