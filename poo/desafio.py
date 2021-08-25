
class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual


if __name__ == '__main__':
    # se o programa esta sendo executado por si só
    c1 = Carro(180)

    for _ in range(25):
        print(f'Carro acelerando : {c1.acelerar(8)}')

    for _ in range(10):
        print(f'Carro freiando:{c1.frear(7)}')
