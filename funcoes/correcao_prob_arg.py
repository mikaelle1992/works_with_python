
def fibonacci(seguencia=None):
    #usando o None , toda vez que o fabonacci for chamado ira resertar os valores do parametro
    seguencia = seguencia or [0, 1]
    seguencia.append(seguencia[-1] + seguencia[-2])
    return seguencia


if __name__ == '__main__':# se o programa esta sendo executado por si só   
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart ==[0, 1, 1]