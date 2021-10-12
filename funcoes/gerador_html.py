

def tag_bloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'
    # parametro class opcional
 

if __name__ == '__main__':
    # testes com assertions
    assert tag_bloco('incluindo texto') ==\
        '<div class="sucess">incluindo texto</div>'
    assert tag_bloco('excluir conteudo','error') ==\
        '<div class="error">excluir conteudo</div>'   

    print(tag_bloco('bloco'))     