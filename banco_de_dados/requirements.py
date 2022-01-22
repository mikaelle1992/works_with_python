#!python3
try:
    from mysql import connector as connect
except ModuleNotFoundError:
    print('Mysql connector não instalado')
else:
    print('Mysql connector instalado')