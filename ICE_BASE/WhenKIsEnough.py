'''
Given a list of items, some of which may be duplicated, create and return a new Iterable that
is otherwise the same as items, but only up to k occurrences of each element are kept, and all
occurrences of that element after those first k are discarded. Note also the counterintuitive
but still completely legitimate edge case of k == 0 that has a well defined answer of an empty list!

Input: A list and an integer.

Output: List or another Iterable (tuple, iterator, generator).

Examples:
assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

This task is taken from the course CCPS 109 Computer Science I, as taught by Ilkka Kokkarinen.

----------
----------

Dada una lista de elementos, algunos de los cuales pueden estar duplicados, crea y devuelve
un nuevo Iterable que, por lo demás, es igual que los elementos, pero sólo se conservan
hasta k ocurrencias de cada elemento, y todas las ocurrencias de ese elemento después de
esas primeras k se descartan. Nótese también el caso contraintuitivo pero completamente
legítimo de k == 0, que tiene una respuesta bien definida: ¡una lista vacía!

Entrada: Una lista y un número entero.

Salida: Lista u otro Iterable (tupla, iterador, generador).

Ejemplos:
assert list(remove_after_kth([42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

Esta tarea está tomada del curso CCPS 109 Computer Science I, impartido por Ilkka Kokkarinen.
'''


from typing import Iterable, Any


def remove_after_kth(items: list[Any], k: int) -> Iterable[Any]:
    # your code here
    return []


print("Example:")
print(list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)))

# These "asserts" are used for self-checking
assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

print("The mission is done! Click 'Check Solution' to earn rewards!")
