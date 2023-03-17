'''
It would seem that it’s a short, brief journey, which should take less than one day -
what could go wrong? And yet, when the island was already visible on the horizon, suddenly,
a terrible storm began! It’s really hard to put into words what you and your men went through.
Actually… You were the sole survivor who’ve made it to the island alive - the huge waves
destroyed both ships, and what’s left from their hulls was finally shattered by the sea-cliff.
Perhaps, someone else from your crew has managed to survive, but it was very unlikely. Now you
are facing 2 tasks - to take the Hypercube from the castle and find a way off from this damned island.

Let's just take things one step at a time. For starters, you need to find a compass, map and spyglass
to navigate the terrain. Hurry up! The nature is very unpredictable and if you don’t pick up those things
in time, they will be absorbed by the coastal sand or washed away into the sea.
Your task is to count the sum of the number of steps required to pick up all 3 items - ('C' - compass),
('M' - map), ('S' - spyglass) from your starting position. So the result will be the sum of distance from
Y to C, from Y to M and from Y to S (not Y-C-M-S).
Note that you can walk in 8 directions - left, right, up, down and sideways (on the diagonal in any direction).
Your starting position is 'Y'.

Input: Array with the objects placements.

Output: The length of the path.

Example:
navigation([['Y', 0, 0, 0, 'C'],
            [ 0,  0, 0, 0,  0],
            [ 0,  0, 0, 0,  0],
            ['M', 0, 0, 0, 'S']]) == 11 #4 steps from Y to C, 4 from Y to S and 3 from Y to M

How it is used: For the finding the length of the path.

Precondition :
3x2 <= array size <= 10x10

----------
----------

Al parecer, se trata de un viaje corto y breve, que debería durar menos de un día: ¿qué
podría salir mal? Y sin embargo, cuando la isla ya era visible en el horizonte, de repente,
¡empezó una terrible tormenta! Es realmente difícil expresar con palabras lo que usted y sus
hombres pasaron. En realidad... Fuiste el único superviviente que ha llegado vivo a la isla -
las enormes olas destruyeron ambos barcos, y lo que quedó de sus cascos fue finalmente destrozado
por el acantilado. Tal vez, alguien más de su tripulación ha logrado sobrevivir, pero era muy poco
probable. Ahora te enfrentas a dos tareas: coger el Hipercubo del castillo y encontrar una salida de
esta maldita isla.

Vayamos paso a paso. Para empezar, necesitas encontrar una brújula, un mapa y un catalejo para navegar
por el terreno. Date prisa. La naturaleza es muy impredecible y si no recoges esas cosas a tiempo, serán
absorbidas por la arena de la costa o arrastradas por el mar.
Tu tarea consiste en contar la suma del número de pasos necesarios para recoger los 3 objetos -
('C' - brújula), ('M' - mapa), ('S' - catalejo) desde tu posición inicial. Así que el resultado
será la suma de la distancia de Y a C, de Y a M y de Y a S (no Y-C-M-S).
Ten en cuenta que puedes caminar en 8 direcciones: izquierda, derecha, arriba, abajo y de lado
(en diagonal en cualquier dirección). Tu posición inicial es 'Y'.

Entrada: Array con las colocaciones de los objetos.

Salida: La longitud del camino.

Ejemplo:
navegación(['Y', 0, 0, 0, 'C'],
            [ 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0],
            ['M', 0, 0, 0, 'S']]) == 11 #4 pasos de Y a C, 4 de Y a S y 3 de Y a M

Cómo se utiliza: Para hallar la longitud del camino.

Precondición :
3x2 <= tamaño del array <= 10x10
'''


def navigation(seaside):
    #replace this for solution
    # Find the starting position
    start_row = None
    start_col = None
    for row in range(len(seaside)):
        for col in range(len(seaside[row])):
            if seaside[row][col] == 'Y':
                start_row = row
                start_col = col
                break
        if start_row is not None:
            break

    # Find the positions of the compass, map, and spyglass
    compass_row = None
    compass_col = None
    map_row = None
    map_col = None
    spyglass_row = None
    spyglass_col = None
    for row in range(len(seaside)):
        for col in range(len(seaside[row])):
            if seaside[row][col] == 'C':
                compass_row = row
                compass_col = col
            elif seaside[row][col] == 'M':
                map_row = row
                map_col = col
            elif seaside[row][col] == 'S':
                spyglass_row = row
                spyglass_col = col

    # Calculate the distances
    dist_to_compass = max(abs(start_row - compass_row), abs(start_col - compass_col))
    dist_to_map = max(abs(start_row - map_row), abs(start_col - map_col))
    dist_to_spyglass = max(abs(start_row - spyglass_row), abs(start_col - spyglass_col))

    # Return the sum of the distances
    return dist_to_compass + dist_to_map + dist_to_spyglass


if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
    