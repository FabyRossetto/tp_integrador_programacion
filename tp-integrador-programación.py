
import time
import random

# --- Algoritmo 1: Suma Iterativa Manual (O(n)) ---
def suma_iterativa_manual(lista):
    """
    Suma todos los elementos de una lista usando un bucle for.
    """
    total = 0 # 1 operación (inicialización)
    for elemento in lista: # n iteraciones
        total += elemento # 2 operaciones (suma y asignación)
    return total # 1 operación

# Análisis Teórico (Suma Iterativa Manual):
# T(n) = 1 (inicialización) + n * 2 (bucle) + 1 (retorno) = 2n + 2
# Big-O: O(n)

# --- Algoritmo 2: Suma con Función sum() de Python (O(n) optimizado) ---
def suma_con_funcion_sum(lista):
    """
    Suma todos los elementos de una lista usando la función sum() de Python.
    Internamente es altamente optimizada 
    """
    return sum(lista) # 1 operación (llamada a función y cálculo interno)

# Análisis Teórico (Suma con función sum()):
# La función sum() de Python, aunque conceptualmente también recorre la lista (O(n)),
# está implementada en C, lo que la hace extremadamente rápida y eficiente.
# A nivel de "operaciones Python", es una sola llamada, pero su costo real depende de n.
# Su Big-O sigue siendo O(n), pero con una constante muy pequeña.


# --- Función para medir el tiempo de ejecución ---
def medir_tiempo(funcion, lista):
    """
    Mide el tiempo de ejecución de una función y retorna el resultado y el tiempo en milisegundos.
    """
    inicio = time.time()
    resultado = funcion(lista)
    fin = time.time()
    return resultado, (fin - inicio) * 1000 # Tiempo en milisegundos

if __name__ == "__main__":
    print("Iniciando análisis de algoritmos para sumar elementos de una lista...")

    # Tamaños de lista para la prueba
    # Usaremos valores que crecen exponencialmente para ver el impacto
    tamanios_n = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

    resultados_manual = []
    resultados_sum_func = []

    for n in tamanios_n:
        # Generar una lista de números aleatorios para la prueba
        lista_prueba = [random.randint(1, 100) for _ in range(n)]

        # Medir Suma Iterativa Manual
        _, tiempo_manual = medir_tiempo(suma_iterativa_manual, lista_prueba)
        resultados_manual.append(tiempo_manual)

        # Medir Suma con función sum()
        _, tiempo_sum_func = medir_tiempo(suma_con_funcion_sum, lista_prueba)
        resultados_sum_func.append(tiempo_sum_func)

        print(f"\n--- Para n = {n:,} ---")
        print(f"Tiempo Suma Iterativa Manual: {tiempo_manual:.8f} ms")
        print(f"Tiempo Suma con sum(): {tiempo_sum_func:.8f} ms")
