"""
You are given a sequence of intervals, as iterator of the tuples of ints.
It is your task to minimize the number of intervals by merging those that intersect or by
removing intervals fitting into another one. After that you have to create an iterator object
which is linked to this list.

Since the range of values for the intervals is restricted to integers, you must also merge those
intervals between which no value can be found.

An example:
Let's say you've got these 5 intervals: 1..6, 3..5, 7..10, 9..12 and 14..16 .

1..6 and 3..5
3..5 is a part of 1..6 , so 3..5 must disappear.
1..6 and 7..10
Even though the intervals don't intersect, there isn't an int type value between them, so they
have to be merged with the new interval 1..10 .
1..10 and 9..12
These intervals do intersect, because 9 < 10 , so they have to be merged with the new interval 1..12 .
1..12 and 14..16
These two intervals don't intersect, so they mustn't be merged.
So the intervals to be returned are:
1..12 and 14..16
Input: A sequence of intervals as an iterator of the tuples of 2 ints.

Output: The iterator object linked to the list of merged intervals.

Examples:
list(merge_intervals(iter([(1, 4), (2, 6), (8, 10), (12, 19)]))) == [(1, 6), (8, 10), (12, 19)]
list(merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))) == [(1, 12)]
list(merge_intervals(iter([(1, 5), (6, 10), (10, 15), (17, 20)]))) == [(1, 15), (17, 20)]

----------
----------

Se le da una secuencia de intervalos, como iterador de las tuplas de ints.
Tu tarea es minimizar el número de intervalos fusionando los que se cruzan o eliminando los
intervalos que encajan en otro. Después tienes que crear un objeto iterador que esté enlazado
a esta lista.

Como el rango de valores para los intervalos está restringido a enteros, también debes fusionar
aquellos intervalos entre los que no se puede encontrar ningún valor.

Un ejemplo:
Supongamos que tienes estos 5 intervalos: 1..6, 3..5, 7..10, 9..12 y 14..16 .

1..6 y 3..5
3..5 es una parte de 1..6 , por lo que 3..5 debe desaparecer.
1..6 y 7..10
Aunque los intervalos no se cruzan, no hay ningún valor de tipo int entre ellos, por lo
que deben fusionarse con el nuevo intervalo 1..10 .
1..10 y 9..12
Estos intervalos sí se intersecan, porque 9 < 10 , por lo que deben combinarse con el
nuevo intervalo 1..12 .
1..12 y 14..16
Estos dos intervalos no se cruzan, por lo que no deben fusionarse.
Así que los intervalos a devolver son:
1..12 y 14..16
Entrada: Una secuencia de intervalos como un iterador de las tuplas de 2 ints.

Salida: El objeto iterador enlazado a la lista de intervalos fusionados.

Ejemplos:
list(fusionar_intervalos(iter([(1, 4), (2, 6), (8, 10), (12, 19)]))) == [(1, 6), (8, 10), (12, 19)]
list(merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))) == [(1, 12)]
list(merge_intervals(iter([(1, 5), (6, 10), (10, 15), (17, 20)]))) == [(1, 15), (17, 20)]
"""


def merge_intervals(intervals):
    """
    Merge overlapped intervals.
    """
    # Your code here
    it = iter(intervals)
    b: None
    a, b = next(it, (None, None))
    if a is not None:
        for c, d in it:
            if c - b >= 2:
                yield a, b
                a, b = c, d
            elif b < d:
                b = d
        yield a, b


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    res = merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))
    assert hasattr(res, "__iter__"), "your function should return the iterator object"
    assert hasattr(res, "__next__"), "your function should return the iterator object"

    assert list(merge_intervals(iter([(1, 4), (2, 6), (8, 10), (12, 19)]))) == [
        (1, 6),
        (8, 10),
        (12, 19),
    ], "First"
    assert list(merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))) == [(1, 12)], "Second"
    assert list(merge_intervals(iter([(1, 5), (6, 10), (10, 15), (17, 20)]))) == [
        (1, 15),
        (17, 20),
    ], "Third"
    print("Done! Go ahead and Check IT")
