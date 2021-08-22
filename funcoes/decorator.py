
def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada : {resultado}')
        return resultado
    return decorator    


@log
def soma(a, b):
    return a + b



@log
def sub (b, c, d):
    return b - c - d



if __name__ == '__main__':# se o programa esta sendo executado por si só  

    print(soma(1, 5))
    print(sub(1, c= 4, d=2))
