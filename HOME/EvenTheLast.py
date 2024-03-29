'''
You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then
multiply this summed number and the final element of the array together. Don't forget that the first element has an
index of 0.
For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

Example:

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

How it is used: Indexes and slices are important elements of coding. This will come in handy down the road!

Precondition: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)

---------
---------

Se te da un arreglo de enteros. Deberías encontrar la suma de los elementos con índices pares (0, 2do, 4to... ) luego
multiplicar ese resultado con el elmento final del arreglo. No olvides que el primer elemento tiene el índice 0.
Para un arreglo vacio, el resultado siempre será 0 (cero).

Entrada: Una lista de enteros.

Salida: El número como un entero.

Ejemplo:
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

Cómo se usa: Índices y fragmentos son elementos importantes de la programación en python y otros lenguajes. Esto se
volverá útil en el camino más adelante!

Precondición: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
'''


def checkio(array: list[int]) -> int:
    # your code here
    if not array:
        return 0
    even_index_sum = sum(array[i] for i in range(0, len(array), 2))
    return even_index_sum * array[-1]

# These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    print("Example:")
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30
    assert checkio([1, 3, 5]) == 30
    assert checkio([6]) == 36
    assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
