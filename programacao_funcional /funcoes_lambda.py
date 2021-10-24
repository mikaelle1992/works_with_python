compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 50},
    {'quantidade': 5, 'preco': 30},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print('Preços totais:', list(totais))
print('total geral:', sum(totais) )