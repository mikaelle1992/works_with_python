from funcao_primeira_class import dobro, quadrado


def processando(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(f'{i} => {funcao(i)}')


if __name__ == "__main__":
    processando('Dobros de 1 a 10', range(1, 11), dobro)
    processando('Quadrado de 1 a 10', range(1, 11), quadrado)