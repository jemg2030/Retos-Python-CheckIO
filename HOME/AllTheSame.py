'''
In this mission you should check if all elements in the given list are equal.

Input: List.
Output: Bool.
Example:
1 all_the_same([1, 1, 1]) == True
2 all_the_same([1, 2, 1]) == False
3 all_the_same(['a', 'a', 'a']) == True
4 all_the_same([]) == True
The idea for this mission was found on Python Tricks series by Dan Bader
Precondition: all elements of the input list are hashable

En esta misión, debe verificar si todos los elementos en la lista dada son iguales.

Entrada: Lista.
Salida: Bool.
Ejemplo:
1 all_the_same ([1, 1, 1]) == Verdadero
2 all_the_same ([1, 2, 1]) == Falso
3 all_the_same (['a', 'a', 'a']) == Verdadero
4 all_the_same ([]) == True
La idea de esta misión se encontró en la serie Python Tricks de Dan Bader.
Precondición: todos los elementos de la lista de entrada son hashable

https://dbader.org/
https://github.com/oduvan/checkio-mission-all-the-same
'''

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if bool(not elements):
        return True
    else:
        position = 0
        element = elements[position]
        if elements.count(element) == len(elements):
            return True
        else:
            return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    assert all_the_same([1, "a", 1]) == False
    assert all_the_same([1, "a", 1]) == False
    assert all_the_same([600000]) == True
    assert all_the_same([10000, 99999]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")