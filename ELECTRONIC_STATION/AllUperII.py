'''
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in
it - function should return False.

Input: A string.

Output: A boolean.

Examples:
# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False

Precondition: a-z, A-Z, 1-9 and spaces.

----------
----------

Registra si una cadena dada tiene todos los símbolos en mayúsculas. Si la cadena está vacía o no
contiene ninguna letra, la función devolverá False.

Entrada: Una cadena.

Salida: Un booleano.

Ejemplos:
# Estos "asserts" se utilizan para el autocontrol
assert is_all_upper("todo superior") == True
assert is_all_upper("todo inferior") == False
assert is_all_upper("todo superior e inferior") == False
assert is_all_upper("") == False

Condición previa: a-z, A-Z, 1-9 y espacios.
'''


# Taken from mission All Upper I

def is_all_upper(text: str) -> bool:
    # your code here
    return text.isupper() and any(c.isalpha() for c in text)


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
