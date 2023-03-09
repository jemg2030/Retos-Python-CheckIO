'''
In a given list the first element should become the last one. An empty list or list with only one
element should stay the same.

Input: List.

Output: Iterable.

Example:
assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

----------
----------

En una lista dada, el primer elemento debe convertirse en el último. Una lista vacía o con un solo elemento debe permanecer igual.

Entrada: Lista.

Salida: Iterable.

Ejemplo:
assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []
'''


from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) <= 1:  # If empty or only 1 element
        return items
    else:
        return items[1:] + [items[0]]


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
