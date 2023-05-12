'''
JABBERWOCKY

'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

'Beware the Jabberwock, my son!
The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
The frumious Bandersnatch!'

He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.

And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!

One, two! One, two! And through and through
The vorpal blade went snicker-snack!
He left it dead, and with its head
He went galumphing back.

'And hast thou slain the Jabberwock?
Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!'
He chortled in his joy.

'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

"Through the Looking-Glass." Lewis Carroll

DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?

"Puzzles from Wonderland." Lewis Carroll

Nicola has solved this puzzle (and I am sure that you will do equally well). To be prepared
for more such puzzles, Nicola wants to invent a method to search for words inside poetry.
You can help him create a function to search for certain words.

You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n).
Casing does not matter for your search, but whitespaces should be removed before your search.
You should find the word inside the rhyme in the horizontal (from left to right) or vertical
(from up to down) lines. For this you need envision the rhyme as a matrix (2D array). Find the
coordinates of the word in the cut rhyme (without whitespaces).

The result must be represented as a list -- [row_start,column_start,row_end,column_end], where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.
Counting of the rows and columns start from 1.
rhymes

Input: Two arguments. A rhyme as a string and a word as a string (lowercase).

Output: The coordinates of the word.

Example:
checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]

How it is used: This task shows the variance of the positional ciphers. With this cipher you can
hide a message within a book which allows you and receiver to send these coded messages.

Precondition: The word is given in lowercase
0 < |word| < 10
0 < |rhyme| < 300

----------
----------

JABBERWOCKY

'Twas brillig, and the slithy toves
Hicieron giro y gimble en el wabe;
Todo mimsy eran los borogoves,
Y los ratones mome outgrabe.

¡Cuidado con el Jabberwock, hijo mío!
¡Las mandíbulas que muerden, las garras que atrapan!
Cuidado con el pájaro Jubjub, y evitar
al frumoso Bandersnatch".

Tomó su espada vorpal en la mano:
Durante mucho tiempo buscó al enemigo...
Así descansó junto al árbol Tumtum,
y se quedó pensativo.

Y mientras reflexionaba..,
El Jabberwock, con ojos de fuego,
Vino silbando a través del bosque tulgey,
¡Y eructó mientras venía!

¡Uno, dos! ¡Uno, dos! Y a través y a través
¡La hoja vorpal fue snicker-snack!
Lo dejó muerto, y con su cabeza
Volvió galopando.

¿Y has matado al Jabberwock?
¡Ven a mis brazos, muchacho!
¡Frabioso día! ¡Callooh! Callay!
Se rió en su alegría.

'Twas brillig, and the slithy toves
Giraron y giraron en el agua;
Todos mimosos eran los borogoves,
Y los ratones mimosos se agarraban.

"A través del espejo". Lewis Carroll

Soñando con manzanas en una pared,
Y soñando a menudo, querida,
Soñé que, si las contaba todas,
-¿Cuántas aparecerían?

"Rompecabezas del País de las Maravillas". Lewis Carroll

Nicola ha resuelto este enigma (y estoy seguro de que tú lo harás igual de bien). Para estar preparado para más enigmas de este tipo, Nicola quiere inventar un método para buscar palabras dentro de la poesía. Puedes ayudarle a crear una función para buscar determinadas palabras.

Se le da una rima (una cadena de varias líneas), en la que las líneas están separadas por "nueva línea" (\n). Las mayúsculas y minúsculas no importan para su búsqueda, pero los espacios en blanco deben eliminarse antes de su búsqueda. Debe encontrar la palabra dentro de la rima en las líneas horizontales (de izquierda a derecha) o verticales (de arriba a abajo). Para ello, debe visualizar la rima como una matriz (matriz 2D). Encontrar las coordenadas de la palabra en la rima cortada (sin espacios en blanco).

El resultado debe representarse como una lista -- [fila_inicio,columna_inicio,fila_fin,columna_fin], donde

row_start es el número de línea para la primera letra de la palabra.
inicio_columna es el número de columna de la primera letra de la palabra.
row_end es el número de línea de la última letra de la palabra.
fin_columna es el número de columna de la última letra de la palabra.
El recuento de las filas y columnas empieza por 1.
rimas

Entrada: Dos argumentos. Una rima como cadena y una palabra como cadena (en minúsculas).

Salida: Las coordenadas de la palabra.

Ejemplo:
checkio(u"""SOÑANDO con manzanas en una pared,
Y soñando a menudo, querida,
Soñaba que, si las contaba todas,
-¿Cuántas aparecerían?"", "diez") == [2, 14, 2, 16]
checkio("""Tomó su espada vorpal en la mano:
Durante mucho tiempo buscó al enemigo...
Así que descansó junto al árbol Tumtum,
y se quedó pensativo.
Y como en uffish pensamiento se puso de pie,
El Jabberwock, con ojos de fuego,
Vino silbando a través del bosque tulgey,
Y eructó mientras venía!"", "noir") == [4, 16, 7, 16]

Cómo se utiliza: Esta tarea muestra la varianza de los cifrados posicionales. Con este cifrado puedes ocultar un mensaje dentro de un libro que te permite a ti y al receptor enviar estos mensajes codificados.

Condición previa: La palabra se da en minúsculas
0 < |palabra| < 10
0 < |rhyme| < 300
'''


from itertools import zip_longest


def checkio(text, word):
    horizontal = text.lower().replace(' ', '').splitlines()
    for i, row in enumerate(horizontal, 1):
        index = row.find(word)
        if index >= 0:
            return [i, index + 1, i, index + len(word)]

    vertical = [''.join(line) for line in zip_longest(*horizontal, fillvalue='-')]
    for i, col in enumerate(vertical, 1):
        index = col.find(word)
        if index >= 0:
            return [index + 1, i, index + len(word), i]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert (
        checkio(
            """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
            "ten",
        )
        == [2, 14, 2, 16]
    )
    assert (
        checkio(
            """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""",
            "noir",
        )
        == [4, 16, 7, 16]
    )
print("Coding complete? Click 'Check' to earn cool rewards!")
