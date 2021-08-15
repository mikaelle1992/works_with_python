import csv
with open('pessoas.csv') as entrada:
        for dado in csv.reader(entrada):
            print('Nome:{} Idade:{}'.format(*dado))
    

