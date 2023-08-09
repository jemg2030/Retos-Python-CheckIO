"""
A square on the two-dimensional plane can be defined as a tuple (x, y, l), where (x, y) are
the coordinates of its bottom left corner and l is the length of the side of the square (we
only consider squares that are aligned to the axes). Given two squares as tuples (x1, y1, l1)
and (x2, y2, l2), your function should determine whether these two squares intersect, that is,
their areas have at least one point in common, even if that one point is merely the shared corner
point when these two squares are placed kitty corner.

We also prepared a stick and a carrot for you:

try to write this mission with no loops or list comprehensions of any kind, but should compute
the result using only integer comparisons and conditional statements;

it is actually much easier to determine that the two squares do not intersect, and then negate
that answer. Two squares do not intersect if one of them ends in the horizontal direction before
the other one begins, or if the same thing happens in the vertical direction.

Input: Two tuples with three integers in each.

Output: Bool.

Examples:
assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False

This task is taken from the course CCPS 109 Computer Science I, as taught by Ilkka Kokkarinen.

----------
----------

Un cuadrado en el plano bidimensional puede definirse como una tupla (x, y, l), donde (x, y)
son las coordenadas de su esquina inferior izquierda y l es la longitud del lado del cuadrado
(sólo consideramos cuadrados que están alineados con los ejes). Dados dos cuadrados como tuplas
(x1, y1, l1) y (x2, y2, l2), tu función debe determinar si estos dos cuadrados se intersecan, es
decir, sus áreas tienen al menos un punto en común, incluso si ese único punto es simplemente el
punto de esquina compartido cuando estos dos cuadrados se colocan kitty corner.

También te hemos preparado un palo y una zanahoria:

intente escribir esta misión sin bucles ni comprensiones de lista de ningún tipo, sino que deberá
calcular el resultado utilizando únicamente comparaciones de enteros y sentencias condicionales;

en realidad es mucho más fácil determinar que los dos cuadrados no se intersecan, y luego negar esa
respuesta. Dos cuadrados no se intersecan si uno de ellos termina en la dirección horizontal antes de
que empiece el otro, o si ocurre lo mismo en la dirección vertical.

Entrada: Dos tuplas con tres enteros en cada una.

Salida: Bool.

Ejemplos:
assert cuadrado_intersec((2, 2, 3), (5, 5, 2)) == True
assert intersección_cuadrados((3, 6, 1), (8, 3, 5)) == False
assert intersección_cuadrados((3000, 6000, 1000), (8000, 3000, 5000)) == False

Esta tarea está tomada del curso CCPS 109 Computer Science I, impartido por Ilkka Kokkarinen.

https://github.com/ikokkari
"""


def squares_intersect(s1: tuple[int, int, int], s2: tuple[int, int, int]) -> bool:
    # your code here
    x1, y1, l1 = s1
    x2, y2, l2 = s2

    # Check if one square ends before the other begins in the horizontal direction
    if x1 + l1 < x2 or x2 + l2 < x1:
        return False

    # Check if one square ends before the other begins in the vertical direction
    if y1 + l1 < y2 or y2 + l2 < y1:
        return False

    # If the above conditions are not met, the squares intersect
    return True


print("Example:")
print(squares_intersect((2, 2, 3), (5, 5, 2)))

# These "asserts" are used for self-checking
assert squares_intersect((2, 2, 3), (5, 5, 2)) == True
assert squares_intersect((3, 6, 1), (8, 3, 5)) == False
assert squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
