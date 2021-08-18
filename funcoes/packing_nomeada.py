
def resuldo_f1(**podium):
    #** aceita um dict
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')

if __name__ == '__main__':
    resuldo_f1(primeiro='Ana',
                segundo='Pedro', terceiro='Andre')