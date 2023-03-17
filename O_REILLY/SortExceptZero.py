'''
Sort the integers in a list. But the position of zeros should not be changed.

Input: A list of integers.

Output: A list or another Iterable (tuple, generator, iterator) of integers.

Examples:
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]

Precondition:
All numbers are positive.

----------
----------

Ordena los números enteros de una lista. Pero no se debe cambiar la posición de los ceros.

Entrada: Una lista de enteros.

Salida: Una lista u otro Iterable (tupla, generador, iterador) de enteros.

Ejemplos:
assert list(excepto_cero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(excepto_cero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(excepto_cero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(excepto_cero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]

Precondición:
Todos los números son positivos.
'''


from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    # your code here
    # First, we extract the positions of the zeros
    zero_positions = [i for i, num in enumerate(items) if num == 0]
    # Next, we remove the zeros from the list
    items_without_zeros = [num for num in items if num != 0]
    # We sort the list without zeros
    sorted_items = sorted(items_without_zeros)
    # Finally, we insert the zeros back into their original positions
    for pos in zero_positions:
        sorted_items.insert(pos, 0)
    return sorted_items


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
