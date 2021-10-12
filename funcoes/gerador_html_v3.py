bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def get_atri(informa, suportado):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informa.items() if k in suportado)
    # -1 do split , retorna a ultimo elemento


def tag_bloco(conteudo, *args, classe='sucess', inline=False, **atributos):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **atributos)
    atr = get_atri(atributos, bloco_atrs)
    return f'<{tag} {atr} class="{classe}">{html}</{tag}>'
    # parametro class opcional


def tag_lista(*itens, **atri):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    atr = get_atri(atri, ul_atrs)
    return f'<ul {atr}>{lista}</ul>'


if __name__ == '__main__':# se o programa esta sendo executado por si só
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('Falhou', classe='error'))
    print(tag_bloco(tag_lista('Item1', 'Item2'), classe='item'))
    print(tag_bloco(tag_lista, 'Item1','Item2', classe='info', bloco_accesskey='m',
                    bloco_id='conteudo' , ul_id='lista'))