import random
import timeit

def busqueda_lineal(lista, objetivo):
    """
    Recorre la lista desde el primer elemento hasta el ultimo.
    Si encuentra el elemento buscado, devuelve su indice.
    Si no lo encuentra, devuelve -1.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    """
    Realiza una busqueda binaria en una lista ordenada.
    Divide la lista en mitades hasta encontrar el objetivo.
    Ventaja: muy rapida en listas grandes ordenadas.
    Desventaja: requiere lista ordenada.
    """
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def bubble_sort(lista):
    """
    Ordena la lista usando el algoritmo de burbuja.
    Compara elementos adyacentes y los intercambia si estan en el orden incorrecto.
    Ventaja: facil de implementar.
    Desventaja: muy lento para listas grandes.
    """
    
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista

def insertion_sort(lista):
    """
    Ordena la lista usando el algoritmo de inserción.
    Inserta cada elemento en su posición correcta dentro de la lista ordenada.
    Ventaja: eficiente en listas pequeñas o casi ordenadas.
    Desventaja: ineficiente en listas grandes.
    """
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def selection_sort(lista):
    """
    Ordena la lista usando el algoritmo de selección.
    Selecciona el mínimo de la lista y lo coloca en su lugar, iterativamente.
    Ventaja: facil de entender.
    Desventaja: lento para listas largas.
    """
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def quicksort(lista):
    """
    Ordena la lista usando el algoritmo quicksort.
    Elige un pivote y divide la lista en dos sublistas recursivamente.
    """
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

def comparar_busquedas(lista, objetivo):
    """
    Compara los tiempos de ejecucion de busqueda lineal y binaria.
    """
    #Ordenamos la lista usando el metodo sorted
    lista_ordenada = sorted(lista)
    
    print(f"\nEjecutando Búsqueda Lineal:")
    print(f"Lista enviada a búsqueda lineal: {lista}")
    indice_lineal = busqueda_lineal(lista, objetivo)
    print(f"Resultado de búsqueda lineal (índice): Objetivo {objetivo} encontrado en el indice {indice_lineal}")

    print(f"Ejecutando Búsqueda Binaria:")
    print(f"Lista enviada a búsqueda binaria: {lista_ordenada}")
    indice_binaria = busqueda_binaria(lista_ordenada, objetivo)
    print(f"Resultado de búsqueda binaria (índice): Objetivo {objetivo} encontrado en el indice  {indice_binaria}")

    #Le enviamos a timeit una funcion anonima(lambda) 
    #para que mida el tiempo que tarda en ejecutarse la funcion de busqueda lineal y binaria.
    #El segundo parametro de timeit es para que ejecuta la funciona anonima una X cantidad de veces.
    tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(lista, objetivo), number=1)
    tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(lista_ordenada, objetivo), number=1)
    
    print(f"\nAlgoritmo de busqueda comparacion")
    print(f"Búsqueda lineal: {tiempo_lineal:.6f} segundos")
    print(f"Búsqueda binaria: {tiempo_binaria:.6f} segundos\n")

def comparar_ordenamientos(lista):
    """
    Compara los tiempos de ejecucion de los algoritmos de ordenamiento.
    Usa timeit para medir el tiempo de cada algoritmo.
    """
    lista1 = lista.copy()
    lista2 = lista.copy()
    lista3 = lista.copy()
    lista4 = lista.copy()
    
    print(f"Ejecutando Bubble Sort:")
    print(f"Lista enviada a bubbleSort: {lista1}")
    lista_ordenada_1 = bubble_sort(lista1)
    print(f"Lista ordenada con bubbleSort: {lista_ordenada_1}")
    
    print(f"Ejecutando Insertion Sort")
    print(f"Lista enviada a Insertion Sort: {lista2}")
    lista_ordenada_2 = insertion_sort(lista2)
    print(f"Lista ordenada con Insertion Sort: {lista_ordenada_2}")
    
    print(f"Ejecutando Selection Sort")
    print(f"Lista enviada a Selection Sort: {lista3}")
    lista_ordenada_3 = selection_sort(lista3)
    print(f"Lista ordenada con Selection Sort: {lista_ordenada_3}")
    
    print(f"Ejecutando Quicksort")
    print(f"Lista enviada a Quicksort: {lista4}")
    lista_ordenada_4 = quicksort(lista4)
    print(f"Lista ordenada con Quicksort: {lista_ordenada_4}")

    tiempo_bubble = timeit.timeit(lambda: bubble_sort(lista1), number=1)
    tiempo_insertion = timeit.timeit(lambda: insertion_sort(lista2), number=1)
    tiempo_selection = timeit.timeit(lambda: selection_sort(lista3), number=1)
    tiempo_quick = timeit.timeit(lambda: quicksort(lista4), number=1)
    
    print(f"\nAlgoritmos de ordenamiento comparacion")
    print(f"Bubble Sort: {tiempo_bubble:.6f} segundos")
    print(f"Insertion Sort: {tiempo_insertion:.6f} segundos")
    print(f"Selection Sort: {tiempo_selection:.6f} segundos")
    print(f"Quicksort: {tiempo_quick:.6f} segundos")

def pruebas():
    """
    Realiza pruebas con listas pequeñas (20 elementos) y grandes (1000 elementos).
    Muestra los resultados de las busquedas y ordenamientos.
    """
    
    print("Pruebas con listas pequeñas (10 elementos):")
    
    # random.sample crea una lista de 10 numeros aleatorios distintos entre 0 y 99
    lista_pequena = random.sample(range(100), 10)
    objetivo = lista_pequena[5]
    
    # llamamos a comparar busquedas y le pasamos la lista de 10 elementos unicos y el objetivo
    comparar_busquedas(lista_pequena, objetivo)
    comparar_ordenamientos(lista_pequena)

    print("\nPruebas con listas grandes (1000 elementos):")
    
    lista_grande = random.sample(range(10000), 1000)
    objetivo_grande = lista_grande[100]
    
    comparar_busquedas(lista_grande, objetivo_grande)
    comparar_ordenamientos(lista_grande)

if __name__ == "__main__":
    pruebas()