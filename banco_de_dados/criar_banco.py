from mysql.connector import connect

conexao = connect(
    host='localhost',
    port= 3306,
    user='admin',
    password='root'
)

cursor = conexao.cursor()
# IF NOT EXISTS caso exista no banco ele não dá erro.
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')