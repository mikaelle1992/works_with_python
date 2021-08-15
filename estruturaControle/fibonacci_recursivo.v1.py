def fibonacci(qtd, sequencia = (0, 1)):
    
   if len(sequencia) == qtd:
       return sequencia
   return fibonacci(qtd, sequencia + (sum(sequencia[-2:]),))    




if __name__ == '__main__':
        for fib in fibonacci(3):
            print(fib)
