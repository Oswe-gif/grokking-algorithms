#devuelve el index del array del elemento a buscar haciendo uso de una busqueda binaria
def busqueda_binaria(array, elemento):
    rangoMenor = 0
    rangoMayor = len(array)
    numeroDeOperaciones=1
    while rangoMenor != rangoMayor:
        index= int((rangoMayor+rangoMenor)/2)
        print('pasos',numeroDeOperaciones)
        numeroDeOperaciones +=1
        if(elemento == array[index]):
            return index
        if(array[index] > elemento):
            rangoMayor = index
        else:
            rangoMenor = index

listaOrdenada = [1,2,3,4,5,6]

print("El elemento esta en el index", busqueda_binaria(listaOrdenada, 5))

#el algoritmo tiene una complejidad de O(log n) -->Cantidad de operaciones o tiempo de ejecución en el peor caso, se evidencia en la variable de "numeroDeOperaciones"
            
        
        
    
    
