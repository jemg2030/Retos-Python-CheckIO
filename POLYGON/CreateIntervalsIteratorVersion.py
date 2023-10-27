"""
From a set of ints (which will be an iterator of the sorted list) you have to create a
list of closed intervals as tuples, so the intervals are covering all the values found in
the set. After that you have to create an iterator object which is linked to this list.

A closed interval includes its endpoints! The interval 1..5 , for example, includes each
value x that satisfies the condition 1 <= x <= 5 .

Values can only be in the same interval if the difference between a value and the next
smaller value in the set equals one, otherwise a new interval begins. Of course, the start
value of an interval is excluded from this rule.
A single value, that doesn't fit into an existing interval becomes the start- and endpoint of
a new interval.

Input: An iterator of the sorted list of ints.

Output: An iterator object linked to the list of tuples.

Examples:
list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
                                      (1, 5), (7, 8), (12, 12)]
list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
                                      (1, 8)]

----------
----------

A partir de un conjunto de ints (que será un iterador de la lista ordenada) tienes que
crear una lista de intervalos cerrados como tuplas, de forma que los intervalos cubran
todos los valores encontrados en el conjunto. Después tienes que crear un objeto iterador
que esté enlazado a esta lista.

¡Un intervalo cerrado incluye sus puntos finales! El intervalo 1..5 , por ejemplo, incluye
cada valor x que satisface la condición 1 <= x <= 5 .

Los valores sólo pueden estar en el mismo intervalo si la diferencia entre un valor y el
siguiente valor más pequeño del conjunto es igual a uno; de lo contrario, comienza un nuevo
intervalo. Por supuesto, el valor inicial de un intervalo queda excluido de esta regla.
Un único valor que no encaje en un intervalo existente se convierte en el punto inicial y
final de un nuevo intervalo.

Entrada: Un iterador de la lista ordenada de ints.

Salida: Un objeto iterador enlazado a la lista de tuplas.

Ejemplos:
list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
                                      (1, 5), (7, 8), (12, 12)]
list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
                                      (1, 8)]
"""


def create_intervals(data):
    """
    Create a list of intervals out of set of ints.
    """
    # your code here
    try:
        first, *data = sorted(data)
    except ValueError:
        return
    last = first
    for current in data:
        if last + 1 < current:
            yield first, last
            first = current
        last = current
    yield first, last


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    assert hasattr(res, "__iter__"), "your function should return the iterator object"
    assert hasattr(res, "__next__"), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
        (1, 8)
    ], "Second"
    print("Almost done! The only thing left to do is to Check it!")
