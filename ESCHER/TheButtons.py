"""
After completing the previous task you’ve been a “little” agitated. The ghost said just one word: “Worthy...”,
and disappeared through the wall. You are incredibly lucky that you’ve met him here, and not next to the Hypercube,
because in that case he surely wouldn’t let you go alive.

Walking down the corridor further, you’ve been taken aback by the fact that it’s becoming narrower and the ceiling
is getting lower. But it didn’t last long, because soon you’ve hit the dead end in a form of a bare wall, not in
any way suggesting the it’s possible to go further. Some kind of figures on the ceiling made you wonder. Maybe
there is a way to interact with them?..
There were buttons on the ceiling in the form of geometrical figures with written numbers on them. Your task
is to press them in the correct order - starting from the most "valuable" and finishing with the least "valuable"
one. The figure’s value corresponds with the sum of all the numbers on it. A separate geometrical figure is the
one whose elements are directly connected to one another (horizontally or vertically). Your function should
return a list where the values ​​of all figures will be listed in the order in which they should be pressed.
0 is a symbol for separating the individual figures. If several figures have the same value, they can be pressed
in any order.

Input: ceiling with numbers as the multiline string.

Output: right order of the buttons.

Example:
#buttons('''
#001203
#023001
#100220''') == [8, 4, 4, 1]

How it is used: For the graphical analisys.

Precondition :
1 <= the number of buttons <= 10

----------
----------

Después de completar la tarea anterior te has agitado un "poco". El fantasma ha dicho una sola palabra: "Digno...", 
y ha desaparecido a través de la pared. Tienes una suerte increíble de haberte encontrado con él aquí, y no al lado 
del Hipercubo, porque en ese caso seguramente no te dejaría ir vivo.

Siguiendo caminando por el pasillo, te ha sorprendido el hecho de que cada vez es más estrecho y el techo cada 
vez más bajo. Pero no duró mucho, porque pronto llegasteis a un callejón sin salida en forma de pared desnuda, 
que no sugería en modo alguno que fuera posible seguir avanzando. Unas figuras similares en el techo te hacen 
dudar. Tal vez haya alguna forma de interactuar con ellas...
Había botones en el techo en forma de figuras geométricas con números escritos en ellos. Tu tarea consiste en 
pulsarlos en el orden correcto, empezando por el más "valioso" y terminando por el menos "valioso". El valor de 
la figura corresponde a la suma de todos los números que aparecen en ella. Una figura geométrica independiente 
es aquella cuyos elementos están directamente conectados entre sí (horizontal o verticalmente). Su función debe 
devolver una lista en la que los valores de todas las figuras estarán en el orden en que deben pulsarse. 0 es un 
símbolo para separar las cifras individuales. Si varias cifras tienen el mismo valor, pueden pulsarse en 
cualquier orden.

Entrada: techo con números como cadena multilínea.

Salida: orden correcto de los botones.

Ejemplo:
#botones('''
#001203
#023001
#100220''') == [8, 4, 4, 1]

Cómo se utiliza: Para el análisis gráfico.

Condición previa :
1 <= el número de botones <= 10
"""


def buttons(ceiling):
    #replace this for solution
    # parse the input string to create a two-dimensional list
    ceiling = [[int(c) for c in line.strip()] for line in ceiling.strip().split('\n')]
    n_rows, n_cols = len(ceiling), len(ceiling[0])
    # compute the value of each figure
    figures = []
    for i in range(n_rows):
        for j in range(n_cols):
            if ceiling[i][j] != 0:
                # find all numbers on the same figure
                stack = [(i, j)]
                value = ceiling[i][j]
                ceiling[i][j] = 0
                while stack:
                    r, c = stack.pop()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n_rows and 0 <= nc < n_cols and ceiling[nr][nc] != 0:
                            stack.append((nr, nc))
                            value += ceiling[nr][nc]
                            ceiling[nr][nc] = 0
                figures.append(value)
    # sort the figures in descending order and return their order
    return sorted(figures, reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(buttons('''
001203
023001
100220'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert buttons('''
001203
023001
100220''') == [8, 4, 4, 1]

    assert buttons('''
000000
000055
000055''') == [20]

    assert buttons('''
908070
060504
302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
