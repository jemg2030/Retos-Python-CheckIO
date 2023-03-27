'''
Going up to the door you’ve noticed the case that was standing next to it - it was piled high with
the keys of all shapes and sizes. Yes, Lord Escher definitely loved puzzles and difficulties. When
you’ve attempted to open the door, you discovered with no particular surprise that it was closed.
Well, let's find the right key and move on.
As input you are getting two multi-line strings - one is a schematic image of the keyhole, the
second - of the key. Your task is to return True if the key fits the lock and False if otherwise.
The key and keyhole are represented by the '#' symbols, and '0' shows the empty space around the
key and the door material around the keyhole. Pay attention that the key and keyhole can be
displayed both vertically and horizontally.

Input: The key and lock representation as multilines string.

Output: True or False.

How it is used: To determine the correspondence of objects to each other.

Precondition :
size of key and lock <= 10x10

----------
----------

Al acercarse a la puerta se fijó en el maletín que había junto a ella, lleno de llaves de todas
las formas y tamaños. Sí, a Lord Escher le encantaban los rompecabezas y las dificultades. Cuando
intentaste abrir la puerta, descubriste sin sorpresa que estaba cerrada. Bueno, vamos a encontrar
la llave correcta y seguir adelante.
Como entrada recibes dos cadenas de varias líneas - una es una imagen esquemática del ojo de la
cerradura, la segunda - de la llave. Tu tarea es devolver True si la llave encaja en la cerradura
y False en caso contrario. La llave y el ojo de la cerradura están representados por los símbolos '
#', y '0' muestra el espacio vacío alrededor de la llave y el material de la puerta alrededor del ojo
de la cerradura. Preste atención a que la llave y el ojo de la cerradura pueden mostrarse tanto
vertical como horizontalmente.

Entrada: La representación de la llave y la cerradura como cadena multilínea.

Salida: Verdadero o Falso.

Cómo se utiliza: Para determinar la correspondencia de unos objetos con otros.

Condición previa :
tamaño de la llave y la cerradura <= 10x10
'''


def rotate_90_degrees(matrix):
    """Returns the matrix rotated 90 degrees clockwise."""
    return [''.join([line[::-1][i] for line in matrix]) for i in range(len(matrix[0]))]

def trim_matrix(matrix):
    """Returns a copy of the matrix with empty rows and columns removed."""
    while matrix and not '#' in matrix[0]:
        matrix = matrix[1:]
    while matrix and not '#' in matrix[-1]:
        matrix = matrix[:-1]
    while matrix and not any(row[0] == '#' for row in matrix):
        matrix = [row[1:] for row in matrix]
    while matrix and not any(row[-1] == '#' for row in matrix):
        matrix = [row[:-1] for row in matrix]
    return matrix

def keys_and_locks(lock, key):
    """Returns True if the key can unlock the lock by a series of moves, False otherwise."""
    lock_matrix = trim_matrix(lock.split())
    key_matrix = trim_matrix(key.split())
    for _ in range(4):
        if lock_matrix == key_matrix:
            return True
        key_matrix = rotate_90_degrees(key_matrix)
    return False


if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False

    print("Coding complete? Click 'Check' to earn cool rewards!")
