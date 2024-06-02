
#4.1
lista1 = [1,2,2]
#función para sumar elementos de un array sin bucles.
def suma(array):
    total=0
    #caso base -->fin del bucle
    if(len(array)==1):
        return array[0]
    else:
        #continua el bucle
        total += array.pop(0)
        return total + suma(array)

#4.2
lista2 = [2,1,3]
#función para contar elementos de un array sin bucles.
def contarElementos(array):
    total =1
    #caso base
    if(len(array)==1):
        return 1
    else:
        #continua el bucle
        array.pop(0)
        return total + contar(array)

#4.3  
lista3 = [2,1,3]
#función para encontrar el maximo de un array sin bucles.
def maximo(array):
    #caso base
    if(len(array)==1):
        return array[0]
    else:
        actual=array.pop(0)
        if(actual< maximo(array)):
            return maximo(array)
        else:
            return actual
           

print(suma(lista1))
print(contar(lista2))
print(maximo(lista3))


