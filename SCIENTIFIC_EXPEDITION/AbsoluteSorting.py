'''
Let's try some sorting. Here is an array with the specific rules.

The array (a list) has various numbers. You should sort it, but sort it by absolute value in ascending order.
For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should
return the sorted list or tuple.

Precondition: The numbers in the array are unique by their absolute values.

Input: An array of numbers , a tuple..

Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.

Addition: The results of your function will be shown as a list in the tests explanation panel.

Example:
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

How it is used: Sorting is a part of many tasks, so it will be useful to know how to use it.

Precondition: len(set(abs(x) for x in array)) == len(array)
0 < len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)

----------
----------

Vamos a experimentar con ordenamiento (clasificación). Aquí hay una matriz con normas específicas.

El vector (una list) tiene varios números. Debes ordenarla por valor absoluto en orden ascendente.
Por ejemplo, la secuencia (-20, -5, 10, 15), queda ordenada de la siguiente forma: (-5, 10, 15, -20).
Tu función debe devolver la lista (o tupla) ordenada.

Condiciones: Los números de la matriz son únicos por sus valores absolutos.

Datos de Entrada: Un conjunto de números, una tupla.

Salida: La lista o tupla (pero no un generador) ordenados por valores absolutos en orden ascendente.

Adicional: Los resultados de tu función serán presentados como una lista en panel de explicación de pruebas.

Ejemplo:
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

¿Cómo se usa?: La clasificación /ordenamiento es una parte de muchas tareas, por lo que es bastante
útil saber cómo se usa.

Condiciones: len(set(abs(x) for x in array)) == len(array)
0 < len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
'''


def checkio(values: list) -> list:
    # your code here
    return sorted(values, key=abs)


print("Example:")
print(checkio([-20, -5, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")
