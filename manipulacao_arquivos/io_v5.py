
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for dado in arquivo:
            pessoa = dado.strip().split(',')
            print('Nome:{} Idade:{}'.format(*pessoa), file=saida)
    # o strip tira os espaços em brancos

if arquivo.closed:
    print('O arquivo foi fechado')

if saida.closed:
    print('Arquivo de saida já foi fechado')
