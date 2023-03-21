'''
The main architect of the city wants to build a new highest building.
You have to help him find the current highest building in the city.

Input: Heights of the buildings as a 2D-list. Building height is defined as a column in a list.

Output: The number of the highest building and height of it as a list of integers (Important:
in this task the building numbers starts from "1", not from "0").

Examples:
assert highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == [
    3,
    4,
]
assert highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == [
    4,
    1,
]

How it is used: Every true programmer should know how to work with the 2D-lists.

Preconditions:
array width <= 10;
array height <= 10;
there is only 1 highest building in each array.

----------
----------

El arquitecto principal de la ciudad quiere construir un nuevo edificio más alto.
Tienes que ayudarle a encontrar el actual edificio más alto de la ciudad.

Entrada: Alturas de los edificios como una lista 2D. La altura de los edificios se define
como una columna de la lista.

Salida: El número del edificio más alto y su altura como una lista de enteros (Importante: en
esta tarea los números de los edificios empiezan por "1", no por "0").

Ejemplos:
assert edificio_más_alto([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == [
    3,
    4,
]
assert edificio_mayor([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == [
    4,
    1,
]

Cómo se utiliza: Todo verdadero programador debe saber trabajar con las listas 2D.

Precondiciones:
array anchura <= 10;
altura del array <= 10;
sólo hay 1 edificio más alto en cada array.
'''


def highest_building(buildings: list[list[int]]) -> list[int]:
    # your code here
    max_height = 0
    max_building = 0
    for col in range(len(buildings[0])):
        height = 0
        for row in range(len(buildings)):
            if buildings[row][col] == 1:
                height = len(buildings) - row
                break
        if height > max_height:
            max_height = height
            max_building = col + 1
    return [max_building, max_height]


print("Example:")
print(highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))

# These "asserts" are used for self-checking
assert highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]) == [
    3,
    4,
]
assert highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == [
    4,
    1,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
