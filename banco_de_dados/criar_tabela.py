from bd import nova_conexao
from mysql.connector import ProgrammingError


tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50),tel VARCHAR(40)
        )
"""

tabela_email = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
        )
"""

        
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        # cursor.execute(tabela_email)
        cursor.execute(tabela_contatos)
    except ProgrammingError as e :
        print("Erro", e.msg)
        