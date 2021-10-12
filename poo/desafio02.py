from datetime import datetime
from loja.cliente import Cliente
from loja.compra import Compra
from loja.vendedor import Vendedor


def main():
    cliente = Cliente('Ana', 54)
    cliente2 = Cliente('Ricardo', 29)
    vendedor = Vendedor('Andre', 27, 1000)
    compra1 = Compra(vendedor, datetime.now(), 150)
    compra2 = Compra(vendedor, datetime(2021, 9, 15), 250)
    compra3 = Compra(vendedor, datetime.now(), 527)

    cliente.registrar(compra1)
    cliente2.registrar(compra2)
    cliente.registrar(compra3)

    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor:{compra1.vendedor}')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Valor da compra: {valor_total} em {qtde_compras}')
    print(f'Ultima compra {cliente.get_data_ultima_compra()}')
    print('--------------------------------------------------------')

    print(f'Cliente: {cliente2}', '(adulto)' if cliente2.is_adulto() else '')
    print(f'Vendedor:{compra2.vendedor}')

    valor_total = cliente2.total_compras()
    qtde_compras = len(cliente2.compras)
    print(f'Valor da compra: {valor_total} em {qtde_compras}')
    print(f'Ultima compra: {cliente2.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
else:
    print(__name__)
