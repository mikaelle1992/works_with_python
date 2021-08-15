import csv
from urllib import request

def read(url):
    with request.urlopen(url) as entrada:
        print('baixando')
        dados = entrada.read().decode('latin1')
        #decode('latin1') , para ler o arquivo direito com acentuação tudo de forma correta
        print('Download completo')
        for cidade in csv.reader(dados.splitlines()):
            #splitlines() = ler cada uma das linhas 
            print(f'{cidade[8]} : {cidade[3]}')
            #[8],[3] indices da colunas que quero o retorno
    
if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')  
    # 'r'=quando trabalhar com url é usar o 'r' para que os caracter especial não sejam interpretada de forma indevida

