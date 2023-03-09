'''
Check if the given number is even or not. Your function should return True if the number is even, and
False if the number is odd.

Input: An integer.

Output: Bool.

Example:
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

How it’s used: (math is used everywhere)

Precondition: given int should be between -1000 and 1000

----------
----------

Registra si el número dado es par o no. Su función debe devolver True si el número es par, y False si
el número es impar.

Entrada: Un número entero.

Salida: Bool.

Ejemplo:
assert es_par(2) == Verdadero
assert es_par(5) == Falso
assert es_par(0) == Verdadero

Cómo se usa: (las matemáticas se usan en todas partes)

Precondición: el int dado debe estar entre -1000 y 1000
'''


def is_even(num: int) -> bool:
    # your code here
    return num % 2 == 0


print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
