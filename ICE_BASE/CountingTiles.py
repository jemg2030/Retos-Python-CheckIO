"""
Stephan needs some help building a circular landing zone using the ice square tiles for their
new Ice Base. Before he converts the area to a construction place, Stephan needs to figure out
how many square tiles he will need.

Each square tile has size of 1x1 meters. You need to calculate how many whole and partial tiles
are needed for a circle with a radius of N meters. The center of the circle will be at the
intersection of four tiles. For example: a circle with a radius of 2 metres requires 4 whole
tiles and 12 partial tiles.

Input: The radius of a circle as a float

Output: The quantities whole and partial tiles as a list with two integers -- [solid, partial].

Example:
checkio(2) == [4, 12]
checkio(3) == [16, 20]
checkio(2.1) == [4, 20]
checkio(2.5) == [12, 20]

How it is used: This task is a simple geometry problem; but you can use it for architecture and
topography. As we see in the description, you can calculate the amount of materials needed for a project.

Precondition:
0 < radius ≤ 4

----------
----------

Stephan necesita un poco de ayuda con la construcción de una zona de aterrizaje circular para
su nueva Base de Hielo. Para esta labor, Stephan dispone de bloques cuadrados de hielo pero es
necesario que conozca de antemano cuantos cuadrados necesita, antes que pueda convertir la zona
en un lugar de construcción.

Cada bloque cuadrado de hielo es de 1x1 metros. Deberás calcular cuántos bloques enteros y cuantos
bloques fragmentados se necesitan para construir un círculo con un radio de N metros. El centro del
círculo estará en la intersección de bloques. Por ejemplo: un círculo con un radio de 2 metros requiere
4 bloques enteros y 12 bloques fragmentados.

Datos de Entrada: El radio de un círculo como un decimal ( float )

Salida: El número de bloques enteros y bloques fragmentados, como una lista con dos enteros - [entero, fragmentado].

Ejemplo:
checkio(2) == [4, 12]
checkio(3) == [16, 20]
checkio(2.1) == [4, 20]
checkio(2.5) == [12, 20]

¿Cómo se usa?: Esta tarea es un problema de geometría simple; pero se puedes utilizarla en arquitectura
y topografía. Como vimos en la descripción, podrías calcular la cantidad de materiales necesarios para un
proyecto.

Condiciones:
0 < radius ≤ 4
"""


from math import ceil


def checkio(radius):
    """count tiles"""
    solid = 0
    partial = 0
    a = ceil(radius)
    for x in range(a):
        for y in range(a):
            if (x + 1) ** 2 + (y + 1) ** 2 <= radius ** 2:
                # "outer" corner in circle
                solid += 1
            elif x**2 + y**2 <= radius**2:
                # "inner" corner in circle
                partial += 1
    # we counted one quadrant only, so multiply by 4
    return [solid * 4, partial * 4]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
