'''
As soon as the buttons were pressed in the correct order, the floor beneath you swiftly broke apart and
you fell into a deeper level of the dungeon. This castle still hasn’t ceased to surprise you! Fortunately,
you didn’t hurt yourself during the fall, otherwise you could’ve forget about ever going home.

Standing up and sorting yourself out, you saw a door which looked as if an unimaginable treasure was hidden
behind it - massive, metal, and despite the past centuries without a single spot of rust. There were two
options - it was either made of stainless steel, or all these years someone carefully looked after it. You
would very much like the first option to be true. One encounter with a ghost was quite enough.

This door didn’t have anything even remotely resembling a keyhole. But there was a small field, suspiciously
similar to the touch screen with dots. It resembled a lock that requires drawing of a certain pattern to be
unlocked. Where could such technologies come from in the old castle?! Hundreds of different ideas raced through
your mind, one crazier than the other. But all of this can wait until you are on the way home. The priority
now is to open this door.

As soon as you’ve touched the screen, each point turned into a digit. Probably, you need to draw some kind of
an unlock pattern here. Except… On what principle to choose the digits?
Your task is to write a function that accepts a set of digits (a two-dimensional array) as an argument,
and then returns the sum of the digits on the direction from the upper-left corner to the lower right so
that the sum is maximum. At the same time, you can visit no more than N points, taking into account the
first and the last one. You can move in any of the 8 directions (horizontally, vertically and diagonally).

Input: array of numbers, length of the path.

Output: the sum of the numbers on the path.

Example:
g_key([[1, 6, 7, 2, 4],
       [0, 4, 9, 5, 3],
       [7, 2, 5, 1, 4],
       [3, 3, 2, 2, 9],
       [2, 6, 1, 4, 0]], 9) == 46

How it is used: For the pathfinding.

Precondition :
2x2 <= grid size <= 5x5

----------
----------

En cuanto pulsaste los botones en el orden correcto, el suelo se rompió y caíste en un nivel más profundo
de la mazmorra. ¡Este castillo aún no ha dejado de sorprenderte! Afortunadamente, no te has hecho daño
durante la caída, de lo contrario podrías haberte olvidado de volver a casa.

Levantándote y ordenándote, viste una puerta que parecía esconder tras de sí un tesoro inimaginable: maciza,
metálica y, a pesar de los siglos transcurridos, sin una sola mancha de óxido. Había dos opciones: o era de
acero inoxidable, o todos estos años alguien la había cuidado con esmero. Le gustaría mucho que la primera
opción fuera cierta. Un encuentro con un fantasma era suficiente.

Esta puerta no tenía nada ni remotamente parecido a un ojo de cerradura. Pero había un pequeño campo,
sospechosamente similar a la pantalla táctil con puntos. Se parecía a una cerradura que requiere dibujar
un cierto patrón para ser desbloqueado. ¡¿De dónde podrían venir tales tecnologías en el viejo castillo?!
Cientos de ideas diferentes pasaron por tu mente, una más loca que la otra. Pero todo esto puede esperar
hasta que estés de camino a casa. La prioridad ahora es abrir esta puerta.

En cuanto tocas la pantalla, cada punto se convierte en un dígito. Probablemente, usted necesita para dibujar
algún tipo de un patrón de desbloqueo aquí. Excepto... ¿Sobre qué principio elegir los dígitos?
Tu tarea es escribir una función que acepte un conjunto de dígitos (una matriz bidimensional) como argumento, y
luego devuelva la suma de los dígitos en la dirección de la esquina superior izquierda a la inferior derecha,
de modo que la suma sea máxima. Al mismo tiempo, no puede visitar más de N puntos, teniendo en cuenta el primero
y el último. Puede moverse en cualquiera de las 8 direcciones (horizontal, vertical y diagonal).

Entrada: array de números, longitud del camino.

Salida: la suma de los números del camino.

Ejemplo:
g_key([[1, 6, 7, 2, 4],
       [0, 4, 9, 5, 3],
       [7, 2, 5, 1, 4],
       [3, 3, 2, 2, 9],
       [2, 6, 1, 4, 0]], 9) == 46

Cómo se utiliza: Para el pathfinding.

Precondición :
2x2 <= tamaño de la cuadrícula <= 5x5
'''



import numpy as np
from copy import deepcopy


def g_key(grid, path):
    #replace this for solution
    row = len(grid)
    column = len(grid[0])

    # special case
    if path == row * column:
        temp = 0
        for i in grid:
            temp += sum(i)
        return temp

    # dfs
    def route(s, x, y, step, record):
        if step > path - 1 or max(row - 1 - x, column - 1 - y) > path - 1 - step:
            return []
        else:
            if x == row - 1 and y == column - 1:
                if step == path - 1:
                    return [s]
                else:
                    return []
            else:
                temp_list = []
                for (dx, dy) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if x + dx >= 0 and x + dx < row and y + dy >= 0 and y + dy < column and (
                    not record[(x + dx, y + dy)]):
                        temp_record = deepcopy(record)
                        temp_record[(x + dx, y + dy)] = 1
                        temp_list += route(s + grid[x + dx][y + dy], x + dx, y + dy, step + 1, temp_record)

                return temp_list

    record = np.zeros((row, column), dtype=int)
    record[(0, 0)] = 1
    temp = route(grid[0][0], 0, 0, 0, record)
    return max(temp)


if __name__ == '__main__':
    print("Example:")
    print(g_key([[1, 6, 7, 2, 4],
                 [0, 4, 9, 5, 3],
                 [7, 2, 5, 1, 4],
                 [3, 3, 2, 2, 9],
                 [2, 6, 1, 4, 0]], 9))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert g_key([[1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9) == 46

    assert g_key([[2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]], 6) == 27

    assert g_key([[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]], 25) == 75

    assert g_key([[1, 6],
                  [5, 1]], 2) == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")
