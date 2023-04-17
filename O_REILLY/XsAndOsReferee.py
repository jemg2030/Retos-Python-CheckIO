'''
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking
the spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical,
or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of
a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure
to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as list of strings (unicode).

Output: "X", "O" or "D" as a string.

Examples:
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

How it is used: The concepts in this task will help you when iterating data types. They can also be used in
game algorithms, allowing you to know how to check results.

Preconditions:
there is either one winner or a draw;
len(game_result) == 3;
all(len(row) == 3 for row in game_result).

----------
----------

Tic-Tac-Toe, a veces también conocido como Xs y Os, es un juego para dos jugadores (X y O) que se turnan
para marcar los espacios de una cuadrícula de 3×3. El jugador que consiga colocar tres marcas respectivas
en una fila horizontal, vertical o diagonal (NO-SE y NE-SO) gana la partida. El jugador que consiga colocar
tres marcas respectivas en una fila horizontal, vertical o diagonal (NO-SE y NE-SO) gana la partida.

Pero no estaremos jugando a este juego. Tú serás el árbitro de los resultados de este juego. Se te dará el
resultado de un juego y deberás determinar si el juego termina en victoria o empate, así como quién será el
ganador. Asegúrate de devolver "X" si el jugador X gana y "O" si el jugador O gana. Si la partida acaba en
empate, anota "D".

x-o-árbitro

El resultado de una partida se presenta como una lista de cadenas, donde "X" y "O" son las marcas de los
jugadores y "." es la celda vacía.

Entrada: Un resultado de juego como lista de cadenas (unicode).

Salida: "X", "O" o "D" como cadena.

Ejemplos:
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

Cómo se utiliza: Los conceptos de esta tarea te ayudarán a la hora de iterar tipos de datos. También pueden
utilizarse en algoritmos de juegos, permitiéndote saber cómo registrar resultados.

Precondiciones:
hay un ganador o un empate;
len(resultado_juego) == 3;
all(len(fila) == 3 for fila en resultado_juego).
'''


def checkio(game_result: list[str]) -> str:
    # your code here
    # Check horizontal rows
    for row in game_result:
        if row == "XXX":
            return "X"
        elif row == "OOO":
            return "O"

    # Check vertical columns
    for i in range(3):
        if game_result[0][i] == game_result[1][i] == game_result[2][i]:
            if game_result[0][i] == "X":
                return "X"
            elif game_result[0][i] == "O":
                return "O"

    # Check diagonal lines
    if game_result[0][0] == game_result[1][1] == game_result[2][2]:
        if game_result[0][0] == "X":
            return "X"
        elif game_result[0][0] == "O":
            return "O"
    elif game_result[0][2] == game_result[1][1] == game_result[2][0]:
        if game_result[0][2] == "X":
            return "X"
        elif game_result[0][2] == "O":
            return "O"

    # Check for empty cells
    for row in game_result:
        if "." in row:
            return "D"

    # If no winner and no empty cells, game is a draw
    return "D"


print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
