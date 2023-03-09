'''
You have a non-negative integer. Try to find out how many digits it has.

Input: A non-negative integer.

Output: An integer.

Examples:
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

----------
----------

Tienes un número entero no negativo. Intenta averiguar cuántos dígitos tiene.

Entrada: Un entero no negativo.

Salida: Un número entero.

Ejemplo:
assert longitud_numero(10) == 2
assert longitud_numero(0) == 1
assert longitud_numero(4) == 1
assert longitud_numero(44) == 2
'''


def number_length(value: int) -> int:
    # your code here
    return len(str(value))


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")
