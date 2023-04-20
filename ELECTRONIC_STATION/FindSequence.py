'''
“There’s nothing here...” sighed Nikola.

“You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” Said

Sofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.

“Where did you get-”

“Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.

CLUNK

“Hey we hit something.” Stephen exclaimed in surprise.

“It’s the treasure!” Sofia was jumping up and down in excitement.

The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia
tried grabbing the lid but it was locked. Nikola studied the locking mechanism.

“I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is
a sequence of 4 or more matching numbers and output a bool.”

“Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.

You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits.
The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence
Input: A matrix as list of lists with integers.

Output: Whether or not a sequence exists as a boolean.

Examples:
assert checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
assert checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) == False
assert (
    checkio(
        [
            [2, 1, 1, 6, 1],
            [1, 3, 2, 1, 1],
            [4, 1, 1, 3, 1],
            [5, 5, 5, 5, 5],
            [1, 1, 3, 1, 1],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [7, 1, 1, 8, 1, 1],
            [1, 1, 7, 3, 1, 5],
            [2, 3, 1, 2, 5, 1],
            [1, 1, 1, 5, 1, 4],
            [4, 6, 5, 1, 3, 1],
            [1, 1, 9, 1, 2, 1],
        ]
    )
    == True
)

How it is used: This concept is useful for games where you need to detect various lines of the same
elements (match 3 games for example). This algorithm can be used for basic pattern recognition.

Preconditions:
0 ≤ len(matrix) ≤ 10;
all(all(0 < x < 10 for x in row) for row in matrix).

----------
----------

"Aquí no hay nada..." suspiró Nikola.

"Estás de broma, ¿verdad? ¡Todo tesoro es un tesoro enterrado! Si no, no sería un tesoro". Dijo

Sofía. "Toma, coge esto". Sacó tres palas de una mochila que pareció aparecer de la nada.

"¿De dónde sacaste..."

"No hagas preguntas. Sólo cava". Ella saltó en la pala y comenzó a cavar furiosamente.

CLUNK

"Hey le dimos a algo". Stephen exclamó sorprendido.

"¡Es el tesoro!" Sofía saltaba de emoción.

El trío escarbó alrededor del cofre del tesoro y lo sacó del agujero y le limpió la suciedad. Sofía
intentó agarrar la tapa, pero estaba cerrada. Nikola estudió el mecanismo de cierre.

"He visto este tipo de cerradura antes. Es bastante sencillo. Sólo tenemos que registrar si hay una
secuencia de 4 o más números iguales y sacar un bool".

"Bastante fácil. Abramos a este mamón". Sofía temblaba de emoción.

Te dan una matriz de NxN (4≤N≤10). Debes registrar si hay una secuencia de 4 o más dígitos iguales. La
secuencia puede colocarse horizontal, vertical o diagonalmente (diagonales NO-SE o NE-SO).

buscar-secuencia
Entrada: Una matriz como lista de listas con enteros.

Salida: Si existe o no una secuencia como booleano.

Ejemplos:
assert checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
assert checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) == False
assert (
    checkio(
        [
            [2, 1, 1, 6, 1],
            [1, 3, 2, 1, 1],
            [4, 1, 1, 3, 1],
            [5, 5, 5, 5, 5],
            [1, 1, 3, 1, 1],
        ]
    )
    == Verdadero
)
assert (
    checkio(
        [
            [7, 1, 1, 8, 1, 1],
            [1, 1, 7, 3, 1, 5],
            [2, 3, 1, 2, 5, 1],
            [1, 1, 1, 5, 1, 4],
            [4, 6, 5, 1, 3, 1],
            [1, 1, 9, 1, 2, 1],
        ]
    )
    == Verdadero
)

Cómo se utiliza: Este concepto es útil para juegos en los que es necesario detectar varias líneas
de los mismos elementos (juegos de tres en raya, por ejemplo). Este algoritmo puede utilizarse para
el reconocimiento básico de patrones.

Precondiciones:
0 ≤ len(matriz) ≤ 10;
all(all(0 < x < 10 para x en fila) para fila en matriz).
'''


def checkio(matrix: list[list[int]]) -> bool:
    # replace this for solution
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            # check horizontal sequence
            if j + 3 < n and matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2] == matrix[i][j + 3]:
                return True
            # check vertical sequence
            if i + 3 < n and matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j]:
                return True
            # check diagonal (NW-SE) sequence
            if i + 3 < n and j + 3 < n and matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == \
                    matrix[i + 3][j + 3]:
                return True
            # check diagonal (NE-SW) sequence
            if i + 3 < n and j - 3 >= 0 and matrix[i][j] == matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == \
                    matrix[i + 3][j - 3]:
                return True
    return False


print("Example:")
print(checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]))

