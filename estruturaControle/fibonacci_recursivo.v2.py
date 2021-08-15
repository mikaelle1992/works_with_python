def fibonacci(qtd, sequencia = (0, 1)):
    
       return sequencia if len(sequencia) == qtd else\
            fibonacci(qtd, sequencia + (sum(sequencia[-2:]),))    


if __name__ == '__main__':
        for fib in fibonacci(7):
            print(fib)
