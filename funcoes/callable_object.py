
class Potencia:

    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self,base):
        return base ** self.expoente

if __name__ == '__main__':# se o programa esta sendo executado por si só
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'resposta: {quadrado(3)} \nresposta: {cubo(3)} ')
        print (Potencia(4)(2))