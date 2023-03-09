'''
You should return a given string in reverse order.

Input: A string.

Output: A string.

Example:
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

----------
----------

Debe devolver una cadena dada en orden inverso.

Entrada: Una cadena.

Salida: Una cadena.

Ejemplo:
assert cadena_hacia_atrás("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"
'''


def backward_string(val: str) -> str:
    # your code here
    return val[::-1]


print("Example:")
print(backward_string("val"))

# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")
