"""
You are given a list of integers. Your function should return the number of elements, which
are not at their places as if the list would be sorted ascending. For example, for the sequence
[1, 1, 4, 2, 1, 3] the result is 3, since elements at indexes 2, 4, 5 (remember about 0-based
indexing in Python) are not at their places as in the same sequence sorted ascending -
[1, 1, 1, 2, 3, 4].

Input: List of integers (int).

Output: Integer (int).

Examples:
assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0

----------
----------

Se le da una lista de enteros. Tu función debe devolver el número de elementos que no
están en su lugar como si la lista estuviera ordenada de forma ascendente. Por ejemplo,
para la secuencia [1, 1, 4, 2, 1, 3] el resultado es 3, ya que los elementos en los índices
2, 4, 5 (recuerde acerca de la indexación basada en 0 en Python) no están en sus lugares como
en la misma secuencia ordenada ascendentemente - [1, 1, 1, 2, 3, 4].

Entrada: Lista de enteros (int).

Salida: Entero (int).

Ejemplos:
assert no_orden([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0
"""


def not_order(data: list[int]) -> int:
    # your code here
    if not data:
        return 0

    sorted_nums = sorted(data)
    misplaced_count = 0

    for i in range(len(data)):
        if data[i] != sorted_nums[i]:
            misplaced_count += 1

    return misplaced_count


print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

# These "asserts" are used for self-checking
assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
