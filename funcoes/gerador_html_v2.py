from typing import Text


def tag_bloco(texto, classe='sucess', inline = False):
    tag = 'span' if inline else 'div'

    return f'<{tag} class="{classe}">{texto}</{tag}>'
 #parametro class opcional 
if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe','info',True))
    print(tag_bloco('inline', inline = True))     
    print(tag_bloco('Falhou', classe='error'))     