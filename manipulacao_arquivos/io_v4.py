
with open('pessoas.csv') as arquivo:

    for dado in arquivo:
        print('Nome:{} Idade:{}'.format(*dado.strip().split(',')))
    # o strip tira os espaços em brancos

if arquivo.closed: 
        print('O arquivo foi fechado')
