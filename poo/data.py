class Data:
    # construtor __init__
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 4, 2017)
# d1.dia = 5
# d1.mes = 4
# d1.ano = 2017
print(d1)

d2 = Data(14, 7, 2021)
d2.dia = 14
d2.mes = 8
d2.ano = 2021
print(d2)
