def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

if __name__ == '__main__': 
    todos_params('a','b','c')
    todos_params(1, 2, 3, sol = False, lua =  True)
    todos_params('Ana', True, [1, 2, 3], tamano = 'G', altura = 1.67)
    todos_params(primeiro =  'Pinheiro', segundo = 'Sousa')
    todos_params('Sousa', primeiro = 'Pinheiro')
