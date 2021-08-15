

def notasDaTurma(nota):
    nota = float(nota)
    if nota >10:
        return 'nota invalida'
    elif nota >= 9.1:
        return'A'
    elif nota >= 8.1:
        return'A-'
    elif nota >= 7.1:
        return'B'
    elif nota >= 6.1:
        return'B-'
    elif nota >= 5.1:
        return'C'
    elif nota >= 4.1:
        return'C-'    
    elif nota >= 3.1:
        return'D'
    elif nota >= 2.1:
        return'D-'   
    elif nota >= 1.1:
        return'E'
    elif nota >=0.0:
        return'E-'
    else:
      print('Nota invalida , viu')


if __name__ == '__main__':
        nota = input('Informe a nota do aluno: ')
        resultado = notasDaTurma(nota)
        print(resultado)
        
    
