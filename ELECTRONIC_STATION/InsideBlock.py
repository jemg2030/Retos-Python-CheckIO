'''
When it comes to city planning it's important to understand the borders of various city structures. Parks,
lakes or living blocks can be represented as closed polygon and can be described using cartesian coordinates
on a map. We need a functionality to determine if a point (a building or a tree) lies inside the structure.

For the purpose of this mission, a city structure may be considered a polygon represented as a sequence of
vertex coordinates on a plane or map. The vertices are connected sequentially with the last vertex in the
list connecting to the first. We are given the coordinates of the point which we need to check. If the point
of impact lies on the edge of the polygon then it should be considered inside of it. For this mission, you
need to determine whether the given point lies inside the polygon.


For example, on the left image you see a polygon which is described by [[2, 1], [1, 5],[5, 7], [7, 7], [7, 2]]
and the point at [2, 7]. The result is False.
For the right image the point lies on the edge and gets counted as inside the polygon, making the result True.

Input: Two arguments. Polygon coordinates as a list of lists with two integers each. A checking point coordinates
as a list of two integers.

Output: Whatever the point inside the polygon or not as a boolean.

Example:
is_inside([[1, 1], [1, 3], [3, 3], [3, 1]), [2, 2]) == True
is_inside([[1,1], [1, 3], [3, 3], [3, 1]), [4, 2]) == False

How it is used: This concept is using for image recognizing. But as we said early it can be useful for
topographical software and city planning.

Precondition:
all(x ≥ 0 and y ≥ 0 for x, y in polygon)
point[0] ≥ 0 and point[1] ≥ 0

----------
----------

A la hora de planificar una ciudad, es importante conocer los límites de sus distintas estructuras. Los
parques, lagos o manzanas habitables pueden representarse como polígonos cerrados y describirse mediante
coordenadas cartesianas en un mapa. Necesitamos una funcionalidad para determinar si un punto (un edificio
o un árbol) se encuentra dentro de la estructura.

A efectos de esta misión, la estructura de una ciudad puede considerarse un polígono representado como una
secuencia de coordenadas de vértices en un plano o mapa. Los vértices se conectan secuencialmente y el
último vértice de la lista se conecta con el primero. Se nos dan las coordenadas del punto que tenemos que
registrar. Si el punto de impacto se encuentra en el borde del polígono, entonces debe considerarse dentro de
él. Para esta misión, es necesario determinar si el punto dado se encuentra dentro del polígono.

Por ejemplo, en la imagen de la izquierda se ve un polígono descrito por [[2, 1], [1, 5],[5, 7], [7, 7], [7, 2]]
y el punto en [2, 7]. El resultado es Falso.
Para la imagen de la derecha, el punto se encuentra en el borde y se cuenta como dentro del polígono, haciendo
que el resultado sea True.

Entrada: Dos argumentos. Coordenadas del polígono como una lista de listas con dos enteros cada una. Las
coordenadas del punto a registrar como una lista de dos enteros.

Salida: Cualquiera que sea el punto dentro del polígono o no como un booleano.

Ejemplo:
is_inside([[1, 1], [1, 3], [3, 3], [3, 1]), [2, 2]) == True
is_inside([[1,1], [1, 3], [3, 3], [3, 1]), [4, 2]) == Falso

Cómo se utiliza: Este concepto se utiliza para el reconocimiento de imágenes. Pero como dijimos al principio
puede ser útil para software topográfico y planificación de ciudades.

Precondición:
all(x ≥ 0 and y ≥ 0 for x, y in polygon)
punto[0] ≥ 0 y punto[1] ≥ 0
'''


from typing import Tuple


def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    # shift polygon so that point is origin
  polygon = [(p[0]-point[0],p[1]-point[1]) for p in polygon]

  count = 0
  for i,p1 in enumerate(polygon):
    p2 = polygon[(i+1)%len(polygon)]
    if p2[1]*p1[1] <= 0:
      if p1[1]==0==p2[1]:
        if p1[0]>=0 or p2[0]>=0:
          return True
      else:
        x_int = p2[0] - p2[1]*(p2[0]-p1[0])/(p2[1]-p1[1])
        if x_int == 0:
          return True
        elif x_int > 0:
          count = count + 1
    for (u,v) in ((p1,p2),(p2,p1)):
      if u[1] == 0 and u[0] >= 0 and u[1] > v[1]:
        count = count + 1

  return count%2==1


if __name__ == "__main__":
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)), (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)), (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)), (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)), (4, 3)) is False, "Sixth"
    assert (
        is_inside(
            ((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)), (3, 3)
        )
        is True
    ), "Seventh"
    assert (
        is_inside(
            ((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)), (4, 3)
        )
        is False
    ), "Eighth"
    print("All done! Let's check now")
