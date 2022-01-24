from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '98748-5301'),
    ('Bia', '98773-1321'),
    ('Gui', '98772-5321'),
    ('Pedro', '98764-9721'),
    ('Paulo', '98764-5300'),
)

try:        
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
           
        except ProgrammingError as e :
            print("Erro", e.msg)
        else:
            print(f'Foram incluidos {cursor.rowcount} registros')
except ProgrammingError as e :
    print("Erro Conexao", e.msg)
       