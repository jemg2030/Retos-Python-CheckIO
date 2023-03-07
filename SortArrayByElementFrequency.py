'''
Sort the given list so that its elements should be grouped and those groups end up in the decreasing
frequency order, that is, the number of times element appears in list. If two elements have the same
frequency, their groups should end up in the same order as the first appearance of element in the list.

If you want to practice more with the similar case, try Frequency Sorting mission.

Input: List

Output: List or another Iterable (tuple, iterator, generator)

Examples:
assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]

How it is used: For analyzing data using mathematical statistics and mathematical analysis, and for
finding trends and predicting future changes (systems, phenomena, etc.)

Precondition:
elements can be ints or strings
The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of
Continuing Education by Ilkka Kokkarinen

---------
---------

Ordena la lista dada de modo que sus elementos se agrupen y esos grupos terminen en el orden de
frecuencia decreciente, es decir, el número de veces que el elemento aparece en la lista. Si dos
elementos tienen la misma frecuencia, sus grupos deben terminar en el mismo orden que la primera
aparición del elemento en la lista.

Si quieres practicar más con un caso similar, prueba la misión Ordenación por frecuencia.

Entrada: Lista

Salida: Lista u otro Iterable (tupla, iterador, generador)

Ejemplos:
assert list(frecuencia_sorteo([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frecuencia_orden([4, 6, 2, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob"
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frecuencia_sorteo([17, 99, 42])) == [17, 99, 42]

Cómo se utiliza: Para analizar datos mediante estadística matemática y análisis matemático, y para
encontrar tendencias y predecir cambios futuros (sistemas, fenómenos, etc.)

Condición previa:
los elementos pueden ser ints o cadenas
La misión fue tomada de Python CCPS 109 Otoño 2018. Está siendo impartida para la escuela de educación
continua Ryerson Chang por Ilkka Kokkarinen
'''


from typing import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    # your code here
    return items


print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

# These "asserts" are used for self-checking
assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
