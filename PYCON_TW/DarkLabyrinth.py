"""
Do you remember the classic mission Open Labyrinth ? Well, you once again find yourself
inside a labyrinth, but the lights are out and you cannot see the full map. You have
flashlight and know that all passages in the Labyrinth are directed along South-North
and East-West lines. You don't yet know your position or the location of the exit. You
must hurry as you cannot run forever.

This is a "multicall" mission and as such, your function will be called until you have
solved the maze or run out of moves. For each iteration you see a part of the labyrinth
in four directions (function input). You can see passages and where they have crossings
and turns. If it's in your range of vision, you'll see the exit too. The visible zones
are represented as a grid as a tuple of strings, where "X" is a wall, "." is a passage
cell, "?" is unknown, "P" is player and "E" is the exit. Grids are represented as 2D
rectangular arrays. The size is related to size of the visible zone.

For each iteration your function should return one or several actions as a string with
directions. Actions are described as directions: "N" - North, "S" - South, "W" - West
and "E" - East. For example: the string "NWS" describes a sequence of three moves.
The walls are coated in a weird slime so you shouldn't make a move that would have you
walk into a wall. To make things interesting, you are limited to 250 moves (not iterations).
You can use global variables between iterations.

For example on the image you can see the full labyrinth and that will be visible for player.
And your function will receive:

("???XXX",
 "???...",
 "???X.X",
 "XXXX.X",
 "X...PX",
 "XXXX.X",
 "???X.X",
 "???...",
 "???X.X",
 "???X.X",
 "???..X",
 "???XXX")
Input: A visible part as a tuple of strings.

Output: An action or several actions as a string.

Example:
1

How it is used: This concept is pathfinding algorithm with search. It can be used to explore
territory and make a map.

Precondition:
The labyrinth are surrounded by walls.
All passages are narrow (1 cell width)
3 < len(visible) ≤ 15
all(len(row) == len(visible[0]) for row in visible)

----------
----------

¿Recuerdas la clásica misión Laberinto abierto? Pues bien, una vez más te encuentras dentro
de un laberinto, pero las luces están apagadas y no puedes ver el mapa completo. Tienes una
linterna y sabes que todos los pasadizos del Laberinto se dirigen a lo largo de las líneas
Sur-Norte y Este-Oeste. Aún no conoces tu posición ni la ubicación de la salida. Debes darte
prisa ya que no puedes correr eternamente.

Esta es una misión "multicall" y como tal, tu función será llamada hasta que hayas resuelto el
laberinto o te quedes sin movimientos. En cada iteración ves una parte del laberinto en cuatro
direcciones (entrada de la función). Puedes ver los pasajes y dónde tienen cruces y giros.
Si está en tu rango de visión, también verás la salida. Las zonas visibles se representan como
una cuadrícula como una tupla de cadenas, donde "X" es una pared, "." es una celda de paso, "?"
es desconocido, "P" es jugador y "E" es la salida. Las rejillas se representan como matrices
rectangulares 2D. El tamaño está relacionado con el tamaño de la zona visible.

Para cada iteración tu función debe devolver una o varias acciones como una cadena con
direcciones. Las acciones se describen como direcciones: "N" - Norte, "S" - Sur, "O" - Oeste y
"E" - Este. Por ejemplo: la cadena "NWS" describe una secuencia de tres movimientos. Las
paredes están recubiertas de una extraña baba, por lo que no debes hacer un movimiento que te
haga chocar contra una pared. Para hacer las cosas interesantes, estás limitado a 250 movimientos
(no iteraciones). Puedes usar variables globales entre iteraciones.

Por ejemplo en la imagen puedes ver el laberinto completo y que será visible para el jugador.
Y tu función recibirá

("???XXX",
 "???...",
 "XXXX.X",
 "XXXX.X",
 "X...PX",
 "XXXX.X",
 "X.X",
 "???...",
 "X.X",
 "X.X",
 "???..X",
 "XXX")

Entrada: Una parte visible como tupla de cadenas.

Salida: Una acción o varias acciones como cadena.

Ejemplo:
1
Cómo se utiliza: Este concepto es un algoritmo de pathfinding con búsqueda. Se puede utilizar para explorar un territorio y hacer un mapa.

Condición previa:
El laberinto está rodeado de muros.
Todos los pasajes son estrechos (1 celda de ancho)
3 < len(visible) ≤ 15
all(len(fila) == len(visible[0]) for fila en visible)
"""


from itertools import groupby, product


dirs = dict(zip((-1j, 1, -1, 1j), "NEWS"))
unit = lambda z: z / abs(z)
branches, route = {}, []


def find_path(maze):
    coords = tuple(product(*map(range, map(len, (maze, maze[0])))))
    find = lambda xs: set(complex(c, r) for r, c in coords if maze[r][c] in xs)
    relp, goal, area = find("P").pop(), find("E"), find(".EP")
    if not route:
        route.append(0)
    absp = route[-1]

    hasturn = lambda drs: any(d.real for d in drs) and any(d.imag for d in drs)
    if absp not in branches:
        cross = (z for z in area if z != relp and unit(z - relp) in dirs)
        steps = {z: [d for d in dirs if z + d in area] for z in cross}
        diffs = (z - relp for z in steps if z in goal or hasturn(steps[z]))

        az = dict(key=lambda z: dirs[unit(z)])
        mins = (min(g, key=abs) for i, g in groupby(sorted(diffs, **az), **az))
        branches[absp] = set(d + absp for d in mins) - set(route)

    getpath = lambda src, dst: dirs[unit(dst - src)] * int(abs(dst - src))
    if not branches[absp]:
        return getpath(route.pop(), route[-1])

    dst = branches[absp].pop()
    route.append(dst)
    if goal and dst == goal.pop() - relp + absp:
        branches.clear()
        route.clear()
    return getpath(absp, dst)
