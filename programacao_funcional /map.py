
lista_1 = [1, 2, 3]
dobro = map(lambda x: x*2, lista_1)
print(list(dobro))

lista_2 = [
    {'Nome': 'João', 'idade': 16},
    {'Nome': 'Ana', 'idade': 46},
    {'Nome': 'Maria', 'idade': 27},
    {'Nome': 'Bia', 'idade': 44},
]

so_nomes = map(lambda p: p['Nome'], lista_2)

so_idade = map(lambda idade: idade['idade'], lista_2)

node_idade = map(lambda p: f'{p["Nome"]} tem {p["idade"]} anos', lista_2)

print(list(node_idade))
print(list(so_nomes))
print('Soma das idades:', sum(so_idade))