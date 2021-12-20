'''

Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. It
has various units with a wide range of movement patterns allowing for a huge number of possible different game positions
(for example Number of possible chess games at the end of the n-th plies. ) For this mission, we will examine the
movements and behavior of chess pawns.

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted
with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the
chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission
we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front
of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row
number than the square they currently occupy.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this
strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have
several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are
safe.

pawns

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:
1 safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
2 safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

How it is used: For a game AI one of the important tasks is the ability to estimate game state. This concept will show
how you can do this on the simple chess figures positions.

Precondition:
0 < pawns ≤ 8

-----------
-----------

Casi todo el mundo conoce el antiguo juego del ajedrez y tiene al menos un conocimiento básico de sus reglas. En
tiene varias unidades con una amplia gama de patrones de movimiento que permiten un enorme número de posibles posiciones
de juego diferentes (por ejemplo, el número de partidas de ajedrez posibles al final de las n-ésimas. ) Para esta
misión, examinaremos los movimientos y el comportamiento de los peones de ajedrez.

El ajedrez es un juego de estrategia para dos jugadores que se juega en un tablero de ajedrez distribuido en ocho filas
(llamadas filas y denotadas con números del 1 al 8) y ocho columnas (llamadas filas y denotadas con letras de la a a la
h) de casillas. Cada casilla del tablero de ajedrez se identifica con un único par de coordenadas: una letra y un
número (por ejemplo, "a1", "h8", "d6"). Para esta misión sólo tenemos que preocuparnos de los peones. Un peón puede
capturar una pieza del adversario en una casilla en diagonal delante de él en una fila adyacente. de él en una fila
adyacente, moviéndose a esa casilla. Para los peones blancos las casillas delanteras son casillas con mayor número de
fila que la casilla que ocupan actualmente.

Un peón es generalmente una unidad débil, pero tenemos 8 de ellos que podemos utilizar para construir un muro de
defensa de peones. Con esta estrategia, un peón defiende a los demás. Un peón está a salvo si otro peón puede capturar
una unidad en esa casilla. Tenemos varios peones blancos en el tablero de ajedrez y sólo peones blancos. Debes diseñar
tu código para encontrar cuántos peones son seguros.

peones

Se te da un conjunto de coordenadas de casillas donde hemos colocado peones blancos. Debes contar cuántos peones son
seguros.

Entrada: Coordenadas de los peones colocados como un conjunto de cadenas.

Salida: El número de peones seguros como un entero.

Ejemplo:
1 peones_seguros({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
2 safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

Cómo se utiliza: Para una IA de juego una de las tareas importantes es la capacidad de estimar el estado de la partida.
Este concepto mostrará cómo se puede hacer esto en las posiciones de figuras de ajedrez simples.

Condición previa:
0 < peones ≤ 8

'''


def safe_pawns(pawns):
    if 0 < len(pawns) <= 8:
        cont = 0
        for elem in pawns:
            for pos, item in enumerate(elem):
                if pos == 0:
                    l1 = chr(ord(item) - 1)
                    l2 = chr(ord(item) + 1)
                else:
                    num = chr(ord(item) - 1)

            u1 = l1+num in pawns
            u2 = l2+num in pawns
            if u1 or u2 is True:
                cont += 1

        return cont
    else:
        return print("Invalid sequence to Run the program, try again")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
