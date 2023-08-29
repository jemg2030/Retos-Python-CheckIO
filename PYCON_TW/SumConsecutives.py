"""
You are given a list that contains solely integers (positive and negative). Your job is to sum
only the numbers that are identical and consecutive.

Input: a list.

Output: an iterable.

Example:
sum_consecutives([1, 1, 1, 1]) == [4]
sum_consecutives([1, 1, 2, 2]) == [2, 4]

----------
----------

Se le da una lista que contiene únicamente números enteros (positivos y negativos). Su
trabajo consiste en sumar sólo los números que son idénticos y consecutivos.

Entrada: una lista.

Salida: un iterable.

Ejemplo:
suma_consecutivos([1, 1, 1, 1]) == [4]
suma_consecutivos([1, 1, 2, 2]) == [2, 4]
"""


def sum_consecutives(a):
    # your code here
    if not a:
        return []

    result = [a[0]]
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            result[-1] += a[i]
        else:
            result.append(a[i])

    return result


if __name__ == "__main__":
    print("Example:")
    print(list(sum_consecutives([1, 1, 1, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(sum_consecutives([1, 1, 1, 1])) == [4]
    assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
    assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
    assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
    assert list(sum_consecutives([1])) == [1]
    assert list(sum_consecutives([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
