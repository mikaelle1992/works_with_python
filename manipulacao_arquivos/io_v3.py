try:
arquivo = open('pessoas.csv')
    for dado in arquivo:
        print('Nome novo:{} Idade:{}'.format(*dado.strip().split(',')))
    # o strip tira os espaços em brancos 
finally:
#finally sempre sera executado, mesmo que tenha uma erro no codigo
    print("arquivo fechado")
    arquivo.close() 

    if arquivo.closed: 
        print('O arquivo foi fechado') 