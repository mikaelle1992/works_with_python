compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 50},
    {'quantidade': 5, 'preco': 30},
)


def calculo_compras(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(calculo_compras, compras))

print('Preços totais:', list(totais))
print('total geral:', sum(totais))
