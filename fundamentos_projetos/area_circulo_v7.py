from math import pi


def circulo(raio):
     print('Área do circulo', pi * float(raio) ** 2)

if __name__ == '__main__':
    raio = input('Informe o valor do raio :' )#o input retun string
    circulo(raio)

