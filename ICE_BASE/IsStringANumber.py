'''
You are given a string. Your function should return True if the string is a valid number (contains
digits only), otherwise - False. Look at the example.

Input: A string.

Output: A boolean.

Examples:
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False

How it’s used: For checking string values that must contain only digits.

Precondition: The text contains only letters, digits and whitespace.

----------
----------

Se le da una cadena. Su función debe devolver True si la cadena es un número válido (sólo
contiene dígitos), en caso contrario - False. Mira el ejemplo.

Entrada: Una cadena.

Salida: Un booleano.

Ejemplo
assert es_número("34") == True
assert es_número("df") == False
assert es_número("") == False
assert es_número("a5") == False

Cómo se utiliza: Para registrar valores de cadena que deben contener sólo dígitos.

Condición previa: El texto sólo contiene letras, dígitos y espacios en blanco.
'''


def is_number(val: str) -> bool:
    # your code here
    return val.isdigit()


print("Example:")
print(is_number("34"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False
assert is_number("ITS A NUMBER") == False
assert is_number("5a") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
