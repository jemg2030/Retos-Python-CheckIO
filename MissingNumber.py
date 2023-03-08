'''
You are given a list of integers, which are elements of arithmetic progression - the difference between
the consecutive elements is constant. But this list is unsorted and one element is missing...good luck!

Input: List of integers.

Output: Integer.

Examples:
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

Preconditions:
length of sequence > 2;
missing element is always between two elements in sequence.

---------
---------

Se le da una lista de números enteros, que son elementos de progresión aritmética - la diferencia entre
los elementos consecutivos es constante. Pero esta lista no está ordenada y falta un elemento... ¡buena suerte!

Entrada: Lista de enteros.

Salida: Número entero.

Ejemplo:
assert numero_faltante([1, 4, 2, 5]) == 3
assert número_faltante([2, 6, 8]) == 4

Precondiciones:
longitud de la secuencia > 2;
el elemento que falta está siempre entre dos elementos de la secuencia.
'''


def missing_number(items: list[int]) -> int:
    # your code here
    items.sort()
    diff = items[1] - items[0]
    for i in range(1, len(items)):
        if items[i] - items[i - 1] != diff:
            return items[i] - diff
    return 0


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4
assert missing_number([5, 25, 30, 20, 15]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")
