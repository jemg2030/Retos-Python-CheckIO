'''
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in
it - function should return True.

Input: A string.

Output: a boolean.

Example:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

Precondition: a-z, A-Z, 1-9 and spaces

----------
----------

Registra si una cadena dada tiene todos los símbolos en mayúsculas. Si la cadena está vacía o no contiene
ninguna letra, la función devolverá True.

Entrada: Una cadena.

Salida: un booleano.

Ejemplo:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

Precondición: a-z, A-Z, 1-9 y espacios

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
'''


def is_all_upper(text: str) -> bool:
    # your code here
    return text.isupper() or not any(c.isalpha() for c in text)


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
