'''
From a set of ints you have to create a list of closed intervals as tuples, so the intervals
are covering all the values found in the set.

A closed interval includes its endpoints! The interval 1..5 , for example, includes each value
x that satifies the condition 1 <= x <= 5 .

Values can only be in the same interval if the difference between a value and the next smaller
value in the set equals one, otherwise a new interval begins. Of course, the start value of an
interval is excluded from this rule.
A single value, that does not fit into an existing interval becomes the start- and endpoint of a
new interval.

Input: A set of ints.

Output: A list of tuples of two ints, indicating the endpoints of the interval. The Array should be
sorted by start point of each interval

Examples:
create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]

----------
----------

A partir de un conjunto de ints hay que crear una lista de intervalos cerrados como tuplas, de forma
que los intervalos cubran todos los valores encontrados en el conjunto.

¡Un intervalo cerrado incluye sus puntos finales! El intervalo 1..5 , por ejemplo, incluye cada valor x
que satisface la condición 1 <= x <= 5 .

Los valores sólo pueden estar en el mismo intervalo si la diferencia entre un valor y el siguiente valor
más pequeño del conjunto es igual a uno; de lo contrario, comienza un nuevo intervalo. Por supuesto, el
valor inicial de un intervalo queda excluido de esta regla.
Un único valor que no encaje en un intervalo existente se convierte en el punto inicial y final de un nuevo
intervalo.

Entrada: Un conjunto de ints.

Salida: Una lista de tuplas de dos ints, indicando los puntos finales del intervalo. El array debe estar
ordenado por punto inicial de cada intervalo

Ejemplos:
crear_intervalos({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
crear_intervalos({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]
'''


def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    numbers = sorted(data)
    intervals = []
    start, end = None, None
    for num in numbers:
        if start is None:
            start = num
            end = num
        elif num == end + 1:
            end = num
        else:
            intervals.append((start, end))
            start = num
            end = num
    if start is not None:
        intervals.append((start, end))
    return intervals


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
