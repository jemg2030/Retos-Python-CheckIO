'''
In this mission you must count chains.

You are given a list of details of the circle (tuple of X-coordinate, Y-coordinate, radius).
You have to return the number of groups of circles where their circumferences intersect.

NOTE:

Only one circle counts as one group.

Example:

count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2
count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1
count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4

Input:

A list of details of the circle.
Details of the circle is a tuple of three integers(X-coordinate, Y-coordinate, radius).
Output: An integer.

Precondition:
-10 ≤ x(, y) coordinate ≤ 10
1 ≤ radius ≤ 10

----------
----------

En esta misión debes contar cadenas.

Se te da una lista de detalles del círculo (tupla de coordenada X, coordenada Y, radio).
Tienes que devolver el número de grupos de círculos donde se cruzan sus circunferencias.

NOTA:

Sólo un círculo cuenta como un grupo.

Ejemplo:

contar_cadenas([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2
count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1
cuenta_cadenas([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4

Entrada:

Una lista de detalles del círculo.
Los detalles del círculo son una tupla de tres enteros (coordenada X, coordenada Y, radio).
Salida: Un entero.

Precondición:
-10 ≤ coordenada x(, y) ≤ 10
1 ≤ radio ≤ 10
'''


from typing import List, Tuple
from math import hypot


def intersect(circ1, circ2):
    distance = hypot(circ1[0] - circ2[0], circ1[1] - circ2[1])
    return distance < circ1[2] + circ2[2] and not (distance + circ1[2] <= circ2[2] or distance + circ2[2] <= circ1[2])


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    # your code here
    chains = []
    # check which chains intersect with it.
    for circ in circles:
        newchain = [circ]
        nonconnected_chains = []
        for chain in chains:
            if any(intersect(c, circ) for c in chain):
                newchain += chain
            else:
                nonconnected_chains.append(chain)
        chains = [newchain] + nonconnected_chains

    return len(chains)


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    assert count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
