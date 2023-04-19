'''
Here goes the last task! All you’ve left to do is to remove the small force field that directly
surrounded the Hypercube and you are free to go home (unless, of course, there will be no unforeseen
difficulties).

There were several small cubes with the multi-colored sides laying around the cylinder which inclosed the
Hypercube. It’s highly possible that you need to use them somehow to remove the force field.
Your task is to return the maximum possible height of the tower built from the cubes in such a way that
each of four its side sides are of the same color (4 sides - 4 colors, each side has its own color).
Each cube is described by a string of 6 letters in capital Latin characters which represent the color
of the respective side (A — Azure, B — Blue, C — Cyan, G — Green, O — Orange, R — Red, S — Scarlet, V — Violet,
W — White, Y — Yellow).

The sides are numbered in the following order: front, right, left, back, top, bottom. A cube doesn’t
have two sides of the same color.
You may rotate each cube as you wish to build the tower.

Input: Array of the cubes descriptions.

Output: Maximum height of the tower.

Example:
tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']) == 3
tower(['ABCGYW', 'CAYRGO', 'OCYWBA', 'ACYVBR', 'GYVABW']) == 1

How it is used: For the geometry analysis.

Precondition :
2 <= number of cubes <= 10

----------
----------

¡Aquí va la última tarea! Todo lo que te queda por hacer es eliminar el pequeño campo de fuerza que
rodeaba directamente al Hipercubo y ya eres libre para irte a casa (a menos, por supuesto, que no
esté lleno de dificultades imprevistas).

Alrededor del cilindro que rodeaba el Hipercubo había varios cubos pequeños con las caras multicolores.
Es muy posible que necesites utilizarlos de alguna manera para eliminar el campo de fuerza.
Tu tarea es devolver la máxima altura posible de la torre construida con los cubos de tal manera que
cada uno de sus cuatro lados laterales sean del mismo color (4 lados - 4 colores, cada lado tiene su
propio color).
Cada cubo se describe mediante una cadena de 6 letras en mayúsculas latinas que representan el color del
lado respectivo (A - Azur, B - Azul, C - Cian, G - Verde, O - Naranja, R - Rojo, S - Escarlata, V - Violeta,
W - Blanco, Y - Amarillo).

Las caras se numeran en el siguiente orden: delante, derecha, izquierda, detrás, arriba, abajo. Un cubo no
tiene dos caras del mismo color.
Puedes rotar cada cubo como quieras para construir la torre.

Entrada: Matriz con las descripciones de los cubos.

Salida: Altura máxima de la torre.

Ejemplo:
torre(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']) == 3
tower(['ABCGYW', 'CAYRGO', 'OCYWBA', 'ACYVBR', 'GYVABW']) == 1

Cómo se utiliza: Para el análisis geométrico.

Precondición :
2 <= número de cubos <= 10
'''


from itertools import combinations, permutations


def check(cube):
    common = set(cube[0])
    for i in range(1, len(cube)):
        common = common & set(cube[i])
    if len(common) < 4:
        return False

    for i in combinations(common, 4):
        for (c1, c2, c3, c4) in permutations(i, 4):
            relationship = None
            if (set([cube[0].index(c1), cube[0].index(c2)]) in ({0, 3}, {1, 2}, {4, 5}) and
                    set([cube[0].index(c3), cube[0].index(c4)]) in ({0, 3}, {1, 2}, {4, 5})):
                relationship = [(c1, c2), (c3, c4)]
                break
        if not relationship:
            continue
        else:
            if all(set([j.index(c1), j.index(c2)]) in ({0, 3}, {1, 2}, {4, 5}) and
                   set([j.index(c3), j.index(c4)]) in ({0, 3}, {1, 2}, {4, 5}) for j in cube[1:]):
                return True

    return False


def tower(cubes):
    #replace this for solution
    n = len(cubes)
    while n > 1:
        for i in combinations(cubes, n):
            if check(i):
                return n
        n -= 1
    return 1


if __name__ == '__main__':
    print("Example:")
    print(tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']) == 3
    assert tower(['ABCGYW', 'CAYRGO', 'OCYWBA', 'ACYVBR', 'GYVABW']) == 1
    assert tower(['GYCABW', 'GYCABW', 'GYCABW', 'GYCABW', 'GYCABW']) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
