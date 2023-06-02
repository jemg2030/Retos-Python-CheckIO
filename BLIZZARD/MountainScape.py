'''
You are given the coordinates of the tops of the triangles as input values.

The slope angle is 45 degrees.
The base is always on the x-axis.
You must return the total area of all triangles. But count the overlapping areas only once.

NOTE:
The sum of the X and Y coordinates is always even. (e.g. (1, 3) (0, 2) ...)

Example:
mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37

Input: A list of a tuple of two integers.

Output: An integer.

Precondition:
0 ≤ x ≤ 100
1 ≤ y ≤ 50
(x+y) % 2 == 0
1 ≤ len(tops) ≤ 50

----------
----------

Se le dan las coordenadas de las cimas de los triángulos como valores de entrada.

El ángulo de inclinación es de 45 grados.
La base está siempre en el eje x.
Debe devolver el área total de todos los triángulos. Pero cuenta las áreas superpuestas sólo una vez.

NOTA:
La suma de las coordenadas X e Y es siempre par. (por ejemplo: (1, 3) (0, 2) ...)

Ejemplo:
paisaje_montaña([(1, 1), (4, 2), (7, 3)]) == 13
paisaje_montañoso([(0, 2), (5, 3), (7, 5)]) == 29
paisaje_montañoso([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37

Entrada: Una lista de una tupla de dos enteros.

Salida: Un entero.

Precondición:
0 ≤ x ≤ 100
1 ≤ y ≤ 50
(x+y) % 2 == 0
1 ≤ len(tops) ≤ 50
'''


from typing import List, Tuple
from operator import itemgetter


def mountain_scape(tops: List[Tuple[int, int]]) -> int:
    # your code here
    area = 0
    tops.sort(key=itemgetter(0))
    tops_copy = tops[:]
    for i in range(len(tops_copy)):
        x0, y0 = tops_copy[i]
        for j in range(i + 1, len(tops_copy)):
            x1, y1 = tops_copy[j]
            # next one contains previous one
            if x1 - y1 <= x0 - y0:
                try:
                    # remove previous one
                    tops.remove(tops_copy[i])
                except ValueError:
                    continue
            # previous one contains next one
            elif x1 + y1 < x0 + y0:
                try:
                    # remove next one
                    tops.remove(tops_copy[j])
                except ValueError:
                    continue

    for i in range(len(tops) - 1):
        x0, y0 = tops[i]
        x1, y1 = tops[i + 1]
        # if x1 - y1 >= x0 + y0 means both triangles don't intersect with each other
        a = (x0 + y0 if x1 - y1 >= x0 + y0 else x1 - y1) - (x0 - y0)
        area += a ** 2 / 4 + a * (y0 - a / 2)
    return area + tops[-1][1] ** 2


if __name__ == '__main__':
    print("Example:")
    print(mountain_scape([(1, 1), (4, 2), (7, 3)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
    assert mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
    assert mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37
    print("Coding complete? Click 'Check' to earn cool rewards!")
