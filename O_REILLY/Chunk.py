'''
You have a lot of work to do, so you might want to split it into smaller pieces. This way you'll know
which piece you'll do on Monday, which will be for Tuesday and so on.

Split a list into smaller lists of the same size (chunks). The last chunk can be smaller than the default
chunk-size. If the list is empty, then you shouldn't have any chunks at all.

Input: Two arguments. A List and chunk size.

Output: An Iterable with chunked Iterable.

Example:
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []

Precondition: chunk-size > 0

----------
----------

Tienes mucho trabajo por hacer, así que te conviene dividirlo en trozos más pequeños. Así sabrás qué
trozo harás el lunes, cuál será para el martes y así sucesivamente.

Divide una lista en listas más pequeñas del mismo tamaño (trozos). El último trozo puede ser más pequeño
que el tamaño de trozo por defecto. Si la lista está vacía, entonces no deberías tener ningún trozo.

Entrada: Dos argumentos. Una lista y un tamaño de trozo.

Salida: Un Iterable con chunked Iterable.

Ejemplo:
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []

Requisito: chunk-size > 0
'''


from collections.abc import Iterable


def chunking_by(items: list[int], size: int) -> Iterable[list[int]]:
    # your code here
    if not items:
        return []
    return (items[i:i + size] for i in range(0, len(items), size))


print("Example:")
print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

# These "asserts" are used for self-checking
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []
assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]

print("The mission is done! Click 'Check Solution' to earn rewards!")
