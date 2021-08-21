
def fibonacci(seguencia=[0,1]):
    #Uso de mutáveis como valor defualt (armadilha)
    seguencia.append(seguencia[-1] + seguencia[-2])
    return seguencia


if __name__ == '__main__':# se o programa esta sendo executado por si só   
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart ==[0, 1, 1]