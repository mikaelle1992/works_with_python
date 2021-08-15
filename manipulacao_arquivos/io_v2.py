arquivo = open('pessoas.csv')
for dado in arquivo:
    print('Nome:{} Idade:{}'.format(*dado.strip().split(',')))
    # o strip tira os espaços em brancos 

arquivo.close()    