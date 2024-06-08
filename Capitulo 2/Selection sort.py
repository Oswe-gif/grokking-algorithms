#Ordenar lista de mayor a menor
#toma un tiempo de O(nxn) porque itera todo el array en cada bucle.
lista=[1,2,3,4]
def selectionSort(array):
    listaOrdenada=[]
    while len(array) != 0:
        mayor = array[0]
        for i in array:
            if(mayor < i):
                mayor = i
        listaOrdenada.append(mayor)
        array.remove(mayor)
    return listaOrdenada

print(selectionSort(lista))
            
