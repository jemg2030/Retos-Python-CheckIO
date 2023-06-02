'''
In this mission you'll have to make the Minimum spanning tree (Wikipedia) .

You are given a list of coordinates of vertices. Each coordinate is a tuple of x (integer)
and y (integer).
You have to return a list (or an iterable) of lines that connect all vertices. The total length of
lines should be the minimum. Each line is a tuple of two integers. These integers represent the
index of list of input.

NOTE:
The output of tests has a unique combination of lines.

Example:
connect_stars([(1, 1), (4, 4)])) == [(0, 1)]                         # or [(1, 0)]
connect_stars([(1, 1), (4, 1), (4, 4)])) == [(0, 1), (1, 2)]         # or [(1, 2), (0, 1)] , [(1, 0), (2,1)] etc
connect_stars([(6, 6), (6, 8), (8, 4), (3, 2)])) == [(0, 1), (0, 2), (0, 3)]   # or [(2, 0), (0, 3), (1, 0)] etc

Input:
A list of coordinates of vertices.
Each coordinate is a tuple of x (integer) and y (integer).

Output:
A list (or an iterable) of lines.
Each line is a tuple of two integers. These integers represent the index of list of input.
The order of lines and each index is arbitrary (see examples).
Precondition:

2 ≤ len(input) ≤ 50
0 ≤ x (,y) ≤ 999

----------
----------

En esta misión tendrás que hacer el Árbol de mínima expansión (Wikipedia) .

Se te da una lista de coordenadas de vértices. Cada coordenada es una tupla de x
(entero) e y (entero).
Tienes que devolver una lista (o un iterable) de líneas que conectan todos los vértices.
La longitud total de las líneas debe ser la mínima. Cada línea es una tupla de dos enteros.
Estos enteros representan el índice de la lista de entrada.

NOTA:
La salida de las pruebas tiene una única combinación de líneas.

Ejemplo:
conectar_estrellas([(1, 1), (4, 4)])) == [(0, 1)] # o [(1, 0)]
connect_stars([(1, 1), (4, 1), (4, 4)])) == [(0, 1), (1, 2)] # o [(1, 2), (0, 1)] , [(1, 0), (2,1)] etc
conectar_estrellas([(6, 6), (6, 8), (8, 4), (3, 2)])) == [(0, 1), (0, 2), (0, 3)] # o [(2, 0), (0, 3), (1, 0)] etc

Entrada:
Una lista de coordenadas de vértices.
Cada coordenada es una tupla de x (entero) e y (entero).
Salida:

Una lista (o un iterable) de líneas.
Cada línea es una tupla de dos enteros. Estos enteros representan el índice de la lista de entrada.
El orden de las líneas y de cada índice es arbitrario (ver ejemplos).
Condición previa:

2 ≤ len(entrada) ≤ 50
0 ≤ x (,y) ≤ 999
'''


from typing import List, Tuple, Iterable

def connect_stars(coords: List[Tuple[int, int]]) -> Iterable[Tuple[int, int]]:
    # your code here
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def calculate_distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Create a list of edges with their corresponding distances
    edges = []
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_distance(coords[i], coords[j])
            edges.append((i, j, distance))

    # Sort the edges by distance in ascending order
    edges.sort(key=lambda x: x[2])

    # Initialize parent and rank arrays for union-find
    parent = [i for i in range(n)]
    rank = [0] * n

    # Perform Kruskal's algorithm to find the minimum spanning tree
    minimum_spanning_tree = []
    for edge in edges:
        u, v, distance = edge
        if find(parent, u) != find(parent, v):
            minimum_spanning_tree.append((u, v))
            union(parent, rank, u, v)

    return minimum_spanning_tree


if __name__ == '__main__':

    print("Example:")
    print(connect_stars([(1, 1), (4, 4)]))

    def sort_edges(edges): return sorted(map(lambda e: tuple(sorted(e)), edges))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_edges(connect_stars([(1, 1), (4, 4)])) == [(0, 1)], '2 vertices'
    assert sort_edges(connect_stars([(1, 1), (4, 1), (4, 4)])) == [(0, 1), (1, 2)], '3 vertices'
    assert sort_edges(connect_stars([(6, 6), (6, 8), (8, 4), (3, 2)])) == [(0, 1), (0, 2), (0, 3)], '4 vertices'
    assert sort_edges(connect_stars([(5, 4), (5, 1), (2, 6), (7, 2), (6, 9)])) == [(0, 2), (0, 3), (1, 3), (2, 4)], '5 vertices'
    assert sort_edges(connect_stars([(5, 8), (5, 1), (4, 2), (7, 6), (8, 6), (2, 2)])) == [(0, 3), (1, 2), (2, 3), (2, 5), (3, 4)], '6 vertices'
    assert sort_edges(connect_stars([(2, 7), (9, 9), (4, 9), (9, 6), (3, 3), (1, 6), (9, 7)])) == [(0, 2), (0, 5), (1, 2), (1, 6), (3, 6), (4, 5)], '7 vertices'
    print("Coding complete? Click 'Check' to earn cool rewards!")
