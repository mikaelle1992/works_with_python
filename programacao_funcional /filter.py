
pessoas = [
    {'nome': 'João Pedro', 'idade': 16},
    {'nome': 'Ana', 'idade': 17},
    {'nome': 'Maria', 'idade': 27},
    {'nome': 'Bia', 'idade': 44},
    {'nome': 'Mariana', 'idade': 15},
    {'nome': 'Henrique', 'idade': 8},
    {'nome': 'Pedro', 'idade': 21},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
nomes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print("Menores:", list(menores))
print(list(nomes))
