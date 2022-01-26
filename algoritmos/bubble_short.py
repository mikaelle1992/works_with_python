
def bubble_short(lista):
    n= len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                #troca de elementos
                lista[i], lista[i+1] = lista[i+1], lista[i] 
                # aux = lista[i]
                # lista[i] = lista[i+1]
                # lista[i+1] = aux
    return lista

if __name__ == '__main__':
    lista = [1, 5, 0, 6, 10, 3]
    print(bubble_short(lista))