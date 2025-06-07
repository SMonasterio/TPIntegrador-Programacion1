import random
import timeit

# Ejercicio 1: Búsqueda Lineal
def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en la lista.
    Recorre elemento por elemento hasta encontrar el objetivo.
    Ventaja: funciona en listas desordenadas.
    Desventaja: ineficiente para listas grandes.
    """
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  # Devuelve el índice donde se encontró el objetivo
    return -1  # No encontrado

# Ejercicio 2: Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.
    Divide la lista en mitades hasta encontrar el objetivo.
    Ventaja: muy rápida en listas grandes ordenadas.
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
    return -1  # No encontrado

# Ejercicio 3: Bubble Sort
def bubble_sort(lista):
    """
    Ordena la lista usando el algoritmo de burbuja.
    Compara elementos adyacentes y los intercambia si están en el orden incorrecto.
    Ventaja: fácil de implementar.
    Desventaja: muy lento para listas grandes.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejercicio 4: Insertion Sort
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

# Ejercicio 5: Selection Sort
def selection_sort(lista):
    """
    Ordena la lista usando el algoritmo de selección.
    Selecciona el mínimo de la lista y lo coloca en su lugar, iterativamente.
    Ventaja: fácil de entender.
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

# Ejercicio 6: Quicksort
def quicksort(lista):
    """
    Ordena la lista usando el algoritmo quicksort (divide y conquista).
    Elige un pivote y divide la lista en dos sublistas recursivamente.
    Ventaja: muy eficiente para listas grandes.
    Desventaja: rendimiento variable dependiendo del pivote.
    """
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

# Ejercicio 7: Comparación de tiempos de búsqueda
def comparar_busquedas(lista, objetivo):
    """
    Compara los tiempos de ejecución de búsqueda lineal y binaria.
    """
    # Para búsqueda binaria, la lista debe estar ordenada
    lista_ordenada = sorted(lista)

    tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(lista, objetivo), number=100)
    tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(lista_ordenada, objetivo), number=100)

    print(f"Búsqueda lineal: {tiempo_lineal:.6f} segundos (100 elementos)")
    print(f"Búsqueda binaria: {tiempo_binaria:.6f} segundos (100 elementos)")

# Ejercicio 8: Comparación de tiempos de ordenamiento
def comparar_ordenamientos(lista):
    """
    Compara los tiempos de ejecución de los algoritmos de ordenamiento.
    Usa timeit para medir el tiempo de cada algoritmo.
    """
    lista1 = lista.copy()
    lista2 = lista.copy()
    lista3 = lista.copy()
    lista4 = lista.copy()

    tiempo_bubble = timeit.timeit(lambda: bubble_sort(lista1), number=1)
    tiempo_insertion = timeit.timeit(lambda: insertion_sort(lista2), number=1)
    tiempo_selection = timeit.timeit(lambda: selection_sort(lista3), number=1)
    tiempo_quick = timeit.timeit(lambda: quicksort(lista4), number=1)

    print(f"Bubble Sort: {tiempo_bubble:.6f} segundos")
    print(f"Insertion Sort: {tiempo_insertion:.6f} segundos")
    print(f"Selection Sort: {tiempo_selection:.6f} segundos")
    print(f"Quicksort: {tiempo_quick:.6f} segundos")

# Ejercicio 9: Pruebas con listas pequeñas y grandes
def pruebas():
    """
    Realiza pruebas con listas pequeñas (20 elementos) y grandes (1000 elementos).
    Muestra los resultados de las búsquedas y ordenamientos.
    """
    print("Pruebas con listas pequeñas (20 elementos):")
    lista_pequena = random.sample(range(100), 20)
    objetivo = lista_pequena[10]
    comparar_busquedas(lista_pequena, objetivo)
    comparar_ordenamientos(lista_pequena)

    print("\nPruebas con listas grandes (1000 elementos):")
    lista_grande = random.sample(range(10000), 1000)
    objetivo = lista_grande[500]
    comparar_busquedas(lista_grande, objetivo)
    comparar_ordenamientos(lista_grande)

if __name__ == "__main__":
    pruebas()