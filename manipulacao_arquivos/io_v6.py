import json

with open('postos.json') as entrada:
    for dado in json.reader(entrada):
        print('NomeNovao:{} Idade:{}'.format(*dado))
    

