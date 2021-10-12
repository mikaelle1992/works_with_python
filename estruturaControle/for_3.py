produto = {'Nome': 'Arroz', 'Preço': 3.5, 'Importado':True,'Estoque':'197'}

for chave in produto.keys():
    print(chave)
for valor in produto.values():
    print(valor)
for chave, valor in produto.items():
    print(chave, '=', valor)


print(chave, '=', valor)
# fica armazenado o ultimo valor
