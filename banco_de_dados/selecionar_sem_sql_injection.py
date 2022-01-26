from bd import nova_conexao

sql = "SELECT * FROM contatos where nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar:')
    args = (f'%{nome}%',)
    # os % tem que vim aqui
    cursor = conexao.cursor()
    cursor.execute(sql, args)
    
    for x in cursor:
        print(x)
        