'''
This is a mission to calculate the volume of objects that combines cubes.

You are given a list of cube details (tuple of 4 integers: X coordinate, Y coordinate,
Z coordinate, edge length).

Each coordinate is the minimum value.
All edges parallel to the coordinate axes.
If the cube share the part of another cube or touch with the face of another cube, they
are considered as one object.
You should return a list (or iterable) of the volumes of all objects.

Example:

sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52]       # fused
sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54]       # touch with faces
sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27]   # touch with edges

input: A list of tuples of 4 integers.

output: A list (or iterable) of integers.

----------
----------

Esta es una misión para calcular el volumen de objetos que combinan cubos.

Se le da una lista de detalles cubo (tupla de 4 enteros: Coordenada X, Coordenada Y,
coordenada Z, longitud de arista).

Cada coordenada es el valor mínimo.
Todas las aristas son paralelas a los ejes de coordenadas.
Si el cubo comparte la parte de otro cubo o toca con la cara de otro cubo, ellos
se consideran como un solo objeto.
Debe devolver una lista (o iterable) de los volúmenes de todos los objetos.

Ejemplo:

sorted(cubos_fusionados([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52] # fusionados
sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)]) == [54] # tocar con caras
sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27] # tocar con aristas

entrada: Una lista de tuplas de 4 enteros.

salida: Una lista (o iterable) de enteros.
'''


from typing import Tuple, List, Iterable
from scipy.ndimage import label
from itertools import product
import numpy as np


def fused_cubes(cubes: List[Tuple[int]]) -> Iterable[int]:
    ''' find volume of cubes '''

    # find min and max values
    lower, upper = min(sum(cubes, ())), max(sum(cubes, ()))

    # create 3d array of voxels
    voxels = np.zeros([2*upper - lower]*3)

    # mark every lit voxel in 3d space
    for x0, y0, z0, edge in cubes:
        for x, y, z in product(range(edge), repeat=3):
            voxels[(x0 + x - lower, y0 + y - lower, z0 + z - lower)] = 1

    # label all and convert it to flat list
    labeled, number = label(voxels)
    labeled = np.ndarray.flatten(labeled).tolist()

    return [labeled.count(group+1) for group in range(number)]


if __name__ == '__main__':
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52], 'fused'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54], 'touch with faces'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27], 'touch with edges'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 3, 3, 3)])) == [27, 27], 'touch with vertices'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 4, 3, 3)])) == [27, 27], 'separated'
    assert sorted(fused_cubes([(0, 0, 0, 3), (-2, -2, -2, 3)])) == [53], 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
