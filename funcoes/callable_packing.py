
def calc_preco_final(preco_bruto, calc_importo, *params):
    return preco_bruto + preco_bruto * calc_importo(*params)


def importo_x(importado):
    return 0.22 if importado else 0.13


def importo_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0        


if __name__ == '__main__':# se o programa esta sendo executado por si só
    preco_bruto = 135.01
    preco_final = calc_preco_final(preco_bruto, importo_x, True)
    preco_final = calc_preco_final(preco_final, importo_y, True, 1.5)   
    print(f'Preço final : {preco_final}')