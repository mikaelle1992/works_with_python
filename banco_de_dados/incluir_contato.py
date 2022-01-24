from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Lucas', '98764-5321')

try:        
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
           
        except ProgrammingError as e :
            print("Erro", e.msg)
        else:
            print('1 registro incluido, ID:', cursor.lastrowid)
except ProgrammingError as e :
    print("Erro Conexao", e.msg)
       