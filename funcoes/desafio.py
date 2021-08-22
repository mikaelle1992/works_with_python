
def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ' '.join(f'{k} = "{v}"' for k, v in kwargs.items())
    inner = ' '.join(args)    
    return f'<{tag} {attrs}>{inner}</{tag}>'

if __name__ == '__main__':# se o programa esta sendo executado por si só        
    print(
        tag('p',
        tag('span', 'Curso de Python , por'),
        tag('strong', 'Juracy Filho', id = 'jf'),
        tag('span','e'),
        tag('strong', 'Leonardo Leitão', id = 'll'),
        tag('span','.'),
        html_class = 'alert')
    )