'''
You are given an array with positive numbers and a number N. You should find the N-th power of the
element in the array with the index N. If N is outside of the array, then return -1. Don't forget
that the first element has the index 0.

Let's look at a few examples:
- array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Input: Two arguments. An array as a list of integers and a number as a integer.

Output: The result as an integer.

Example:
assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1

How it is used: This mission teaches you how to use basic arrays and indexes when combined with simple mathematics.

Precondition: 0 < len(array) ≤ 10
0 ≤ N
all(0 ≤ x ≤ 100 for x in array)

----------
----------

Se te da un arreglo con números positivos y un número N. Deberías encontrar la N-ésima potencia del
elemento en el arreglo con el índice N. Si el indíce N está afuera del arreglo, entonces devolver -1.
No olvides que el primer elemento tene el índice 0.

Miremos algunos ejemplos:
- arreglo = [1, 2, 3, 4] y N = 2, entonces el resultado es 32 == 9;
- arreglo = [1, 2, 3] y N = 3, pero N está afuera del arrego, entonces el resultado es -1.

Entrada: Dos parametros. Un arreglo como una lista de enteros y un número como un entero.

Salida: El resultado como un entero.

Ejemplo:
assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1

Cómo se usa: Esta misión te enseña a como usar arreglos básicos e índices cuando son combinados con matemáticas sencillas.

Precondición: 0 < len(array) ≤ 10
0 ≤ N
all(0 ≤ x ≤ 100 for x in array)
'''


def index_power(ar: list[int], n: int) -> int:
    # your code here
    if n < 0 or n >= len(ar):
        return -1
    return ar[n] ** n


print("Example:")
print(index_power([1, 2, 3], 2))

# These "asserts" are used for self-checking
assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")
