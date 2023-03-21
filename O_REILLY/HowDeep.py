'''
You are given a tuple that consists of integers and other tuples, which in turn can also contain tuples.

Your task is to find out how deep this structure is or how deep the nesting of these tuples is.

For example, in the (1, 2, 3) tuple the depth of nesting is 1. And in the (1, 2, (3,)) tuple the depth of
nesting is 2, since one of the elements of the first tuple is also a tuple. And in the (1, 2, (3, (4,)))
tuple the depth of nesting is 3, since one of the elements of the first tuple is a tuple, but since inside
it contains another tuple, it increases the depth by one, so the nesting depth turns out to be 3.

It’s important to note that an empty tuple also increases the depth of the structure, that is, () - indicates
the nesting depth 1, ((),) - indicates the nesting depth 2.

Input: Tuple of tuples of tuples...of integers.

Output: Integer.

Examples:
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1

Precondition: Given iterables have to be well founded.

----------
----------

Se le da una tupla que consta de enteros y otras tuplas, que a su vez también pueden contener tuplas.

Tu tarea consiste en averiguar la profundidad de esta estructura o la profundidad de anidamiento de estas tuplas.

Por ejemplo, en la tupla (1, 2, 3) la profundidad de anidamiento es 1. Y en la tupla (1, 2, (3,)) la profundidad
de anidamiento es 2, ya que uno de los elementos de la primera tupla es también una tupla. Y en la tupla
(1, 2, (3, (4,))) la profundidad de anidamiento es 3, ya que uno de los elementos de la primera tupla es una
tupla, pero como dentro contiene otra tupla, aumenta la profundidad en uno, por lo que la profundidad de
anidamiento resulta ser 3.

Es importante tener en cuenta que una tupla vacía también aumenta la profundidad de la estructura, es decir, () -
indica la profundidad de anidamiento 1, ((),) - indica la profundidad de anidamiento 2.

Entrada: Tupla de tuplas de tuplas...de enteros.

Salida: Entero.

Ejemplos:
assert como_profundo((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert profundidad(()) == 1

Precondición: Los iterables dados tienen que estar bien fundamentados.
'''


def how_deep(structure: tuple) -> int:
    # your code here
    if not structure:
        return 1
    depths = []
    for element in structure:
        if isinstance(element, int):
            continue
        else:
            depths.append(how_deep(element) + 1)
    if depths:
        return max(depths)
    else:
        return 1


print("Example:")
print(how_deep((1, 2, 3)))

# These "asserts" are used for self-checking
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1
assert how_deep(((),)) == 2
assert how_deep((((),),)) == 3
assert how_deep((1, (2,), (3,))) == 2
assert how_deep((1, ((),), (3,))) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
