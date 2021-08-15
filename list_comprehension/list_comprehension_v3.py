generator = (i ** 2 for i in range (10) if i % 2 == 0)
#generator, gera sob demanda
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# o proximo gera um erro 
       
