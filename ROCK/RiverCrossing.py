"""
'River crossing puzzle' is the famous classic puzzle. (also known as Wolf, goat and cabbage problem)

summary:
The farmer needs to carry wolf, goat and cabbage by boat across the river.
Only one can be loaded on the boat at a time.
Don't leave wolf and goat on the bank (wolf eats goat).
Don't leave goat and cabbage on the bank (goat eats cabbage).
This time, I will extend this puzzle a little. The number of wolves, goat, cabbages and payload is arbitrary.
(see precondition)

You are given four integers as the number of wolves, goats, cabbages and payload of the boat.
You have to return the minimum number of boat crossings required to carry all the loads.
(If not possible, return None.)

NOTE:
All loads can live together on the boat.

Example:
river_crossing(1, 1, 1, 1) == 7  # original
river_crossing(1, 1, 1, 2) == 3  # payload +1
river_crossing(2, 1, 1, 2) == 5  # payload +1, wolf +1
river_crossing(1, 2, 1, 1) is None  # impossible

Input: The number of wolves, goats, cabbages and payload (4 integers).

Output: The minimum number of the boat crossings (an integer).

Precondition:
1 ≤ wolves + goats + cabbages ≤ 10
1 ≤ payload ≤ 5

----------
----------

El 'Rompecabezas del cruce del río' es el famoso rompecabezas clásico.
(también conocido como Problema del lobo, la cabra y la col)


resumen:
El granjero tiene que llevar lobo, cabra y repollo en barca a través del río.
Sólo uno puede ser cargado en el barco a la vez.
No dejes al lobo y a la cabra en la orilla (el lobo se come a la cabra).
No dejes la cabra y la col en la orilla (la cabra se come la col).
Esta vez, voy a ampliar un poco este rompecabezas. El número de lobos, cabras, coles y carga es arbitrario.
(ver precondición)

Se te dan cuatro enteros como número de lobos, cabras, coles y carga útil del barco.
Tiene que devolver el número mínimo de travesías del barco necesarias para transportar
todas las cargas. (Si no es posible, devuelva Ninguno).

NOTA:
Todas las cargas pueden convivir en el barco.

Ejemplo:
river_crossing(1, 1, 1, 1) == 7 # original
river_crossing(1, 1, 1, 2) == 3 # carga +1
cruce_río(2, 1, 1, 2) == 5 # carga +1, lobo +1
river_crossing(1, 2, 1, 1) is None # imposible

Entrada: El número de lobos, cabras, coles y carga útil (4 enteros).

Salida: El número mínimo de cruces del barco (un entero).

Precondición:

1 ≤ lobos + cabras + coles ≤ 10
1 ≤ carga útil ≤ 5
"""


from collections import deque


def river_crossing(wolves, goats, cabbages, payload):
    W, G, C = 0, 1, 2
    banks = [(wolves, goats, cabbages), (0, 0, 0)]

    res = None
    used = set()
    que = deque([(0, banks)])
    while que:
        cnt, banks = que.popleft()
        side = cnt % 2

        if (side, banks[0]) in used:
            continue
        used.add((side, banks[0]))

        if sum(banks[0]) == 0 and side == 1:
            res = cnt
            break

        if (
            banks[1 - side][W] * banks[1 - side][G]
            or banks[1 - side][G] * banks[1 - side][C]
        ):
            continue

        for w in range(min(banks[side][W], payload) + 1):
            for g in range(min(banks[side][G], payload - w) + 1):
                for c in range(min(banks[side][C], payload - w - g) + 1):
                    n_banks = [None] * 2
                    n_banks[side] = tuple(
                        v1 - v2 for v1, v2 in zip(banks[side], [w, g, c])
                    )
                    n_banks[1 - side] = tuple(
                        v1 + v2 for v1, v2 in zip(banks[1 - side], [w, g, c])
                    )
                    que.append((cnt + 1, n_banks))

    return res


if __name__ == "__main__":
    print("Example:")
    print(river_crossing(1, 1, 1, 1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert river_crossing(1, 1, 1, 1) == 7, "original"
    assert river_crossing(1, 1, 1, 2) == 3, "payload +1"
    assert river_crossing(2, 1, 1, 2) == 5, "payload +1, wolf +1"
    assert river_crossing(1, 2, 1, 1) is None, "impossible"
    print("Coding complete? Click 'Check' to earn cool rewards!")
