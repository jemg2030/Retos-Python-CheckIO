'''
This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Example:
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True

Input:
Two lists as coordinates of vertices of each triangle.
Coordinates is three tuples of two integers.
Output: True or False.

Precondition:
-10 ≤ x(, y) coordinate ≤ 10

----------
----------

Esta es una misión para registrar la similitud de dos triángulos.

Se le dan dos listas como coordenadas de los vértices de cada triángulo.
Tienes que devolver un bool. (Los triángulos son similares o no)

Ejemplo:
triángulos_similares([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) es True
triángulos_similares([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) es Falso
triángulos_similares([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) es True

Entrada:
Dos listas como coordenadas de los vértices de cada triángulo.
Las coordenadas son tres tuplas de dos enteros.
Salida: Verdadero o Falso.

Precondición:
-10 ≤ coordenada x(, y) ≤ 10
'''


from math import dist, acos, degrees

def similar_triangles(triangle1, triangle2):
    # Calculate the lengths of all sides of each triangle
    sides1 = [dist(triangle1[i], triangle1[(i+1)%3]) for i in range(3)]
    sides2 = [dist(triangle2[i], triangle2[(i+1)%3]) for i in range(3)]

    # Sort the sides of each triangle by length
    sides1.sort()
    sides2.sort()

    # Check if the ratios of corresponding sides are equal
    if abs(sides1[0]/sides2[0] - sides1[1]/sides2[1]) > 1e-9:
        return False
    if abs(sides1[0]/sides2[0] - sides1[2]/sides2[2]) > 1e-9:
        return False

    # Calculate the cosine of each angle in both triangles
    cos1 = [0]*3
    cos2 = [0]*3
    for i in range(3):
        j, k = (i+1)%3, (i+2)%3
        a, b, c = sides1[j], sides1[k], sides1[i]
        cos1[i] = (a*a + b*b - c*c)/(2*a*b)
        a, b, c = sides2[j], sides2[k], sides2[i]
        cos2[i] = (a*a + b*b - c*c)/(2*a*b)

    # Check if the cosine of each corresponding angle is equal
    if abs(cos1[0]-cos2[0]) > 1e-9:
        return False
    if abs(cos1[1]-cos2[1]) > 1e-9:
        return False
    if abs(cos1[2]-cos2[2]) > 1e-9:
        return False

    # If we reach this point, then the triangles are similar
    return True


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
