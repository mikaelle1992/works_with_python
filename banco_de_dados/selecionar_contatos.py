from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'SELECT * FROM contatos'


try:        
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)   
            contatos = cursor.fetchall()
           
        except ProgrammingError as e :
            print("Erro", e.msg)
        else:
            for contato in contatos:
                print(f'{contato[2]:2d} - {contato[0]:20s} Telefone: {contato[1]}')
except ProgrammingError as e :
    print("Erro Conexao", e.msg)