
class Humano:

    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def inteligent(self):
        raise NotImplementedError('Propriedade não implementada')   

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('idade deve ser um numero positivo')
        self._idade = idade

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligent(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligent(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('Jose')

    try:
        print(anonimo.inteligent)
    except NotImplementedError:
        print('Propriedade abstrata')
    
    jose = HomoSapiens('outro jose')
    print(f'{jose.nome} da classe {jose.__class__.__name__}, inteligente:{jose.inteligent}')

    grong = Neanderthal('grong')
    print(f'{grong.nome} da classe {grong.__class__.__name__}, inteligente:{grong.inteligent}')