
def selection_short(lista):
    n= len(lista)
    
    for j in range(n-1):
        min_index = j 
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    return lista
            
            

if __name__ == '__main__':
    lista = [1, 5, 0, 6, 10, 3]
    print(selection_short(lista))