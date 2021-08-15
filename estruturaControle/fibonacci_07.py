def fibonacci (qtd):
    resultado = [0, 1]
    for _ in range(qtd):
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == qtd:
           
            return resultado




if __name__ == '__main__':
        for fib in fibonacci(5):
            print(fib)
