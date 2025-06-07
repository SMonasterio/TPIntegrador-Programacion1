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

