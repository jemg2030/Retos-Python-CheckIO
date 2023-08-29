"""
Our Robo-Trio need to train for future journeys and treasure hunts. Stephan has built a special
flat model of a pyramid. Now the robots can train for speed gold running. They start at the top
of the pyramid and must collect gold in each room, choose to take the left or right path and
continue down to the next level. To optimize their gold runs, Stephan need to know the maximum
amount of gold that can be collected in one run.

Consider a list of lists in which the first list has one integer and each consecutive list has
one more integer then the last. Such a list of lists would look like a pyramid. You should write
a program that will help Stephan find the highest possible sum on the most profitable route down
the pyramid. All routes down the pyramid involve stepping down and to the left or down and to the
right.

Tips: Think of each step down to the left as moving to the same index location or to the right as
one index location higher. Be very careful if you plan to use recursion here.

Input: A pyramid as a list of lists of integers.

Output: The maximum possible sum as an integer.

Examples:
assert (
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)
assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
    count_gold(
        [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
    )
    == 35
)

How it is used: this is a classical problem which shows you how to use dynamic programming.
This concept is a core component of many optimizations tasks.

Preconditions:
0 < len(pyramid) ≤ 20;
all(all(0 < x < 10 for x in row) for row in pyramid).

----------
----------

Nuestro Robotrío necesita entrenarse para futuros viajes y búsquedas del tesoro. Stephan
ha construido un modelo plano especial de una pirámide. Ahora los robots pueden entrenarse
para correr a toda velocidad en busca del oro. Empiezan en la cima de la pirámide y deben
recoger oro en cada habitación, elegir entre tomar el camino de la izquierda o el de la
derecha y seguir bajando hasta el siguiente nivel. Para optimizar sus carreras de oro,
Stephan necesita saber la cantidad máxima de oro que puede recoger en una carrera.

Considere una lista de listas en la que la primera lista tiene un número entero y cada lista
consecutiva tiene un número entero más que la última. Tal lista de listas tendría el aspecto
de una pirámide. Usted debe escribir un programa que ayudará a Stephan encontrar la suma más
alta posible en la ruta más rentable hacia abajo de la pirámide. Todas las rutas hacia abajo
de la pirámide implican un paso hacia abajo y hacia la izquierda o hacia abajo y hacia la
derecha.

Consejos: Piense en cada paso hacia la izquierda como un movimiento hacia la misma posición
de índice o hacia la derecha como una posición de índice más alta. Tenga mucho cuidado si
planea utilizar la recursividad aquí.

Entrada: Una pirámide como una lista de listas de enteros.

Salida: La suma máxima posible como un entero.

Ejemplos:
assert (
    cuenta_oro(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    cuenta_oro(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)
assert cuenta_oro([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
    cuenta_oro(
        [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
    )
    == 35
)

Cómo se utiliza: se trata de un problema clásico que muestra cómo utilizar la programación dinámica.
Este concepto es un componente básico de muchas tareas de optimización.

Precondiciones:
0 < len(pirámide) ≤ 20;
all(all(0 < x < 10 para x en fila) para fila en pirámide).
"""


def count_gold(pyramid: list[list[int]]) -> int:
    # replace this for solution
    n = len(pyramid)

    # Create a table to store the maximum sums
    max_sums = [[0] * (i + 1) for i in range(n)]

    # Initialize the last row of max_sums with the values from the bottom of the pyramid
    max_sums[-1] = pyramid[-1]

    # Starting from the second-to-last row, calculate the maximum sums
    for i in range(n - 2, -1, -1):
        for j in range(len(pyramid[i])):
            max_sums[i][j] = pyramid[i][j] + max(
                max_sums[i + 1][j], max_sums[i + 1][j + 1]
            )

    # The maximum possible sum is stored at the top of the pyramid
    return max_sums[0][0]


print("Example:")
print(
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
)

# These "asserts" are used for self-checking
assert (
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)
assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
    count_gold(
        [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
    )
    == 35
)
assert (
    count_gold(
        [
            [4],
            [3, 0],
            [5, 1, 1],
            [2, 0, 2, 0],
            [1, 1, 1, 8, 3],
            [5, 3, 4, 8, 2, 8],
            [1, 0, 5, 0, 4, 3, 1],
        ]
    )
    == 30
)
assert (
    count_gold(
        [
            [6],
            [7, 9],
            [3, 8, 3],
            [3, 4, 0, 2],
            [6, 9, 9, 6, 8],
            [3, 7, 0, 8, 2, 2],
            [0, 6, 3, 0, 0, 6, 7],
        ]
    )
    == 49
)
assert (
    count_gold(
        [
            [6],
            [0, 6],
            [3, 0, 7],
            [0, 4, 2, 9],
            [4, 4, 3, 6, 9],
            [3, 1, 0, 5, 9, 0],
            [8, 9, 7, 7, 3, 4, 5],
        ]
    )
    == 50
)
assert (
    count_gold(
        [
            [6],
            [6, 9],
            [7, 1, 4],
            [6, 9, 9, 7],
            [1, 6, 7, 9, 7],
            [5, 7, 2, 6, 0, 9],
            [1, 2, 2, 6, 0, 1, 6],
            [8, 5, 0, 3, 1, 4, 3, 1],
            [9, 6, 4, 1, 1, 9, 3, 7, 9],
            [5, 8, 4, 3, 5, 4, 5, 1, 8, 3],
        ]
    )
    == 66
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