# These "asserts" are used for self-checking
assert checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
assert checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) == False
assert (
    checkio(
        [
            [2, 1, 1, 6, 1],
            [1, 3, 2, 1, 1],
            [4, 1, 1, 3, 1],
            [5, 5, 5, 5, 5],
            [1, 1, 3, 1, 1],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [7, 1, 1, 8, 1, 1],
            [1, 1, 7, 3, 1, 5],
            [2, 3, 1, 2, 5, 1],
            [1, 1, 1, 5, 1, 4],
            [4, 6, 5, 1, 3, 1],
            [1, 1, 9, 1, 2, 1],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [2, 6, 2, 2, 7, 6, 5],
            [3, 4, 8, 7, 7, 3, 6],
            [6, 7, 3, 1, 2, 4, 1],
            [2, 5, 7, 6, 3, 2, 2],
            [3, 4, 3, 2, 7, 5, 6],
            [8, 4, 6, 5, 2, 9, 7],
            [5, 8, 3, 1, 3, 7, 8],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [1, 7, 6, 1, 8, 5, 1],
            [7, 9, 1, 7, 2, 8, 6],
            [5, 1, 4, 5, 8, 8, 3],
            [8, 6, 3, 9, 7, 6, 9],
            [9, 8, 9, 8, 6, 8, 2],
            [1, 7, 2, 4, 9, 3, 8],
            [9, 9, 8, 6, 9, 2, 6],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [6, 9, 1, 1, 6, 2],
            [5, 9, 7, 8, 2, 5],
            [2, 1, 1, 7, 9, 8],
            [1, 8, 1, 4, 7, 4],
            [7, 8, 5, 4, 5, 1],
            [6, 4, 8, 8, 1, 8],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [2, 7, 6, 2, 1, 5, 2, 8, 4, 4],
            [8, 7, 5, 8, 9, 2, 8, 9, 5, 5],
            [5, 7, 7, 7, 4, 1, 1, 2, 6, 8],
            [4, 6, 6, 3, 2, 7, 6, 6, 5, 1],
            [2, 6, 6, 9, 8, 5, 5, 6, 7, 7],
            [9, 4, 1, 9, 1, 3, 7, 2, 3, 1],
            [5, 1, 4, 3, 6, 5, 9, 3, 4, 1],
            [6, 5, 5, 1, 7, 7, 8, 2, 1, 1],
            [9, 5, 7, 8, 2, 9, 2, 6, 9, 3],
            [8, 2, 5, 7, 3, 7, 3, 8, 6, 2],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [1, 9, 7, 8, 9, 3, 6, 5, 6, 2],
            [4, 9, 4, 8, 3, 4, 8, 8, 5, 9],
            [2, 8, 5, 5, 7, 8, 6, 1, 3, 6],
            [6, 4, 7, 6, 9, 1, 4, 5, 7, 8],
            [4, 7, 7, 9, 8, 8, 8, 8, 4, 4],
            [3, 7, 3, 2, 1, 9, 1, 8, 9, 1],
            [4, 7, 2, 4, 8, 1, 2, 3, 6, 2],
            [4, 4, 1, 3, 3, 3, 9, 2, 6, 7],
            [8, 6, 1, 9, 3, 5, 8, 1, 7, 5],
            [7, 3, 6, 5, 3, 6, 6, 4, 8, 2],
        ]
    )
    == True
)
assert checkio([[1, 6, 1, 7], [4, 7, 3, 6], [3, 5, 7, 9], [8, 6, 6, 9]]) == False
assert (
    checkio(
        [
            [1, 2, 4, 6, 3],
            [2, 5, 2, 6, 3],
            [8, 7, 5, 9, 5],
            [2, 1, 1, 4, 3],
            [4, 2, 7, 5, 1],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [2, 3, 6, 5, 6, 2, 8, 3, 7, 4],
            [6, 9, 5, 9, 7, 6, 8, 5, 1, 6],
            [6, 8, 2, 6, 1, 9, 3, 6, 6, 4],
            [5, 8, 3, 2, 3, 8, 7, 4, 6, 4],
            [2, 3, 1, 4, 5, 1, 2, 5, 6, 9],
            [5, 4, 8, 7, 5, 5, 8, 4, 9, 5],
            [9, 7, 9, 9, 5, 9, 9, 8, 1, 2],
            [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
            [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
            [4, 8, 1, 4, 5, 8, 8, 7, 4, 7],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [7, 7, 4, 4, 8],
            [7, 4, 5, 5, 6],
            [6, 6, 5, 2, 8],
            [6, 2, 3, 8, 4],
            [6, 1, 3, 1, 2],
        ]
    )
    == False
)
assert (
    checkio(
        [
            [7, 9, 1, 7, 6, 7, 5, 9, 6],
            [5, 5, 9, 3, 1, 6, 7, 4, 7],
            [1, 7, 5, 2, 3, 1, 6, 4, 7],
            [2, 2, 2, 8, 7, 2, 6, 6, 9],
            [5, 6, 4, 2, 6, 7, 3, 4, 7],
            [5, 5, 6, 4, 9, 4, 3, 1, 7],
            [7, 3, 2, 3, 2, 4, 4, 7, 3],
            [3, 6, 9, 7, 2, 5, 6, 2, 5],
            [4, 1, 3, 9, 4, 2, 4, 8, 4],
        ]
    )
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
