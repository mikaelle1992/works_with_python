
from functools import reduce


pessoas = [
    {'nome': 'João Pedro', 'idade': 16},
    {'nome': 'Ana', 'idade': 17},
    {'nome': 'Maria', 'idade': 27},
    {'nome': 'Bia', 'idade': 44},
    {'nome': 'Mariana', 'idade': 15},
    {'nome': 'Henrique', 'idade': 8},
    {'nome': 'Pedro', 'idade': 21},
]

so_idade = map(lambda idade: idade['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idade)
soma_idade = reduce(lambda idades, idade: idades + idade, menores, 0)


# soma_idade = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
#idades é o acumulador e começa com 0, p:idades é o item atual 
print('a soma das idades:', soma_idade)
