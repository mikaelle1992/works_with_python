
class HtmlToStringMixin:
    def __str__(self):
        #Conversão para Html
        html = super().__str__().replace('(', '<strong>(').replace(')', ')<strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + '(pet)' if self.pet else ''


class HtmlPessoa(HtmlToStringMixin, Pessoa):
    pass


class HtmlAnimal(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Pessoa('Andre')
    p2 = HtmlPessoa('Bia')
    gato1 = Animal('pandora')
    leao = HtmlAnimal('Rei Da selva')

    print(f'{p1}')
    print(f'{p2}')
    print(f'{gato1}')
    print(f'{leao}')