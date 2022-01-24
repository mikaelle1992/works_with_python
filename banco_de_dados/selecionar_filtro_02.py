from bd import nova_conexao

# sql = "SELECT * FROM contatos where nome like '%bi%'"
sql = "SELECT * FROM contatos where nome like 'A%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    for x in cursor:
        print(x)
        