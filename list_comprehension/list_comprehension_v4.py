generator = (i ** 2 for i in range (10) if i % 2 == 0)

for numero in generator:
    print(numero)

# dependendo da quantidade de elementos prefira o generator por ser mais economico no que diz respeita a memoria    
