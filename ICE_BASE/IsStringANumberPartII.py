'''
You are given a string. Your function should return True if the string is a valid number
(contains only digits and "+-." at proper places), otherwise - False. Look at the mask:

[+- ][zero or more digits][.][zero or more digits]
Of course, not all parts are necessary (but at least one digit part is!). For example,
"+10." or "-.55" are valid numbers, where part equal 0 is omitted.

Input: A string.

Output: A boolean.

Examples:
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True

----------
----------

Se le da una cadena. Su función debe devolver True si la cadena es un número válido
(sólo contiene dígitos y "+-." en los lugares adecuados), en caso contrario - False.
Mira la máscara:

[+- ][cero o más dígitos][.][cero o más dígitos]
Por supuesto, no todas las partes son necesarias (¡pero al menos una parte de dígitos sí
lo es!). Por ejemplo, "+10." o "-.55" son números válidos, en los que se omite la parte igual a 0.

Entrada: Una cadena.

Salida: Un booleano.

Ejemplo:
assert es_número("34") == True
assert es_número("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
'''


def is_number(val: str) -> bool:
    # your code here
    # Remove leading and trailing whitespaces
    s = val.strip()

    # Check if the string is empty
    if not s:
        return False

    # Check if the string starts with '+' or '-', contains two consecutive signs, or starts with a decimal point
    if s[0] not in '+-.' and not s[0].isdigit():
        return False
    for i in range(1, len(s)):
        if s[i] not in '+-.0123456789' or (s[i] in '+-' and s[i - 1] not in 'eE'):
            return False

    # Check if the string contains at least one digit
    if not any(char.isdigit() for char in s):
        return False

    return True


print("Example:")
print(is_number("10"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
assert is_number("1OOO") == False
assert is_number("1.") == True
assert is_number("+.l") == False
assert is_number("++1+.2-") == False
assert is_number("3e4") == False
assert is_number('--5') == False
assert is_number('.1') == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
