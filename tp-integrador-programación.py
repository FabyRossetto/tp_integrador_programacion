import time
import random

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Generar lista de 10 millones de elementos
lista = sorted(random.sample(range(100_000_000), 10_000_000))
objetivo = lista[5000000]  # Elemento en la mitad

# Medir tiempo búsqueda lineal
inicio = time.time()
busqueda_lineal(lista, objetivo)
fin = time.time()
print(f"Búsqueda lineal: {fin - inicio:.5f} segundos")

# Medir tiempo búsqueda binaria
inicio = time.time()
busqueda_binaria(lista, objetivo)
fin = time.time()
print(f"Búsqueda binaria: {fin - inicio:.5f} segundos")
