'''
You have to split a given list into two lists inside an Iterable. If input sequence has an odd amount of elements,
then the first list inside result Iterable should have more elements. If input sequence has no elements, then two
empty lists inside result Iterable should be returned.

Input: A list.

Output: An Iterable of two lists.

Examples:
assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"],
]
assert list(split_list([1])) == [[1], []]

---------
---------

Tienes que dividir una lista dada en dos listas dentro de un Iterable. Si la secuencia de entrada tiene un número
impar de elementos, entonces la primera lista dentro del Iterable resultante debería tener más elementos. Si la
secuencia de entrada no tiene elementos, entonces se devolverán dos listas vacías dentro del Iterable resultante.

Entrada: Una lista.

Salida: Un Iterable de dos listas.

Ejemplos:
assert lista(lista_partida([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["plátano", "manzana", "naranja", "cereza", "sandía"])) == [
    ["plátano", "manzana", "naranja"],
    ["cereza", "sandía"],
]
assert list(split_list([1])) == [[1], []]
'''


from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    # your code here
    midpoint = (len(items) + 1) // 2
    return items[:midpoint], items[midpoint:]


print("Example:")
print(list(split_list([1, 2, 3, 4, 5, 6])))

assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"],
]
assert list(split_list([1])) == [[1], []]
assert list(split_list([])) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
