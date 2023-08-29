"""
For our future Robotropolis we need to help the city planners calculate the way light
reaches our fair city so as to limit the Urban Canyon effect. To do this, you will need
to define the visibility of buildings from the southern edge of the base. You have been
given a map of the buildings in the complex as an aide for your planning.

The map is an orthogonal projection of each of the buildings onto a horizontal plane.
It's oriented on a rectangular coordinate system so that the positive x-axis points
east and the positive y-axis points north. No two buildings in the map overlap or touch.
Each of the buildings have perfectly rectangular sides which are aligned from north to
south and east to west. The map is a list of buildings with each building presented as
a list with coordinates describing the south-west corner, and north-east corner along
with the height - [Xsw, Ysw, Xne, Yne, height]. We need to determinate how many of the
buildings are visible from the area just south of the base (excluding the angle of
vision, just using projection.) See the illustration below.

Input: Building coordinates and heights as a list of lists. The coordinates are integers.
The heights are integers or floats.

Output: The quantity of visible buildings as an integer.

Example:
checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
        ]) == 5 #"First"
        checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
        ]) == 2 #"Second"
        assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
        ]) == 4 #"Third"

How it is used: This concept is useful for image recognition systems and graphical systems.
When rendering of 3D model you should determine the visibility of the surfaces. It can also
be applied in architecture and city planning, allowing you to plan out which sides of a
building will receive sunlight, or if a building will block natural light in another building.

Precondition:
0 < len(buildings) < 10
all(all(0 ≤ x < 12 for x in row[:4]) for row in buildings)
all(0 < row[4] ≤ 20 for row in buildings)

----------
----------

Para nuestra futura Robotropolis , tenemos que ayudar a los planificadores de la
ciudad a calcular como la luz alcanza nuestra bella ciudad, así como limitar el efecto
Urban Canyon . Para ello, tendrás que definir la visibilidad de los edificios desde el
extremo sur de la base. Se te ha asignado un mapa de los edificios del complejo, como
ayuda para tu planificación.

El mapa es una proyección ortogonal de cada uno de los edificios sobre un plano horizontal.
Está orientado en un sistema de coordenadas rectangulares de modo que el eje x positivo
se dirige hacia el este y el eje y positivo hacia el norte. No existen dos edificios en
el mapa que se sobre posicionen o se toquen. Cada uno de los edificios tiene lados perfectamente
rectangulares, que se encuentran alineados de norte a sur y de este a oeste. El mapa es una
lista de edificios con cada edificio presentado como una lista incluyendo las coordenadas de
la esquina suroeste, de la esquina noreste, así como la altura -[Xsw, Ysw, Xne, Yne, height].
Debemos determinar cuántos edificios son visibles desde la zona al sur de la base (excluyendo
el ángulo de visión, simplemente usando proyección.) Consulta la siguiente ilustración.

Datos de Entrada: Coordenadas y alturas de los edificios, como una lista de listas. Las
coordenadas son enteros ( int ). Las alturas son enteros ( int ) o decimales ( float ).

Salida: La cantidad de edificios visibles, como un entero ( int ).

Ejemplo:
checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
        ]) == 5 #"First"
        checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
        ]) == 2 #"Second"
        assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
        ]) == 4 #"Third"

¿Cómo se usa?: Este concepto es útil para sistemas de reconocimiento de imágenes y sistemas gráficos.
Cuando se representan modelos 3D, debes determinar la visibilidad de las superficies. También se
puede aplicar en la arquitectura y la planificación urbana, para determinar cuáles edificios van
a recibir la luz del sol (y en que lugares), o si un edificio bloqueará la luz natural para otro
edificio.

Condiciones:
0 < len(buildings) < 10
all(all(0 ≤ x < 12 for x in row[:4]) for row in buildings)
all(0 < row[4] ≤ 20 for row in buildings)
"""


def checkio(buildings):
    # for example
    d = {}
    for n, b in enumerate(buildings):
        for i in range(b[0], b[2]):
            d[i] = d.get(i, []) + [[n, b[1], b[4]]]
    s = set()
    for L in d.values():
        mh = 0
        for ceil in sorted(L, key=lambda x: x[1]):
            if ceil[2] > mh:
                s.add(ceil[0])
                mh = ceil[2]
    return len(s)


if __name__ == "__main__":
    assert (
        checkio(
            [
                [1, 1, 4, 5, 3.5],
                [2, 6, 4, 8, 5],
                [5, 1, 9, 3, 6],
                [5, 5, 6, 6, 8],
                [7, 4, 10, 6, 4],
                [5, 7, 10, 8, 3],
            ]
        )
        == 5
    ), "First"
    assert (
        checkio([[1, 1, 11, 2, 2], [2, 3, 10, 4, 1], [3, 5, 9, 6, 3], [4, 7, 8, 8, 2]])
        == 2
    ), "Second"
    assert (
        checkio(
            [
                [1, 1, 3, 3, 6],
                [5, 1, 7, 3, 6],
                [9, 1, 11, 3, 6],
                [1, 4, 3, 6, 6],
                [5, 4, 7, 6, 6],
                [9, 4, 11, 6, 6],
                [1, 7, 11, 8, 3.25],
            ]
        )
        == 4
    ), "Third"
    assert checkio([[0, 0, 1, 1, 10]]) == 1, "Alone"
    assert checkio([[2, 2, 3, 3, 4], [2, 5, 3, 6, 4]]) == 1, "Shadow"
