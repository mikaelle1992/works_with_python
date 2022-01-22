from bd import nova_conexao
from mysql.connector import ProgrammingError


deleta_tabela = """
    DROP TABLE IF EXISTS emails;
"""

try:        
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(deleta_tabela)
           
        except ProgrammingError as e :
            print("Erro", e.msg)
except ProgrammingError as e :
    print("Erro Conexao", e.msg)   