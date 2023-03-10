'''
Not all of the elements are important. What you need to do here is to remove all of the elements
after the given one from list.

For illustration, we have a list [1, 2, 3, 4, 5] and we need to remove all the elements that go after
3 - which is 4 and 5.

We have two edge cases here:

if a cutting element cannot be found, then the list shouldn't be changed;
if the list is empty, then it should remains empty.
Input: List of integers and the border element integer.

Output: List or other Iterable (tuple, iterator, generator ...) of integers.

Examples:
assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]

----------
----------

No todos los elementos son importantes. Lo que hay que hacer aquí es eliminar de la lista todos los
elementos después del dado.

Por ejemplo, tenemos una lista [1, 2, 3, 4, 5] y tenemos que eliminar todos los elementos que van después de
3 - que es 4 y 5.

Aquí tenemos dos casos extremos

si un elemento de corte no se puede encontrar, entonces la lista no debe ser cambiado;
si la lista está vacía, entonces debe permanecer vacía.
Entrada: Lista de enteros y el elemento frontera entero.

Salida: Lista u otro Iterable (tupla, iterador, generador ...) de enteros.

Ejemplos:
assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
'''


from collections.abc import Iterable


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    # your code here
    try:
        index = items.index(border)
        return items[:index + 1]
    except ValueError:
        return items
    except IndexError:
        return []


print("Example:")
print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking
assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_after([], 0)) == []
assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]

print("The mission is done! Click 'Check Solution' to earn rewards!")
