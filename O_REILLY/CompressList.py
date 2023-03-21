'''
A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one
after another, there should be only one in the result Iterable (list, tuple, iterator, generator).

Input: A list.

Output: "Compressed" List or another Iterable (tuple, iterator, generator).

Examples:
assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []

----------
----------

Una lista dada debe ser "comprimida" de forma que, en lugar de dos (o más) elementos iguales,
quedando uno detrás de otro, sólo haya uno en el resultado Iterable (lista, tupla, iterador, generador).

Entrada: Una lista.

Salida: Lista "comprimida" u otro Iterable (tupla, iterador, generador).

Ejemplos:
assert list(comprimir([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(comprimir([])) == []
'''


from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    # your code here
    """Compress iterable by removing consecutive duplicates."""
    last_item = None
    for item in items:
        if item != last_item:
            yield item
        last_item = item


print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

# These "asserts" are used for self-checking
assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []
assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]

print("The mission is done! Click 'Check Solution' to earn rewards!")
