from functools import partial


"""
primeiro faz os testes
"""


# def multiplo_n(num, multiplo):
#     return num % multiplo == 0


# def multiplo_5(num):
#     return num % 5 == 0


multipo_of = lambda multiplo, num: num % multiplo == 0
multipo_of_3 = partial(multipo_of, 3)
multipo_of_5 = partial(multipo_of, 5)


def robot(pos):
    say = str(pos)
    if multipo_of_3(pos) and multipo_of_5(pos):
        say = 'fizzbuzz'
    elif multipo_of_3(pos):
        say = 'fizz'
    elif multipo_of_5(pos):
        say = 'buzz'

    return say


if __name__ == '__main__':
    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'
    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
