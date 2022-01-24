from bd import nova_conexao

sql = "SELECT * FROM contatos where tel = '98764-5321'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    for x in cursor:
        print(x)
        