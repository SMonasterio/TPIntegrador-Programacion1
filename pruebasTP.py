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

