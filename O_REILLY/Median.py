'''
A median is a numerical value separating the upper half of a sorted list of numbers from the lower half.
In a list where there are an odd number of entities, the median is the number found in the middle of the
list. If the list contains an even number of entities, then there is no single middle value, instead the
median becomes the average of the two numbers found in the middle. For this mission, you are given a non-empty
list of natural integers. With it, you must separate the upper half of the numbers from the lower half
and find the median.

If you want to practice more with the similar case, try Middle Characters mission.

Input: A list of integers.

Output: The median as a float or an integer.

Examples:

assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5

How it is used: The median has usage for Statistics and Probability theory, it has especially significant
value for skewed distribution. For example: we want to know average wealth of people from a set of data -
100 people earn $100 in month and 10 people earn $1,000,000. If we average it out, we get $91,000. This
is weird value and does nothing to show us the real picture. In this case the median would give to us more
useful value and a better picture. The Article at Wikipedia.

Preconditions:

1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data)

----------
----------

La mediana representa el valor en la posición central de un conjunto de datos ordenados. En una
lista con un número impar de elementos la mediana se encuentra en la posición central. Si la lista
tiene un número par de elementos, no existe un valor central que divida la lista en dos partes iguales
por lo que la mediana equivale a la media de los dos valores centrales. En esta misión, recibirás una
lista no vacía de números naturales (X). Con ella deberás de separar la parte superior e inferior para
encontrar la mediana.

If you want to practice more with the similar case, try Middle Characters mission.

Entrada: Lista de enteros.

Salida: La mediana en formato entero/flotante.

Ejemplo:
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5

Utilidad: La mediana se usa en estadística y teoría de probabilidad, con relevante importancia en
distribuciones asimétricas. Por ejemplo: Podemos saber la media de la riqueza de las personas dentro
un conjunto de datos -- 100 personas ganan 100€/mes y 10 personas ganan 1,000,000€/mes. Si calculamos
la media de estos datos, obtenemos 91,000€/mes. Como podemos observar este valor no representa la realidad
de la población estudiada. Sin embargo, usando la mediana podemos obtener un valor más cercano a la realidad.
Mediana (Wikipedia)

Precondiciones:
1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data)
'''


def checkio(data: list[int]) -> int | float:
    # replace this for solution
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]
    return median


print("Example:")
print(checkio([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

print("The mission is done! Click 'Check Solution' to earn rewards!")
