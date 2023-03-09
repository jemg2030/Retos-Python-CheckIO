'''
Not all of the elements are important. What you need to do here is to remove from the list all of the
elements before the given one.

For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 -
which is 1 and 2.

We have two edge cases here: (1) if a cutting element cannot be found, then the list shoudn't be changed.
(2) if the list is empty, then it should remain empty.

Input: List and the border element.

Output: Iterable (tuple, list, iterator ...).

Example:
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]

----------
----------

No todos los elementos son importantes. Lo que hay que hacer aquí es eliminar de la lista todos
los elementos anteriores al dado.

Para la ilustración tenemos una lista [1, 2, 3, 4, 5] y necesitamos eliminar todos los elementos que van
antes del 3 - que son el 1 y el 2.

Aquí tenemos dos casos extremos (1) si un elemento de corte no se puede encontrar, entonces la lista no
debe ser cambiado. (2) si la lista está vacía, entonces debe permanecer vacía.

Entrada: Lista y el elemento de corte.

Salida: Iterable (tupla, lista, iterador ...).

Ejemplo:
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
'''


from collections.abc import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    try:
        index = items.index(border)
        return items[index:]
    except ValueError:
        return items


print("Example:")
print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_before([], 0)) == []
assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
