'''
An interval of consecutive positive integers can be succinctly described as a tuple that contains
first and last values. For example, the interval that contains the numbers 5, 6, 7, 8, 9 can be
described as (5,9). Multiple intervals can be united together into iterable. Given an iterable
with intervals (guaranteed not to overlap with each other and to be listed in a sorted ascending order),
create and return the list that contains all the integers contained by these intervals.

Input: The iterable of tuples of two integers.

Output: The iterable of integers.

Example:
expand_intervals([(1, 3), (5, 7)]) == [1, 2, 3, 5, 6, 7]
expand_intervals([(1, 3)]) == [1, 2, 3]

Precondition: Each element in the interval is an integer and

The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School
of Continuing Education by Ilkka Kokkarinen

See also:
Create Intervals
Merge Intervals

----------
----------

Un intervalo de números enteros positivos consecutivos puede describirse sucintamente como una tupla
que contiene los valores primero y último. Por ejemplo, el intervalo que contiene los números 5, 6, 7,
8, 9 puede describirse como (5,9). Múltiples intervalos pueden unirse en un iterable. Dado un iterable
con intervalos (se garantiza que no se solapan entre sí y que se enumeran en orden ascendente ordenado),
crear y devolver la lista que contiene todos los enteros contenidos por estos intervalos.

Entrada: El iterable de tuplas de dos enteros.

Salida: El iterable de enteros.

Ejemplo:
expand_intervals([(1, 3), (5, 7)]) == [1, 2, 3, 5, 6, 7]
expand_intervals([(1, 3)]) == [1, 2, 3]

Condición previa: Cada elemento del intervalo es un entero y

La misión fue tomada de Python CCPS 109 Otoño 2018. Está siendo impartido para la Escuela de Educación
Continua Ryerson Chang por Ilkka Kokkarinen.

Ver también:
Crear Intervalos
Fusionar intervalos
'''


from typing import Iterable

def expand_intervals(items: Iterable) -> Iterable:
    # your code here
    result = []
    for interval in items:
        result.extend(range(interval[0], interval[1] + 1))
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(expand_intervals([(1, 3), (5, 7)])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
    assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
    assert list(expand_intervals([])) == []
    assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]
    print("Coding complete? Click 'Check' to earn cool rewards!")
