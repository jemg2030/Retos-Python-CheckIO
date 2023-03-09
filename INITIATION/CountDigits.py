'''
You need to count the number of digits in a given string.

Input: String.

Output: Integer.

Examples:
assert count_digits("hi") == 0
assert count_digits("who is 1st here") == 1
assert count_digits("my numbers is 2") == 1
assert (
    count_digits(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 8
)

----------
----------

Necesitas contar el número de dígitos de una cadena dada.

Entrada: Cadena.

Salida: Entero.

Ejemplo:
assert cuenta_digitos("hola") == 0
assert count_digits("quién es el primero aquí") == 1
assert cuenta_digitos("mi número es 2") == 1
assert (
    cuenta_dígitos(
        "Este cuadro es un óleo sobre lienzo pintado por la artista danesa Anna Petersen entre 1845 y 1910 año"
    )
    == 8
)
'''


def count_digits(text: str) -> int:
    # your code here
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count


print("Example:")
print(count_digits("hi"))

# These "asserts" are used for self-checking
assert count_digits("hi") == 0
assert count_digits("who is 1st here") == 1
assert count_digits("my numbers is 2") == 1
assert (
    count_digits(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 8
)
assert count_digits("5 plus 6 is") == 2
assert count_digits("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
