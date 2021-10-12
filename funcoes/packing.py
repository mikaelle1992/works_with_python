def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


num = (1, 5, 6)
num1 = (1, 1, 1)
# tupla
num2 = [3, 5, 9]


if __name__ == '__main__':
    print(soma_2(5, 6))
    print(soma_3(5, 6, 7))
    print(soma_n(5, 6, 7, 9, 3))
    print(soma_3(*num))
    print(soma_3(*num1))
    print(soma_3(*num2))
  
