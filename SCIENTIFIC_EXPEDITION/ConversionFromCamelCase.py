'''
Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName")
into the Python format ("my_function_name") where all chars are in lowercase and all words are
concatenated with an intervening underscore symbol "_".

Input: A function name as a CamelCase string.

Output: The same string, but in under_score.

Example:

assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"
1
2
How it is used: To apply function names in the style in which they are adopted in a specific
language (Python, JavaScript, etc.).

Precondition:
0 < len(string) <= 100
Input data won't contain any numbers.

----------
----------

Tu misión es convertir el nombre de una función (una cadena) de CamelCase ("MiNombreDeFunción")
al formato Python ("mi_nombre_de_función") donde todos los caracteres están en minúsculas y todas
las palabras están concatenadas con un guión bajo intercalado "_".

Entrada: Un nombre de función como cadena CamelCase.

Salida: La misma cadena, pero con guión bajo.

Ejemplo:
assert from_camel_case("NombreDeMiFunción") == "nombre_de_mi_función"
assert from_camel_case("IPhone") == "i_phone"

Cómo se utiliza: Para aplicar nombres de función en el estilo en que se adoptan en un lenguaje
específico (Python, JavaScript, etc.).

Condición previa:
0 < len(cadena) <= 100
Los datos de entrada no contendrán ningún número.
'''


def from_camel_case(name: str) -> str:
    # replace this for solution
    converted_string = ""
    for i, char in enumerate(name):
        if char.isupper():
            if i > 0:
                converted_string += "_" + char.lower()
            else:
                converted_string += char.lower()
        else:
            converted_string += char
    return converted_string


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
