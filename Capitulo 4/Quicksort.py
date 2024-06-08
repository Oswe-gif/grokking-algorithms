#el peor caso toma O(n*n), pero el caso promedio es de O(n log n).
#El otro algoritmo es merge sort el cual tiene un tiempo O(n log n)
#Pero muchas veces es mejor usar el quicksort porque la constante de tiempo tiende a ser menor y en la practica tiende a ser más rapido.
def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[int(len(array)/2)]
    menores = [i for i in array if i < pivot]
    mayores = [i for i in array if i > pivot]

    return quicksort(menores) + [pivot] + quicksort(mayores)

print(quicksort([10,5,2,3,1]))
