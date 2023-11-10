"""
This mission is dedicated to the Ulam–Warburton cellular automaton (UWCA) - a 2-dimensional
fractal pattern that grows on a regular grid of cells consisting of squares.

Starting with one square initially ON and all others OFF, successive iterations are generated
by turning ON all squares that share precisely one edge with an ON square.

This pattern is shown among others (so I recommend you to watch it all) in the following video
with Neil Sloane (founder of the On-Line Encyclopedia of Integer Sequences) starting from the 8.10.

The playground of this and other patterns may be seen on the page. It will be easier to solve
the task and it's just a beautiful hypnotic view!)

So, your function must return the number of activated cells after given number of steps.

Input: Number of steps as integer.

Output: Number of cells as integer.

Examples:
assert automaton(1) == 1
assert automaton(2) == 5
assert automaton(3) == 9
assert automaton(4) == 21

----------
----------

Esta misión está dedicada al autómata celular de Ulam-Warburton (UWCA), un patrón fractal
bidimensional que crece sobre una rejilla regular de celdas formadas por cuadrados.

Comenzando con un cuadrado inicialmente en ON y todos los demás en OFF, las iteraciones
sucesivas se generan encendiendo todos los cuadrados que comparten precisamente un borde
con un cuadrado en ON.

Este patrón se muestra entre otros (por lo que te recomiendo que lo veas entero) en el siguiente
vídeo con Neil Sloane (fundador de la Enciclopedia On-Line de Secuencias Enteras) a partir del 8.10.



El campo de juego de este y otros patrones se puede ver en la página. Será más fácil resolver
la tarea y es simplemente una hermosa vista hipnótica).

Por lo tanto, su función debe devolver el número de células activadas después de un número
dado de pasos.

Entrada: Número de pasos como entero.

Salida: Número de células como entero.

Ejemplo:
assert autómata(1) == 1
assert autómata(2) == 5
assert autómata(3) == 9
assert autómata(4) == 21
"""


def wt(n):
    return bin(n).count("1")


def u(n):
    return 1 if n == 1 else 4 * 3 ** (wt(n - 1) - 1)


def automaton(step: int) -> int:
    # your code here
    return sum(map(u, range(1, step + 1)))


print("Example:")
print(automaton(2))

# These "asserts" are used for self-checking
assert automaton(1) == 1
assert automaton(2) == 5
assert automaton(3) == 9
assert automaton(4) == 21
assert automaton(5) == 25

print("The mission is done! Click 'Check Solution' to earn rewards!")
