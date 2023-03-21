'''
Create and return a new Iterable that contains the same elements as the argument list items, but
with the reversed order of the elements inside every maximal strictly ascending subsequence. This
function should not modify the contents of the original list.

Input: List of integers.

Output: Iterable of integers.

Examples:
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []

How it is used: (math is used everywhere)

Precondition: List contains only integers.

The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of
Continuing Education by Ilkka Kokkarinen

----------
----------

Crea y devuelve un nuevo Iterable que contiene los mismos elementos que los elementos de la lista de
argumentos, pero con el orden invertido de los elementos dentro de cada subsecuencia máxima estrictamente
ascendente. Esta función no debe modificar el contenido de la lista original.

Entrada: Lista de enteros.

Salida: Iterable de enteros.

Ejemplos:
assert list(inversa_ascendente([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(inversa_ascendente([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(inversa_ascendente([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(inversa_ascendente([])) == []

Cómo se utiliza: (las matemáticas se usan en todas partes)

Condición previa: La lista contiene sólo enteros.

La misión fue tomada de Python CCPS 109 Otoño 2018. Está siendo impartido para la escuela de educación
continua Ryerson Chang por Ilkka Kokkarinen
'''


from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    # your code here
    result = []
    i = 0
    while i < len(items):
        start = i
        while i < len(items) - 1 and items[i] < items[i + 1]:
            i += 1
        end = i
        result += items[start:end + 1][::-1]
        i += 1
    return result


print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
