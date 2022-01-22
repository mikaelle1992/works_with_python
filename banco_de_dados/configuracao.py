from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3006,
    user='admin',
    password='root',
)

print(conexao)