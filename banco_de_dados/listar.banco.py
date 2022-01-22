from mysql.connector import connect

conexao = connect(
    host='localhost',
    port= 3306,
    user='admin',
    password='root'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco da dados {i}: {database[0]}')
