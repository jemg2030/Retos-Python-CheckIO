'''
Determine whether the list of elements is ascending such that each of its elements is strictly larger than
(and not merely equal to) the preceding element. Empty list consider as ascending.

Input: A list with integers.

Output: Boolean.

Examples:
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True

The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing
Education by Ilkka Kokkarinen

----------
----------

Determinar si la lista de elementos es ascendente tal que cada uno de sus elementos es estrictamente
mayor que (y no meramente igual a) el elemento precedente. La lista vacía se considera ascendente.

Entrada: Una lista con enteros.

Salida: Booleana.

Ejemplos:
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True

La misión fue tomada de Python CCPS 109 Otoño 2018. Se imparte para la escuela de educación continua
Ryerson Chang por Ilkka Kokkarinen
'''


def is_ascending(items: list[int]) -> bool:
    # your code here
    for i in range(1, len(items)):
        if items[i] <= items[i - 1]:
            return False

    return True


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

# These "asserts" are used for self-checking
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
assert is_ascending([1, 3, 3, 5]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
