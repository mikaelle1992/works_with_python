

def tag_bloco(texto, classe='sucess', inline = False):
    tag = 'span' if inline else 'div'

    return f'<{tag} class="{classe}">{texto}</{tag}>'
 #parametro class opcional 

def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe','info',True))
    print(tag_bloco('inline', inline = True))     
    print(tag_bloco('Falhou', classe='error'))     
    print(tag_bloco(tag_lista('Item1','Item2'), classe= 'item'))