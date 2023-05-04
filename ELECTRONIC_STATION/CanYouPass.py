'''
If you have solved the "How to find friends" mission, then you already know how to check for the existence of
a path in graphs. Let's try to add something more to that problem.

You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value. The
matrix consists of digits. You may move to neighbouring cells either horizontally or vertically provided the
values of the origin and destination cells are equal. You should determine if a path exists between two given
cells.

A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two
numbers: row and column. The result should be any value which can be converted into a boolean. If a path
exists, then return True. Return False if there is none.

Input: Three arguments. A matrix as a tuple of tuples with integers, first and second cell coordinates
as tuples of two integers.

Output: The existence of a path between two given cells as a boolean or a value that can be converted to
boolean.

Example:
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 2), (0, 5)) == True, 'First example'
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 3), (6, 0)) == False,

How it is used: Sometimes we don't need the full pathfinding algorithms implementation and can use
simplified realisation of these algorithms. It can be an useful skill to find a simple ways.

Precondition:
1 < len(matrix) ≤ 10
all(1 < len(row) ≤ 10 for row in matrix)
all(all(0 ≤ x < 10 for x in row) for row in matrix)
matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
first != second

----------
----------

Si has completado la misión "¿Cómo encontrar amigos?" , entonces ya sabes cómo comprobar la existencia
de una ruta ( path ) en grafos. Tratemos de añadir algo más a ese problema.

Se te dará una matriz (array 2D) y las coordenadas (fila y columna) de dos celdas con el mismo valor.
La matriz se compone de dígitos y puedes mover a las celdas vecinas ya sea horizontal o verticalmente,
siempre y cuando los valores de las celdas de origen y destino sean iguales. Deberás determinar si existe
una ruta entre las dos celdas indicadas.

Una matriz se representa como una tupla de tuplas con dígitos. Las coordenadas se representan como una tupla
con dos números: fila y columna. El resultado deberá ser cualquier valor que pueda convertirse en un valor
lógico ( bool ). Si existe la ruta, deberás regresar "Verdadero" ( True ); de otra forma deberás regresar
"Falso" ( False ).

Datos de Entrada: Tres argumentos. Una matriz como una tupla de tuplas con enteros ( int ); y las
coordenadas de la primera y segunda celda, como tuplas de dos enteros ( int ).

Salida: La existencia de una ruta ( path ) entre las dos celdas, como un valor booleano ( bool ) o como
cualquier valor que puede ser convertido a booleano.

Ejemplo:
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 2), (0, 5)) == True, 'First example'
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 3), (6, 0)) == False,

¿Cómo se usa?: A veces no es necesario implementar por completo los algoritmos de búsqueda de rutas
( pathfinding ) sino que podemos usar una versión simplificada. Esta habilidad puede ser útil para
encontrar alternativas más simples.

Condiciones:
1 < len(matrix) ≤ 10
all(1 < len(row) ≤ 10 for row in matrix)
all(all(0 ≤ x < 10 for x in row) for row in matrix)
matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
first != second
'''


def can_pass(matrix, first, second):
    visited = set()  # keep track of visited cells

    def dfs(cell):
        if cell == second:
            return True
        visited.add(cell)
        row, col = cell
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r, c = row + dr, col + dc
            if (r, c) in visited:
                continue
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == matrix[row][col]:
                if dfs((r, c)):
                    return True
        return False

    return dfs(first)


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
