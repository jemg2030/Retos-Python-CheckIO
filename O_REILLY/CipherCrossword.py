'''
Everyone has tried solving a crossword puzzle at some point in their lives. We're going to mix things
up by adding a cipher to the classic puzzle. A cipher crossword replaces the clues for each entry with
clues for each white cell of the grid. These clues are integers ranging from 1 to 26, inclusive. The
objective, as any other crossword, is to determine the proper letter for each cell. In a cipher crossword,
the 26 numbers serve as a cipher for those letters: cells that share matching numbers are filled with
matching letters, and no two numbers stand for the same letter. All resulting entries must be valid words.

For this task you should solve the cipher crossword. You are given a crossword template as a list of
lists (2D array) with numbers (from 0 to 26), where 0 is a blank cell and other numbers are encrypted
letters. You will be given a list of words for the crossword puzzle. You should fill that template with
a given word and return the solved crossword as a list of lists with letters. Blank cells are replaced
with whitespaces (0 => " ").

The words are placed in rows and columns with NO diagonals. The crossword contains six words with 5
letters each. These words are placed in a grid.

Input: The Cipher Crossword as a list of lists with integers. Words as a list of strings.

Output: The solution to the Crossword as a list of lists with letters.

Examples:
assert checkio(
    [
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6],
    ],
    ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
) == [
    ["h", "e", "l", "l", "o"],
    ["a", " ", "e", " ", "z"],
    ["b", "i", "m", "b", "o"],
    ["i", " ", "m", " ", "n"],
    ["t", "r", "a", "c", "e"],
]
assert checkio(
    [
        [19, 26, 8, 25, 18],
        [24, 0, 24, 0, 8],
        [4, 24, 23, 21, 3],
        [3, 0, 26, 0, 13],
        [8, 6, 15, 17, 13],
    ],
    ["world", "rings", "tache", "water", "racon", "dress"],
) == [
    ["w", "o", "r", "l", "d"],
    ["a", " ", "a", " ", "r"],
    ["t", "a", "c", "h", "e"],
    ["e", " ", "o", " ", "s"],
    ["r", "i", "n", "g", "s"],
]

How it is used: This is a type of restriction problem. You have rules and should try to find a
combination that conforms to these rules. This concept can help you to solve scheduling conflicts
and - a situation where you would encounter many variables and restrictions, among other things.

Preconditions:
|crossword| = 5x5;
∀ x ∈ crossword : 1 ≤ x ≤ 26.

----------
----------

Todo el mundo ha intentado resolver un crucigrama en algún momento de sus vidas, pero nosotros vamos
a complicar las cosas un poco, adicionando un sistema de cifrado al juego clásico. Un crucigrama cifrado
reemplaza las pistas para cada entrada con pistas para cada casilla blanca de la cuadrícula. Estas pistas
son números enteros de 1 a 26, inclusive. El objetivo, como con cualquier otro crucigrama, es determinar la
letra correcta para cada celda. En un crucigrama cifrado, los 26 números se utilizan para codificar las
letras de la siguiente forma: las celdas que comparten un mismo número se rellenan con la misma letra, y no
existen dos números que representen la misma letra. Todos los resultados deben ser palabras válidas en inglés.

Para esta misión deberás resolver el crucigrama cifrado. Se te dará la plantilla del crucigrama como una lista
de listas (array 2D) con números (de 0 a 26), donde 0 es una celda en blanco y los otros números representan
letras codificadas. Se te proporcionará también una lista de palabras para el crucigrama. Deberás llenar la
plantilla con las palabras entregadas, y devolver el crucigrama resuelto, como una lista de listas con letras.
Las celdas en blanco se sustituyen por espacios en blanco (0 => " ").

Las palabras se colocan en filas y columnas, NUNCA en diagonales. El crucigrama contiene seis palabras con
cinco letras cada una. Las palabras se ubican sobre una cuadrícula.

Datos de Entrada: Un crucigrama cifrado como una lista de listas con enteros (int); y las palabras a utilizar,
como una lista de cadenas (str).

Salida: La solución del crucigrama, como una lista de listas con letras.

Ejemplo:
assert checkio(
    [
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6],
    ],
    ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
) == [
    ["h", "e", "l", "l", "o"],
    ["a", " ", "e", " ", "z"],
    ["b", "i", "m", "b", "o"],
    ["i", " ", "m", " ", "n"],
    ["t", "r", "a", "c", "e"],
]
assert checkio(
    [
        [19, 26, 8, 25, 18],
        [24, 0, 24, 0, 8],
        [4, 24, 23, 21, 3],
        [3, 0, 26, 0, 13],
        [8, 6, 15, 17, 13],
    ],
    ["world", "rings", "tache", "water", "racon", "dress"],
) == [
    ["w", "o", "r", "l", "d"],
    ["a", " ", "a", " ", "r"],
    ["t", "a", "c", "h", "e"],
    ["e", " ", "o", " ", "s"],
    ["r", "i", "n", "g", "s"],
]

¿Cómo se usa?: Este es un ejemplo de problemas con restricciones, en donde se te indican algunas reglas
y debes tratar de encontrar una combinación que se ajuste a dichas reglas. Este concepto puede ayudar,
por ejemplo, a resolver conflictos con horarios - una situación común en la que se encuentran muchas
variables y restricciones- entre otras cosas.

Condiciones:
|crossword| = 5x5;
∀ x ∈ crossword : 1 ≤ x ≤ 26.
'''


from itertools import chain, permutations


def checkio(crossword: list[list[int]], words: list[str]) -> list[list[str]]:
    # your code here
    flattened = crossword[0::2] + list(map(list, zip(*crossword)))[0::2]
    flattened = list(chain.from_iterable(flattened))
    expected = len(set(chain.from_iterable(words)))
    placement = [set(zip(flattened, chain.from_iterable(w))) for w in permutations(words)]
    placement = [{k: v for k, v in p} for p in placement if len(p) == expected][0]
    return [[placement[x] if x else ' ' for x in row] for row in crossword]


print("Example:")
print(
    checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6],
        ],
        ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
    )
)

# These "asserts" are used for self-checking
assert checkio(
    [
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6],
    ],
    ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
) == [
    ["h", "e", "l", "l", "o"],
    ["a", " ", "e", " ", "z"],
    ["b", "i", "m", "b", "o"],
    ["i", " ", "m", " ", "n"],
    ["t", "r", "a", "c", "e"],
]
assert checkio(
    [
        [19, 26, 8, 25, 18],
        [24, 0, 24, 0, 8],
        [4, 24, 23, 21, 3],
        [3, 0, 26, 0, 13],
        [8, 6, 15, 17, 13],
    ],
    ["world", "rings", "tache", "water", "racon", "dress"],
) == [
    ["w", "o", "r", "l", "d"],
    ["a", " ", "a", " ", "r"],
    ["t", "a", "c", "h", "e"],
    ["e", " ", "o", " ", "s"],
    ["r", "i", "n", "g", "s"],
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
