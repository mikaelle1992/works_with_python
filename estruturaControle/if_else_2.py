def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(19, 68):
        return 'Adulto'
    elif idade in range(65, 101):
        return 'Melhor Idade'


if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -2):
        print(f'Idade : {idade} / Faixa Etaria: {faixa_etaria(idade)}')