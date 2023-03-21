'''
Given an iterable of ints , create and return a new iterable whose first two elements are the same
as in items, after which each element equals the median element in the sorted list of the three elements
from the original list. Third element in sorted list is current position (position 2 and go on), first two
elements are going before the third element in the original list.

Wait...You don't know what the "median" is? Go check out the separate "Median" mission on CheckiO.

Input: Iterable of ints.

Output: Iterable of ints.

Example:
assert median_three([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 2, 3, 4, 5, 6]
assert median_three([1]) == [1]

The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of
Continuing Education by Ilkka Kokkarinen

----------
----------

Dado un iterable de ints , crear y devolver un nuevo iterable cuyos dos primeros elementos son los
mismos que en items, después de lo cual cada elemento es igual al elemento mediano en la lista
ordenada de los tres elementos de la lista original. El tercer elemento de la lista ordenada es la
posición actual (posición 2 y siguientes), los dos primeros elementos van antes del tercer elemento
de la lista original.

Espera... ¿No sabes lo que es la "mediana"? Vaya a registrar la misión "Mediana" por separado en CheckiO.

Entrada: Iterable de ints.

Salida: Iterable de ints.

Ejemplo:
assert mediana_tres([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 2, 3, 4, 5, 6]
assert mediana_tres([1]) == [1]

La misión fue tomada de Python CCPS 109 Otoño 2018. Está siendo impartido para la escuela de
educación continua Ryerson Chang por Ilkka Kokkarinen
'''


from typing import Iterable
from statistics import median


def median_three(els: Iterable[int]) -> Iterable[int]:
    # your code here
    output = els[:2]  # first two elements are the same as in els
    for i in range(2, len(els)):
        sublist = els[i - 2:i + 1]  # sublist of three elements
        sublist.sort()  # sort the sublist
        output.append(median(sublist))  # take the median and add to output
    return output


print('Example:')
print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

assert median_three([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 2, 3, 4, 5, 6]
assert median_three([1]) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
