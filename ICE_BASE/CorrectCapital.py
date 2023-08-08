"""
You are given a word in which letters can be in different cases. Your task is to check whether
the case was used correctly in the line. If everything is correct - return True, if there are errors
- return False.

Examples of the correct use of cases:

All characters in the string are in uppercase. For example, "CHECKIO";
None of the characters are in uppercase. For example, "checkio";
Only the first character is in uppercase. For example, "Checkio".
Input: String (str).

Output: Logic value (bool).

Examples:
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

----------
----------

Se le da una palabra en la que las letras pueden estar en distintos casos. Su tarea consiste
en comprobar si las mayúsculas y minúsculas se han utilizado correctamente en la línea. Si todo
es correcto - devuelva Verdadero, si hay errores - devuelva Falso.

Ejemplos del uso correcto de mayúsculas y minúsculas:

Todos los caracteres de la cadena están en mayúsculas. Por ejemplo, "CHECKIO";
Ninguno de los caracteres está en mayúsculas. Por ejemplo, "checkio";
Sólo el primer carácter está en mayúsculas. Por ejemplo, "Checkio".
Entrada: Cadena (str).

Salida: Valor lógico (bool).

Ejemplos:
assert capital_correcto("Checkio") == True
assert correct_capital("CheCkio") == False
assert capital_correcto("CHECKIO") == True
"""


def correct_capital(line: str) -> bool:
    # your code here
    # Check if all characters are uppercase
    if line.isupper():
        return True
    # Check if all characters are lowercase
    elif line.islower():
        return True
    # Check if only the first character is uppercase
    elif line[0].isupper() and line[1:].islower():
        return True
    else:
        return False


print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
