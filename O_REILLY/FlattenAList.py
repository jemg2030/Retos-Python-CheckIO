'''
Nicola likes to categorize all sorts of things. He categorized a series of numbers and as the
result of his efforts, a simple sequence of numbers became a deeply-nested list. Sophia and
Stephan don't really understand his organization and need to figure out what it all means.
They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which may contain yet more lists
and integers which then… you get the idea. You should put all of the integer values into one flat
list. The order should be as it was in the original list with string representation from left to right.

We need to hide this program from Nikola by keeping it small and easy to hide. Because of this,
your code should be shorter than 140 characters (with whitespaces).

Input: A nested list of integers.

Output: List or another Iterable (tuple, generator, iterator) of integers.

Examples:
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

How it is used: This concept is useful for parsing and analyzing files with complex structures and
the task challenges your creativity in writing short code.

Preconditions:
0 ≤ |array| ≤ 100;
∀ x ∈ array : -232 < x < 232 or x is a list;
depth < 10.

----------
----------

A Nicola le gusta categorizar todo tipo de cosas. Categoriza una serie de números y, como resultado de
sus esfuerzos, una simple secuencia de números se convierte en una lista profundamente anidada. Sophia y
Stephan no entienden muy bien su organización y necesitan averiguar qué significa todo esto. Necesitan tu
ayuda para entender la loca lista de Nikolas.

Hay una lista que contiene enteros u otras listas anidadas que pueden contener aún más listas y enteros
que luego... ya te haces una idea. Deberías poner todos los valores enteros en una lista plana. El orden
debe ser como estaba en la lista original con la representación de cadena de izquierda a derecha.

Necesitamos esconder este programa de Nikola manteniéndolo pequeño y fácil de esconder. Debido a esto, su
código debe ser más corto que 140 caracteres (con espacios en blanco).

Entrada: Una lista anidada de enteros.

Salida: Lista u otro Iterable (tupla, generador, iterador) de enteros.

Ejemplos:
assert lista(lista_plana([1, 2, 3])) == [1, 2, 3]
assert list(lista_plana([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
assert list(lista_plana([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(lista_plana([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

Cómo se utiliza: Este concepto es útil para parsear y analizar archivos con estructuras complejas y
la tarea desafía tu creatividad para escribir código corto.

Precondiciones:
0 ≤ |array| ≤ 100;
∀ x ∈ array : -232 < x < 232 o x es una lista;
'''


from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    # your code here
    return eval("["+str(array).replace("[","").replace("]","")+"]")


print("Example:")
print(list(flat_list([1, 2, 3])))

# These "asserts" are used for self-checking
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
