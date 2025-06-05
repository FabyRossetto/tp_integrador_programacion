# Análisis de Algoritmos en Python: Suma de Lista

## Proyecto

Este repositorio contiene el trabajo práctico sobre análisis de algoritmos realizado por Fabiana Rossetto y Federico Savastano para la materia Programación I. El objetivo principal es comprender y demostrar la importancia de la eficiencia algorítmica utilizando la notación BIG-O.

## Qué exploramos?

Comparamos dos enfoques para sumar todos los elementos de una lista de números enteros:

1.  **Suma Iterativa Manual:** Una implementación usando un bucle `for`.
2.  **Suma con `sum()` de Python:** Utilizando la función integrada altamente optimizada del lenguaje.

Ambos algoritmos, aunque teóricamente tienen una complejidad O(n), muestran diferencias drásticas en su rendimiento real, lo que subraya la importancia de las optimizaciones de bajo nivel en Python.

## Resultados Destacados

Nuestras pruebas empíricas revelaron que, para listas muy grandes (hasta 10 millones de elementos), la función `sum()` de Python es más rápida que la implementación manual. Esto ilustra cómo las funciones nativas y optimizadas del lenguaje pueden superar significativamente las implementaciones manuales, incluso para algoritmos con la misma complejidad asintótica.

## Video Explicativo

Hemos preparado un video donde explicamos en detalle los conceptos de análisis de algoritmos, nuestra metodología, el caso práctico, los resultados obtenidos y las conclusiones.

## Contenido del Repositorio

* `tp-integrador-programación.py`: El código fuente de los algoritmos y las mediciones de tiempo.
* `README.md`: Este archivo.