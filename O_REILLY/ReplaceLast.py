'''
In a given list the last element should become the first one. An empty list or list with only one element
should stay the same

Input: List.

Output: Iterable (tuple, generator, Iterator ...).

Example:
assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []

---------
---------

En una lista dada, el último elemento debe convertirse en el primero. Una lista vacía o con un solo
elemento debe permanecer igual

Entrada: Lista.

Salida: Iterable (tupla, generador, Iterador ...).

Ejemplo:
assert lista(reemplazar_última([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []
'''


from typing import Iterable


def replace_last(line: list) -> Iterable:
    # your code here
    if len(line) <= 1:
        yield from line
    else:
        yield line[-1]
        yield from line[:-1]


print("Example:")
print(list(replace_last([2, 3, 4, 1])))

assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
